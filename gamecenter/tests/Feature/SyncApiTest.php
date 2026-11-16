<?php

namespace Tests\Feature;

use App\Enums\ProgressStatus;
use App\Enums\QuestionType;
use App\Models\Assessment;
use App\Models\GameSession;
use App\Models\Question;
use App\Models\SyncQueue;
use App\Models\User;
use App\Models\UserProgress;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Str;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class SyncApiTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_guest_cannot_push_a_sync_batch(): void
    {
        $this->postJson('/api/sync', [
            'items' => [[
                'uuid' => (string) Str::uuid(),
                'type' => 'progress',
                'payload' => ['chapter_id' => 1],
            ]],
        ])->assertUnauthorized();
    }

    public function test_session_is_stored_scored_and_rewarded(): void
    {
        $user = $this->student();
        $assessment = $this->easyAssessment();

        $item = $this->sessionItem($assessment, fn (Question $question) => [
            'option_id' => $this->correctOptionId($question),
        ]);

        $response = $this->actingAs($user, 'sanctum')->postJson('/api/sync', [
            'items' => [$item],
        ]);

        $response->assertOk()
            ->assertJsonPath('results.0.status', 'completed')
            ->assertJsonPath('summary.completed', 1)
            ->assertJsonPath('summary.failed', 0);

        $this->assertDatabaseHas('game_sessions', [
            'client_uuid' => $item['uuid'],
            'user_id' => $user->id,
            'assessment_id' => $assessment->id,
            'mode' => 'easy',
            'score' => 100,
            'correct_answers' => 5,
            'total_questions' => 5,
            'synced' => true,
        ]);

        $session = GameSession::query()->where('client_uuid', $item['uuid'])->firstOrFail();

        $this->assertSame(5, $session->answers()->count());
        $this->assertSame(5, $session->answers()->where('is_correct', true)->count());

        $this->assertDatabaseHas('session_results', [
            'game_session_id' => $session->id,
            'total_score' => 100,
            'max_score' => 50,
            'correct_count' => 5,
            'wrong_count' => 0,
            'unanswered_count' => 0,
            'xp_earned' => 50,
            'coins_earned' => 10,
            'is_passed' => true,
        ]);

        $user->refresh();

        $this->assertSame(135, $user->xp);
        $this->assertSame(2, $user->level);
        $this->assertSame(50, $user->coins);
        $this->assertSame(1, $user->streak_days);
        $this->assertNotNull($user->last_played_at);

        $progress = UserProgress::query()
            ->where('user_id', $user->id)
            ->where('chapter_id', $assessment->chapter_id)
            ->firstOrFail();

        $this->assertSame(1, $progress->attempts);
        $this->assertSame(100, $progress->best_score);
        $this->assertSame(100, $progress->progress_percentage);
        $this->assertSame(ProgressStatus::Completed, $progress->status);

        $this->assertDatabaseHas('sync_queue', [
            'client_uuid' => $item['uuid'],
            'user_id' => $user->id,
            'type' => 'session',
            'status' => 'completed',
        ]);
    }

    public function test_server_recomputes_objective_answers_instead_of_trusting_client(): void
    {
        $user = $this->student();
        $assessment = $this->easyAssessment();
        $first = $assessment->questions->first();

        $item = $this->sessionItem($assessment, function (Question $question) use ($first) {
            if ($question->id === $first->id) {
                return ['option_id' => $this->correctOptionId($question)];
            }

            return ['option_id' => $this->wrongOptionId($question)];
        });

        // Client mencoba mengaku semua jawaban benar.
        foreach ($item['payload']['answers'] as $index => $answer) {
            $item['payload']['answers'][$index]['is_correct'] = true;
            $item['payload']['answers'][$index]['points_earned'] = 10;
        }

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$item]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'completed');

        $session = GameSession::query()->where('client_uuid', $item['uuid'])->firstOrFail();
        $result = $session->result;

        $this->assertSame(1, $result->correct_count);
        $this->assertSame(4, $result->wrong_count);
        $this->assertSame(20, $result->total_score);
        $this->assertSame(10, $result->xp_earned);
        $this->assertSame(2, $result->coins_earned);
        $this->assertFalse($result->is_passed);
        $this->assertSame(30, $user->refresh()->xp);
    }

    public function test_essay_answer_is_stored_but_excluded_from_the_session_score(): void
    {
        $user = $this->student();
        $assessment = Assessment::query()
            ->where('difficulty', 'hard')
            ->with(['questions.questionOptions', 'chapter'])
            ->firstOrFail();

        $answers = $assessment->questions->map(function (Question $question): array {
            $answer = [
                'question_id' => $question->id,
                'time_spent' => 10,
                'answered_at' => now()->toIso8601String(),
                'is_correct' => true,
                'points_earned' => $question->points,
            ];

            if ($question->type === QuestionType::Essay) {
                $answer['user_answer'] = ['text' => 'Jawaban uraian lengkap.'];
                $answer['is_correct'] = false;
                $answer['points_earned'] = 0;

                return $answer;
            }

            if ($question->type === QuestionType::MultipleChoice || $question->type === QuestionType::Simulation) {
                $answer['user_answer'] = ['option_id' => $this->correctOptionId($question)];

                return $answer;
            }

            if ($question->type === QuestionType::MultipleAnswer) {
                $answer['user_answer'] = [
                    'option_ids' => $question->questionOptions
                        ->where('is_correct', true)
                        ->pluck('id')
                        ->values()
                        ->all(),
                ];

                return $answer;
            }

            if (in_array($question->type, [QuestionType::DragDrop, QuestionType::Puzzle], true)) {
                $answer['user_answer'] = [
                    'order' => $question->correct_answer['order'],
                ];

                return $answer;
            }

            $answer['user_answer'] = [
                'pairs' => $question->correct_answer['pairs'],
            ];

            return $answer;
        })->all();

        $item = [
            'uuid' => (string) Str::uuid(),
            'type' => 'session',
            'recorded_at' => now()->toIso8601String(),
            'payload' => [
                'assessment_id' => $assessment->id,
                'mode' => 'hard',
                'duration_seconds' => 600,
                'started_at' => now()->subMinutes(10)->toIso8601String(),
                'completed_at' => now()->toIso8601String(),
                'answers' => $answers,
            ],
        ];

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$item]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'completed');

        $session = GameSession::query()->where('client_uuid', $item['uuid'])->firstOrFail();
        $essay = $assessment->questions->firstWhere('type', QuestionType::Essay);
        $essayAnswer = $session->answers()->where('question_id', $essay->id)->firstOrFail();

        $this->assertSame(count($answers), $session->answers()->count());
        $this->assertFalse($essayAnswer->is_correct);
        $this->assertSame(0, $essayAnswer->points_earned);
        $this->assertSame(['text' => 'Jawaban uraian lengkap.'], $essayAnswer->user_answer);

        $result = $session->result;

        $this->assertSame(240, $result->max_score);
        $this->assertSame(100, $result->total_score);
        $this->assertSame(8, $session->total_questions);
        $this->assertSame(8, $result->correct_count);
        $this->assertSame(0, $result->unanswered_count);
        $this->assertTrue($result->is_passed);
        $this->assertSame(240, $result->xp_earned);
        $this->assertSame(48, $result->coins_earned);
        $this->assertSame(525, $user->refresh()->xp);
    }

    public function test_session_sync_is_idempotent_per_uuid(): void
    {
        $user = $this->student();
        $assessment = $this->easyAssessment();
        $item = $this->sessionItem($assessment, fn (Question $question) => [
            'option_id' => $this->correctOptionId($question),
        ]);

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$item]])
            ->assertOk();

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$item]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'completed');

        $this->assertSame(1, GameSession::query()->where('client_uuid', $item['uuid'])->count());
        $this->assertSame(135, $user->refresh()->xp);
        $this->assertDatabaseCount('sync_queue', 1);
    }

    public function test_failed_item_does_not_block_other_items_and_can_be_retried(): void
    {
        $user = $this->student();
        $chapter = Assessment::query()->firstOrFail()->chapter_id;

        $broken = [
            'uuid' => (string) Str::uuid(),
            'type' => 'session',
            'payload' => ['mode' => 'easy', 'answers' => []],
        ];

        $progress = [
            'uuid' => (string) Str::uuid(),
            'type' => 'progress',
            'payload' => [
                'chapter_id' => $chapter,
                'status' => 'in_progress',
                'progress_percentage' => 40,
                'best_score' => 40,
                'total_time_spent' => 120,
            ],
        ];

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$broken, $progress]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'failed')
            ->assertJsonPath('results.1.status', 'completed')
            ->assertJsonPath('summary.completed', 1)
            ->assertJsonPath('summary.failed', 1);

        $queue = SyncQueue::query()->where('client_uuid', $broken['uuid'])->firstOrFail();
        $this->assertSame('failed', $queue->status->value);
        $this->assertNotNull($queue->error_message);
        $this->assertSame(1, $queue->attempts);

        $assessment = $this->easyAssessment();
        $retry = $this->sessionItem($assessment, fn (Question $question) => [
            'option_id' => $this->correctOptionId($question),
        ], $broken['uuid']);

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$retry]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'completed');

        $this->assertSame('completed', $queue->refresh()->status->value);
        $this->assertSame(2, $queue->attempts);
    }

    public function test_progress_sync_keeps_best_values_and_completed_status(): void
    {
        $user = $this->student();
        $chapter = Assessment::query()->firstOrFail()->chapter_id;

        $first = [
            'uuid' => (string) Str::uuid(),
            'type' => 'progress',
            'payload' => [
                'chapter_id' => $chapter,
                'status' => 'completed',
                'progress_percentage' => 100,
                'best_score' => 80,
                'total_time_spent' => 600,
                'last_accessed_at' => now()->toIso8601String(),
            ],
        ];

        $second = [
            'uuid' => (string) Str::uuid(),
            'type' => 'progress',
            'payload' => [
                'chapter_id' => $chapter,
                'status' => 'in_progress',
                'progress_percentage' => 60,
                'best_score' => 60,
                'total_time_spent' => 900,
                'last_accessed_at' => now()->addMinute()->toIso8601String(),
            ],
        ];

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$first, $second]])
            ->assertOk()
            ->assertJsonPath('summary.completed', 2);

        $progress = UserProgress::query()
            ->where('user_id', $user->id)
            ->where('chapter_id', $chapter)
            ->firstOrFail();

        $this->assertSame(ProgressStatus::Completed, $progress->status);
        $this->assertSame(100, $progress->progress_percentage);
        $this->assertSame(80, $progress->best_score);
        $this->assertSame(900, $progress->total_time_spent);
        $this->assertNotNull($progress->completed_at);
    }

    public function test_answer_item_updates_an_existing_session_answer(): void
    {
        $user = $this->student();
        $assessment = $this->easyAssessment();
        $sessionItem = $this->sessionItem($assessment, fn (Question $question) => [
            'option_id' => $this->correctOptionId($question),
        ]);

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$sessionItem]])
            ->assertOk();

        $question = $assessment->questions->firstOrFail();
        $answerItem = [
            'uuid' => (string) Str::uuid(),
            'type' => 'answer',
            'payload' => [
                'session_uuid' => $sessionItem['uuid'],
                'question_id' => $question->id,
                'user_answer' => ['option_id' => $this->wrongOptionId($question)],
                'time_spent' => 15,
                'answered_at' => now()->toIso8601String(),
            ],
        ];

        $this->actingAs($user, 'sanctum')
            ->postJson('/api/sync', ['items' => [$answerItem]])
            ->assertOk()
            ->assertJsonPath('results.0.status', 'completed');

        $session = GameSession::query()->where('client_uuid', $sessionItem['uuid'])->firstOrFail();
        $answer = $session->answers()->where('question_id', $question->id)->firstOrFail();

        $this->assertFalse($answer->is_correct);
        $this->assertSame(0, $answer->points_earned);
        $this->assertSame(15, $answer->time_spent);
    }

    private function student(): User
    {
        return User::factory()->create([
            'username' => 'pemain-uji',
            'email' => 'pemain-uji@gamecenter.test',
        ]);
    }

    private function easyAssessment(): Assessment
    {
        return Assessment::query()
            ->where('difficulty', 'easy')
            ->with(['questions.questionOptions', 'chapter'])
            ->firstOrFail();
    }

    private function correctOptionId(Question $question): int
    {
        return (int) $question->questionOptions->firstWhere('is_correct', true)->id;
    }

    private function wrongOptionId(Question $question): int
    {
        return (int) $question->questionOptions->firstWhere('is_correct', false)->id;
    }

    /**
     * @return array<string, mixed>
     */
    private function sessionItem(Assessment $assessment, callable $answer, ?string $uuid = null): array
    {
        return [
            'uuid' => $uuid ?? (string) Str::uuid(),
            'type' => 'session',
            'recorded_at' => now()->toIso8601String(),
            'payload' => [
                'assessment_id' => $assessment->id,
                'mode' => $assessment->difficulty->value,
                'duration_seconds' => 300,
                'started_at' => now()->subMinutes(5)->toIso8601String(),
                'completed_at' => now()->toIso8601String(),
                'answers' => $assessment->questions->map(fn (Question $question) => [
                    'question_id' => $question->id,
                    'user_answer' => $answer($question),
                    'time_spent' => 10,
                    'answered_at' => now()->toIso8601String(),
                ])->all(),
            ],
        ];
    }
}
