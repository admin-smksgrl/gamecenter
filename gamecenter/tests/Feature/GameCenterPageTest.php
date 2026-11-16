<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class GameCenterPageTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_home_page_renders_the_jelajah_materi_view(): void
    {
        $response = $this->get('/');

        $response->assertOk();
        $response->assertInertia(fn (AssertableInertia $page) => $page
            ->component('GameCenter/Index')
            ->has('levels', 6)
            ->has('levels.0.classes')
            ->has('levels.0.classes.0.subjects')
            ->where('stats.levels', 6)
            ->where('stats.classes', 18)
            ->where('stats.chapters', 5)
            ->where('stats.questions', 82)
        );
    }

    public function test_home_page_exposes_the_eksponen_chapter_for_matematika_kelas_10(): void
    {
        $response = $this->get('/');

        $response->assertInertia(function (AssertableInertia $page) {
            $levels = collect($page->toArray()['props']['levels']);
            $sma = $levels->firstWhere('slug', 'sma');

            $this->assertSame('sma', $sma['slug']);

            $kelas10 = collect($sma['classes'])->firstWhere('slug', 'kelas-10');
            $this->assertNotNull($kelas10);

            $matematika = collect($kelas10['subjects'])->firstWhere('slug', 'matematika');
            $this->assertNotNull($matematika);
            $this->assertSame(1, $matematika['chapters_count']);
            $this->assertSame('Eksponen', $matematika['chapters'][0]['title']);
            $this->assertSame(3, $matematika['chapters'][0]['materials_count']);

            $difficulties = collect($matematika['chapters'][0]['assessments'])->pluck('difficulty');
            $this->assertEqualsCanonicalizing(['easy', 'medium', 'hard'], $difficulties->all());
        });
    }

    public function test_api_health_endpoint_responds(): void
    {
        $this->getJson('/api/health')
            ->assertOk()
            ->assertJsonPath('status', 'ok');
    }
}
