"""PRA 8 — Budi Daya Tanaman Pangan dan Pemanfaatan Limbahnya (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 8',
    'slug': 'prakarya-8-budi-daya-tanaman-pangan',
    'title': 'Budi Daya Tanaman Pangan dan Pemanfaatan Limbahnya',
    'description': (
        'Mengenal jenis dan karakteristik tanaman pangan, teknik budi daya sorgum, '
        'pemanfaatan limbah menjadi kompos, pakan, dan biogas, serta analisis usaha.'
    ),
    'objectives': [
        'Mendeskripsikan budi daya tanaman pangan dan jenis-jenisnya.',
        'Mengidentifikasi alat, bahan, dan teknik budi daya tanaman pangan.',
        'Menyusun rencana budi daya tanaman pangan sesuai potensi lokal.',
        'Mempraktikkan budi daya sorgum dari penanaman sampai panen.',
        'Menganalisis usaha dan memanfaatkan limbah budi daya secara ekonomis.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Budi-Daya-BG-KLS-X.pdf Unit I Budi Daya Tanaman Pangan dan Pemanfaatan Limbahnya',
    'glossary': [
        {'term': 'Tanaman pangan', 'definition': 'Tanaman yang menjadi sumber utama karbohidrat dan protein bagi manusia.'},
        {'term': 'Serealia', 'definition': 'Kelompok rumput-rumputan yang dipanen bijinya, seperti padi, jagung, dan sorgum.'},
        {'term': 'Kacang-kacangan', 'definition': 'Kelompok tanaman famili Leguminoseae yang dipanen biji dalam polong.'},
        {'term': 'Umbi-umbian', 'definition': 'Kelompok tanaman yang bagian umbinya dipanen, seperti ubi kayu dan ubi jalar.'},
        {'term': 'Limbah budi daya', 'definition': 'Bagian tanaman yang tidak dipanen, misalnya akar, batang, cabang, dan daun.'},
        {'term': 'Kompos', 'definition': 'Pupuk organik hasil pelapukan limbah oleh mikroorganisme.'},
        {'term': 'Silase', 'definition': 'Pakan hijauan hasil fermentasi untuk ternak.'},
        {'term': 'BEP', 'definition': 'Titik impas, yaitu jumlah penjualan yang menutup seluruh biaya usaha.'},
    ],
    'intro': {
        'material_title': 'Mengapa tanaman pangan penting?',
        'title': 'Sumber pangan dari lahan sendiri',
        'paragraphs': [
            'Tanaman pangan adalah segala jenis tanaman yang menjadi sumber utama karbohidrat dan protein untuk kebutuhan tubuh manusia. Tanaman ini juga mengandung lemak, vitamin, dan mineral dalam jumlah kecil. Bagi banyak keluarga petani, tanaman pangan menjadi sumber mata pencaharian.',
            'Indonesia kaya akan jenis tanaman pangan. Padi, jagung, sorgum, kedelai, kacang tanah, kacang hijau, ubi kayu, dan ubi jalar termasuk komoditi unggulan nasional. Talas, garut, dan gembili menjadi komoditi unggulan daerah.',
            'Budi daya tanaman pangan tidak berhenti pada panen. Batang, daun, dan bagian yang tidak dipanen dapat diolah menjadi kompos, biogas, atau pakan ternak sehingga bernilai ekonomi dan mengurangi pencemaran.',
        ],
        'diagram': (
            'Alur budi daya tanaman pangan',
            'flowchart LR\n'
            '  A[Perencanaan] --> B[Pengolahan lahan]\n'
            '  B --> C[Penanaman]\n'
            '  C --> D[Pemeliharaan]\n'
            '  D --> E[Panen]\n'
            '  E --> F[Pascapanen]\n'
            '  F --> G[Pemanfaatan limbah]',
        ),
        'callout': 'Gunakan sarung tangan dan masker saat memupuk atau menyemprot pestisida. Cuci tangan setelah bekerja di lahan.',
        'checkpoint': (
            'Apa kandungan utama tanaman pangan bagi tubuh manusia?',
            [
                ('Karbohidrat dan protein', True),
                ('Air dan udara', False),
                ('Logam dan plastik', False),
                ('Pewarna dan pengawet', False),
            ],
            'Tanaman pangan menjadi sumber utama karbohidrat dan protein.',
        ),
    },
    'concept': {
        'material_title': 'Jenis tanaman dan pemanfaatan limbah',
        'title': 'Mengelompokkan tanaman pangan',
        'paragraphs': [
            'Berdasarkan umurnya, tanaman pangan dibedakan menjadi tanaman semusim dan tanaman tahunan. Padi, jagung, dan sorgum berumur 3–4 bulan, sedangkan ubi kayu dan ubi jalar sekitar 4–8 bulan. Sukun dan sagu termasuk tanaman tahunan karena tumbuh lebih dari dua tahun.',
            'Dalam budi dayanya, tanaman pangan dikelompokkan menjadi serealia, kacang-kacangan, dan umbi-umbian. Serealia seperti padi, jagung, dan sorgum dipanen bijinya. Kacang-kacangan seperti kedelai, kacang tanah, dan kacang hijau dipanen biji dalam polong. Umbi-umbian dipanen bagian umbinya.',
            'Padi, sorgum, dan kacang-kacangan menyerbuk sendiri, sedangkan jagung menyerbuk silang. Limbah budi daya berupa akar, batang, cabang, dan daun dapat diolah menjadi pupuk organik, biogas, atau pakan ternak seperti jerami dan silase.',
        ],
        'table': [
            ['Kelompok', 'Ciri', 'Contoh'],
            ['Serealia', 'Rumput-rumputan, dipanen bijinya', 'Padi, jagung, sorgum'],
            ['Kacang-kacangan', 'Biji dalam polong', 'Kedelai, kacang tanah, kacang hijau'],
            ['Umbi-umbian', 'Bagian umbi dipanen', 'Ubi kayu, ubi jalar, talas'],
            ['Tanaman tahunan', 'Tumbuh lebih dari 2 tahun', 'Sukun, sagu'],
        ],
        'visual': chart_block(
            'pra-8-umur-panen',
            'Perkiraan umur panen tanaman pangan (hari)',
            'bar',
            [('Sorgum', 100), ('Jagung', 110), ('Padi', 120), ('Ubi jalar', 150)],
        ),
        'activity': categorize_block(
            'pra-8-klasifikasi',
            'Kelompokkan tanaman berikut ke dalam serealia, kacang-kacangan, atau umbi-umbian.',
            [('b1', 'Serealia'), ('b2', 'Kacang-kacangan'), ('b3', 'Umbi-umbian')],
            [
                ('i1', 'Padi', 'b1'),
                ('i2', 'Sorgum', 'b1'),
                ('i3', 'Kedelai', 'b2'),
                ('i4', 'Kacang tanah', 'b2'),
                ('i5', 'Ubi kayu', 'b3'),
                ('i6', 'Ubi jalar', 'b3'),
            ],
            'Tepat. Padi dan sorgum serealia; kedelai dan kacang tanah kacang-kacangan; ubi kayu dan ubi jalar umbi-umbian.',
            'Periksa lagi: lihat bagian tanaman yang dipanen.',
        ),
        'subtitle': 'Limbah bernilai ekonomi',
        'list': [
            'Kompos meningkatkan kesuburan tanah dan mengurangi pupuk anorganik.',
            'Biogas dihasilkan dari fermentasi limbah bercampur kotoran ternak.',
            'Jerami dan daun sorgum dapat menjadi pakan ternak atau silase.',
            'Pemanfaatan limbah mengurangi biaya produksi dan pencemaran lingkungan.',
        ],
        'checkpoint': (
            'Hijauan hasil fermentasi untuk pakan ternak disebut…',
            [
                ('Silase', True),
                ('Kompos', False),
                ('Biogas', False),
                ('BEP', False),
            ],
            'Silase adalah pakan hijauan yang difermentasikan terlebih dahulu.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Budi daya sorgum dari tanam sampai panen',
        'paragraphs': [
            'Sorgum dipilih karena dapat dimanfaatkan sebagai pangan, pakan, dan bioenergi. Gunakan benih varietas unggul seperti Samurai, Bioguma, atau Agritan Super 6. Olah lahan dengan cangkul dan garpu hingga gembur, lalu tambahkan kapur bila tanah terlalu asam.',
            'Buat lubang tanam dengan jarak 75 cm × 20 cm dan kedalaman sekitar 5 cm. Tanam dua benih per lubang, lalu lakukan penyulaman lima hari setelah tanam. Beri pupuk dasar pada 1 MST dan pupuk susulan pada 5 MST dengan dosis Urea 200 kg/ha, SP-36 100 kg/ha, dan KCl 100 kg/ha.',
            'Panen dilakukan saat biji mengeras dan muncul black layer. Potong tangkai malai, angin-anginkan 3–4 hari, lalu rontokkan biji. Batang dan daun diolah menjadi pakan ternak. Hitung biaya produksi dan keuntungan dengan rumus A = B − C − D.',
        ],
        'scenario': scenario(
            'pra-8-skenario',
            'Lahan sekolah yang sempit',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Sekolah memiliki lahan sempit dan tanah agak asam. Tanaman pangan apa yang paling tepat dicoba?',
                    'choices': [
                        {'text': 'Sorgum karena adaptif dan bernilai ekonomi', 'next': 'n2', 'score': 2, 'feedback': 'Sorgum dapat tumbuh di lahan kering dan punya banyak manfaat.'},
                        {'text': 'Padi sawah karena butuh banyak air', 'next': 'n3', 'score': 0, 'feedback': 'Lahan sempit dan kering kurang cocok untuk padi sawah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Tanaman terserang kutu daun. Apa tindakan yang tepat?',
                    'choices': [
                        {'text': 'Mengendalikan hama sesuai kebutuhan dan dosis', 'next': 'n4', 'score': 2, 'feedback': 'Pengendalian tepat menjaga tanaman dan lingkungan.'},
                        {'text': 'Menyemprot pestisida sebanyak mungkin', 'next': 'n3', 'score': 0, 'feedback': 'Dosis berlebihan merusak tanaman dan lingkungan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tanaman gagal tumbuh dan biaya membengkak.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Sorgum panen dan limbahnya bernilai ekonomi.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu tanaman pangan?', 'back': 'Tanaman sumber utama karbohidrat dan protein.'},
            {'front': 'Sebutkan tiga kelompok tanaman pangan.', 'back': 'Serealia, kacang-kacangan, dan umbi-umbian.'},
            {'front': 'Apa manfaat kompos?', 'back': 'Meningkatkan kesuburan tanah dan mengurangi pupuk anorganik.'},
            {'front': 'Apa rumus keuntungan usaha?', 'back': 'A = B − C − D, yaitu pendapatan dikurangi penyusutan dan biaya produksi.'},
        ],
        'checkpoint': (
            'Ciri sorgum siap panen adalah…',
            [
                ('Biji mengeras dan muncul black layer', True),
                ('Daun berwarna biru', False),
                ('Batang berisi air', False),
                ('Malai belum keluar', False),
            ],
            'Sorgum siap panen saat biji mengeras dan terbentuk black layer.',
        ),
        'challenge': challenge_block(
            'pra-8-tantangan',
            'Tantangan istilah tanaman pangan',
            90,
            [
                ('Sumber karbohidrat dan protein', 'tanaman pangan'),
                ('Kelompok rumput-rumputan', 'serealia'),
                ('Biji dalam polong', 'kacang-kacangan'),
                ('Pupuk dari pelapukan limbah', 'kompos'),
                ('Titik impas usaha', 'BEP'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Tanaman pangan menjadi sumber utama…', 'Karbohidrat dan protein', ['Air dan udara', 'Logam dan plastik', 'Pewarna dan pengawet'], 'Tanaman pangan adalah sumber utama karbohidrat dan protein.', 'Juga mengandung lemak, vitamin, dan mineral.'),
        ('Kelompok tanaman rumput-rumputan yang dipanen bijinya disebut…', 'Serealia', ['Kacang-kacangan', 'Umbi-umbian', 'Tanaman tahunan'], 'Serealia termasuk Gramineae atau rumput-rumputan.', 'Contohnya padi dan sorgum.'),
        ('Tanaman famili Leguminoseae yang dipanen biji dalam polong disebut…', 'Kacang-kacangan', ['Serealia', 'Umbi-umbian', 'Tanaman tahunan'], 'Kacang-kacangan termasuk famili Leguminoseae.', 'Contohnya kedelai dan kacang hijau.'),
        ('Manakah contoh serealia?', 'Padi, jagung, dan sorgum', ['Kedelai, kacang tanah, kacang hijau', 'Ubi kayu dan ubi jalar', 'Sukun dan sagu'], 'Padi, jagung, dan sorgum termasuk serealia.', 'Bagian yang dipanen adalah biji.'),
        ('Manakah contoh kacang-kacangan?', 'Kedelai, kacang tanah, kacang hijau', ['Padi, jagung, sorgum', 'Ubi kayu, ubi jalar, talas', 'Sukun, sagu, kelapa'], 'Kedelai, kacang tanah, dan kacang hijau termasuk kacang-kacangan.', 'Biji berada dalam polong.'),
        ('Tanaman yang menyerbuk silang adalah…', 'Jagung', ['Padi', 'Sorgum', 'Kacang hijau'], 'Jagung adalah contoh tanaman menyerbuk silang.', 'Padi dan sorgum menyerbuk sendiri.'),
        ('Manakah contoh tanaman tahunan?', 'Sukun dan sagu', ['Padi dan jagung', 'Sorgum dan kedelai', 'Kacang tanah dan kacang hijau'], 'Sukun dan sagu tumbuh lebih dari dua tahun.', 'Tanaman semusim berumur beberapa bulan.'),
        ('Umur tanaman padi, jagung, dan sorgum sekitar…', '3–4 bulan', ['1–2 minggu', '4–8 bulan', 'Lebih dari 2 tahun'], 'Padi, jagung, dan sorgum berumur semusim 3–4 bulan.', 'Ubi kayu dan ubi jalar 4–8 bulan.'),
        ('Limbah tanaman pangan yang mengalami pelapukan menjadi…', 'Kompos', ['Biogas', 'Silase', 'Pestisida'], 'Limbah yang melapuk berubah menjadi kompos.', 'Kompos menyuburkan tanah.'),
        ('Hijauan hasil fermentasi untuk pakan ternak disebut…', 'Silase', ['Kompos', 'Biogas', 'Pupuk cair'], 'Silase dibuat dengan fermentasi hijauan.', 'Contohnya daun dan batang sorgum.'),
        ('Manakah varietas unggul sorgum?', 'Samurai, Bioguma, Agritan Super 6', ['IR64, Ciherang, Inpari', 'Bisi 18, Pioneer 32', 'Kentang Granola, Atlantik'], 'Buku menyebut Samurai, Bioguma, dan Agritan Super 6.', 'Benih dapat dibeli di toko pertanian.'),
        ('Jarak tanam sorgum yang dianjurkan adalah…', '75 cm × 20 cm', ['25 cm × 25 cm', '50 cm × 50 cm', '100 cm × 100 cm'], 'Lubang tanam dibuat dengan jarak 75 cm × 20 cm.', 'Kedalaman lubang sekitar 5 cm.'),
        ('Ciri sorgum siap panen adalah…', 'Biji mengeras dan muncul black layer', ['Daun berwarna biru', 'Batang berongga', 'Malai masih hijau'], 'Biji yang mengeras dengan black layer menandakan siap panen.', 'Malai dipotong lalu diangin-anginkan.'),
        ('Rumus keuntungan usaha budi daya adalah…', 'A = B − C − D', ['A = B + C + D', 'A = B × C × D', 'A = B ÷ C ÷ D'], 'Keuntungan adalah pendapatan dikurangi penyusutan dan biaya produksi.', 'B adalah pendapatan hasil penjualan.'),
    ],
    'multi': [
        ('Manakah komoditi unggulan nasional tanaman pangan?', ['Padi', 'Jagung', 'Sorgum'], ['Talas', 'Gembili'], 'Padi, jagung, dan sorgum termasuk komoditi unggulan nasional.', 'Talas dan gembili komoditi unggulan daerah.'),
        ('Manakah kelompok tanaman pangan dalam budi daya?', ['Serealia', 'Kacang-kacangan', 'Umbi-umbian'], ['Tanaman hias', 'Tanaman obat'], 'Buku mengelompokkan tanaman pangan menjadi serealia, kacang-kacangan, dan umbi-umbian.', 'Tanaman hias dan obat bukan kelompok tersebut.'),
        ('Manakah pemanfaatan limbah budi daya tanaman?', ['Pupuk organik', 'Biogas', 'Pakan ternak'], ['Dibuang ke sungai', 'Dibakar sembarangan'], 'Limbah dapat menjadi pupuk, biogas, dan pakan ternak.', 'Membuang ke sungai mencemari lingkungan.'),
        ('Manakah kegiatan pascapanen?', ['Penjemuran', 'Penyortiran', 'Pencucian'], ['Penanaman', 'Penyiangan'], 'Pascapanen meliputi penjemuran, pencucian, dan penyortiran.', 'Penanaman dan penyiangan sebelum panen.'),
        ('Manakah ciri sorgum siap panen?', ['Biji mengeras', 'Muncul black layer'], ['Biji masih lunak', 'Malai belum keluar'], 'Biji keras dan black layer menandakan siap panen.', 'Panen dilakukan dengan memotong tangkai malai.'),
        ('Manakah alat budi daya tanaman pangan?', ['Cangkul', 'Garpu', 'Tugal'], ['Solder', 'Aerator'], 'Cangkul, garpu, dan tugal dipakai dalam budi daya tanaman.', 'Solder dan aerator dipakai pada Budikdamber.'),
        ('Manakah faktor keberhasilan budi daya?', ['Benih unggul', 'Pemupukan tepat'], ['Benih asal-asalan', 'Hama dibiarkan'], 'Benih unggul dan pemupukan tepat meningkatkan hasil.', 'Hama perlu dikendalikan.'),
        ('Manakah tahap budi daya tanaman pangan?', ['Pengolahan lahan', 'Penanaman', 'Pemeliharaan', 'Panen'], ['Menghindari perencanaan', 'Membuang limbah ke sungai'], 'Budi daya melalui pengolahan lahan, penanaman, pemeliharaan, dan panen.', 'Perencanaan tetap penting.'),
    ],
    'pairs': [
        ('Tanaman pangan', 'sumber karbohidrat dan protein'),
        ('Serealia', 'biji dari rumput-rumputan'),
        ('Kacang-kacangan', 'biji yang berada dalam polong'),
        ('Umbi-umbian', 'bagian umbi yang dipanen'),
        ('Kompos', 'pupuk dari pelapukan limbah'),
        ('Silase', 'hijauan fermentasi untuk pakan'),
        ('BEP', 'titik impas usaha'),
        ('Sorgum', 'tanaman pangan serbaguna'),
    ],
    'steps': [
        ('Urutkan alur budi daya tanaman pangan.', ['Perencanaan', 'Pengolahan lahan', 'Penanaman', 'Pemeliharaan', 'Panen dan pascapanen'], 'Budi daya bergerak dari perencanaan menuju panen.', 'Perencanaan mendahului pengolahan lahan.'),
        ('Urutkan langkah budi daya sorgum.', ['Siapkan benih unggul', 'Olah lahan', 'Buat lubang tanam', 'Tanam dua benih per lubang', 'Pupuk dan pelihara', 'Panen'], 'Budi daya sorgum dimulai dari benih lalu penanaman.', 'Penyulaman dilakukan lima hari setelah tanam.'),
        ('Urutkan langkah membuat kompos.', ['Kumpulkan limbah organik', 'Cacah bahan', 'Campur dengan bahan pemacu', 'Tumpuk dan tutup', 'Balik berkala hingga matang'], 'Kompos dibuat dari pencampuran lalu pemeraman.', 'Pembalikan mempercepat pematangan.'),
        ('Urutkan langkah pascapanen sorgum.', ['Potong tangkai malai', 'Angin-anginkan 3–4 hari', 'Rontokkan biji', 'Sosoh bila perlu', 'Simpan dalam kemasan tertutup'], 'Pascapanen dimulai dari pemotongan malai.', 'Pengeringan mencegah kerusakan.'),
        ('Urutkan langkah analisis usaha.', ['Catat biaya investasi', 'Hitung biaya produksi', 'Hitung pendapatan', 'Tentukan BEP', 'Nilai keuntungan'], 'Analisis usaha bergerak dari biaya menuju keuntungan.', 'BEP menunjukkan titik impas.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
