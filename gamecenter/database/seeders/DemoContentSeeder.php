<?php

namespace Database\Seeders;

use App\Enums\Difficulty;
use App\Enums\QuestionType;
use App\Models\Assessment;
use App\Models\Chapter;
use App\Models\QuestionOption;
use App\Models\Subject;
use Illuminate\Database\Seeder;

/**
 * Data contoh satu chapter (SMA kelas 10 — Eksponen) untuk keperluan **tes**.
 *
 * Seeder ini sengaja TIDAK dipanggil dari `DatabaseSeeder`: chapter Eksponen
 * yang sesungguhnya berasal dari materi kurikulum di
 * `database/seeders/data/sma-smk`. Menyemai keduanya pada chapter yang sama
 * membuat baris materi berlipat setiap kali seed diulang.
 *
 * Tes yang membutuhkan fixture mesin game (tipe soal matching, puzzle,
 * simulation, dan essay) memakai `Tests\Concerns\SeedsDemoContent`.
 */
class DemoContentSeeder extends Seeder
{
    /**
     * Konten contoh: Matematika Kelas 10 (Fase E) — Bab Eksponen.
     * Sumber: Modul Ajar "MA 1.1 Eksponen" (Kemdikdasmen) + Buku Siswa Matematika Kelas X.
     */
    public function run(): void
    {
        $subject = Subject::query()
            ->where('slug', 'matematika')
            ->whereHas('classRoom', fn ($query) => $query
                ->where('slug', 'kelas-10')
                ->whereHas('educationLevel', fn ($q) => $q->where('slug', 'sma')))
            ->first();

        if ($subject === null) {
            $this->command?->warn('Subjek Matematika Kelas 10 SMA tidak ditemukan, DemoContentSeeder dilewati.');

            return;
        }

        $chapter = Chapter::updateOrCreate(
            ['subject_id' => $subject->id, 'slug' => 'eksponen'],
            [
                'code' => 'MA 1.1',
                'title' => 'Eksponen',
                'description' => 'Bilangan berpangkat, sifat-sifat eksponen, dan penerapannya dalam masalah nyata.',
                'learning_objectives' => [
                    'Menjelaskan definisi bilangan berpangkat (eksponen) beserta notasinya.',
                    'Menerapkan sifat-sifat eksponen untuk menyederhanakan bentuk aljabar.',
                    'Menyelesaikan persamaan eksponen sederhana.',
                    'Memodelkan pertumbuhan dan peluruhan dengan fungsi eksponen.',
                ],
                'estimated_minutes' => 120,
                'order' => 1,
            ],
        );

        $this->seedMaterials($chapter);
        $easy = $this->seedAssessment($chapter, Difficulty::Easy, 'Kuis Eksponen — Mudah', 600);
        $medium = $this->seedAssessment($chapter, Difficulty::Medium, 'Kuis Eksponen — Sedang', 900);
        $hard = $this->seedAssessment($chapter, Difficulty::Hard, 'Kuis Eksponen — Sulit', 1200);

        $this->seedEasyQuestions($easy);
        $this->seedMediumQuestions($medium);
        $this->seedHardQuestions($hard);
    }

    private function seedMaterials(Chapter $chapter): void
    {
        $materials = [
            [
                'type' => 'text',
                'title' => 'Mengenal Bilangan Berpangkat',
                'content' => <<<'MD'
## Apa itu eksponen?

Eksponen (bilangan berpangkat) adalah cara singkat menulis perkalian berulang.

```
a^n = a × a × a × ... × a   (sebanyak n kali)
```

- `a` disebut **basis** (bilangan pokok)
- `n` disebut **eksponen** atau pangkat

**Contoh:** `2^5 = 2 × 2 × 2 × 2 × 2 = 32`

Kalau pangkatnya 0? `a^0 = 1` untuk setiap `a ≠ 0`.
Kalau pangkatnya negatif? `a^-n = 1 / a^n`.
MD,
                'source_reference' => 'Buku Siswa Matematika Kelas X — Bab Eksponen',
                'order' => 1,
                'duration' => 240,
            ],
            [
                'type' => 'text',
                'title' => 'Sifat-Sifat Eksponen',
                'content' => <<<'MD'
## Sifat utama eksponen

| Sifat | Rumus |
|-------|-------|
| Perkalian | `a^m × a^n = a^(m+n)` |
| Pembagian | `a^m ÷ a^n = a^(m-n)` |
| Pangkat berpangkat | `(a^m)^n = a^(m×n)` |
| Pangkat dari perkalian | `(a × b)^n = a^n × b^n` |
| Pangkat nol | `a^0 = 1` |
| Pangkat negatif | `a^-n = 1 / a^n` |
| Pangkat pecahan | `a^(m/n) = ⁿ√(a^m)` |

**Contoh cepat:**
- `2^3 × 2^4 = 2^(3+4) = 2^7 = 128`
- `5^6 ÷ 5^2 = 5^4 = 625`
- `(3^2)^3 = 3^6 = 729`
MD,
                'source_reference' => 'Buku Siswa Matematika Kelas X — Bab Eksponen',
                'order' => 2,
                'duration' => 300,
            ],
            [
                'type' => 'interactive',
                'title' => 'Mini Game: Sederhanakan Eksponen',
                'content' => 'Pilih bentuk paling sederhana dari setiap eksponen yang muncul. Waktu terbatas!',
                'blocks' => [
                    ['type' => 'prompt', 'value' => 'Sederhanakan: 2^3 × 2^2'],
                    ['type' => 'answer', 'value' => '2^5'],
                ],
                'order' => 3,
                'duration' => 120,
            ],
        ];

        foreach ($materials as $material) {
            $chapter->materials()->updateOrCreate(
                ['title' => $material['title']],
                [...$material, 'is_active' => true],
            );
        }
    }

