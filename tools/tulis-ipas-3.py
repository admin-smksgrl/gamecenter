"""IPAS 3 — Teknologi Pertanian dan Pangan untuk Mengatasi Stunting (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'IPAS 3',
    'slug': 'ipas-3-teknologi-pangan-stunting',
    'title': 'Mengembangkan Teknologi Pertanian dan Pangan untuk Mengatasi Stunting',
    'description': (
        'Mengenali ciri, penyebab, dan dampak stunting, menelaah solusi berbasis '
        'gizi dan pertanian seperti hidroponik, serta merancang projek dan '
        'kampanye anti-stunting di lingkungan sekitar.'
    ),
    'objectives': [
        'Mengidentifikasi bukti ilmiah kasus stunting di Indonesia.',
        'Menjelaskan ciri, penyebab, dan dampak stunting pada anak.',
        'Menyusun alternatif solusi pencegahan stunting berbasis potensi lokal.',
        'Merancang dan membuat purwarupa projek anti-stunting sederhana.',
        'Melakukan kampanye anti-stunting dengan media yang sesuai.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 3 Mengembangkan Teknologi Pertanian dan '
        'Pangan untuk Mengatasi Stunting; CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'Stunting', 'definition': 'Gangguan tumbuh kembang anak yang ditandai tinggi badan lebih pendek daripada anak seusianya.'},
        {'term': 'Gizi esensial', 'definition': 'Zat gizi yang tidak dapat diproduksi tubuh sehingga harus dipenuhi dari makanan.'},
        {'term': 'Prevalensi', 'definition': 'Angka kejadian penyakit atau kondisi pada suatu populasi dalam waktu tertentu.'},
        {'term': 'Hidroponik', 'definition': 'Sistem pertanian yang memakai air sebagai media tanam, tanpa tanah.'},
        {'term': 'Kampanye', 'definition': 'Komunikasi kepada banyak orang untuk memengaruhi pengetahuan, sikap, atau tindakan.'},
        {'term': 'Posyandu', 'definition': 'Pos pelayanan terpadu, struktur terdepan pelayanan kesehatan pemerintah.'},
        {'term': 'Purwarupa', 'definition': 'Gambaran awal produk yang dikembangkan sebelum produksi sebenarnya.'},
        {'term': 'Rubrik', 'definition': 'Daftar kriteria dan ukuran yang dipakai menilai hasil projek.'},
    ],
    'intro': {
        'material_title': 'Mengapa stunting darurat di Indonesia?',
        'title': 'Stunting dan bukti ilmiahnya',
        'paragraphs': [
            'Pada 2021, Indonesia menempati urutan kedua kasus stunting terbanyak di Asia Tenggara dengan prevalensi 24%. Kementerian Kesehatan mencatat satu dari tiga bayi yang dilahirkan mengalami stunting. Pada 2022 angka itu turun menjadi 21,6%.',
            'Standar WHO menetapkan ambang batas prevalensi stunting sebesar 20%. Artinya, pada 2022 masih banyak provinsi Indonesia yang belum memenuhi standar tersebut, bahkan Nusa Tenggara Timur mencapai 35,3%.',
            'Stunting bukan sekadar tubuh pendek. Kekurangan gizi sejak dalam kandungan sampai usia dua tahun mengganggu pertumbuhan fisik, perkembangan kognitif, dan kemampuan motorik anak. Kondisi ini permanen, tetapi dapat dicegah.',
        ],
        'diagram': (
            'Rantai penyebab sampai dampak stunting',
            'flowchart LR\n'
            '  A[Kurang gizi esensial] --> B[Gangguan pertumbuhan]\n'
            '  B --> C[Tubuh lebih pendek dari seusia]\n'
            '  B --> D[Perkembangan kognitif terganggu]\n'
            '  B --> E[Keterlambatan motorik]\n'
            '  C --> F[Prestasi belajar rendah]\n'
            '  D --> F\n'
            '  E --> F',
        ),
        'callout': 'Stunting tidak dapat disembuhkan, tetapi dapat dicegah. Pencegahan paling kuat dilakukan sejak masa kehamilan hingga usia dua tahun.',
        'checkpoint': (
            'Berapa ambang batas prevalensi stunting menurut standar WHO?',
            [
                ('20%', True),
                ('10%', False),
                ('30%', False),
                ('50%', False),
            ],
            'WHO menetapkan ambang 20%; prevalensi di atas angka itu dianggap masalah kesehatan masyarakat.',
        ),
    },
    'concept': {
        'material_title': 'Ciri, penyebab, dan dampak stunting',
        'title': 'Membaca data stunting dan faktor penyebabnya',
        'paragraphs': [
            'Ciri stunting meliputi keterlambatan pertumbuhan, penurunan tingkat kecerdasan, gangguan berbicara, kesulitan belajar, dan daya tahan tubuh rendah sehingga mudah terkena infeksi. Anak yang pendek belum tentu stunting, tetapi tinggi badan yang jauh di bawah anak seusianya perlu diperiksa tenaga kesehatan.',
            'Menurut Ikatan Dokter Anak Indonesia, stunting dipengaruhi faktor lingkungan dan genetik. Faktor lingkungan mencakup gizi ibu selama hamil, pola pemberian makan anak, kebersihan lingkungan, dan angka kejadian infeksi.',
            'Dampaknya berlangsung jangka panjang: prestasi belajar rendah, keterlambatan motorik, sedikit kosakata, serta kurang fokus. Karena itu penanganan harus segera dan melibatkan keluarga, sekolah, posyandu, dan pemerintah.',
        ],
        'table': [
            ['Aspek', 'Uraian', 'Contoh'],
            ['Ciri fisik', 'Tinggi badan jauh di bawah anak seusia', 'Pertumbuhan lambat sejak balita'],
            ['Ciri kognitif', 'Kecerdasan dan kemampuan belajar menurun', 'Kesulitan belajar, kosakata sedikit'],
            ['Penyebab lingkungan', 'Gizi ibu, pola makan, sanitasi, infeksi', 'ASI dan MPASI tidak memadai'],
            ['Penyebab genetik', 'Faktor keturunan orang tua', 'Orang tua bertubuh pendek'],
            ['Dampak', 'Prestasi rendah dan mudah sakit', 'Sering absen karena infeksi'],
        ],
        'visual': chart_block(
            'ipas-3-prevalensi',
            'Lima provinsi dengan prevalensi stunting tertinggi 2022 (%)',
            'bar',
            [('NTT', 35.3), ('Sulawesi Barat', 35.0), ('Papua', 34.6), ('NTB', 32.7), ('Aceh', 31.2)],
        ),
        'activity': categorize_block(
            'ipas-3-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam penyebab, ciri, atau solusi stunting.',
            [('b1', 'Penyebab'), ('b2', 'Ciri atau dampak'), ('b3', 'Solusi')],
            [
                ('i1', 'Gizi ibu kurang selama kehamilan', 'b1'),
                ('i2', 'Pola pemberian makan anak tidak memadai', 'b1'),
                ('i3', 'Kebersihan lingkungan buruk dan infeksi berulang', 'b1'),
                ('i4', 'Tinggi badan jauh di bawah anak seusia', 'b2'),
                ('i5', 'Keterlambatan berbicara dan kurang fokus', 'b2'),
                ('i6', 'Menanam sayuran dengan hidroponik', 'b3'),
                ('i7', 'Memberi bantuan makanan bergizi bagi keluarga miskin', 'b3'),
                ('i8', 'Memantau tumbuh kembang di posyandu', 'b3'),
            ],
            'Tepat. Penyebab berasal dari gizi, pola makan, dan lingkungan; ciri tampak pada tubuh serta kemampuan anak; solusi berupa tindakan pencegahan.',
            'Periksa lagi: hidroponik dan bantuan pangan adalah tindakan, bukan gejala.',
        ),
        'subtitle': 'Solusi berbasis pangan dan teknologi',
        'list': [
            'Memenuhi gizi esensial melalui makanan beragam: karbohidrat, protein, lemak, vitamin, dan mineral.',
            'Memanfaatkan lahan sempit dengan hidroponik berdesain 105 cm × 105 cm dari pipa PVC bertingkat.',
            'Meningkatkan pendapatan keluarga agar mampu mengakses makanan bergizi.',
            'Memantau pertumbuhan anak secara rutin di posyandu dan fasilitas kesehatan terdekat.',
        ],
        'checkpoint': (
            'Mengapa hidroponik dipilih sebagai solusi pencegahan stunting di sekolah?',
            [
                ('Bisa dilakukan di lahan sempit dengan biaya terjangkau', True),
                ('Memerlukan lahan pertanian yang sangat luas', False),
                ('Tidak memerlukan air sama sekali', False),
                ('Hanya dapat dipakai di daerah pegunungan', False),
            ],
            'Hidroponik memungkinkan penanaman sayuran di lahan terbatas dengan bahan murah dan mudah didapat.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Projek anti-stunting dan kampanyenya',
        'paragraphs': [
            'Projek anti-stunting dijalankan melalui lima kegiatan: mendesain purwarupa, membangun purwarupa, mengevaluasi, mendesain ulang berdasarkan hasil evaluasi, dan menyusun rencana tindak lanjut.',
            'Sebelum membangun purwarupa, kelompok melengkapi jadwal waktu, pembagian tugas, prosedur kerja, dan manajemen risiko. Alur kerja projek membantu pelaksanaan berjalan bertahap dan terukur.',
            'Evaluasi memakai rubrik produk, misalnya kerapian, estetika, dan bentuk. Bila hasil belum sesuai, produk diperbaiki. Setelah itu kampanye anti-stunting dilakukan lewat poster, video singkat, atau kunjungan ke rumah warga.',
        ],
        'scenario': scenario(
            'ipas-3-skenario',
            'Kampanye di posyandu',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu menemukan banyak warga belum memahami stunting. Apa langkah pertama?',
                    'choices': [
                        {'text': 'Melakukan survei pemahaman warga', 'next': 'n2', 'score': 2, 'feedback': 'Survei memberi data awal untuk kampanye yang tepat sasaran.'},
                        {'text': 'Langsung mencetak poster tanpa data', 'next': 'n3', 'score': 0, 'feedback': 'Kampanye tanpa data sulit mengukur keberhasilan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Data menunjukkan warga memahami stunting tetapi sulit menyediakan sayur. Apa solusinya?',
                    'choices': [
                        {'text': 'Membuat hidroponik sederhana di pekarangan', 'next': 'n4', 'score': 2, 'feedback': 'Solusi ini murah dan langsung menambah ketersediaan sayur.'},
                        {'text': 'Hanya menambah poster di balai desa', 'next': 'n3', 'score': 0, 'feedback': 'Poster tidak mengatasi akar masalah ketersediaan pangan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Kampanye berjalan tanpa perubahan perilaku yang terukur.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Warga menanam sayur sendiri dan kebutuhan gizi anak membaik.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu stunting?', 'back': 'Gangguan tumbuh kembang dengan tinggi badan lebih pendek dari anak seusianya.'},
            {'front': 'Berapa prevalensi stunting Indonesia 2022?', 'back': '21,6%.'},
            {'front': 'Apa media tanam hidroponik?', 'back': 'Air, bukan tanah.'},
            {'front': 'Di mana pemantauan tumbuh kembang dilakukan?', 'back': 'Posyandu dan fasilitas kesehatan terdekat.'},
        ],
        'checkpoint': (
            'Dokumen berisi kriteria penilaian produk projek disebut…',
            [
                ('rubrik', True),
                ('proposal', False),
                ('jadwal waktu', False),
                ('laporan keuangan', False),
            ],
            'Rubrik memuat kriteria yang dipakai menilai kesesuaian produk dengan standar projek.',
        ),
        'challenge': challenge_block(
            'ipas-3-tantangan',
            'Tantangan istilah stunting',
            90,
            [
                ('Angka kejadian pada populasi', 'Prevalensi'),
                ('Bercocok tanam memakai air', 'Hidroponik'),
                ('Ambang batas WHO', '20%'),
                ('Provinsi prevalensi tertinggi 2022', 'NTT'),
                ('Kegiatan memengaruhi banyak orang', 'Kampanye'),
            ],
            'Lima istilah stunting terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Berapa prevalensi stunting Indonesia pada 2021?', '24%', ['14%', '34%', '44%'], 'Pada 2021 prevalensi stunting Indonesia 24%, kedua tertinggi di Asia Tenggara.', 'Angka ini turun pada 2022.'),
        ('Berapa prevalensi stunting Indonesia pada 2022?', '21,6%', ['11,6%', '31,6%', '25%'], 'Pada 2022 prevalensi turun menjadi 21,6%.', 'Masih di atas ambang WHO.'),
        ('Apa ambang batas prevalensi stunting menurut WHO?', '20%', ['10%', '25%', '30%'], 'WHO memakai ambang 20% sebagai batas masalah kesehatan masyarakat.', 'Sedikit di bawah angka nasional 2022.'),
        ('Provinsi dengan prevalensi stunting tertinggi pada 2022 adalah…', 'Nusa Tenggara Timur', ['Bali', 'DKI Jakarta', 'DI Yogyakarta'], 'NTT memiliki prevalensi 35,3% pada 2022.', 'Provinsi dengan angka terendah justru Bali.'),
        ('Apa yang dimaksud stunting?', 'gangguan tumbuh kembang dengan tinggi badan lebih pendek dari anak seusia', ['kegemukan pada anak', 'penyakit kulit menular', 'kekurangan vitamin A saja'], 'Stunting ditandai tinggi badan lebih pendek daripada anak seusianya.', 'Bukan sekadar tubuh pendek karena keturunan.'),
        ('Apakah stunting dapat disembuhkan?', 'tidak, tetapi dapat dicegah', ['ya, dengan obat khusus', 'ya, dengan operasi', 'tidak dapat dicegah'], 'Stunting bersifat permanen, namun pencegahannya dapat dilakukan.', 'Pencegahan paling kuat sejak kehamilan.'),
        ('Menurut IDAI, stunting dipengaruhi faktor…', 'lingkungan dan genetik', ['cuaca dan musim', 'ekonomi negara lain', 'teknologi digital'], 'IDAI menyebut faktor lingkungan dan genetik sebagai penyebab stunting.', 'Faktor lingkungan mencakup gizi dan sanitasi.'),
        ('Manakah yang termasuk faktor lingkungan penyebab stunting?', 'gizi ibu selama hamil', ['jumlah anggota keluarga', 'warna rumah', 'jenis pekerjaan ayah'], 'Gizi ibu hamil, pola makan anak, kebersihan, dan infeksi termasuk faktor lingkungan.', 'Berhubungan langsung dengan asupan gizi anak.'),
        ('Apa media tanam pada hidroponik?', 'air', ['tanah liat', 'pasir pantai', 'arang kayu'], 'Hidroponik memakai air sebagai media tanam.', 'Cocok untuk lahan sempit.'),
        ('Berapa ukuran desain hidroponik pada buku?', '105 cm × 105 cm', ['50 cm × 50 cm', '200 cm × 200 cm', '150 cm × 300 cm'], 'Desain hidroponik berukuran 105 cm × 105 cm agar mudah ditempatkan di lahan sempit.', 'Ukurannya persegi.'),
        ('Bahan pipa pada desain hidroponik buku adalah…', 'PVC', ['besi', 'kaca', 'kayu jati'], 'Hidroponik buku memakai pipa PVC yang tahan lama dan disusun bertingkat.', 'Bahan ini ringan dan tahan air.'),
        ('Kegiatan komunikasi untuk memengaruhi banyak orang disebut…', 'kampanye', ['survei', 'observasi', 'wawancara'], 'Kampanye bertujuan memengaruhi pengetahuan dan tindakan banyak orang.', 'Contohnya kampanye anti-stunting.'),
        ('Alat untuk menilai hasil produk projek disebut…', 'rubrik', ['proposal', 'notulen', 'kwitansi'], 'Rubrik memuat kriteria penilaian produk.', 'Dipakai pada tahap evaluasi.'),
        ('Layanan kesehatan terdepan milik pemerintah untuk memantau balita adalah…', 'posyandu', ['puskesmas rawat inap', 'rumah sakit umum', 'apotek'], 'Posyandu menjadi struktur terkecil dan terdepan pelayanan kesehatan.', 'Tempat penimbangan dan imunisasi balita.'),
    ],
    'multi': [
        ('Manakah ciri anak mengalami stunting?', ['Keterlambatan pertumbuhan', 'Daya tahan tubuh rendah', 'Kesulitan belajar'], ['Penglihatan tajam', 'Pendengaran berlebih'], 'Stunting memengaruhi pertumbuhan, imunitas, dan kemampuan belajar.', 'Ciri utamanya tampak pada pertumbuhan dan perkembangan.'),
        ('Manakah termasuk penyebab stunting?', ['Gizi ibu selama hamil kurang', 'Pola pemberian makan tidak memadai', 'Kebersihan lingkungan buruk'], ['Olahraga berlebihan', 'Tidur siang terlalu lama'], 'Asupan gizi dan sanitasi berperan besar terhadap stunting.', 'Penyebab utama berkaitan dengan gizi dan infeksi.'),
        ('Manakah solusi pencegahan stunting?', ['Menanam sayur dengan hidroponik', 'Bantuan makanan bergizi', 'Pemantauan di posyandu'], ['Menghindari sayuran', 'Mengurangi kunjungan kesehatan'], 'Solusi stunting meningkatkan akses dan kualitas gizi anak.', 'Semua menambah asupan atau pemantauan gizi.'),
        ('Manakah dampak stunting di masa depan?', ['Prestasi belajar rendah', 'Keterlambatan motorik', 'Kosakata sedikit'], ['Penglihatan bertambah tajam', 'Tinggi badan bertambah cepat'], 'Stunting menurunkan capaian belajar dan perkembangan motorik.', 'Dampaknya berlangsung jangka panjang.'),
        ('Manakah tahap projek anti-stunting menurut buku?', ['Mendesain purwarupa', 'Membangun purwarupa', 'Mengevaluasi purwarupa'], ['Menghapus laporan', 'Menghentikan kampanye'], 'Projek dijalankan berurutan dari desain sampai evaluasi dan tindak lanjut.', 'Evaluasi menentukan perbaikan berikutnya.'),
        ('Manakah media kampanye anti-stunting?', ['Poster', 'Video singkat', 'Kunjungan ke rumah'], ['Rapat internal sekolah', 'Surat pribadi'], 'Kampanye memakai media yang menjangkau banyak warga.', 'Kunjungan langsung juga termasuk kampanye.'),
        ('Manakah yang termasuk gizi esensial?', ['Karbohidrat', 'Protein', 'Vitamin dan mineral'], ['Pewarna buatan', 'Pengawet makanan'], 'Gizi esensial harus dipenuhi dari makanan sehari-hari.', 'Tubuh tidak dapat memproduksinya sendiri.'),
        ('Manakah kegiatan evaluasi produk projek?', ['Menilai kesesuaian dengan rubrik', 'Mendata kriteria yang belum tercapai', 'Merencanakan perbaikan produk'], ['Membuang catatan projek', 'Menghindari umpan balik guru'], 'Evaluasi membandingkan hasil dengan kriteria lalu menyusun perbaikan.', 'Perbaikan mengikuti temuan evaluasi.'),
    ],
    'pairs': [
        ('Stunting', 'tinggi badan lebih pendek dari anak seusia'),
        ('Prevalensi', 'angka kejadian pada suatu populasi'),
        ('Gizi esensial', 'zat gizi yang tak dapat diproduksi tubuh'),
        ('Hidroponik', 'bertanam memakai air tanpa tanah'),
        ('Posyandu', 'layanan kesehatan terdepan untuk balita'),
        ('Kampanye', 'komunikasi untuk memengaruhi banyak orang'),
        ('Rubrik', 'kriteria penilaian hasil projek'),
        ('Purwarupa', 'gambaran awal produk yang dikembangkan'),
    ],
    'steps': [
        ('Urutkan tahap projek anti-stunting menurut buku.', ['Mendesain purwarupa', 'Membangun purwarupa', 'Mengevaluasi purwarupa', 'Menyusun rencana tindak lanjut'], 'Projek bergerak dari desain, pembangunan, evaluasi, sampai tindak lanjut.', 'Tindak lanjut disusun setelah evaluasi.'),
        ('Urutkan langkah menyusun projek baru.', ['Menentukan konsep atau ide', 'Membentuk tim', 'Membuat rancangan desain', 'Menyusun rencana produksi', 'Mendokumentasikan'], 'Alur kerja projek dimulai dari ide, tim, desain, rencana produksi, lalu dokumentasi.', 'Tim dibentuk sebelum desain dibuat.'),
        ('Urutkan langkah kampanye anti-stunting.', ['Mensurvei pemahaman warga', 'Menentukan pesan kampanye', 'Memilih media kampanye', 'Melaksanakan kampanye', 'Menilai perubahan pemahaman'], 'Kampanye dimulai dari data warga sampai penilaian hasil.', 'Tanpa survei awal, hasil kampanye sulit diukur.'),
        ('Urutkan langkah menanam sayur hidroponik sederhana.', ['Menyiapkan pipa dan pompa', 'Menyemai benih', 'Memindahkan bibit ke instalasi', 'Menambahkan nutrisi', 'Memanen sayuran'], 'Hidroponik dimulai dari instalasi, penyemaian, pemindahan, pemberian nutrisi, lalu panen.', 'Nutrisi diberikan setelah bibit tumbuh.'),
        ('Urutkan langkah evaluasi sampai perbaikan produk.', ['Menetapkan kriteria rubrik', 'Menilai produk', 'Mendata kriteria yang belum tercapai', 'Mendesain ulang produk'], 'Evaluasi memakai rubrik, lalu perbaikan diarahkan pada kriteria yang gagal.', 'Desain ulang mengikuti temuan penilaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
