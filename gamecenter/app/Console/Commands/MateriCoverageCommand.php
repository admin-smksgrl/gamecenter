<?php

namespace App\Console\Commands;

use App\Models\Chapter;
use App\Models\LearningMaterial;
use App\Services\Materi\BlockSchema;
use Illuminate\Console\Command;

/**
 * Laporan kesiapan konten terhadap minimum plan §5.3 (Fase 5.1).
 *
 * Perintah ini **tidak mengubah data**; ia hanya membaca blok yang sudah
 * diimpor dan memberi tahu chapter mana yang masih perlu dilengkapi. Dipakai
 * untuk memantau progres konversi 49 bab tanpa menebak-nebak.
 */
class MateriCoverageCommand extends Command
{
    protected $signature = 'gamecenter:materi-coverage
        {--chapter= : Batasi ke satu kode chapter, misalnya "MA 1.1"}
        {--json : Keluarkan JSON agar bisa dipakai skrip/CI}
        {--only-incomplete : Hanya tampilkan chapter yang belum memenuhi minimum}';

    protected $description = 'Laporkan cakupan blok interaktif per chapter (plan §5.3)';

    /** @var array<int, string> */
    private const VISUAL_TYPES = ['diagram', 'chart', 'hotspots', 'timeline'];

    /** @var array<int, string> */
    private const ACTIVITY_TYPES = ['sort', 'categorize', 'label', 'checkpoint'];

    /** @var array<int, string> */
    private const SCENARIO_TYPES = ['scenario', 'challenge'];

    /** @var array<int, string> */
    private const RECALL_TYPES = ['glossary', 'flashcards'];

    /**
     * Blok teks. Wajib ada bila materi punya `blocks`, karena renderer
     * menampilkan blok **atau** markdown — bukan keduanya. Tanpa blok teks,
     * isi asli materi hilang dari layar (lihat §5.3: teks dipertahankan 100%).
     *
     * @var array<int, string>
     */
    private const TEXT_TYPES = ['heading', 'paragraph', 'list', 'table', 'callout', 'code'];