    private function seedAssessment(Chapter $chapter, Difficulty $difficulty, string $title, int $duration): Assessment
    {
        return $chapter->assessments()->updateOrCreate(
            ['difficulty' => $difficulty->value],
            [
                'title' => $title,
                'duration' => $duration,
                'passing_score' => 70,
                'order' => match ($difficulty) {
                    Difficulty::Easy => 1,
                    Difficulty::Medium => 2,
                    Difficulty::Hard => 3,
                },
                'is_active' => true,
            ],
        );
    }

    /**
     * @param  array<int, array{text: string, correct?: bool}>  $options
     */
    private function createChoice(
        Assessment $assessment,
        int $order,
        string $question,
        array $options,
        string $explanation,
        int $points,
        ?string $hint = null,
    ): void {
        $model = $assessment->questions()->updateOrCreate(
            ['order' => $order],
            [
                'type' => QuestionType::MultipleChoice->value,
                'question' => $question,
                'correct_answer' => [
                    'text' => collect($options)->firstWhere('correct', true)['text'] ?? null,
                ],
                'explanation' => $explanation,
                'hint' => $hint,
                'points' => $points,
                'order' => $order,
                'ai_assisted' => false,
            ],
        );

        $model->questionOptions()->delete();

        foreach ($options as $index => $option) {
            QuestionOption::create([
                'question_id' => $model->id,
                'label' => chr(65 + $index),
                'text' => $option['text'],
                'is_correct' => $option['correct'] ?? false,
                'order' => $index + 1,
            ]);
        }
    }

    /**
     * @param  array<int, array{point: string, weight: int}>  $rubric
     */
    private function createEssay(
        Assessment $assessment,
        int $order,
        string $question,
        array $rubric,
        string $guideline,
        int $points,
    ): void {
        $assessment->questions()->updateOrCreate(
            ['order' => $order],
            [
                'type' => QuestionType::Essay->value,
                'question' => $question,
                'correct_answer' => ['guideline' => $guideline],
                'rubric' => $rubric,
                'explanation' => $guideline,
                'points' => $points,
                'order' => $order,
                'ai_assisted' => true,
            ],
        );
    }

    /**
     * @param  array<int, array{text: string, correct?: bool}>  $options
     */
    private function createOptionQuestion(
        Assessment $assessment,
        int $order,
        QuestionType $type,
        string $question,
        array $options,
        string $explanation,
        int $points,
        ?string $hint = null,
    ): void {
        $model = $assessment->questions()->updateOrCreate(
            ['order' => $order],
            [
                'type' => $type->value,
                'question' => $question,
                'correct_answer' => [
                    'texts' => collect($options)->where('correct', true)->pluck('text')->all(),
                ],
                'explanation' => $explanation,
                'hint' => $hint,
                'points' => $points,
                'order' => $order,
                'ai_assisted' => false,
            ],
        );

        $model->questionOptions()->delete();

        foreach ($options as $index => $option) {
            QuestionOption::create([
                'question_id' => $model->id,
                'label' => chr(65 + $index),
                'text' => $option['text'],
                'is_correct' => $option['correct'] ?? false,
                'order' => $index + 1,
            ]);
        }
    }

