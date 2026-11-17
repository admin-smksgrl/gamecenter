<?php

namespace App\Http\Controllers;

use App\Enums\Difficulty;
use App\Enums\ProgressStatus;
use App\Models\Achievement;
use App\Models\GameSession;
use App\Models\User;
use App\Models\UserProgress;
use App\Services\Materi\BlockPracticeReport;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Inertia\Inertia;
use Inertia\Response;

class ProgressController extends Controller
{
    private const LEVEL_TITLES = [
        1 => 'Pemula',
        2 => 'Pemain',
        3 => 'Ahli',
        4 => 'Master',
        5 => 'Legenda',
    ];

    /**
     * Ringkasan progres, riwayat sesi, dan koleksi lencana siswa.
     */
    public function index(Request $request, BlockPracticeReport $blockPractice): Response
    {
        $user = $request->user();
        $user->loadMissing('classRoom.educationLevel');

        $progressRows = UserProgress::query()
            ->where('user_id', $user->id)
            ->with([
                'chapter.subject.classRoom.educationLevel',
                'chapter.assessments' => fn ($query) => $query
                    ->active()
                    ->orderBy('order'),
            ])
            ->orderByDesc('last_accessed_at')
            ->get();

        $sessions = GameSession::query()
            ->where('user_id', $user->id)
            ->where('status', 'completed')
            ->with(['assessment.chapter.subject', 'result'])
            ->orderByDesc('completed_at')
            ->limit(12)
            ->get();

        $allSessions = GameSession::query()
            ->where('user_id', $user->id)
            ->where('status', 'completed')
            ->get(['id', 'score', 'duration_seconds', 'completed_at']);

        $achievementRows = Achievement::query()
            ->active()
            ->orderBy('order')
            ->get();

        $unlocked = $user->achievements()->get()->keyBy('id');

        $totalSessions = $allSessions->count();
        $materialsRead = (int) $progressRows->sum('materials_read');
        $completedChapters = $progressRows
            ->filter(fn (UserProgress $row) => $row->status === ProgressStatus::Completed)
            ->count();

        $thresholds = User::LEVEL_THRESHOLDS;
        $currentThreshold = $thresholds[$user->level] ?? 0;
        $nextThreshold = $thresholds[$user->level + 1] ?? null;
        $levelPercent = $nextThreshold === null
            ? 100
            : min(100, (int) round((($user->xp - $currentThreshold) / max(1, $nextThreshold - $currentThreshold)) * 100));

        return Inertia::render('GameCenter/Progress', [
            'user' => [
                'name' => $user->name,
                'username' => $user->username,
                'xp' => (int) $user->xp,
                'coins' => (int) $user->coins,
                'level' => (int) $user->level,
                'level_title' => self::LEVEL_TITLES[$user->level] ?? 'Pemula',
                'streak_days' => (int) $user->streak_days,
                'class_name' => $user->classRoom?->name,
                'education_level' => $user->classRoom?->educationLevel?->name,
                'level_theme' => $user->classRoom?->educationLevel?->theme ?? 'default',
                'level_progress' => [
                    'percent' => $levelPercent,
                    'xp_to_next' => $nextThreshold === null
                        ? null
                        : max(0, $nextThreshold - (int) $user->xp),
                ],
            ],
            'stats' => [
                'sessions' => $totalSessions,
                'completed_chapters' => $completedChapters,
                'materials_read' => $materialsRead,
                'total_minutes' => (int) round($allSessions->sum('duration_seconds') / 60),
                'average_score' => $totalSessions > 0
                    ? (int) round((float) $allSessions->avg('score'))
                    : 0,
                'best_score' => (int) ($allSessions->max('score') ?? 0),
                'achievements_unlocked' => $unlocked->count(),
                'achievements_total' => $achievementRows->count(),
            ],
            'activity' => $this->weeklyActivity($allSessions),
            // Skor blok interaktif bersifat formatif (plan §3.4.1) — terpisah
            // dari statistik sesi/rapor di atas.
            'block_practice' => $blockPractice->forStudent($user),
            'progress' => $progressRows->map(function (UserProgress $row) {
                $chapter = $row->chapter;
                $subject = $chapter?->subject;
                $classRoom = $subject?->classRoom;
                $level = $classRoom?->educationLevel;
                $assessment = $chapter?->assessments
                    ->firstWhere('difficulty', Difficulty::Easy)
                    ?? $chapter?->assessments->first();

                return [
                    'chapter_id' => $row->chapter_id,
                    'chapter_title' => $chapter?->title,
                    'chapter_code' => $chapter?->code,
                    'subject_name' => $subject?->name,
                    'subject_icon' => $subject?->icon,
                    'subject_color' => $subject?->color,
                    'class_name' => $classRoom?->name,
                    'level_name' => $level?->name,
                    'level_slug' => $level?->slug,
                    'level_theme' => $level?->theme ?? 'default',
                    'status' => $row->status->value,
                    'status_label' => $row->status->label(),
                    'best_score' => (int) $row->best_score,
                    'attempts' => (int) $row->attempts,
                    'materials_read' => (int) $row->materials_read,
                    'total_time_spent' => (int) $row->total_time_spent,
                    'last_accessed_at' => $row->last_accessed_at?->toIso8601String(),
                    'assessment_id' => $assessment?->id,
                ];
            })->values(),
            'sessions' => $sessions->map(function (GameSession $session) {
                $assessment = $session->assessment;
                $chapter = $assessment?->chapter;
                $subject = $chapter?->subject;

                return [
                    'id' => $session->id,
                    'assessment_title' => $assessment?->title,
                    'chapter_title' => $chapter?->title,
                    'subject_name' => $subject?->name,
                    'subject_icon' => $subject?->icon,
                    'subject_color' => $subject?->color,
                    'mode' => $session->mode->value,
                    'score' => (int) $session->score,
                    'correct_answers' => (int) $session->correct_answers,
                    'total_questions' => (int) $session->total_questions,
                    'duration_seconds' => (int) $session->duration_seconds,
                    'xp_earned' => (int) ($session->result?->xp_earned ?? 0),
                    'coins_earned' => (int) ($session->result?->coins_earned ?? 0),
                    'is_passed' => (bool) ($session->result?->is_passed ?? false),
                    'completed_at' => $session->completed_at?->toIso8601String(),
                    'result_url' => route('result.show', $session->id),
                ];
            })->values(),
            'achievements' => $achievementRows->map(function (Achievement $achievement) use ($unlocked) {
                $record = $unlocked->get($achievement->id);

                return [
                    'id' => $achievement->id,
                    'slug' => $achievement->slug,
                    'title' => $achievement->title,
                    'description' => $achievement->description,
                    'icon' => $achievement->icon,
                    'category' => $achievement->category,
                    'requirement_type' => $achievement->requirement_type,
                    'requirement_value' => (int) $achievement->requirement_value,
                    'xp_reward' => (int) $achievement->xp_reward,
                    'coin_reward' => (int) $achievement->coin_reward,
                    'unlocked' => $record !== null,
                    'unlocked_at' => $record?->pivot?->unlocked_at
                        ? Carbon::parse($record->pivot->unlocked_at)->toIso8601String()
                        : null,
                ];
            })->values(),
        ]);
    }

    /**
     * @param  \Illuminate\Support\Collection<int, GameSession>  $sessions
     * @return array<int, array<string, mixed>>
     */
    private function weeklyActivity($sessions): array
    {
        return collect(range(6, 0))
            ->map(function (int $daysAgo) use ($sessions) {
                $date = now()->subDays($daysAgo)->startOfDay();
                $daySessions = $sessions->filter(
                    fn (GameSession $session) => $session->completed_at?->isSameDay($date),
                );

                return [
                    'date' => $date->toDateString(),
                    'label' => $date->locale('id')->isoFormat('ddd'),
                    'sessions' => $daySessions->count(),
                    'score' => $daySessions->isEmpty()
                        ? 0
                        : (int) round((float) $daySessions->avg('score')),
                ];
            })
            ->values()
            ->all();
    }
}
