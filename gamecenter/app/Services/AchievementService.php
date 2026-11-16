<?php

namespace App\Services;

use App\Enums\Difficulty;
use App\Enums\QuestionType;
use App\Models\Achievement;
use App\Models\GameSession;
use App\Models\User;
use App\Models\UserProgress;
use Illuminate\Support\Collection;

/**
 * Menentukan lencana yang layak dibuka setelah sesi atau progres tersinkron.
 *
 * Semua hadiah lencana (XP/koin) hanya diberikan sekali. Pemeriksaan memakai
 * data yang sudah tersimpan di server, sehingga perangkat offline tidak bisa
 * mengklaim lencana yang sama berulang kali.
 */
class AchievementService
{
    /**
     * @return array<int, array<string, mixed>>
     */
    public function awardForSession(User $user, GameSession $session): array
    {
        $session->loadMissing([
            'assessment.chapter.subject',
            'assessment.questions',
            'answers.question',
            'result',
        ]);

        $assessment = $session->assessment;
        $result = $session->result;

        if ($assessment === null || $result === null) {
            return [];
        }

        $subject = $assessment->chapter?->subject;
        $isMath = str_contains(mb_strtolower((string) $subject?->name), 'matematika');
        $hasSimulation = $assessment->questions
            ->contains(fn ($question) => $question->type === QuestionType::Simulation);

        $stats = [
            'sessions_completed' => GameSession::query()
                ->where('user_id', $user->id)
                ->where('status', 'completed')
                ->count(),
            'perfect_score' => $result->total_score >= 100 ? 1 : 0,
            'answer_streak' => $this->bestStreak($session),
            'chapter_all_difficulties' => $this->completedDifficulties($user, $assessment->chapter_id),
            'perfect_hard_math' => $result->total_score >= 100
                && $session->mode === Difficulty::Hard
                && $isMath ? 1 : 0,
            'simulation_above_80' => $hasSimulation && $result->total_score >= 80
                ? $result->total_score
                : 0,
            'materials_read' => $this->materialsRead($user),
        ];

        return $this->award($user, $stats);
    }

    /**
     * @return array<int, array<string, mixed>>
     */
    public function awardForProgress(User $user): array
    {
        return $this->award($user, [
            'materials_read' => $this->materialsRead($user),
        ]);
    }

    private function bestStreak(GameSession $session): int
    {
        $answers = $session->answers->keyBy('question_id');
        $best = 0;
        $current = 0;

        foreach ($session->assessment->questions->sortBy('order') as $question) {
            $answer = $answers->get($question->id);

            if ($answer !== null && $answer->is_correct) {
                $current += 1;
                $best = max($best, $current);
            } else {
                $current = 0;
            }
        }

        return $best;
    }

    private function completedDifficulties(User $user, int $chapterId): int
    {
        return GameSession::query()
            ->where('user_id', $user->id)
            ->where('status', 'completed')
            ->whereHas('assessment', fn ($query) => $query->where('chapter_id', $chapterId))
            ->pluck('mode')
            ->map(fn ($mode) => $mode instanceof Difficulty ? $mode->value : (string) $mode)
            ->unique()
            ->count();
    }

    private function materialsRead(User $user): int
    {
        return (int) UserProgress::query()
            ->where('user_id', $user->id)
            ->sum('materials_read');
    }

    /**
     * @param  array<string, int>  $stats
     * @return array<int, array<string, mixed>>
     */
    private function award(User $user, array $stats): array
    {
        $achievements = Achievement::query()
            ->active()
            ->orderBy('order')
            ->get();

        /** @var Collection<int, int> $unlocked */
        $unlocked = $user->achievements()->pluck('achievements.id');
        $awarded = [];
        $xp = 0;
        $coins = 0;

        foreach ($achievements as $achievement) {
            if ($unlocked->contains($achievement->id)) {
                continue;
            }

            $value = $stats[$achievement->requirement_type] ?? null;

            if ($value === null) {
                continue;
            }

            if ($value < max(1, (int) $achievement->requirement_value)) {
                continue;
            }

            $user->achievements()->attach($achievement->id, [
                'unlocked_at' => now(),
            ]);

            $xp += (int) $achievement->xp_reward;
            $coins += (int) $achievement->coin_reward;

            $awarded[] = [
                'slug' => $achievement->slug,
                'title' => $achievement->title,
                'description' => $achievement->description,
                'icon' => $achievement->icon,
                'xp_reward' => (int) $achievement->xp_reward,
                'coin_reward' => (int) $achievement->coin_reward,
            ];
        }

        if ($xp > 0 || $coins > 0) {
            $user->refresh();
            $user->update([
                'xp' => $user->xp + $xp,
                'coins' => $user->coins + $coins,
                'level' => User::levelForXp($user->xp + $xp),
            ]);
        }

        return $awarded;
    }
}
