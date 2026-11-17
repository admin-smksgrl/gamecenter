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
 * Kurasi materi lintas jenjang (PAUD, TK, SMP, SMK).
 *
 * Sumber acuan: buku siswa & modul ajar Kurikulum Merdeka (SIBI). Isi soal
 * ditulis ulang secara ringkas agar cocok dimainkan, bukan salinan mentah.
 */
class CuratedContentSeeder extends Seeder
{
    public function run(): void
    {
        $this->seedPaudShapes();
        $this->seedTkCounting();
        $this->seedSmpIntegers();
        $this->seedSmkAlgorithms();
    }

    private function seedPaudShapes(): void
    {
        $this->seedChapter('paud', 'kb', 'bentuk-warna', [
            'slug' => 'bentuk-dasar',
            'code' => 'PAUD 1.1',
            'title' => 'Mengenal Bentuk Dasar',
            'description' => 'Mengenali lingkaran, persegi, segitiga, dan persegi panjang lewat benda di sekitar.',
            'learning_objectives' => [
                'Menunjukkan benda yang berbentuk lingkaran, persegi, segitiga, dan persegi panjang.',
                'Menyebutkan jumlah sisi pada bentuk dasar.',
                'Mengelompokkan benda berdasarkan bentuknya.',
            ],
            'estimated_minutes' => 45,
            'materials' => [
                [
                    'type' => 'text',
                    'title' => 'Bentuk di Sekitar Kita',
                    'content' => <<<'MD'
## Empat bentuk dasar

- **Lingkaran** ⭕ tidak punya sudut. Contoh: roda, bola, uang koin.
- **Persegi** ⬜ punya 4 sisi sama panjang. Contoh: dadu, papan catur.
- **Segitiga** 🔺 punya 3 sisi. Contoh: atap tenda, rambu jalan.
- **Persegi panjang** ▭ punya 4 sisi, dua sisi lebih panjang. Contoh: pintu, buku.

**Ingat:** bentuk berbeda punya jumlah sisi berbeda.
MD,
                    'duration' => 180,
                    'source_reference' => 'Buku Siswa PAUD — Mengenal Bentuk dan Warna',
                ],
                [
                    'type' => 'interactive',
                    'title' => 'Cari Pasangan Bentuk',
                    'content' => 'Tarik garis dari bentuk ke benda yang mirip.',
                    'blocks' => [
                        ['type' => 'prompt', 'value' => 'Lingkaran → ?'],
                        ['type' => 'answer', 'value' => 'Bola'],
                    ],
                    'duration' => 120,
                    'source_reference' => 'Modul Ajar PAUD — Bentuk Dasar',
                ],
            ],
            'assessments' => [
                'easy' => [
                    'title' => 'Bentuk Dasar — Mudah',
                    'duration' => 480,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk roda sepeda adalah …',
                            'options' => [
                                ['text' => '⭕ Lingkaran', 'correct' => true],
                                ['text' => '⬜ Persegi'],
                                ['text' => '🔺 Segitiga'],
                                ['text' => '⭐ Bintang'],
                            ],
                            'explanation' => 'Roda berbentuk lingkaran karena tidak memiliki sudut.',
                            'points' => 10,
                            'hint' => 'Lihat bentuk roda saat berputar.',
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk pintu rumah biasanya …',
                            'options' => [
                                ['text' => 'Persegi panjang', 'correct' => true],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Segitiga'],
                                ['text' => 'Hati'],
                            ],
                            'explanation' => 'Pintu umumnya berbentuk persegi panjang.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Atap tenda berbentuk …',
                            'options' => [
                                ['text' => '🔺 Segitiga', 'correct' => true],
                                ['text' => '⬜ Persegi'],
                                ['text' => '⭕ Lingkaran'],
                                ['text' => '▭ Persegi panjang'],
                            ],
                            'explanation' => 'Atap tenda runcing seperti segitiga.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Benda yang berbentuk lingkaran adalah …',
                            'options' => [
                                ['text' => '⚽ Bola', 'correct' => true],
                                ['text' => '📕 Buku'],
                                ['text' => '📏 Penggaris'],
                                ['text' => '🎲 Dadu'],
                            ],
                            'explanation' => 'Bola bulat seperti lingkaran.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Papan tulis di kelas berbentuk …',
                            'options' => [
                                ['text' => 'Persegi panjang', 'correct' => true],
                                ['text' => 'Segitiga'],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Bintang'],
                            ],
                            'explanation' => 'Papan tulis lebih panjang daripada lebarnya.',
                            'points' => 10,
                        ],
                    ],
                ],
                'medium' => [
                    'title' => 'Bentuk Dasar — Sedang',
                    'duration' => 600,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk yang memiliki 4 sisi sama panjang adalah …',
                            'options' => [
                                ['text' => 'Persegi', 'correct' => true],
                                ['text' => 'Segitiga'],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Oval'],
                            ],
                            'explanation' => 'Persegi punya empat sisi yang sama panjang.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk yang memiliki 3 sisi adalah …',
                            'options' => [
                                ['text' => 'Segitiga', 'correct' => true],
                                ['text' => 'Persegi'],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Persegi panjang'],
                            ],
                            'explanation' => 'Segitiga memiliki tiga sisi.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Manakah yang bukan bentuk dasar?',
                            'options' => [
                                ['text' => 'Hati', 'correct' => true],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Persegi'],
                                ['text' => 'Segitiga'],
                            ],
                            'explanation' => 'Hati bukan termasuk bentuk dasar yang dipelajari.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk telur lebih mirip dengan …',
                            'options' => [
                                ['text' => 'Oval', 'correct' => true],
                                ['text' => 'Persegi'],
                                ['text' => 'Segitiga'],
                                ['text' => 'Bintang'],
                            ],
                            'explanation' => 'Telur berbentuk oval atau bulat lonjong.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'drag_drop',
                            'question' => 'Urutkan bentuk dari sisi paling sedikit ke paling banyak.',
                            'payload' => [
                                ['id' => 'a', 'text' => 'Segitiga (3 sisi)'],
                                ['id' => 'b', 'text' => 'Persegi (4 sisi)'],
                                ['id' => 'c', 'text' => 'Segi lima (5 sisi)'],
                            ],
                            'correct' => ['order' => ['a', 'b', 'c']],
                            'explanation' => 'Segitiga 3 sisi, persegi 4 sisi, segi lima 5 sisi.',
                            'points' => 20,
                        ],
                    ],
                ],
                'hard' => [
                    'title' => 'Bentuk Dasar — Sulit',
                    'duration' => 720,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bentuk yang memiliki 5 sisi disebut …',
                            'options' => [
                                ['text' => 'Segi lima', 'correct' => true],
                                ['text' => 'Segitiga'],
                                ['text' => 'Persegi'],
                                ['text' => 'Lingkaran'],
                            ],
                            'explanation' => 'Segi lima memiliki lima sisi.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Dua segitiga siku-siku dapat digabung menjadi …',
                            'options' => [
                                ['text' => 'Persegi', 'correct' => true],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Oval'],
                                ['text' => 'Bintang'],
                            ],
                            'explanation' => 'Dua segitiga siku-siku yang sama dapat membentuk persegi.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Benda yang paling mirip bola adalah …',
                            'options' => [
                                ['text' => 'Bola dunia', 'correct' => true],
                                ['text' => 'Buku'],
                                ['text' => 'Pensil'],
                                ['text' => 'Penggaris'],
                            ],
                            'explanation' => 'Bola dunia berbentuk bulat seperti bola.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'matching',
                            'question' => 'Jodohkan bentuk dengan benda yang mirip.',
                            'payload' => [
                                ['id' => 'p1', 'left' => 'Lingkaran', 'right' => 'Bola'],
                                ['id' => 'p2', 'left' => 'Persegi', 'right' => 'Dadu'],
                                ['id' => 'p3', 'left' => 'Segitiga', 'right' => 'Atap rumah'],
                                ['id' => 'p4', 'left' => 'Persegi panjang', 'right' => 'Pintu'],
                            ],
                            'correct' => [
                                'pairs' => [
                                    'p1' => 'Bola',
                                    'p2' => 'Dadu',
                                    'p3' => 'Atap rumah',
                                    'p4' => 'Pintu',
                                ],
                            ],
                            'explanation' => 'Setiap benda memiliki bentuk dasar yang paling mirip.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'simulation',
                            'question' => 'Kamu melihat rambu STOP berbentuk segi delapan. Bentuk apa itu?',
                            'options' => [
                                ['text' => 'Segi delapan', 'correct' => true],
                                ['text' => 'Lingkaran'],
                                ['text' => 'Segitiga'],
                                ['text' => 'Persegi'],
                            ],
                            'explanation' => 'Rambu STOP memiliki delapan sisi.',
                            'points' => 30,
                        ],
                    ],
                ],
            ],
        ]);
    }

    private function seedTkCounting(): void
    {
        $this->seedChapter('tk', 'tk-a', 'numerasi-awal', [
            'slug' => 'berhitung-1-10',
            'code' => 'TK 1.1',
            'title' => 'Berhitung 1–10',
            'description' => 'Membilang, menjumlah, dan mengurang bilangan 1 sampai 10 dengan benda konkret.',
            'learning_objectives' => [
                'Membilang benda dari 1 sampai 10.',
                'Menjumlah dua bilangan dengan hasil sampai 10.',
                'Mengurangi bilangan dengan hasil tidak negatif.',
            ],
            'estimated_minutes' => 50,
            'materials' => [
                [
                    'type' => 'text',
                    'title' => 'Membilang Benda',
                    'content' => <<<'MD'
## Bilangan 1–10

Hitung benda satu per satu sambil menunjuk:

1. Satu apel 🍎
2. Dua bola ⚽⚽
3. Tiga bintang ⭐⭐⭐

**Tambah** berarti menggabungkan. **Kurang** berarti mengambil sebagian.

Contoh: 3 permen + 2 permen = 5 permen.
MD,
                    'duration' => 180,
                    'source_reference' => 'Buku Siswa TK — Numerasi Awal',
                ],
                [
                    'type' => 'interactive',
                    'title' => 'Hitung Jari',
                    'content' => 'Angkat jari sesuai bilangan yang muncul.',
                    'blocks' => [
                        ['type' => 'prompt', 'value' => 'Tunjukkan 4 jari'],
                        ['type' => 'answer', 'value' => 'Empat jari terangkat'],
                    ],
                    'duration' => 120,
                    'source_reference' => 'Modul Ajar TK — Berhitung 1–10',
                ],
            ],
            'assessments' => [
                'easy' => [
                    'title' => 'Berhitung — Mudah',
                    'duration' => 480,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => '3 + 2 = …',
                            'options' => [
                                ['text' => '5', 'correct' => true],
                                ['text' => '4'],
                                ['text' => '6'],
                                ['text' => '7'],
                            ],
                            'explanation' => 'Tiga ditambah dua sama dengan lima.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => '4 + 1 = …',
                            'options' => [
                                ['text' => '5', 'correct' => true],
                                ['text' => '3'],
                                ['text' => '6'],
                                ['text' => '4'],
                            ],
                            'explanation' => 'Empat ditambah satu sama dengan lima.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => '6 − 2 = …',
                            'options' => [
                                ['text' => '4', 'correct' => true],
                                ['text' => '5'],
                                ['text' => '3'],
                                ['text' => '8'],
                            ],
                            'explanation' => 'Enam diambil dua tersisa empat.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Angka setelah 7 adalah …',
                            'options' => [
                                ['text' => '8', 'correct' => true],
                                ['text' => '6'],
                                ['text' => '9'],
                                ['text' => '5'],
                            ],
                            'explanation' => 'Urutan bilangan: 7 lalu 8.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Angka sebelum 5 adalah …',
                            'options' => [
                                ['text' => '4', 'correct' => true],
                                ['text' => '6'],
                                ['text' => '3'],
                                ['text' => '7'],
                            ],
                            'explanation' => 'Urutan bilangan: 4 lalu 5.',
                            'points' => 10,
                        ],
                    ],
                ],
                'medium' => [
                    'title' => 'Berhitung — Sedang',
                    'duration' => 600,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => '5 + 5 = …',
                            'options' => [
                                ['text' => '10', 'correct' => true],
                                ['text' => '9'],
                                ['text' => '8'],
                                ['text' => '11'],
                            ],
                            'explanation' => 'Lima ditambah lima sama dengan sepuluh.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => '9 − 4 = …',
                            'options' => [
                                ['text' => '5', 'correct' => true],
                                ['text' => '4'],
                                ['text' => '6'],
                                ['text' => '3'],
                            ],
                            'explanation' => 'Sembilan diambil empat tersisa lima.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => '2 + 2 + 2 = …',
                            'options' => [
                                ['text' => '6', 'correct' => true],
                                ['text' => '4'],
                                ['text' => '5'],
                                ['text' => '8'],
                            ],
                            'explanation' => 'Dua ditambah dua ditambah dua sama dengan enam.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Bilangan yang lebih besar adalah …',
                            'options' => [
                                ['text' => '7', 'correct' => true],
                                ['text' => '5'],
                                ['text' => '3'],
                                ['text' => '1'],
                            ],
                            'explanation' => 'Tujuh lebih besar daripada lima, tiga, dan satu.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'drag_drop',
                            'question' => 'Urutkan bilangan dari kecil ke besar.',
                            'payload' => [
                                ['id' => 'a', 'text' => '1'],
                                ['id' => 'b', 'text' => '2'],
                                ['id' => 'c', 'text' => '3'],
                                ['id' => 'd', 'text' => '4'],
                                ['id' => 'e', 'text' => '5'],
                            ],
                            'correct' => ['order' => ['a', 'b', 'c', 'd', 'e']],
                            'explanation' => 'Urutan bilangan dimulai dari 1 sampai 5.',
                            'points' => 20,
                        ],
                    ],
                ],
                'hard' => [
                    'title' => 'Berhitung — Sulit',
                    'duration' => 720,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => '10 − 3 − 2 = …',
                            'options' => [
                                ['text' => '5', 'correct' => true],
                                ['text' => '6'],
                                ['text' => '4'],
                                ['text' => '7'],
                            ],
                            'explanation' => 'Sepuluh diambil tiga menjadi tujuh, lalu diambil dua menjadi lima.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => '3 + 4 + 2 = …',
                            'options' => [
                                ['text' => '9', 'correct' => true],
                                ['text' => '8'],
                                ['text' => '10'],
                                ['text' => '7'],
                            ],
                            'explanation' => 'Tiga ditambah empat ditambah dua sama dengan sembilan.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Ada 6 sepatu. Berapa pasang sepatu?',
                            'options' => [
                                ['text' => '3 pasang', 'correct' => true],
                                ['text' => '6 pasang'],
                                ['text' => '2 pasang'],
                                ['text' => '4 pasang'],
                            ],
                            'explanation' => 'Setiap pasang berisi 2 sepatu, jadi 6 ÷ 2 = 3 pasang.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'matching',
                            'question' => 'Jodohkan operasi dengan hasilnya.',
                            'payload' => [
                                ['id' => 'p1', 'left' => '2 + 2', 'right' => '4'],
                                ['id' => 'p2', 'left' => '5 + 3', 'right' => '8'],
                                ['id' => 'p3', 'left' => '10 − 4', 'right' => '6'],
                                ['id' => 'p4', 'left' => '9 − 2', 'right' => '7'],
                            ],
                            'correct' => [
                                'pairs' => [
                                    'p1' => '4',
                                    'p2' => '8',
                                    'p3' => '6',
                                    'p4' => '7',
                                ],
                            ],
                            'explanation' => 'Hitung setiap operasi lalu pasangkan hasilnya.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'simulation',
                            'question' => 'Kamu punya 5 permen dan memberi 2 kepada teman. Berapa sisa permenmu?',
                            'options' => [
                                ['text' => '3 permen', 'correct' => true],
                                ['text' => '2 permen'],
                                ['text' => '7 permen'],
                                ['text' => '5 permen'],
                            ],
                            'explanation' => '5 − 2 = 3, jadi sisa 3 permen.',
                            'points' => 30,
                        ],
                    ],
                ],
            ],
        ]);
    }

    private function seedSmpIntegers(): void
    {
        $this->seedChapter('smp', 'kelas-7', 'matematika', [
            'slug' => 'bilangan-bulat',
            'code' => 'MTK 7.1',
            'title' => 'Bilangan Bulat',
            'description' => 'Membandingkan, menjumlah, mengurang, mengali, dan membagi bilangan bulat positif serta negatif.',
            'learning_objectives' => [
                'Membandingkan dan mengurutkan bilangan bulat.',
                'Menghitung operasi campuran bilangan bulat.',
                'Menyelesaikan masalah kontekstual dengan bilangan bulat.',
            ],
            'estimated_minutes' => 120,
            'materials' => [
                [
                    'type' => 'text',
                    'title' => 'Mengenal Bilangan Bulat',
                    'content' => <<<'MD'
## Bilangan bulat

Bilangan bulat terdiri dari bilangan negatif, nol, dan bilangan positif.

```
… −3, −2, −1, 0, 1, 2, 3 …
```

- Semakin ke kanan pada garis bilangan, nilainya semakin besar.
- **Nilai mutlak** `|a|` adalah jarak dari nol, selalu positif.
- `−5 < −2` karena −5 berada lebih kiri.

**Operasi tanda:**
- `(+) × (+) = (+)`
- `(−) × (−) = (+)`
- `(+) × (−) = (−)`
MD,
                    'duration' => 300,
                    'source_reference' => 'Buku Siswa Matematika Kelas VII — Bilangan Bulat',
                ],
                [
                    'type' => 'text',
                    'title' => 'Operasi Campuran',
                    'content' => <<<'MD'
## Urutan pengerjaan

1. Kerjakan operasi di dalam kurung.
2. Kerjakan perkalian dan pembagian dari kiri ke kanan.
3. Kerjakan penjumlahan dan pengurangan dari kiri ke kanan.

**Contoh:**
`−3 × (4 − 7) = −3 × (−3) = 9`

**Masalah suhu:**
Suhu awal −5 °C, lalu naik 8 °C. Suhu akhir = −5 + 8 = 3 °C.
MD,
                    'duration' => 300,
                    'source_reference' => 'Modul Ajar Matematika Kelas VII — Operasi Bilangan Bulat',
                ],
            ],
            'assessments' => [
                'easy' => [
                    'title' => 'Bilangan Bulat — Mudah',
                    'duration' => 600,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari −3 + 5 adalah …',
                            'options' => [
                                ['text' => '2', 'correct' => true],
                                ['text' => '−2'],
                                ['text' => '8'],
                                ['text' => '−8'],
                            ],
                            'explanation' => '−3 + 5 = 2 karena bergerak 5 langkah ke kanan dari −3.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari 4 − (−2) adalah …',
                            'options' => [
                                ['text' => '6', 'correct' => true],
                                ['text' => '2'],
                                ['text' => '−6'],
                                ['text' => '−2'],
                            ],
                            'explanation' => 'Mengurangi bilangan negatif sama dengan menambah: 4 + 2 = 6.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari −5 × 2 adalah …',
                            'options' => [
                                ['text' => '−10', 'correct' => true],
                                ['text' => '10'],
                                ['text' => '−7'],
                                ['text' => '7'],
                            ],
                            'explanation' => 'Bilangan negatif dikali positif menghasilkan negatif.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Urutan dari terkecil ke terbesar adalah …',
                            'options' => [
                                ['text' => '−3, −1, 0, 2', 'correct' => true],
                                ['text' => '0, −1, 2, −3'],
                                ['text' => '2, 0, −1, −3'],
                                ['text' => '−1, −3, 0, 2'],
                            ],
                            'explanation' => 'Pada garis bilangan, −3 paling kiri lalu −1, 0, dan 2.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Nilai dari |−7| adalah …',
                            'options' => [
                                ['text' => '7', 'correct' => true],
                                ['text' => '−7'],
                                ['text' => '0'],
                                ['text' => '14'],
                            ],
                            'explanation' => 'Nilai mutlak adalah jarak dari nol, jadi |−7| = 7.',
                            'points' => 10,
                        ],
                    ],
                ],
                'medium' => [
                    'title' => 'Bilangan Bulat — Sedang',
                    'duration' => 900,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari −12 ÷ 3 adalah …',
                            'options' => [
                                ['text' => '−4', 'correct' => true],
                                ['text' => '4'],
                                ['text' => '−9'],
                                ['text' => '9'],
                            ],
                            'explanation' => 'Negatif dibagi positif menghasilkan negatif: −12 ÷ 3 = −4.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari (−4) × (−5) adalah …',
                            'options' => [
                                ['text' => '20', 'correct' => true],
                                ['text' => '−20'],
                                ['text' => '−9'],
                                ['text' => '9'],
                            ],
                            'explanation' => 'Negatif dikali negatif menghasilkan positif.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari 8 + (−15) adalah …',
                            'options' => [
                                ['text' => '−7', 'correct' => true],
                                ['text' => '7'],
                                ['text' => '−23'],
                                ['text' => '23'],
                            ],
                            'explanation' => '8 + (−15) = −7 karena pengurangan lebih besar.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari −2 + 3 − 5 adalah …',
                            'options' => [
                                ['text' => '−4', 'correct' => true],
                                ['text' => '4'],
                                ['text' => '−6'],
                                ['text' => '6'],
                            ],
                            'explanation' => '−2 + 3 = 1, lalu 1 − 5 = −4.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'drag_drop',
                            'question' => 'Urutkan langkah pengerjaan operasi campuran.',
                            'payload' => [
                                ['id' => 'a', 'text' => 'Kerjakan operasi dalam kurung'],
                                ['id' => 'b', 'text' => 'Kerjakan perkalian dan pembagian'],
                                ['id' => 'c', 'text' => 'Kerjakan penjumlahan dan pengurangan'],
                            ],
                            'correct' => ['order' => ['a', 'b', 'c']],
                            'explanation' => 'Kurung lebih dulu, lalu kali/bagi, terakhir tambah/kurang.',
                            'points' => 20,
                        ],
                    ],
                ],
                'hard' => [
                    'title' => 'Bilangan Bulat — Sulit',
                    'duration' => 1200,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari (−2)³ adalah …',
                            'options' => [
                                ['text' => '−8', 'correct' => true],
                                ['text' => '8'],
                                ['text' => '−6'],
                                ['text' => '6'],
                            ],
                            'explanation' => '(−2) × (−2) × (−2) = −8.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari −3 × (4 − 7) adalah …',
                            'options' => [
                                ['text' => '9', 'correct' => true],
                                ['text' => '−9'],
                                ['text' => '3'],
                                ['text' => '−3'],
                            ],
                            'explanation' => '4 − 7 = −3, lalu −3 × (−3) = 9.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Nilai x yang memenuhi x + (−8) = −3 adalah …',
                            'options' => [
                                ['text' => '5', 'correct' => true],
                                ['text' => '−5'],
                                ['text' => '11'],
                                ['text' => '−11'],
                            ],
                            'explanation' => 'x = −3 + 8 = 5.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'matching',
                            'question' => 'Jodohkan operasi dengan hasilnya.',
                            'payload' => [
                                ['id' => 'p1', 'left' => '−3 + 5', 'right' => '2'],
                                ['id' => 'p2', 'left' => '−4 × (−5)', 'right' => '20'],
                                ['id' => 'p3', 'left' => '8 ÷ (−2)', 'right' => '−4'],
                                ['id' => 'p4', 'left' => '|−9|', 'right' => '9'],
                            ],
                            'correct' => [
                                'pairs' => [
                                    'p1' => '2',
                                    'p2' => '20',
                                    'p3' => '−4',
                                    'p4' => '9',
                                ],
                            ],
                            'explanation' => 'Hitung setiap operasi dengan aturan tanda yang tepat.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'simulation',
                            'question' => 'Suhu di sebuah kota −5 °C. Setelah siang, suhu naik 8 °C. Suhu akhirnya adalah …',
                            'options' => [
                                ['text' => '3 °C', 'correct' => true],
                                ['text' => '−13 °C'],
                                ['text' => '13 °C'],
                                ['text' => '−3 °C'],
                            ],
                            'explanation' => '−5 + 8 = 3, jadi suhu akhir 3 °C.',
                            'points' => 30,
                        ],
                    ],
                ],
            ],
        ]);
    }

    private function seedSmkAlgorithms(): void
    {
        $this->seedChapter('smk', 'kelas-10', 'pemrograman-dasar', [
            'slug' => 'algoritma-logika',
            'code' => 'PEMDAS 1.1',
            'title' => 'Algoritma & Logika',
            'description' => 'Menyusun langkah algoritma, membaca flowchart, dan menggunakan logika benar/salah dalam program.',
            'learning_objectives' => [
                'Menjelaskan pengertian algoritma dan pseudocode.',
                'Membaca simbol flowchart dasar.',
                'Menerapkan logika AND, OR, dan kondisi if.',
            ],
            'estimated_minutes' => 120,
            'materials' => [
                [
                    'type' => 'text',
                    'title' => 'Langkah Menulis Algoritma',
                    'content' => <<<'MD'
## Algoritma

Algoritma adalah urutan langkah yang jelas untuk menyelesaikan masalah.

Contoh algoritma menghitung luas persegi panjang:

1. Masukkan panjang.
2. Masukkan lebar.
3. Hitung luas = panjang × lebar.
4. Tampilkan luas.

**Pseudocode** adalah penulisan algoritma dengan bahasa yang mirip kode manusia.

```
mulai
  baca panjang, lebar
  luas ← panjang × lebar
  tampilkan luas
selesai
```
MD,
                    'duration' => 300,
                    'source_reference' => 'Buku Siswa Pemrograman Dasar SMK Kelas X',
                    'blocks' => [
                        [
                            'type' => 'glossary',
                            'terms' => [
                                ['term' => 'Algoritma', 'definition' => 'Urutan langkah yang jelas untuk menyelesaikan masalah.'],
                                ['term' => 'Pseudocode', 'definition' => 'Penulisan algoritma dengan bahasa yang mirip kode manusia.'],
                                ['term' => 'Input', 'definition' => 'Data yang dimasukkan ke program, misalnya panjang dan lebar.'],
                                ['term' => 'Output', 'definition' => 'Hasil yang ditampilkan program, misalnya luas persegi panjang.'],
                            ],
                        ],
                        ['type' => 'heading', 'level' => 2, 'text' => 'Algoritma'],
                        ['type' => 'paragraph', 'text' => 'Algoritma adalah urutan langkah yang jelas untuk menyelesaikan masalah.'],
                        ['type' => 'paragraph', 'text' => 'Contoh algoritma menghitung luas persegi panjang:'],
                        ['type' => 'list', 'ordered' => true, 'items' => [
                            'Masukkan panjang.',
                            'Masukkan lebar.',
                            'Hitung luas = panjang × lebar.',
                            'Tampilkan luas.',
                        ]],
                        ['type' => 'paragraph', 'text' => '**Pseudocode** adalah penulisan algoritma dengan bahasa yang mirip kode manusia.'],
                        ['type' => 'code', 'text' => "mulai\n  baca panjang, lebar\n  luas ← panjang × lebar\n  tampilkan luas\nselesai"],
                        [
                            'type' => 'diagram',
                            'id' => 'dg-pemdas-luas',
                            'engine' => 'mermaid',
                            'title' => 'Alur algoritma menghitung luas persegi panjang',
                            'code' => "flowchart TD\n  A[Mulai] --> B[Masukkan panjang]\n  B --> C[Masukkan lebar]\n  C --> D[Hitung luas = panjang x lebar]\n  D --> E[Tampilkan luas]\n  E --> F[Selesai]",
                        ],
                        [
                            'type' => 'sort',
                            'id' => 'srt-pemdas-langkah',
                            'prompt' => 'Urutkan langkah menghitung luas persegi panjang.',
                            'items' => [
                                ['id' => 's1', 'text' => 'Masukkan panjang'],
                                ['id' => 's2', 'text' => 'Masukkan lebar'],
                                ['id' => 's3', 'text' => 'Hitung luas = panjang × lebar'],
                                ['id' => 's4', 'text' => 'Tampilkan luas'],
                            ],
                            'answer' => ['s1', 's2', 's3', 's4'],
                            'feedback' => [
                                'correct' => 'Benar — panjang dan lebar dimasukkan lebih dulu, lalu luas dihitung dan ditampilkan.',
                                'wrong' => 'Urutannya: masukkan panjang, masukkan lebar, hitung luas, lalu tampilkan luas.',
                            ],
                        ],
                        [
                            'type' => 'checkpoint',
                            'id' => 'cp-pemdas-pseudocode',
                            'question' => 'Penulisan algoritma dengan bahasa yang mirip kode manusia disebut…',
                            'choices' => [
                                ['id' => 'a', 'text' => 'Pseudocode', 'correct' => true],
                                ['id' => 'b', 'text' => 'Flowchart'],
                                ['id' => 'c', 'text' => 'Compiler'],
                            ],
                            'explanation' => 'Pseudocode menuliskan langkah algoritma dengan bahasa yang mirip kode manusia agar mudah dibaca sebelum diterjemahkan ke bahasa pemrograman.',
                        ],
                        [
                            'type' => 'checkpoint',
                            'id' => 'cp-pemdas-luas',
                            'question' => 'Jika panjang 8 dan lebar 5, luas persegi panjang adalah…',
                            'choices' => [
                                ['id' => 'a', 'text' => '40', 'correct' => true],
                                ['id' => 'b', 'text' => '13'],
                                ['id' => 'c', 'text' => '26'],
                            ],
                            'explanation' => 'Luas = panjang × lebar = 8 × 5 = 40.',
                        ],
                    ],
                ],
                [
                    'type' => 'text',
                    'title' => 'Flowchart & Logika',
                    'content' => <<<'MD'
## Simbol flowchart

| Simbol | Fungsi |
|--------|--------|
| Oval | Mulai / selesai |
| Persegi panjang | Proses |
| Belah ketupat | Keputusan |
| Jajar genjang | Input / output |

## Logika

- `true AND false = false`
- `false OR true = true`
- `if (nilai >= 70)` berarti lulus hanya jika nilai minimal 70.
MD,
                    'duration' => 300,
                    'source_reference' => 'Modul Ajar Pemrograman Dasar SMK Kelas X',
                    'blocks' => [
                        [
                            'type' => 'glossary',
                            'terms' => [
                                ['term' => 'Flowchart', 'definition' => 'Diagram alur yang menggambarkan langkah dan keputusan sebuah algoritma.'],
                                ['term' => 'Proses', 'definition' => 'Langkah kerja yang digambarkan dengan persegi panjang.'],
                                ['term' => 'Keputusan', 'definition' => 'Percabangan bersyarat yang digambarkan dengan belah ketupat.'],
                                ['term' => 'Logika boolean', 'definition' => 'Logika benar/salah yang memakai AND, OR, dan kondisi if.'],
                            ],
                        ],
                        ['type' => 'heading', 'level' => 2, 'text' => 'Simbol flowchart'],
                        ['type' => 'table', 'rows' => [
                            ['Simbol', 'Fungsi'],
                            ['Oval', 'Mulai / selesai'],
                            ['Persegi panjang', 'Proses'],
                            ['Belah ketupat', 'Keputusan'],
                            ['Jajar genjang', 'Input / output'],
                        ]],
                        ['type' => 'heading', 'level' => 2, 'text' => 'Logika'],
                        ['type' => 'list', 'ordered' => false, 'items' => [
                            '`true AND false = false`',
                            '`false OR true = true`',
                            '`if (nilai >= 70)` berarti lulus hanya jika nilai minimal 70.',
                        ]],
                        [
                            'type' => 'diagram',
                            'id' => 'dg-pemdas-kelulusan',
                            'engine' => 'mermaid',
                            'title' => 'Flowchart keputusan kelulusan',
                            'code' => "flowchart TD\n  A[Mulai] --> B[Input nilai]\n  B --> C{Nilai minimal 70?}\n  C -->|Ya| D[Lulus]\n  C -->|Tidak| E[Tidak lulus]\n  D --> F[Selesai]\n  E --> F",
                        ],
                        [
                            'type' => 'categorize',
                            'id' => 'cat-pemdas-simbol',
                            'prompt' => 'Kelompokkan fungsi berikut menurut simbol flowchart-nya.',
                            'buckets' => [
                                ['id' => 'oval', 'label' => 'Oval'],
                                ['id' => 'persegi', 'label' => 'Persegi panjang'],
                                ['id' => 'ketupat', 'label' => 'Belah ketupat'],
                                ['id' => 'jajar', 'label' => 'Jajar genjang'],
                            ],
                            'items' => [
                                ['id' => 'c1', 'text' => 'Mulai / selesai', 'bucket' => 'oval'],
                                ['id' => 'c2', 'text' => 'Proses', 'bucket' => 'persegi'],
                                ['id' => 'c3', 'text' => 'Keputusan', 'bucket' => 'ketupat'],
                                ['id' => 'c4', 'text' => 'Input / output', 'bucket' => 'jajar'],
                            ],
                            'feedback' => [
                                'correct' => 'Benar — oval untuk mulai/selesai, persegi panjang untuk proses, belah ketupat untuk keputusan, jajar genjang untuk input/output.',
                                'wrong' => 'Ingat pasangannya: oval, persegi panjang, belah ketupat, dan jajar genjang.',
                            ],
                        ],
                        [
                            'type' => 'checkpoint',
                            'id' => 'cp-pemdas-and',
                            'question' => 'Hasil dari `true AND false` adalah…',
                            'choices' => [
                                ['id' => 'a', 'text' => 'false', 'correct' => true],
                                ['id' => 'b', 'text' => 'true'],
                                ['id' => 'c', 'text' => 'tidak dapat ditentukan'],
                            ],
                            'explanation' => 'AND hanya bernilai true jika kedua pernyataan benar. Karena salah satunya false, hasilnya false.',
                        ],
                        [
                            'type' => 'checkpoint',
                            'id' => 'cp-pemdas-if',
                            'question' => '`if (nilai >= 70)` berarti siswa lulus hanya jika…',
                            'choices' => [
                                ['id' => 'a', 'text' => 'nilainya minimal 70', 'correct' => true],
                                ['id' => 'b', 'text' => 'nilainya kurang dari 70'],
                                ['id' => 'c', 'text' => 'nilainya tepat 70 saja'],
                            ],
                            'explanation' => 'Tanda >= berarti lebih dari atau sama dengan, sehingga nilai 70 pun memenuhi syarat lulus.',
                        ],
                        [
                            'type' => 'scenario',
                            'id' => 'sc-pemdas-kelulusan',
                            'title' => 'Membaca flowchart kelulusan dengan jujur',
                            'start' => 'n1',
                            'nodes' => [
                                ['id' => 'n1', 'text' => 'Nilaimu 65, sedangkan syarat lulus pada flowchart adalah nilai minimal 70. Apa yang kamu lakukan?', 'choices' => [
                                    ['text' => 'Mengikuti jalur “Tidak lulus” dan menanyakan cara memperbaiki', 'next' => 'n2', 'score' => 2, 'feedback' => 'Flowchart harus dibaca apa adanya. Nilai 65 kurang dari 70 sehingga jalurnya “Tidak lulus”.'],
                                    ['text' => 'Mengubah syarat menjadi 60 agar lulus', 'next' => 'n3', 'score' => 0, 'feedback' => 'Mengubah syarat agar hasilnya sesuai keinginan bukan membaca flowchart dengan benar.'],
                                    ['text' => 'Menganggap lulus karena 65 hampir 70', 'next' => 'n4', 'score' => 0, 'feedback' => 'Kondisi >= 70 bersifat tegas; 65 tidak memenuhi syarat.'],
                                ]],
                                ['id' => 'n2', 'text' => 'Guru menawarkan ujian perbaikan. Apa langkahmu?', 'choices' => [
                                    ['text' => 'Belajar dan mengerjakan ujian perbaikan dengan jujur', 'next' => 'n5', 'score' => 2, 'feedback' => 'Menerima hasil lalu berusaha memperbaiki adalah langkah yang benar.'],
                                    ['text' => 'Meminta nilai tambahan tanpa ujian', 'next' => 'n6', 'score' => 0, 'feedback' => 'Meminta nilai tanpa usaha tidak sesuai aturan dan tidak jujur.'],
                                ]],
                                ['id' => 'n3', 'text' => 'Temanmu menyetujui syarat diubah agar semua lulus. Apa sikapmu?', 'choices' => [
                                    ['text' => 'Menolak dan menjelaskan bahwa syarat harus dipatuhi', 'next' => 'n2', 'score' => 1, 'feedback' => 'Mengingatkan bahwa aturan tidak diubah hanya karena hasilnya tidak sesuai.'],
                                    ['text' => 'Setuju karena semua orang jadi senang', 'next' => 'n7', 'score' => 0, 'feedback' => 'Mengubah aturan demi kenyamanan merusak kejujuran penilaian.'],
                                ]],
                                ['id' => 'n4', 'text' => 'Guru menunjukkan bahwa 65 tidak memenuhi kondisi. Apa yang kamu lakukan?', 'choices' => [
                                    ['text' => 'Menerima kenyataan dan meminta bimbingan belajar', 'next' => 'n2', 'score' => 1, 'feedback' => 'Menerima hasil dan meminta bimbingan membuka jalan perbaikan.'],
                                    ['text' => 'Tetap bersikeras bahwa dirimu lulus', 'next' => 'n7', 'score' => 0, 'feedback' => 'Bersikeras melawan kondisi yang jelas tidak menyelesaikan masalah.'],
                                ]],
                                ['id' => 'n5', 'end' => true, 'outcome' => 'good', 'text' => 'Kamu membaca flowchart dengan benar, menerima hasil, dan memperbaikinya dengan usaha yang jujur.'],
                                ['id' => 'n6', 'end' => true, 'outcome' => 'bad', 'text' => 'Nilai diminta tanpa usaha. Keputusan tidak sesuai aturan dan kepercayaan guru berkurang.'],
                                ['id' => 'n7', 'end' => true, 'outcome' => 'bad', 'text' => 'Aturan diabaikan dan masalah tidak selesai. Flowchart yang benar tetap menunjukkan hasil yang sebenarnya.'],
                            ],
                        ],
                        [
                            'type' => 'challenge',
                            'id' => 'ch-pemdas-flowchart',
                            'title' => 'Tantangan Kilat: Flowchart dan Logika',
                            'time_limit' => 70,
                            'items' => [
                                ['question' => 'Simbol keputusan adalah…', 'answer' => 'belah ketupat'],
                                ['question' => 'Simbol input/output adalah…', 'answer' => 'jajar genjang'],
                                ['question' => 'Simbol mulai/selesai adalah…', 'answer' => 'oval'],
                                ['question' => 'true AND false = …', 'answer' => 'false'],
                                ['question' => 'false OR true = …', 'answer' => 'true'],
                            ],
                            'feedback' => [
                                'correct' => 'Tepat — simbol flowchart dan logika boolean bekerja bersama dalam satu alur.',
                                'wrong' => 'Ingat simbol flowchart dan aturan AND/OR: AND butuh keduanya benar, OR cukup salah satu benar.',
                            ],
                        ],
                    ],
                ],
            ],
            'assessments' => [
                'easy' => [
                    'title' => 'Algoritma & Logika — Mudah',
                    'duration' => 600,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Algoritma adalah …',
                            'options' => [
                                ['text' => 'Urutan langkah untuk menyelesaikan masalah', 'correct' => true],
                                ['text' => 'Bahasa pemrograman tertentu'],
                                ['text' => 'Perangkat keras komputer'],
                                ['text' => 'Nama variabel dalam program'],
                            ],
                            'explanation' => 'Algoritma adalah urutan langkah logis penyelesaian masalah.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Simbol flowchart untuk keputusan adalah …',
                            'options' => [
                                ['text' => 'Belah ketupat', 'correct' => true],
                                ['text' => 'Oval'],
                                ['text' => 'Persegi panjang'],
                                ['text' => 'Jajar genjang'],
                            ],
                            'explanation' => 'Keputusan (if) digambarkan dengan belah ketupat.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Proses input berarti …',
                            'options' => [
                                ['text' => 'Memasukkan data ke program', 'correct' => true],
                                ['text' => 'Menampilkan hasil program'],
                                ['text' => 'Menghapus program'],
                                ['text' => 'Mematikan komputer'],
                            ],
                            'explanation' => 'Input adalah data yang dimasukkan ke program.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Program biasanya dieksekusi …',
                            'options' => [
                                ['text' => 'Dari atas ke bawah', 'correct' => true],
                                ['text' => 'Dari bawah ke atas'],
                                ['text' => 'Secara acak'],
                                ['text' => 'Hanya baris terakhir'],
                            ],
                            'explanation' => 'Eksekusi berurutan dari atas ke bawah kecuali ada percabangan/perulangan.',
                            'points' => 10,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Pseudocode adalah …',
                            'options' => [
                                ['text' => 'Kode mirip bahasa manusia untuk menulis algoritma', 'correct' => true],
                                ['text' => 'Aplikasi pengolah gambar'],
                                ['text' => 'Jenis kabel jaringan'],
                                ['text' => 'Nama mesin pencari'],
                            ],
                            'explanation' => 'Pseudocode menuliskan algoritma dengan bahasa yang mudah dibaca.',
                            'points' => 10,
                        ],
                    ],
                ],
                'medium' => [
                    'title' => 'Algoritma & Logika — Sedang',
                    'duration' => 900,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Jika x = 5, apakah hasil dari x > 3?',
                            'options' => [
                                ['text' => 'Benar', 'correct' => true],
                                ['text' => 'Salah'],
                                ['text' => 'Tidak dapat ditentukan'],
                                ['text' => 'Error'],
                            ],
                            'explanation' => '5 lebih besar dari 3, jadi kondisi bernilai benar.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Perulangan for i = 1 to 3 akan mencetak …',
                            'options' => [
                                ['text' => '1, 2, 3', 'correct' => true],
                                ['text' => '3, 2, 1'],
                                ['text' => '1, 1, 1'],
                                ['text' => '0, 1, 2'],
                            ],
                            'explanation' => 'Perulangan dari 1 sampai 3 mencetak 1, 2, lalu 3.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Variabel dalam program digunakan untuk …',
                            'options' => [
                                ['text' => 'Menyimpan nilai', 'correct' => true],
                                ['text' => 'Mencetak kertas'],
                                ['text' => 'Menghapus file'],
                                ['text' => 'Mengganti monitor'],
                            ],
                            'explanation' => 'Variabel menyimpan nilai yang bisa dipakai dan diubah.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari true AND false adalah …',
                            'options' => [
                                ['text' => 'false', 'correct' => true],
                                ['text' => 'true'],
                                ['text' => '0'],
                                ['text' => 'tidak terdefinisi'],
                            ],
                            'explanation' => 'AND hanya benar jika kedua kondisi benar.',
                            'points' => 20,
                        ],
                        [
                            'type' => 'drag_drop',
                            'question' => 'Urutkan langkah membuat program dari awal hingga akhir.',
                            'payload' => [
                                ['id' => 'a', 'text' => 'Pahami masalah'],
                                ['id' => 'b', 'text' => 'Rancang algoritma'],
                                ['id' => 'c', 'text' => 'Tulis kode program'],
                                ['id' => 'd', 'text' => 'Uji dan perbaiki program'],
                            ],
                            'correct' => ['order' => ['a', 'b', 'c', 'd']],
                            'explanation' => 'Pahami masalah, rancang algoritma, tulis kode, lalu uji.',
                            'points' => 20,
                        ],
                    ],
                ],
                'hard' => [
                    'title' => 'Algoritma & Logika — Sulit',
                    'duration' => 1200,
                    'questions' => [
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Setelah x = 2; x = x × 3; x = x + 4, nilai x adalah …',
                            'options' => [
                                ['text' => '10', 'correct' => true],
                                ['text' => '9'],
                                ['text' => '12'],
                                ['text' => '6'],
                            ],
                            'explanation' => 'x = 2 × 3 = 6, lalu x = 6 + 4 = 10.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Jika nilai = 65 dan kondisi if (nilai >= 70), maka hasilnya …',
                            'options' => [
                                ['text' => 'Tidak lulus', 'correct' => true],
                                ['text' => 'Lulus'],
                                ['text' => 'Error'],
                                ['text' => 'Nilai berubah menjadi 70'],
                            ],
                            'explanation' => '65 tidak memenuhi syarat minimal 70.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'multiple_choice',
                            'question' => 'Hasil dari false OR true adalah …',
                            'options' => [
                                ['text' => 'true', 'correct' => true],
                                ['text' => 'false'],
                                ['text' => '0'],
                                ['text' => 'tidak terdefinisi'],
                            ],
                            'explanation' => 'OR bernilai benar jika salah satu kondisi benar.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'matching',
                            'question' => 'Jodohkan simbol flowchart dengan fungsinya.',
                            'payload' => [
                                ['id' => 'p1', 'left' => 'Oval', 'right' => 'Mulai / selesai'],
                                ['id' => 'p2', 'left' => 'Persegi panjang', 'right' => 'Proses'],
                                ['id' => 'p3', 'left' => 'Belah ketupat', 'right' => 'Keputusan'],
                                ['id' => 'p4', 'left' => 'Jajar genjang', 'right' => 'Input / output'],
                            ],
                            'correct' => [
                                'pairs' => [
                                    'p1' => 'Mulai / selesai',
                                    'p2' => 'Proses',
                                    'p3' => 'Keputusan',
                                    'p4' => 'Input / output',
                                ],
                            ],
                            'explanation' => 'Setiap simbol flowchart memiliki fungsi khusus.',
                            'points' => 30,
                        ],
                        [
                            'type' => 'simulation',
                            'question' => 'Program harus menampilkan angka terbesar dari tiga angka. Pendekatan mana yang paling tepat?',
                            'options' => [
                                ['text' => 'Bandingkan berpasangan dan simpan nilai terbesar', 'correct' => true],
                                ['text' => 'Jumlahkan ketiga angka'],
                                ['text' => 'Kalikan ketiga angka'],
                                ['text' => 'Urutkan menaik lalu ambil angka tengah'],
                            ],
                            'explanation' => 'Membandingkan berpasangan memungkinkan penyimpanan nilai maksimum.',
                            'points' => 30,
                        ],
                    ],
                ],
            ],
        ]);
    }

    /**
     * @param  array<string, mixed>  $config
     */
    private function seedChapter(
        string $levelSlug,
        string $classSlug,
        string $subjectSlug,
        array $config,
    ): void {
        $subject = Subject::query()
            ->where('slug', $subjectSlug)
            ->whereHas('classRoom', fn ($query) => $query
                ->where('slug', $classSlug)
                ->whereHas('educationLevel', fn ($level) => $level->where('slug', $levelSlug)))
            ->first();

        if ($subject === null) {
            $this->command?->warn(
                "Mapel {$subjectSlug} {$classSlug} {$levelSlug} tidak ditemukan; konten dilewati.",
            );

            return;
        }

        $chapter = Chapter::updateOrCreate(
            ['subject_id' => $subject->id, 'slug' => $config['slug']],
            [
                'code' => $config['code'],
                'title' => $config['title'],
                'description' => $config['description'],
                'learning_objectives' => $config['learning_objectives'],
                'estimated_minutes' => $config['estimated_minutes'],
                'order' => 1,
                'is_active' => true,
            ],
        );

        foreach ($config['materials'] as $index => $material) {
            $chapter->materials()->updateOrCreate(
                ['title' => $material['title']],
                [
                    ...$material,
                    'order' => $index + 1,
                    'is_active' => true,
                ],
            );
        }

        $order = 1;

        foreach (['easy', 'medium', 'hard'] as $difficulty) {
            if (! isset($config['assessments'][$difficulty])) {
                continue;
            }

            $definition = $config['assessments'][$difficulty];
            $assessment = $chapter->assessments()->updateOrCreate(
                ['difficulty' => $difficulty],
                [
                    'title' => $definition['title'],
                    'duration' => $definition['duration'],
                    'passing_score' => 70,
                    'order' => $order++,
                    'is_active' => true,
                ],
            );

            foreach ($definition['questions'] as $questionOrder => $question) {
                $this->seedQuestion($assessment, $questionOrder + 1, $question);
            }
        }
    }

    /**
     * @param  array<string, mixed>  $question
     */
    private function seedQuestion(Assessment $assessment, int $order, array $question): void
    {
        $type = QuestionType::from($question['type']);
        $options = $question['options'] ?? [];

        $model = $assessment->questions()->updateOrCreate(
            ['order' => $order],
            [
                'type' => $type->value,
                'question' => $question['question'],
                'options' => $question['payload'] ?? null,
                'correct_answer' => $question['correct'] ?? $this->defaultCorrectAnswer($type, $options),
                'rubric' => null,
                'explanation' => $question['explanation'] ?? null,
                'hint' => $question['hint'] ?? null,
                'points' => $question['points'] ?? 10,
                'time_limit' => $question['time_limit'] ?? null,
                'ai_assisted' => false,
                'order' => $order,
            ],
        );

        $model->questionOptions()->delete();

        if (! in_array($type, [QuestionType::MultipleChoice, QuestionType::MultipleAnswer, QuestionType::Simulation], true)) {
            return;
        }

        foreach ($options as $index => $option) {
            QuestionOption::create([
                'question_id' => $model->id,
                'label' => chr(65 + $index),
                'text' => $option['text'],
                'is_correct' => (bool) ($option['correct'] ?? false),
                'order' => $index + 1,
            ]);
        }
    }

    /**
     * @param  array<int, array{text: string, correct?: bool}>  $options
     * @return array<string, mixed>
     */
    private function defaultCorrectAnswer(QuestionType $type, array $options): array
    {
        $correct = collect($options)
            ->where('correct', true)
            ->pluck('text')
            ->all();

        return match ($type) {
            QuestionType::MultipleChoice, QuestionType::Simulation => ['text' => $correct[0] ?? null],
            QuestionType::MultipleAnswer => ['texts' => $correct],
            default => [],
        };
    }
}
