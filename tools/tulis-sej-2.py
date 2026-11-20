"""SEJ 2 — Penelitian Sejarah (Fase E)."""
from sejarah_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'SEJ 2',
    'slug': 'sej-2-penelitian-sejarah',
    'title': 'Penelitian Sejarah',
    'description': (
        'Menelusuri jejak masa lalu melalui sumber primer dan sekunder, menilai '
        'keaslian dan kredibilitasnya, lalu menyusun langkah penelitian sejarah '
        'berbasis lingkungan terdekat.'
    ),
    'objectives': [
        'Membedakan sumber sejarah primer dan sekunder beserta contohnya.',
        'Menjelaskan kritik ekstern dan intern dalam menilai sumber sejarah.',
        'Menyusun langkah-langkah penelitian sejarah dari pemilihan topik hingga penulisan.',
        'Melakukan penelitian sejarah sederhana berbasis lingkungan terdekat.',
    ],
    'minutes': 180,
    'source': (
        'Sejarah-BG-KLS-X.pdf materi Penelitian Sejarah dan Proyek Penelitian Sejarah; '
        'CP Fase E Mata Pelajaran Sejarah'
    ),
    'glossary': [
        {'term': 'Sumber primer', 'definition': 'Sumber yang dihasilkan pada masa peristiwa terjadi atau oleh pelaku langsung, misalnya arsip, foto sezaman, dan kesaksian pelaku.'},
        {'term': 'Sumber sekunder', 'definition': 'Sumber yang ditulis belakangan berdasarkan sumber primer, misalnya buku teks dan artikel sejarah.'},
        {'term': 'Kritik ekstern', 'definition': 'Penilaian keaslian sumber: bahan, gaya, waktu pembuatan, dan asal dokumen.'},
        {'term': 'Kritik intern', 'definition': 'Penilaian kredibilitas isi sumber: kesesuaian isi dengan bukti lain dan kepentingan penulisnya.'},
        {'term': 'Heuristik', 'definition': 'Tahap mencari dan mengumpulkan sumber sejarah.'},
        {'term': 'Verifikasi', 'definition': 'Tahap menguji kebenaran sumber setelah pengumpulan.'},
        {'term': 'Interpretasi', 'definition': 'Tahap menafsirkan data dan menghubungkan fakta menjadi peristiwa bermakna.'},
        {'term': 'Historiografi', 'definition': 'Tahap penulisan kisah sejarah berdasarkan fakta yang telah diuji.'},
        {'term': 'Sejarah lisan', 'definition': 'Kesaksian yang diperoleh melalui wawancara dengan pelaku atau saksi peristiwa.'},
    ],
    'intro': {
        'material_title': 'Jejak masa lalu',
        'title': 'Dari mana sejarah mengetahui masa lalu?',
        'paragraphs': [
            'Sejarah tidak lahir dari ingatan tanpa bukti. Sejarawan bekerja dengan sumber: arsip, surat, foto, bangunan, benda, peta, koran sezaman, dan kesaksian orang yang mengalami peristiwa.',
            'Sumber primer dihasilkan pada masa peristiwa terjadi atau oleh pelakunya. Sumber sekunder ditulis belakangan oleh orang yang tidak mengalami langsung, misalnya buku dan artikel sejarah.',
            'Semakin banyak sumber yang saling menguatkan, semakin kuat kesimpulan sejarah. Sebaliknya, satu sumber tunggal tanpa pembanding harus dinyatakan sebagai dugaan, bukan fakta final.',
        ],
        'diagram': (
            'Alur penelitian sejarah',
            'flowchart LR\n'
            '  A[Pemilihan topik] --> B[Heuristik: mencari sumber]\n'
            '  B --> C[Verifikasi: kritik ekstern dan intern]\n'
            '  C --> D[Interpretasi: menafsirkan fakta]\n'
            '  D --> E[Historiografi: menulis kisah]\n'
            '  E --> F[Karya sejarah yang dapat diuji]',
        ),
        'callout': 'Tanpa verifikasi, cerita masa lalu hanya menjadi dongeng yang menarik tetapi tidak dapat dipertanggungjawabkan.',
        'checkpoint': (
            'Foto yang diambil pada saat peristiwa berlangsung termasuk sumber…',
            [
                ('primer', True),
                ('sekunder', False),
                ('tersier', False),
                ('fiktif', False),
            ],
            'Sumber primer dibuat pada masa peristiwa atau oleh pelakunya langsung.',
        ),
    },
    'concept': {
        'material_title': 'Menilai sumber',
        'title': 'Kritik ekstern dan kritik intern',
        'paragraphs': [
            'Kritik ekstern memeriksa keaslian sumber: bahan kertas, jenis tinta, ejaan, cap, dan riwayat penyimpanan. Dokumen yang ejaannya tidak sesuai zaman patut dicurigai sebagai tiruan.',
            'Kritik intern memeriksa isi: apakah keterangan sumber masuk akal, sesuai dengan sumber lain, dan apakah penulisnya punya kepentingan tertentu. Kesaksian yang menguntungkan diri sendiri perlu ditimbang hati-hati.',
            'Setelah lolos kedua kritik, data ditafsirkan. Interpretasi bukan mengarang; ia menyusun fakta menjadi penjelasan yang logis tentang apa yang terjadi, mengapa, dan apa akibatnya.',
        ],
        'table': [
            ['Jenis sumber', 'Contoh', 'Kegunaan'],
            ['Sumber primer tertulis', 'Arsip, surat, akta, koran sezaman', 'Bukti langsung peristiwa'],
            ['Sumber primer lisan', 'Wawancara pelaku atau saksi', 'Keterangan pengalaman langsung'],
            ['Sumber primer benda', 'Bangunan, alat, foto', 'Bukti fisik dan visual'],
            ['Sumber sekunder', 'Buku, artikel, ensiklopedia', 'Penjelasan dan konteks'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'sej-2-kritik-sumber',
            'engine': 'mermaid',
            'title': 'Penyaringan sumber sebelum menjadi fakta',
            'code': 'flowchart TB\n'
                    '  A[Sumber ditemukan] --> B{Asli?}\n'
                    '  B -- Tidak --> Z[Ditolak atau dipakai hati-hati]\n'
                    '  B -- Ya --> C{Kredibel?}\n'
                    '  C -- Tidak --> Z\n'
                    '  C -- Ya --> D[Fakta sejarah]\n'
                    '  D --> E[Interpretasi]\n'
                    '  E --> F[Kisah sejarah tertulis]',
        },
        'activity': categorize_block(
            'sej-2-klasifikasi',
            'Kelompokkan sumber berikut sebagai sumber primer atau sekunder.',
            [('b1', 'Sumber primer'), ('b2', 'Sumber sekunder')],
            [
                ('i1', 'Akta kelahiran tahun 1950', 'b1'),
                ('i2', 'Buku teks sejarah kelas X', 'b2'),
                ('i3', 'Wawancara dengan pelaku peristiwa', 'b1'),
                ('i4', 'Artikel majalah sejarah terbitan 2020', 'b2'),
                ('i5', 'Foto upacara kemerdekaan tahun 1950', 'b1'),
                ('i6', 'Ensiklopedia sejarah Indonesia', 'b2'),
                ('i7', 'Surat pribadi seorang pejuang', 'b1'),
                ('i8', 'Ringkasan materi di situs pembelajaran', 'b2'),
            ],
            'Tepat. Primer lahir pada masa peristiwa, sekunder ditulis belakangan.',
            'Periksa lagi: yang dibuat setelah peristiwa dan berdasarkan sumber lain termasuk sekunder.',
        ),
        'subtitle': 'Prinsip kerja penelitian sejarah',
        'list': [
            'Topik harus terbatas dan terjangkau agar sumbernya dapat ditemukan di lingkungan terdekat.',
            'Sumber perlu dicatat lengkap: siapa pembuatnya, kapan, di mana, dan dalam keadaan apa.',
            'Satu fakta sebaiknya dibuktikan lebih dari satu sumber agar tidak bergantung pada satu kesaksian.',
            'Laporan penelitian harus terbuka: menyebut sumber, menyadari keterbatasan, dan menghindari kesimpulan berlebihan.',
        ],
        'checkpoint': (
            'Pemeriksaan keaslian bahan dan waktu pembuatan dokumen disebut kritik…',
            [
                ('ekstern', True),
                ('intern', False),
                ('interpretasi', False),
                ('heuristik', False),
            ],
            'Kritik ekstern menilai keaslian fisik dan asal sumber; kritik intern menilai isinya.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Proyek sejarah lingkungan terdekat',
        'paragraphs': [
            'Pilih satu gejala sejarah di sekitarmu: berdirinya pasar, perubahan nama jalan, bangunan tua, atau tradisi kampung. Tetapkan batas waktu dan tempat agar kajian tidak melebar.',
            'Kumpulkan sumber: foto lama, arsip kelurahan, koran daerah, dan wawancara warga tua. Catat identitas narasumber dan tanggal wawancara sebagai bukti kerja.',
            'Bandingkan sumber, tulis temuan secara berurutan, lalu presentasikan. Sebutkan bagian yang belum pasti agar pembaca tahu batas pengetahuanmu.',
        ],
        'scenario': scenario(
            'sej-2-skenario',
            'Bukti yang saling bertentangan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Wawancara warga menyebut pasar berdiri 1935, sedangkan arsip kelurahan mencatat 1948. Sikapmu?',
                    'choices': [
                        {'text': 'Mencari sumber ketiga, misalnya koran atau foto lama', 'next': 'n2', 'score': 2, 'feedback': 'Sumber pembanding membantu menilai dua keterangan yang berbeda.'},
                        {'text': 'Memilih angka yang lebih tua agar terkesan bersejarah', 'next': 'n3', 'score': 0, 'feedback': 'Memilih data demi kesan menarik bukan cara kerja sejarah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Sumber ketiga mendukung tahun 1948. Bagaimana melaporkannya?',
                    'choices': [
                        {'text': 'Menuliskan tahun 1948 dengan menyebut perbedaan keterangan warga', 'next': 'n4', 'score': 2, 'feedback': 'Laporan jujur menyebut perbedaan dan alasan pemilihannya.'},
                        {'text': 'Menulis 1948 tanpa menyebut sumber lain', 'next': 'n3', 'score': 0, 'feedback': 'Menyembunyikan keterangan lain membuat laporan tidak transparan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Laporanmu lemah karena tidak dapat diperiksa ulang.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Laporanmu kuat, terbuka, dan dapat diuji siapa pun.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu sumber primer?', 'back': 'Sumber dari masa peristiwa atau pelaku langsung.'},
            {'front': 'Apa beda kritik ekstern dan intern?', 'back': 'Ekstern menilai keaslian; intern menilai kredibilitas isi.'},
            {'front': 'Sebutkan empat tahap penelitian sejarah.', 'back': 'Heuristik, verifikasi, interpretasi, historiografi.'},
            {'front': 'Mengapa perlu lebih dari satu sumber?', 'back': 'Agar fakta tidak bergantung pada satu kesaksian yang mungkin keliru.'},
        ],
        'checkpoint': (
            'Tahap mencari dan mengumpulkan sumber disebut…',
            [
                ('heuristik', True),
                ('historiografi', False),
                ('interpretasi', False),
                ('verifikasi', False),
            ],
            'Heuristik adalah tahap pencarian sumber; verifikasi mengujinya.',
        ),
        'challenge': challenge_block(
            'sej-2-tantangan',
            'Tantangan istilah penelitian sejarah',
            90,
            [
                ('Sumber dari masa peristiwa', 'Sumber primer'),
                ('Penilaian keaslian sumber', 'Kritik ekstern'),
                ('Tahap pencarian sumber', 'Heuristik'),
                ('Penulisan kisah sejarah', 'Historiografi'),
                ('Kesaksian pelaku peristiwa', 'Sejarah lisan'),
            ],
            'Lima istilah penelitian sejarah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Sumber yang dihasilkan pada masa peristiwa terjadi disebut…', 'sumber primer', ['sumber sekunder', 'sumber tersier', 'sumber fiktif'], 'Primer berasal dari masa peristiwa atau pelakunya.', 'Sekunder ditulis belakangan.'),
        ('Buku teks sejarah termasuk sumber…', 'sekunder', ['primer', 'lisan', 'benda'], 'Buku teks disusun berdasarkan sumber lain.', 'Bukan dibuat pada masa peristiwa.'),
        ('Wawancara dengan pelaku peristiwa termasuk sumber…', 'primer', ['sekunder', 'tersier', 'palsu'], 'Kesaksian pelaku adalah sumber primer lisan.', 'Perlu dicatat identitas dan tanggalnya.'),
        ('Penilaian keaslian bahan dan waktu pembuatan sumber disebut…', 'kritik ekstern', ['kritik intern', 'interpretasi', 'heuristik'], 'Kritik ekstern memeriksa fisik dan asal dokumen.', 'Kritik intern memeriksa isi.'),
        ('Penilaian kredibilitas isi sumber disebut…', 'kritik intern', ['kritik ekstern', 'historiografi', 'verifikasi luar'], 'Kritik intern menimbang isi dan kepentingan penulis.', 'Misalnya kesaksian yang menguntungkan diri sendiri.'),
        ('Tahap mengumpulkan sumber dalam penelitian sejarah disebut…', 'heuristik', ['interpretasi', 'historiografi', 'kritik intern'], 'Heuristik berarti mencari.', 'Tahap pertama setelah memilih topik.'),
        ('Tahap menafsirkan fakta menjadi penjelasan disebut…', 'interpretasi', ['heuristik', 'historiografi', 'verifikasi'], 'Interpretasi menyusun fakta menjadi penjelasan logis.', 'Bukan mengarang.'),
        ('Tahap menuliskan kisah sejarah disebut…', 'historiografi', ['heuristik', 'interpretasi', 'kritik ekstern'], 'Historiografi adalah penulisan sejarah.', 'Tahap terakhir penelitian.'),
        ('Topik penelitian sejarah sebaiknya…', 'terbatas dan terjangkau sumbernya', ['seluas mungkin', 'tanpa batas waktu', 'tanpa sumber'], 'Topik terbatas memudahkan pencarian sumber.', 'Sesuaikan dengan lingkungan terdekat.'),
        ('Sumber tertulis yang dibuat pada masa peristiwa, misalnya…', 'arsip dan surat sezaman', ['ensiklopedia modern', 'buku pelajaran', 'artikel blog'], 'Arsip dan surat sezaman adalah bukti langsung.', 'Ensiklopedia bersifat sekunder.'),
        ('Agar kesimpulan sejarah kuat, sebaiknya…', 'menggunakan beberapa sumber yang saling menguatkan', ['memakai satu sumber saja', 'memilih sumber yang menarik', 'mengabaikan sumber berbeda'], 'Banyak sumber memperkuat kesimpulan.', 'Satu sumber tunggal masih dugaan.'),
        ('Sumber lisan dalam penelitian sejarah diperoleh melalui…', 'wawancara dengan pelaku atau saksi', ['membaca novel', 'menonton film fiksi', 'menebak sendiri'], 'Sejarah lisan bergantung pada kesaksian langsung.', 'Catat identitas narasumber.'),
        ('Sikap yang benar bila sumber saling bertentangan adalah…', 'mencari sumber pembanding dan menuliskan perbedaannya', ['menyembunyikan salah satu', 'memilih yang paling menarik', 'berhenti meneliti'], 'Keterbukaan menjaga kejujuran laporan.', 'Perbedaan adalah bagian dari temuan.'),
        ('Laporan penelitian sejarah harus memuat…', 'sumber dan keterbatasan kajian', ['hanya kesimpulan', 'hanya foto', 'hanya pendapat pribadi'], 'Pembaca perlu tahu dasar dan batas pengetahuan.', 'Tanpa sumber, laporan tidak dapat diuji.'),
    ],
    'multi': [
        ('Manakah yang termasuk sumber primer?', ['Arsip kelurahan', 'Foto sezaman', 'Wawancara pelaku'], ['Buku teks', 'Ensiklopedia'], 'Primer lahir pada masa peristiwa.', 'Buku dan ensiklopedia bersifat sekunder.'),
        ('Manakah yang termasuk sumber sekunder?', ['Buku sejarah', 'Artikel majalah', 'Ringkasan pelajaran'], ['Akta kelahiran', 'Surat asli'], 'Sekunder disusun berdasarkan sumber lain.', 'Akta dan surat adalah primer.'),
        ('Manakah tahap penelitian sejarah?', ['Heuristik', 'Verifikasi', 'Interpretasi'], ['Menghafal tahun', 'Menyalin tanpa sumber'], 'Penelitian melalui tahap pencarian, pengujian, dan penafsiran.', 'Hafalan bukan tahap penelitian.'),
        ('Manakah yang diperiksa dalam kritik ekstern?', ['Bahan dan tinta', 'Ejaan dan gaya tulisan', 'Asal dan riwayat dokumen'], ['Makna isi', 'Kepentingan penulis'], 'Kritik ekstern menilai keaslian fisik.', 'Isi dinilai lewat kritik intern.'),
        ('Manakah yang diperiksa dalam kritik intern?', ['Kesesuaian isi dengan sumber lain', 'Kepentingan penulis', 'Kelayakan keterangan'], ['Bahan kertas', 'Jenis tinta'], 'Kritik intern menilai kredibilitas isi.', 'Bahan dan tinta urusan kritik ekstern.'),
        ('Manakah sumber untuk sejarah lingkungan terdekat?', ['Foto lama kampung', 'Arsip kelurahan', 'Wawancara warga senior'], ['Ramalan cuaca', 'Novel fantasi'], 'Sejarah lokal dapat ditelusuri dari sumber setempat.', 'Fiksi bukan sumber sejarah.'),
        ('Manakah sikap jujur dalam laporan penelitian?', ['Menyebut sumber', 'Menyatakan keterbatasan', 'Menuliskan perbedaan sumber'], ['Menyembunyikan bukti yang berbeda', 'Mengarang data'], 'Kejujuran membuat laporan dapat diuji.', 'Mengarang merusak kredibilitas.'),
        ('Manakah ciri sumber yang perlu dicurigai?', ['Ejaan tidak sesuai zaman', 'Isi menguntungkan penulis sendiri', 'Tidak jelas asalnya'], ['Dibuat pada masa peristiwa', 'Disimpan di arsip resmi'], 'Ciri itu menuntut kritik lebih ketat.', 'Sumber resmi sezaman lebih kuat.'),
    ],
    'pairs': [
        ('Sumber primer', 'dari masa peristiwa'),
        ('Sumber sekunder', 'ditulis belakangan'),
        ('Kritik ekstern', 'keaslian sumber'),
        ('Kritik intern', 'kredibilitas isi'),
        ('Heuristik', 'mencari sumber'),
        ('Interpretasi', 'menafsirkan fakta'),
        ('Historiografi', 'menulis kisah sejarah'),
        ('Sejarah lisan', 'kesaksian pelaku'),
    ],
    'steps': [
        ('Urutkan tahap penelitian sejarah.', ['Pemilihan topik', 'Heuristik', 'Verifikasi', 'Interpretasi', 'Historiografi'], 'Penelitian bergerak dari topik sampai penulisan.', 'Verifikasi menjaga kejujuran data.'),
        ('Urutkan langkah kritik sumber.', ['Mengumpulkan sumber', 'Memeriksa keaslian fisik', 'Memeriksa kredibilitas isi', 'Membandingkan dengan sumber lain', 'Menetapkan fakta'], 'Kritik berjalan dari fisik ke isi lalu pembandingan.', 'Fakta ditetapkan setelah lolos kritik.'),
        ('Urutkan langkah wawancara sejarah lisan.', ['Menentukan narasumber', 'Menyiapkan daftar pertanyaan', 'Merekam atau mencatat', 'Meminta izin dan mencatat identitas', 'Menuliskan transkrip dan memverifikasi'], 'Wawancara perlu persiapan dan pencatatan yang rapi.', 'Identitas narasumber menjadi bukti.'),
        ('Urutkan langkah proyek sejarah lingkungan.', ['Menetapkan batas topik', 'Mengumpulkan sumber lokal', 'Menguji sumber', 'Menyusun kronologi temuan', 'Mempresentasikan laporan'], 'Proyek berjalan dari batas topik sampai presentasi.', 'Kronologi memudahkan pembaca.'),
        ('Urutkan penyaringan sumber menjadi kisah.', ['Sumber ditemukan', 'Diuji keasliannya', 'Diuji kredibilitasnya', 'Ditafsirkan', 'Ditulis menjadi kisah sejarah'], 'Sumber harus lolos dua kritik sebelum ditafsirkan.', 'Kisah sejarah adalah hasil akhir.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
