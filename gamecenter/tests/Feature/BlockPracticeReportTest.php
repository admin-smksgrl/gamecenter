<?php

namespace Tests\Feature;

use App\Models\LearningMaterial;
use App\Models\MaterialBlockResponse;
use App\Models\User;
use App\Services\Materi\BlockPracticeReport;
use Database\Seeders\ClassSeeder;
use Database\Seeders\EducationLevelSeeder;
use Database\Seeders\SmaSmkMaterialSeeder;
use Database\Seeders\SubjectSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

/**
 * Rekap skor blok interaktif (Fase 5): laporan siswa, rekap guru, CSV, dan
 * audit blok. Semua skor bersifat formatif dan terpisah dari sesi/rapor.
 */
class BlockPracticeReportTest extends TestCase
{
    use RefreshDatabase;

    private BlockPracticeReport $report;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seed([
            EducationLevelSeeder::class,
            ClassSeeder::class,
            SubjectSeeder::class,
            SmaSmkMaterialSeeder::class,
        ]);

        $this->report = app(BlockPracticeReport::class);
    }

    private function pancasilaMaterial(): LearningMaterial
    {
        return LearningMaterial::query()
            ->where('title', 'Menerapkan Pancasila dalam Kehidupan Berbangsa')
            ->firstOrFail();
    }

    private function mathMaterial(): LearningMaterial
    {
        return LearningMaterial::query()
            ->where('title', 'Sifat-Sifat Eksponen')
            ->firstOrFail();
    }

    private function response(User $user, LearningMaterial $material, string $blockId, string $type, int $score, int $attempts = 1): MaterialBlockResponse
    {
        return MaterialBlockResponse::query()->create([
            'user_id' => $user->id,
            'material_id' => $material->id,
            'block_id' => $blockId,
            'block_type' => $type,
            'score' => $score,
            'max_score' => 100,
            'attempts' => $attempts,
            'is_completed' => true,
            'last_answered_at' => now(),
            'first_completed_at' => now(),
        ]);
    }

    public function test_student_report_groups_scores_per_material(): void
    {
        $user = User::factory()->create();

        $this->response($user, $this->pancasilaMaterial(), 'sc-rapat-kelas', 'scenario', 100, 2);
        $this->response($user, $this->mathMaterial(), 'ch-eksponen-cepat', 'challenge', 80, 3);

        // Baris milik siswa lain tidak boleh ikut terhitung.
        $this->response(User::factory()->create(), $this->mathMaterial(), 'ch-eksponen-cepat', 'challenge', 40);

        $data = $this->report->forStudent($user);

        $this->assertSame(2, $data['totals']['blocks']);
        $this->assertSame(2, $data['totals']['completed']);
        $this->assertSame(5, $data['totals']['attempts']);
        $this->assertSame(90, $data['totals']['average_score']);

        $this->assertCount(2, $data['materials']);

        $pancasila = collect($data['materials'])->firstWhere('material_id', $this->pancasilaMaterial()->id);
        $this->assertNotNull($pancasila);
        $this->assertSame(100, $pancasila['average_score']);
        $this->assertSame('Skenario', $pancasila['block_rows'][0]['label']);
        $this->assertNotNull($pancasila['assessment_id'], 'kartu progres butuh tautan ke halaman materi');

        $labels = collect($data['materials'])
            ->flatMap(fn (array $material): array => array_column($material['block_rows'], 'label'))
            ->all();
        $this->assertContains('Tantangan kilat', $labels);
    }

    public function test_empty_student_report_has_zero_totals(): void
    {
        $data = $this->report->forStudent(User::factory()->create());

        $this->assertSame([
            'blocks' => 0,
            'completed' => 0,
            'attempts' => 0,
            'average_score' => 0,
        ], $data['totals']);
        $this->assertSame([], $data['materials']);
    }

    public function test_chapter_recap_lists_blocks_and_students(): void
    {
        $chapter = $this->pancasilaMaterial()->chapter;
        $alice = User::factory()->create(['name' => 'Alice Siswa', 'username' => 'alice']);
        $bob = User::factory()->create(['name' => 'Bob Siswa', 'username' => 'bob']);

        $this->response($alice, $this->pancasilaMaterial(), 'sc-rapat-kelas', 'scenario', 100);
        $this->response($bob, $this->pancasilaMaterial(), 'sc-rapat-kelas', 'scenario', 60);

        $recap = $this->report->forChapter($chapter);

        $this->assertSame(2, $recap['totals']['blocks']);
        $this->assertSame(2, $recap['totals']['students']);
        $this->assertSame(80, $recap['totals']['average_score']);

        $this->assertCount(1, $recap['blocks']);
        $this->assertSame('sc-rapat-kelas', $recap['blocks'][0]['block_id']);
        $this->assertSame('Skenario', $recap['blocks'][0]['label']);
        $this->assertSame(2, $recap['blocks'][0]['students']);

        $this->assertCount(2, $recap['students']);
        $this->assertSame(
            ['Alice Siswa', 'Bob Siswa'],
            collect($recap['students'])->pluck('name')->sort()->values()->all(),
        );
    }

    public function test_csv_export_contains_bom_header_and_rows(): void
    {
        $chapter = $this->pancasilaMaterial()->chapter;
        $student = User::factory()->create([
            'name' => 'Citra, Siswa',
            'username' => 'citra',
        ]);

        $this->response($student, $this->pancasilaMaterial(), 'sc-rapat-kelas', 'scenario', 100);

        $csv = $this->report->chapterCsv($chapter);

        $this->assertStringStartsWith("\xEF\xBB\xBF", $csv, 'BOM membantu Excel membaca UTF-8');
        $this->assertStringContainsString('chapter_code,chapter_title,nama_siswa,username,kelas', $csv);
        $this->assertStringContainsString($chapter->code, $csv);
        $this->assertStringContainsString('"Citra, Siswa"', $csv, 'nama dengan koma harus dikutip');
        $this->assertStringContainsString('sc-rapat-kelas', $csv);
        $this->assertStringContainsString('Skenario', $csv);
        $this->assertStringContainsString('ya', $csv);
    }

    public function test_block_audit_previews_blocks_and_flags_broken_ones(): void
    {
        $material = $this->pancasilaMaterial();
        $chapter = $material->chapter;

        $audit = $this->report->blockAudit($chapter);
        $this->assertNotEmpty($audit);
        $this->assertSame(
            [],
            collect($audit)->flatMap(fn (array $row): array => $row['problems'])->all(),
            'blok hasil impor harus lolos validasi',
        );

        $material->blocks = [
            ['type' => 'checkpoint', 'id' => 'cp-rusak', 'question' => 'Hanya pertanyaan'],
        ];
        $material->save();

        // Muat ulang relasi karena `materials` sudah ter-cache sebelum diubah.
        $broken = collect($this->report->blockAudit($chapter->fresh()))
            ->firstWhere('id', 'cp-rusak');

        $this->assertNotNull($broken);
        $this->assertNotEmpty($broken['problems']);
    }
}