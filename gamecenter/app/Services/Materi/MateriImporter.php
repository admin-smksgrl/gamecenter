<?php

namespace App\Services\Materi;

use App\Enums\Difficulty;
use App\Enums\QuestionType;
use App\Models\Assessment;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\QuestionOption;
use App\Models\Subject;
use Illuminate\Support\Facades\DB;

/**
 * Mengimpor berkas JSON materi SMA/SMK ke database.
 *
 * Sifat penting: **idempoten**. Menjalankan impor yang sama dua kali tidak
 * menambah baris apa pun; ia hanya memperbarui baris yang sudah ada. Ini
 * yang membuat impor aman diulang setelah materi diperbaiki.
 *
 * Kunci idempotensi:
 *   chapter     → (subject_id, slug)
 *   materi      → (chapter_id, order)
 *   asesmen     → (chapter_id, difficulty)  [sudah unik di skema]
 *   soal        → (assessment_id, order)
 *   opsi        → dihapus lalu dibuat ulang per soal
 */
class MateriImporter
{
    public function __construct(
        private readonly MateriSchema $schema = new MateriSchema,
    ) {}

    /**
     * @param  array<string, mixed>  $payload
     *
     * @throws MateriValidationException
     */
    public function import(array $payload, ?string $sourceFile = null): MateriImportResult
    {
        $problems = $this->schema->problems($payload);

        if ($problems !== []) {
            throw MateriValidationException::inFile($sourceFile ?? 'materi', $problems);
        }

        $subject = $this->resolveSubject($payload);

        if ($subject === null) {
            $label = sprintf(
                '%s / %s / %s',
                $payload['level'],
                $payload['class'],
                $payload['subject'],
            );

            throw MateriValidationException::plain(
                "Mapel tidak ditemukan untuk {$label}. Periksa slug level/class/subject.",
            );
        }

        $result = new MateriImportResult;

        DB::transaction(function () use ($payload, $subject, $result): void {
            foreach (array_values($payload['chapters']) as $index => $chapterData) {
                $this->importChapter($subject, $chapterData, $index + 1, $result);
            }
        });

        return $result;
    }

    /**
     * @param  array<string, mixed>  $payload
     */
    private function resolveSubject(array $payload): ?Subject
    {
        $level = (string) $payload['level'];
        $class = (string) $payload['class'];
        $subject = (string) $payload['subject'];

        return Subject::query()
            ->where('slug', $subject)
            ->whereHas('classRoom', fn ($query) => $query
                ->where('slug', $class)
                ->whereHas('educationLevel', fn ($levelQuery) => $levelQuery->where('slug', $level)))
            ->first();
    }

    /**
     * @param  array<string, mixed>  $data
     */
    private function importChapter(Subject $subject, array $data, int $order, MateriImportResult $result): void
    {
        $slug = (string) ($data['slug'] ?? $this->schema->slug((string) $data['title']));

        $chapter = Chapter::query()->firstOrNew([
            'subject_id' => $subject->id,
            'slug' => $slug,
        ]);

        $isNew = ! $chapter->exists;

        $chapter->fill([
            'code' => $data['code'] ?? null,
            'title' => $data['title'],
            'description' => $data['description'] ?? null,
            'learning_objectives' => array_values($data['learning_objectives']),
            'estimated_minutes' => (int) ($data['estimated_minutes'] ?? 0),
            'order' => (int) ($data['order'] ?? $order),
            'is_active' => true,
        ]);

        $chapter->save();

        $isNew ? $result->chaptersCreated++ : $result->chaptersUpdated++;

        $this->importMaterials($chapter, $data['materials'] ?? [], $result);
        $this->importAssessments($chapter, $data['assessments'], $result);
    }

    /**
     * @param  array<int, array<string, mixed>>  $materials
     */
    private function importMaterials(Chapter $chapter, array $materials, MateriImportResult $result): void
    {
        foreach (array_values($materials) as $index => $material) {
            $existing = $chapter->materials()->where('order', $index + 1)->first();

            $chapter->materials()->updateOrCreate(
                ['order' => $index + 1],
                [
                    'type' => (string) ($material['type'] ?? 'text'),
                    'title' => $material['title'],
                    'content' => $material['content'],
                    'blocks' => $material['blocks'] ?? null,
                    'media_url' => $material['media_url'] ?? null,
                    'media_type' => $material['media_type'] ?? null,
                    'duration' => (int) ($material['duration'] ?? 0),
                    'source_reference' => $material['source_reference'] ?? null,
                    'is_active' => true,
                ],
            );

            $existing === null ? $result->materialsCreated++ : $result->materialsUpdated++;
        }

        // Materi yang tidak lagi ada di berkas sumber dinonaktifkan, bukan
        // dihapus, supaya progres siswa lama tidak ikut terhapus.
        $chapter->materials()
            ->where('order', '>', count($materials))
            ->update(['is_active' => false]);
    }

