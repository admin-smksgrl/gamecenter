<?php

namespace App\Services;

use App\Enums\Difficulty;
use App\Enums\ProgressStatus;
use App\Enums\QuestionType;
use App\Enums\SyncStatus;
use App\Models\Assessment;
use App\Models\Chapter;
use App\Models\GameSession;
use App\Models\LearningMaterial;
use App\Models\MaterialBlockResponse;
use App\Models\Question;
use App\Models\SessionAnswer;
use App\Models\SyncQueue;
use App\Models\User;
use App\Models\UserProgress;
use App\Services\Materi\BlockSchema;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;
use Illuminate\Validation\Rule;
use Illuminate\Validation\ValidationException;
use Throwable;

/**
 * Menyimpan batch antrean offline yang dikirim perangkat.
 *
 * Server hanya memvalidasi & menyimpan: jawaban pilihan ganda dinilai ulang
 * di server, tipe interaktif (drag & drop, menjodohkan, puzzle, simulasi)
 * menerima penilaian client, sedangkan uraian disimpan tanpa skor sampai
 * penilaian AI/guru tersedia.
 */
class SyncService
{
    private const MAX_ERROR_LENGTH = 300;

    public function __construct(private AchievementService $achievements)
    {
    }

    /**
     * @param  array<int, array<string, mixed>>  $items
     * @return array{results: array<int, array{uuid: string, status: string, message: string|null}>, summary: array{completed: int, failed: int}}
     */
    public function sync(User $user, array $items): array
    {
        $results = [];

        foreach ($items as $item) {
            $results[] = $this->syncItem($user, $item);
        }

        $completed = count(array_filter(
            $results,
            fn (array $result) => $result['status'] === SyncStatus::Completed->value,
        ));

        return [
            'results' => $results,
            'summary' => [
                'completed' => $completed,
                'failed' => count($results) - $completed,
            ],
        ];
    }

    /**
     * @param  array<string, mixed>  $item
     * @return array{uuid: string, status: string, message: string|null}
     */
    private function syncItem(User $user, array $item): array
    {
        $uuid = (string) $item['uuid'];
        $type = (string) $item['type'];

        $queue = SyncQueue::query()->firstOrCreate(
            ['client_uuid' => $uuid],
            [
                'user_id' => $user->id,
                'type' => $type,
                'payload' => $item,
                'status' => SyncStatus::Pending,
                'received_at' => now(),
            ],
        );

        if ($queue->user_id !== $user->id) {
            return $this->result($uuid, SyncStatus::Failed, 'UUID sinkronisasi sudah dipakai pengguna lain.');
        }

        if ($queue->status === SyncStatus::Completed) {
            return $this->result($uuid, SyncStatus::Completed);
        }

        $queue->update([
            'status' => SyncStatus::Processing,
            'attempts' => $queue->attempts + 1,
            'received_at' => now(),
        ]);

        try {
            DB::transaction(function () use ($user, $type, $item) {
                match ($type) {
                    'session' => $this->processSession($user, $item),
                    'progress' => $this->processProgress($user, $item),
                    'answer' => $this->processAnswer($user, $item),
                    'material_block' => $this->processMaterialBlock($user, $item),
                };
            });

            $queue->update([
                'status' => SyncStatus::Completed,
                'processed_at' => now(),
                'error_message' => null,
            ]);

            return $this->result($uuid, SyncStatus::Completed);
        } catch (ValidationException $exception) {
            $message = (string) (collect($exception->errors())->flatten()->first()
                ?? 'Payload sinkronisasi tidak valid.');

            $queue->update([
                'status' => SyncStatus::Failed,
                'error_message' => Str::limit($message, self::MAX_ERROR_LENGTH),
            ]);

            return $this->result($uuid, SyncStatus::Failed, $message);
        } catch (Throwable $exception) {
            report($exception);

            $queue->update([
                'status' => SyncStatus::Failed,
                'error_message' => 'Gagal memproses item sinkronisasi.',
            ]);

            return $this->result($uuid, SyncStatus::Failed, 'Gagal memproses item sinkronisasi.');
        }
    }

