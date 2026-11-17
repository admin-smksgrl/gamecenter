<?php

namespace Tests\Unit;

use App\Services\Materi\BlockSchema;
use PHPUnit\Framework\TestCase;

/**
 * Aturan blok materi interaktif (plan-materi-interaktif §3.2) diuji langsung
 * tanpa basis data supaya pesan kesalahannya cepat diperbaiki.
 */
class BlockSchemaTest extends TestCase
{
    private BlockSchema $schema;

    protected function setUp(): void
    {
        parent::setUp();

        $this->schema = new BlockSchema;
    }

    public function test_text_and_visual_blocks_are_accepted(): void
    {
        $blocks = [
            ['type' => 'heading', 'level' => 2, 'text' => 'Judul'],
            ['type' => 'paragraph', 'text' => 'Paragraf.'],
            ['type' => 'list', 'ordered' => true, 'items' => ['Satu', 'Dua']],
            ['type' => 'table', 'rows' => [['A', 'B'], ['1', '2']]],
            ['type' => 'callout', 'tone' => 'info', 'text' => 'Catatan.'],
            ['type' => 'code', 'text' => 'echo 1;'],
            ['type' => 'diagram', 'engine' => 'mermaid', 'code' => 'flowchart LR\n A-->B'],
            ['type' => 'chart', 'kind' => 'bar', 'data' => [['label' => 'A', 'value' => 3]]],
            [
                'type' => 'hotspots',
                'id' => 'hs-1',
                'image_url' => '/media/a.png',
                'image_source' => ['book' => 'Buku.pdf', 'page' => 33],
                'caption' => 'Diagram pilar',
                'points' => [['id' => 'p1', 'x' => 0.2, 'y' => 0.5, 'label' => 'Titik']],
            ],
            ['type' => 'timeline', 'items' => [['when' => '1950', 'title' => 'Awal']]],
            ['type' => 'glossary', 'terms' => [['term' => 'Pola', 'definition' => 'Kesamaan.']]],
            ['type' => 'flashcards', 'cards' => [['front' => 'Apa?', 'back' => 'Itu.']]],
        ];

        $this->assertSame([], $this->schema->problems($blocks, 'materi'));
    }

    public function test_activity_blocks_are_accepted(): void
    {
        $feedback = ['correct' => 'Tepat.', 'wrong' => 'Coba lagi.'];

        $blocks = [
            [
                'type' => 'sort', 'id' => 'srt-1', 'prompt' => 'Urutkan.',
                'items' => [['id' => 'a', 'text' => 'A'], ['id' => 'b', 'text' => 'B']],
                'answer' => ['b', 'a'], 'feedback' => $feedback,
            ],
            [
                'type' => 'categorize', 'id' => 'cat-1', 'prompt' => 'Kelompokkan.',
                'buckets' => [['id' => 'b1', 'label' => 'Satu'], ['id' => 'b2', 'label' => 'Dua']],
                'items' => [['id' => 'i1', 'text' => 'X', 'bucket' => 'b1']],
                'feedback' => $feedback,
            ],
            [
                'type' => 'label', 'id' => 'lbl-1', 'prompt' => 'Beri label.',
                'image_url' => '/media/b.png',
                'image_source' => ['book' => 'Buku.pdf', 'page' => 7],
                'targets' => [['id' => 't1', 'x' => 0.3, 'y' => 0.4, 'answer' => 'resultan']],
                'choices' => ['resultan', 'komponen x'],
                'feedback' => $feedback,
            ],
            [
                'type' => 'checkpoint', 'id' => 'cp-1', 'question' => 'Berapa?',
                'choices' => [['id' => 'c1', 'text' => '8', 'correct' => true], ['id' => 'c2', 'text' => '6']],
                'explanation' => 'Karena 2 × 2 × 2.',
            ],
            [
                'type' => 'scenario', 'id' => 'sc-1', 'title' => 'Rapat kelas', 'start' => 'n1',
                'nodes' => [
                    ['id' => 'n1', 'text' => 'Pilih?', 'choices' => [['text' => 'Ajak diskusi', 'next' => 'n2']]],
                    ['id' => 'n2', 'text' => 'Selesai.', 'end' => true],
                ],
            ],
            [
                'type' => 'challenge', 'id' => 'ch-1', 'time_limit' => 90,
                'items' => [['question' => 'Istilah?', 'answer' => 'abstraksi']],
                'feedback' => $feedback,
            ],
        ];

        $this->assertSame([], $this->schema->problems($blocks, 'materi'));
    }

