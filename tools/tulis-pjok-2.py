"""PJOK 2 — Permainan Sepak Bola (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 2',
    'slug': 'pjok-2-sepak-bola',
    'title': 'Permainan Sepak Bola',
    'description': (
        'Mempelajari sejarah dan peraturan sepak bola, teknik dasar mengoper, '
        'menggiring, menembak, dan menyundul bola, serta taktik dan '
        'sportivitas dalam pertandingan.'
    ),
    'objectives': [
        'Menjelaskan sejarah dan peraturan dasar permainan sepak bola.',
        'Mempraktikkan teknik passing, dribbling, shooting, dan heading.',
        'Menerapkan taktik menyerang dan bertahan dalam permainan sepak bola.',
        'Menunjukkan sportivitas, disiplin, dan kerja sama selama bertanding.',
        'Menjaga keselamatan diri dan teman melalui pemanasan serta pendinginan.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 2 Permainan Sepak Bola; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Sepak bola', 'definition': 'Olahraga dua tim berisi sebelas pemain yang berusaha memasukkan bola ke gawang lawan.'},
        {'term': 'Passing', 'definition': 'Mengoper bola kepada rekan satu tim.'},
        {'term': 'Dribbling', 'definition': 'Menggiring bola dengan kaki secara terkendali.'},
        {'term': 'Shooting', 'definition': 'Menembak bola ke arah gawang untuk mencetak gol.'},
        {'term': 'Heading', 'definition': 'Menyundul bola memakai dahi saat bola berada di udara.'},
        {'term': 'Offside', 'definition': 'Posisi pemain penyerang yang lebih dekat ke garis gawang lawan daripada bola dan pemain lawan kedua.'},
        {'term': 'Handball', 'definition': 'Pelanggaran karena pemain lapangan menyentuh bola dengan tangan atau lengan.'},
        {'term': 'Penalti', 'definition': 'Tendangan dari titik 11 meter akibat pelanggaran di area penalti.'},
    ],
    'intro': {
        'material_title': 'Mengapa sepak bola digemari?',
        'title': 'Permainan sederhana dengan aturan yang jelas',
        'paragraphs': [
            'Sepak bola adalah permainan bola besar yang dimainkan dua tim. Setiap tim berusaha memasukkan bola ke gawang lawan dan mencegah lawan mencetak gol. Permainan ini hanya membutuhkan bola, lapangan, dan gawang, sehingga mudah dimainkan di banyak tempat.',
            'Asosiasi sepak bola modern lahir di Inggris pada 1863 melalui Football Association. Di Indonesia, Persatuan Sepak Bola Seluruh Indonesia (PSSI) berdiri pada 19 April 1930. Sepak bola menjadi olahraga yang menyatukan banyak kalangan.',
            'Selain kebugaran, sepak bola melatih kerja sama, pengambilan keputusan, dan pengendalian emosi. Pemain harus membaca posisi rekan dan lawan sebelum memilih operan atau tembakan.',
        ],
        'diagram': (
            'Alur dasar permainan sepak bola',
            'flowchart LR\n'
            '  A[Menguasai bola] --> B[Passing atau dribbling]\n'
            '  B --> C[Membuka ruang]\n'
            '  C --> D[Shooting ke gawang]\n'
            '  D --> E[Gol atau rebound]\n'
            '  E --> F[Bertahan dan serang lagi]',
        ),
        'callout': 'Gunakan sepatu yang sesuai, periksa permukaan lapangan, dan lakukan pemanasan sebelum bermain untuk mencegah cedera kaki.',
        'checkpoint': (
            'Kapan PSSI didirikan?',
            [
                ('19 April 1930', True),
                ('23 Oktober 1951', False),
                ('28 Oktober 1928', False),
                ('17 Agustus 1945', False),
            ],
            'PSSI berdiri pada 19 April 1930; PERBASI berdiri pada 23 Oktober 1951.',
        ),
    },
    'concept': {
        'material_title': 'Peraturan dan teknik dasar',
        'title': 'Peraturan, teknik, dan taktik',
        'paragraphs': [
            'Pertandingan sepak bola terdiri atas dua babak, masing-masing 45 menit, dengan jeda 15 menit. Setiap tim menurunkan sebelas pemain inti, termasuk satu penjaga gawang. Bola yang keluar melewati garis samping dimainkan kembali dengan lemparan ke dalam.',
            'Lapangan standar FIFA berukuran panjang 105 meter dan lebar 68 meter. Gawang memiliki lebar 7,32 meter dan tinggi 2,44 meter. Titik penalti berjarak 11 meter dari garis gawang.',
            'Pelanggaran umum meliputi handball, tackling berbahaya, menarik baju lawan, dan menghalangi lawan tanpa bola. Wasit dapat memberi kartu kuning sebagai peringatan atau kartu merah sebagai pengusiran.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Passing', 'Memindahkan bola ke rekan', 'Kaki tumpu di samping bola, perkenaan kaki bagian dalam'],
            ['Dribbling', 'Melewati lawan atau membuka ruang', 'Sentuhan kecil, bola dekat kaki, pandangan ke depan'],
            ['Shooting', 'Mencetak gol', 'Kaki tumpu di samping bola, perkenaan punggung kaki'],
            ['Heading', 'Menyundul bola di udara', 'Mata ke bola, sundul dengan dahi, leher kaku'],
            ['Tackling', 'Merebut bola dari lawan', 'Sasaran bola, bukan kaki lawan'],
        ],
        'visual': chart_block(
            'pjok-2-ukuran-lapangan',
            'Ukuran penting lapangan sepak bola (meter)',
            'bar',
            [('Panjang', 105), ('Lebar', 68), ('Lebar gawang', 7), ('Tinggi gawang', 2)],
        ),
        'activity': categorize_block(
            'pjok-2-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pelanggaran atau gerak sah.',
            [('b1', 'Pelanggaran'), ('b2', 'Gerak sah')],
            [
                ('i1', 'Menyentuh bola dengan tangan di luar area penalti', 'b1'),
                ('i2', 'Menarik baju lawan', 'b1'),
                ('i3', 'Mengoper bola dengan kaki bagian dalam', 'b2'),
                ('i4', 'Menyundul bola dengan dahi', 'b2'),
                ('i5', 'Menjegal lawan dari belakang tanpa menyentuh bola', 'b1'),
                ('i6', 'Merebut bola dengan sasaran bola', 'b2'),
            ],
            'Tepat. Handball, menarik baju, dan menjegal lawan termasuk pelanggaran.',
            'Periksa lagi: passing, heading, dan tackling yang benar adalah gerakan sah.',
        ),
        'subtitle': 'Taktik sederhana',
        'list': [
            'Formasi 4-4-2 menempatkan empat bek, empat gelandang, dan dua penyerang.',
            'Formasi 4-3-3 menambah penyerang untuk menekan lawan sejak awal.',
            'Pressing dilakukan dengan menekan pemegang bola secara berkelompok agar lawan kehilangan bola.',
            'Komunikasi singkat seperti “saya”, “kiri”, atau “jaga” mencegah tabrakan dan salah posisi.',
        ],
        'checkpoint': (
            'Berapa jarak titik penalti dari garis gawang?',
            [
                ('11 meter', True),
                ('9 meter', False),
                ('12 meter', False),
                ('10 meter', False),
            ],
            'Titik penalti berjarak 11 meter dari garis gawang.',
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
            'pjok-2-skenario',
            'Keputusan di menit terakhir',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Timmu tertinggal satu gol dan waktu tersisa dua menit. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menyusun serangan cepat dan mencari ruang terbuka', 'next': 'n2', 'score': 2, 'feedback': 'Keputusan ini memberi tim peluang terbaik.'},
                        {'text': 'Menembak dari jauh setiap kali mendapat bola', 'next': 'n3', 'score': 0, 'feedback': 'Tembakan terburu-buru mudah dihalangi.'},
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
            {'front': 'Apa itu offside?', 'back': 'Posisi penyerang lebih dekat ke garis gawang lawan daripada bola dan pemain lawan kedua.'},
            {'front': 'Apa fungsi heading?', 'back': 'Menyundul bola di udara untuk mengoper atau menembak.'},
            {'front': 'Berapa lama satu babak?', 'back': '45 menit.'},
            {'front': 'Apa itu handball?', 'back': 'Pelanggaran karena pemain lapangan menyentuh bola dengan tangan.'},
        ],
        'checkpoint': (
            'Saat menerima bola dengan lawan sangat dekat, tindakan paling aman adalah…',
            [
                ('Mengontrol bola lalu mengoper ke rekan', True),
                ('Langsung menembak tanpa melihat gawang', False),
                ('Menendang bola ke sembarang arah', False),
                ('Berhenti dan menahan bola dengan tangan', False),
            ],
            'Kontrol bola lalu operan aman menjaga penguasaan bola.',
        ),
        'challenge': challenge_block(
            'pjok-2-tantangan',
            'Tantangan istilah sepak bola',
            90,
            [
                ('Induk organisasi sepak bola Indonesia', 'PSSI'),
                ('Jumlah pemain inti', '11'),
                ('Lama satu babak', '45 menit'),
                ('Jarak titik penalti', '11 meter'),
                ('Pelanggaran menyentuh bola dengan tangan', 'handball'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa induk organisasi sepak bola Indonesia?', 'PSSI', ['PERBASI', 'PBSI', 'PBVSI'], 'PSSI adalah induk organisasi sepak bola Indonesia.', 'Bandingkan dengan PERBASI untuk bola basket.'),
        ('Berapa lama satu babak pertandingan sepak bola?', '45 menit', ['30 menit', '40 menit', '60 menit'], 'Satu babak berlangsung 45 menit.', 'Dua babak berarti 90 menit.'),
        ('Berapa jumlah pemain inti setiap tim sepak bola?', '11 pemain', ['10 pemain', '9 pemain', '12 pemain'], 'Setiap tim menurunkan sebelas pemain inti.', 'Termasuk satu penjaga gawang.'),
        ('Apa istilah operan yang langsung menghasilkan gol?', 'Assist', ['Offside', 'Corner', 'Throw-in'], 'Assist adalah operan terakhir sebelum gol.', 'Istilah ini juga dipakai di bola basket.'),
        ('Apa nama pelanggaran menyentuh bola dengan tangan?', 'Handball', ['Offside', 'Tackling', 'Dribbling'], 'Handball terjadi saat pemain lapangan menyentuh bola dengan tangan.', 'Penjaga gawang boleh memakai tangan di area penalti.'),
        ('Apa kartu yang diberikan untuk pelanggaran sangat berat?', 'Kartu merah', ['Kartu kuning', 'Kartu hijau', 'Kartu biru'], 'Kartu merah berarti pemain dikeluarkan dari pertandingan.', 'Kartu kuning hanya peringatan.'),
        ('Apa istilah tendangan dari sudut lapangan?', 'Corner kick', ['Free kick', 'Penalty kick', 'Goal kick'], 'Corner kick dilakukan dari sudut lapangan.', 'Tendangan ini terjadi saat bola melewati garis gawang setelah disentuh pemain bertahan.'),
        ('Berapa panjang lapangan sepak bola standar FIFA?', '105 meter', ['100 meter', '110 meter', '90 meter'], 'Lapangan standar FIFA berukuran 105 meter × 68 meter.', 'Lebarnya 68 meter.'),
        ('Berapa jarak titik penalti dari garis gawang?', '11 meter', ['9 meter', '10 meter', '12 meter'], 'Titik penalti berjarak 11 meter dari garis gawang.', 'Angka ini juga menjadi nama tendangan penalti.'),
        ('Apa arti offside?', 'Pemain penyerang berada lebih dekat ke garis gawang lawan daripada bola dan lawan kedua', ['Pemain keluar lapangan', 'Pemain menyentuh bola dengan tangan', 'Pemain menendang bola ke gawang sendiri'], 'Offside membatasi posisi penyerang agar tidak menunggu di belakang pertahanan.', 'Perhatikan bola dan pemain lawan kedua.'),
        ('Berapa jumlah wasit dalam pertandingan sepak bola?', '3 orang', ['1 orang', '2 orang', '4 orang'], 'Ada satu wasit utama dan dua asisten wasit.', 'Asisten berada di garis samping.'),
        ('Berapa lama babak tambahan dalam sepak bola?', '2 × 15 menit', ['2 × 10 menit', '2 × 20 menit', '1 × 30 menit'], 'Babak tambahan terdiri atas dua periode 15 menit.', 'Babak tambahan dimainkan bila skor masih imbang.'),
        ('Apa istilah menyundul bola dengan dahi?', 'Heading', ['Passing', 'Dribbling', 'Tackling'], 'Heading adalah menyundul bola, biasanya dengan dahi.', 'Mata harus tetap ke arah bola.'),
        ('Berapa berat bola sepak standar?', '410–450 gram', ['300–350 gram', '500–550 gram', '600–650 gram'], 'Bola sepak standar beratnya 410–450 gram.', 'Bola basket jauh lebih berat.'),
    ],
    'multi': [
        ('Manakah yang termasuk teknik dasar sepak bola?', ['Passing', 'Dribbling', 'Shooting'], ['Smash', 'Servis'], 'Passing, dribbling, dan shooting adalah teknik dasar sepak bola.', 'Smash dan servis berasal dari bola voli.'),
        ('Manakah yang termasuk pelanggaran dalam sepak bola?', ['Handball', 'Menarik baju lawan'], ['Passing', 'Heading'], 'Handball dan menarik baju lawan termasuk pelanggaran.', 'Passing dan heading adalah gerakan sah.'),
        ('Apa tujuan melakukan passing?', ['Memindahkan bola ke rekan', 'Membuka ruang serangan'], ['Mencetak gol langsung', 'Menghentikan waktu'], 'Passing memindahkan bola dan membuka ruang, bukan mencetak gol langsung.', 'Gol dicetak melalui shooting.'),
        ('Manakah ciri dribbling yang benar?', ['Bola dekat dengan kaki', 'Pandangan ke depan'], ['Bola ditahan dengan tangan', 'Mata selalu menunduk ke bola'], 'Dribbling benar menjaga bola dekat kaki dengan pandangan ke depan.', 'Pandangan ke depan membantu membaca lawan.'),
        ('Manakah yang termasuk jenis tendangan dalam sepak bola?', ['Tendangan bebas', 'Tendangan penalti', 'Tendangan sudut'], ['Smash', 'Jump shot'], 'Tendangan bebas, penalti, dan sudut adalah bagian permainan sepak bola.', 'Smash dan jump shot bukan istilah sepak bola.'),
        ('Manakah tugas wasit utama?', ['Mengatur jalannya pertandingan', 'Memberi kartu kepada pemain'], ['Mencetak gol', 'Menjaga gawang'], 'Wasit utama mengatur pertandingan dan memberi kartu.', 'Wasit tidak bermain untuk tim mana pun.'),
        ('Manakah formasi sepak bola yang umum?', ['4-4-2', '4-3-3', '3-5-2'], ['5-5-1', '2-2-6'], '4-4-2, 4-3-3, dan 3-5-2 adalah formasi yang umum.', 'Jumlah pemain dalam formasi harus sebelas.'),
        ('Manakah pernyataan yang benar tentang offside?', ['Penyerang tidak boleh menunggu di belakang pertahanan', 'Offside ditentukan saat bola dimainkan'], ['Offside berlaku untuk penjaga gawang', 'Offside terjadi saat bola keluar lapangan'], 'Offside membatasi posisi penyerang saat bola dimainkan.', 'Perhatikan posisi bola dan pemain lawan kedua.'),
    ],
    'pairs': [
        ('Passing', 'mengoper bola kepada rekan'),
        ('Dribbling', 'menggiring bola dengan kaki'),
        ('Shooting', 'menembak bola ke gawang'),
        ('Heading', 'menyundul bola dengan dahi'),
        ('Tackling', 'merebut bola dari lawan'),
        ('Offside', 'berada di belakang pertahanan saat bola dimainkan'),
        ('Handball', 'menyentuh bola dengan tangan'),
        ('Penalti', 'tendangan dari titik 11 meter'),
    ],
    'steps': [
        ('Urutkan langkah melakukan shooting dengan punggung kaki.', ['Letakkan kaki tumpu di samping bola', 'Tarik kaki penendang ke belakang', 'Ayunkan kaki ke arah gawang', 'Lepaskan bola dengan punggung kaki'], 'Shooting dimulai dari kaki tumpu yang stabil lalu ayunan ke gawang.', 'Arahkan pandangan ke bola saat menendang.'),
        ('Urutkan langkah melakukan passing dengan kaki bagian dalam.', ['Letakkan kaki tumpu di samping bola', 'Putar kaki penendang ke luar', 'Ayunkan kaki ke arah rekan', 'Lepaskan bola dengan kaki bagian dalam'], 'Passing kaki dalam mengarahkan bola mendatar ke rekan.', 'Perkenaan bola ada di tengah agar operan mendatar.'),
        ('Urutkan fase menggiring bola.', ['Sentuh bola dengan kaki', 'Jaga bola tetap dekat', 'Arahkan pandangan ke depan', 'Percepat langkah saat melewati lawan'], 'Dribbling menjaga bola dekat sambil membaca situasi.', 'Sentuhan kecil lebih aman daripada tendangan jauh.'),
        ('Urutkan langkah melakukan tendangan penalti.', ['Letakkan bola di titik penalti', 'Ambil awalan beberapa langkah', 'Arahkan pandangan ke target', 'Tendang bola dengan punggung kaki'], 'Penalti dimulai dari penempatan bola lalu awalan yang terkendali.', 'Jangan mengubah keputusan di detik terakhir.'),
        ('Urutkan alur serangan dari bertahan sampai mencetak gol.', ['Rebut bola dari lawan', 'Oper ke gelandang', 'Buka ruang di sayap', 'Umpan ke depan gawang', 'Selesaikan dengan shooting'], 'Serangan bergerak dari rebutan bola menuju penyelesaian di gawang.', 'Semakin cepat bola berpindah, semakin sulit lawan bertahan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
