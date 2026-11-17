<?php

namespace App\Services\Materi;

use App\Enums\Difficulty;
use App\Models\Chapter;
use App\Models\LearningMaterial;
use App\Models\MaterialBlockResponse;
use App\Models\User;
use Illuminate\Support\Collection;

/**
 * Rekap skor blok interaktif untuk siswa dan guru (plan §3.4.1, Fase 5).
 *
 * Skor blok bersifat formatif: laporan ini **tidak** menyentuh
 * `game_sessions`/rapor, hanya menampilkan latihan mandiri per blok.
 */
class BlockPracticeReport
{
    /** Label tipe blok untuk tampilan Indonesia. */
    public const TYPE_LABELS = [
        'glossary' => 'Glosarium',
        'flashcards' => 'Flashcard',
        'checkpoint' => 'Cek pemahaman',
        'sort' => 'Urutkan',
        'categorize' => 'Kelompokkan',
        'label' => 'Beri label',
        'scenario' => 'Skenario',
        'challenge' => 'Tantangan kilat',
    ];

    public static function typeLabel(string $type): string
    {
        return self::TYPE_LABELS[$type] ?? ucfirst($type);
    }

    /**
     * Ringkasan untuk halaman `/progres` siswa.
     *
     * @return array<string, mixed>
     */
    public function forStudent(User $user, int $limit = 8): array
    {
        $rows = MaterialBlockResponse::query()
            ->where('user_id', $user->id)
            ->with([
                'material.chapter.subject.classRoom.educationLevel',
                'material.chapter.assessments',
            ])
            ->orderByDesc('last_answered_at')
            ->get();

        $totals = [
            'blocks' => $rows->count(),
            'completed' => $rows->filter(fn (MaterialBlockResponse $row): bool => $row->is_completed)->count(),
            'attempts' => (int) $rows->sum('attempts'),
            'average_score' => $rows->isEmpty()
                ? 0
                : (int) round((float) $rows->avg('score')),
        ];

        $materials = $rows
            ->groupBy('material_id')
            ->map(function (Collection $group): array {
                /** @var MaterialBlockResponse $first */
                $first = $group->first();
                $material = $first->material;
                $chapter = $material?->chapter;
                $subject = $chapter?->subject;
                $assessment = $chapter?->assessments
                    ?->firstWhere('difficulty', Difficulty::Easy)
                    ?? $chapter?->assessments?->first();

                return [
                    'material_id' => (int) $first->material_id,
                    'material_title' => $material?->title,
                    'chapter_id' => $chapter?->id,
                    'chapter_code' => $chapter?->code,
                    'chapter_title' => $chapter?->title,
                    'subject_name' => $subject?->name,
                    'subject_icon' => $subject?->icon,
                    'subject_color' => $subject?->color,
                    'level_theme' => $subject?->classRoom?->educationLevel?->theme ?? 'default',
                    'assessment_id' => $assessment?->id,
                    'blocks' => $group->count(),
                    'completed' => $group->filter(fn (MaterialBlockResponse $row): bool => $row->is_completed)->count(),
                    'average_score' => (int) round((float) $group->avg('score')),
                    'attempts' => (int) $group->sum('attempts'),
                    'last_answered_at' => $first->last_answered_at?->toIso8601String(),
                    'block_rows' => $group
                        ->sortBy('block_id')
                        ->map(fn (MaterialBlockResponse $row): array => [
                            'block_id' => $row->block_id,
                            'block_type' => $row->block_type,
                            'label' => self::typeLabel($row->block_type),
                            'score' => (int) $row->score,
                            'attempts' => (int) $row->attempts,
                            'is_completed' => (bool) $row->is_completed,
                            'last_answered_at' => $row->last_answered_at?->toIso8601String(),
                        ])
                        ->values()
                        ->all(),
                ];
            })
            ->sortByDesc('last_answered_at')
            ->take($limit)
            ->values()
            ->all();

        return [
            'totals' => $totals,
            'materials' => $materials,
        ];
    }