    /**
     * @param  array<string, mixed>  $item
     */
    private function processSession(User $user, array $item): void
    {
        $data = $this->validatePayload($item['payload'], [
            'assessment_id' => ['required', 'integer', 'exists:assessments,id'],
            'mode' => ['required', 'string', Rule::in(Difficulty::values())],
            'duration_seconds' => ['nullable', 'integer', 'min:0', 'max:86400'],
            'started_at' => ['nullable', 'date'],
            'completed_at' => ['nullable', 'date'],
            'answers' => ['required', 'array', 'max:100'],
            'answers.*.question_id' => ['required', 'integer'],
            'answers.*.user_answer' => ['nullable'],
            'answers.*.time_spent' => ['nullable', 'integer', 'min:0', 'max:86400'],
            'answers.*.answered_at' => ['nullable', 'date'],
            'answers.*.is_correct' => ['nullable', 'boolean'],
            'answers.*.points_earned' => ['nullable', 'integer', 'min:0', 'max:1000'],
            'answers.*.ai_feedback' => ['nullable', 'array'],
        ]);

        if (GameSession::query()->where('client_uuid', $item['uuid'])->exists()) {
            return;
        }

        $assessment = Assessment::query()
            ->with(['questions.questionOptions', 'chapter'])
            ->findOrFail($data['assessment_id']);

        if (! $assessment->is_active) {
            throw ValidationException::withMessages([
                'assessment_id' => 'Asesmen sudah tidak aktif.',
            ]);
        }

        $questions = $assessment->questions->keyBy('id');
        $submitted = collect($data['answers'])->keyBy('question_id');
        $evaluated = [];

        foreach ($submitted as $answer) {
            $question = $questions->get((int) $answer['question_id']);

            if (! $question instanceof Question) {
                throw ValidationException::withMessages([
                    'answers' => 'Soal tidak termasuk dalam asesmen ini.',
                ]);
            }

            [$isCorrect, $points] = $this->evaluateAnswer($question, $answer);

            $evaluated[] = [
                'question_id' => $question->id,
                'user_answer' => $answer['user_answer'] ?? null,
                'is_correct' => $isCorrect,
                'points_earned' => $points,
                'time_spent' => min(
                    (int) ($answer['time_spent'] ?? 0),
                    $assessment->duration,
                ),
                'ai_feedback' => $answer['ai_feedback'] ?? null,
                'answered_at' => isset($answer['answered_at'])
                    ? Carbon::parse($answer['answered_at'])
                    : now(),
            ];
        }

        // Uraian tetap disimpan, tetapi belum masuk skor sampai dinilai AI/guru.
        $gradedQuestions = $assessment->questions
            ->reject(fn (Question $question) => $question->type === QuestionType::Essay);
        $gradedAnswers = array_values(array_filter(
            $evaluated,
            fn (array $row) => $questions->get($row['question_id'])?->type !== QuestionType::Essay,
        ));

        $maxScore = (int) $gradedQuestions->sum('points');
        $earned = (int) array_sum(array_column($gradedAnswers, 'points_earned'));
        $correctCount = count(array_filter($gradedAnswers, fn (array $row) => $row['is_correct']));
        $answeredCount = count($gradedAnswers);
        $totalQuestions = $gradedQuestions->count();
        $wrongCount = $answeredCount - $correctCount;
        $unanswered = max(0, $totalQuestions - $answeredCount);
        $totalScore = $maxScore > 0 ? (int) round($earned / $maxScore * 100) : 0;
        $isPassed = $totalScore >= $assessment->passing_score;

        $completedAt = isset($data['completed_at'])
            ? Carbon::parse($data['completed_at'])
            : now();
        $startedAt = isset($data['started_at'])
            ? Carbon::parse($data['started_at'])
            : $completedAt->copy()->subSeconds((int) ($data['duration_seconds'] ?? 0));
        $duration = (int) ($data['duration_seconds'] ?? max(0, $startedAt->diffInSeconds($completedAt)));

        $xpEarned = $earned;
        $coinsEarned = intdiv($xpEarned, 5);

        $session = GameSession::query()->create([
            'client_uuid' => (string) $item['uuid'],
            'user_id' => $user->id,
            'assessment_id' => $assessment->id,
            'mode' => $data['mode'],
            'score' => $totalScore,
            'correct_answers' => $correctCount,
            'total_questions' => $totalQuestions,
            'duration_seconds' => $duration,
            'status' => 'completed',
            'synced' => true,
            'started_at' => $startedAt,
            'completed_at' => $completedAt,
        ]);

        foreach ($evaluated as $row) {
            $session->answers()->create([
                'question_id' => $row['question_id'],
                'user_answer' => $row['user_answer'],
                'is_correct' => $row['is_correct'],
                'points_earned' => $row['points_earned'],
                'time_spent' => $row['time_spent'],
                'ai_feedback' => $row['ai_feedback'],
                'answered_at' => $row['answered_at'],
            ]);
        }

        $session->result()->create([
            'total_score' => $totalScore,
            'max_score' => $maxScore,
            'correct_count' => $correctCount,
            'wrong_count' => $wrongCount,
            'unanswered_count' => $unanswered,
            'xp_earned' => $xpEarned,
            'coins_earned' => $coinsEarned,
            'is_passed' => $isPassed,
            'detailed_results' => array_map(fn (array $row) => [
                'question_id' => $row['question_id'],
                'is_correct' => $row['is_correct'],
                'points_earned' => $row['points_earned'],
                'time_spent' => $row['time_spent'],
            ], $evaluated),
        ]);

        $lockedUser = User::query()->lockForUpdate()->findOrFail($user->id);
        $streak = $this->nextStreak($lockedUser, $completedAt);

        $lockedUser->update([
            'xp' => $lockedUser->xp + $xpEarned,
            'coins' => $lockedUser->coins + $coinsEarned,
            'level' => User::levelForXp($lockedUser->xp + $xpEarned),
            'streak_days' => $streak,
            'last_played_at' => $completedAt,
        ]);

        $this->touchProgress(
            $lockedUser,
            $assessment,
            $totalScore,
            $duration,
            $isPassed,
            $completedAt,
        );

        $this->achievements->awardForSession($lockedUser, $session);
    }

