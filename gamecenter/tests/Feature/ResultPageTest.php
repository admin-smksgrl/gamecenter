<?php

namespace Tests\Feature;

use App\Enums\QuestionType;
use App\Models\Assessment;
use App\Models\GameSession;
use App\Models\Question;
use App\Models\SessionAnswer;
use App\Models\SessionResult;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Str;
use Inertia\Testing\AssertableInertia;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class ResultPageTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_guest_is_redirected_from_the_result_page(): void
    {
        [$session] = $this->makeSession(User::factory()->create());

        $this->get("/hasil/{$session->id}")->assertRedirect('/masuk');
    }

    public function test_owner_can_review_the_synced_session(): void
    {
        $user = User::factory()->create();
        [$session, $question] = $this->makeSession($user);

        $response = $this->actingAs($user)->get("/hasil/{$session->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) use ($session, $question) {
            $page->component('GameCenter/Result');

            $props = $page->toArray()['props'];

            $this->assertSame($session->id, $props['session']['id']);
            $this->assertSame(80, $props['session']['score']);
            $this->assertSame('Matematika', $props['context']['subject_name']);
            $this->assertSame('Eksponen', $props['context']['chapter_title']);
            $this->assertSame('default', $props['context']['level_theme']);

            $this->assertSame(80, $props['summary']['total_score']);
            $this->assertSame(100, $props['summary']['max_score']);
            $this->assertSame(8, $props['summary']['correct_count']);
            $this->assertSame(1, $props['summary']['wrong_count']);
            $this->assertSame(1, $props['summary']['unanswered_count']);
            $this->assertSame(80, $props['summary']['xp_earned']);
            $this->assertSame(16, $props['summary']['coins_earned']);
            $this->assertTrue($props['summary']['is_passed']);

            $this->assertCount(1, $props['answers']);
            $this->assertSame($question->question, $props['answers'][0]['question']);
            $this->assertSame('multiple_choice', $props['answers'][0]['type']);
            $this->assertTrue($props['answers'][0]['is_correct']);
            $this->assertSame(10, $props['answers'][0]['points_earned']);
            $this->assertSame(12, $props['answers'][0]['time_spent']);
            $this->assertNotNull($props['answers'][0]['expected']);
            $this->assertSame($question->explanation, $props['answers'][0]['explanation']);
        });
    }

    public function test_another_student_cannot_open_the_result(): void
    {
        $owner = User::factory()->create();
        $other = User::factory()->create();
        [$session] = $this->makeSession($owner);

        $this->actingAs($other)->get("/hasil/{$session->id}")->assertForbidden();
    }

    public function test_teacher_can_open_a_student_result(): void
    {
        $owner = User::factory()->create();
        $teacher = User::factory()->teacher()->create();
        [$session] = $this->makeSession($owner);

        $this->actingAs($teacher)->get("/hasil/{$session->id}")->assertOk();
    }

    /**
     * @return array{0: GameSession, 1: Question}
     */
    private function makeSession(User $user): array
    {
        $assessment = Assessment::query()
            ->where('difficulty', 'easy')
            ->with(['chapter.subject.classRoom.educationLevel', 'questions.questionOptions'])
            ->firstOrFail();

        $question = $assessment->questions
            ->first(fn (Question $item) => $item->type === QuestionType::MultipleChoice)
            ?? $assessment->questions->firstOrFail();

        $session = GameSession::query()->create([
            'client_uuid' => (string) Str::uuid(),
            'user_id' => $user->id,
            'assessment_id' => $assessment->id,
            'mode' => $assessment->difficulty,
            'score' => 80,
            'correct_answers' => 8,
            'total_questions' => 10,
            'duration_seconds' => 420,
            'status' => 'completed',
            'synced' => true,
            'started_at' => now()->subMinutes(7),
            'completed_at' => now(),
        ]);

        SessionResult::query()->create([
            'game_session_id' => $session->id,
            'total_score' => 80,
            'max_score' => 100,
            'correct_count' => 8,
            'wrong_count' => 1,
            'unanswered_count' => 1,
            'xp_earned' => 80,
            'coins_earned' => 16,
            'is_passed' => true,
        ]);

        SessionAnswer::query()->create([
            'game_session_id' => $session->id,
            'question_id' => $question->id,
            'user_answer' => ['option_id' => $question->questionOptions->firstWhere('is_correct', true)?->id],
            'is_correct' => true,
            'points_earned' => 10,
            'time_spent' => 12,
            'answered_at' => now(),
        ]);

        return [$session, $question];
    }
}
