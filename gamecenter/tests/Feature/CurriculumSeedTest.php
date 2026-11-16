<?php

namespace Tests\Feature;

use App\Enums\Difficulty;
use App\Enums\QuestionType;
use App\Enums\UserRole;
use App\Models\Assessment;
use App\Models\Chapter;
use App\Models\ClassRoom;
use App\Models\EducationLevel;
use App\Models\Question;
use App\Models\Subject;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\Concerns\SeedsDemoContent;
use Tests\TestCase;

class CurriculumSeedTest extends TestCase
{
    use RefreshDatabase;
    use SeedsDemoContent;

    protected function setUp(): void
    {
        parent::setUp();

        $this->seedDemoContent();
    }

    public function test_all_education_levels_are_seeded(): void
    {
        $this->assertSame(6, EducationLevel::count());
        $this->assertDatabaseHas('education_levels', ['slug' => 'paud']);
        $this->assertDatabaseHas('education_levels', ['slug' => 'tk']);
        $this->assertDatabaseHas('education_levels', ['slug' => 'sd', 'name' => 'SD-MI']);
        $this->assertDatabaseHas('education_levels', ['slug' => 'smp', 'name' => 'SMP-MTs']);
        $this->assertDatabaseHas('education_levels', ['slug' => 'sma']);
        $this->assertDatabaseHas('education_levels', ['slug' => 'smk']);
    }

    public function test_each_sma_class_has_the_core_subjects(): void
    {
        $sma = EducationLevel::where('slug', 'sma')->firstOrFail();

        $this->assertSame(3, $sma->classes()->count());

        foreach ($sma->classes as $class) {
            foreach (['matematika', 'bahasa-indonesia', 'bahasa-inggris', 'fisika', 'kimia', 'biologi'] as $slug) {
                $this->assertTrue(
                    $class->subjects()->where('slug', $slug)->exists(),
                    "Mapel {$slug} tidak ada di {$class->name}",
                );
            }
        }
    }

    public function test_every_sma_and_smk_class_has_subjects(): void
    {
        $this->assertSame(18, ClassRoom::count());

        ClassRoom::all()->each(function (ClassRoom $class) {
            $this->assertGreaterThan(
                0,
                $class->subjects()->count(),
                "Kelas {$class->name} tidak punya mata pelajaran",
            );
        });
    }

    public function test_eksponen_chapter_has_three_difficulties_with_questions(): void
    {
        $chapter = Chapter::where('slug', 'eksponen')->firstOrFail();

        $this->assertCount(3, $chapter->assessments);

        foreach ([Difficulty::Easy, Difficulty::Medium, Difficulty::Hard] as $difficulty) {
            $assessment = $chapter->assessments
                ->firstWhere('difficulty', $difficulty);

            $this->assertInstanceOf(Assessment::class, $assessment);
            $this->assertGreaterThanOrEqual(5, $assessment->questions()->count());
        }
    }

    public function test_essay_questions_are_flagged_for_ai_assistance(): void
    {
        $essays = Question::where('type', QuestionType::Essay->value)->get();

        $this->assertCount(2, $essays);
        $this->assertTrue($essays->every(fn (Question $question) => $question->ai_assisted));
        $this->assertTrue($essays->every(fn (Question $question) => ! empty($question->rubric)));
    }

    public function test_multiple_choice_questions_have_exactly_one_correct_option(): void
    {
        $choices = Question::where('type', QuestionType::MultipleChoice->value)
            ->with('questionOptions')
            ->get();

        $this->assertGreaterThan(0, $choices->count());

        foreach ($choices as $question) {
            $this->assertSame(
                1,
                $question->questionOptions->where('is_correct', true)->count(),
                "Soal #{$question->id} harus punya tepat satu opsi benar",
            );
            $this->assertSame(4, $question->questionOptions->count());
        }
    }

    public function test_pemrograman_dasar_only_exists_for_smk_kelas_10(): void
    {
        $subjects = Subject::where('slug', 'pemrograman-dasar')->with('classRoom.educationLevel')->get();

        $this->assertCount(1, $subjects);
        $this->assertSame('smk', $subjects->first()->classRoom->educationLevel->slug);
        $this->assertSame(10, $subjects->first()->classRoom->grade_level);
    }

    public function test_demo_users_are_seeded_with_expected_roles(): void
    {
        $this->assertSame(UserRole::Admin, User::where('username', 'admin')->firstOrFail()->role);
        $this->assertSame(UserRole::Teacher, User::where('username', 'guru')->firstOrFail()->role);
        $this->assertSame(UserRole::Student, User::where('username', 'siswa')->firstOrFail()->role);
    }

    public function test_level_is_derived_from_total_xp(): void
    {
        $this->assertSame(1, User::levelForXp(0));
        $this->assertSame(2, User::levelForXp(120));
        $this->assertSame(3, User::levelForXp(250));
        $this->assertSame(4, User::levelForXp(500));
        $this->assertSame(5, User::levelForXp(1500));
    }

    public function test_seeders_are_idempotent(): void
    {
        $this->seedDemoContent();

        $this->assertSame(6, EducationLevel::count());
        $this->assertSame(18, ClassRoom::count());
        $this->assertSame(82, Question::count());
        $this->assertSame(4, User::count());
    }
}
