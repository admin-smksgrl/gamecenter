"""PRA 14 — Manfaatkan Bahan Nonpangan Hewani (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 14',
    'slug': 'prakarya-14-bahan-nonpangan-hewani',
    'title': 'Manfaatkan Bahan Nonpangan Hewani',
    'description': (
        'Mengolah tulang, darah, kulit, bulu, dan sisik menjadi produk nonpangan '
        'bernilai ekonomi, membuat kemoceng dan kemasannya, serta memasarkan '
        'produk dengan bauran 7P.'
    ),
    'objectives': [
        'Mengeksplorasi produk olahan nonpangan dari bahan hewani yang bernilai ekonomis.',
        'Menganalisis karakteristik bahan, alat, teknik, dan prosedur pengolahan nonpangan hewani.',
        'Mengembangkan desain produk dan kemasan nonpangan hewani.',
        'Merancang pemasaran dan analisis usaha nonpangan hewani secara sederhana.',
        'Membuat, mengemas, dan mempromosikan produk nonpangan hewani.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Pengolahan-BG-KLS-X.pdf Unit 4 Manfaatkan Bahan Nonpangan Hewani',
    'glossary': [
        {'term': 'Bahan nonpangan hewani', 'definition': 'Bagian hewan yang tidak diolah menjadi pangan, seperti tulang, darah, kulit, bulu, dan sisik.'},
        {'term': 'Bovine hidroksiapatit', 'definition': 'Serbuk putih hasil pemanasan dan penggilingan tulang sapi atau ikan.'},
        {'term': 'Kolagen', 'definition': 'Protein dari tulang atau kulit yang dapat dimanfaatkan sebagai perekat atau bahan produk.'},
        {'term': 'Tepung darah', 'definition': 'Produk olahan darah yang dikeringkan atau difermentasi untuk pakan atau pupuk.'},
        {'term': 'Kemoceng', 'definition': 'Alat pembersih dari bulu ayam yang dirangkai pada tangkai kayu atau rotan.'},
        {'term': 'Kemasan sekunder', 'definition': 'Kemasan tambahan yang memudahkan penyimpanan dan pengangkutan produk.'},
        {'term': 'Bauran pemasaran 7P', 'definition': 'Tujuh unsur pemasaran: product, price, place, promotion, people, process, dan physical evidence.'},
        {'term': 'Brand image', 'definition': 'Citra atau kesan produk di mata konsumen yang dijaga melalui pemasaran.'},
    ],
    'intro': {
        'material_title': 'Mengapa bahan nonpangan hewani perlu diolah?',
        'title': 'Dari limbah menjadi produk bernilai',
        'paragraphs': [
            'Produk olahan nonpangan dari bahan hewani banyak dimanfaatkan untuk kehidupan sehari-hari. Bahan tersebut antara lain tulang, darah, kulit, bulu, dan sisik. Bagian-bagian ini sering menjadi limbah yang dapat mencemari lingkungan jika tidak ditangani dengan baik.',
            'Tulang merupakan bagian rangka pembentuk tubuh tempat melekatnya otot dan daging. Darah adalah cairan yang terdiri atas plasma, sel merah, dan sel putih yang mengalir dalam pembuluh darah. Kulit adalah bagian terluar daging, sedangkan bulu merupakan lapisan luar kulit yang menutup tubuh unggas.',
            'Sisik adalah lapisan kulit keras berupa kepingan tipis yang tersusun pada ikan. Dengan pengolahan yang tepat, bahan-bahan tersebut berubah menjadi produk bernilai ekonomi sekaligus mengurangi pencemaran lingkungan. Pemanfaatan ini juga meningkatkan nilai tambah bahan.',
        ],
        'diagram': (
            'Lima bahan nonpangan hewani',
            'flowchart TB\n'
            '  A[Bahan nonpangan hewani] --> B[Tulang]\n'
            '  A --> C[Darah]\n'
            '  A --> D[Kulit]\n'
            '  A --> E[Bulu]\n'
            '  A --> F[Sisik]',
        ),
        'callout': 'Gunakan sarung tangan dan masker saat mengolah tulang, darah, atau bahan hewani lain. Cuci tangan serta peralatan dengan sabun setelah selesai.',
        'checkpoint': (
            'Manakah yang termasuk bahan nonpangan hewani?',
            [
                ('Tulang, darah, kulit, bulu, dan sisik', True),
                ('Beras, jagung, dan gandum', False),
                ('Bayam, kangkung, dan selada', False),
                ('Kacang tanah, kedelai, dan kacang hijau', False),
            ],
            'Bahan nonpangan hewani meliputi tulang, darah, kulit, bulu, dan sisik.',
        ),
    },
    'concept': {
        'material_title': 'Produk olahan dari tulang, darah, kulit, bulu, dan sisik',
        'title': 'Mengubah limbah menjadi produk',
        'paragraphs': [
            'Tulang sapi dan tulang ikan dapat dimurnikan dengan pemanasan pada suhu 1.000 °C selama 2 jam, lalu digiling menjadi serbuk putih yang disebut bovine hidroksiapatit. Tulang ayam dapat diekstraksi dengan perendaman asam asetat, kemudian dipanaskan pada suhu 60–70 °C selama 8 jam untuk menghasilkan kolagen yang dapat dimanfaatkan sebagai perekat kayu. Penepungan tulang juga menghasilkan pakan ternak kaya kalsium.',
            'Darah ternak besar dari rumah potong hewan dapat diolah menjadi tepung darah melalui pengeringan, penyerapan, atau fermentasi dengan mikroorganisme tertentu. Tepung darah dapat menjadi bahan pakan atau pupuk sehingga mengurangi pencemaran limbah rumah potong hewan. Kulit sapi, kerbau, kambing, atau domba dapat diolah menjadi tas, sepatu, karpet, atau hiasan bernilai ekonomi tinggi karena struktur jaringannya kuat.',
            'Bulu unggas seperti ayam, bebek, dan itik dimanfaatkan untuk membuat kemoceng atau sulak. Sentra pembuatan kemoceng Nusantara antara lain berada di Dusun Ngriman, Desa Karanglo, Kecamatan Klaten Selatan, Kabupaten Klaten. Sisik ikan dapat diolah menjadi obat luka karena mengandung kolagen tinggi, serta menjadi bros atau gantungan kunci.',
        ],
        'table': [
            ['Bahan', 'Produk olahan', 'Manfaat'],
            ['Tulang sapi dan ikan', 'Bovine hidroksiapatit', 'Bahan baku produk bernilai'],
            ['Tulang ayam', 'Kolagen', 'Perekat kayu'],
            ['Darah', 'Tepung darah', 'Pakan atau pupuk'],
            ['Kulit', 'Tas, sepatu, karpet', 'Produk bernilai ekonomi tinggi'],
            ['Bulu', 'Kemoceng atau sulak', 'Alat pembersih'],
            ['Sisik', 'Obat luka, bros, gantungan kunci', 'Kesehatan dan hiasan'],
        ],
        'visual': chart_block(
            'pra-14-suhu-pengolahan',
            'Suhu pengolahan beberapa bahan nonpangan hewani (°C)',
            'bar',
            [('Tulang sapi', 1000), ('Tulang ayam', 70), ('Perapian telur', 30)],
        ),
        'activity': categorize_block(
            'pra-14-klasifikasi',
            'Kelompokkan produk berikut berdasarkan bahan asalnya.',
            [('b1', 'Tulang'), ('b2', 'Darah'), ('b3', 'Kulit'), ('b4', 'Bulu'), ('b5', 'Sisik')],
            [
                ('i1', 'Bovine hidroksiapatit', 'b1'),
                ('i2', 'Tepung darah', 'b2'),
                ('i3', 'Tas dan sepatu', 'b3'),
                ('i4', 'Kemoceng', 'b4'),
                ('i5', 'Obat luka', 'b5'),
                ('i6', 'Bros dan gantungan kunci', 'b5'),
            ],
            'Tepat. Bovine hidroksiapatit dari tulang; tepung darah dari darah; tas dan sepatu dari kulit; kemoceng dari bulu; obat luka serta hiasan dari sisik.',
            'Periksa lagi: cocokkan produk dengan bahan asal yang disebut buku.',
        ),
        'subtitle': 'Kemasan dan pemasaran',
        'list': [
            'Kemasan melindungi produk dari kerusakan saat penyimpanan dan pendistribusian.',
            'Label unik menjadi daya tarik dan ciri khas yang membedakan produk.',
            'Kemasan sekunder dan tersier memudahkan pengangkutan produk.',
            'Pemasaran memakai bauran 7P: product, price, place, promotion, people, process, dan physical evidence.',
            'Pemasaran menjaga brand image, sedangkan promosi menawarkan produk.',
        ],
        'checkpoint': (
            'Serbuk putih hasil pemanasan dan penggilingan tulang disebut…',
            [
                ('Bovine hidroksiapatit', True),
                ('Tepung darah', False),
                ('Kolagen', False),
                ('Kitosan', False),
            ],
            'Bovine hidroksiapatit adalah serbuk putih dari tulang sapi atau ikan yang dipanaskan dan digiling.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat kemoceng dan memasarkan produk',
        'paragraphs': [
            'Kemoceng dibuat dari bulu ayam. Pilih bulu ekor ayam jago yang lebih besar untuk bagian atas, bulu leher yang lembut dan rapi untuk bagian badan, serta bulu kecil untuk bagian bawah. Bersihkan bulu dengan air mengalir, campur pewarna dan air sesuai intensitas yang diinginkan, rendam bulu, lalu keringkan di bawah sinar matahari langsung.',
            'Setelah kering, rangkai bulu dengan menjahitnya satu per satu menggunakan jarum dan benang. Lilitkan bulu yang telah dirangkai ke tangkai kayu atau rotan, ikat ujung lilitan dengan tali atau benang sol sepatu, lalu buat kait pada tangkai. Kemoceng siap dikemas dan dipasarkan.',
            'Kemasan kemoceng melindungi produk dari kerusakan saat penyimpanan dan distribusi. Label yang unik dan merek yang mudah diingat meningkatkan daya tarik konsumen. Untuk memasarkan produk, gunakan bauran 7P yang meliputi produk, harga, tempat, promosi, sumber daya manusia, proses bisnis, dan bukti fisik perusahaan.',
        ],
        'scenario': scenario(
            'pra-14-skenario',
            'Kemoceng sekolah yang belum dikenal',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kemoceng buatan kelompokmu bagus, tetapi belum ada yang membeli. Apa langkah pertama?',
                    'choices': [
                        {'text': 'Menyusun promosi dan menentukan target pasar', 'next': 'n2', 'score': 2, 'feedback': 'Promosi dan target pasar membantu produk dikenal pembeli.'},
                        {'text': 'Menurunkan harga sampai di bawah biaya produksi', 'next': 'n3', 'score': 0, 'feedback': 'Menjual di bawah biaya produksi menimbulkan kerugian.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Pembeli mengeluh kemasan mudah rusak saat dikirim. Apa tindakanmu?',
                    'choices': [
                        {'text': 'Menambah kemasan sekunder yang melindungi produk', 'next': 'n4', 'score': 2, 'feedback': 'Kemasan sekunder memudahkan dan melindungi saat pengangkutan.'},
                        {'text': 'Mengirim tanpa kemasan agar lebih ringan', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa kemasan produk mudah rusak.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk rusak dan usaha merugi.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk aman sampai dan usaha memperoleh laba.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan lima bahan nonpangan hewani.', 'back': 'Tulang, darah, kulit, bulu, dan sisik.'},
            {'front': 'Apa itu bovine hidroksiapatit?', 'back': 'Serbuk putih dari tulang yang dipanaskan 1.000 °C lalu digiling.'},
            {'front': 'Di mana sentra kemoceng Nusantara?', 'back': 'Dusun Ngriman, Desa Karanglo, Klaten Selatan, Kabupaten Klaten.'},
            {'front': 'Sebutkan tujuh unsur bauran pemasaran.', 'back': 'Product, price, place, promotion, people, process, physical evidence.'},
        ],
        'checkpoint': (
            'Bulu ayam banyak dimanfaatkan untuk membuat…',
            [
                ('Kemoceng atau sulak', True),
                ('Tepung darah', False),
                ('Bovine hidroksiapatit', False),
                ('Obat luka', False),
            ],
            'Bulu ayam, bebek, dan itik dimanfaatkan untuk membuat kemoceng atau sulak.',
        ),
        'challenge': challenge_block(
            'pra-14-tantangan',
            'Tantangan istilah nonpangan hewani',
            90,
            [
                ('Serbuk putih dari tulang', 'bovine hidroksiapatit'),
                ('Produk olahan darah', 'tepung darah'),
                ('Alat pembersih dari bulu ayam', 'kemoceng'),
                ('Bahan hiasan dari sisik ikan', 'bros'),
                ('Bauran pemasaran tujuh unsur', '7P'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Manakah yang termasuk bahan nonpangan hewani?', 'Tulang, darah, kulit, bulu, dan sisik', ['Beras, jagung, dan gandum', 'Bayam, kangkung, dan selada', 'Kacang tanah dan kedelai'], 'Bahan nonpangan hewani meliputi tulang, darah, kulit, bulu, dan sisik.', 'Beras dan sayur termasuk bahan nabati.'),
        ('Bulu ayam banyak dimanfaatkan untuk membuat…', 'Kemoceng atau sulak', ['Tepung darah', 'Obat luka', 'Bovine hidroksiapatit'], 'Bulu unggas dimanfaatkan untuk membuat kemoceng atau sulak.', 'Bulu diwarnai lalu dirangkai pada tangkai.'),
        ('Kulit sapi dapat diolah menjadi…', 'Tas, sepatu, dan karpet', ['Tepung darah', 'Obat luka', 'Bovine hidroksiapatit'], 'Kulit ternak besar dapat diolah menjadi tas, sepatu, karpet, atau hiasan.', 'Struktur jaringannya kuat.'),
        ('Tulang sapi dipanaskan pada suhu… untuk menghasilkan bovine hidroksiapatit', '1.000 °C', ['60–70 °C', '100 °C', '500 °C'], 'Tulang sapi dipanaskan pada suhu 1.000 °C selama 2 jam.', 'Setelah itu digiling menjadi serbuk putih.'),
        ('Lama pemanasan tulang sapi untuk bovine hidroksiapatit adalah…', '2 jam', ['8 jam', '30 menit', '2 hari'], 'Tulang sapi dipanaskan pada suhu 1.000 °C selama 2 jam.', 'Hasilnya digiling menjadi serbuk.'),
        ('Kolagen dari tulang ayam dapat dimanfaatkan sebagai…', 'Perekat kayu', ['Pewarna kain', 'Bahan bakar', 'Pupuk tanaman'], 'Kolagen dari tulang ayam dapat dimanfaatkan sebagai perekat kayu.', 'Diperoleh melalui ekstraksi asam asetat.'),
        ('Sisik ikan mengandung… dalam jumlah tinggi', 'Kolagen', ['Garam', 'Gula', 'Lemak jenuh'], 'Sisik ikan mengandung kolagen tinggi sehingga dapat menjadi obat luka.', 'Kolagennya lebih tinggi dari mamalia.'),
        ('Sentra pembuatan kemoceng Nusantara berada di…', 'Dusun Ngriman, Klaten', ['Desa Cilembu, Sumedang', 'Brebes, Jawa Tengah', 'Lembang, Bandung'], 'Sentra kemoceng berada di Dusun Ngriman, Desa Karanglo, Klaten Selatan, Kabupaten Klaten.', 'Bulu ayam diolah menjadi kemoceng.'),
        ('Tepung darah dapat diperoleh melalui…', 'Pengeringan, penyerapan, atau fermentasi', ['Pembekuan dan pengasapan', 'Pengalengan dan pemanasan', 'Pemanggangan dan penggorengan'], 'Tepung darah diperoleh melalui pengeringan, penyerapan, atau fermentasi darah segar.', 'Dapat menjadi pakan atau pupuk.'),
        ('Ekstraksi kolagen tulang ayam menggunakan…', 'Asam asetat', ['Garam dapur', 'Gula pasir', 'Air kapur'], 'Tulang ayam direndam asam asetat lalu dipanaskan untuk menghasilkan kolagen.', 'Pemanasan pada suhu 60–70 °C.'),
        ('Suhu pemanasan tulang ayam untuk menghasilkan kolagen adalah…', '60–70 °C selama 8 jam', ['1.000 °C selama 2 jam', '100 °C selama 30 menit', '200 °C selama 1 jam'], 'Tulang ayam dipanaskan pada suhu 60–70 °C selama 8 jam.', 'Menghasilkan kolagen untuk perekat kayu.'),
        ('Bauran pemasaran 7P meliputi…', 'Product, price, place, promotion, people, process, physical evidence', ['Product, profit, place, power, people, price, process', 'Price, profit, promotion, place, people, power, product', 'Product, price, promotion, profit, place, people, process'], '7P terdiri atas product, price, place, promotion, people, process, dan physical evidence.', 'Dipakai untuk menyusun pemasaran.'),
        ('Perbedaan pemasaran dan promosi adalah…', 'Pemasaran menjaga brand image, promosi menawarkan produk', ['Pemasaran menawarkan produk, promosi menjaga brand image', 'Keduanya sama saja', 'Pemasaran hanya untuk produk mahal'], 'Pemasaran menjaga citra produk, sedangkan promosi menawarkan produk.', 'Keduanya saling melengkapi.'),
        ('Kemasan sekunder dan tersier berfungsi untuk…', 'Memudahkan pengangkutan saat penyimpanan dan distribusi', ['Mempercepat kerusakan produk', 'Menambah berat tanpa manfaat', 'Menggantikan label produk'], 'Kemasan sekunder dan tersier memudahkan pengangkutan produk.', 'Selain itu melindungi produk.'),
    ],
    'multi': [
        ('Manakah bahan nonpangan hewani?', ['Tulang', 'Darah', 'Kulit', 'Bulu', 'Sisik'], ['Beras', 'Jagung'], 'Tulang, darah, kulit, bulu, dan sisik termasuk bahan nonpangan hewani.', 'Beras dan jagung bahan nabati.'),
        ('Manakah produk dari kulit ternak?', ['Tas', 'Sepatu', 'Karpet'], ['Tempe', 'Tahu'], 'Kulit ternak diolah menjadi tas, sepatu, dan karpet.', 'Tempe dan tahu berbahan kedelai.'),
        ('Manakah produk dari tulang?', ['Bovine hidroksiapatit', 'Kolagen', 'Tepung tulang untuk pakan'], ['Tepung terigu', 'Gula pasir'], 'Tulang dapat menghasilkan bovine hidroksiapatit, kolagen, dan tepung tulang.', 'Tepung terigu dan gula bukan dari tulang.'),
        ('Manakah pemanfaatan sisik ikan?', ['Obat luka', 'Bros', 'Gantungan kunci'], ['Bahan bakar', 'Semen'], 'Sisik ikan dapat menjadi obat luka, bros, dan gantungan kunci.', 'Sisik mengandung kolagen tinggi.'),
        ('Manakah alat membuat kemoceng?', ['Baskom', 'Jarum', 'Gunting'], ['Traktor', 'Cangkul'], 'Kemoceng dibuat dengan baskom, jarum, benang, dan gunting.', 'Traktor dan cangkul untuk lahan.'),
        ('Manakah unsur bauran pemasaran 7P?', ['Product', 'Price', 'Place', 'Promotion'], ['Profit', 'Power'], '7P meliputi product, price, place, promotion, people, process, dan physical evidence.', 'Profit dan power bukan unsur 7P.'),
        ('Manakah tahap membuat kemoceng?', ['Pilih bulu ayam', 'Bersihkan bulu', 'Warnai bulu', 'Keringkan bulu', 'Jahit dan lilitkan ke tangkai'], ['Membakar bulu', 'Membuang tangkai'], 'Kemoceng dibuat dari pemilihan, pencucian, pewarnaan, pengeringan, lalu perangkaian.', 'Bulu dijahit satu per satu.'),
        ('Manakah manfaat pengolahan nonpangan hewani?', ['Mengurangi pencemaran', 'Menambah nilai ekonomi', 'Menghasilkan produk bernilai'], ['Menambah limbah', 'Mencemari lingkungan'], 'Pengolahan mengurangi pencemaran dan menambah nilai ekonomi bahan.', 'Limbah yang diolah tidak dibiarkan mencemari.'),
    ],
    'pairs': [
        ('Tulang', 'bovine hidroksiapatit'),
        ('Darah', 'tepung darah'),
        ('Kulit', 'tas dan sepatu'),
        ('Bulu', 'kemoceng dan sulak'),
        ('Sisik', 'obat luka dan hiasan'),
        ('Bovine hidroksiapatit', 'serbuk putih dari tulang'),
        ('7P', 'bauran pemasaran'),
        ('Kemasan', 'pelindung produk saat distribusi'),
    ],
    'steps': [
        ('Urutkan langkah membuat kemoceng.', ['Pilih bulu ayam', 'Bersihkan bulu dengan air mengalir', 'Campur pewarna dan air', 'Rendam bulu hingga berwarna', 'Keringkan di bawah sinar matahari', 'Jahit bulu satu per satu', 'Lilitkan ke tangkai dan ikat', 'Buat kait pada tangkai'], 'Kemoceng dibuat dari bulu yang dibersihkan, diwarnai, dikeringkan, lalu dirangkai.', 'Bulu dijahit sebelum dililitkan ke tangkai.'),
        ('Urutkan langkah membuat tepung darah.', ['Tampung darah segar', 'Keringkan atau fermentasikan', 'Giling menjadi tepung', 'Ayak untuk menyeragamkan', 'Kemas untuk pakan atau pupuk'], 'Tepung darah dibuat dari darah yang dikeringkan lalu digiling.', 'Hasilnya berupa tepung halus.'),
        ('Urutkan langkah membuat bovine hidroksiapatit.', ['Bersihkan tulang', 'Panaskan pada 1.000 °C selama 2 jam', 'Giling tulang', 'Ayak menjadi serbuk putih', 'Kemas produk'], 'Bovine hidroksiapatit dibuat melalui pemanasan suhu tinggi lalu penggilingan.', 'Pemanasan berlangsung 2 jam.'),
        ('Urutkan langkah menyusun bauran pemasaran 7P.', ['Tentukan produk', 'Tentukan harga', 'Tentukan tempat', 'Rancang promosi', 'Siapkan sumber daya manusia dan proses', 'Siapkan bukti fisik'], 'Bauran pemasaran disusun dari produk hingga bukti fisik.', 'Ketujuh unsur saling mendukung.'),
        ('Urutkan langkah promosi produk.', ['Tentukan tujuan promosi', 'Tentukan target pasar', 'Pilih media promosi', 'Jalankan promosi', 'Ukur efektivitas'], 'Promosi dimulai dari tujuan lalu diakhiri pengukuran.', 'Efektivitas menentukan perbaikan berikutnya.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
