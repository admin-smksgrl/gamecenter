"""PJOK 6 — Atletik (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 6',
    'slug': 'pjok-6-atletik',
    'title': 'Atletik',
    'description': (
        'Mempelajari nomor jalan, lari, lompat, dan lempar dalam atletik, '
        'teknik start, lari estafet, lompat jauh, serta tolak peluru.'
    ),
    'objectives': [
        'Menjelaskan nomor-nomor dalam cabang atletik.',
        'Mempraktikkan teknik start, lari, lompat jauh, dan tolak peluru.',
        'Menerapkan prinsip keselamatan dan disiplin dalam latihan atletik.',
        'Menunjukkan sportivitas dan kerja sama dalam kegiatan atletik.',
        'Menjaga kebugaran melalui pemanasan dan pendinginan yang benar.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 6 Atletik; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Atletik', 'definition': 'Cabang olahraga yang mencakup jalan, lari, lompat, dan lempar.'},
        {'term': 'Start jongkok', 'definition': 'Posisi awal berlutut untuk lari jarak pendek.'},
        {'term': 'Start berdiri', 'definition': 'Posisi awal berdiri untuk lari jarak menengah dan jauh.'},
        {'term': 'Estafet', 'definition': 'Lari berkelompok yang memindahkan tongkat dari pelari satu ke pelari berikutnya.'},
        {'term': 'Lompat jauh', 'definition': 'Melompat sejauh mungkin dari titik tolakan dengan satu kaki.'},
        {'term': 'Tolak peluru', 'definition': 'Mendorong peluru sejauh mungkin dari bahu dengan satu tangan.'},
        {'term': 'Jalan cepat', 'definition': 'Berjalan cepat dengan syarat selalu ada kaki yang menyentuh tanah.'},
        {'term': 'Diskualifikasi', 'definition': 'Pembatalan hasil karena pelanggaran aturan, misalnya start terlalu awal.'},
    ],
    'intro': {
        'material_title': 'Mengapa atletik disebut induk olahraga?',
        'title': 'Gerak dasar yang mendasari banyak cabang',
        'paragraphs': [
            'Atletik mencakup nomor jalan, lari, lompat, dan lempar. Gerakan dasarnya berupa berjalan, berlari, melompat, dan melempar, sehingga atletik disebut sebagai induk banyak cabang olahraga.',
            'Nomor lari terdiri atas jarak pendek, menengah, dan jauh, serta estafet. Nomor lompat mencakup lompat jauh, lompat tinggi, dan lompat jangkit. Nomor lempar mencakup tolak peluru, lempar lembing, dan lempar cakram.',
            'Atletik melatih kecepatan, kekuatan, daya tahan, dan koordinasi. Di Indonesia, Persatuan Atletik Seluruh Indonesia (PASI) menjadi induk organisasinya.',
        ],
        'diagram': (
            'Cabang nomor dalam atletik',
            'flowchart LR\n'
            '  A[Atletik] --> B[Jalan]\n'
            '  A --> C[Lari]\n'
            '  A --> D[Lompat]\n'
            '  A --> E[Lempar]\n'
            '  C --> F[Pendek, menengah, jauh, estafet]\n'
            '  D --> G[Jauh, tinggi, jangkit]\n'
            '  E --> H[Peluru, lembing, cakram]',
        ),
        'callout': 'Lakukan pemanasan menyeluruh, periksa lintasan dan alat, serta patuhi arahan guru agar latihan atletik aman.',
        'checkpoint': (
            'Apa induk organisasi atletik Indonesia?',
            [
                ('PASI', True),
                ('PSSI', False),
                ('PBSI', False),
                ('PERBASI', False),
            ],
            'PASI adalah Persatuan Atletik Seluruh Indonesia.',
        ),
    },
    'concept': {
        'material_title': 'Nomor dan teknik dasar',
        'title': 'Jalan, lari, lompat, dan lempar',
        'paragraphs': [
            'Lari jarak pendek meliputi 100 meter, 200 meter, dan 400 meter. Pelari jarak pendek memakai start jongkok agar dapat melesat cepat. Lari jarak menengah dan jauh memakai start berdiri.',
            'Lompat jauh terdiri atas empat fase: awalan, tolakan, melayang, dan mendarat. Tolakan dilakukan dengan satu kaki, sedangkan pendaratan memakai kedua kaki dengan lutut lentur agar aman.',
            'Tolak peluru dilakukan dengan mendorong peluru dari bahu memakai satu tangan. Berat peluru putra 7,26 kilogram dan putri 4 kilogram. Jalan cepat mewajibkan selalu ada kaki yang menyentuh tanah.',
        ],
        'table': [
            ['Nomor', 'Tujuan', 'Kunci gerak'],
            ['Lari pendek', 'Menempuh jarak tercepat', 'Start jongkok, langkah panjang, ayunan tangan kuat'],
            ['Lari estafet', 'Memindahkan tongkat cepat', 'Penerimaan tongkat di area pergantian'],
            ['Lompat jauh', 'Melompat sejauh mungkin', 'Awalan cepat, tolakan satu kaki, mendarat dua kaki'],
            ['Tolak peluru', 'Mendorong peluru jauh', 'Peluru di bahu, dorong dengan satu tangan'],
            ['Jalan cepat', 'Berjalan secepat mungkin', 'Selalu ada kaki menyentuh tanah'],
        ],
        'visual': chart_block(
            'pjok-6-berat-peluru',
            'Berat peluru dalam tolak peluru (kg)',
            'bar',
            [('Putra', 7.26), ('Putri', 4)],
        ),
        'activity': categorize_block(
            'pjok-6-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam nomor lari atau nomor lempar.',
            [('b1', 'Nomor lari'), ('b2', 'Nomor lempar')],
            [
                ('i1', 'Lari 100 meter', 'b1'),
                ('i2', 'Lari estafet', 'b1'),
                ('i3', 'Tolak peluru', 'b2'),
                ('i4', 'Lempar lembing', 'b2'),
                ('i5', 'Lari 400 meter', 'b1'),
                ('i6', 'Lempar cakram', 'b2'),
            ],
            'Tepat. Lari dan estafet termasuk nomor lari; peluru, lembing, dan cakram termasuk nomor lempar.',
            'Periksa lagi: nomor lempar memakai alat, nomor lari mengutamakan kecepatan.',
        ),
        'subtitle': 'Prinsip keselamatan',
        'list': [
            'Periksa lintasan dari kerikil atau benda yang dapat menyebabkan terpeleset.',
            'Lakukan pemanasan dan peregangan sebelum latihan lari atau lompat.',
            'Pada nomor lempar, pastikan area lemparan kosong sebelum melempar.',
            'Mendaratlah dengan lutut lentur dan jangan menahan tubuh dengan tangan.',
        ],
        'checkpoint': (
            'Berapa berat peluru untuk putra?',
            [
                ('7,26 kg', True),
                ('4 kg', False),
                ('5 kg', False),
                ('6 kg', False),
            ],
            'Peluru putra beratnya 7,26 kilogram, sedangkan putri 4 kilogram.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Berlatih dengan disiplin',
        'paragraphs': [
            'Atletik menuntut latihan berulang dan disiplin. Pelari harus menjaga ritme langkah, pelompat harus mengatur awalan, dan pelempar harus menjaga keseimbangan. Kesalahan kecil dapat mengurangi hasil.',
            'Sportivitas tampak ketika atlet mengakui pelanggaran start, menghormati hasil, dan mendukung teman. Kerja sama terlihat dalam estafet yang membutuhkan ketepatan pergantian tongkat.',
            'Gunakan latihan berpasangan untuk mengukur waktu lari dan mencatat hasil lompatan. Hentikan latihan sesaat untuk membahas teknik yang perlu diperbaiki.',
        ],
        'scenario': scenario(
            'pjok-6-skenario',
            'Keputusan saat latihan lompat jauh',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu akan melakukan lompat jauh, tetapi lintasan awalan terlihat licin. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Membersihkan lintasan dan memeriksa kembali', 'next': 'n2', 'score': 2, 'feedback': 'Keselamatan harus diperiksa sebelum latihan.'},
                        {'text': 'Tetap melompat karena sudah siap', 'next': 'n3', 'score': 0, 'feedback': 'Lintasan licin meningkatkan risiko cedera.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Saat awalan, kamu merasa langkah terlalu dekat dengan papan tolak. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Mengatur ulang awalan agar tolakan tepat', 'next': 'n4', 'score': 2, 'feedback': 'Awalan yang tepat menghasilkan tolakan yang sah.'},
                        {'text': 'Tetap melompat dan berharap hasilnya baik', 'next': 'n3', 'score': 0, 'feedback': 'Tolakan yang salah dapat membatalkan lompatan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Latihan terhenti karena risiko cedera atau lompatan batal.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Lompatan berjalan aman dan hasilnya tercatat.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu start jongkok?', 'back': 'Posisi awal berlutut untuk lari jarak pendek.'},
            {'front': 'Berapa fase lompat jauh?', 'back': 'Awalan, tolakan, melayang, dan mendarat.'},
            {'front': 'Berapa berat peluru putra?', 'back': '7,26 kilogram.'},
            {'front': 'Apa syarat jalan cepat?', 'back': 'Selalu ada kaki yang menyentuh tanah.'},
        ],
        'checkpoint': (
            'Saat mendarat setelah lompat jauh, sikap yang paling aman adalah…',
            [
                ('Mendarat dengan kedua kaki dan lutut lentur', True),
                ('Mendarat dengan satu kaki kaku', False),
                ('Menahan tubuh dengan tangan', False),
                ('Mendarat dengan badan tegak kaku', False),
            ],
            'Pendaratan dua kaki dengan lutut lentur mengurangi risiko cedera.',
        ),
        'challenge': challenge_block(
            'pjok-6-tantangan',
            'Tantangan istilah atletik',
            90,
            [
                ('Induk organisasi atletik Indonesia', 'PASI'),
                ('Jumlah pelari estafet', '4'),
                ('Berat peluru putra', '7,26 kg'),
                ('Start lari jarak pendek', 'jongkok'),
                ('Syarat jalan cepat', 'kaki selalu menyentuh tanah'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa induk organisasi atletik Indonesia?', 'PASI', ['PSSI', 'PBSI', 'PERBASI'], 'PASI adalah Persatuan Atletik Seluruh Indonesia.', 'Bandingkan dengan PSSI untuk sepak bola.'),
        ('Nomor lari 100 meter termasuk kelompok apa?', 'Lari jarak pendek', ['Lari jarak menengah', 'Lari jarak jauh', 'Jalan cepat'], '100 meter termasuk lari jarak pendek.', 'Jarak pendek berkisar 100–400 meter.'),
        ('Start apa yang dipakai untuk lari jarak pendek?', 'Start jongkok', ['Start berdiri', 'Start melayang', 'Start duduk'], 'Lari jarak pendek memakai start jongkok.', 'Start berdiri dipakai untuk jarak menengah dan jauh.'),
        ('Berapa jumlah pelari dalam satu tim estafet?', '4 pelari', ['3 pelari', '5 pelari', '6 pelari'], 'Estafet dijalankan oleh empat pelari yang memindahkan tongkat.', 'Setiap pelari menempuh satu bagian lintasan.'),
        ('Apa alat yang dipindahkan dalam lari estafet?', 'Tongkat', ['Bola', 'Shuttlecock', 'Peluru'], 'Estafet memindahkan tongkat dari pelari satu ke pelari berikutnya.', 'Tongkat harus diterima di area pergantian.'),
        ('Berapa fase dalam lompat jauh?', '4 fase', ['2 fase', '3 fase', '5 fase'], 'Lompat jauh terdiri atas awalan, tolakan, melayang, dan mendarat.', 'Tolakan dilakukan dengan satu kaki.'),
        ('Berapa berat peluru untuk putra?', '7,26 kg', ['4 kg', '5 kg', '6 kg'], 'Peluru putra beratnya 7,26 kilogram.', 'Peluru putri lebih ringan, yaitu 4 kilogram.'),
        ('Berapa berat peluru untuk putri?', '4 kg', ['7,26 kg', '3 kg', '5 kg'], 'Peluru putri beratnya 4 kilogram.', 'Perbedaan berat disesuaikan dengan kategori.'),
        ('Apa syarat utama jalan cepat?', 'Selalu ada kaki yang menyentuh tanah', ['Kedua kaki melayang', 'Berlari secepat mungkin', 'Melompat setiap langkah'], 'Jalan cepat mewajibkan selalu ada kaki yang menyentuh tanah.', 'Jika kedua kaki melayang, itu sudah menjadi lari.'),
        ('Apa nama nomor melompat sejauh mungkin?', 'Lompat jauh', ['Lompat tinggi', 'Lompat jangkit', 'Tolak peluru'], 'Lompat jauh bertujuan melompat sejauh mungkin.', 'Lompat tinggi mengukur ketinggian.'),
        ('Apa nama nomor melempar dengan alat berbentuk tombak?', 'Lempar lembing', ['Lempar cakram', 'Tolak peluru', 'Lompat jangkit'], 'Lempar lembing memakai alat berbentuk tombak.', 'Cakram berbentuk piring.'),
        ('Apa yang terjadi jika pelari start sebelum aba-aba?', 'Diskualifikasi', ['Mendapat poin tambahan', 'Lari diulang tanpa sanksi', 'Waktu dikurangi'], 'Start terlalu awal menyebabkan diskualifikasi.', 'Aturan ini menjaga keadilan perlombaan.'),
        ('Apa nama gaya lompat tinggi yang melompat membelakangi mistar?', 'Fosbury flop', ['Straddle', 'Gunting', 'Jongkok'], 'Fosbury flop dilakukan dengan membelakangi mistar.', 'Gaya straddle melompat dengan badan menyamping.'),
        ('Apa tujuan pemanasan sebelum atletik?', 'Menyiapkan otot dan mengurangi risiko cedera', ['Menambah berat badan', 'Mempercepat waktu tidur', 'Mengganti teknik dasar'], 'Pemanasan menyiapkan otot dan sendi untuk bergerak.', 'Pemanasan diikuti peregangan ringan.'),
    ],
    'multi': [
        ('Manakah yang termasuk nomor atletik?', ['Lari', 'Lompat', 'Lempar'], ['Renang', 'Bola basket'], 'Lari, lompat, dan lempar termasuk nomor atletik.', 'Renang dan bola basket cabang olahraga lain.'),
        ('Manakah yang termasuk nomor lari?', ['Lari 100 meter', 'Lari estafet'], ['Tolak peluru', 'Lompat jauh'], 'Lari 100 meter dan estafet termasuk nomor lari.', 'Tolak peluru dan lompat jauh nomor berbeda.'),
        ('Apa tujuan start jongkok?', ['Memberi dorongan awal cepat', 'Menjaga keseimbangan saat mulai'], ['Memperlambat langkah', 'Mengganti arah lari'], 'Start jongkok memberi dorongan awal dan keseimbangan.', 'Posisi tubuh lebih rendah saat mulai.'),
        ('Manakah ciri lompat jauh yang benar?', ['Tolakan dengan satu kaki', 'Mendarat dengan kedua kaki'], ['Tolakan dengan dua kaki', 'Mendarat dengan tangan'], 'Lompat jauh menolak dengan satu kaki dan mendarat dengan dua kaki.', 'Pendaratan dua kaki lebih aman.'),
        ('Manakah yang termasuk nomor lempar?', ['Tolak peluru', 'Lempar lembing', 'Lempar cakram'], ['Lompat tinggi', 'Lari 400 meter'], 'Tolak peluru, lembing, dan cakram adalah nomor lempar.', 'Lompat tinggi dan lari bukan nomor lempar.'),
        ('Manakah prinsip keselamatan dalam atletik?', ['Memeriksa lintasan', 'Memastikan area lempar kosong'], ['Melempar ke arah teman', 'Berlari tanpa pemanasan'], 'Memeriksa lintasan dan area lempar mencegah cedera.', 'Pemanasan juga penting sebelum latihan.'),
        ('Manakah pernyataan yang benar tentang estafet?', ['Tongkat diterima di area pergantian', 'Setiap pelari menempuh satu bagian'], ['Tongkat boleh dilempar', 'Pelari boleh berlari ke segala arah'], 'Estafet memindahkan tongkat di area pergantian dan setiap pelari menempuh bagiannya.', 'Kerja sama tim sangat penting.'),
        ('Manakah pernyataan yang benar tentang jalan cepat?', ['Selalu ada kaki menyentuh tanah', 'Tidak boleh ada fase melayang'], ['Kedua kaki melayang saat melangkah', 'Boleh berlari jika ingin cepat'], 'Jalan cepat tidak memiliki fase melayang.', 'Jika melayang, sudah termasuk lari.'),
    ],
    'pairs': [
        ('Start jongkok', 'posisi awal lari jarak pendek'),
        ('Start berdiri', 'posisi awal lari jarak menengah dan jauh'),
        ('Estafet', 'lari berkelompok dengan tongkat'),
        ('Lompat jauh', 'melompat sejauh mungkin'),
        ('Tolak peluru', 'mendorong peluru dari bahu'),
        ('Lempar lembing', 'melempar alat berbentuk tombak'),
        ('Jalan cepat', 'selalu ada kaki menyentuh tanah'),
        ('Diskualifikasi', 'pembatalan hasil karena pelanggaran'),
    ],
    'steps': [
        ('Urutkan fase lompat jauh.', ['Awalan', 'Tolakan', 'Melayang', 'Mendarat'], 'Lompat jauh bergerak dari awalan sampai pendaratan.', 'Tolakan dilakukan dengan satu kaki.'),
        ('Urutkan langkah melakukan start jongkok.', ['Ambil posisi jongkok di belakang garis', 'Letakkan tangan di belakang garis', 'Angkat pinggul saat aba-aba siap', 'Dorong tubuh saat aba-aba lari'], 'Start jongkok dimulai dari posisi jongkok lalu dorongan kuat.', 'Jangan start sebelum aba-aba.'),
        ('Urutkan langkah pergantian tongkat estafet.', ['Pelari pertama berlari', 'Pelari berikutnya bersiap di area pergantian', 'Tongkat diserahkan saat kedua pelari secepat mungkin', 'Penerima melanjutkan lari'], 'Pergantian tongkat harus dilakukan di area pergantian.', 'Jangan memperlambat langkah saat menerima tongkat.'),
        ('Urutkan langkah melakukan tolak peluru.', ['Pegang peluru di bahu', 'Ambil posisi di lingkaran', 'Putar badan untuk menambah tenaga', 'Dorong peluru dengan satu tangan'], 'Tolak peluru mendorong dari bahu dengan satu tangan.', 'Peluru tidak boleh dilempar seperti bola.'),
        ('Urutkan alur latihan atletik yang aman.', ['Pemanasan', 'Latihan teknik', 'Latihan intensitas ringan', 'Pendinginan'], 'Latihan atletik dimulai dari pemanasan dan diakhiri pendinginan.', 'Jangan langsung berlatih berat tanpa pemanasan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