    /**
     * @param  array<int, array<string, string>>  $payload
     * @param  array<string, mixed>  $correctAnswer
     */
    private function createInteractive(
        Assessment $assessment,
        int $order,
        QuestionType $type,
        string $question,
        array $payload,
        array $correctAnswer,
        string $explanation,
        int $points,
        ?string $hint = null,
    ): void {
        $model = $assessment->questions()->updateOrCreate(
            ['order' => $order],
            [
                'type' => $type->value,
                'question' => $question,
                'options' => $payload,
                'correct_answer' => $correctAnswer,
                'explanation' => $explanation,
                'hint' => $hint,
                'points' => $points,
                'order' => $order,
                'ai_assisted' => false,
            ],
        );

        $model->questionOptions()->delete();
    }

    private function seedEasyQuestions(Assessment $assessment): void
    {
        $this->createChoice($assessment, 1,
            'Berapakah hasil dari 2³?',
            [
                ['text' => '6'],
                ['text' => '8', 'correct' => true],
                ['text' => '9'],
                ['text' => '12'],
            ],
            '2³ = 2 × 2 × 2 = 8.',
            10,
            'Kalikan angka 2 sebanyak tiga kali.',
        );

        $this->createChoice($assessment, 2,
            'Berapakah hasil dari 5²?',
            [
                ['text' => '10'],
                ['text' => '15'],
                ['text' => '25', 'correct' => true],
                ['text' => '32'],
            ],
            '5² = 5 × 5 = 25.',
            10,
        );

        $this->createChoice($assessment, 3,
            'Berapakah nilai dari 3⁰?',
            [
                ['text' => '0'],
                ['text' => '1', 'correct' => true],
                ['text' => '3'],
                ['text' => 'Tidak terdefinisi'],
            ],
            'Setiap bilangan bukan nol yang dipangkatkan 0 hasilnya 1.',
            10,
        );

        $this->createChoice($assessment, 4,
            'Bentuk perkalian berulang dari 4⁵ adalah …',
            [
                ['text' => '4 × 5'],
                ['text' => '5 × 5 × 5 × 5'],
                ['text' => '4 × 4 × 4 × 4 × 4', 'correct' => true],
                ['text' => '4 + 4 + 4 + 4 + 4'],
            ],
            'Eksponen menunjukkan banyaknya faktor basis yang dikalikan.',
            10,
        );

        $this->createChoice($assessment, 5,
            'Berapakah hasil dari 10³?',
            [
                ['text' => '30'],
                ['text' => '100'],
                ['text' => '1.000', 'correct' => true],
                ['text' => '10.000'],
            ],
            '10³ = 10 × 10 × 10 = 1.000.',
            10,
        );
    }

