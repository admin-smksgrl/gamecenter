"""PRA 2 — Produk Aksesoris Interior Nusantara (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 2',
    'slug': 'prakarya-2-aksesoris-interior',
    'title': 'Produk Aksesoris Interior Nusantara',
    'description': (
        'Mengenal aksesoris interior Nusantara, bahan lokal, teknik makrame, '
        'tanah liat, dan anyaman, serta merancang produk yang ergonomis.'
    ),
    'objectives': [
        'Mengeksplorasi bentuk, bahan, alat, dan teknik aksesoris interior Nusantara.',
        'Menganalisis potensi nilai ekonomis produk aksesoris interior berbasis sumber daya lokal.',
        'Merancang aksesoris interior dengan pertimbangan ergonomi dan keselamatan.',
        'Membuat produk aksesoris interior yang fungsional dan estetis.',
        'Mempresentasikan serta mengevaluasi produk dan rencana tindak lanjut.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Kerajinan-BG-KLS-X.pdf Unit 2 Produk Aksesoris Interior Nusantara',
    'glossary': [
        {'term': 'Aksesoris interior', 'definition': 'Benda penghias dan pelengkap ruangan di dalam rumah.'},
        {'term': 'Makrame', 'definition': 'Teknik membuat kerajinan dengan simpul tali tanpa alat tenun.'},
        {'term': 'Tanah liat', 'definition': 'Bahan alami yang dapat dibentuk dan dibakar menjadi keramik.'},
        {'term': 'Teknik pilin', 'definition': 'Membentuk tanah liat dengan menggulungnya memanjang seperti tali.'},
        {'term': 'Teknik lempeng', 'definition': 'Membentuk tanah liat menjadi lembaran tipis yang rata.'},
        {'term': 'Anyaman', 'definition': 'Teknik menyilangkan bahan pipih seperti bambu atau rotan.'},
        {'term': 'Finishing', 'definition': 'Tahap akhir pelapisan produk agar rapi, kuat, dan menarik.'},
        {'term': 'Terakota', 'definition': 'Warna merah kecokelatan khas tanah liat setelah dibakar.'},
    ],
    'intro': {
        'material_title': 'Mengapa aksesoris interior menarik?',
        'title': 'Menghias ruang dengan kearifan lokal',
        'paragraphs': [
            'Aksesoris interior adalah benda yang memperindah dan melengkapi ruangan di dalam rumah. Contohnya hiasan dinding, vas, kap lampu, cermin hias, bantal, dan taplak meja. Benda-benda ini membuat ruangan terasa lebih hangat dan personal.',
            'Nusantara memiliki bahan lokal yang kaya untuk aksesoris interior, seperti bambu, rotan, tanah liat, kayu, dan kain. Setiap daerah mengembangkan teknik dan motif yang khas, sehingga produknya tidak mudah disamakan dengan daerah lain.',
            'Membuat aksesoris interior melatih kreativitas, ketelitian, dan jiwa wirausaha. Produk yang dirancang baik dapat mempercantik ruangan sekaligus menjadi sumber penghasilan.',
        ],
        'diagram': (
            'Alur proyek aksesoris interior',
            'flowchart LR\n'
            '  A[Observasi kebutuhan ruang] --> B[Pemilihan bahan lokal]\n'
            '  B --> C[Perancangan produk]\n'
            '  C --> D[Pembuatan]\n'
            '  D --> E[Finishing]\n'
            '  E --> F[Presentasi dan evaluasi]',
        ),
        'callout': 'Saat membentuk tanah liat atau memotong bambu, gunakan alas kerja dan sarung tangan agar tangan tetap aman.',
        'checkpoint': (
            'Apa yang dimaksud aksesoris interior?',
            [
                ('Benda penghias ruangan di dalam rumah', True),
                ('Benda penghias taman', False),
                ('Alat memasak', False),
                ('Pakaian yang dipakai di tubuh', False),
            ],
            'Aksesoris interior memperindah dan melengkapi ruangan di dalam rumah.',
        ),
    },
    'concept': {
        'material_title': 'Bahan dan teknik aksesoris interior',
        'title': 'Makrame, tanah liat, dan anyaman',
        'paragraphs': [
            'Makrame dibuat dengan menyimpul tali atau benang. Teknik ini tidak memerlukan alat tenun dan cocok untuk hiasan dinding, kap lampu, serta gantungan pot. Kekuatan simpul menentukan kerapian dan daya tahan produk.',
            'Tanah liat dibentuk dengan tiga teknik utama: pilin, lempeng, dan putar. Teknik pilin menggulung tanah liat memanjang, teknik lempeng membentuk lembaran, sedangkan teknik putar memakai roda putar untuk membuat bentuk bulat simetris.',
            'Anyaman memakai bahan pipih seperti bambu dan rotan yang disilangkan. Produk anyaman dapat berupa keranjang, tempat tisu, atau kap lampu. Setelah dibentuk, produk diberi finishing agar kuat, rapi, dan tahan lama.',
        ],
        'table': [
            ['Teknik', 'Bahan', 'Kunci gerak'],
            ['Makrame', 'Tali atau benang', 'Simpul kuat dan seragam'],
            ['Pilin', 'Tanah liat', 'Gulung memanjang, sambung rapi'],
            ['Lempeng', 'Tanah liat', 'Ratakan ketebalan lembaran'],
            ['Anyaman', 'Bambu atau rotan', 'Silang teratur, jaga kerapatan'],
            ['Finishing', 'Cat, pelitur, atau pelapis', 'Bersihkan permukaan sebelum melapisi'],
        ],
        'visual': chart_block(
            'pra-2-waktu-kering',
            'Perkiraan waktu pengeringan bahan (jam)',
            'bar',
            [('Lem', 2), ('Cat', 6), ('Finishing kayu', 12), ('Tanah liat', 24)],
        ),
        'activity': categorize_block(
            'pra-2-klasifikasi',
            'Kelompokkan bahan berikut ke dalam bahan alami atau bahan olahan.',
            [('b1', 'Bahan alami'), ('b2', 'Bahan olahan')],
            [
                ('i1', 'Bambu', 'b1'),
                ('i2', 'Rotan', 'b1'),
                ('i3', 'Tanah liat', 'b1'),
                ('i4', 'Kawat', 'b2'),
                ('i5', 'Benang', 'b2'),
                ('i6', 'Cat', 'b2'),
            ],
            'Tepat. Bambu, rotan, dan tanah liat adalah bahan alami; kawat, benang, dan cat adalah bahan olahan.',
            'Periksa lagi: bahan alami berasal langsung dari alam.',
        ),
        'subtitle': 'Ergonomi dan keselamatan kerja',
        'list': [
            'Letakkan aksesoris pada tempat yang tidak menghalangi jalan dan tidak mudah terjatuh.',
            'Hindari sudut tajam pada produk yang dijangkau anak-anak.',
            'Gunakan masker saat mengampelas atau mencampur bahan kimia.',
            'Pastikan ruang kerja memiliki ventilasi yang baik saat memakai cat atau pelitur.',
        ],
        'checkpoint': (
            'Teknik membentuk tanah liat dengan menggulung memanjang disebut…',
            [
                ('Pilin', True),
                ('Lempeng', False),
                ('Putar', False),
                ('Anyam', False),
            ],
            'Teknik pilin membentuk tanah liat dengan menggulungnya memanjang seperti tali.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat hiasan interior yang fungsional',
        'paragraphs': [
            'Amati ruangan di sekitarmu. Cari sudut yang terasa kosong atau kurang menarik, lalu tentukan apakah ruangan itu membutuhkan hiasan dinding, vas, atau tempat penyimpanan kecil.',
            'Pilih bahan yang tersedia di daerahmu. Jika memakai tanah liat, pastikan tanah cukup lembap dan bebas kerikil. Jika memakai bambu, keringkan terlebih dahulu agar tidak mudah berjamur.',
            'Buat satu produk sederhana, lalu uji kekuatannya. Gantung hiasan dinding dengan aman, letakkan vas di permukaan datar, dan pastikan kap lampu tidak bersentuhan langsung dengan bola lampu panas.',
        ],
        'scenario': scenario(
            'pra-2-skenario',
            'Menghias sudut baca',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Sudut baca sekolah terlihat kosong dan kurang nyaman. Produk apa yang paling tepat dibuat?',
                    'choices': [
                        {'text': 'Hiasan dinding dan tempat buku dari bahan lokal', 'next': 'n2', 'score': 2, 'feedback': 'Produk dipilih sesuai kebutuhan ruang.'},
                        {'text': 'Lampu taman besar', 'next': 'n3', 'score': 0, 'feedback': 'Lampu taman tidak sesuai untuk ruang dalam.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bahan bambu yang tersedia masih basah. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Mengeringkan bambu sebelum dipakai', 'next': 'n4', 'score': 2, 'feedback': 'Bambu kering lebih kuat dan tidak mudah berjamur.'},
                        {'text': 'Langsung memakainya agar cepat selesai', 'next': 'n3', 'score': 0, 'feedback': 'Bambu basah mudah berjamur dan berubah bentuk.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk cepat rusak karena bahan belum siap.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk awet dan sudut baca menjadi nyaman.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu makrame?', 'back': 'Teknik membuat kerajinan dengan simpul tali.'},
            {'front': 'Sebutkan tiga teknik tanah liat.', 'back': 'Pilin, lempeng, dan putar.'},
            {'front': 'Apa itu finishing?', 'back': 'Tahap akhir pelapisan produk agar rapi dan tahan lama.'},
            {'front': 'Apa warna khas tanah liat setelah dibakar?', 'back': 'Terakota, yaitu merah kecokelatan.'},
        ],
        'checkpoint': (
            'Agar kap lampu buatan sendiri aman digunakan, hal yang perlu diperhatikan adalah…',
            [
                ('Jarak dari bola lampu panas', True),
                ('Warna kap lampu', False),
                ('Jumlah simpul saja', False),
                ('Berat cat', False),
            ],
            'Kap lampu harus menjaga jarak dari bola lampu agar tidak terbakar.',
        ),
        'challenge': challenge_block(
            'pra-2-tantangan',
            'Tantangan istilah aksesoris interior',
            90,
            [
                ('Teknik simpul tali', 'makrame'),
                ('Bahan keramik alami', 'tanah liat'),
                ('Teknik membentuk lembaran', 'lempeng'),
                ('Warna khas tanah liat bakar', 'terakota'),
                ('Tahap akhir produk', 'finishing'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa yang dimaksud aksesoris interior?', 'Benda penghias ruangan di dalam rumah', ['Benda penghias taman', 'Alat memasak', 'Pakaian olahraga'], 'Aksesoris interior memperindah dan melengkapi ruangan dalam rumah.', 'Contohnya vas dan hiasan dinding.'),
        ('Manakah contoh aksesoris interior?', 'Vas bunga', ['Lampu taman', 'Pot pagar', 'Sepatu'], 'Vas bunga dipakai di dalam ruangan.', 'Lampu taman dan pot pagar untuk eksterior.'),
        ('Apa nama teknik kerajinan dengan simpul tali?', 'Makrame', ['Anyaman', 'Pilin', 'Lempeng'], 'Makrame dibuat dengan menyimpul tali atau benang.', 'Teknik ini tidak memerlukan alat tenun.'),
        ('Bahan utama makrame adalah…', 'Tali atau benang', ['Tanah liat', 'Bambu', 'Batu'], 'Makrame memakai tali atau benang yang disimpul.', 'Pilih tali yang kuat dan lentur.'),
        ('Apa nama teknik membentuk tanah liat dengan menggulung memanjang?', 'Pilin', ['Lempeng', 'Putar', 'Anyam'], 'Teknik pilin menggulung tanah liat memanjang seperti tali.', 'Gulungan disambung hingga membentuk benda.'),
        ('Apa nama teknik membentuk tanah liat menjadi lembaran?', 'Lempeng', ['Pilin', 'Putar', 'Anyam'], 'Teknik lempeng membentuk tanah liat menjadi lembaran tipis.', 'Lembaran dipotong dan disambung sesuai pola.'),
        ('Apa nama teknik membentuk tanah liat dengan roda putar?', 'Putar', ['Pilin', 'Lempeng', 'Anyam'], 'Teknik putar memakai roda putar untuk bentuk bulat simetris.', 'Cocok untuk vas dan mangkuk.'),
        ('Apa nama teknik menyilangkan bambu atau rotan?', 'Anyaman', ['Makrame', 'Pilin', 'Lempeng'], 'Anyaman menyilangkan bahan pipih secara teratur.', 'Kerapatan anyaman menentukan kekuatan.'),
        ('Apa warna khas tanah liat setelah dibakar?', 'Terakota', ['Biru', 'Hijau', 'Putih'], 'Tanah liat yang dibakar menghasilkan warna terakota.', 'Warnanya merah kecokelatan.'),
        ('Apa fungsi finishing pada produk kerajinan?', 'Melapisi agar rapi dan tahan lama', ['Menambah berat produk', 'Menghilangkan bentuk', 'Mengganti bahan'], 'Finishing melindungi permukaan dan mempercantik produk.', 'Permukaan dibersihkan sebelum dilapisi.'),
        ('Mengapa produk anyaman perlu dikeringkan sebelum dipakai?', 'Agar tidak mudah berjamur', ['Agar warnanya hilang', 'Agar lebih berat', 'Agar mudah pecah'], 'Bahan yang lembap mudah berjamur dan berubah bentuk.', 'Pengeringan menjaga kekuatan produk.'),
        ('Apa yang dimaksud ergonomi pada aksesoris interior?', 'Menyesuaikan produk dengan kenyamanan dan keamanan ruang', ['Membuat produk sebesar mungkin', 'Memakai warna paling terang', 'Menambah sudut tajam'], 'Ergonomi membuat produk aman dan nyaman digunakan di ruang.', 'Hindari sudut tajam dan penghalang jalan.'),
        ('Apa yang memengaruhi nilai ekonomis aksesoris interior?', 'Keunikan desain dan kualitas produk', ['Jumlah bahan yang terbuang', 'Kerapian yang diabaikan', 'Kemasan rusak'], 'Desain unik dan kualitas membuat produk bernilai lebih tinggi.', 'Kemasan juga mendukung pemasaran.'),
        ('Apa langkah pertama dalam proyek aksesoris interior?', 'Observasi kebutuhan ruang', ['Langsung mengecat', 'Menjual produk', 'Membuang bahan'], 'Proyek dimulai dari mengamati kebutuhan ruang.', 'Kebutuhan menentukan bentuk dan fungsi produk.'),
    ],
    'multi': [
        ('Manakah yang termasuk aksesoris interior?', ['Hiasan dinding', 'Vas', 'Kap lampu'], ['Lampu taman', 'Pot pagar'], 'Hiasan dinding, vas, dan kap lampu dipakai di dalam ruangan.', 'Lampu taman dan pot pagar untuk luar ruangan.'),
        ('Manakah yang termasuk bahan alami?', ['Bambu', 'Rotan', 'Tanah liat'], ['Kawat', 'Cat'], 'Bambu, rotan, dan tanah liat berasal langsung dari alam.', 'Kawat dan cat adalah bahan olahan.'),
        ('Manakah yang termasuk teknik tanah liat?', ['Pilin', 'Lempeng', 'Putar'], ['Makrame', 'Anyaman'], 'Pilin, lempeng, dan putar adalah teknik membentuk tanah liat.', 'Makrame dan anyaman memakai bahan lain.'),
        ('Apa fungsi aksesoris interior?', ['Memperindah ruangan', 'Melengkapi fungsi ruang'], ['Menghalangi jalan', 'Membuat ruangan gelap'], 'Aksesoris interior memperindah dan melengkapi ruangan.', 'Penempatan harus aman.'),
        ('Manakah prinsip keselamatan kerja?', ['Memakai sarung tangan', 'Memastikan ventilasi baik'], ['Bekerja tanpa alas', 'Menghirup cat tanpa masker'], 'Sarung tangan dan ventilasi baik menjaga keselamatan.', 'Masker dipakai saat mengampelas atau mengecat.'),
        ('Manakah yang termasuk finishing?', ['Cat', 'Pelitur'], ['Tanah liat', 'Bambu'], 'Cat dan pelitur dipakai pada tahap finishing.', 'Tanah liat dan bambu adalah bahan dasar.'),
        ('Manakah ciri produk aksesoris interior berkualitas?', ['Simpul kuat', 'Permukaan rapi'], ['Sudut tajam', 'Bahan mudah lapuk'], 'Simpul kuat dan permukaan rapi menandakan kualitas.', 'Keselamatan juga bagian dari kualitas.'),
        ('Manakah tahap proyek aksesoris interior?', ['Perancangan', 'Pembuatan', 'Evaluasi'], ['Menghindari presentasi', 'Membuang sisa bahan sembarangan'], 'Proyek melalui perancangan, pembuatan, dan evaluasi.', 'Presentasi membantu mendapat masukan.'),
    ],
    'pairs': [
        ('Aksesoris interior', 'benda penghias ruangan dalam rumah'),
        ('Makrame', 'kerajinan simpul tali'),
        ('Pilin', 'menggulung tanah liat memanjang'),
        ('Lempeng', 'membentuk tanah liat menjadi lembaran'),
        ('Anyaman', 'menyilangkan bambu atau rotan'),
        ('Finishing', 'tahap akhir pelapisan produk'),
        ('Terakota', 'warna merah kecokelatan tanah liat bakar'),
        ('Ergonomi', 'menyesuaikan produk dengan kenyamanan pemakai'),
    ],
    'steps': [
        ('Urutkan alur proyek aksesoris interior.', ['Observasi kebutuhan ruang', 'Pemilihan bahan', 'Perancangan produk', 'Pembuatan', 'Finishing dan evaluasi'], 'Proyek bergerak dari observasi menuju finishing dan evaluasi.', 'Kebutuhan ruang menentukan rancangan.'),
        ('Urutkan langkah membuat makrame sederhana.', ['Siapkan tali dan pengait', 'Tentukan panjang tali', 'Buat simpul dasar', 'Rapikan dan potong ujung tali'], 'Makrame dimulai dari penyiapan tali lalu pembuatan simpul.', 'Simpul harus seragam agar rapi.'),
        ('Urutkan langkah membuat vas dengan teknik pilin.', ['Siapkan tanah liat lembap', 'Gulung tanah liat memanjang', 'Susun gulungan membentuk vas', 'Haluskan sambungan', 'Keringkan dan bakar'], 'Vas pilin dibuat dari gulungan yang disusun bertingkat.', 'Sambungan harus dihaluskan agar kuat.'),
        ('Urutkan langkah menganyam bambu.', ['Siapkan bilah bambu', 'Susun bilah secara menyilang', 'Rapatkan anyaman', 'Potong dan rapikan tepi'], 'Menganyam dimulai dari penyiapan bilah lalu penyusunan silang.', 'Kerapatan anyaman menentukan kekuatan.'),
        ('Urutkan langkah finishing produk kayu.', ['Ampelas permukaan', 'Bersihkan debu', 'Lapisi cat atau pelitur', 'Keringkan di tempat berventilasi'], 'Finishing kayu dimulai dari pengampelasan lalu pelapisan.', 'Permukaan bersih membuat lapisan menempel rata.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