    private function touchProgress(
        User $user,
        Assessment $assessment,
        int $score,
        int $duration,
        bool $isPassed,
        Carbon $completedAt,
    ): void {
        $progress = UserProgress::query()->firstOrNew([
            'user_id' => $user->id,
            'chapter_id' => $assessment->chapter_id,
        ]);

        $progress->attempts = (int) ($progress->attempts ?? 0) + 1;
        $progress->best_score = max((int) ($progress->best_score ?? 0), $score);
        $progress->total_time_spent = (int) ($progress->total_time_spent ?? 0) + $duration;
        $progress->progress_percentage = max((int) ($progress->progress_percentage ?? 0), $score);
        $progress->last_accessed_at = $completedAt;

        if ($isPassed || $progress->status === ProgressStatus::Completed) {
            $progress->status = ProgressStatus::Completed;
            $progress->completed_at ??= $completedAt;
        } else {
            $progress->status = ProgressStatus::InProgress;
        }

        $progress->save();
    }

    /**
     * @param  array<string, mixed>  $item
     */
    private function processProgress(User $user, array $item): void
    {
        $data = $this->validatePayload($item['payload'], [
            'chapter_id' => ['required', 'integer', 'exists:chapters,id'],
            'status' => ['nullable', 'string', Rule::in(ProgressStatus::values())],
            'progress_percentage' => ['nullable', 'integer', 'min:0', 'max:100'],
            'total_time_spent' => ['nullable', 'integer', 'min:0', 'max:864000'],
            'best_score' => ['nullable', 'integer', 'min:0', 'max:100'],
            'materials_read' => ['nullable', 'integer', 'min:0', 'max:10000'],
            'last_accessed_at' => ['nullable', 'date'],
        ]);

        $chapter = Chapter::query()->findOrFail($data['chapter_id']);
        $incomingStatus = ProgressStatus::tryFrom((string) ($data['status'] ?? ProgressStatus::InProgress->value))
            ?? ProgressStatus::InProgress;

        $progress = UserProgress::query()->firstOrNew([
            'user_id' => $user->id,
            'chapter_id' => $chapter->id,
        ]);

        $statusRank = [
            ProgressStatus::NotStarted->value => 0,
            ProgressStatus::InProgress->value => 1,
            ProgressStatus::Completed->value => 2,
        ];

        $currentStatus = $progress->status ?? ProgressStatus::NotStarted;

        if ($statusRank[$incomingStatus->value] >= $statusRank[$currentStatus->value]) {
            $progress->status = $incomingStatus;
        }

        $progress->progress_percentage = max(
            (int) ($progress->progress_percentage ?? 0),
            (int) ($data['progress_percentage'] ?? 0),
        );
        $progress->best_score = max(
            (int) ($progress->best_score ?? 0),
            (int) ($data['best_score'] ?? 0),
        );
        $progress->materials_read = max(
            (int) ($progress->materials_read ?? 0),
            (int) ($data['materials_read'] ?? 0),
        );
        $progress->total_time_spent = max(
            (int) ($progress->total_time_spent ?? 0),
            (int) ($data['total_time_spent'] ?? 0),
        );

        $accessedAt = isset($data['last_accessed_at'])
            ? Carbon::parse($data['last_accessed_at'])
            : now();

        if ($progress->last_accessed_at === null || $accessedAt->greaterThan($progress->last_accessed_at)) {
            $progress->last_accessed_at = $accessedAt;
        }

        if ($progress->status === ProgressStatus::Completed) {
            $progress->completed_at ??= $accessedAt;
        }

        $progress->save();

        $this->achievements->awardForProgress($user);
    }