    private function seedMediumQuestions(Assessment $assessment): void
    {
        $this->createChoice($assessment, 1,
            'Bentuk sederhana dari 2³ × 2⁴ adalah …',
            [
                ['text' => '2⁷', 'correct' => true],
                ['text' => '2¹²'],
                ['text' => '4⁷'],
                ['text' => '2¹'],
            ],
            'a^m × a^n = a^(m+n), sehingga 2^(3+4) = 2⁷.',
            20,
            'Jumlahkan pangkatnya karena basisnya sama.',
        );

        $this->createChoice($assessment, 2,
            'Bentuk sederhana dari (3²)³ adalah …',
            [
                ['text' => '3⁵'],
                ['text' => '3⁶', 'correct' => true],
                ['text' => '3⁹'],
                ['text' => '9⁶'],
            ],
            '(a^m)^n = a^(m×n), sehingga (3²)³ = 3⁶.',
            20,
        );

        $this->createChoice($assessment, 3,
            'Hasil dari 5⁶ ÷ 5² adalah …',
            [
                ['text' => '5³'],
                ['text' => '5⁴', 'correct' => true],
                ['text' => '5⁸'],
                ['text' => '1⁴'],
            ],
            'a^m ÷ a^n = a^(m−n), sehingga 5^(6−2) = 5⁴.',
            20,
        );

        $this->createChoice($assessment, 4,
            'Nilai dari 2⁻² adalah …',
            [
                ['text' => '−4'],
                ['text' => '−1/4'],
                ['text' => '1/4', 'correct' => true],
                ['text' => '4'],
            ],
            'a⁻ⁿ = 1/aⁿ, sehingga 2⁻² = 1/2² = 1/4.',
            20,
        );

        $this->createChoice($assessment, 5,
            'Bentuk sederhana dari (2x³)² adalah …',
            [
                ['text' => '2x⁶'],
                ['text' => '4x⁵'],
                ['text' => '4x⁶', 'correct' => true],
                ['text' => '4x⁹'],
            ],
            '(2x³)² = 2² × (x³)² = 4x⁶.',
            20,
        );

        $this->createEssay($assessment, 6,
            'Jelaskan mengapa a⁰ = 1 untuk setiap a ≠ 0. Gunakan sifat pembagian eksponen dalam penjelasanmu.',
            [
                ['point' => 'Menyebutkan sifat pembagian eksponen a^m ÷ a^n = a^(m−n)', 'weight' => 30],
                ['point' => 'Mengambil contoh seperti a^3 ÷ a^3 = a^0', 'weight' => 30],
                ['point' => 'Menyimpulkan bahwa hasil pembagian bilangan yang sama adalah 1', 'weight' => 30],
                ['point' => 'Menyebutkan syarat a ≠ 0', 'weight' => 10],
            ],
            'Karena a^m ÷ a^m = a^(m−m) = a^0, sementara membagi bilangan dengan bilangan itu sendiri (bukan nol) hasilnya 1, maka a⁰ = 1 dengan syarat a ≠ 0.',
            40,
        );

        $this->createOptionQuestion($assessment, 7,
            QuestionType::MultipleAnswer,
            'Manakah pernyataan berikut yang bernilai benar? Pilih semua jawaban yang tepat.',
            [
                ['text' => '2³ × 2⁴ = 2⁷', 'correct' => true],
                ['text' => '(3²)³ = 3⁹'],
                ['text' => '5⁰ = 1', 'correct' => true],
                ['text' => '2⁻³ = −8'],
                ['text' => '(2x)² = 4x²', 'correct' => true],
            ],
            '2³ × 2⁴ = 2⁷, 5⁰ = 1, dan (2x)² = 4x². Sementara (3²)³ = 3⁶ dan 2⁻³ = 1/8.',
            20,
            'Periksa satu per satu dengan sifat eksponen, jangan terkecoh tanda negatif.',
        );

        $this->createInteractive($assessment, 8,
            QuestionType::DragDrop,
            'Urutkan langkah menyederhanakan (2³ × 2⁴) ÷ 2² dari langkah pertama hingga hasil akhir.',
            [
                ['id' => 'a', 'text' => 'Tulis bentuk: (2³ × 2⁴) ÷ 2²'],
                ['id' => 'b', 'text' => 'Gabungkan pangkat pembilang: 2³⁺⁴ = 2⁷'],
                ['id' => 'c', 'text' => 'Gunakan sifat pembagian: 2⁷ ÷ 2² = 2⁷⁻²'],
                ['id' => 'd', 'text' => 'Sederhanakan menjadi 2⁵'],
            ],
            ['order' => ['a', 'b', 'c', 'd']],
            'Pembilang disederhanakan lebih dulu menjadi 2⁷, lalu dibagi 2² sehingga 2⁵.',
            25,
            'Kerjakan operasi di dalam tanda kurung terlebih dahulu.',
        );
    }

