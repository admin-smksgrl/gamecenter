<?php

namespace App\Services\Materi;

/**
 * Pemeriksa skema `blocks` materi interaktif (plan-materi-interaktif §3.2).
 *
 * Dipisah dari `MateriSchema` supaya aturan blok bisa diuji sendiri dan tidak
 * membuat pemeriksa materi utama membengkak. Semua masalah dikembalikan
 * sebagai daftar teks; daftar kosong berarti valid.
 */
class BlockSchema
{
    public function __construct(
        private readonly ScenarioValidator $scenarios = new ScenarioValidator,
    ) {}

    /**
     * Tipe blok yang dikenal renderer. Harus sama dengan union
     * `MaterialBlock` di `resources/js/lib/material/blocks.ts`.
     *
     * @var array<int, string>
     */
    public const TYPES = [
        'heading',
        'paragraph',
        'list',
        'table',
        'callout',
        'code',
        'diagram',
        'chart',
        'hotspots',
        'timeline',
        'glossary',
        'flashcards',
        'sort',
        'categorize',
        'label',
        'checkpoint',
        'scenario',
        'challenge',
    ];

    /**
     * Blok aktivitas wajib punya umpan balik dan tidak menentukan skor sesi.
     *
     * @var array<int, string>
     */
    public const ACTIVITY_TYPES = [
        'sort',
        'categorize',
        'label',
        'checkpoint',
        'scenario',
        'challenge',
    ];

    /**
     * Blok yang menampilkan gambar hasil ekstraksi PDF wajib mencantumkan
     * `image_source` (book + page) agar dapat diaudit (plan §6.0).
     *
     * @var array<int, string>
     */
    private const IMAGE_TYPES = ['hotspots', 'label'];

    /**
     * Batas maksimum node skenario (plan §8), dipakai juga oleh
     * `ScenarioValidator`.
     */
    public const MAX_SCENARIO_NODES = ScenarioValidator::MAX_NODES;

