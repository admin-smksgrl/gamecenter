<?php

namespace App\Http\Controllers;

use App\Models\Assessment;
use App\Models\Question;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class PlayController extends Controller
{
    /**
     * Halaman bermain untuk satu asesmen. Soal dikirim lengkap agar mesin
     * permainan bisa menilai dan memberi umpan balik saat offline; server
     * tetap menilai ulang jawaban objektif saat sesi disinkronkan.
     */
    public function show(Request $request, Assessment $assessment): Response
    {
        $assessment->load([
            'chapter.subject.classRoom.educationLevel',
            'questions.questionOptions',
        ]);

        $chapter = $assessment->chapter;
        $subject = $chapter?->subject;
        $classRoom = $subject?->classRoom;
        $level = $classRoom?->educationLevel;

        abort_unless(
            $assessment->is_active
            && $chapter?->is_active
            && $subject?->is_active
            && $classRoom?->is_active
            && $level?->is_active,
            404,
        );

        abort_if($assessment->questions->isEmpty(), 404);

        $progress = $request->user()
            ?->progress()
            ->where('chapter_id', $chapter->id)
            ->first();

        $materials = $chapter->materials()
            ->active()
            ->get()
            ->map(fn ($material) => [
                'id' => $material->id,
                'type' => $material->type->value,
                'type_label' => $material->type->label(),
                'title' => $material->title,
                'content' => $material->content,
                'blocks' => $material->blocks,
                'media_url' => $material->media_url,
                'media_type' => $material->media_type,
                'duration' => $material->duration,
                'order' => $material->order,
                'source_reference' => $material->source_reference,
            ])
            ->values();

        return Inertia::render('GameCenter/Play', [
            'assessment' => [
                'id' => $assessment->id,
                'title' => $assessment->title,
                'difficulty' => $assessment->difficulty->value,
                'duration' => $assessment->duration,
                'passing_score' => $assessment->passing_score,
                'question_count' => $assessment->questions->count(),
            ],
            'context' => [
                'chapter_id' => $chapter->id,
                'chapter_title' => $chapter->title,
                'chapter_code' => $chapter->code,
                'subject_name' => $subject->name,
                'subject_icon' => $subject->icon,
                'subject_color' => $subject->color,
                'subject_group' => $subject->group,
                'class_name' => $classRoom->name,
                'level_name' => $level->name,
                'level_theme' => $level->theme,
            ],
            'questions' => $assessment->questions
                ->map(fn (Question $question) => [
                    'id' => $question->id,
                    'type' => $question->type->value,
                    'type_label' => $question->type->label(),
                    'question' => $question->question,
                    'media_url' => $question->media_url,
                    'hint' => $question->hint,
                    'explanation' => $question->explanation,
                    'points' => $question->points,
                    'time_limit' => $question->time_limit,
                    'order' => $question->order,
                    'options' => $question->questionOptions
                        ->map(fn ($option) => [
                            'id' => $option->id,
                            'label' => $option->label,
                            'text' => $option->text,
                            'order' => $option->order,
                            'is_correct' => $option->is_correct,
                        ])
                        ->values(),
                    'payload' => $question->options,
                    'correct_answer' => $question->correct_answer,
                    'rubric' => $question->rubric,
                ])
                ->values(),
            'progress' => $progress ? [
                'status' => $progress->status->value,
                'best_score' => $progress->best_score,
                'attempts' => $progress->attempts,
                'materials_read' => $progress->materials_read,
            ] : null,
            'materials' => $materials,
        ]);
    }
}