    /**
     * @param  array<string, mixed>  $item
     */
    private function processAnswer(User $user, array $item): void
    {
        $data = $this->validatePayload($item['payload'], [
            'session_uuid' => ['required', 'uuid'],
            'question_id' => ['required', 'integer'],
            'user_answer' => ['nullable'],
            'time_spent' => ['nullable', 'integer', 'min:0', 'max:86400'],
            'answered_at' => ['nullable', 'date'],
            'is_correct' => ['nullable', 'boolean'],
            'points_earned' => ['nullable', 'integer', 'min:0', 'max:1000'],
            'ai_feedback' => ['nullable', 'array'],
        ]);

        $session = GameSession::query()
            ->where('client_uuid', $data['session_uuid'])
            ->where('user_id', $user->id)
            ->with('assessment.questions.questionOptions')
            ->first();

        if (! $session instanceof GameSession) {
            throw ValidationException::withMessages([
                'session_uuid' => 'Sesi belum tersinkron. Kirim sesi terlebih dahulu.',
            ]);
        }

        $question = $session->assessment->questions
            ->firstWhere('id', (int) $data['question_id']);

        if (! $question instanceof Question) {
            throw ValidationException::withMessages([
                'question_id' => 'Soal tidak termasuk dalam sesi ini.',
            ]);
        }

        [$isCorrect, $points] = $this->evaluateAnswer($question, $data);

        SessionAnswer::query()->updateOrCreate(
            [
                'game_session_id' => $session->id,
                'question_id' => $question->id,
            ],
            [
                'user_answer' => $data['user_answer'] ?? null,
                'is_correct' => $isCorrect,
                'points_earned' => $points,
                'time_spent' => (int) ($data['time_spent'] ?? 0),
                'ai_feedback' => $data['ai_feedback'] ?? null,
                'answered_at' => isset($data['answered_at'])
                    ? Carbon::parse($data['answered_at'])
                    : now(),
            ],
        );
    }

    /**
     * @param  array<string, mixed>  $answer
     * @return array{0: bool, 1: int}
     */
    private function evaluateAnswer(Question $question, array $answer): array
    {
        $userAnswer = $answer['user_answer'] ?? null;

        return match ($question->type) {
            QuestionType::MultipleChoice => $this->evaluateChoice($question, $userAnswer),
            QuestionType::MultipleAnswer => $this->evaluateMultipleAnswer($question, $userAnswer),
            QuestionType::Essay => [false, 0],
            default => $this->evaluateClientScored($question, $answer),
        };
    }

    private function evaluateChoice(Question $question, mixed $userAnswer): array
    {
        $optionId = is_array($userAnswer) ? ($userAnswer['option_id'] ?? null) : null;

        if ($optionId !== null) {
            $option = $question->questionOptions->firstWhere('id', (int) $optionId);
            $isCorrect = $option?->is_correct === true;

            return [$isCorrect, $isCorrect ? $question->points : 0];
        }

        $text = is_array($userAnswer)
            ? (string) ($userAnswer['text'] ?? '')
            : (string) ($userAnswer ?? '');
        $expected = (string) (($question->correct_answer ?? [])['text'] ?? '');
        $isCorrect = $text !== ''
            && $expected !== ''
            && mb_strtolower(trim($text)) === mb_strtolower(trim($expected));

        return [$isCorrect, $isCorrect ? $question->points : 0];
    }

    private function evaluateMultipleAnswer(Question $question, mixed $userAnswer): array
    {
        $selected = is_array($userAnswer)
            ? ($userAnswer['option_ids'] ?? [])
            : [];

        $selected = collect(is_array($selected) ? $selected : [])
            ->map(fn ($id) => (int) $id)
            ->unique()
            ->sort()
            ->values();

        $expected = $question->questionOptions
            ->where('is_correct', true)
            ->pluck('id')
            ->map(fn ($id) => (int) $id)
            ->sort()
            ->values();

        $isCorrect = $expected->isNotEmpty()
            && $selected->all() === $expected->all();

        return [$isCorrect, $isCorrect ? $question->points : 0];
    }

