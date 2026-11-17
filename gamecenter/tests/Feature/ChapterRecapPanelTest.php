<?php

namespace Tests\Feature;

use App\Filament\Resources\Chapters\Pages\ViewChapter;
use App\Models\Chapter;
use App\Models\LearningMaterial;
use App\Models\MaterialBlockResponse;
use App\Models\User;
use Database\Seeders\ClassSeeder;
use Database\Seeders\EducationLevelSeeder;
use Database\Seeders\SmaSmkMaterialSeeder;
use Database\Seeders\SubjectSeeder;
use Filament\Facades\Filament;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use Tests\TestCase;

/**
 * Panel guru: rekap skor blok pada halaman chapter (Fase 5.3) dan ekspor CSV
 * (Fase 5.4). Keduanya hanya membaca `material_block_responses`.
 */
class ChapterRecapPanelTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seed([
            EducationLevelSeeder::class,
            ClassSeeder::class,
            SubjectSeeder::class,
            SmaSmkMaterialSeeder::class,
        ]);

        Filament::setCurrentPanel(Filament::getPanel('admin'));
    }

    private function admin(): User
    {
        return User::factory()->admin()->create();
    }

    private function material(): LearningMaterial
    {
        return LearningMaterial::query()
            ->where('title', 'Menerapkan Pancasila dalam Kehidupan Berbangsa')
            ->firstOrFail();
    }

    public function test_chapter_page_shows_block_recap_and_validation_preview(): void
    {
        $material = $this->material();
        $chapter = $material->chapter;
        $student = User::factory()->create([
            'name' => 'Dewi Rekap',
            'username' => 'dewi',
        ]);

        MaterialBlockResponse::query()->create([
            'user_id' => $student->id,
            'material_id' => $material->id,
            'block_id' => 'sc-rapat-kelas',
            'block_type' => 'scenario',
            'score' => 100,
            'max_score' => 100,
            'attempts' => 1,
            'is_completed' => true,
            'last_answered_at' => now(),
        ]);

        $this->actingAs($this->admin())
            ->get('/admin/chapters/' . $chapter->getRouteKey())
            ->assertOk()
            ->assertSee('Latihan interaktif (formatif)')
            ->assertSee('Pratinjau &amp; validasi blok', false)
            ->assertSee('Dewi Rekap')
            ->assertSee('sc-rapat-kelas')
            ->assertSee('Skenario')
            ->assertSee('semua blok valid');
    }

    public function test_chapter_page_explains_when_no_blocks_were_practised(): void
    {
        $chapter = Chapter::query()
            ->whereHas('materials')
            ->firstOrFail();

        $this->actingAs($this->admin())
            ->get('/admin/chapters/' . $chapter->getRouteKey())
            ->assertOk()
            ->assertSee('Belum ada siswa yang mengerjakan blok interaktif');
    }

    public function test_export_csv_action_downloads_chapter_block_scores(): void
    {
        $material = $this->material();
        $chapter = $material->chapter;
        $student = User::factory()->create([
            'name' => 'Eko Ekspor',
            'username' => 'eko',
        ]);

        MaterialBlockResponse::query()->create([
            'user_id' => $student->id,
            'material_id' => $material->id,
            'block_id' => 'sc-rapat-kelas',
            'block_type' => 'scenario',
            'score' => 75,
            'max_score' => 100,
            'attempts' => 3,
            'is_completed' => true,
            'last_answered_at' => now(),
        ]);

        $this->actingAs($this->admin());

        Livewire::test(ViewChapter::class, ['record' => $chapter->getRouteKey()])
            ->assertActionVisible('exportBlockScores')
            ->callAction('exportBlockScores')
            ->assertFileDownloaded('skor-blok-' . $chapter->code . '.csv');
    }

    public function test_export_action_is_hidden_when_chapter_has_no_block_scores(): void
    {
        $chapter = $this->material()->chapter;

        $this->actingAs($this->admin());

        Livewire::test(ViewChapter::class, ['record' => $chapter->getRouteKey()])
            ->assertActionHidden('exportBlockScores');
    }
}