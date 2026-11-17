<?php

namespace App\Services\Materi;

/**
 * Pemeriksa graf skenario bercabang (plan §4.4 & Fase 4.3).
 *
 * Skenario adalah graf: node → pilihan → node, sebagian node menjadi akhir.
 * Yang diperiksa di luar bentuk dasar:
 * - setiap node dapat dicapai dari `start` (tidak ada node mati);
 * - setiap node punya jalan menuju salah satu node akhir (tidak ada siklus
 *   tanpa ujung);
 * - id node unik, `next` menunjuk node yang ada atau ditandai `end`;
 * - jumlah node dibatasi 15 supaya skenario tetap mudah dirawat.
 *
 * Pemeriksaan ini tidak memakai Laravel/HTTP apa pun agar bisa dipakai
 * validator materi, perintah impor, dan tes unit.
 */
class ScenarioValidator
{
    /** Batas node per skenario (plan §8). */
    public const MAX_NODES = 15;

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    public function problems(array $block, string $path): array
    {
        $problems = [];

        if (! $this->filled($block['title'] ?? null)) {
            $problems[] = "{$path}.title wajib diisi";
        }

        $nodes = $block['nodes'] ?? null;

        if (! is_array($nodes) || $nodes === []) {
            return [...$problems, "{$path}.nodes harus berisi minimal satu node"];
        }

        if (count($nodes) > self::MAX_NODES) {
            $problems[] = "{$path}.nodes maksimal " . self::MAX_NODES . ' node';
        }

        $nodes = array_values($nodes);

        // Kumpulkan id lebih dulu supaya `next` bisa diperiksa per node.
        /** @var array<string, int> $indexById */
        $indexById = [];
        $duplicateAt = [];

        foreach ($nodes as $i => $node) {
            if (! is_array($node)) {
                continue;
            }

            $id = $node['id'] ?? null;

            if (! $this->filled($id)) {
                continue;
            }

            if (isset($indexById[$id])) {
                $duplicateAt[$i] = true;
                continue;
            }

            $indexById[$id] = $i;
        }

        foreach ($nodes as $i => $node) {
            $nodePath = "{$path}.nodes[{$i}]";

            if (! is_array($node)) {
                $problems[] = "{$nodePath} harus berupa objek";
                continue;
            }

            $id = $node['id'] ?? null;

            if (! $this->filled($id)) {
                $problems[] = "{$nodePath}.id wajib diisi";
            } elseif (isset($duplicateAt[$i])) {
                $problems[] = "{$nodePath}.id \"{$id}\" dobel dalam skenario";
            }

            if (! $this->filled($node['text'] ?? null)) {
                $problems[] = "{$nodePath}.text wajib diisi";
            }

            $problems = [...$problems, ...$this->nodeProblems($node, $nodePath, $indexById)];
        }

        $start = (string) ($block['start'] ?? '');

        if (! isset($indexById[$start])) {
            $problems[] = "{$path}.start harus menunjuk salah satu node";
        }

        // Tanpa daftar id yang utuh, pemeriksaan graf tidak bisa dipercaya.
        if ($problems !== [] || $indexById === []) {
            return $problems;
        }

        $graph = $this->adjacency($nodes, $indexById);
        $ends = [];

        foreach ($indexById as $id => $index) {
            if (($nodes[$index]['end'] ?? false) === true) {
                $ends[] = $id;
            }
        }

        if ($ends === []) {
            return [...$problems, "{$path}.nodes wajib punya minimal satu node akhir (end)"];
        }

        foreach ($this->unreachableFrom($start, $graph) as $id) {
            $problems[] = "{$path}.nodes[{$indexById[$id]}].id \"{$id}\" tidak dapat dicapai dari start";
        }

        foreach ($this->withoutPathToEnd($graph, $ends) as $id) {
            $problems[] = "{$path}.nodes[{$indexById[$id]}].id \"{$id}\" tidak punya jalan menuju node akhir (siklus tak berujung)";
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $node
     * @param  array<string, int>  $indexById
     * @return array<int, string>
     */
    private function nodeProblems(array $node, string $path, array $indexById): array
    {
        $problems = [];
        $isEnd = ($node['end'] ?? false) === true;
        $choices = $node['choices'] ?? null;

        if (! $isEnd && (! is_array($choices) || $choices === [])) {
            $problems[] = "{$path} harus punya minimal satu pilihan atau ditandai end";
        }

        if (! is_array($choices)) {
            return $problems;
        }

        foreach (array_values($choices) as $j => $choice) {
            $choicePath = "{$path}.choices[{$j}]";

            if (! is_array($choice) || ! $this->filled($choice['text'] ?? null)) {
                $problems[] = "{$choicePath}.text wajib diisi";
                continue;
            }

            $next = $choice['next'] ?? null;

            if ($next === null && ($choice['end'] ?? null) !== true) {
                $problems[] = "{$choicePath} harus punya next atau menandai end";
            }

            if ($next !== null && ! is_string($next)) {
                $problems[] = "{$choicePath}.next harus berupa teks id node";
            }

            if (is_string($next) && ! isset($indexById[$next])) {
                $problems[] = "{$choicePath}.next \"{$next}\" tidak menunjuk node yang ada";
            }

            if (isset($choice['score']) && ! is_numeric($choice['score'])) {
                $problems[] = "{$choicePath}.score harus berupa angka";
            }

            if (isset($choice['feedback']) && ! $this->filled($choice['feedback'])) {
                $problems[] = "{$choicePath}.feedback harus berupa teks";
            }
        }

        return $problems;
    }

    /**
     * Peta id node → daftar id tujuan. Pilihan tanpa `next` dianggap berakhir.
     *
     * @param  array<int, mixed>  $nodes
     * @param  array<string, int>  $indexById
     * @return array<string, array<int, string>>
     */
    private function adjacency(array $nodes, array $indexById): array
    {
        $graph = [];

        foreach ($indexById as $id => $index) {
            $graph[$id] = [];
            $node = $nodes[$index];

            if (! is_array($node) || ($node['end'] ?? false) === true) {
                continue;
            }

            foreach (is_array($node['choices'] ?? null) ? $node['choices'] : [] as $choice) {
                if (is_array($choice) && is_string($choice['next'] ?? null) && isset($indexById[$choice['next']])) {
                    $graph[$id][] = $choice['next'];
                }
            }
        }

        return $graph;
    }

    /**
     * @param  array<string, array<int, string>>  $graph
     * @return array<int, string>
     */
    private function unreachableFrom(string $start, array $graph): array
    {
        $seen = [$start => true];
        $queue = [$start];

        while ($queue !== []) {
            $current = array_shift($queue);

            foreach ($graph[$current] ?? [] as $next) {
                if (! isset($seen[$next])) {
                    $seen[$next] = true;
                    $queue[] = $next;
                }
            }
        }

        return array_values(array_diff(array_keys($graph), array_keys($seen)));
    }

    /**
     * Balik arah graf lalu telusuri dari node akhir. Node yang tidak tercapai
     * berarti semua jalurnya memutar (tidak pernah selesai).
     *
     * @param  array<string, array<int, string>>  $graph
     * @param  array<int, string>  $ends
     * @return array<int, string>
     */
    private function withoutPathToEnd(array $graph, array $ends): array
    {
        $reverse = [];

        foreach ($graph as $from => $targets) {
            foreach ($targets as $to) {
                $reverse[$to][] = $from;
            }
        }

        $seen = [];

        foreach ($ends as $end) {
            $seen[$end] = true;
        }

        $queue = $ends;

        while ($queue !== []) {
            $current = array_shift($queue);

            foreach ($reverse[$current] ?? [] as $previous) {
                if (! isset($seen[$previous])) {
                    $seen[$previous] = true;
                    $queue[] = $previous;
                }
            }
        }

        return array_values(array_diff(array_keys($graph), array_keys($seen)));
    }

    private function filled(mixed $value): bool
    {
        return is_string($value) && trim($value) !== '';
    }
}
