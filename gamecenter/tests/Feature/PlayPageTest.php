<?php

namespace Tests\Feature;

use App\Enums\ProgressStatus;
use App\Models\Assessment;
use App\Models\User;
use App\Models\UserProgress;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class PlayPageTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_guest_can_open_the_medium_game_with_all_question_payloads(): void
    {
        $assessment = $this->assessment('medium');

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $page->component('GameCenter/Play');

            $props = $page->toArray()['props'];
            $questions = collect($props['questions']);

            $this->assertSame('Matematika', $props['context']['subject_name']);
            $this->assertSame('Eksponen', $props['context']['chapter_title']);
            $this->assertSame(8, $props['assessment']['question_count']);
            $this->assertNull($props['progress']);
            $this->assertCount(8, $questions);
            $this->assertSame('multiple_answer', $questions[6]['type']);
            $this->assertCount(5, $questions[6]['options']);

            $drag = $questions[7];
            $this->assertSame('drag_drop', $drag['type']);
            $this->assertSame(['a', 'b', 'c', 'd'], array_column($drag['payload'], 'id'));
            $this->assertSame(['a', 'b', 'c', 'd'], $drag['correct_answer']['order']);
        });
    }

    public function test_hard_game_exposes_matching_puzzle_and_simulation_data(): void
    {
        $assessment = $this->assessment('hard');

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];
            $questions = collect($props['questions'])->keyBy('type');

            $this->assertSame(9, $props['assessment']['question_count']);
            $this->assertSame(
                ['essay', 'matching', 'multiple_choice', 'puzzle', 'simulation'],
                $questions->keys()->sort()->values()->all(),
            );

            $matching = $questions['matching'];
            $this->assertCount(4, $matching['payload']);
            $this->assertSame('81', $matching['correct_answer']['pairs']['p2']);

            $puzzle = $questions['puzzle'];
            $this->assertCount(5, $puzzle['payload']);
            $this->assertSame('s5', $puzzle['correct_answer']['order'][4]);

            $simulation = $questions['simulation'];
            $this->assertCount(4, $simulation['options']);
            $this->assertCount(1, array_filter(
                $simulation['options'],
                fn (array $option) => $option['is_correct'],
            ));
        });
    }

    public function test_inactive_assessment_cannot_be_played(): void
    {
        $assessment = $this->assessment('easy');
        $assessment->update(['is_active' => false]);

        $this->get("/main/{$assessment->id}")->assertNotFound();
    }

    public function test_play_page_exposes_learning_materials_for_the_intro(): void
    {
        $assessment = $this->assessment('easy');

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];
            $materials = collect($props['materials']);

            $this->assertNull($props['progress']);
            $this->assertSame('default', $props['context']['level_theme']);
            $this->assertGreaterThan(0, $materials->count());
            $this->assertArrayHasKey('title', $materials[0]);
            $this->assertArrayHasKey('content', $materials[0]);
            $this->assertArrayHasKey('type_label', $materials[0]);
            $this->assertSame(1, $materials[0]['order']);
        });
    }

    public function test_logged_in_student_gets_progress_and_materials_read_count(): void
    {
        $assessment = $this->assessment('easy');
        $user = User::factory()->create();

        UserProgress::query()->create([
            'user_id' => $user->id,
            'chapter_id' => $assessment->chapter_id,
            'status' => ProgressStatus::InProgress,
            'progress_percentage' => 40,
            'best_score' => 70,
            'materials_read' => 2,
            'attempts' => 1,
            'last_accessed_at' => now(),
        ]);

        $response = $this->actingAs($user)->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('in_progress', $props['progress']['status']);
            $this->assertSame(70, $props['progress']['best_score']);
            $this->assertSame(2, $props['progress']['materials_read']);
        });
    }

    private function assessment(string $difficulty): Assessment
    {
        return Assessment::query()
            ->where('difficulty', $difficulty)
            ->firstOrFail();
    }
}
