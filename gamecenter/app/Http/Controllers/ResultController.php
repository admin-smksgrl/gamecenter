<?php

namespace App\Http\Controllers;

use App\Enums\QuestionType;
use App\Models\GameSession;
use App\Models\Question;
use App\Models\SessionAnswer;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class ResultController extends Controller
{
    /**
     * Halaman hasil sesi yang sudah tersinkron, bisa dibuka ulang dari
     * riwayat progres.
     */
    public function show(Request $request, GameSession $gameSession): Response
    {
        $user = $request->user();

        abort_unless(
            $gameSession->user_id === $user->id || $user->isAdmin() || $user->isTeacher(),
            403,
        );

        $gameSession->load([
            'assessment.chapter.subject.classRoom.educationLevel',
            'result',
            'answers.question.questionOptions',
        ]);

        $assessment = $gameSession->assessment;
        $chapter = $assessment?->chapter;
        $subject = $chapter?->subject;
        $classRoom = $subject?->classRoom;
        $level = $classRoom?->educationLevel;
        $result = $gameSession->result;

        return Inertia::render('GameCenter/Result', [
            'session' => [
                'id' => $gameSession->id,
                'mode' => $gameSession->mode->value,
                'score' => (int) $gameSession->score,
                'correct_answers' => (int) $gameSession->correct_answers,
                'total_questions' => (int) $gameSession->total_questions,
                'duration_seconds' => (int) $gameSession->duration_seconds,
                'completed_at' => $gameSession->completed_at?->toIso8601String(),
            ],
            'context' => [
                'assessment_title' => $assessment?->title,
                'chapter_title' => $chapter?->title,
                'chapter_code' => $chapter?->code,
                'subject_name' => $subject?->name,
                'subject_icon' => $subject?->icon,
                'subject_color' => $subject?->color,
                'class_name' => $classRoom?->name,
                'level_name' => $level?->name,
                'level_theme' => $level?->theme ?? 'default',
            ],
            'summary' => [
                'total_score' => (int) ($result?->total_score ?? $gameSession->score),
                'max_score' => (int) ($result?->max_score ?? 0),
                'correct_count' => (int) ($result?->correct_count ?? $gameSession->correct_answers),
                'wrong_count' => (int) ($result?->wrong_count ?? 0),
                'unanswered_count' => (int) ($result?->unanswered_count ?? 0),
                'xp_earned' => (int) ($result?->xp_earned ?? 0),
                'coins_earned' => (int) ($result?->coins_earned ?? 0),
                'is_passed' => (bool) ($result?->is_passed ?? false),
            ],
            'answers' => $gameSession->answers
                ->sortBy(fn (SessionAnswer $answer) => $answer->question?->order ?? 0)
                ->values()
                ->map(fn (SessionAnswer $answer) => [
                    'id' => $answer->id,
                    'question' => $answer->question?->question,
                    'type' => $answer->question?->type?->value,
                    'type_label' => $answer->question?->type?->label(),
                    'is_correct' => (bool) $answer->is_correct,
                    'ungraded' => $answer->question?->type === QuestionType::Essay,
                    'points_earned' => (int) $answer->points_earned,
                    'user_answer' => $answer->user_answer,
                    'expected' => $this->expectedAnswer($answer->question),
                    'explanation' => $answer->question?->explanation,
                    'time_spent' => (int) $answer->time_spent,
                ])
                ->all(),
        ]);
    }

    private function expectedAnswer(?Question $question): ?string
    {
        if ($question === null || $question->type === QuestionType::Essay) {
            return null;
        }

        if (in_array($question->type, [QuestionType::MultipleChoice, QuestionType::MultipleAnswer, QuestionType::Simulation], true)) {
            $text = $question->questionOptions
                ->where('is_correct', true)
                ->pluck('text')
                ->implode(' · ');

            return $text !== '' ? $text : null;
        }

        if (in_array($question->type, [QuestionType::DragDrop, QuestionType::Puzzle], true)) {
            $pieces = collect($question->options ?? [])
                ->filter(fn ($piece) => is_array($piece) && isset($piece['id']))
                ->keyBy(fn ($piece) => (string) $piece['id']);

            $order = $question->correct_answer['order'] ?? [];

            return collect(is_array($order) ? $order : [])
                ->map(fn ($id) => data_get($pieces->get((string) $id), 'text', (string) $id))
                ->implode(' → ') ?: null;
        }

        if ($question->type === QuestionType::Matching) {
            $pairs = collect($question->options ?? [])
                ->filter(fn ($pair) => is_array($pair) && isset($pair['id']))
                ->keyBy(fn ($pair) => (string) $pair['id']);

            $expected = $question->correct_answer['pairs'] ?? [];

            return collect(is_array($expected) ? $expected : [])
                ->map(fn ($right, $id) => data_get($pairs->get((string) $id), 'left', (string) $id).' → '.$right)
                ->implode(' · ') ?: null;
        }

        return null;
    }
}
