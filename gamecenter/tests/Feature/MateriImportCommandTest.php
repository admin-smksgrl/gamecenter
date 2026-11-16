<?php

namespace Tests\Feature;

use App\Models\Assessment;
use App\Models\Chapter;
use App\Models\Question;
use App\Models\Subject;
use App\Services\Materi\MateriImporter;
use App\Services\Materi\MateriValidationException;
use Database\Seeders\ClassSeeder;
use Database\Seeders\EducationLevelSeeder;
use Database\Seeders\SmaSmkMaterialSeeder;
use Database\Seeders\SubjectSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class MateriImportCommandTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();

        // Importer mencari mapel lewat relasi level → kelas → mapel,
        // jadi data acuan harus ada lebih dulu.
        $this->seed([
            EducationLevelSeeder::class,
            ClassSeeder::class,
            SubjectSeeder::class,
        ]);
    }

    private function payload(): array
    {
        return [
            'schema_version' => 1,
            'level' => 'sma',
            'class' => 'kelas-10',
            'subject' => 'matematika',
            'chapters' => [
                [
                    'code' => 'TEST 1.1',
                    'title' => 'Eksponen Uji',
                    'learning_objectives' => ['Menjelaskan sifat eksponen.'],
                    'estimated_minutes' => 45,
                    'materials' => [
                        [
                            'type' => 'text',
                            'title' => 'Pengantar',
                            'content' => 'Isi materi.',
                        ],
                    ],
                    'assessments' => [
                        [
                            'difficulty' => 'easy',
                            'questions' => [
                                [
                                    'type' => 'multiple_choice',
                                    'question' => 'Berapakah 2³?',
                                    'options' => [
                                        ['text' => '8', 'correct' => true],
                                        ['text' => '6', 'correct' => false],
                                    ],
                                    'explanation' => '2 × 2 × 2 = 8.',
                                    'hint' => 'Kalikan tiga kali.',
                                ],
                            ],
                        ],
                    ],
                ],
            ],
        ];
    }

    public function test_import_creates_chapter_material_assessment_and_question(): void
    {
        $result = app(MateriImporter::class)->import($this->payload());

        $this->assertSame(1, $result->chaptersCreated);
        $this->assertSame(1, $result->materialsCreated);
        $this->assertSame(1, $result->assessmentsCreated);
        $this->assertSame(1, $result->questionsCreated);

        $subject = Subject::query()
            ->where('slug', 'matematika')
            ->whereHas('classRoom', fn ($q) => $q->where('slug', 'kelas-10')
                ->whereHas('educationLevel', fn ($l) => $l->where('slug', 'sma')))
            ->firstOrFail();

        $chapter = Chapter::query()
            ->where('subject_id', $subject->id)
            ->where('slug', 'eksponen-uji')
            ->firstOrFail();

        $this->assertSame('Eksponen Uji', $chapter->title);
        $this->assertSame('TEST 1.1', $chapter->code);
        $this->assertSame(['Menjelaskan sifat eksponen.'], $chapter->learning_objectives);
        $this->assertSame(45, $chapter->estimated_minutes);
        $this->assertSame(1, $chapter->materials()->count());
        $this->assertSame(1, $chapter->assessments()->count());
    }

    public function test_import_is_idempotent(): void
    {
        $importer = app(MateriImporter::class);
        $importer->import($this->payload());

        $chapters = Chapter::count();
        $materials = \App\Models\LearningMaterial::count();
        $assessments = Assessment::count();
        $questions = Question::count();
        $options = \App\Models\QuestionOption::count();

        $second = $importer->import($this->payload());

        $this->assertSame($chapters, Chapter::count());
        $this->assertSame($materials, \App\Models\LearningMaterial::count());
        $this->assertSame($assessments, Assessment::count());
        $this->assertSame($questions, Question::count());
        $this->assertSame($options, \App\Models\QuestionOption::count());

        $this->assertTrue($second->isRepeat(), 'Impor kedua seharusnya tidak membuat baris baru.');
        $this->assertSame(0, $second->chaptersCreated);
        $this->assertSame(0, $second->questionsCreated);
    }

    public function test_import_applies_difficulty_defaults(): void
    {
        app(MateriImporter::class)->import($this->payload());

        $question = Question::firstOrFail();

        $this->assertSame(10, $question->points);
        $this->assertSame(90, $question->time_limit);
        $this->assertSame(['text' => '8'], $question->correct_answer);
    }

    public function test_import_drops_hint_for_hard_questions(): void
    {
        $payload = $this->payload();
        $payload['chapters'][0]['assessments'][0]['difficulty'] = 'hard';
        $payload['chapters'][0]['assessments'][0]['questions'][0]['hint'] = '';

        app(MateriImporter::class)->import($payload);

        $this->assertNull(Question::firstOrFail()->hint);
        $this->assertSame(30, Question::firstOrFail()->points);
    }

    public function test_import_rejects_question_without_explanation(): void
    {
        $payload = $this->payload();
        unset($payload['chapters'][0]['assessments'][0]['questions'][0]['explanation']);

        $this->expectException(MateriValidationException::class);

        app(MateriImporter::class)->import($payload);
    }

    public function test_import_rejects_multiple_choice_with_two_correct_answers(): void
    {
        $payload = $this->payload();
        $payload['chapters'][0]['assessments'][0]['questions'][0]['options'][1]['correct'] = true;

        try {
            app(MateriImporter::class)->import($payload);
            $this->fail('Seharusnya menolak pilihan ganda dengan dua kunci.');
        } catch (MateriValidationException $exception) {
            $this->assertStringContainsString('tepat satu opsi benar', implode(' ', $exception->problems));
        }
    }

    public function test_import_writes_nothing_when_validation_fails(): void
    {
        $payload = $this->payload();
        $payload['chapters'][0]['title'] = '';

        try {
            app(MateriImporter::class)->import($payload);
        } catch (MateriValidationException) {
            // diharapkan
        }

        $this->assertSame(0, Chapter::count());
        $this->assertSame(0, Question::count());
    }

    public function test_import_rejects_unknown_subject(): void
    {
        $payload = $this->payload();
        $payload['subject'] = 'mapel-tidak-ada';

        $this->expectException(MateriValidationException::class);

        app(MateriImporter::class)->import($payload);
    }

    public function test_command_reports_success_for_bundled_materials(): void
    {
        $this->artisan('gamecenter:materi-import', ['--no-ansi' => true])
            ->assertSuccessful();

        $this->assertGreaterThan(0, Chapter::query()->where('code', 'MA 1.1')->count());
    }

    public function test_command_dry_run_writes_nothing(): void
    {
        $this->artisan('gamecenter:materi-import', ['--dry-run' => true, '--no-ansi' => true])
            ->assertSuccessful();

        $this->assertSame(0, Chapter::count());
    }

    public function test_full_database_seed_is_idempotent_including_materi(): void
    {
        $this->seed(\Database\Seeders\DatabaseSeeder::class);

        $counts = [
            'chapters' => Chapter::count(),
            'materials' => \App\Models\LearningMaterial::count(),
            'assessments' => Assessment::count(),
            'questions' => Question::count(),
            'options' => \App\Models\QuestionOption::count(),
        ];

        // Menjalankan seluruh seeder sekali lagi tidak boleh menambah baris.
        $this->seed(\Database\Seeders\DatabaseSeeder::class);

        $this->assertSame($counts['chapters'], Chapter::count());
        $this->assertSame($counts['materials'], \App\Models\LearningMaterial::count());
        $this->assertSame($counts['assessments'], Assessment::count());
        $this->assertSame($counts['questions'], Question::count());
        $this->assertSame($counts['options'], \App\Models\QuestionOption::count());

        $this->assertDatabaseHas('chapters', ['code' => 'MA 1.1', 'title' => 'Eksponen']);
    }

    public function test_bundled_pilot_chapter_has_full_question_coverage(): void
    {
        app(MateriImporter::class)->import(
            json_decode(
                file_get_contents(database_path('seeders/data/sma-smk/fase-e/matematika/ma-1.1-eksponen.json')),
                true,
                512,
                JSON_THROW_ON_ERROR,
            ),
        );

        $chapter = Chapter::query()->where('code', 'MA 1.1')->firstOrFail();

        $this->assertSame(3, $chapter->materials()->count());

        $counts = $chapter->assessments()->get()
            ->mapWithKeys(fn (Assessment $a) => [$a->difficulty->value => $a->questions()->count()])
            ->all();

        $this->assertSame(['easy' => 5, 'medium' => 10, 'hard' => 15], $counts);
        $this->assertSame(0, Question::query()->whereNull('explanation')->count());
    }

    public function test_bundled_chapters_are_complete(): void
    {
        $this->seed(SmaSmkMaterialSeeder::class);

        $expected = [
            'MA 1.1', 'MA 1.2', 'MA 2.1', 'MA 2.2', 'MA 3.1', 'MA 4.1',
            'MA 5.1', 'MA 5.2', 'MA 6.1', 'MA 6.2', 'MA 6.3', 'MA 7.1', 'MA 8.1',
            'INF 1', 'INF 2', 'INF 3', 'INF 4', 'INF 5', 'INF 6', 'INF 7', 'INF 8',
            'BI 1', 'BI 2', 'BI 3', 'BI 4', 'BI 5',
            'FIS 1', 'FIS 2',
            'KIM 1', 'KIM 2', 'KIM 3',
            'BIO 1', 'BIO 2', 'BIO 3',
            'PAN 1', 'PAN 2', 'PAN 3', 'PAN 4',
            'PAI 1', 'PAI 2', 'PAI 3', 'PAI 4', 'PAI 5',
            'PAI 6', 'PAI 7', 'PAI 8', 'PAI 9', 'PAI 10',
        ];

        foreach ($expected as $code) {
            $chapter = Chapter::query()->where('code', $code)->firstOrFail();

            $this->assertGreaterThanOrEqual(
                3,
                $chapter->materials()->count(),
                "{$code} minimal punya 3 materi",
            );

            $counts = $chapter->assessments()->get()
                ->mapWithKeys(fn (Assessment $a) => [$a->difficulty->value => $a->questions()->count()])
                ->all();

            $this->assertSame(['easy' => 5, 'medium' => 10, 'hard' => 15], $counts, "{$code} harus 5/10/15 soal");
        }

        $this->assertSame(0, Question::query()->whereNull('explanation')->count(), 'setiap soal wajib punya penjelasan');

        $hardWithHint = Question::query()
            ->whereHas('assessment', fn ($q) => $q->where('difficulty', 'hard'))
            ->whereNotNull('hint')
            ->count();

        $this->assertSame(0, $hardWithHint, 'soal sulit tidak boleh punya hint');
    }

    public function test_bundled_materials_cover_every_question_type(): void
    {
        $this->seed(SmaSmkMaterialSeeder::class);

        $types = Question::query()->distinct()->pluck('type')
            ->map(fn ($type) => $type instanceof \App\Enums\QuestionType ? $type->value : $type)
            ->all();

        foreach (['multiple_choice', 'multiple_answer', 'matching', 'drag_drop', 'puzzle'] as $type) {
            $this->assertContains($type, $types, "tipe soal {$type} belum dipakai materi bawaan");
        }

        $this->assertSame(48, Chapter::query()->whereIn('code', [
            'MA 1.1', 'MA 1.2', 'MA 2.1', 'MA 2.2', 'MA 3.1', 'MA 4.1',
            'MA 5.1', 'MA 5.2', 'MA 6.1', 'MA 6.2', 'MA 6.3', 'MA 7.1', 'MA 8.1',
            'INF 1', 'INF 2', 'INF 3', 'INF 4', 'INF 5', 'INF 6', 'INF 7', 'INF 8',
            'BI 1', 'BI 2', 'BI 3', 'BI 4', 'BI 5',
            'FIS 1', 'FIS 2', 'KIM 1', 'KIM 2', 'KIM 3',
            'BIO 1', 'BIO 2', 'BIO 3',
            'PAN 1', 'PAN 2', 'PAN 3', 'PAN 4',
            'PAI 1', 'PAI 2', 'PAI 3', 'PAI 4', 'PAI 5',
            'PAI 6', 'PAI 7', 'PAI 8', 'PAI 9', 'PAI 10',
        ])->count());

        $this->assertSame(1440, Question::query()->count());
    }
}
