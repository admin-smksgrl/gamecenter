"""PRA 13 — Gugah Selera dengan Olahan Pangan Hewani (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 13',
    'slug': 'prakarya-13-olahan-pangan-hewani',
    'title': 'Gugah Selera dengan Olahan Pangan Hewani',
    'description': (
        'Mengenal daging, ikan, susu, dan telur, ragam olahan pangan hewani '
        'Nusantara, teknik pengawetan, kemasan dan label, serta promosi produk.'
    ),
    'objectives': [
        'Mengeksplorasi produk olahan pangan higienis Nusantara dari bahan hewani.',
        'Menganalisis karakteristik bahan, alat, teknik, dan prosedur pengolahan pangan hewani.',
        'Mengembangkan desain produk dan kemasan olahan pangan hewani.',
        'Merancang pemasaran dan analisis usaha olahan pangan hewani secara sederhana.',
        'Membuat, mengemas, dan mempromosikan olahan pangan hewani Nusantara.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Pengolahan-BG-KLS-X.pdf Unit 3 Gugah Selera dengan Olahan Pangan Hewani',
    'glossary': [
        {'term': 'Bahan pangan hewani', 'definition': 'Bahan pangan yang berasal dari hewan, seperti daging, ikan, susu, dan telur.'},
        {'term': 'Daging', 'definition': 'Bagian lunak hewan yang melekat pada tulang dan dibungkus kulit.'},
        {'term': 'Pengasapan', 'definition': 'Pengawetan dengan panas dan asap pembakaran kayu tertentu.'},
        {'term': 'Fermentasi', 'definition': 'Pengawetan dengan mikroorganisme yang mengubah karbohidrat menjadi alkohol atau asam.'},
        {'term': 'Pengasinan', 'definition': 'Pengawetan dengan garam untuk menghambat mikroorganisme perusak.'},
        {'term': 'Kemasan', 'definition': 'Wadah untuk melindungi produk dari cemaran saat penyimpanan atau pendistribusian.'},
        {'term': 'Label', 'definition': 'Keterangan pada kemasan yang memuat informasi produk sesuai ketentuan.'},
        {'term': 'Promosi', 'definition': 'Kegiatan memperkenalkan dan menawarkan produk agar konsumen tertarik membeli.'},
    ],
    'intro': {
        'material_title': 'Apa saja bahan pangan hewani?',
        'title': 'Sumber protein dari hewan',
        'paragraphs': [
            'Daging merupakan bagian lunak hewan yang melekat pada tulang dan dibungkus kulit. Daging memiliki protein dengan susunan asam amino lengkap. Pada umumnya daging mengandung sekitar 75 persen air, 18 persen protein, 3 persen lemak, dan 1,5 persen senyawa nitrogen bukan protein serta vitamin dan mineral dalam jumlah sedikit.',
            'Ikan merupakan sumber protein yang lebih mudah diserap tubuh dibandingkan daging sapi karena susunan asam aminonya lebih sederhana. Protein ikan bermanfaat untuk peremajaan jaringan dan sumber energi. Susu adalah cairan putih dari kelenjar mamalia seperti sapi dan kambing, dengan kandungan protein, lemak, vitamin, dan mineral.',
            'Telur merupakan bahan makanan hewani yang dikonsumsi selain daging, ikan, dan susu. Telur yang biasa dikonsumsi adalah telur ayam, bebek, dan puyuh. Setiap bahan hewani memiliki karakteristik dan olahan khas yang berbeda di berbagai daerah Nusantara.',
        ],
        'diagram': (
            'Empat kelompok bahan pangan hewani',
            'flowchart TB\n'
            '  A[Bahan pangan hewani] --> B[Daging]\n'
            '  A --> C[Ikan]\n'
            '  A --> D[Susu]\n'
            '  A --> E[Telur]',
        ),
        'callout': 'Simpan daging dan ikan di wadah tertutup pada suhu dingin. Cuci tangan serta alat masak setelah menyentuh bahan mentah agar tidak terjadi kontaminasi silang.',
        'checkpoint': (
            'Kandungan protein daging pada umumnya sekitar…',
            [
                ('18 persen', True),
                ('3 persen', False),
                ('75 persen', False),
                ('50 persen', False),
            ],
            'Daging mengandung sekitar 75 persen air, 18 persen protein, dan 3 persen lemak.',
        ),
    },
    'concept': {
        'material_title': 'Olahan Nusantara dan teknik pengawetan',
        'title': 'Kekayaan olahan pangan hewani',
        'paragraphs': [
            'Olahan pangan hewani Nusantara sangat beragam. Daging diolah menjadi sate padang, coto makassar, isian sosis solo, rendang padang, rawon malang, dan soto betawi. Ikan diolah menjadi cakalang fufu khas Manado, mangut khas Yogyakarta, arsik khas Tapanuli, sop ikan jantung pisang khas Palu, dan gabus pucung khas Jakarta.',
            'Susu diolah menjadi dadiah atau yoghurt khas Minang, dangke khas Sulawesi Selatan, serta tahu atau dodol susu dari Lembang. Telur diolah menjadi telur asin khas Brebes, kerak telor khas Betawi, telur balado khas Minang, dan rendang talua khas Payakumbuh. Setiap daerah memberi ciri khas pada produknya.',
            'Pengawetan pangan hewani terdiri atas pengawetan fisik, biologi, dan kimia. Pembekuan menurunkan suhu di bawah titik beku air, contohnya sosis solo frozen. Pengasapan memanfaatkan asap pembakaran kayu, contohnya cakalang fufu. Fermentasi memakai mikroorganisme, contohnya dadiah, sedangkan pengasinan memakai garam, contohnya telur asin Brebes.',
        ],
        'table': [
            ['Makanan', 'Daerah', 'Bahan dasar'],
            ['Kuah Sie Itek', 'Aceh', 'Itik'],
            ['Rendang Padang', 'Padang', 'Daging sapi'],
            ['Bandeng Presto', 'Semarang', 'Ikan bandeng'],
            ['Sate Madura', 'Madura', 'Daging ayam'],
            ['Soto Makassar', 'Makassar', 'Daging sapi'],
            ['Ayam Betutu', 'Bali', 'Ayam'],
        ],
        'visual': chart_block(
            'pra-13-komposisi-daging',
            'Perkiraan komposisi daging (%)',
            'bar',
            [('Air', 75), ('Protein', 18), ('Lemak', 3), ('Senyawa nitrogen', 1.5)],
        ),
        'activity': categorize_block(
            'pra-13-klasifikasi',
            'Kelompokkan olahan berikut berdasarkan bahan dasarnya.',
            [('b1', 'Daging sapi'), ('b2', 'Ikan'), ('b3', 'Susu'), ('b4', 'Telur')],
            [
                ('i1', 'Rendang padang', 'b1'),
                ('i2', 'Soto makassar', 'b1'),
                ('i3', 'Cakalang fufu', 'b2'),
                ('i4', 'Bandeng presto', 'b2'),
                ('i5', 'Dadiah', 'b3'),
                ('i6', 'Telur asin', 'b4'),
            ],
            'Tepat. Rendang dan soto berbahan daging sapi; cakalang fufu dan bandeng presto berbahan ikan; dadiah dari susu; telur asin dari telur.',
            'Periksa lagi: cocokkan bahan dasar dengan nama produk.',
        ),
        'subtitle': 'Kemasan, label, dan promosi',
        'list': [
            'Kemasan melindungi produk dari cemaran dan memiliki fungsi promosi, simbolik, serta estetik.',
            'Menurut UU No. 18 Tahun 2012, label memuat nama produk, daftar bahan, berat bersih, nama dan alamat produsen, informasi halal, tanggal dan kode produksi, kadaluarsa, nomor izin edar, serta asal-usul bahan.',
            'Promosi dimulai dengan menentukan tujuan, target pasar dan harga jual, anggaran, media, lalu mengukur efektivitasnya.',
            'Promosi lebih menekankan cara menarik konsumen untuk mencoba dan membeli produk.',
        ],
        'checkpoint': (
            'Undang-Undang yang mengatur pencantuman label pangan adalah…',
            [
                ('UU No. 18 Tahun 2012', True),
                ('UU No. 18 Tahun 2002', False),
                ('UU No. 20 Tahun 2003', False),
                ('UU No. 12 Tahun 2012', False),
            ],
            'Pencantuman label pangan diatur dalam UU RI No. 18 Tahun 2012.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat olahan hewani dan mempromosikannya',
        'paragraphs': [
            'Sosis solo dibuat dari kulit tepung terigu, air, telur, dan garam, dengan isi daging ayam yang direbus lalu disuwir. Bumbu bawang merah, bawang putih, merica, kaldu, gula, dan air ditumis hingga meresap. Kulit diisi, dibentuk seperti lumpia kecil panjang, direkatkan dengan putih telur, lalu disimpan di freezer dalam wadah tertutup.',
            'Cakalang fufu dibuat dengan membersihkan ikan, membelahnya, dan menjepitnya dengan bambu. Ikan disusun di tempat pengasapan, lalu bara tempurung kelapa disebar hingga kadar air berkurang sekitar 4 jam. Dadiah dibuat dari susu kerbau segar yang dimasukkan ke bambu tiga per empat penuh, ditutup, lalu disimpan pada suhu ruang selama 1–3 hari.',
            'Telur asin dibuat dengan memilih telur bermutu, membersihkannya, lalu mengamplas permukaan agar pori terbuka. Adonan pengasin dibuat dari campuran abu gosok atau bata merah dan garam dengan perbandingan 2:1, ditambah air hingga berbentuk pasta. Telur dibalut adonan, diperam 1–2 minggu, dicuci, lalu direbus sekitar 45 menit dengan api kecil. Setelah produk siap, susun promosi dan ukur efektivitasnya.',
        ],
        'scenario': scenario(
            'pra-13-skenario',
            'Telur asin yang terlalu lama diperam',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Telur asin kelompokmu terasa terlalu asin. Apa penyebab yang paling mungkin?',
                    'choices': [
                        {'text': 'Pemeraman terlalu lama atau garam terlalu banyak', 'next': 'n2', 'score': 2, 'feedback': 'Lama pemeraman dan jumlah garam memengaruhi rasa asin.'},
                        {'text': 'Telur terlalu banyak air', 'next': 'n3', 'score': 0, 'feedback': 'Air tidak membuat telur menjadi lebih asin.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Agar produk laku di bazar, apa langkah promosi yang tepat?',
                    'choices': [
                        {'text': 'Menentukan target pasar, media, dan anggaran promosi', 'next': 'n4', 'score': 2, 'feedback': 'Promosi yang terencana lebih efektif menarik konsumen.'},
                        {'text': 'Menjual tanpa memperkenalkan produk', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa promosi konsumen sulit mengenal produk.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk tidak dikenal dan tidak terjual.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk dikenal dan habis terjual.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Berapa kandungan air dan protein daging?', 'back': 'Sekitar 75 persen air dan 18 persen protein.'},
            {'front': 'Apa teknik pengawetan cakalang fufu?', 'back': 'Pengasapan dengan bara tempurung kelapa.'},
            {'front': 'Berapa lama dadiah disimpan pada suhu ruang?', 'back': '1–3 hari sampai susu menggumpal.'},
            {'front': 'Apa perbandingan adonan pengasin telur asin?', 'back': 'Dua bagian abu atau bata merah dan satu bagian garam.'},
        ],
        'checkpoint': (
            'Cakalang fufu diawetkan dengan teknik…',
            [
                ('Pengasapan', True),
                ('Pembekuan', False),
                ('Fermentasi', False),
                ('Pengentalan', False),
            ],
            'Cakalang fufu diawetkan dengan pengasapan menggunakan bara tempurung kelapa.',
        ),
        'challenge': challenge_block(
            'pra-13-tantangan',
            'Tantangan istilah pangan hewani',
            90,
            [
                ('Cairan putih dari kelenjar mamalia', 'susu'),
                ('Pengawetan dengan asap kayu', 'pengasapan'),
                ('Pengawetan dengan garam', 'pengasinan'),
                ('Olahan susu khas Minang', 'dadiah'),
                ('Kegiatan menawarkan produk', 'promosi'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Daging pada umumnya mengandung air sekitar…', '75 persen', ['18 persen', '3 persen', '50 persen'], 'Daging mengandung sekitar 75 persen air.', 'Proteinnya sekitar 18 persen.'),
        ('Kandungan protein daging pada umumnya sekitar…', '18 persen', ['3 persen', '75 persen', '50 persen'], 'Daging mengandung sekitar 18 persen protein.', 'Lemaknya sekitar 3 persen.'),
        ('Bahan pangan hewani berupa cairan putih dari kelenjar mamalia adalah…', 'Susu', ['Telur', 'Daging', 'Ikan'], 'Susu adalah cairan putih yang dihasilkan kelenjar mamalia.', 'Diperoleh dengan cara pemerahan.'),
        ('Protein ikan lebih mudah diserap tubuh karena…', 'Susunan asam aminonya lebih sederhana', ['Kandungan airnya lebih sedikit', 'Tidak mengandung lemak', 'Berwarna putih'], 'Protein ikan mudah diserap karena susunan asam aminonya lebih sederhana.', 'Bermanfaat untuk peremajaan jaringan.'),
        ('Cakalang fufu merupakan makanan khas…', 'Manado', ['Padang', 'Brebes', 'Makassar'], 'Cakalang fufu adalah makanan khas Manado.', 'Dibuat dari ikan cakalang yang diasap.'),
        ('Rendang merupakan makanan khas…', 'Padang', ['Manado', 'Brebes', 'Bali'], 'Rendang padang berasal dari Padang dan berbahan daging sapi.', 'Dimasak dengan rempah dan santan.'),
        ('Telur asin merupakan makanan khas…', 'Brebes', ['Padang', 'Manado', 'Bali'], 'Telur asin khas Brebes dibuat dengan pengasinan.', 'Berbahan dasar telur bebek.'),
        ('Dadiah dibuat dari…', 'Susu kerbau segar', ['Daging sapi', 'Ikan cakalang', 'Telur bebek'], 'Dadiah dibuat dari susu kerbau segar yang difermentasi dalam bambu.', 'Merupakan olahan khas Minang.'),
        ('Pengawetan cakalang fufu menggunakan teknik…', 'Pengasapan', ['Pembekuan', 'Fermentasi', 'Pengentalan'], 'Cakalang fufu diawetkan dengan pengasapan.', 'Memakai bara tempurung kelapa.'),
        ('Pengawetan dadiah menggunakan teknik…', 'Fermentasi', ['Pengasapan', 'Pengasinan', 'Pembekuan'], 'Dadiah dibuat melalui fermentasi susu kerbau.', 'Bakteri baik berasal dari bambu.'),
        ('Pengawetan telur asin menggunakan teknik…', 'Pengasinan', ['Pengasapan', 'Fermentasi', 'Pembekuan'], 'Telur asin diawetkan dengan garam atau pengasinan.', 'Garam menghambat mikroorganisme perusak.'),
        ('Perbandingan adonan pengasin telur asin adalah…', '2 bagian abu atau bata merah : 1 bagian garam', ['1 bagian abu : 2 bagian garam', '1 bagian abu : 1 bagian gula', '3 bagian garam : 1 bagian air'], 'Adonan pengasin memakai perbandingan abu atau bata merah dan garam 2:1.', 'Ditambah air hingga berbentuk pasta.'),
        ('Lama pemeraman telur asin adalah…', '1–2 minggu', ['1–2 jam', '1–2 hari', '1–2 bulan'], 'Telur asin diperam selama 1–2 minggu.', 'Setelah itu dicuci dan direbus.'),
        ('Undang-Undang yang mengatur pencantuman label pangan adalah…', 'UU No. 18 Tahun 2012', ['UU No. 18 Tahun 2002', 'UU No. 20 Tahun 2003', 'UU No. 12 Tahun 2012'], 'Label pangan diatur dalam UU RI No. 18 Tahun 2012.', 'Label memuat informasi produk secara lengkap.'),
    ],
    'multi': [
        ('Manakah yang termasuk bahan pangan hewani?', ['Daging', 'Ikan', 'Susu', 'Telur'], ['Bayam', 'Kangkung'], 'Daging, ikan, susu, dan telur termasuk bahan pangan hewani.', 'Bayam dan kangkung bahan nabati.'),
        ('Manakah makanan khas berbahan daging sapi?', ['Rendang', 'Soto Makassar', 'Sate Padang'], ['Cakalang fufu', 'Dadiah'], 'Rendang, soto Makassar, dan sate Padang berbahan daging sapi.', 'Cakalang fufu berbahan ikan dan dadiah dari susu.'),
        ('Manakah makanan khas berbahan ikan?', ['Cakalang fufu', 'Mangut', 'Arsik', 'Gabus pucung'], ['Rendang', 'Sate Madura'], 'Cakalang fufu, mangut, arsik, dan gabus pucung berbahan ikan.', 'Rendang dan sate Madura berbahan daging.'),
        ('Manakah olahan berbahan susu?', ['Dadiah', 'Dangke', 'Yoghurt'], ['Telur asin', 'Kerak telor'], 'Dadiah, dangke, dan yoghurt merupakan olahan susu.', 'Telur asin dan kerak telor berbahan telur.'),
        ('Manakah teknik pengawetan pangan hewani?', ['Pembekuan', 'Pengasapan', 'Fermentasi', 'Pengasinan'], ['Pembakaran langsung', 'Penyimpanan di tempat terbuka'], 'Pangan hewani diawetkan dengan pembekuan, pengasapan, fermentasi, dan pengasinan.', 'Pembakaran dan penyimpanan terbuka bukan pengawetan.'),
        ('Manakah unsur label menurut UU No. 18 Tahun 2012?', ['Nama produk', 'Berat bersih', 'Informasi halal', 'Nomor izin edar'], ['Nomor rekening pribadi', 'Nama sekolah'], 'Label memuat nama produk, berat bersih, informasi halal, dan nomor izin edar.', 'Data pribadi tidak termasuk.'),
        ('Manakah fungsi kemasan?', ['Melindungi produk', 'Sarana promosi', 'Memberi nilai estetika'], ['Mempercepat pembusukan', 'Menambah cemaran'], 'Kemasan melindungi produk serta berfungsi promosi dan estetika.', 'Kemasan justru mencegah cemaran.'),
        ('Manakah tahap kegiatan promosi?', ['Menentukan tujuan promosi', 'Menentukan target pasar', 'Menentukan anggaran', 'Memilih media promosi'], ['Menghindari evaluasi', 'Menaikkan harga tanpa alasan'], 'Promosi dimulai dari tujuan, target pasar, anggaran, dan media.', 'Efektivitas promosi tetap diukur.'),
    ],
    'pairs': [
        ('Daging', 'sekitar 75 persen air dan 18 persen protein'),
        ('Ikan', 'protein mudah diserap tubuh'),
        ('Susu', 'cairan dari kelenjar mamalia'),
        ('Telur', 'bahan hewani selain daging, ikan, dan susu'),
        ('Cakalang fufu', 'pengasapan khas Manado'),
        ('Dadiah', 'fermentasi susu kerbau khas Minang'),
        ('Telur asin', 'pengasinan khas Brebes'),
        ('Kemasan', 'pelindung produk dari cemaran'),
    ],
    'steps': [
        ('Urutkan langkah membuat sosis solo.', ['Buat kulit dadar tipis', 'Rebus dan suwir daging ayam', 'Tumis bumbu hingga harum', 'Isi kulit dan bentuk', 'Rekatkan ujung dengan putih telur', 'Simpan di freezer'], 'Sosis solo dibuat dari kulit dadar dan isi ayam berbumbu.', 'Ujung kulit direkatkan dengan putih telur.'),
        ('Urutkan langkah membuat cakalang fufu.', ['Bersihkan ikan', 'Belah ikan dan jepit dengan bambu', 'Susun ikan di tempat pengasapan', 'Bakar tempurung kelapa menjadi arang', 'Sebar bara sekitar 4 jam'], 'Cakalang fufu dibuat dengan membersihkan lalu mengasapi ikan.', 'Pengasapan berlangsung sekitar 4 jam.'),
        ('Urutkan langkah membuat dadiah.', ['Masukkan susu kerbau ke bambu tiga per empat', 'Tutup bambu dengan daun atau plastik', 'Simpan pada suhu ruang', 'Tunggu 1–3 hari hingga menggumpal', 'Dadiah siap disimpan atau disajikan'], 'Dadiah difermentasi dalam bambu pada suhu ruang.', 'Fermentasi memanfaatkan bakteri baik dari bambu.'),
        ('Urutkan langkah membuat telur asin.', ['Pilih dan bersihkan telur', 'Amplas permukaan telur', 'Buat adonan abu dan garam 2:1', 'Balut telur dengan adonan', 'Peram 1–2 minggu', 'Cuci dan rebus sekitar 45 menit'], 'Telur asin dibuat dengan membalut adonan lalu memeramnya.', 'Pemeraman berlangsung 1–2 minggu.'),
        ('Urutkan langkah promosi produk.', ['Tentukan tujuan promosi', 'Tentukan target pasar dan harga jual', 'Tentukan anggaran promosi', 'Pilih media promosi', 'Ukur efektivitas promosi'], 'Promosi dimulai dari tujuan lalu diakhiri pengukuran.', 'Efektivitas perlu diukur agar promosi dapat diperbaiki.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
