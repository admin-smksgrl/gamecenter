<?php

namespace Tests\Feature;

use Database\Seeders\ClassSeeder;
use Database\Seeders\EducationLevelSeeder;
use App\Models\Assessment;
use Database\Seeders\SmaSmkMaterialSeeder;
use Database\Seeders\SubjectSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Artisan;
use Inertia\Testing\AssertableInertia;
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

    public function test_bahasa_inggris_chapters_meet_the_plan_minimums(): void
    {
        // Enam bab Bahasa Inggris X adalah batch 11 (rilis 0.34.0). Tes ini
        // menjaga seluruh babnya tetap lengkap dan tidak menyembunyikan teks.
        foreach (['ENG 1', 'ENG 2', 'ENG 3', 'ENG 4', 'ENG 5', 'ENG 6'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_ips_chapters_meet_the_plan_minimums(): void
    {
        // Empat bab IPS X (rilis 0.35.0 dan 0.36.0) selesai: sejarah,
        // sosiologi, ekonomi, dan geografi. Tes menjaga minimum §5.3 tetap
        // terpenuhi saat isi diperbarui.
        foreach (['IPS 1', 'IPS 2', 'IPS 3', 'IPS 4'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_pjok_chapters_meet_the_plan_minimums(): void
    {
        // Delapan bab PJOK X (rilis 0.37.0 dan 0.38.0): permainan bola besar,
        // bola kecil, atletik, senam, dan gerak berirama. Tes menjaga minimum
        // §5.3 tetap terpenuhi saat isi diperbarui.
        foreach (['PJOK 1', 'PJOK 2', 'PJOK 3', 'PJOK 4', 'PJOK 5', 'PJOK 6', 'PJOK 7', 'PJOK 8'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_prakarya_chapters_meet_the_plan_minimums(): void
    {
        // Buku Prakarya Kerajinan X (rilis 0.38.0) tuntas 3/3 unit,
        // buku Prakarya Rekayasa X (rilis 0.39.0) tuntas 4/4 unit,
        // buku Prakarya Budi Daya X (rilis 0.40.0) tuntas 3/3 unit, dan
        // buku Prakarya Pengolahan X (rilis 0.41.0) tuntas 4/4 unit.
        foreach (['PRA 1', 'PRA 2', 'PRA 3', 'PRA 4', 'PRA 5', 'PRA 6', 'PRA 7', 'PRA 8', 'PRA 9', 'PRA 10', 'PRA 11', 'PRA 12', 'PRA 13', 'PRA 14'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_prakarya_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'PRA 1'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Ragam Hias Nusantara pada Produk Fesyen', $props['context']['chapter_title']);
            $this->assertSame('prakarya', $props['context']['subject_slug'] ?? 'prakarya');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_prakarya_rekayasa_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'PRA 4'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Lampu Sensor Suara', $props['context']['chapter_title']);
            $this->assertSame('prakarya', $props['context']['subject_slug'] ?? 'prakarya');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('diagram', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_prakarya_budi_daya_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'PRA 8'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Budi Daya Tanaman Pangan dan Pemanfaatan Limbahnya', $props['context']['chapter_title']);
            $this->assertSame('prakarya', $props['context']['subject_slug'] ?? 'prakarya');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('diagram', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_prakarya_pengolahan_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'PRA 11'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Bahan Pangan Nabati: Lebih Sehat dan Ramah Lingkungan', $props['context']['chapter_title']);
            $this->assertSame('prakarya', $props['context']['subject_slug'] ?? 'prakarya');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('diagram', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_ipas_chapters_meet_the_plan_minimums(): void
    {
        // Buku Projek IPAS SMK/MAK Kelas X (rilis 0.42.0) tuntas 6/6 bab.
        foreach (['IPAS 1', 'IPAS 2', 'IPAS 3', 'IPAS 4', 'IPAS 5', 'IPAS 6'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_kepercayaan_chapters_meet_the_plan_minimums(): void
    {
        // Buku Pendidikan Kepercayaan SMA/SMK Kelas X (rilis 0.43.0) tuntas 8/8 bab.
        foreach (['KEP 1', 'KEP 2', 'KEP 3', 'KEP 4', 'KEP 5', 'KEP 6', 'KEP 7', 'KEP 8'] as $code) {
            $row = $this->coverage($code)['chapters'][0];

            $this->assertTrue(
                $row['complete'],
                "{$code} belum memenuhi §5.3: " . implode(', ', $row['missing']),
            );
            $this->assertSame(0, $row['hidden'], "{$code} menyembunyikan isi materi");
            $this->assertGreaterThan(0, $row['theory'], "{$code} tidak punya blok teks");
            $this->assertGreaterThanOrEqual(1, $row['visual'], "{$code} tidak punya blok visual");
            $this->assertGreaterThanOrEqual(2, $row['activities'], "{$code} butuh dua blok aktivitas");
            $this->assertGreaterThanOrEqual(1, $row['scenario'], "{$code} butuh skenario atau tantangan");
            $this->assertGreaterThanOrEqual(1, $row['recall'], "{$code} butuh glossary atau flashcards");
            $this->assertGreaterThanOrEqual(
                $row['required_checkpoints'],
                $row['checkpoints'],
                "{$code} butuh {$row['required_checkpoints']} checkpoint",
            );
        }
    }

    public function test_kepercayaan_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'KEP 1'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Sejarah Kepercayaan terhadap Tuhan Yang Maha Esa', $props['context']['chapter_title']);
            $this->assertSame('kepercayaan', $props['context']['subject_slug'] ?? 'kepercayaan');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('diagram', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_ipas_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'IPAS 1'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Mengatasi Masalah Lingkungan Melalui Projek IPAS', $props['context']['chapter_title']);
            $this->assertSame('ipas', $props['context']['subject_slug'] ?? 'ipas');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('diagram', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_pjok_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'PJOK 1'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Permainan Bola Basket', $props['context']['chapter_title']);
            $this->assertSame('pjok', $props['context']['subject_slug'] ?? 'pjok');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_ips_play_page_serves_three_materials_and_five_easy_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'IPS 1'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Manusia, Ruang, dan Waktu', $props['context']['chapter_title']);
            $this->assertSame('ips', $props['context']['subject_slug'] ?? 'ips');
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $types = array_column($first['blocks'], 'type');

            $this->assertContains('glossary', $types);
            $this->assertContains('checkpoint', $types);
        });
    }

    public function test_eng_6_play_page_serves_material_blocks_and_questions(): void
    {
        $assessment = Assessment::query()
            ->whereHas('chapter', fn ($query) => $query->where('code', 'ENG 6'))
            ->where('difficulty', 'easy')
            ->firstOrFail();

        $response = $this->get("/main/{$assessment->id}");

        $response->assertOk();
        $response->assertInertia(function (AssertableInertia $page) {
            $props = $page->toArray()['props'];

            $this->assertSame('Fractured Stories', $props['context']['chapter_title']);
            $this->assertCount(5, $props['questions']);
            $this->assertCount(3, $props['materials']);

            $first = $props['materials'][0];
            $this->assertNotEmpty($first['blocks'], 'materi ENG 6 harus tampil sebagai blok');
            $this->assertContains('glossary', array_column($first['blocks'], 'type'));
            $this->assertContains('checkpoint', array_column($first['blocks'], 'type'));
        });
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