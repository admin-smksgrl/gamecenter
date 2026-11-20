"""PJOK 3 — Permainan Bola Tangan (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 3',
    'slug': 'pjok-3-bola-tangan',
    'title': 'Permainan Bola Tangan',
    'description': (
        'Mengenal permainan bola tangan, peraturan dasarnya, teknik passing, '
        'dribbling, shooting, dan kerja sama tim dalam menyerang serta bertahan.'
    ),
    'objectives': [
        'Menjelaskan sejarah dan peraturan dasar permainan bola tangan.',
        'Mempraktikkan teknik passing, catching, dribbling, dan shooting bola tangan.',
        'Menerapkan pola serangan dan pertahanan sederhana dalam bola tangan.',
        'Menunjukkan sportivitas, disiplin, dan kerja sama selama bermain.',
        'Menjaga keselamatan diri dan teman melalui pemanasan serta pendinginan.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 3 Permainan Bola Tangan; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Bola tangan', 'definition': 'Olahraga dua tim berisi tujuh pemain yang berusaha melempar bola ke gawang lawan.'},
        {'term': 'Catching', 'definition': 'Menangkap bola dengan dua tangan saat menerima operan.'},
        {'term': 'Dribbling', 'definition': 'Memantulkan bola ke lantai sambil bergerak.'},
        {'term': 'Shooting', 'definition': 'Melempar bola ke gawang untuk mencetak gol.'},
        {'term': 'Area gawang', 'definition': 'Daerah selebar enam meter di depan gawang yang hanya boleh dimasuki penjaga gawang.'},
        {'term': 'Penalti', 'definition': 'Lemparan dari garis tujuh meter akibat pelanggaran di area gawang.'},
        {'term': 'Pivot', 'definition': 'Gerakan memutar badan untuk melepaskan diri dari penjagaan.'},
        {'term': 'Throw-in', 'definition': 'Lemparan ke dalam untuk memulai kembali permainan setelah bola keluar lapangan.'},
    ],
    'intro': {
        'material_title': 'Mengapa bola tangan menantang?',
        'title': 'Permainan cepat dengan tangan',
        'paragraphs': [
            'Bola tangan adalah permainan bola besar yang dimainkan dua tim. Setiap tim berusaha melempar bola ke gawang lawan. Berbeda dari sepak bola, pemain memakai tangan untuk mengoper, menggiring, dan menembak.',
            'Bola tangan modern berkembang di Eropa pada akhir abad ke-19. Permainan ini kemudian dipertandingkan pada Olimpiade dan kejuaraan dunia. Di Indonesia, Asosiasi Bola Tangan Indonesia (ABTI) menjadi induk organisasinya.',
            'Permainan ini menuntut kecepatan, kekuatan lengan, dan koordinasi. Pemain juga harus cepat berpindah dari menyerang ke bertahan karena permainan berlangsung bolak-balik.',
        ],
        'diagram': (
            'Alur dasar permainan bola tangan',
            'flowchart LR\n'
            '  A[Menerima bola] --> B[Passing atau dribbling]\n'
            '  B --> C[Membuka ruang]\n'
            '  C --> D[Shooting ke gawang]\n'
            '  D --> E[Gol atau rebound]\n'
            '  E --> F[Bertahan dan serang lagi]',
        ),
        'callout': 'Potong kuku, lepas aksesori, dan gunakan sepatu yang tidak licin agar bola dan lantai tetap aman digunakan.',
        'checkpoint': (
            'Berapa jumlah pemain inti setiap tim bola tangan?',
            [
                ('7 pemain', True),
                ('5 pemain', False),
                ('6 pemain', False),
                ('11 pemain', False),
            ],
            'Setiap tim menurunkan tujuh pemain inti, termasuk penjaga gawang.',
        ),
    },
    'concept': {
        'material_title': 'Peraturan dan teknik dasar',
        'title': 'Peraturan, teknik, dan taktik',
        'paragraphs': [
            'Lapangan bola tangan berukuran panjang 40 meter dan lebar 20 meter. Gawang berukuran lebar 3 meter dan tinggi 2 meter. Area gawang berbentuk setengah lingkaran dengan radius 6 meter.',
            'Pertandingan terdiri atas dua babak, masing-masing 30 menit. Pemain boleh memegang bola paling lama tiga detik dan melangkah paling banyak tiga langkah sebelum menggiring atau mengoper.',
            'Pelanggaran umum meliputi melangkah lebih dari tiga langkah, menahan bola lebih dari tiga detik, dan memasuki area gawang. Pelanggaran di area gawang dapat menghasilkan lemparan penalti dari garis tujuh meter.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Catching', 'Menerima bola dengan aman', 'Kedua tangan terbuka, mata ke bola, jemput bola'],
            ['Passing', 'Memindahkan bola cepat', 'Siku dekat badan, dorong bola ke depan'],
            ['Dribbling', 'Bergerak sambil menguasai bola', 'Pantulkan bola, jaga badan di antara bola dan lawan'],
            ['Shooting', 'Mencetak gol', 'Awalan langkah, lompat, lepaskan bola ke gawang'],
            ['Pivot', 'Melepaskan diri dari penjagaan', 'Putar badan dengan kaki poros'],
        ],
        'visual': chart_block(
            'pjok-3-ukuran-lapangan',
            'Ukuran penting lapangan bola tangan (meter)',
            'bar',
            [('Panjang', 40), ('Lebar', 20), ('Lebar gawang', 3), ('Tinggi gawang', 2)],
        ),
        'activity': categorize_block(
            'pjok-3-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pelanggaran atau gerak sah.',
            [('b1', 'Pelanggaran'), ('b2', 'Gerak sah')],
            [
                ('i1', 'Melangkah empat kali tanpa menggiring bola', 'b1'),
                ('i2', 'Menahan bola lebih dari tiga detik', 'b1'),
                ('i3', 'Mengoper bola dengan dua tangan', 'b2'),
                ('i4', 'Memantulkan bola ke lantai', 'b2'),
                ('i5', 'Memasuki area gawang saat menyerang', 'b1'),
                ('i6', 'Melakukan pivot dengan kaki poros', 'b2'),
            ],
            'Tepat. Langkah berlebih, menahan bola terlalu lama, dan masuk area gawang adalah pelanggaran.',
            'Periksa lagi: passing, dribbling, dan pivot adalah gerakan sah.',
        ),
        'subtitle': 'Taktik sederhana',
        'list': [
            'Serangan cepat dimulai dari penjaga gawang yang melempar bola ke sayap.',
            'Serangan balik efektif ketika lawan belum kembali ke posisi bertahan.',
            'Pertahanan 6-0 menjaga area dekat gawang, sedangkan 5-1 menekan pemain lawan di depan.',
            'Komunikasi singkat seperti “saya”, “kiri”, atau “ganti” mencegah tabrakan dan salah jaga.',
        ],
        'checkpoint': (
            'Berapa lama pemain boleh menahan bola sebelum mengoper atau menembak?',
            [
                ('3 detik', True),
                ('5 detik', False),
                ('2 detik', False),
                ('10 detik', False),
            ],
            'Pemain boleh menahan bola paling lama tiga detik.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bermain dengan sportif',
        'paragraphs': [
            'Permainan sesungguhnya menguji keputusan, bukan hanya teknik. Pemain harus membaca posisi rekan dan lawan, lalu memilih antara mengoper, menggiring, atau menembak. Keputusan yang tergesa-gesa sering menghasilkan kehilangan bola.',
            'Sportivitas tampak ketika pemain mengakui pelanggaran, membantu lawan yang jatuh, dan menghormati keputusan wasit. Kerja sama dibangun melalui komunikasi dan pembagian peran yang jelas.',
            'Gunakan permainan kecil empat lawan empat untuk melatih passing cepat, pergerakan tanpa bola, dan pertahanan. Hentikan permainan sesaat untuk membahas keputusan yang tepat.',
        ],
        'scenario': scenario(
            'pjok-3-skenario',
            'Keputusan di menit terakhir',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Timmu tertinggal satu gol dan waktu tersisa satu menit. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menyusun serangan cepat dan mencari ruang lempar', 'next': 'n2', 'score': 2, 'feedback': 'Keputusan ini memberi tim peluang terbaik.'},
                        {'text': 'Melempar bola dari jauh setiap kali mendapat bola', 'next': 'n3', 'score': 0, 'feedback': 'Lemparan terburu-buru mudah dihalangi.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Rekanmu kosong di depan gawang, tetapi kamu juga punya ruang menembak. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Mengoper ke rekan yang lebih kosong', 'next': 'n4', 'score': 2, 'feedback': 'Operan ke posisi terbaik adalah inti kerja sama.'},
                        {'text': 'Tetap menembak meski dijaga', 'next': 'n3', 'score': 0, 'feedback': 'Peluang rekan yang lebih baik terbuang.'},
                    ],
                },
                {'id': 'n3', 'text': 'Peluang habis karena keputusan diambil tergesa-gesa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tim mencetak gol dan bermain sebagai satu kesatuan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu catching?', 'back': 'Menangkap bola dengan dua tangan saat menerima operan.'},
            {'front': 'Berapa ukuran lapangan bola tangan?', 'back': '40 meter × 20 meter.'},
            {'front': 'Berapa lama satu babak?', 'back': '30 menit.'},
            {'front': 'Apa itu pivot?', 'back': 'Memutar badan dengan kaki poros untuk melepaskan diri dari penjagaan.'},
        ],
        'checkpoint': (
            'Saat menerima bola dengan lawan sangat dekat, tindakan paling aman adalah…',
            [
                ('Melakukan pivot untuk melindungi bola', True),
                ('Langsung menembak tanpa melihat gawang', False),
                ('Melempar bola ke sembarang arah', False),
                ('Berhenti dan menahan bola lebih dari tiga detik', False),
            ],
            'Pivot melindungi bola sambil membuka pandangan untuk mencari rekan.',
        ),
        'challenge': challenge_block(
            'pjok-3-tantangan',
            'Tantangan istilah bola tangan',
            90,
            [
                ('Jumlah pemain inti', '7'),
                ('Lama satu babak', '30 menit'),
                ('Batas menahan bola', '3 detik'),
                ('Jarak garis penalti', '7 meter'),
                ('Induk organisasi bola tangan Indonesia', 'ABTI'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Berapa jumlah pemain inti setiap tim bola tangan?', '7 pemain', ['5 pemain', '6 pemain', '11 pemain'], 'Setiap tim menurunkan tujuh pemain inti.', 'Bandingkan dengan bola voli yang enam pemain.'),
        ('Berapa ukuran lapangan bola tangan?', '40 m × 20 m', ['28 m × 15 m', '18 m × 9 m', '105 m × 68 m'], 'Lapangan bola tangan berukuran 40 meter × 20 meter.', 'Lapangan ini lebih panjang daripada lapangan bola basket.'),
        ('Berapa ukuran gawang bola tangan?', '3 m × 2 m', ['7,32 m × 2,44 m', '2 m × 1 m', '4 m × 3 m'], 'Gawang bola tangan berukuran lebar 3 meter dan tinggi 2 meter.', 'Gawang sepak bola jauh lebih lebar.'),
        ('Apa induk organisasi bola tangan Indonesia?', 'ABTI', ['PSSI', 'PERBASI', 'PBVSI'], 'ABTI adalah Asosiasi Bola Tangan Indonesia.', 'Bandingkan dengan PSSI untuk sepak bola.'),
        ('Berapa lama satu babak pertandingan bola tangan?', '30 menit', ['45 menit', '20 menit', '40 menit'], 'Satu babak berlangsung 30 menit.', 'Ada dua babak dalam satu pertandingan.'),
        ('Berapa langkah maksimal sebelum pemain harus menggiring atau mengoper?', '3 langkah', ['2 langkah', '4 langkah', '5 langkah'], 'Pemain boleh melangkah paling banyak tiga langkah.', 'Aturan ini mirip batas menahan bola tiga detik.'),
        ('Berapa radius area gawang bola tangan?', '6 meter', ['5 meter', '7 meter', '9 meter'], 'Area gawang berbentuk setengah lingkaran dengan radius 6 meter.', 'Garis penalti berada di belakang area ini.'),
        ('Berapa jarak garis penalti bola tangan?', '7 meter', ['9 meter', '11 meter', '6 meter'], 'Lemparan penalti dilakukan dari garis tujuh meter.', 'Angka ini juga menjadi nama lemparan penalti.'),
        ('Apa nama lemparan untuk memulai kembali permainan setelah bola keluar?', 'Throw-in', ['Corner', 'Goal kick', 'Free kick'], 'Throw-in dilakukan dari garis samping tempat bola keluar.', 'Lawan tidak boleh menghalangi jarak pelempar.'),
        ('Apa yang terjadi bila pemain memasuki area gawang saat menyerang?', 'Pelanggaran dan bola diserahkan ke lawan', ['Gol dianggap sah', 'Pemain mendapat poin tambahan', 'Permainan diulang dari tengah'], 'Area gawang hanya boleh dimasuki penjaga gawang.', 'Pelanggaran di area gawang dapat berujung penalti.'),
        ('Berapa jumlah pemain cadangan yang boleh didaftarkan dalam pertandingan resmi?', 'Sesuai regulasi, umumnya hingga 7 pemain', ['Tidak ada cadangan', 'Hanya 1 pemain', 'Hanya 3 pemain'], 'Regulasi umumnya mengizinkan beberapa pemain cadangan untuk rotasi.', 'Jumlah pastinya bergantung pada regulasi turnamen.'),
        ('Apa istilah gerakan memutar badan untuk melepaskan diri dari penjagaan?', 'Pivot', ['Dribbling', 'Catching', 'Throw-in'], 'Pivot memakai satu kaki sebagai poros untuk memutar badan.', 'Kaki poros tidak boleh diangkat.'),
        ('Apa tujuan utama shooting dalam bola tangan?', 'Mencetak gol ke gawang lawan', ['Menghentikan waktu', 'Mengoper ke rekan', 'Menjaga bola dari lawan'], 'Shooting diarahkan ke gawang untuk mencetak gol.', 'Operan adalah tugas passing.'),
        ('Berapa ukuran bola tangan untuk pemain putra?', '58–60 cm', ['54–56 cm', '62–64 cm', '50–52 cm'], 'Bola putra berdiameter 58–60 cm, bola putri 54–56 cm.', 'Ukuran bola putri lebih kecil.'),
    ],
    'multi': [
        ('Manakah yang termasuk teknik dasar bola tangan?', ['Passing', 'Catching', 'Shooting'], ['Smash', 'Servis'], 'Passing, catching, dan shooting adalah teknik dasar bola tangan.', 'Smash dan servis berasal dari bola voli.'),
        ('Manakah yang termasuk pelanggaran dalam bola tangan?', ['Melangkah lebih dari tiga langkah', 'Menahan bola lebih dari tiga detik'], ['Melakukan pivot', 'Mengoper dengan dua tangan'], 'Langkah berlebih dan menahan bola terlalu lama adalah pelanggaran.', 'Pivot dan operan dua tangan adalah gerakan sah.'),
        ('Apa tujuan melakukan passing?', ['Memindahkan bola ke rekan', 'Membuka ruang serangan'], ['Mencetak gol langsung', 'Menghentikan waktu'], 'Passing memindahkan bola dan membuka ruang, bukan mencetak gol langsung.', 'Gol dicetak melalui shooting.'),
        ('Manakah ciri dribbling yang benar?', ['Bola dipantulkan ke lantai', 'Badan menjaga bola dari lawan'], ['Bola ditahan dengan dua tangan', 'Bola dilempar ke udara terus-menerus'], 'Dribbling memantulkan bola sambil melindunginya dengan badan.', 'Sentuhan bola tetap terkendali.'),
        ('Manakah yang termasuk jenis lemparan dalam bola tangan?', ['Lemparan penalti', 'Throw-in', 'Lemparan gawang'], ['Smash', 'Jump shot'], 'Lemparan penalti, throw-in, dan lemparan gawang adalah bagian permainan.', 'Smash dan jump shot bukan istilah bola tangan.'),
        ('Manakah tugas penjaga gawang?', ['Menghalangi bola masuk gawang', 'Memulai serangan dengan lemparan'], ['Mencetak gol dari area lawan', 'Mengatur kartu pemain'], 'Penjaga gawang menghalangi bola dan dapat memulai serangan.', 'Penjaga gawang boleh berada di area gawang.'),
        ('Manakah pola pertahanan yang umum?', ['6-0', '5-1'], ['4-4-2', '2-2-6'], '6-0 dan 5-1 adalah pola pertahanan bola tangan.', '4-4-2 adalah formasi sepak bola.'),
        ('Manakah pernyataan yang benar tentang area gawang?', ['Hanya penjaga gawang yang boleh berada di dalamnya', 'Pemain lapangan tidak boleh memasukinya saat menyerang'], ['Semua pemain boleh berdiri di dalamnya', 'Area gawang tidak memiliki batas'], 'Area gawang khusus penjaga gawang; pemain lapangan tidak boleh memasukinya.', 'Garis area gawang berbentuk setengah lingkaran.'),
    ],
    'pairs': [
        ('Passing', 'mengoper bola kepada rekan'),
        ('Catching', 'menangkap bola dengan dua tangan'),
        ('Dribbling', 'memantulkan bola ke lantai'),
        ('Shooting', 'melempar bola ke gawang'),
        ('Pivot', 'memutar badan dengan kaki poros'),
        ('Throw-in', 'lemparan ke dalam setelah bola keluar'),
        ('Penalti', 'lemparan dari garis tujuh meter'),
        ('Area gawang', 'daerah radius enam meter di depan gawang'),
    ],
    'steps': [
        ('Urutkan langkah melakukan passing dada dalam bola tangan.', ['Pegang bola dengan dua tangan di depan dada', 'Tarik bola sedikit ke belakang', 'Dorong bola ke depan', 'Lepaskan bola ke arah rekan'], 'Passing dada dimulai dari pegangan di dada lalu didorong lurus.', 'Arahkan bola ke dada rekan.'),
        ('Urutkan langkah melakukan shooting dengan awalan langkah.', ['Ambil awalan satu hingga tiga langkah', 'Tolak dengan kaki tumpu', 'Angkat bola ke atas bahu', 'Lepaskan bola ke gawang'], 'Shooting berawalan memakai tolakan untuk menambah kekuatan.', 'Jaga keseimbangan saat melepaskan bola.'),
        ('Urutkan fase menggiring bola.', ['Pantulkan bola ke lantai', 'Jaga bola dekat tangan', 'Arahkan pandangan ke depan', 'Percepat langkah saat melewati lawan'], 'Dribbling menjaga bola dekat sambil membaca situasi.', 'Pantulan terlalu tinggi memudahkan lawan merebut.'),
        ('Urutkan langkah melakukan pivot.', ['Terima bola', 'Tetapkan satu kaki sebagai poros', 'Putar badan menjauhi lawan', 'Cari rekan atau tembakan'], 'Pivot dimulai dari menerima bola lalu memutar badan dengan kaki poros.', 'Kaki poros tidak boleh diangkat.'),
        ('Urutkan alur serangan cepat dalam bola tangan.', ['Penjaga gawang menangkap bola', 'Lempar ke sayap', 'Buka jalur ke gawang', 'Selesaikan dengan shooting'], 'Serangan cepat bergerak dari penjaga gawang menuju penyelesaian.', 'Semakin cepat bola berpindah, semakin sulit lawan bertahan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