    /**
     * @return array<int, string>
     */
    public function problems(mixed $blocks, string $path): array
    {
        if ($blocks === null) {
            return [];
        }

        if (! is_array($blocks)) {
            return ["{$path}.blocks harus berupa array"];
        }

        $problems = [];
        $seenIds = [];

        foreach (array_values($blocks) as $i => $block) {
            $blockPath = "{$path}.blocks[{$i}]";

            if (! is_array($block)) {
                $problems[] = "{$blockPath} harus berupa objek";
                continue;
            }

            $type = (string) ($block['type'] ?? '');

            if (! in_array($type, self::TYPES, true)) {
                $problems[] = "{$blockPath}.type \"{$type}\" tidak dikenal (pilihan: " . implode(', ', self::TYPES) . ')';
                continue;
            }

            $id = $block['id'] ?? null;

            if ($id !== null) {
                if (! is_string($id) || trim($id) === '') {
                    $problems[] = "{$blockPath}.id harus berupa teks";
                } elseif (isset($seenIds[$id])) {
                    $problems[] = "{$blockPath}.id \"{$id}\" dobel dalam satu materi";
                } else {
                    $seenIds[$id] = true;
                }
            } elseif (in_array($type, self::ACTIVITY_TYPES, true)) {
                // Blok aktivitas dinilai & disinkronkan per id, jadi id wajib.
                $problems[] = "{$blockPath}.id wajib diisi untuk blok aktivitas {$type}";
            }

            $problems = [...$problems, ...$this->typeProblems($type, $block, $blockPath)];
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function typeProblems(string $type, array $block, string $path): array
    {
        $problems = match ($type) {
            'heading' => $this->headingProblems($block, $path),
            'paragraph', 'callout', 'code' => $this->textProblems($block, $path),
            'list' => $this->listProblems($block, $path),
            'table' => $this->tableProblems($block, $path),
            'diagram' => $this->diagramProblems($block, $path),
            'chart' => $this->chartProblems($block, $path),
            'hotspots' => $this->hotspotsProblems($block, $path),
            'timeline' => $this->timelineProblems($block, $path),
            'glossary' => $this->glossaryProblems($block, $path),
            'flashcards' => $this->flashcardsProblems($block, $path),
            'sort' => $this->sortProblems($block, $path),
            'categorize' => $this->categorizeProblems($block, $path),
            'label' => $this->labelProblems($block, $path),
            'checkpoint' => $this->checkpointProblems($block, $path),
            'scenario' => $this->scenarioProblems($block, $path),
            'challenge' => $this->challengeProblems($block, $path),
            default => [],
        };

        if (in_array($type, self::IMAGE_TYPES, true)) {
            $problems = [...$problems, ...$this->imageProblems($block, $path)];
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function headingProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'text', $path);

        $level = $block['level'] ?? null;

        if ($level !== null && (! is_int($level) || $level < 2 || $level > 4)) {
            $problems[] = "{$path}.level harus bilangan bulat 2..4";
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function textProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'text', $path);
        $tone = $block['tone'] ?? null;

        if ($tone !== null && ! in_array($tone, ['info', 'success', 'warn', 'danger'], true)) {
            $problems[] = "{$path}.tone \"{$tone}\" tidak dikenal (pilihan: info, success, warn, danger)";
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function listProblems(array $block, string $path): array
    {
        $items = $block['items'] ?? null;

        if (! is_array($items) || $items === []) {
            return ["{$path}.items harus berisi minimal satu butir"];
        }

        $problems = [];

        foreach (array_values($items) as $i => $item) {
            if (! $this->filled($item)) {
                $problems[] = "{$path}.items[{$i}] harus berupa teks";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function tableProblems(array $block, string $path): array
    {
        $rows = $block['rows'] ?? null;

        if (! is_array($rows) || count($rows) < 2) {
            return ["{$path}.rows harus berisi minimal dua baris (header + isi)"];
        }

        $problems = [];
        $width = null;

        foreach (array_values($rows) as $i => $row) {
            if (! is_array($row) || $row === []) {
                $problems[] = "{$path}.rows[{$i}] harus berupa array sel";
                continue;
            }

            $width ??= count($row);

            if (count($row) !== $width) {
                $problems[] = "{$path}.rows[{$i}] harus berisi {$width} sel seperti baris pertama";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function diagramProblems(array $block, string $path): array
    {
        $problems = [];

        $engine = (string) ($block['engine'] ?? '');

        if (! in_array($engine, ['mermaid', 'svg'], true)) {
            $problems[] = "{$path}.engine harus \"mermaid\" atau \"svg\"";
        }

        $problems = [...$problems, ...$this->requiredText($block, 'code', $path)];

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function chartProblems(array $block, string $path): array
    {
        $problems = [];

        $kind = (string) ($block['kind'] ?? '');

        if (! in_array($kind, ['bar', 'line', 'pie'], true)) {
            $problems[] = "{$path}.kind harus bar, line, atau pie";
        }

        $data = $block['data'] ?? null;

        if (! is_array($data) || $data === []) {
            return [...$problems, "{$path}.data harus berisi minimal satu titik"];
        }

        foreach (array_values($data) as $i => $point) {
            if (! is_array($point)) {
                $problems[] = "{$path}.data[{$i}] harus berupa objek";
                continue;
            }

            if (! $this->filled($point['label'] ?? null)) {
                $problems[] = "{$path}.data[{$i}].label wajib diisi";
            }

            if (! is_numeric($point['value'] ?? null)) {
                $problems[] = "{$path}.data[{$i}].value harus berupa angka";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function hotspotsProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'image_url', $path);
        $points = $block['points'] ?? null;

        if (! is_array($points) || $points === []) {
            return [...$problems, "{$path}.points harus berisi minimal satu titik"];
        }

        if (! $this->filled($block['caption'] ?? null)) {
            // Plan §4.1: setiap blok visual wajib punya caption/teks alternatif.
            $problems[] = "{$path}.caption wajib diisi sebagai teks alternatif";
        }

        foreach (array_values($points) as $i => $point) {
            $pointPath = "{$path}.points[{$i}]";

            if (! is_array($point)) {
                $problems[] = "{$pointPath} harus berupa objek";
                continue;
            }

            if (! $this->filled($point['id'] ?? null)) {
                $problems[] = "{$pointPath}.id wajib diisi";
            }

            if (! $this->filled($point['label'] ?? null)) {
                $problems[] = "{$pointPath}.label wajib diisi";
            }

            foreach (['x', 'y'] as $axis) {
                $value = $point[$axis] ?? null;

                if (! is_numeric($value) || (float) $value < 0 || (float) $value > 1) {
                    $problems[] = "{$pointPath}.{$axis} harus angka 0..1 (ternormalisasi)";
                }
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function timelineProblems(array $block, string $path): array
    {
        $items = $block['items'] ?? null;

        if (! is_array($items) || $items === []) {
            return ["{$path}.items harus berisi minimal satu kejadian"];
        }

        $problems = [];

        foreach (array_values($items) as $i => $item) {
            if (! is_array($item)) {
                $problems[] = "{$path}.items[{$i}] harus berupa objek";
                continue;
            }

            foreach (['when', 'title'] as $key) {
                if (! $this->filled($item[$key] ?? null)) {
                    $problems[] = "{$path}.items[{$i}].{$key} wajib diisi";
                }
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function glossaryProblems(array $block, string $path): array
    {
        $terms = $block['terms'] ?? null;

        if (! is_array($terms) || $terms === []) {
            return ["{$path}.terms harus berisi minimal satu istilah"];
        }

        $problems = [];

        foreach (array_values($terms) as $i => $term) {
            if (! is_array($term)) {
                $problems[] = "{$path}.terms[{$i}] harus berupa objek";
                continue;
            }

            foreach (['term', 'definition'] as $key) {
                if (! $this->filled($term[$key] ?? null)) {
                    $problems[] = "{$path}.terms[{$i}].{$key} wajib diisi";
                }
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function flashcardsProblems(array $block, string $path): array
    {
        $cards = $block['cards'] ?? null;

        if (! is_array($cards) || $cards === []) {
            return ["{$path}.cards harus berisi minimal satu kartu"];
        }

        $problems = [];

        foreach (array_values($cards) as $i => $card) {
            if (! is_array($card)) {
                $problems[] = "{$path}.cards[{$i}] harus berupa objek";
                continue;
            }

            foreach (['front', 'back'] as $key) {
                if (! $this->filled($card[$key] ?? null)) {
                    $problems[] = "{$path}.cards[{$i}].{$key} wajib diisi";
                }
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function sortProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'prompt', $path);
        $problems = [...$problems, ...$this->feedbackProblems($block, $path)];

        $items = $block['items'] ?? null;

        if (! is_array($items) || count($items) < 2) {
            return [...$problems, "{$path}.items harus berisi minimal dua butir"];
        }

        $ids = [];

        foreach (array_values($items) as $i => $item) {
            if (! is_array($item) || ! $this->filled($item['id'] ?? null) || ! $this->filled($item['text'] ?? null)) {
                $problems[] = "{$path}.items[{$i}] wajib punya id dan text";
                continue;
            }

            $ids[] = (string) $item['id'];
        }

        $answer = $block['answer'] ?? null;

        if (! is_array($answer)) {
            return [...$problems, "{$path}.answer harus berupa array id yang benar"];
        }

        $answer = array_map(fn ($id) => (string) $id, array_values($answer));

        if (count($answer) !== count($ids)) {
            $problems[] = "{$path}.answer harus berisi semua id butir (" . count($ids) . ' id)';
        }

        if ($ids !== [] && count(array_unique($ids)) !== count($ids)) {
            $problems[] = "{$path}.items punya id dobel";
        }

        foreach ($answer as $id) {
            if (! in_array($id, $ids, true)) {
                $problems[] = "{$path}.answer memuat id \"{$id}\" yang tidak ada di items";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function categorizeProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'prompt', $path);
        $problems = [...$problems, ...$this->feedbackProblems($block, $path)];

        $buckets = $block['buckets'] ?? null;

        if (! is_array($buckets) || count($buckets) < 2) {
            return [...$problems, "{$path}.buckets harus berisi minimal dua keranjang"];
        }

        $bucketIds = [];

        foreach (array_values($buckets) as $i => $bucket) {
            if (! is_array($bucket) || ! $this->filled($bucket['id'] ?? null) || ! $this->filled($bucket['label'] ?? null)) {
                $problems[] = "{$path}.buckets[{$i}] wajib punya id dan label";
                continue;
            }

            $bucketIds[] = (string) $bucket['id'];
        }

        $items = $block['items'] ?? null;

        if (! is_array($items) || $items === []) {
            return [...$problems, "{$path}.items harus berisi minimal satu butir"];
        }

        foreach (array_values($items) as $i => $item) {
            $itemPath = "{$path}.items[{$i}]";

            if (! is_array($item) || ! $this->filled($item['id'] ?? null) || ! $this->filled($item['text'] ?? null)) {
                $problems[] = "{$itemPath} wajib punya id dan text";
                continue;
            }

            $bucket = (string) ($item['bucket'] ?? '');

            if (! in_array($bucket, $bucketIds, true)) {
                $problems[] = "{$itemPath}.bucket \"{$bucket}\" tidak ada di buckets";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function labelProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'prompt', $path);
        $problems = [...$problems, ...$this->requiredText($block, 'image_url', $path)];
        $problems = [...$problems, ...$this->feedbackProblems($block, $path)];

        $targets = $block['targets'] ?? null;
        $choices = $block['choices'] ?? null;

        if (! is_array($targets) || $targets === []) {
            $problems[] = "{$path}.targets harus berisi minimal satu titik";
        }

        if (! is_array($choices) || $choices === []) {
            $problems[] = "{$path}.choices harus berisi minimal satu label";
        }

        $choiceValues = is_array($choices)
            ? array_map(fn ($choice) => (string) $choice, array_values($choices))
            : [];

        foreach (is_array($targets) ? array_values($targets) : [] as $i => $target) {
            $targetPath = "{$path}.targets[{$i}]";

            if (! is_array($target)) {
                $problems[] = "{$targetPath} harus berupa objek";
                continue;
            }

            if (! $this->filled($target['id'] ?? null)) {
                $problems[] = "{$targetPath}.id wajib diisi";
            }

            foreach (['x', 'y'] as $axis) {
                $value = $target[$axis] ?? null;

                if (! is_numeric($value) || (float) $value < 0 || (float) $value > 1) {
                    $problems[] = "{$targetPath}.{$axis} harus angka 0..1 (ternormalisasi)";
                }
            }

            $answer = (string) ($target['answer'] ?? '');

            if (! in_array($answer, $choiceValues, true)) {
                $problems[] = "{$targetPath}.answer \"{$answer}\" tidak ada di choices";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function checkpointProblems(array $block, string $path): array
    {
        $problems = $this->requiredText($block, 'question', $path);

        $choices = $block['choices'] ?? null;

        if (! is_array($choices) || count($choices) < 2) {
            return [...$problems, "{$path}.choices harus berisi minimal dua pilihan"];
        }

        $correct = 0;

        foreach (array_values($choices) as $i => $choice) {
            if (! is_array($choice) || ! $this->filled($choice['id'] ?? null) || ! $this->filled($choice['text'] ?? null)) {
                $problems[] = "{$path}.choices[{$i}] wajib punya id dan text";
                continue;
            }

            if (($choice['correct'] ?? false) === true) {
                $correct++;
            }
        }

        if ($correct !== 1) {
            $problems[] = "{$path} harus punya tepat satu pilihan benar (ditemukan {$correct})";
        }

        // Plan §4.3: umpan balik wajib menjelaskan mengapa, bukan hanya benar/salah.
        if (! $this->filled($block['explanation'] ?? null)) {
            $problems[] = "{$path}.explanation wajib diisi agar umpan balik menjelaskan alasan";
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function scenarioProblems(array $block, string $path): array
    {
        // Aturan graf (reachability, siklus tak berujung, batas node) ada di
        // kelas tersendiri supaya bisa diuji tanpa membangun blok lain.
        return $this->scenarios->problems($block, $path);
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function challengeProblems(array $block, string $path): array
    {
        $problems = $this->feedbackProblems($block, $path);

        $limit = $block['time_limit'] ?? null;

        if ($limit !== null && (! is_int($limit) || $limit < 10 || $limit > 600)) {
            $problems[] = "{$path}.time_limit harus bilangan bulat 10..600 detik";
        }

        $items = $block['items'] ?? null;

        if (! is_array($items) || $items === []) {
            return [...$problems, "{$path}.items harus berisi minimal satu butir"];
        }

        foreach (array_values($items) as $i => $item) {
            if (! is_array($item)) {
                $problems[] = "{$path}.items[{$i}] harus berupa objek";
                continue;
            }

            foreach (['question', 'answer'] as $key) {
                if (! $this->filled($item[$key] ?? null)) {
                    $problems[] = "{$path}.items[{$i}].{$key} wajib diisi";
                }
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function imageProblems(array $block, string $path): array
    {
        $source = $block['image_source'] ?? null;

        if (! is_array($source)) {
            return ["{$path}.image_source wajib diisi (book + page asal gambar)"];
        }

        $problems = [];

        if (! $this->filled($source['book'] ?? null)) {
            $problems[] = "{$path}.image_source.book wajib diisi";
        }

        if (! is_int($source['page'] ?? null) || $source['page'] < 1) {
            $problems[] = "{$path}.image_source.page harus nomor halaman >= 1";
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function feedbackProblems(array $block, string $path): array
    {
        $feedback = $block['feedback'] ?? null;

        if (! is_array($feedback)) {
            return ["{$path}.feedback wajib diisi untuk blok aktivitas"];
        }

        $problems = [];

        foreach (['correct', 'wrong'] as $key) {
            if (! $this->filled($feedback[$key] ?? null)) {
                $problems[] = "{$path}.feedback.{$key} wajib diisi";
            }
        }

        return $problems;
    }

    /**
     * @param  array<string, mixed>  $block
     * @return array<int, string>
     */
    private function requiredText(array $block, string $key, string $path): array
    {
        return $this->filled($block[$key] ?? null)
            ? []
            : ["{$path}.{$key} wajib diisi"];
    }

    private function filled(mixed $value): bool
    {
        return is_string($value) && trim($value) !== '';
    }
}