    public function handle(): int
    {
        $query = Chapter::query()
            ->with(['materials', 'subject'])
            ->orderBy('subject_id')
            ->orderBy('order');

        if ($code = $this->option('chapter')) {
            $query->where('code', $code);
        }

        $rows = $query->get()->map(fn (Chapter $chapter): array => $this->audit($chapter));

        if ($this->option('only-incomplete')) {
            $rows = $rows->reject(fn (array $row): bool => $row['complete'])->values();
        }

        if ($this->option('json')) {
            $this->line((string) json_encode([
                'chapters' => $rows->all(),
                'summary' => $this->summary($rows->all()),
            ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

            return self::SUCCESS;
        }

        $this->table(
            ['Chapter', 'Materi', 'Kata', 'Blok', 'Teori', 'Visual', 'Aktivitas', 'Skenario', 'Recall', 'Checkpoint', 'Status'],
            $rows->map(fn (array $row): array => [
                $row['code'],
                $row['materials'],
                $row['words'],
                $row['blocks'],
                $row['theory'],
                $row['visual'],
                $row['activities'],
                $row['scenario'],
                $row['recall'],
                "{$row['checkpoints']}/{$row['required_checkpoints']}",
                $row['complete'] ? '✅ lengkap' : '⚠ ' . implode(', ', $row['missing']),
            ])->all(),
        );

        $summary = $this->summary($rows->all());

        $this->newLine();
        $this->line(sprintf(
            '%d dari %d chapter memenuhi minimum §5.3 · total %d blok interaktif.',
            $summary['complete'],
            $summary['chapters'],
            $summary['blocks'],
        ));

        return self::SUCCESS;
    }

    /**
     * @return array<string, mixed>
     */
    private function audit(Chapter $chapter): array
    {
        $blocks = $chapter->materials
            ->flatMap(fn (LearningMaterial $material): array => is_array($material->blocks) ? $material->blocks : [])
            ->filter(fn (mixed $block): bool => is_array($block))
            ->values();

        $types = $blocks->pluck('type')->filter()->countBy();

        $content = $chapter->materials
            ->map(fn (LearningMaterial $material): string => (string) $material->content)
            ->implode(' ');

        $words = collect(preg_split('/\s+/u', strip_tags($content), -1, PREG_SPLIT_NO_EMPTY) ?: [])
            ->count();

        // Materi yang punya blok tetapi tanpa satu pun blok teks: isi aslinya
        // tidak akan tampil di layar karena renderer memilih salah satu jalur.
        $hidden = $chapter->materials
            ->filter(fn (LearningMaterial $material): bool => $this->hidesContent($material))
            ->count();

        $theory = $blocks
            ->filter(fn (array $block): bool => in_array($block['type'] ?? '', self::TEXT_TYPES, true))
            ->count();

        $visual = $this->countTypes($types, self::VISUAL_TYPES);
        $activities = $this->countTypes($types, self::ACTIVITY_TYPES);
        $scenario = $this->countTypes($types, self::SCENARIO_TYPES);
        $recall = $this->countTypes($types, self::RECALL_TYPES);
        $checkpoints = (int) ($types['checkpoint'] ?? 0);
        $requiredCheckpoints = max(1, (int) ceil($words / 500));

        $missing = [];

        if ($visual < 1) {
            $missing[] = 'visual';
        }

        if ($activities < 2) {
            $missing[] = 'aktivitas';
        }

        if ($scenario < 1) {
            $missing[] = 'skenario/tantangan';
        }

        if ($recall < 1) {
            $missing[] = 'glossary/flashcards';
        }

        if ($checkpoints < $requiredCheckpoints) {
            $missing[] = 'checkpoint';
        }

        if ($hidden > 0) {
            $missing[] = "teks tidak tampil ({$hidden} materi)";
        }

        return [
            'chapter_id' => $chapter->id,
            'code' => $chapter->code,
            'title' => $chapter->title,
            'materials' => $chapter->materials->count(),
            'blocks' => $blocks->count(),
            'theory' => $theory,
            'hidden' => $hidden,
            'words' => $words,
            'visual' => $visual,
            'activities' => $activities,
            'scenario' => $scenario,
            'recall' => $recall,
            'checkpoints' => $checkpoints,
            'required_checkpoints' => $requiredCheckpoints,
            'missing' => $missing,
            'complete' => $missing === [],
        ];
    }

    /**
     * @param  \Illuminate\Support\Collection<string, int>  $types
     * @param  array<int, string>  $wanted
     */
    private function countTypes($types, array $wanted): int
    {
        return (int) collect($wanted)->sum(fn (string $type): int => (int) ($types[$type] ?? 0));
    }

    /**
     * Materi dengan blok aktivitas/visual tetapi tanpa blok teks: konten
     * markdown-nya tidak dirender sama sekali oleh `MaterialViewer`.
     *
     * Blok lama berbentuk `{type, value}` (dipakai materi PAUD/TK) tidak
     * dihitung: renderer mengenalinya sebagai daftar nilai dan tetap
     * menampilkan markdown.
     */
    private function hidesContent(LearningMaterial $material): bool
    {
        $blocks = is_array($material->blocks) ? $material->blocks : [];
        $recognized = false;

        foreach ($blocks as $block) {
            if (! is_array($block)) {
                continue;
            }

            $type = (string) ($block['type'] ?? '');

            if (! in_array($type, BlockSchema::TYPES, true)) {
                continue;
            }

            if (in_array($type, self::TEXT_TYPES, true)) {
                return false;
            }

            $recognized = true;
        }

        return $recognized;
    }

    /**
     * @param  array<int, array<string, mixed>>  $rows
     * @return array<string, int>
     */
    private function summary(array $rows): array
    {
        return [
            'chapters' => count($rows),
            'complete' => count(array_filter($rows, fn (array $row): bool => $row['complete'])),
            'blocks' => (int) array_sum(array_column($rows, 'blocks')),
        ];
    }
}