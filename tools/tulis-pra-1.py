"""PRA 1 — Ragam Hias Nusantara pada Produk Fesyen (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 1',
    'slug': 'prakarya-1-ragam-hias-fesyen',
    'title': 'Ragam Hias Nusantara pada Produk Fesyen',
    'description': (
        'Mengeksplorasi motif ragam hias Nusantara, teknik sulam dan aplikasi, '
        'serta merancang produk fesyen yang ergonomis dan bernilai ekonomis.'
    ),
    'objectives': [
        'Mengeksplorasi bentuk, bahan, alat, dan teknik ragam hias Nusantara pada produk fesyen.',
        'Menganalisis potensi nilai ekonomis produk kerajinan fesyen berbasis sumber daya Nusantara.',
        'Merancang produk fesyen dengan modifikasi bentuk, bahan, alat, dan teknik secara ergonomis.',
        'Membuat produk kerajinan fesyen yang ergonomis dan layak dipakai.',
        'Mempresentasikan serta mengevaluasi produk dan rencana tindak lanjut.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Kerajinan-BG-KLS-X.pdf Unit 1 Ragam Hias Nusantara pada Produk Fesyen',
    'glossary': [
        {'term': 'Ragam hias', 'definition': 'Motif atau corak hias yang diterapkan pada benda untuk menambah nilai keindahan.'},
        {'term': 'Motif flora', 'definition': 'Ragam hias yang meniru bentuk tumbuhan seperti daun, bunga, dan sulur.'},
        {'term': 'Motif fauna', 'definition': 'Ragam hias yang meniru bentuk hewan seperti burung, ikan, dan kupu-kupu.'},
        {'term': 'Motif geometris', 'definition': 'Ragam hias yang dibentuk dari garis, lingkaran, segitiga, atau pola berulang.'},
        {'term': 'Sulam', 'definition': 'Teknik menghias kain dengan benang dan jarum mengikuti pola tertentu.'},
        {'term': 'Aplikasi', 'definition': 'Teknik menempelkan potongan kain lain pada kain utama lalu dijahit.'},
        {'term': 'Ergonomi', 'definition': 'Prinsip menyesuaikan produk dengan tubuh dan kenyamanan pemakainya.'},
        {'term': 'Presentasi', 'definition': 'Kegiatan memaparkan produk dan proses pembuatannya kepada orang lain.'},
    ],
    'intro': {
        'material_title': 'Mengapa ragam hias penting?',
        'title': 'Budaya Nusantara pada produk fesyen',
        'paragraphs': [
            'Prakarya kerajinan adalah kegiatan membuat produk yang berguna sekaligus indah. Salah satu cabangnya adalah kerajinan fesyen, yaitu busana dan aksesori yang dipakai di tubuh. Produk fesyen Nusantara kaya akan ragam hias yang diwarisi dari generasi ke generasi.',
            'Ragam hias Nusantara tidak hanya berfungsi mempercantik benda. Setiap motif sering membawa makna, misalnya harapan kesuburan, keberanian, atau penghormatan kepada alam. Motif flora, fauna, geometris, dan figuratif muncul pada kain batik, tenun, songket, dan ukiran.',
            'Mempelajari ragam hias melatih kreativitas dan kepedulian terhadap budaya lokal. Dengan rancangan yang tepat, produk fesyen tradisional dapat menjadi produk bernilai ekonomi tanpa kehilangan jati dirinya.',
        ],
        'diagram': (
            'Alur proyek kerajinan fesyen',
            'flowchart LR\n'
            '  A[Observasi gagasan] --> B[Analisis nilai ekonomis]\n'
            '  B --> C[Perancangan desain]\n'
            '  C --> D[Pembuatan produk]\n'
            '  D --> E[Presentasi dan evaluasi]\n'
            '  E --> F[Rencana tindak lanjut]',
        ),
        'callout': 'Gunakan gunting, jarum, dan alat panas dengan hati-hati. Simpan alat tajam setelah digunakan agar aman.',
        'checkpoint': (
            'Apa yang dimaksud ragam hias?',
            [
                ('Motif atau corak hias pada benda', True),
                ('Bahan dasar pembuat kain', False),
                ('Alat untuk memotong kain', False),
                ('Tempat menjual produk', False),
            ],
            'Ragam hias adalah motif atau corak hias yang diterapkan pada benda.',
        ),
    },
    'concept': {
        'material_title': 'Motif, bahan, dan teknik',
        'title': 'Mengenal ragam hias dan tekniknya',
        'paragraphs': [
            'Motif ragam hias Nusantara dapat dikelompokkan menjadi empat: flora, fauna, geometris, dan figuratif. Motif flora meniru daun dan bunga, fauna meniru hewan, geometris memakai bentuk beraturan, sedangkan figuratif meniru bentuk manusia.',
            'Teknik penerapan ragam hias pada kain cukup beragam. Sulam memakai benang dan jarum, aplikasi menempelkan kain lain, lukis tekstil memakai cat khusus kain, dan manik-manik ditempel atau dijahit mengikuti pola.',
            'Bahan yang dipakai harus sesuai dengan fungsi produk. Kain tenun, batik, dan songket cocok untuk busana; logam tipis, kawat, kulit, dan batuan alam cocok untuk aksesori. Prinsip ergonomi memastikan produk nyaman, aman, dan sesuai ukuran pemakai.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Sulam', 'Menambah hiasan pada kain', 'Pola jelas, tusukan rapi, benang tidak kusut'],
            ['Aplikasi', 'Menempel motif dari kain lain', 'Pola dipotong rapi, jahit tepi kuat'],
            ['Lukis tekstil', 'Mewarnai motif pada kain', 'Gunakan cat kain, kunci warna dengan panas'],
            ['Manik-manik', 'Memberi kilau dan tekstur', 'Susun sesuai pola, jahit atau lem kuat'],
        ],
        'visual': chart_block(
            'pra-1-waktu-teknik',
            'Perkiraan waktu pengerjaan tiap teknik (menit)',
            'bar',
            [('Lukis tekstil', 60), ('Aplikasi', 90), ('Sulam', 120), ('Manik-manik', 150)],
        ),
        'activity': categorize_block(
            'pra-1-klasifikasi',
            'Kelompokkan istilah berikut ke dalam motif atau teknik ragam hias.',
            [('b1', 'Motif'), ('b2', 'Teknik')],
            [
                ('i1', 'Flora', 'b1'),
                ('i2', 'Fauna', 'b1'),
                ('i3', 'Geometris', 'b1'),
                ('i4', 'Sulam', 'b2'),
                ('i5', 'Aplikasi', 'b2'),
                ('i6', 'Lukis tekstil', 'b2'),
            ],
            'Tepat. Flora, fauna, dan geometris adalah motif; sulam, aplikasi, dan lukis tekstil adalah teknik.',
            'Periksa lagi: motif adalah bentuk hiasan, teknik adalah cara mengerjakannya.',
        ),
        'subtitle': 'Prinsip ergonomi dan nilai ekonomis',
        'list': [
            'Produk harus nyaman dipakai: tidak menusuk kulit, tidak terlalu berat, dan ukurannya sesuai.',
            'Keunikan motif lokal meningkatkan daya tarik dan nilai jual produk.',
            'Kualitas jahitan dan kerapian finishing memengaruhi kepuasan pembeli.',
            'Kemasan dan foto produk yang baik membantu pemasaran di pasar lokal maupun daring.',
        ],
        'checkpoint': (
            'Mengapa prinsip ergonomi penting dalam produk fesyen?',
            [
                ('Agar produk nyaman dan aman dipakai', True),
                ('Agar produk lebih mahal tanpa alasan', False),
                ('Agar warna produk berubah', False),
                ('Agar bahan cepat rusak', False),
            ],
            'Ergonomi memastikan produk nyaman, aman, dan sesuai dengan tubuh pemakai.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merancang produk fesyen Nusantara',
        'paragraphs': [
            'Mulailah dengan mengamati lingkungan sekitar: kain tradisional, motif bangunan, atau aksesori yang dipakai masyarakat. Catat bentuk, warna, dan makna yang mungkin terkandung di dalamnya.',
            'Setelah gagasan terkumpul, buat sketsa beberapa alternatif. Pilih satu desain yang paling sesuai dengan fungsi, bahan yang tersedia, dan kemampuan alat. Pertimbangkan kenyamanan serta keamanan pemakai.',
            'Buat produk pada skala kecil terlebih dahulu, misalnya satu aksesori. Uji kekuatan jahitan dan kerapian hasilnya. Presentasikan produk kepada teman untuk mendapat masukan sebelum memperbaiki desain.',
        ],
        'scenario': scenario(
            'pra-1-skenario',
            'Pesanan aksesori sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kelompokmu mendapat pesanan tas kain bermotif Nusantara. Bahan yang tersedia terbatas. Apa langkah pertamamu?',
                    'choices': [
                        {'text': 'Mengamati kebutuhan dan memilih motif yang sesuai', 'next': 'n2', 'score': 2, 'feedback': 'Observasi kebutuhan menghasilkan rancangan yang tepat.'},
                        {'text': 'Langsung memotong kain tanpa rancangan', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa rancangan, bahan mudah terbuang.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Motif yang dipilih membutuhkan banyak manik-manik, sedangkan waktu terbatas. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Mengganti dengan teknik aplikasi yang lebih efisien', 'next': 'n4', 'score': 2, 'feedback': 'Alternatif teknik menjaga kualitas dan tenggat.'},
                        {'text': 'Tetap memakai manik-manik meski hasilnya terburu-buru', 'next': 'n3', 'score': 0, 'feedback': 'Hasil terburu-buru mengurangi kualitas produk.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pesanan terlambat dan kualitas produk menurun.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk selesai tepat waktu dengan motif yang tetap khas.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan empat jenis motif ragam hias.', 'back': 'Flora, fauna, geometris, dan figuratif.'},
            {'front': 'Apa itu teknik aplikasi?', 'back': 'Menempelkan potongan kain lain pada kain utama lalu dijahit.'},
            {'front': 'Apa itu ergonomi?', 'back': 'Prinsip menyesuaikan produk dengan kenyamanan dan keamanan pemakai.'},
            {'front': 'Apa tujuan presentasi produk?', 'back': 'Mengomunikasikan hasil dan memperoleh masukan untuk perbaikan.'},
        ],
        'checkpoint': (
            'Saat merancang aksesori, hal yang paling perlu dipertimbangkan adalah…',
            [
                ('Kenyamanan dan keamanan pemakai', True),
                ('Harga bahan termahal', False),
                ('Jumlah warna sebanyak mungkin', False),
                ('Ukuran yang paling besar', False),
            ],
            'Ergonomi menempatkan kenyamanan dan keamanan pemakai sebagai pertimbangan utama.',
        ),
        'challenge': challenge_block(
            'pra-1-tantangan',
            'Tantangan istilah kerajinan fesyen',
            90,
            [
                ('Motif meniru tumbuhan', 'flora'),
                ('Motif meniru hewan', 'fauna'),
                ('Teknik menempel kain', 'aplikasi'),
                ('Teknik menyulam', 'sulam'),
                ('Prinsip kenyamanan produk', 'ergonomi'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa yang dimaksud ragam hias?', 'Motif atau corak hias pada benda', ['Bahan dasar kain', 'Alat pemotong kain', 'Tempat penjualan'], 'Ragam hias adalah motif atau corak hias yang diterapkan pada benda.', 'Fungsinya menambah keindahan.'),
        ('Motif yang meniru bentuk tumbuhan disebut…', 'Flora', ['Fauna', 'Geometris', 'Figuratif'], 'Motif flora meniru daun, bunga, dan sulur.', 'Kata “flora” berkaitan dengan tumbuhan.'),
        ('Motif yang meniru bentuk hewan disebut…', 'Fauna', ['Flora', 'Geometris', 'Figuratif'], 'Motif fauna meniru bentuk hewan.', 'Kata “fauna” berkaitan dengan hewan.'),
        ('Motif yang dibentuk dari garis dan lingkaran beraturan disebut…', 'Geometris', ['Flora', 'Fauna', 'Figuratif'], 'Motif geometris memakai bentuk beraturan seperti garis dan lingkaran.', 'Bentuknya terukur dan berulang.'),
        ('Apa nama teknik menghias kain dengan benang dan jarum?', 'Sulam', ['Aplikasi', 'Lukis tekstil', 'Manik-manik'], 'Sulam memakai benang dan jarum mengikuti pola.', 'Teknik ini membutuhkan ketelitian.'),
        ('Apa nama teknik menempelkan potongan kain pada kain utama?', 'Aplikasi', ['Sulam', 'Lukis tekstil', 'Tenun'], 'Aplikasi menempelkan kain lain lalu dijahit pada tepinya.', 'Motif terbentuk dari kain berbeda warna.'),
        ('Apa nama teknik mewarnai motif langsung pada kain?', 'Lukis tekstil', ['Sulam', 'Aplikasi', 'Makrame'], 'Lukis tekstil memakai cat khusus kain.', 'Warna perlu dikunci dengan panas.'),
        ('Apa fungsi pemidangan saat menyulam?', 'Menjaga kain tetap tegang', ['Memotong benang', 'Mewarnai kain', 'Mengukur tubuh'], 'Pemidangan menjaga kain tegang agar tusukan rapi.', 'Kain yang tegang memudahkan pembentukan pola.'),
        ('Apa yang dimaksud ergonomi pada produk fesyen?', 'Prinsip menyesuaikan produk dengan kenyamanan pemakai', ['Menambah jumlah motif', 'Memilih warna paling terang', 'Membuat produk sebesar mungkin'], 'Ergonomi menyesuaikan produk dengan tubuh dan kenyamanan pemakai.', 'Produk tidak boleh melukai atau memberatkan.'),
        ('Manakah contoh produk fesyen?', 'Tas dan topi', ['Vas bunga', 'Lampu taman', 'Pot tanaman'], 'Tas dan topi dipakai di tubuh sehingga termasuk produk fesyen.', 'Vas dan pot termasuk aksesori interior/eksterior.'),
        ('Manakah kain tradisional Indonesia?', 'Batik dan songket', ['Kain kasa steril', 'Kain serat karbon', 'Kain parasut'], 'Batik dan songket adalah kain tradisional Indonesia.', 'Keduanya sering memakai motif Nusantara.'),
        ('Apa langkah pertama dalam proyek kerajinan?', 'Observasi dan eksplorasi gagasan', ['Langsung menjual produk', 'Memotong bahan', 'Membuat kemasan'], 'Proyek dimulai dari observasi dan eksplorasi gagasan.', 'Gagasan menjadi dasar perancangan.'),
        ('Apa tujuan utama presentasi produk?', 'Mengomunikasikan hasil dan memperoleh masukan', ['Menghindari evaluasi', 'Menambah berat produk', 'Mengganti bahan'], 'Presentasi menjelaskan hasil dan membuka ruang masukan.', 'Masukan dipakai untuk perbaikan.'),
        ('Apa yang membuat produk kerajinan bernilai ekonomis lebih tinggi?', 'Keunikan desain dan kualitas pengerjaan', ['Jumlah bahan yang boros', 'Warna yang tidak serasi', 'Kemasan yang rusak'], 'Keunikan dan kualitas meningkatkan daya tarik serta nilai jual.', 'Kerapian finishing juga penting.'),
    ],
    'multi': [
        ('Manakah yang termasuk motif ragam hias Nusantara?', ['Flora', 'Fauna', 'Geometris'], ['Sulam', 'Aplikasi'], 'Flora, fauna, dan geometris adalah motif; sulam dan aplikasi adalah teknik.', 'Bedakan bentuk hiasan dari cara mengerjakannya.'),
        ('Manakah yang termasuk teknik ragam hias pada kain?', ['Sulam', 'Aplikasi', 'Lukis tekstil'], ['Tenun', 'Batik'], 'Sulam, aplikasi, dan lukis tekstil adalah teknik menghias kain.', 'Tenun dan batik adalah teknik pembuatan kain.'),
        ('Manakah yang termasuk bahan produk fesyen?', ['Kain', 'Benang', 'Manik-manik'], ['Tanah liat', 'Bambu'], 'Kain, benang, dan manik-manik dipakai pada produk fesyen.', 'Tanah liat dan bambu lebih cocok untuk interior/eksterior.'),
        ('Manakah prinsip ergonomi produk fesyen?', ['Nyaman dipakai', 'Aman bagi kulit'], ['Terlalu berat', 'Ukuran tidak sesuai'], 'Produk ergonomis nyaman dan aman dipakai.', 'Ukuran harus sesuai pemakai.'),
        ('Manakah tahap dalam proyek kerajinan?', ['Perencanaan', 'Produksi'], ['Menghindari evaluasi', 'Membuang sisa bahan sembarangan'], 'Proyek kerajinan melalui perencanaan dan produksi.', 'Evaluasi juga merupakan tahap penting.'),
        ('Manakah yang meningkatkan nilai ekonomis produk?', ['Desain unik', 'Kualitas jahitan'], ['Bahan yang terbuang', 'Kemasan rusak'], 'Desain unik dan kualitas jahitan meningkatkan nilai jual.', 'Kemasan yang baik juga membantu.'),
        ('Manakah alat yang dipakai dalam kerajinan fesyen?', ['Jarum', 'Gunting kain', 'Pemidangan'], ['Cangkul', 'Palu besar'], 'Jarum, gunting kain, dan pemidangan dipakai dalam kerajinan fesyen.', 'Cangkul dan palu besar bukan alat utama.'),
        ('Manakah ciri produk fesyen yang layak dijual?', ['Jahitan rapi', 'Ukuran sesuai'], ['Motif tidak selesai', 'Bahan mudah sobek'], 'Jahitan rapi dan ukuran sesuai membuat produk layak dijual.', 'Kualitas menentukan kepuasan pembeli.'),
    ],
    'pairs': [
        ('Ragam hias', 'motif atau corak hias pada benda'),
        ('Flora', 'motif yang meniru tumbuhan'),
        ('Fauna', 'motif yang meniru hewan'),
        ('Geometris', 'motif dari garis dan bentuk beraturan'),
        ('Sulam', 'menghias kain dengan benang dan jarum'),
        ('Aplikasi', 'menempelkan kain lain pada kain utama'),
        ('Ergonomi', 'menyesuaikan produk dengan kenyamanan pemakai'),
        ('Presentasi', 'memaparkan hasil produk'),
    ],
    'steps': [
        ('Urutkan alur proyek kerajinan fesyen.', ['Observasi gagasan', 'Analisis nilai ekonomis', 'Perancangan desain', 'Pembuatan produk', 'Presentasi dan evaluasi'], 'Proyek bergerak dari observasi menuju presentasi dan evaluasi.', 'Jangan melompat langsung ke produksi.'),
        ('Urutkan langkah menyulam.', ['Pasang kain pada pemidangan', 'Gambar pola pada kain', 'Tusukkan jarum mengikuti pola', 'Rapikan benang dan hasil sulaman'], 'Menyulam dimulai dari pemasangan kain lalu mengikuti pola.', 'Kain harus tegang agar hasil rapi.'),
        ('Urutkan langkah membuat aplikasi kain.', ['Siapkan pola motif', 'Potong kain sesuai pola', 'Tempelkan pada kain utama', 'Jahit tepi motif'], 'Aplikasi dimulai dari pola lalu dijahit pada kain utama.', 'Jahitan tepi mencegah kain bertiras.'),
        ('Urutkan langkah membuat aksesori fesyen.', ['Ukur kebutuhan', 'Potong bahan', 'Rakit bagian aksesori', 'Lakukan finishing'], 'Aksesori dibuat dari pengukuran sampai finishing.', 'Finishing menentukan kerapian akhir.'),
        ('Urutkan langkah memasarkan produk.', ['Foto produk', 'Tentukan harga', 'Unggah ke media promosi', 'Layani pesanan'], 'Pemasaran bergerak dari foto dan harga menuju pelayanan pesanan.', 'Harga harus mempertimbangkan biaya dan pasar.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
