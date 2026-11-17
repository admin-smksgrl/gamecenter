<?php

namespace Tests\Unit;

use App\Services\Materi\ScenarioValidator;
use PHPUnit\Framework\TestCase;

class ScenarioValidatorTest extends TestCase
{
    private ScenarioValidator $validator;

    protected function setUp(): void
    {
        parent::setUp();
        $this->validator = new ScenarioValidator;
    }

    /** @return array<string, mixed> */
    private function validScenario(): array
    {
        return [
            'type' => 'scenario',
            'id' => 'sc-1',
            'title' => 'Rapat kelas',
            'start' => 'n1',
            'nodes' => [
                [
                    'id' => 'n1',
                    'text' => 'Usulmu berbeda. Apa yang kamu lakukan?',
                    'choices' => [
                        ['text' => 'Mendengar dulu', 'next' => 'n2', 'score' => 2, 'feedback' => 'Baik.'],
                        ['text' => 'Memaksa', 'next' => 'n3', 'score' => 0],
                    ],
                ],
                [
                    'id' => 'n2',
                    'text' => 'Ketua kelas mengajak voting.',
                    'choices' => [
                        ['text' => 'Musyawarah', 'next' => 'n4', 'score' => 2],
                        ['text' => 'Voting cepat', 'next' => 'n5', 'score' => 1],
                    ],
                ],
                [
                    'id' => 'n3',
                    'text' => 'Suasana memanas.',
                    'choices' => [
                        ['text' => 'Minta maaf', 'next' => 'n2', 'score' => 1],
                        ['text' => 'Keluar ruangan', 'next' => 'n6', 'score' => 0],
                    ],
                ],
                ['id' => 'n4', 'text' => 'Sepakat bersama.', 'end' => true, 'outcome' => 'good'],
                ['id' => 'n5', 'text' => 'Cepat tetapi kecewa.', 'end' => true, 'outcome' => 'neutral'],
                ['id' => 'n6', 'text' => 'Rapat gagal.', 'end' => true, 'outcome' => 'bad'],
            ],
        ];
    }

    public function test_valid_scenario_has_no_problems(): void
    {
        $this->assertSame([], $this->validator->problems($this->validScenario(), 'materi.blocks[0]'));
    }

    public function test_choice_without_next_or_end_is_rejected(): void
    {
        $scenario = $this->validScenario();
        $scenario['nodes'][0]['choices'][0] = ['text' => 'Bingung'];

        $problems = $this->validator->problems($scenario, 'materi.blocks[0]');

        $this->assertContains(
            'materi.blocks[0].nodes[0].choices[0] harus punya next atau menandai end',
            $problems,
        );
    }

    public function test_unknown_next_target_is_rejected(): void
    {
        $scenario = $this->validScenario();
        $scenario['nodes'][1]['choices'][1]['next'] = 'n99';

        $this->assertContains(
            'materi.blocks[0].nodes[1].choices[1].next "n99" tidak menunjuk node yang ada',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_node_unreachable_from_start_is_reported(): void
    {
        $scenario = $this->validScenario();
        $scenario['nodes'][] = ['id' => 'n7', 'text' => 'Tersembunyi.', 'end' => true];

        $this->assertContains(
            'materi.blocks[0].nodes[6].id "n7" tidak dapat dicapai dari start',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_scenario_without_any_end_is_reported(): void
    {
        // n1 ↔ n2 berputar dan tidak ada node yang ditandai end.
        $scenario = [
            'title' => 'Berputar',
            'start' => 'n1',
            'nodes' => [
                ['id' => 'n1', 'text' => 'A.', 'choices' => [['text' => 'Ke B', 'next' => 'n2']]],
                ['id' => 'n2', 'text' => 'B.', 'choices' => [['text' => 'Ke A', 'next' => 'n1']]],
            ],
        ];

        $this->assertContains(
            'materi.blocks[0].nodes wajib punya minimal satu node akhir (end)',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_loop_nodes_without_path_to_end_are_reported(): void
    {
        $scenario = $this->validScenario();
        // n3 diperpanjang dengan lingkaran n7 ↔ n8, sementara n4 tetap akhir.
        $scenario['nodes'][2]['choices'][] = ['text' => 'Putar', 'next' => 'n7'];
        $scenario['nodes'][] = [
            'id' => 'n7',
            'text' => 'Lingkaran A.',
            'choices' => [['text' => 'Ke B', 'next' => 'n8']],
        ];
        $scenario['nodes'][] = [
            'id' => 'n8',
            'text' => 'Lingkaran B.',
            'choices' => [['text' => 'Ke A', 'next' => 'n7']],
        ];

        $problems = $this->validator->problems($scenario, 'materi.blocks[0]');

        $this->assertContains(
            'materi.blocks[0].nodes[6].id "n7" tidak punya jalan menuju node akhir (siklus tak berujung)',
            $problems,
        );
        $this->assertContains(
            'materi.blocks[0].nodes[7].id "n8" tidak punya jalan menuju node akhir (siklus tak berujung)',
            $problems,
        );
    }

    public function test_duplicate_node_id_is_rejected(): void
    {
        $scenario = $this->validScenario();
        $scenario['nodes'][1]['id'] = 'n1';

        $this->assertContains(
            'materi.blocks[0].nodes[1].id "n1" dobel dalam skenario',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_node_without_exit_must_be_end(): void
    {
        $scenario = $this->validScenario();
        $scenario['nodes'][1]['choices'] = [];

        $this->assertContains(
            'materi.blocks[0].nodes[1] harus punya minimal satu pilihan atau ditandai end',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_more_than_fifteen_nodes_is_rejected(): void
    {
        $scenario = [
            'title' => 'Terlalu panjang',
            'start' => 'n1',
            'nodes' => [],
        ];

        for ($i = 1; $i <= 16; $i++) {
            $scenario['nodes'][] = [
                'id' => "n{$i}",
                'text' => "Node {$i}",
                'choices' => $i === 16
                    ? [['text' => 'Selesai', 'end' => true]]
                    : [['text' => 'Lanjut', 'next' => 'n' . ($i + 1)]],
            ];
        }

        $this->assertContains(
            'materi.blocks[0].nodes maksimal 15 node',
            $this->validator->problems($scenario, 'materi.blocks[0]'),
        );
    }

    public function test_missing_start_and_empty_nodes_are_rejected(): void
    {
        $problems = $this->validator->problems(
            ['title' => 'Kosong', 'start' => 'n1', 'nodes' => []],
            'materi.blocks[0]',
        );

        $this->assertSame(
            ['materi.blocks[0].nodes harus berisi minimal satu node'],
            $problems,
        );
    }
}