    /**
     * @param  array<int, array<string, mixed>>  $assessments
     */
    private function importAssessments(Chapter $chapter, array $assessments, MateriImportResult $result): void
    {
        foreach (array_values($assessments) as $index => $data) {
            $difficulty = Difficulty::from((string) $data['difficulty']);

            $assessment = $chapter->assessments()->firstOrNew([
                'difficulty' => $difficulty->value,
            ]);

            $isNew = ! $assessment->exists;

            $assessment->fill([
                'title' => $data['title'] ?? "{$chapter->title} — {$difficulty->label()}",
                'duration' => (int) ($data['duration'] ?? $this->defaultDuration($data, $difficulty)),
                'passing_score' => (int) ($data['passing_score'] ?? 70),
                'order' => (int) ($data['order'] ?? $index + 1),
                'is_active' => true,
            ]);

            $assessment->save();

            $isNew ? $result->assessmentsCreated++ : $result->assessmentsUpdated++;

            $this->importQuestions($assessment, $data['questions'], $difficulty, $result);

            $assessment->questions()
                ->where('order', '>', count($data['questions']))
                ->delete();
        }
    }

    /**
     * @param  array<int, array<string, mixed>>  $questions
     */
    private function importQuestions(
        Assessment $assessment,
        array $questions,
        Difficulty $difficulty,
        MateriImportResult $result,
    ): void {
        foreach (array_values($questions) as $index => $data) {
            $order = $index + 1;
            $type = QuestionType::from((string) $data['type']);

            $question = Question::query()->firstOrNew([
                'assessment_id' => $assessment->id,
                'order' => $order,
            ]);

            $isNew = ! $question->exists;

            $payload = $this->payloadFor($type, $data);

            $question->fill([
                'type' => $type->value,
                'question' => $data['question'],
                'media_url' => $data['media_url'] ?? null,
                'options' => $payload,
                'correct_answer' => $this->correctAnswerFor($type, $data),
                'rubric' => $data['rubric'] ?? null,
                'explanation' => $data['explanation'],
                'hint' => $difficulty === Difficulty::Hard ? null : ($data['hint'] ?? null),
                'points' => (int) ($data['points'] ?? $difficulty->pointsPerQuestion()),
                'time_limit' => (int) ($data['time_limit'] ?? $difficulty->timePerQuestion()),
                'ai_assisted' => (bool) ($data['ai_assisted'] ?? false),
                'order' => $order,
            ]);

            $question->save();

            $isNew ? $result->questionsCreated++ : $result->questionsUpdated++;

            $this->importOptions($question, $type, $data, $result);
        }
    }

    /**
     * @param  array<string, mixed>  $data
     */
    private function importOptions(
        Question $question,
        QuestionType $type,
        array $data,
        MateriImportResult $result,
    ): void {
        $question->questionOptions()->delete();

        if (! in_array($type, [QuestionType::MultipleChoice, QuestionType::MultipleAnswer], true)) {
            return;
        }

        foreach (array_values($data['options'] ?? []) as $index => $option) {
            QuestionOption::create([
                'question_id' => $question->id,
                'label' => chr(65 + $index),
                'text' => $option['text'],
                'media_url' => $option['media_url'] ?? null,
                'is_correct' => (bool) ($option['correct'] ?? false),
                'order' => $index + 1,
            ]);

            $result->optionsCreated++;
        }
    }

    /**
     * Kolom `options` hanya dipakai sebagai payload untuk tipe non-pilihan.
     *
     * @param  array<string, mixed>  $data
     * @return array<string, mixed>|null
     */
    private function payloadFor(QuestionType $type, array $data): ?array
    {
        if (! isset($data['options']) || ! is_array($data['options'])) {
            return null;
        }

        return match ($type) {
            QuestionType::MultipleChoice, QuestionType::MultipleAnswer => null,
            default => $data['options'],
        };
    }

    /**
     * Bentuk kunci jawaban mengikuti plan §4.1.
     *
     * @param  array<string, mixed>  $data
     * @return array<string, mixed>
     */
    private function correctAnswerFor(QuestionType $type, array $data): array
    {
        if (isset($data['correct']) && is_array($data['correct'])) {
            return $data['correct'];
        }

        $correctTexts = collect($data['options'] ?? [])
            ->filter(fn ($option) => is_array($option) && ($option['correct'] ?? false) === true)
            ->pluck('text')
            ->values()
            ->all();

        return match ($type) {
            QuestionType::MultipleChoice => ['text' => $correctTexts[0] ?? null],
            QuestionType::MultipleAnswer => ['texts' => $correctTexts],
            default => [],
        };
    }

    /**
     * Bila `duration` tidak ditulis, hitung dari jumlah soal × waktu per soal.
     *
     * @param  array<string, mixed>  $data
     */
    private function defaultDuration(array $data, Difficulty $difficulty): int
    {
        $count = is_array($data['questions'] ?? null) ? count($data['questions']) : 0;

        return max(60, $count * $difficulty->timePerQuestion());
    }
}
