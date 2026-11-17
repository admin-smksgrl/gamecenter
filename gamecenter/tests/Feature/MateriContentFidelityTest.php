<?php

namespace Tests\Feature;

use Tests\TestCase;

/**
 * Penjaga fidelitas isi materi (plan §5.3: "teks asli dipertahankan 100%").
 *
 * `MaterialViewer` merender `blocks` **atau** markdown, bukan keduanya. Jadi
 * begitu sebuah materi punya blok, seluruh isi `content` harus sudah
 * dipindahkan ke blok teks — kalau tidak, materi kehilangan penjelasannya di
 * layar siswa (pernah terjadi pada 79 materi).
 */
class MateriContentFidelityTest extends TestCase
{
    /** @var array<int, string> */
    private const TEXT_TYPES = ['heading', 'paragraph', 'list', 'table', 'callout', 'code'];

    public function test_materi_berblok_selalu_menampilkan_teks_aslinya(): void
    {
        $problems = [];

        foreach ($this->materials() as $label => $material) {
            $blocks = $material['blocks'] ?? [];

            if ($blocks === []) {
                continue;
            }

            $contentWords = $this->wordCount((string) ($material['content'] ?? ''));
            $textBlocks = array_values(array_filter(
                $blocks,
                fn ($block): bool => is_array($block) && in_array($block['type'] ?? '', self::TEXT_TYPES, true),
            ));

            if ($contentWords >= 100 && $textBlocks === []) {
                $problems[] = "{$label}: punya blok tetapi tidak punya blok teks — isi materi tidak akan tampil";

                continue;
            }

            if ($contentWords < 100) {
                continue;
            }

            $textWords = $this->blocksWordCount($textBlocks);

            if ($textWords < (int) floor($contentWords * 0.7)) {
                $problems[] = "{$label}: blok teks hanya {$textWords} kata, konten asli {$contentWords} kata";
            }
        }

        $this->assertSame([], $problems, "Materi kehilangan teks:\n" . implode("\n", $problems));
    }

    /**
     * Setiap judul `##`/`###` pada markdown harus muncul sebagai blok judul,
     * supaya struktur materi tidak hilang saat dikonversi.
     */
    public function test_judul_markdown_terwakili_sebagai_blok_judul(): void
    {
        $problems = [];

        foreach ($this->materials() as $label => $material) {
            $blocks = $material['blocks'] ?? [];

            if ($blocks === []) {
                continue;
            }

            $contentWords = $this->wordCount((string) ($material['content'] ?? ''));

            if ($contentWords < 100) {
                continue;
            }

            $headings = [];

            foreach ($blocks as $block) {
                if (is_array($block) && ($block['type'] ?? '') === 'heading') {
                    $headings[] = $this->normalize((string) ($block['text'] ?? ''));
                }
            }

            preg_match_all('/^#{2,4}\s+(.+)$/mu', (string) ($material['content'] ?? ''), $matches);

            foreach ($matches[1] ?? [] as $heading) {
                $wanted = $this->normalize($heading);

                if ($wanted === '') {
                    continue;
                }

                if (! in_array($wanted, $headings, true)) {
                    $problems[] = "{$label}: judul \"{$heading}\" tidak ada di blok";
                }
            }
        }

        $this->assertSame([], $problems, "Judul materi hilang:\n" . implode("\n", array_slice($problems, 0, 30)));
    }

    /**
     * @return array<string, array<string, mixed>>
     */
    private function materials(): array
    {
        $root = database_path('seeders/data/sma-smk/fase-e');
        $materials = [];

        $iterator = new \RecursiveIteratorIterator(new \RecursiveDirectoryIterator($root));

        foreach ($iterator as $file) {
            if ($file->getExtension() !== 'json') {
                continue;
            }

            $path = str_replace('\\', '/', $file->getPathname());
            $relative = str_replace(str_replace('\\', '/', $root) . '/', '', $path);
            $data = json_decode((string) file_get_contents($path), true);

            foreach ($data['chapters'] ?? [] as $chapter) {
                foreach ($chapter['materials'] ?? [] as $index => $material) {
                    if (! is_array($material)) {
                        continue;
                    }

                    $materials["{$relative}[{$index}]"] = $material;
                }
            }
        }

        ksort($materials);

        return $materials;
    }

    /**
     * @param  array<int, array<string, mixed>>  $blocks
     */
    private function blocksWordCount(array $blocks): int
    {
        $text = '';

        foreach ($blocks as $block) {
            $type = $block['type'] ?? '';

            if (in_array($type, ['heading', 'paragraph', 'callout', 'code'], true)) {
                $text .= ' ' . ($block['text'] ?? '');
            } elseif ($type === 'list') {
                $text .= ' ' . implode(' ', array_map('strval', $block['items'] ?? []));
            } elseif ($type === 'table') {
                foreach ($block['rows'] ?? [] as $row) {
                    $text .= ' ' . implode(' ', array_map('strval', (array) $row));
                }
            }
        }

        return $this->wordCount($text);
    }

    private function wordCount(string $text): int
    {
        $plain = strip_tags(preg_replace('/[|#>*-]/u', ' ', $text) ?? '');

        return count(preg_split('/\s+/u', trim($plain), -1, PREG_SPLIT_NO_EMPTY) ?: []);
    }

    private function normalize(string $text): string
    {
        $plain = preg_replace('/[|#>*-]/u', ' ', $text) ?? '';

        return mb_strtolower(trim(preg_replace('/\s+/u', ' ', $plain) ?? ''));
    }
}
