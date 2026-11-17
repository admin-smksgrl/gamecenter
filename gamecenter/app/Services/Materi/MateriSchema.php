<?php

namespace App\Services\Materi;

use App\Enums\Difficulty;
use App\Enums\MaterialType;
use App\Enums\QuestionType;

/**
 * Pemeriksa skema berkas materi SMA/SMK.
 *
 * Dipisah dari importer supaya bisa diuji sendiri dan supaya importer
 * tidak menulis apa pun bila ada satu saja masalah.
 */
class MateriSchema
{
    public const VERSION = 1;

    public function __construct(
        private readonly BlockSchema $blocks = new BlockSchema,
    ) {}

    /**
     * Tipe soal yang kuncinya disimpan di kolom `options`.
     *
     * @var array<int, string>
     */
    private const PAYLOAD_TYPES = [
        'drag_drop',
        'matching',
        'puzzle',
    ];

    /**
     * @param  array<string, mixed>  $payload
     * @return array<int, string> daftar masalah; kosong berarti valid
     */
    public function problems(array $payload): array
    {
        $problems = [];

        foreach (['level', 'class', 'subject'] as $key) {
            if (! $this->filledString($payload[$key] ?? null)) {
                $problems[] = "{$key} wajib diisi";
            }
        }

        $version = $payload['schema_version'] ?? self::VERSION;
        if ((int) $version !== self::VERSION) {
            $problems[] = "schema_version harus " . self::VERSION . " (ditemukan {$version})";
        }

        $chapters = $payload['chapters'] ?? null;

        if (! is_array($chapters) || $chapters === []) {
            return [...$problems, 'chapters harus berisi minimal satu chapter'];
        }

        $seenSlugs = [];

        foreach (array_values($chapters) as $i => $chapter) {
            $path = "chapters[{$i}]";

            if (! is_array($chapter)) {
                $problems[] = "{$path} harus berupa objek";
                continue;
            }

            $problems = [...$problems, ...$this->chapterProblems($chapter, $path)];

            $slug = $this->slug((string) ($chapter['title'] ?? ''));
            if ($slug !== '' && isset($seenSlugs[$slug])) {
                $problems[] = "{$path} slug \"{$slug}\" dobel dengan chapter lain di berkas yang sama";
            }
            $seenSlugs[$slug] = true;
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $chapter
     * @return array<int, string>
     */
    private function chapterProblems(array $chapter, string $path): array
    {
        $problems = [];

        if (! $this->filledString($chapter['title'] ?? null)) {
            $problems[] = "{$path}.title wajib diisi";
        }

        $objectives = $chapter['learning_objectives'] ?? null;

        if (! is_array($objectives) || $objectives === []) {
            // Plan §9: tujuan pembelajaran harus berasal dari modul ajar/CP.
            $problems[] = "{$path}.learning_objectives wajib berisi minimal satu tujuan";
        } else {
            foreach ($objectives as $j => $objective) {
                if (! $this->filledString($objective)) {
                    $problems[] = "{$path}.learning_objectives[{$j}] harus berupa teks";
                }
            }
        }

        $minutes = $chapter['estimated_minutes'] ?? null;
        if ($minutes !== null && (! is_int($minutes) || $minutes < 0)) {
            $problems[] = "{$path}.estimated_minutes harus bilangan bulat >= 0";
        }

        $materials = $chapter['materials'] ?? [];

        if (! is_array($materials)) {
            $problems[] = "{$path}.materials harus berupa array";
        } else {
            foreach (array_values($materials) as $j => $material) {
                $problems = [...$problems, ...$this->materialProblems($material, "{$path}.materials[{$j}]")];
            }
        }

        $assessments = $chapter['assessments'] ?? [];

        if (! is_array($assessments) || $assessments === []) {
            $problems[] = "{$path}.assessments harus berisi minimal satu asesmen";
        } else {
            $seenDifficulties = [];

            foreach (array_values($assessments) as $j => $assessment) {
                $assessmentPath = "{$path}.assessments[{$j}]";
                $problems = [...$problems, ...$this->assessmentProblems($assessment, $assessmentPath)];

                if (is_array($assessment)) {
                    $difficulty = (string) ($assessment['difficulty'] ?? '');
                    if (isset($seenDifficulties[$difficulty])) {
                        $problems[] = "{$assessmentPath}.difficulty \"{$difficulty}\" dobel dalam satu chapter";
                    }
                    $seenDifficulties[$difficulty] = true;
                }
            }
        }

        return $problems;
    }

    /**
     * @return array<int, string>
     */
    private function materialProblems(mixed $material, string $path): array
    {
        if (! is_array($material)) {
            return ["{$path} harus berupa objek"];
        }

        $problems = [];

        if (! $this->filledString($material['title'] ?? null)) {
            $problems[] = "{$path}.title wajib diisi";
        }

        $type = (string) ($material['type'] ?? 'text');
        if (! in_array($type, MaterialType::values(), true)) {
            $problems[] = "{$path}.type \"{$type}\" tidak dikenal (pilihan: " . implode(', ', MaterialType::values()) . ')';
        }

        if (! $this->filledString($material['content'] ?? null)) {
            $problems[] = "{$path}.content wajib diisi";
        }

        // Blok interaktif (plan §3.2) diperiksa terpisah agar aturannya bisa
        // diuji sendiri; daftar kosong berarti tidak ada blok.
        $problems = [...$problems, ...$this->blocks->problems($material['blocks'] ?? null, $path)];

        return $problems;
    }

    /**
     * @return array<int, string>
     */
    private function assessmentProblems(mixed $assessment, string $path): array
    {
        if (! is_array($assessment)) {
            return ["{$path} harus berupa objek"];
        }

        $problems = [];

        $difficulty = (string) ($assessment['difficulty'] ?? '');
        if (! in_array($difficulty, Difficulty::values(), true)) {
            $problems[] = "{$path}.difficulty \"{$difficulty}\" tidak dikenal (pilihan: " . implode(', ', Difficulty::values()) . ')';
        }

        $passing = $assessment['passing_score'] ?? null;
        if ($passing !== null && (! is_int($passing) || $passing < 0 || $passing > 100)) {
            $problems[] = "{$path}.passing_score harus bilangan bulat 0..100";
        }

        $questions = $assessment['questions'] ?? null;

        if (! is_array($questions) || $questions === []) {
            return [...$problems, "{$path}.questions harus berisi minimal satu soal"];
        }

        foreach (array_values($questions) as $k => $question) {
            $problems = [...$problems, ...$this->questionProblems($question, "{$path}.questions[{$k}]", $difficulty)];
        }

        return $problems;
    }

    /**
     * @return array<int, string>
     */
    private function questionProblems(mixed $question, string $path, string $difficulty): array
    {
        if (! is_array($question)) {
            return ["{$path} harus berupa objek"];
        }

        $problems = [];

        $type = (string) ($question['type'] ?? '');

        if (! in_array($type, QuestionType::values(), true)) {
            return ["{$path}.type \"{$type}\" tidak dikenal (pilihan: " . implode(', ', QuestionType::values()) . ')'];
        }

        if (! $this->filledString($question['question'] ?? null)) {
            $problems[] = "{$path}.question wajib diisi";
        }

        // Plan §9 butir 4: setiap soal wajib punya penjelasan.
        if (! $this->filledString($question['explanation'] ?? null)) {
            $problems[] = "{$path}.explanation wajib diisi";
        }

        // Plan §4.2 butir 4: hint hanya untuk easy & medium.
        if ($difficulty === 'hard' && $this->filledString($question['hint'] ?? null)) {
            $problems[] = "{$path}.hint tidak boleh diisi untuk soal sulit";
        }

        $problems = [
            ...$problems,
            ...$this->answerProblems($type, $question, $path),
        ];

        return $problems;
    }

    /**
     * Memeriksa bentuk kunci jawaban sesuai tipe soal (plan §4.1).
     *
     * @param  array<string, mixed>  $question
     * @return array<int, string>
     */
    private function answerProblems(string $type, array $question, string $path): array
    {
        $options = $question['options'] ?? null;
        $correct = $question['correct'] ?? null;

        switch ($type) {
            case 'multiple_choice':
                return $this->choiceProblems($options, $path, exactlyOne: true);

            case 'multiple_answer':
                return $this->choiceProblems($options, $path, exactlyOne: false);

            case 'drag_drop':
            case 'matching':
            case 'puzzle':
                $problems = [];

                if (! is_array($options) || $options === []) {
                    $problems[] = "{$path}.options wajib diisi untuk tipe {$type}";
                }

                if (! is_array($correct) || $correct === []) {
                    $problems[] = "{$path}.correct wajib diisi untuk tipe {$type}";
                }

                return $problems;

            case 'simulation':
                $problems = [];

                if (! is_array($correct) || $correct === []) {
                    $problems[] = "{$path}.correct wajib diisi untuk tipe simulation";
                }

                return $problems;

            case 'essay':
                if (! is_array($question['rubric'] ?? null)) {
                    return ["{$path}.rubric wajib diisi untuk soal uraian"];
                }

                return [];

            default:
                return [];
        }
    }

    /**
     * @return array<int, string>
     */
    private function choiceProblems(mixed $options, string $path, bool $exactlyOne): array
    {
        if (! is_array($options) || count($options) < 2) {
            return ["{$path}.options harus berisi minimal dua pilihan"];
        }

        $problems = [];
        $correct = 0;

        foreach (array_values($options) as $i => $option) {
            if (! is_array($option) || ! $this->filledString($option['text'] ?? null)) {
                $problems[] = "{$path}.options[{$i}].text wajib diisi";
                continue;
            }

            if (($option['correct'] ?? false) === true) {
                $correct++;
            }
        }

        if ($exactlyOne && $correct !== 1) {
            $problems[] = "{$path} harus punya tepat satu opsi benar (ditemukan {$correct})";
        }

        if (! $exactlyOne && $correct < 2) {
            $problems[] = "{$path} harus punya minimal dua opsi benar (ditemukan {$correct})";
        }

        return $problems;
    }

    private function filledString(mixed $value): bool
    {
        return is_string($value) && trim($value) !== '';
    }

    /**
     * Slug dipakai sebagai kunci idempotensi chapter.
     */
    public function slug(string $title): string
    {
        $slug = strtolower(trim($title));
        $slug = preg_replace('/[^a-z0-9\s-]/', '', $slug) ?? '';
        $slug = preg_replace('/[\s-]+/', '-', $slug) ?? '';

        return trim($slug, '-');
    }
}
