"""PRA 11 — Bahan Pangan Nabati: Lebih Sehat dan Ramah Lingkungan (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 11',
    'slug': 'prakarya-11-bahan-pangan-nabati',
    'title': 'Bahan Pangan Nabati: Lebih Sehat dan Ramah Lingkungan',
    'description': (
        'Mengenal buah, sayuran, serealia, kacang-kacangan, dan umbi-umbian, '
        'teknik pengawetan fisika, biologis, dan kimiawi, makanan khas Nusantara, '
        'desain kemasan dan label, serta perhitungan harga jual dan BEP.'
    ),
    'objectives': [
        'Mengeksplorasi produk olahan pangan higienis Nusantara dari bahan nabati.',
        'Menganalisis karakteristik bahan, alat, teknik, dan prosedur pengolahan pangan nabati.',
        'Mengembangkan desain produk dan kemasan olahan pangan nabati.',
        'Merancang pemasaran dan analisis usaha produk pangan nabati secara sederhana.',
        'Membuat, mengemas, dan mempromosikan produk olahan pangan nabati Nusantara.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Pengolahan-BG-KLS-X.pdf Unit 1 Bahan Pangan Nabati: Lebih Sehat dan Ramah Lingkungan',
    'glossary': [
        {'term': 'Bahan pangan nabati', 'definition': 'Bahan pangan yang berasal dari tumbuhan, seperti buah, sayur, serealia, kacang, dan umbi.'},
        {'term': 'Serealia', 'definition': 'Bahan pangan dari biji-bijian yang menjadi sumber makanan pokok.'},
        {'term': 'Kacang-kacangan', 'definition': 'Bahan pangan biji berukuran lebih besar dari serealia yang kaya protein dan lemak sehat.'},
        {'term': 'Umbi-umbian', 'definition': 'Bahan pangan dengan bagian umbi yang kaya karbohidrat atau pati.'},
        {'term': 'Pengawetan', 'definition': 'Cara membuat makanan memiliki daya simpan lama serta mempertahankan sifat fisik dan kimianya.'},
        {'term': 'Fermentasi', 'definition': 'Pengawetan biologis dengan peragian yang mengubah karbohidrat menjadi alkohol atau asam.'},
        {'term': 'BTM', 'definition': 'Bahan tambahan makanan yang dipakai pada pengawetan kimiawi sesuai takaran.'},
        {'term': 'BEP', 'definition': 'Titik impas, yaitu keadaan usaha tidak laba dan tidak rugi.'},
    ],
    'intro': {
        'material_title': 'Mengapa bahan pangan nabati penting?',
        'title': 'Kekayaan pangan dari tumbuhan',
        'paragraphs': [
            'Bahan pangan nabati berasal dari tumbuhan dan memiliki karakteristik yang berbeda satu dengan lainnya. Buah-buahan memiliki rasa enak dan menyegarkan serta kaya serat, vitamin A, vitamin B, vitamin B1, vitamin B6, dan vitamin C. Contohnya pisang, jeruk, apel, dan pepaya.',
            'Sayuran mengandung zat gizi lengkap berupa vitamin, mineral, serat, kalsium, zat besi, folat, dan kalium. Contohnya kangkung, selada, terong, kol, dan buncis. Serealia berasal dari biji-bijian dan menjadi sumber makanan pokok karena kaya karbohidrat, protein, serat, serta vitamin E dan B.',
            'Kacang-kacangan memiliki biji lebih besar dari serealia dan kaya serat, protein, lemak sehat, mineral, serta vitamin E. Umbi-umbian menjadi sumber karbohidrat atau pati, vitamin, protein, mineral, zat besi, fosfor, kalsium, dan serat. Semua kelompok ini menjadi bahan utama olahan pangan higienis Nusantara.',
        ],
        'diagram': (
            'Lima kelompok bahan pangan nabati',
            'flowchart TB\n'
            '  A[Bahan pangan nabati] --> B[Buah-buahan]\n'
            '  A --> C[Sayuran]\n'
            '  A --> D[Serealia]\n'
            '  A --> E[Kacang-kacangan]\n'
            '  A --> F[Umbi-umbian]',
        ),
        'callout': 'Cuci bahan pangan dengan air mengalir sebelum diolah. Gunakan celemek dan sarung tangan saat memotong bahan agar aman dari goresan pisau.',
        'checkpoint': (
            'Kelompok bahan pangan nabati yang kaya serat serta vitamin A, B, dan C adalah…',
            [
                ('Buah-buahan', True),
                ('Serealia', False),
                ('Umbi-umbian', False),
                ('Kacang-kacangan', False),
            ],
            'Buah-buahan kaya serat, vitamin A, vitamin B, vitamin B1, vitamin B6, dan vitamin C.',
        ),
    },
    'concept': {
        'material_title': 'Jenis bahan dan teknik pengawetan',
        'title': 'Mengawetkan pangan nabati',
        'paragraphs': [
            'Pengawetan makanan adalah cara membuat makanan memiliki daya simpan lama dan mempertahankan sifat fisik serta kimianya. Teknik pengawetan fisika meliputi pemanasan, pembekuan, pengalengan, pembuatan acar, pengentalan, pengeringan, dan pembuatan tepung. Pemanasan susu cukup pada suhu 60–70 °C selama sekitar 30 menit karena proteinnya mudah rusak.',
            'Pengawetan biologis dilakukan dengan peragian atau fermentasi dan penambahan enzim. Papain adalah enzim dari buah pepaya, sedangkan bromelin adalah enzim dari buah nanas. Pengawetan kimiawi memakai bahan tambahan makanan atau BTM yang harus sesuai takaran, baik pada bahan cair nonminyak maupun yang mengandung minyak.',
            'Kearifan lokal memperkaya pilihan bahan. Ubi Cilembu dari Desa Cilembu, Kabupaten Sumedang, Jawa Barat, memiliki rasa manis seperti madu dan aroma mirip mentega. Rasa itu hanya muncul bila ditanam di tanah Cilembu. Makanan khas Nusantara juga beragam, seperti bika ambon dari Medan berbahan terigu dan kerak telor dari Jakarta berbahan beras ketan.',
        ],
        'table': [
            ['Teknik', 'Cara', 'Contoh'],
            ['Pemanasan', 'Memanaskan pada suhu tertentu', 'Susu 60–70 °C'],
            ['Pembekuan', 'Menurunkan suhu di bawah titik beku air', 'Sayuran frozen'],
            ['Pengalengan', 'Wadah tertutup rapat dan steril', 'Manisan buah kaleng'],
            ['Pembuatan acar', 'Garam dan cuka', 'Acar mentimun'],
            ['Pengentalan', 'Mengentalkan bahan cair', 'Dodol'],
            ['Pengeringan', 'Mengurangi kadar air', 'Keripik'],
            ['Pembuatan tepung', 'Mengubah bahan menjadi bubuk', 'Tepung beras'],
        ],
        'visual': chart_block(
            'pra-11-kadar-air',
            'Perkiraan kadar air beberapa bahan pangan nabati (%)',
            'bar',
            [('Buah', 85), ('Sayuran', 90), ('Umbi', 70), ('Serealia kering', 12)],
        ),
        'activity': categorize_block(
            'pra-11-klasifikasi',
            'Kelompokkan bahan berikut ke dalam buah, sayuran, serealia, kacang-kacangan, atau umbi-umbian.',
            [('b1', 'Buah'), ('b2', 'Sayuran'), ('b3', 'Serealia'), ('b4', 'Kacang-kacangan'), ('b5', 'Umbi-umbian')],
            [
                ('i1', 'Pisang', 'b1'),
                ('i2', 'Kangkung', 'b2'),
                ('i3', 'Beras', 'b3'),
                ('i4', 'Kedelai', 'b4'),
                ('i5', 'Singkong', 'b5'),
                ('i6', 'Kentang', 'b5'),
            ],
            'Tepat. Pisang buah; kangkung sayuran; beras serealia; kedelai kacang-kacangan; singkong dan kentang umbi-umbian.',
            'Periksa lagi: lihat bagian tumbuhan yang dimanfaatkan.',
        ),
        'subtitle': 'Kemasan, label, dan harga jual',
        'list': [
            'Kemasan yang baik melindungi isi, mudah dibuka dan ditutup, bentuknya menarik, labelnya jelas, serta ramah lingkungan.',
            'Bahan kemasan meliputi logam atau kaleng, kaca, plastik, dan kertas atau karton.',
            'Label memuat nama produk, merek, komposisi, berat bersih, nama dan alamat produsen, nomor PIRT atau MD, tanggal kadaluarsa, dan kode produksi.',
            'Harga jual ditentukan dengan mempertimbangkan pelanggan, pesaing, dan biaya produksi.',
        ],
        'checkpoint': (
            'Pengawetan susu dengan pemanasan cukup dilakukan pada suhu…',
            [
                ('60–70 °C', True),
                ('100–120 °C', False),
                ('150–180 °C', False),
                ('200–250 °C', False),
            ],
            'Susu dipanaskan pada suhu 60–70 °C selama sekitar 30 menit agar proteinnya tidak rusak.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat dodol dan menghitung BEP',
        'paragraphs': [
            'Dodol adalah makanan khas Indonesia yang hampir dimiliki setiap daerah. Bahan dasarnya tepung beras, ketan, santan, dan gula merah. Pengawetannya alami melalui pengentalan dan penambahan gula. Dodol memiliki rasa manis legit dengan warna dan tekstur kental, sedangkan pembungkus, perisa, dan namanya berbeda antar daerah.',
            'Untuk membuat dodol, campurkan 250 gram tepung ketan putih dan 150 gram tepung ketan hitam, lalu masukkan agar-agar. Masak 400 gram gula merah, 2 lembar pandan, dan 400 ml santan hingga larut, saring, lalu campurkan bahan kering. Aduk terus sekitar 50 menit sampai warna agak gelap dan tidak lengket di teflon. Tuang, ratakan, potong, dan taburi wijen sangrai.',
            'Sebagai alternatif, buat sirup buah pala dari 750 gram buah pala matang, 750 ml air, 500 gram gula pasir, dan ¼ sendok teh citrun zuur. Setelah produk siap, tentukan harga jual dengan mempertimbangkan pelanggan, pesaing, dan biaya produksi. Hitung BEP produksi dengan membagi total biaya dengan harga penjualan, lalu hitung BEP harga dengan membagi total biaya dengan harga produksi.',
        ],
        'scenario': scenario(
            'pra-11-skenario',
            'Dodol sekolah yang tidak tahan lama',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Dodol buatan kelompokmu cepat berjamur. Apa langkah yang paling tepat?',
                    'choices': [
                        {'text': 'Memperbaiki proses pengentalan dan kadar gula', 'next': 'n2', 'score': 2, 'feedback': 'Pengentalan dan gula membantu menurunkan kadar air sehingga dodol lebih awet.'},
                        {'text': 'Menambah air agar dodol lebih lembut', 'next': 'n3', 'score': 0, 'feedback': 'Air berlebih mempercepat pertumbuhan mikroorganisme.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Dodol sudah awet, tetapi kemasannya mudah rusak saat diangkut. Apa solusinya?',
                    'choices': [
                        {'text': 'Memilih kemasan yang melindungi isi dan mudah dibawa', 'next': 'n4', 'score': 2, 'feedback': 'Kemasan harus melindungi produk, mudah dibuka, dan mudah dibawa.'},
                        {'text': 'Membungkus dengan kertas tipis tanpa label', 'next': 'n3', 'score': 0, 'feedback': 'Kemasan tipis tidak melindungi produk dan tanpa label sulit dikenali.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk rusak dan tidak layak dijual.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Dodol awet, kemasan menarik, dan usaha untung.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan lima kelompok bahan pangan nabati.', 'back': 'Buah, sayuran, serealia, kacang-kacangan, dan umbi-umbian.'},
            {'front': 'Apa enzim dari pepaya dan nanas?', 'back': 'Papain dari pepaya dan bromelin dari nanas.'},
            {'front': 'Apa rumus BEP produksi?', 'back': 'Total biaya dibagi harga penjualan.'},
            {'front': 'Apa saja isi label produk?', 'back': 'Nama produk, merek, komposisi, berat bersih, produsen, nomor PIRT/MD, kadaluarsa, dan kode produksi.'},
        ],
        'checkpoint': (
            'BEP produksi dihitung dengan cara…',
            [
                ('Total biaya dibagi harga penjualan', True),
                ('Harga penjualan dibagi total biaya', False),
                ('Total biaya dikali harga produksi', False),
                ('Laba dibagi jumlah karyawan', False),
            ],
            'BEP produksi = total biaya ÷ harga penjualan.',
        ),
        'challenge': challenge_block(
            'pra-11-tantangan',
            'Tantangan istilah pangan nabati',
            90,
            [
                ('Bahan pangan dari biji-bijian', 'serealia'),
                ('Bahan pangan dari bagian umbi', 'umbi-umbian'),
                ('Enzim dari buah pepaya', 'papain'),
                ('Enzim dari buah nanas', 'bromelin'),
                ('Titik impas usaha', 'BEP'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Kelompok bahan pangan nabati yang kaya serat serta vitamin A, B, dan C adalah…', 'Buah-buahan', ['Serealia', 'Umbi-umbian', 'Kacang-kacangan'], 'Buah-buahan kaya serat, vitamin A, vitamin B, vitamin B1, vitamin B6, dan vitamin C.', 'Rasanya enak dan menyegarkan.'),
        ('Serealia merupakan bahan pangan yang berasal dari…', 'Biji-bijian', ['Umbi', 'Daun', 'Bunga'], 'Serealia berasal dari biji-bijian dan menjadi sumber makanan pokok.', 'Contohnya beras dan gandum.'),
        ('Kandungan utama umbi-umbian adalah…', 'Karbohidrat atau pati', ['Protein hewani', 'Lemak jenuh', 'Garam mineral'], 'Umbi-umbian memiliki kandungan utama karbohidrat atau pati.', 'Juga mengandung vitamin dan serat.'),
        ('Manakah contoh serealia?', 'Beras, sorgum, barley, jagung, gandum', ['Kacang tanah, kacang hijau, kedelai', 'Bengkoang, singkong, talas', 'Pisang, jeruk, apel'], 'Beras, sorgum, barley, jagung, dan gandum termasuk serealia.', 'Bagian yang dimanfaatkan adalah bijinya.'),
        ('Manakah contoh kacang-kacangan?', 'Kacang tanah, kacang merah, kacang hijau, kedelai', ['Beras, jagung, gandum', 'Singkong, talas, kentang', 'Kangkung, selada, kol'], 'Kacang tanah, kacang merah, kacang hijau, dan kedelai termasuk kacang-kacangan.', 'Ukuran bijinya lebih besar dari serealia.'),
        ('Ubi Cilembu berasal dari daerah…', 'Desa Cilembu, Kabupaten Sumedang, Jawa Barat', ['Desa Cilembu, Kalimantan Timur', 'Desa Cilembu, Papua', 'Desa Cilembu, Sulawesi Utara'], 'Ubi Cilembu berasal dari Desa Cilembu, Kabupaten Sumedang, Jawa Barat.', 'Rasanya manis seperti madu.'),
        ('Pemanasan susu pada pengawetan fisika dilakukan pada suhu…', '60–70 °C', ['30–40 °C', '90–100 °C', '150–160 °C'], 'Susu dipanaskan pada suhu 60–70 °C selama sekitar 30 menit.', 'Protein susu mudah rusak pada suhu tinggi.'),
        ('Pengawetan dengan menurunkan suhu hingga di bawah titik beku air disebut…', 'Pembekuan', ['Pemanasan', 'Pengeringan', 'Pengentalan'], 'Pembekuan menurunkan suhu bahan hingga di bawah titik beku air.', 'Contohnya sayuran frozen.'),
        ('Pengawetan sayur atau buah dengan garam dan cuka disebut…', 'Pembuatan acar', ['Pengalengan', 'Pengentalan', 'Pembuatan tepung'], 'Acar dibuat dengan pemberian garam dan cuka pada sayur atau buah.', 'Contohnya acar mentimun.'),
        ('Enzim yang berasal dari buah pepaya adalah…', 'Papain', ['Bromelin', 'Amilase', 'Lipase'], 'Papain adalah enzim dari buah pepaya.', 'Dipakai pada pengawetan biologis.'),
        ('Enzim yang berasal dari buah nanas adalah…', 'Bromelin', ['Papain', 'Pepsin', 'Renin'], 'Bromelin adalah enzim dari buah nanas.', 'Dipakai pada pengawetan biologis.'),
        ('Makanan khas Jakarta yang berbahan dasar beras ketan adalah…', 'Kerak telor', ['Bika ambon', 'Pisang ijo', 'Kalumpe'], 'Kerak telor berasal dari Jakarta dan berbahan beras ketan.', 'Bika ambon dari Medan berbahan terigu.'),
        ('BEP produksi dihitung dengan rumus…', 'Total biaya ÷ harga penjualan', ['Harga penjualan ÷ total biaya', 'Total biaya × harga produksi', 'Laba ÷ beban usaha'], 'BEP produksi = total biaya dibagi harga penjualan.', 'BEP menunjukkan titik impas.'),
        ('Kemasan yang tahan terhadap asam dan basa serta tidak bereaksi dengan bahan adalah…', 'Kemasan kaca', ['Kemasan plastik', 'Kemasan kertas', 'Kemasan daun'], 'Kemasan kaca tahan terhadap produk asam dan basa serta tidak bereaksi.', 'Namun mudah pecah bila terbentur.'),
    ],
    'multi': [
        ('Manakah yang termasuk buah-buahan?', ['Pisang', 'Jeruk', 'Pepaya'], ['Kangkung', 'Bayam'], 'Pisang, jeruk, dan pepaya termasuk buah-buahan.', 'Kangkung dan bayam termasuk sayuran.'),
        ('Manakah yang termasuk sayuran?', ['Kangkung', 'Selada', 'Terong'], ['Beras', 'Gandum'], 'Kangkung, selada, dan terong termasuk sayuran.', 'Beras dan gandum termasuk serealia.'),
        ('Manakah contoh serealia?', ['Beras', 'Jagung', 'Gandum'], ['Kentang', 'Talas'], 'Beras, jagung, dan gandum termasuk serealia.', 'Kentang dan talas termasuk umbi-umbian.'),
        ('Manakah teknik pengawetan secara fisika?', ['Pemanasan', 'Pembekuan', 'Pengeringan'], ['Fermentasi', 'Pengasinan'], 'Pemanasan, pembekuan, dan pengeringan termasuk pengawetan fisika.', 'Fermentasi biologis dan pengasinan kimiawi.'),
        ('Manakah contoh kacang-kacangan?', ['Kacang tanah', 'Kacang hijau', 'Kedelai'], ['Ubi jalar', 'Singkong'], 'Kacang tanah, kacang hijau, dan kedelai termasuk kacang-kacangan.', 'Ubi jalar dan singkong umbi-umbian.'),
        ('Manakah teknik pengawetan secara biologis?', ['Fermentasi', 'Penambahan enzim papain', 'Penambahan enzim bromelin'], ['Pengalengan', 'Pembekuan'], 'Pengawetan biologis memakai fermentasi atau penambahan enzim.', 'Pengalengan dan pembekuan termasuk fisika.'),
        ('Manakah bahan kemasan yang disebut dalam materi?', ['Logam atau kaleng', 'Kaca', 'Plastik', 'Kertas atau karton'], ['Kayu jati', 'Semen'], 'Bahan kemasan meliputi logam, kaca, plastik, serta kertas atau karton.', 'Kayu jati dan semen bukan bahan kemasan pangan.'),
        ('Manakah unsur yang sebaiknya tertera pada label?', ['Nama produk', 'Komposisi produk', 'Tanggal kadaluarsa', 'Nomor PIRT atau MD'], ['Nomor telepon pribadi', 'Alamat rumah tetangga'], 'Label memuat nama produk, komposisi, kadaluarsa, dan nomor PIRT atau MD.', 'Data pribadi yang tidak relevan tidak dicantumkan.'),
    ],
    'pairs': [
        ('Buah-buahan', 'kaya serat dan vitamin C'),
        ('Serealia', 'sumber makanan pokok dari biji-bijian'),
        ('Kacang-kacangan', 'biji berukuran lebih besar dari serealia'),
        ('Umbi-umbian', 'sumber karbohidrat atau pati'),
        ('Papain', 'enzim dari buah pepaya'),
        ('Bromelin', 'enzim dari buah nanas'),
        ('Pengalengan', 'wadah tertutup rapat dan steril'),
        ('BEP', 'titik impas usaha'),
    ],
    'steps': [
        ('Urutkan langkah membuat dodol.', ['Campur tepung ketan dan agar-agar', 'Masak gula merah, pandan, dan santan', 'Saring larutan gula', 'Campur bahan kering dan aduk', 'Masak sekitar 50 menit hingga tidak lengket', 'Tuang, ratakan, dan potong'], 'Dodol dimasak dari larutan gula lalu diaduk hingga kental.', 'Adonan diaduk terus agar tidak menggumpal.'),
        ('Urutkan langkah membuat sirup buah pala.', ['Cuci buah pala', 'Pisahkan biji dan cincang daging buah', 'Blender dengan air', 'Tuang ke panci dan tambah gula', 'Rebus hingga mendidih', 'Saring dan dinginkan'], 'Sirup dibuat dari buah pala yang diblender lalu direbus.', 'Buah dibersihkan sebelum diolah.'),
        ('Urutkan proses pengalengan.', ['Siapkan bahan dan wadah', 'Masukkan bahan ke wadah', 'Tutup wadah rapat', 'Sterilkan dengan panas', 'Dinginkan dan simpan'], 'Pengalengan menutup rapat bahan lalu mensterilkannya.', 'Wadah harus tertutup rapat.'),
        ('Urutkan langkah membuat acar.', ['Cuci sayur atau buah', 'Potong sesuai selera', 'Campur garam dan cuka', 'Masukkan ke wadah tertutup', 'Diamkan hingga meresap'], 'Acar dibuat dengan garam dan cuka lalu didiamkan.', 'Wadah harus bersih dan tertutup.'),
        ('Urutkan langkah menentukan harga jual.', ['Hitung biaya produksi', 'Perhatikan daya beli pelanggan', 'Bandingkan harga pesaing', 'Tetapkan harga jual', 'Hitung BEP'], 'Harga jual ditetapkan setelah biaya dan pasar diketahui.', 'BEP menguji kelayakan usaha.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
