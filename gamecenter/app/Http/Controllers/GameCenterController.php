<?php

namespace App\Http\Controllers;

use App\Models\Chapter;
use App\Models\EducationLevel;
use App\Models\LearningMaterial;
use App\Models\Question;
use App\Models\Subject;
use App\Models\UserProgress;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class GameCenterController extends Controller
{
    /**
     * Halaman jelajah materi: filter jenjang → kelas → mapel → mode.
     */
    public function index(Request $request): Response
    {
        $levels = EducationLevel::query()
            ->active()
            ->orderBy('order')
            ->with([
                'classes' => fn ($query) => $query
                    ->active()
                    ->orderBy('order')
                    ->with([
                        'subjects' => fn ($subjects) => $subjects
                            ->active()
                            ->orderBy('order')
                            ->withCount([
                                'chapters' => fn ($chapters) => $chapters->active(),
                            ])
                            ->with([
                                'chapters' => fn ($chapters) => $chapters
                                    ->active()
                                    ->orderBy('order')
                                    ->withCount('materials')
                                    ->with([
                                        'assessments' => fn ($assessments) => $assessments
                                            ->active()
                                            ->withCount('questions'),
                                    ]),
                            ]),
                    ]),
            ])
            ->get()
            ->map(fn (EducationLevel $level) => [
                'id' => $level->id,
                'name' => $level->name,
                'slug' => $level->slug,
                'short_name' => $level->short_name,
                'description' => $level->description,
                'theme' => $level->theme,
                'icon' => $level->icon,
                'classes' => $level->classes->map(fn ($class) => [
                    'id' => $class->id,
                    'name' => $class->name,
                    'slug' => $class->slug,
                    'grade_level' => $class->grade_level,
                    'phase' => $class->phase,
                    'subjects' => $class->subjects->map(fn (Subject $subject) => [
                        'id' => $subject->id,
                        'name' => $subject->name,
                        'slug' => $subject->slug,
                        'group' => $subject->group,
                        'icon' => $subject->icon,
                        'color' => $subject->color,
                        'chapters_count' => $subject->chapters_count,
                        'chapters' => $subject->chapters->map(fn (Chapter $chapter) => [
                            'id' => $chapter->id,
                            'code' => $chapter->code,
                            'title' => $chapter->title,
                            'description' => $chapter->description,
                            'materials_count' => $chapter->materials_count,
                            'assessments' => $chapter->assessments->map(fn ($assessment) => [
                                'id' => $assessment->id,
                                'difficulty' => $assessment->difficulty->value,
                                'duration' => $assessment->duration,
                                'questions_count' => $assessment->questions_count,
                            ]),
                        ]),
                    ]),
                ]),
            ]);

        return Inertia::render('GameCenter/Index', [
            'levels' => $levels,
            'defaultLevel' => $request->user()?->classRoom?->educationLevel?->slug,
            'recent' => $this->recentProgress($request),
            'stats' => [
                'levels' => $levels->count(),
                'classes' => $levels->sum(fn ($level) => count($level['classes'])),
                'subjects' => $levels->sum(fn ($level) => collect($level['classes'])->sum(fn ($class) => count($class['subjects']))),
                'chapters' => Chapter::query()->active()->count(),
                'materials' => LearningMaterial::query()->active()->count(),
                'questions' => Question::query()->count(),
            ],
        ]);
    }

    /**
     * @return array<int, array<string, mixed>>
     */
    private function recentProgress(Request $request): array
    {
        $user = $request->user();

        if ($user === null) {
            return [];
        }

        return UserProgress::query()
            ->where('user_id', $user->id)
            ->with([
                'chapter.subject.classRoom.educationLevel',
                'chapter.assessments' => fn ($query) => $query
                    ->active()
                    ->orderBy('order'),
            ])
            ->orderByDesc('last_accessed_at')
            ->limit(4)
            ->get()
            ->map(function (UserProgress $progress) {
                $chapter = $progress->chapter;
                $subject = $chapter?->subject;
                $level = $subject?->classRoom?->educationLevel;
                $assessment = $chapter?->assessments->first();

                return [
                    'chapter_id' => $progress->chapter_id,
                    'chapter_title' => $chapter?->title,
                    'subject_name' => $subject?->name,
                    'subject_icon' => $subject?->icon,
                    'subject_color' => $subject?->color,
                    'level_name' => $level?->name,
                    'level_theme' => $level?->theme ?? 'default',
                    'best_score' => (int) $progress->best_score,
                    'status' => $progress->status->value,
                    'assessment_id' => $assessment?->id,
                ];
            })
            ->values()
            ->all();
    }
}
