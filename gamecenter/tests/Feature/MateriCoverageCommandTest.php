<?php

namespace Tests\Feature;

use Database\Seeders\ClassSeeder;
use Database\Seeders\EducationLevelSeeder;
use Database\Seeders\SmaSmkMaterialSeeder;
use Database\Seeders\SubjectSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Artisan;
use Tests\TestCase;

class MateriCoverageCommandTest extends TestCase
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
    }

    /**
     * @return array<string, mixed>
     */
    private function coverage(string $chapter): array
    {
        Artisan::call('gamecenter:materi-coverage', [
            '--chapter' => $chapter,
            '--json' => true,
        ]);

        return json_decode(Artisan::output(), true, 512, JSON_THROW_ON_ERROR);
    }

    public function test_converted_chapter_meets_the_plan_minimums(): void
    {
        foreach (['PAN 1', 'MA 1.1', 'MA 6.1', 'INF 1', 'FIS 1'] as $code) {
            $data = $this->coverage($code);
            $row = $data['chapters'][0];

            $this->assertSame($code, $row['code']);
            $this->assertTrue($row['complete'], "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']));
            $this->assertGreaterThanOrEqual(1, $row['visual']);
            $this->assertGreaterThanOrEqual(2, $row['activities']);
            $this->assertGreaterThanOrEqual(1, $row['scenario']);
            $this->assertGreaterThanOrEqual(1, $row['recall']);
            $this->assertGreaterThanOrEqual($row['required_checkpoints'], $row['checkpoints']);
            // Renderer memilih blok ATAU markdown: materi berblok wajib
            // membawa teks aslinya sebagai blok teks.
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
        }
    }

    public function test_pemdas_chapter_from_curated_seeder_stays_interactive(): void
    {
        // PEMDAS 1.1 ditulis langsung di CuratedContentSeeder (bukan JSON fase-e),
        // jadi tidak tercakup MateriContentFidelityTest. Tes ini menjaganya tetap
        // punya blok teks sekaligus memenuhi minimum §5.3.
        $this->seed(\Database\Seeders\CuratedContentSeeder::class);

        $data = $this->coverage('PEMDAS 1.1');
        $row = $data['chapters'][0];

        $this->assertSame(2, $row['materials']);
        $this->assertTrue($row['complete'], 'PEMDAS 1.1 belum memenuhi §5.3: ' . implode(', ', $row['missing']));
        $this->assertGreaterThan(0, $row['theory'], 'PEMDAS 1.1 tidak punya blok teks');
        $this->assertSame(0, $row['hidden'], 'PEMDAS 1.1 menyembunyikan isi materi');
        $this->assertGreaterThanOrEqual(1, $row['visual']);
        $this->assertGreaterThanOrEqual(2, $row['activities']);
        $this->assertGreaterThanOrEqual(1, $row['scenario']);
        $this->assertGreaterThanOrEqual(1, $row['recall']);
        $this->assertGreaterThanOrEqual($row['required_checkpoints'], $row['checkpoints']);
    }

    public function test_unconverted_chapter_lists_missing_components(): void
    {
        // Konversi §5.3 berjalan bertahap: tes memilih chapter pertama yang
        // belum lengkap, bukan kode tertentu, supaya tidak terus berubah.
        Artisan::call('gamecenter:materi-coverage', [
            '--json' => true,
            '--only-incomplete' => true,
        ]);
        $incomplete = json_decode(Artisan::output(), true, 512, JSON_THROW_ON_ERROR);

        if ($incomplete['chapters'] === []) {
            $this->markTestSkipped('Seluruh chapter sudah memenuhi minimum §5.3.');
        }

        $row = $incomplete['chapters'][0];

        $this->assertFalse($row['complete']);
        $this->assertNotEmpty($row['missing']);
        $this->assertGreaterThan(0, $row['blocks'] + count($row['missing']));
    }

    public function test_only_incomplete_filter_and_summary_counts(): void
    {
        Artisan::call('gamecenter:materi-coverage', ['--json' => true]);
        $all = json_decode(Artisan::output(), true, 512, JSON_THROW_ON_ERROR);

        $this->assertGreaterThanOrEqual(5, $all['summary']['complete']);
        $this->assertSame(count($all['chapters']), $all['summary']['chapters']);

        Artisan::call('gamecenter:materi-coverage', [
            '--json' => true,
            '--only-incomplete' => true,
        ]);
        $incomplete = json_decode(Artisan::output(), true, 512, JSON_THROW_ON_ERROR);

        $this->assertLessThan($all['summary']['chapters'], count($incomplete['chapters']));
        $this->assertSame([], array_filter(
            $incomplete['chapters'],
            fn (array $row): bool => $row['complete'],
        ));
    }
}