    public function test_checkpoint_must_have_exactly_one_correct_choice_and_explanation(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'checkpoint',
            'id' => 'cp-1',
            'question' => 'Pilih?',
            'choices' => [
                ['id' => 'c1', 'text' => 'A', 'correct' => true],
                ['id' => 'c2', 'text' => 'B', 'correct' => true],
            ],
        ]], 'materi');

        $this->assertContains(
            'materi.blocks[0] harus punya tepat satu pilihan benar (ditemukan 2)',
            $problems,
        );
        $this->assertContains(
            'materi.blocks[0].explanation wajib diisi agar umpan balik menjelaskan alasan',
            $problems,
        );
    }

    public function test_activity_blocks_require_id_and_feedback(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'sort',
            'prompt' => 'Urutkan.',
            'items' => [['id' => 'a', 'text' => 'A'], ['id' => 'b', 'text' => 'B']],
            'answer' => ['a', 'b'],
        ]], 'materi');

        $this->assertContains(
            'materi.blocks[0].id wajib diisi untuk blok aktivitas sort',
            $problems,
        );
        $this->assertContains(
            'materi.blocks[0].feedback wajib diisi untuk blok aktivitas',
            $problems,
        );
    }

    public function test_sort_answer_must_match_items(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'sort',
            'id' => 'srt-1',
            'prompt' => 'Urutkan.',
            'items' => [['id' => 'a', 'text' => 'A'], ['id' => 'b', 'text' => 'B']],
            'answer' => ['a', 'z'],
            'feedback' => ['correct' => 'Tepat.', 'wrong' => 'Coba lagi.'],
        ]], 'materi');

        $this->assertContains('materi.blocks[0].answer memuat id "z" yang tidak ada di items', $problems);
    }

    public function test_categorize_item_bucket_must_exist(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'categorize',
            'id' => 'cat-1',
            'prompt' => 'Kelompokkan.',
            'buckets' => [['id' => 'b1', 'label' => 'Satu'], ['id' => 'b2', 'label' => 'Dua']],
            'items' => [['id' => 'i1', 'text' => 'X', 'bucket' => 'b9']],
            'feedback' => ['correct' => 'Tepat.', 'wrong' => 'Coba lagi.'],
        ]], 'materi');

        $this->assertContains('materi.blocks[0].items[0].bucket "b9" tidak ada di buckets', $problems);
    }

    public function test_image_blocks_require_source_book_and_page(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'hotspots',
            'id' => 'hs-1',
            'image_url' => '/media/a.png',
            'caption' => 'Diagram',
            'points' => [['id' => 'p1', 'x' => 0.2, 'y' => 0.5, 'label' => 'Titik']],
        ]], 'materi');

        $this->assertContains(
            'materi.blocks[0].image_source wajib diisi (book + page asal gambar)',
            $problems,
        );
    }

    public function test_duplicate_block_ids_and_unknown_types_are_rejected(): void
    {
        $problems = $this->schema->problems([
            ['type' => 'paragraph', 'id' => 'x', 'text' => 'A'],
            ['type' => 'paragraph', 'id' => 'x', 'text' => 'B'],
            ['type' => 'video-aneh', 'text' => 'C'],
        ], 'materi');

        $this->assertContains('materi.blocks[1].id "x" dobel dalam satu materi', $problems);
        $this->assertStringContainsString('tidak dikenal', implode(' | ', $problems));
    }

    public function test_scenario_requires_valid_start_and_next_target(): void
    {
        $problems = $this->schema->problems([[
            'type' => 'scenario',
            'id' => 'sc-1',
            'title' => 'Rapat',
            'start' => 'n9',
            'nodes' => [
                ['id' => 'n1', 'text' => 'Pilih?', 'choices' => [['text' => 'Lanjut', 'next' => 'n9']]],
            ],
        ]], 'materi');

        $this->assertContains('materi.blocks[0].start harus menunjuk salah satu node', $problems);
        $this->assertContains('materi.blocks[0].nodes[0].choices[0].next "n9" tidak menunjuk node yang ada', $problems);
    }

    public function test_chart_points_need_numeric_values(): void
    {
        $problems = $this->schema->problems([
            ['type' => 'chart', 'kind' => 'bar', 'data' => [['label' => 'A', 'value' => 'banyak']]],
            ['type' => 'chart', 'kind' => 'donut', 'data' => []],
        ], 'materi');

        $this->assertContains('materi.blocks[0].data[0].value harus berupa angka', $problems);
        $this->assertContains('materi.blocks[1].kind harus bar, line, atau pie', $problems);
    }

    public function test_blocks_may_be_absent_or_null(): void
    {
        $this->assertSame([], $this->schema->problems(null, 'materi'));
        $this->assertSame(['materi.blocks harus berupa array'], $this->schema->problems('bukan array', 'materi'));
    }
}