    /**
     * Rekap guru untuk satu chapter (dipakai panel Filament).
     *
     * @return array<string, mixed>
     */
    public function forChapter(Chapter $chapter): array
    {
        $rows = $this->chapterRows($chapter);

        $totals = [
            'blocks' => $rows->count(),
            'students' => $rows->pluck('user_id')->unique()->count(),
            'completed' => $rows->filter(fn (MaterialBlockResponse $row): bool => $row->is_completed)->count(),
            'attempts' => (int) $rows->sum('attempts'),
            'average_score' => $rows->isEmpty()
                ? 0
                : (int) round((float) $rows->avg('score')),
        ];

        $blocks = $rows
            ->groupBy(fn (MaterialBlockResponse $row): string => "{$row->material_id}|{$row->block_id}")
            ->map(function (Collection $group): array {
                /** @var MaterialBlockResponse $first */
                $first = $group->first();

                return [
                    'material_title' => $first->material?->title,
                    'block_id' => $first->block_id,
                    'block_type' => $first->block_type,
                    'label' => self::typeLabel($first->block_type),
                    'students' => $group->pluck('user_id')->unique()->count(),
                    'completed' => $group->filter(fn (MaterialBlockResponse $row): bool => $row->is_completed)->count(),
                    'attempts' => (int) $group->sum('attempts'),
                    'average_score' => (int) round((float) $group->avg('score')),
                ];
            })
            ->sortByDesc('average_score')
            ->values()
            ->all();

        $students = $rows
            ->groupBy('user_id')
            ->map(function (Collection $group): array {
                /** @var MaterialBlockResponse $first */
                $first = $group->first();

                return [
                    'name' => $first->user?->name,
                    'username' => $first->user?->username,
                    'class_name' => $first->user?->classRoom?->name,
                    'blocks' => $group->count(),
                    'completed' => $group->filter(fn (MaterialBlockResponse $row): bool => $row->is_completed)->count(),
                    'attempts' => (int) $group->sum('attempts'),
                    'average_score' => (int) round((float) $group->avg('score')),
                    'last_answered_at' => $group->max('last_answered_at'),
                ];
            })
            ->sortByDesc('last_answered_at')
            ->values()
            ->all();

        return [
            'totals' => $totals,
            'blocks' => $blocks,
            'students' => $students,
        ];
    }

    /**
     * CSV rekap chapter: satu baris per siswa × blok (Fase 5.4).
     */
    public function chapterCsv(Chapter $chapter): string
    {
        $rows = $this->chapterRows($chapter);

        $lines = [
            'chapter_code', 'chapter_title', 'nama_siswa', 'username', 'kelas',
            'materi', 'block_id', 'block_type', 'skor', 'max_skor', 'percobaan',
            'selesai', 'terakhir_dikerjakan',
        ];

        $csv = "\xEF\xBB\xBF" . implode(',', $lines) . "\r\n";

        foreach ($rows->sortBy([['user_id', 'asc'], ['material_id', 'asc'], ['block_id', 'asc']]) as $row) {
            /** @var MaterialBlockResponse $row */
            $csv .= $this->csvLine([
                $chapter->code,
                $chapter->title,
                $row->user?->name,
                $row->user?->username,
                $row->user?->classRoom?->name,
                $row->material?->title,
                $row->block_id,
                self::typeLabel($row->block_type),
                (int) $row->score,
                (int) $row->max_score,
                (int) $row->attempts,
                $row->is_completed ? 'ya' : 'belum',
                $row->last_answered_at?->toDateTimeString(),
            ]) . "\r\n";
        }

        return $csv;
    }

    /**
     * @return Collection<int, MaterialBlockResponse>
     */
    private function chapterRows(Chapter $chapter): Collection
    {
        return MaterialBlockResponse::query()
            ->whereHas('material', fn ($query) => $query->where('chapter_id', $chapter->id))
            ->with(['user.classRoom', 'material'])
            ->get();
    }

    /**
     * @param  array<int, mixed>  $values
     */
    private function csvLine(array $values): string
    {
        return implode(',', array_map(function (mixed $value): string {
            $text = (string) ($value ?? '');

            return str_contains($text, ',') || str_contains($text, '"') || str_contains($text, "\n")
                ? '"' . str_replace('"', '""', $text) . '"'
                : $text;
        }, $values));
    }

    /**
     * Daftar blok pada sebuah chapter beserta status validasinya (Fase 5.2).
     *
     * @return array<int, array<string, mixed>>
     */
    public function blockAudit(Chapter $chapter): array
    {
        $schema = app(BlockSchema::class);

        return $chapter->materials
            ->flatMap(function (LearningMaterial $material) use ($schema): array {
                $blocks = $material->blocks ?? [];

                if (! is_array($blocks)) {
                    return [];
                }

                return collect($blocks)
                    ->map(function (mixed $block, int $index) use ($material, $schema): array {
                        $type = is_array($block) ? (string) ($block['type'] ?? '—') : '—';
                        $id = is_array($block) ? ($block['id'] ?? null) : null;
                        $summary = '';

                        if (is_array($block)) {
                            $summary = (string) (
                                $block['title']
                                ?? $block['text']
                                ?? $block['question']
                                ?? $block['caption']
                                ?? ''
                            );
                        }

                        $problems = is_array($block)
                            ? $schema->problems([$block], 'blok')
                            : ['blok bukan objek'];

                        return [
                            'material_title' => $material->title,
                            'index' => $index + 1,
                            'type' => $type,
                            'id' => is_string($id) ? $id : '—',
                            'summary' => mb_strimwidth(strip_tags($summary), 0, 70, '…'),
                            'problems' => $problems,
                        ];
                    })
                    ->all();
            })
            ->all();
    }
}