    private function seedHardQuestions(Assessment $assessment): void
    {
        $this->createChoice($assessment, 1,
            'Nilai x yang memenuhi 2^(x+1) = 32 adalah …',
            [
                ['text' => '3'],
                ['text' => '4', 'correct' => true],
                ['text' => '5'],
                ['text' => '6'],
            ],
            '32 = 2⁵, sehingga x + 1 = 5 dan x = 4.',
            30,
        );

        $this->createChoice($assessment, 2,
            'Bentuk sederhana dari (a²b⁻¹)³ ÷ (a⁻¹b²) adalah …',
            [
                ['text' => 'a⁷ / b⁵', 'correct' => true],
                ['text' => 'a⁵ / b⁷'],
                ['text' => 'a⁷b⁵'],
                ['text' => 'a⁵b⁷'],
            ],
            '(a²b⁻¹)³ = a⁶b⁻³. Dibagi a⁻¹b² menjadi a^(6+1) b^(−3−2) = a⁷b⁻⁵ = a⁷/b⁵.',
            30,
        );

        $this->createChoice($assessment, 3,
            'Nilai dari 27^(2/3) adalah …',
            [
                ['text' => '3'],
                ['text' => '6'],
                ['text' => '9', 'correct' => true],
                ['text' => '18'],
            ],
            '27^(2/3) = (∛27)² = 3² = 9.',
            30,
        );

        $this->createChoice($assessment, 4,
            'Jika 3ˣ = 81, maka nilai 3^(x−2) adalah …',
            [
                ['text' => '3'],
                ['text' => '9', 'correct' => true],
                ['text' => '27'],
                ['text' => '79'],
            ],
            '3^(x−2) = 3ˣ ÷ 3² = 81 ÷ 9 = 9.',
            30,
        );

        $this->createChoice($assessment, 5,
            'Populasi bakteri mengikuti model P(t) = 1.000 × 2ᵗ, dengan t dalam jam. Berapa populasi setelah 4 jam?',
            [
                ['text' => '4.000'],
                ['text' => '8.000'],
                ['text' => '16.000', 'correct' => true],
                ['text' => '32.000'],
            ],
            'P(4) = 1.000 × 2⁴ = 1.000 × 16 = 16.000.',
            30,
        );

        $this->createEssay($assessment, 6,
            'Seorang siswa menabung Rp5.000.000 dengan bunga majemuk 8% per tahun. Tuliskan model eksponen untuk nilai tabungan setelah t tahun, lalu hitung nilainya setelah 3 tahun (bulatkan ke rupiah terdekat). Tunjukkan langkah perhitunganmu.',
            [
                ['point' => 'Menuliskan model M(t) = 5.000.000 × (1,08)^t', 'weight' => 30],
                ['point' => 'Substitusi t = 3 ke dalam model', 'weight' => 25],
                ['point' => 'Menghitung (1,08)³ dengan benar', 'weight' => 25],
                ['point' => 'Hasil akhir ± Rp6.298.560 dan pembulatan yang tepat', 'weight' => 20],
            ],
            'M(t) = 5.000.000(1,08)^t. Untuk t = 3: 5.000.000 × 1,259712 = Rp6.298.560.',
            60,
        );

        $this->createInteractive($assessment, 7,
            QuestionType::Matching,
            'Jodohkan setiap bentuk eksponen dengan nilainya yang tepat.',
            [
                ['id' => 'p1', 'left' => '2⁵', 'right' => '32'],
                ['id' => 'p2', 'left' => '3⁴', 'right' => '81'],
                ['id' => 'p3', 'left' => '27^(2/3)', 'right' => '9'],
                ['id' => 'p4', 'left' => '2⁻³', 'right' => '1/8'],
            ],
            [
                'pairs' => [
                    'p1' => '32',
                    'p2' => '81',
                    'p3' => '9',
                    'p4' => '1/8',
                ],
            ],
            '2⁵ = 32, 3⁴ = 81, 27^(2/3) = 9, dan 2⁻³ = 1/8.',
            30,
            'Hitung nilai setiap bentuk, lalu pasangkan dengan hasilnya.',
        );

        $this->createInteractive($assessment, 8,
            QuestionType::Puzzle,
            'Susun bukti bahwa a⁰ = 1 untuk a ≠ 0 dalam urutan yang logis.',
            [
                ['id' => 's1', 'text' => 'Mulai dari bentuk aⁿ ÷ aⁿ'],
                ['id' => 's2', 'text' => 'Gunakan sifat pembagian: aⁿ ÷ aⁿ = aⁿ⁻ⁿ'],
                ['id' => 's3', 'text' => 'Karena n − n = 0, bentuknya menjadi a⁰'],
                ['id' => 's4', 'text' => 'Di sisi lain, membagi bilangan bukan nol dengan dirinya sendiri hasilnya 1'],
                ['id' => 's5', 'text' => 'Jadi a⁰ = 1 dengan syarat a ≠ 0'],
            ],
            ['order' => ['s1', 's2', 's3', 's4', 's5']],
            'Bukti dimulai dari aⁿ ÷ aⁿ, disederhanakan menjadi a⁰, lalu dibandingkan dengan hasil pembagian yang bernilai 1.',
            30,
            'Mulai dari dua bentuk yang sama, lalu gunakan sifat pembagian.',
        );

        $this->createOptionQuestion($assessment, 9,
            QuestionType::Simulation,
            'Seorang siswa harus menyederhanakan (2³ × 2⁵) ÷ 2⁴. Keputusan mana yang paling tepat?',
            [
                ['text' => 'Jumlahkan semua pangkat sehingga hasilnya 2¹²'],
                ['text' => 'Gabungkan pembilang menjadi 2⁸, lalu bagi 2⁴ menjadi 2⁴', 'correct' => true],
                ['text' => 'Kalikan basis dengan semua pangkat: 2 × 3 × 5 ÷ 4'],
                ['text' => 'Kurangkan 4 dari masing-masing pangkat secara terpisah'],
            ],
            'Pembilang 2³ × 2⁵ = 2⁸. Kemudian 2⁸ ÷ 2⁴ = 2⁴.',
            30,
            'Sederhanakan pembilang terlebih dahulu, baru gunakan sifat pembagian.',
        );
    }
}
