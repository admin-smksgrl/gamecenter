<?php

namespace Tests\Feature;

use App\Enums\ProgressStatus;
use App\Models\Assessment;
use App\Models\GameSession;
use App\Models\SessionResult;
use App\Models\User;
use App\Models\UserProgress;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class ProgressPageTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_guest_is_redirected_from_the_progress_page(): void
    {
        $this->get('/progres')->assertRedirect('/masuk');
    }

    public function test_student_sees_stats_progress_sessions_and_achievements(): void
    {
        $user = User::factory()->create([
            'name' => 'Siswa Progres',
            'username' => 'siswa-progres',
            'xp' => 150,
            'level' => 2,
            'coins' => 40,
            'streak_days' => 3,
        ]);

        $assessment = Assessment::query()->with('chapter')->firstOrFail();
        $chapter = $assessment->chapter;

        UserProgress::query()->create([
            'user_id' => $user->id,
            'chapter_id' => $chapter->id,
            'status' => ProgressStatus::Completed,
            'progress_percentage' => 100,
            'best_score' => 90,
            'materials_read' => 3,
            'attempts' => 2,
            'total_time_spent' => 600,
            'last_accessed_at' => now(),
            'completed_at' => now(),
        ]);

        $session = GameSession::query()->create([
            'client_uuid' => (string) \Illuminate\Support\Str::uuid(),
            'user_id' => $user->id,
            'assessment_id' => $assessment->id,
            'mode' => $assessment->difficulty,
            'score' => 90,
            'correct_answers' => 9,
            'total_questions' => 10,
            'duration_seconds' => 300,
            'status' => 'completed',
            'synced' => true,
            'started_at' => now()->subMinutes(5),
            'completed_at' => now(),
        ]);

        SessionResult::query()->create([
            'game_session_id' => $session->id,
            'total_score' => 90,
            'max_score' => 100,
            'correct_count' => 9,
            'wrong_count' => 1,
            'unanswered_count' => 0,
            'xp_earned' => 90,
            'coins_earned' => 18,
            'is_passed' => true,
        ]);

        $response = $this->actingAs($user)->get('/progres');

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) use ($chapter, $assessment, $session) {
            $page->component('GameCenter/Progress');

            $props = $page->toArray()['props'];

            $this->assertSame('Siswa Progres', $props['user']['name']);
            $this->assertSame(150, $props['user']['xp']);
            $this->assertSame('Pemain', $props['user']['level_title']);
            $this->assertSame(33, $props['user']['level_progress']['percent']);
            $this->assertSame(100, $props['user']['level_progress']['xp_to_next']);
            $this->assertSame('default', $props['user']['level_theme']);

            $this->assertSame(1, $props['stats']['sessions']);
            $this->assertSame(1, $props['stats']['completed_chapters']);
            $this->assertSame(3, $props['stats']['materials_read']);
            $this->assertSame(5, $props['stats']['total_minutes']);
            $this->assertSame(90, $props['stats']['average_score']);
            $this->assertSame(90, $props['stats']['best_score']);
            $this->assertSame(8, $props['stats']['achievements_total']);

            $this->assertCount(7, $props['activity']);
            $this->assertSame(now()->toDateString(), $props['activity'][6]['date']);
            $this->assertSame(1, $props['activity'][6]['sessions']);

            $this->assertCount(1, $props['progress']);
            $this->assertSame($chapter->id, $props['progress'][0]['chapter_id']);
            $this->assertSame('completed', $props['progress'][0]['status']);
            $this->assertSame(3, $props['progress'][0]['materials_read']);
            $this->assertSame($assessment->id, $props['progress'][0]['assessment_id']);

            $this->assertCount(1, $props['sessions']);
            $this->assertSame(90, $props['sessions'][0]['score']);
            $this->assertSame(90, $props['sessions'][0]['xp_earned']);
            $this->assertSame(
                route('result.show', $session->id),
                $props['sessions'][0]['result_url'],
            );

            $this->assertCount(8, $props['achievements']);
            $this->assertSame(0, $props['stats']['achievements_unlocked']);
            $this->assertFalse($props['achievements'][0]['unlocked']);
        });
    }

    public function test_empty_progress_page_is_rendered_with_zero_stats(): void
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->get('/progres');

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame([], $props['progress']);
            $this->assertSame([], $props['sessions']);
            $this->assertSame(0, $props['stats']['sessions']);
            $this->assertSame(0, $props['stats']['materials_read']);
            $this->assertSame(0, $props['stats']['average_score']);
        });
    }
}
