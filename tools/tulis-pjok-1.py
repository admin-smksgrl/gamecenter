"""PJOK 1 — Permainan Bola Basket (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 1',
    'slug': 'pjok-1-bola-basket',
    'title': 'Permainan Bola Basket',
    'description': (
        'Mengenal sejarah dan peraturan bola basket, menguasai teknik dasar '
        'passing, dribbling, shooting, pivot, dan rebound, serta menerapkan '
        'kerja sama dan sportivitas dalam permainan.'
    ),
    'objectives': [
        'Menjelaskan sejarah dan peraturan dasar permainan bola basket.',
        'Mempraktikkan teknik passing, dribbling, shooting, pivot, dan rebound.',
        'Menerapkan taktik menyerang dan bertahan sederhana dalam permainan.',
        'Menunjukkan sportivitas, kerja sama, dan disiplin selama bermain.',
        'Menjaga keselamatan diri dan teman melalui pemanasan serta pendinginan.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 1 Permainan Bola Basket; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Bola basket', 'definition': 'Olahraga dua tim berisi lima pemain yang berusaha memasukkan bola ke ring lawan.'},
        {'term': 'Dribbling', 'definition': 'Membawa bola dengan memantulkannya ke lantai memakai satu tangan.'},
        {'term': 'Passing', 'definition': 'Mengoper bola kepada rekan satu tim agar serangan berjalan.'},
        {'term': 'Pivot', 'definition': 'Memutar badan dengan satu kaki sebagai poros sambil memegang bola.'},
        {'term': 'Traveling', 'definition': 'Pelanggaran karena melangkah lebih dari dua langkah tanpa menggiring bola.'},
        {'term': 'Rebound', 'definition': 'Merebut bola yang memantul dari ring atau papan pantul.'},
        {'term': 'Man-to-man', 'definition': 'Pertahanan ketika setiap pemain menjaga satu lawan tertentu.'},
        {'term': 'Shot clock', 'definition': 'Batas waktu menembak ke ring, yaitu 24 detik dalam aturan FIBA.'},
    ],
    'intro': {
        'material_title': 'Mengapa bola basket penting?',
        'title': 'Permainan cepat yang menuntut kerja sama',
        'paragraphs': [
            'Bola basket adalah permainan bola besar yang dimainkan dua tim. Setiap tim berusaha memasukkan bola ke ring lawan sekaligus mencegah lawan mencetak poin. Permainan ini menuntut kecepatan, koordinasi mata dan tangan, serta keputusan cepat.',
            'James Naismith menciptakan bola basket pada tahun 1891 di Springfield, Massachusetts, Amerika Serikat. Ia mencari permainan dalam ruangan yang tetap menggerakkan seluruh tubuh. Di Indonesia, organisasi bola basket bernama PERBASI berdiri pada 23 Oktober 1951.',
            'Manfaat bola basket tidak hanya kebugaran. Permainan ini melatih komunikasi, pembagian peran, dan pengendalian diri. Pemain yang baik tahu kapan harus menembak, mengoper, atau bertahan.',
        ],
        'diagram': (
            'Alur dasar permainan bola basket',
            'flowchart LR\n'
            '  A[Menguasai bola] --> B[Passing atau dribbling]\n'
            '  B --> C[Membuka ruang]\n'
            '  C --> D[Shooting ke ring]\n'
            '  D --> E[Rebound]\n'
            '  E --> F[Bertahan dan serang lagi]',
        ),
        'callout': 'Selalu lakukan pemanasan, potong kuku, dan lepas aksesori sebelum bermain agar cedera dapat dicegah.',
        'checkpoint': (
            'Siapa yang menciptakan permainan bola basket?',
            [
                ('James Naismith', True),
                ('William G. Morgan', False),
                ('Pierre de Coubertin', False),
                ('Friedrich Ludwig Jahn', False),
            ],
            'James Naismith menciptakan bola basket pada 1891; William Morgan menciptakan bola voli.',
        ),
    },
    'concept': {
        'material_title': 'Peraturan dan teknik dasar',
        'title': 'Peraturan, teknik, dan taktik',
        'paragraphs': [
            'Lapangan bola basket berukuran panjang 28 meter dan lebar 15 meter menurut FIBA. Ring dipasang setinggi 3,05 meter dari lantai. Satu tim menurunkan lima pemain inti, sedangkan pemain lain menunggu di bangku cadangan.',
            'Poin diperoleh dari lemparan bebas (1 poin), tembakan dari dalam garis tiga poin (2 poin), dan tembakan dari luar garis tiga poin (3 poin). Permainan FIBA terdiri atas empat kuarter, masing-masing 10 menit.',
            'Pelanggaran umum meliputi traveling, double dribble, carrying, foul, dan pelanggaran tiga detik di area terlarang. Setiap tim juga dibatasi 24 detik untuk menembak ke ring.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Passing', 'Memindahkan bola dengan cepat', 'Pandangan ke rekan, dorong bola dengan jari'],
            ['Dribbling', 'Melewati lawan atau membuka ruang', 'Bola dipantulkan, lutut lentur, tangan di atas bola'],
            ['Shooting', 'Mencetak poin', 'Siku mengarah ke ring, lepaskan dengan ujung jari'],
            ['Pivot', 'Melindungi bola dari lawan', 'Satu kaki menjadi poros, kaki poros tidak diangkat'],
            ['Rebound', 'Menguasai bola pantul', 'Rebut posisi, lompat, raih bola dengan dua tangan'],
        ],
        'visual': chart_block(
            'pjok-1-nilai-poin',
            'Nilai poin dalam bola basket',
            'bar',
            [('Lemparan bebas', 1), ('Tembakan 2 poin', 2), ('Tembakan 3 poin', 3)],
        ),
        'activity': categorize_block(
            'pjok-1-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pelanggaran atau gerak sah.',
            [('b1', 'Pelanggaran'), ('b2', 'Gerak sah')],
            [
                ('i1', 'Melangkah lebih dari dua langkah tanpa dribble', 'b1'),
                ('i2', 'Menggiring bola lagi setelah berhenti', 'b1'),
                ('i3', 'Memutar badan dengan satu kaki poros', 'b2'),
                ('i4', 'Mengoper bola ke rekan satu tim', 'b2'),
                ('i5', 'Menahan bola lebih dari tiga detik di area terlarang', 'b1'),
                ('i6', 'Merebut bola pantul dari ring', 'b2'),
            ],
            'Tepat. Traveling, double dribble, dan pelanggaran tiga detik termasuk pelanggaran.',
            'Periksa lagi: pivot, passing, dan rebound adalah gerakan sah.',
        ),
        'subtitle': 'Taktik sederhana',
        'list': [
            'Serangan cepat (fast break) dimulai dari rebound atau steal, lalu bola dioper cepat ke depan.',
            'Pick and roll memakai satu pemain sebagai penghalang agar rekan bisa bergerak bebas.',
            'Pertahanan man-to-man menjaga satu lawan, sedangkan pertahanan zona menjaga area tertentu.',
            'Komunikasi singkat seperti “saya”, “kiri”, atau “ganti” mencegah tabrakan dan salah jaga.',
        ],
        'checkpoint': (
            'Berapa batas waktu shot clock dalam aturan FIBA?',
            [
                ('24 detik', True),
                ('30 detik', False),
                ('20 detik', False),
                ('14 detik', False),
            ],
            'FIBA memberi waktu 24 detik bagi tim untuk melepaskan tembakan ke ring.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bermain dengan sportif',
        'paragraphs': [
            'Permainan sesungguhnya menguji keputusan, bukan hanya teknik. Pemain harus membaca posisi rekan dan lawan, lalu memilih antara menembak, mengoper, atau menggiring. Keputusan yang tergesa-gesa sering menghasilkan kehilangan bola.',
            'Sportivitas tampak ketika pemain mengakui pelanggaran, membantu lawan yang jatuh, dan menghormati keputusan wasit. Kerja sama dibangun melalui komunikasi dan pembagian peran yang jelas.',
            'Gunakan permainan kecil tiga lawan tiga untuk melatih passing cepat, pergerakan tanpa bola, dan pertahanan. Hentikan permainan sesaat untuk membahas keputusan yang tepat.',
        ],
        'scenario': scenario(
            'pjok-1-skenario',
            'Keputusan di menit terakhir',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Timmu tertinggal dua poin dan waktu tersisa 30 detik. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menyusun serangan cepat dan mencari tembakan terbuka', 'next': 'n2', 'score': 2, 'feedback': 'Keputusan ini memberi tim peluang terbaik.'},
                        {'text': 'Memaksa tembakan sendiri dari luar garis', 'next': 'n3', 'score': 0, 'feedback': 'Tembakan terburu-buru mudah dihalangi.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Rekanmu kosong di bawah ring, tetapi kamu juga punya ruang menembak. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Mengoper ke rekan yang lebih kosong', 'next': 'n4', 'score': 2, 'feedback': 'Operan ke posisi terbaik adalah inti kerja sama.'},
                        {'text': 'Tetap menembak meski dijaga', 'next': 'n3', 'score': 0, 'feedback': 'Peluang rekan yang lebih baik terbuang.'},
                    ],
                },
                {'id': 'n3', 'text': 'Peluang habis karena keputusan diambil tergesa-gesa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tim mencetak poin dan bermain sebagai satu kesatuan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu traveling?', 'back': 'Melangkah lebih dari dua langkah tanpa menggiring bola.'},
            {'front': 'Apa fungsi pivot?', 'back': 'Melindungi bola dengan memutar badan memakai satu kaki poros.'},
            {'front': 'Apa itu rebound?', 'back': 'Merebut bola yang memantul dari ring atau papan pantul.'},
            {'front': 'Berapa tinggi ring?', 'back': '3,05 meter dari lantai.'},
        ],
        'checkpoint': (
            'Saat menerima bola dengan lawan sangat dekat, tindakan paling aman adalah…',
            [
                ('Melakukan pivot untuk melindungi bola', True),
                ('Langsung menembak tanpa melihat ring', False),
                ('Melempar bola ke sembarang arah', False),
                ('Berhenti dan menahan bola dengan dua tangan', False),
            ],
            'Pivot melindungi bola sambil membuka pandangan untuk mencari rekan.',
        ),
        'challenge': challenge_block(
            'pjok-1-tantangan',
            'Tantangan istilah bola basket',
            90,
            [
                ('Pencipta bola basket', 'James Naismith'),
                ('Tinggi ring', '3,05 m'),
                ('Jumlah pemain inti', '5'),
                ('Batas waktu menembak', '24 detik'),
                ('Organisasi bola basket Indonesia', 'PERBASI'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Siapa pencipta permainan bola basket?', 'James Naismith', ['William G. Morgan', 'Michael Jordan', 'Pierre de Coubertin'], 'James Naismith menciptakan bola basket pada 1891.', 'Ingat nama pencipta bola voli sebagai pembanding.'),
        ('Berapa tinggi ring bola basket dari lantai?', '3,05 meter', ['2,43 meter', '2,24 meter', '3,50 meter'], 'Ring bola basket dipasang 3,05 meter dari lantai.', 'Angka ini juga dipakai pada kompetisi FIBA.'),
        ('Berapa jumlah pemain inti setiap tim bola basket?', '5 pemain', ['6 pemain', '7 pemain', '11 pemain'], 'Setiap tim menurunkan lima pemain inti.', 'Bandingkan dengan bola voli yang enam pemain.'),
        ('Berapa nilai tembakan dari luar garis tiga poin?', '3 poin', ['1 poin', '2 poin', '4 poin'], 'Tembakan dari luar garis tiga poin bernilai tiga angka.', 'Semakin jauh garis, semakin besar nilainya.'),
        ('Apa nama pelanggaran melangkah tanpa menggiring bola?', 'Traveling', ['Double dribble', 'Pivot', 'Rebound'], 'Traveling terjadi saat pemain melangkah lebih dari dua langkah tanpa dribble.', 'Kata dasarnya berhubungan dengan “bepergian”.'),
        ('Apa organisasi bola basket Indonesia?', 'PERBASI', ['PSSI', 'PBSI', 'PBVSI'], 'PERBASI adalah induk organisasi bola basket Indonesia.', 'Bandingkan dengan PSSI untuk sepak bola.'),
        ('Berapa batas waktu shot clock FIBA?', '24 detik', ['30 detik', '20 detik', '14 detik'], 'FIBA menetapkan 24 detik untuk melepaskan tembakan.', 'Angka ini lebih pendek daripada satu kuarter.'),
        ('Berapa panjang lapangan bola basket FIBA?', '28 meter', ['26 meter', '30 meter', '24 meter'], 'Lapangan FIBA berukuran 28 meter × 15 meter.', 'Lebarnya 15 meter.'),
        ('Berapa ukuran papan pantul bola basket?', '1,8 m × 1,05 m', ['1,2 m × 0,9 m', '2,0 m × 1,2 m', '1,5 m × 1,0 m'], 'Papan pantul FIBA berukuran 1,8 meter × 1,05 meter.', 'Papan lebih lebar daripada tinggi.'),
        ('Berapa diameter ring bola basket?', '45 cm', ['40 cm', '50 cm', '35 cm'], 'Diameter ring sekitar 45 cm agar bola dapat masuk.', 'Bola berdiameter sekitar 24 cm.'),
        ('Berapa lama satu kuarter dalam aturan FIBA?', '10 menit', ['12 menit', '8 menit', '15 menit'], 'Satu kuarter FIBA berlangsung 10 menit.', 'Ada empat kuarter dalam satu pertandingan.'),
        ('Apa istilah merebut bola pantul dari ring?', 'Rebound', ['Steal', 'Assist', 'Block'], 'Rebound adalah merebut bola yang memantul dari ring atau papan.', 'Istilah ini juga dipakai dalam statistik pemain.'),
        ('Apa nama pertahanan satu lawan satu?', 'Man-to-man', ['Zona', 'Press', 'Fast break'], 'Man-to-man berarti setiap pemain menjaga satu lawan.', 'Lawannya adalah pertahanan zona.'),
        ('Berapa berat bola basket FIBA?', '600–650 gram', ['410–450 gram', '500–550 gram', '700–750 gram'], 'Bola basket FIBA beratnya 600–650 gram.', 'Bola sepak jauh lebih ringan.'),
    ],
    'multi': [
        ('Manakah yang termasuk teknik dasar bola basket?', ['Passing', 'Dribbling', 'Shooting'], ['Smash', 'Servis'], 'Passing, dribbling, dan shooting adalah teknik dasar bola basket.', 'Smash dan servis berasal dari bola voli.'),
        ('Manakah yang termasuk pelanggaran dalam bola basket?', ['Traveling', 'Double dribble'], ['Pivot', 'Rebound'], 'Traveling dan double dribble termasuk pelanggaran.', 'Pivot dan rebound adalah gerakan sah.'),
        ('Apa tujuan melakukan passing?', ['Memindahkan bola ke rekan', 'Membuka ruang serangan'], ['Mencetak poin langsung', 'Menghentikan waktu'], 'Passing memindahkan bola dan membuka ruang, bukan mencetak poin langsung.', 'Poin dicetak melalui shooting.'),
        ('Manakah ciri dribbling yang benar?', ['Bola dipantulkan dengan satu tangan', 'Lutut lentur dan pandangan ke depan'], ['Bola ditahan dengan dua tangan', 'Mata selalu menunduk ke bola'], 'Dribbling benar memakai satu tangan dengan lutut lentur dan pandangan ke depan.', 'Pandangan ke depan membantu membaca lawan.'),
        ('Manakah yang termasuk tembakan dalam bola basket?', ['Lay-up', 'Jump shot', 'Free throw'], ['Smash', 'Heading'], 'Lay-up, jump shot, dan free throw adalah tembakan bola basket.', 'Smash dan heading bukan istilah bola basket.'),
        ('Manakah pernyataan yang benar tentang pertahanan?', ['Man-to-man menjaga satu lawan', 'Zona menjaga area tertentu'], ['Man-to-man menjaga area', 'Zona menjaga satu lawan'], 'Man-to-man menjaga lawan, zona menjaga area.', 'Nama jenis pertahanan menggambarkan tugasnya.'),
        ('Manakah yang termasuk pelanggaran saat menyerang?', ['Traveling', 'Double dribble', 'Tiga detik di area terlarang'], ['Pivot', 'Chest pass'], 'Traveling, double dribble, dan pelanggaran tiga detik membatasi penyerang.', 'Pivot dan chest pass adalah gerakan sah.'),
        ('Manakah pernyataan yang benar tentang nilai poin?', ['Lemparan bebas bernilai 1 poin', 'Tembakan dalam garis bernilai 2 poin', 'Tembakan luar garis bernilai 3 poin'], ['Semua tembakan bernilai 2 poin', 'Dunk bernilai 1 poin'], 'Nilai poin bergantung pada jenis dan posisi tembakan.', 'Lemparan bebas adalah tembakan paling sederhana.'),
    ],
    'pairs': [
        ('Passing', 'mengoper bola kepada rekan'),
        ('Dribbling', 'memantulkan bola ke lantai'),
        ('Pivot', 'memutar badan dengan satu kaki poros'),
        ('Rebound', 'merebut bola pantul dari ring'),
        ('Traveling', 'melangkah lebih dari dua langkah tanpa dribble'),
        ('Double dribble', 'menggiring lagi setelah berhenti'),
        ('Man-to-man', 'setiap pemain menjaga satu lawan'),
        ('Shot clock', 'batas 24 detik untuk menembak'),
    ],
    'steps': [
        ('Urutkan langkah melakukan chest pass.', ['Pegang bola di depan dada', 'Tekuk siku di samping badan', 'Dorong bola ke depan', 'Lepaskan dengan jari mengarah ke rekan'], 'Chest pass dimulai dari pegangan di dada lalu didorong lurus ke rekan.', 'Bayangkan bola bergerak lurus dari dada ke dada.'),
        ('Urutkan langkah lay-up dari sisi kanan.', ['Awalan dua langkah', 'Tolakan kaki kiri', 'Angkat lutut kanan', 'Lepaskan bola ke ring'], 'Lay-up kanan memakai tolakan kaki kiri dan lutut kanan terangkat.', 'Kaki tolak berlawanan dengan tangan yang menembak.'),
        ('Urutkan fase gerak jump shot.', ['Berdiri seimbang', 'Tekuk lutut', 'Angkat bola ke atas', 'Lepaskan saat lompatan tertinggi'], 'Jump shot melepaskan bola pada titik tertinggi lompatan.', 'Lepaskan bola sebelum mulai turun.'),
        ('Urutkan langkah melakukan pivot.', ['Terima bola', 'Tetapkan satu kaki sebagai poros', 'Putar badan menjauhi lawan', 'Cari rekan atau tembakan'], 'Pivot dimulai dari menerima bola lalu memutar badan dengan kaki poros.', 'Kaki poros tidak boleh diangkat.'),
        ('Urutkan alur serangan cepat.', ['Rebound defensif', 'Oper cepat ke depan', 'Isi jalur sayap', 'Selesaikan dengan lay-up'], 'Fast break bergerak dari rebound ke operan cepat lalu penyelesaian di ring.', 'Semakin sedikit dribble, semakin cepat serangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