    /**
     * Tipe interaktif menerima penilaian client; poin dibatasi oleh poin
     * maksimum soal. Jawaban pilihan ganda tetap dinilai ulang server.
     *
     * @param  array<string, mixed>  $answer
     * @return array{0: bool, 1: int}
     */
    private function evaluateClientScored(Question $question, array $answer): array
    {
        $isCorrect = (bool) ($answer['is_correct'] ?? false);
        $points = min(
            max(0, (int) ($answer['points_earned'] ?? 0)),
            $question->points,
        );

        return [$isCorrect, $isCorrect ? $points : 0];
    }

    /**
     * Menyimpan hasil kerja satu blok interaktif materi (plan §3.4.1).
     *
     * Idempoten: baris dikunci oleh (user_id, material_id, block_id) dan nilai
     * terbaik dipertahankan, sehingga kiriman ulang dari antrean offline tidak
     * pernah menurunkan skor atau menggandakan baris.
     */
    private function processMaterialBlock(User $user, array $item): void
    {
        $data = $this->validatePayload($item['payload'], [
            'material_id' => ['required', 'integer', 'exists:learning_materials,id'],
            'block_id' => ['required', 'string', 'max:64'],
            'block_type' => ['required', 'string', 'max:32'],
            'score' => ['required', 'integer', 'min:0', 'max:100'],
            'max_score' => ['nullable', 'integer', 'min:1', 'max:100'],
            'attempts' => ['nullable', 'integer', 'min:1', 'max:1000'],
            'is_completed' => ['nullable', 'boolean'],
            'details' => ['nullable', 'array', 'max:50'],
            'last_answered_at' => ['nullable', 'date'],
        ]);

        $material = LearningMaterial::query()
            ->with('chapter')
            ->findOrFail($data['material_id']);

        if (! $material->is_active || $material->chapter?->is_active !== true) {
            throw ValidationException::withMessages([
                'material_id' => 'Materi sudah tidak aktif.',
            ]);
        }

        $block = collect($material->blocks ?? [])
            ->first(fn ($candidate) => is_array($candidate)
                && (string) ($candidate['id'] ?? '') === (string) $data['block_id']);

        if (! is_array($block)) {
            throw ValidationException::withMessages([
                'block_id' => 'Blok tidak ditemukan pada materi ini.',
            ]);
        }

        $type = (string) ($block['type'] ?? '');

        if (! in_array($type, BlockSchema::ACTIVITY_TYPES, true)) {
            throw ValidationException::withMessages([
                'block_id' => 'Blok ini tidak dinilai sehingga tidak boleh dikirim.',
            ]);
        }

        if ($type !== (string) $data['block_type']) {
            throw ValidationException::withMessages([
                'block_type' => 'Tipe blok tidak cocok dengan materi.',
            ]);
        }

        $answeredAt = isset($data['last_answered_at'])
            ? Carbon::parse($data['last_answered_at'])
            : now();

        $response = MaterialBlockResponse::query()->firstOrNew([
            'user_id' => $user->id,
            'material_id' => $material->id,
            'block_id' => (string) $data['block_id'],
        ]);

        $isCompleted = (bool) ($data['is_completed'] ?? false)
            || (bool) ($response->is_completed ?? false);

        $response->fill([
            'block_type' => $type,
            'score' => max((int) ($response->score ?? 0), (int) $data['score']),
            'max_score' => max((int) ($response->max_score ?? 100), (int) ($data['max_score'] ?? 100)),
            'attempts' => max((int) ($response->attempts ?? 0), (int) ($data['attempts'] ?? 1)),
            'is_completed' => $isCompleted,
            'details' => $data['details'] ?? $response->details,
            'last_answered_at' => $answeredAt,
        ]);

        if ($isCompleted && $response->first_completed_at === null) {
            $response->first_completed_at = $answeredAt;
        }

        $response->save();
    }

    private function nextStreak(User $user, Carbon $playedAt): int
    {
        $current = (int) $user->streak_days;
        $last = $user->last_played_at;

        if ($last === null) {
            return 1;
        }

        if ($last->isSameDay($playedAt)) {
            return max(1, $current);
        }

        if ($last->isSameDay($playedAt->copy()->subDay())) {
            return $current + 1;
        }

        return 1;
    }

    /**
     * @param  array<string, mixed>  $payload
     * @param  array<string, mixed>  $rules
     * @return array<string, mixed>
     */
    private function validatePayload(array $payload, array $rules): array
    {
        return Validator::make($payload, $rules)->validate();
    }

    /**
     * @return array{uuid: string, status: string, message: string|null}
     */
    private function result(string $uuid, SyncStatus $status, ?string $message = null): array
    {
        return [
            'uuid' => $uuid,
            'status' => $status->value,
            'message' => $message,
        ];
    }
}
