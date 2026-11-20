"""PRA 9 — Budikdamber dan Pemanfaatan Limbahnya (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 9',
    'slug': 'prakarya-9-budikdamber',
    'title': 'Budikdamber dan Pemanfaatan Limbahnya',
    'description': (
        'Mengenal Budikdamber (budi daya ikan dan sayuran dalam ember): '
        'jenis ikan dan sayuran, alat dan bahan, perakitan ember, pemeliharaan, '
        'pemanenan, dan analisis usaha.'
    ),
    'objectives': [
        'Mengeksplorasi Budikdamber dan pemanfaatan limbahnya.',
        'Mengidentifikasi jenis ikan dan sayuran yang cocok untuk Budikdamber.',
        'Merencanakan serta menyiapkan alat dan bahan Budikdamber.',
        'Membuat, memelihara, dan memanen hasil Budikdamber.',
        'Menganalisis usaha Budikdamber secara sederhana.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Budi-Daya-BG-KLS-X.pdf Unit II Budikdamber dan Pemanfaatan Limbahnya',
    'glossary': [
        {'term': 'Budikdamber', 'definition': 'Budi daya ikan dan sayuran dalam ember dalam satu sistem.'},
        {'term': 'Aerator', 'definition': 'Alat yang memasok oksigen ke dalam air budi daya ikan.'},
        {'term': 'EM4', 'definition': 'Probiotik yang merangsang pertumbuhan bakteri baik di air.'},
        {'term': 'Probiotik', 'definition': 'Mikroorganisme bermanfaat yang membantu menjaga kualitas air dan kesehatan ikan.'},
        {'term': 'Kanibal', 'definition': 'Sifat ikan yang memakan sesamanya, misalnya pada lele.'},
        {'term': 'Benih', 'definition': 'Ikan atau tanaman muda yang siap ditebar atau ditanam.'},
        {'term': 'Limbah Budikdamber', 'definition': 'Sisa air dan kotoran ikan yang mengandung hara bagi tanaman.'},
        {'term': 'BEP', 'definition': 'Titik impas, yaitu jumlah penjualan yang menutup seluruh biaya usaha.'},
    ],
    'intro': {
        'material_title': 'Mengapa Budikdamber cocok untuk lahan sempit?',
        'title': 'Ikan dan sayur dalam satu ember',
        'paragraphs': [
            'Budikdamber adalah singkatan dari budi daya ikan dan sayuran dalam ember. Sistem ini menggabungkan pemeliharaan ikan dengan penanaman sayuran pada gelas plastik yang diletakkan di atas ember. Air kolam yang mengandung hara dimanfaatkan tanaman untuk tumbuh.',
            'Limbah budi daya ikan mengandung nitrogen, fosfor, dan senyawa lain dengan pH sekitar 7–8. Unsur hara tersebut sebenarnya dapat dimanfaatkan tanaman, sehingga Budikdamber mengubah limbah menjadi manfaat.',
            'Budikdamber tidak memerlukan lahan luas dan modal besar. Kegiatan ini cocok dilakukan di rumah, sekolah, atau pekarangan sempit, serta dapat menjadi sumber penghasilan tambahan bagi keluarga.',
        ],
        'diagram': (
            'Alur kerja Budikdamber',
            'flowchart LR\n'
            '  A[Ikan diberi pakan] --> B[Kotoran dan sisa pakan larut]\n'
            '  B --> C[Air kaya hara]\n'
            '  C --> D[Akar sayuran menyerap hara]\n'
            '  D --> E[Air kembali bersih]\n'
            '  E --> F[Ikan dan sayur dipanen]',
        ),
        'callout': 'Gunakan ember yang kuat dan tidak bocor. Jauhkan sambungan listrik aerator dari air dan periksa selang secara berkala.',
        'checkpoint': (
            'Apa kepanjangan Budikdamber?',
            [
                ('Budi Daya Ikan dan Sayuran dalam Ember', True),
                ('Budi Daya Ikan dan Sayuran dalam Bak', False),
                ('Budidaya Ikan dan Sayuran di Sawah', False),
                ('Budi Daya Tanaman dan Ikan di Kolam', False),
            ],
            'Budikdamber adalah budi daya ikan dan sayuran dalam ember.',
        ),
    },
    'concept': {
        'material_title': 'Ikan, sayuran, dan komponen ember',
        'title': 'Memilih ikan dan menyiapkan ember',
        'paragraphs': [
            'Tidak semua ikan cocok untuk Budikdamber. Ikan yang dipilih harus tahan terhadap kadar oksigen rendah, seperti lele, nila, mas, patin, dan gurame. Lele mudah dipelihara, omnivora, dan dapat dipanen pada usia 3–4 bulan, tetapi bersifat kanibal sehingga perlu pengaturan kepadatan.',
            'Sayuran yang umum ditanam adalah kangkung, selada, bayam, sawi, dan pakcoy. Kangkung dan bayam dapat dipanen pada 20–25 hari, sedangkan sawi dan pakcoy sekitar 25–30 hari. Pilih sayuran yang sesuai dengan potensi lokal dan sinar matahari.',
            'Ember berkapasitas 60–80 liter diisi air sekitar 80 persen atau 60 liter. Tutup ember dilubangi untuk gelas plastik 250 ml, lalu gelas diisi arang batok kelapa sebagai media tanam. Tambahkan EM4 sebagai probiotik dan diamkan dua hari sebelum menebar benih.',
        ],
        'table': [
            ['Komponen', 'Fungsi', 'Catatan'],
            ['Ember 60–80 L', 'Wadah air dan ikan', 'Isi air sekitar 80%'],
            ['Gelas plastik 250 ml', 'Media tanam sayuran', 'Lubangi sisi dan bawah'],
            ['Arang batok kelapa', 'Media tanam', 'Isi seperempat gelas'],
            ['Aerator', 'Memasok oksigen', 'Dianjurkan bila ikan padat'],
            ['EM4', 'Probiotik', 'Diamkan dua hari sebelum tebar benih'],
        ],
        'visual': chart_block(
            'pra-9-umur-panen',
            'Perkiraan umur panen sayuran Budikdamber (hari)',
            'bar',
            [('Kangkung', 22), ('Bayam', 25), ('Sawi', 28), ('Pakcoy', 30)],
        ),
        'activity': categorize_block(
            'pra-9-klasifikasi',
            'Kelompokkan berikut ke dalam ikan Budikdamber atau sayuran Budikdamber.',
            [('b1', 'Ikan'), ('b2', 'Sayuran')],
            [
                ('i1', 'Lele', 'b1'),
                ('i2', 'Nila', 'b1'),
                ('i3', 'Patin', 'b1'),
                ('i4', 'Kangkung', 'b2'),
                ('i5', 'Sawi', 'b2'),
                ('i6', 'Pakcoy', 'b2'),
            ],
            'Tepat. Lele, nila, dan patin adalah ikan; kangkung, sawi, dan pakcoy adalah sayuran.',
            'Periksa lagi: ikan hidup di air, sayuran ditanam di gelas media.',
        ),
        'subtitle': 'Pemeliharaan dan keselamatan',
        'list': [
            'Beri pakan secara teratur dan jangan berlebihan agar air tidak memburuk.',
            'Periksa kualitas air dan bersihkan kotoran yang mengendap.',
            'Gunakan aerator bila kepadatan ikan tinggi atau cuaca panas.',
            'Letakkan ember di tempat yang mendapat sinar matahari cukup dan aman dari jangkauan anak kecil.',
        ],
        'checkpoint': (
            'Mengapa lele perlu diatur kepadatannya dalam Budikdamber?',
            [
                ('Karena lele bersifat kanibal', True),
                ('Karena lele tidak tahan air', False),
                ('Karena lele tidak mau makan', False),
                ('Karena lele hidup di darat', False),
            ],
            'Lele bersifat kanibal sehingga kepadatan perlu diatur agar tidak saling memakan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merakit dan merawat Budikdamber',
        'paragraphs': [
            'Siapkan ember 60–80 liter, solder, gelas plastik 250 ml, tang, dan aerator. Lubangi tutup ember dan gelas, lalu pasang kait kawat sepanjang 12 cm agar gelas menggantung di tepi ember. Isi gelas dengan arang batok kelapa seperempat bagian.',
            'Isi ember dengan air sekitar 60 liter, tambahkan EM4, dan diamkan dua hari. Semai benih sayuran, lalu tanam semaian pada arang di dalam gelas. Tebar benih ikan lele atau nila berukuran 5–12 cm sebanyak 60–100 ekor.',
            'Rawat dengan memberi pakan teratur dan menjaga air tetap bersih. Amati pertumbuhan ikan dan sayuran setiap hari. Setelah 20–30 hari sayuran dapat dipanen, sedangkan ikan dipanen pada usia 3–4 bulan. Catat biaya dan hasil untuk analisis usaha.',
        ],
        'scenario': scenario(
            'pra-9-skenario',
            'Budikdamber di halaman sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Halaman sekolah sempit dan panas. Apa pilihan budi daya yang paling sesuai?',
                    'choices': [
                        {'text': 'Budikdamber dengan ember dan aerator', 'next': 'n2', 'score': 2, 'feedback': 'Budikdamber cocok untuk lahan sempit dan dapat memakai aerator.'},
                        {'text': 'Membuat kolam besar', 'next': 'n3', 'score': 0, 'feedback': 'Kolam besar membutuhkan lahan dan biaya lebih banyak.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Air ember mulai keruh dan berbau. Apa tindakanmu?',
                    'choices': [
                        {'text': 'Mengurangi pakan dan memeriksa kualitas air', 'next': 'n4', 'score': 2, 'feedback': 'Pakan berlebih membuat air memburuk.'},
                        {'text': 'Menambah pakan agar ikan cepat besar', 'next': 'n3', 'score': 0, 'feedback': 'Pakan berlebih memperparah kualitas air.'},
                    ],
                },
                {'id': 'n3', 'text': 'Ikan mati dan sayuran ikut rusak.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Air kembali jernih dan panen berhasil.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu Budikdamber?', 'back': 'Budi daya ikan dan sayuran dalam ember.'},
            {'front': 'Ikan apa yang tahan oksigen rendah?', 'back': 'Lele, nila, mas, patin, dan gurame.'},
            {'front': 'Berapa lama air didiamkan setelah diberi EM4?', 'back': 'Dua hari.'},
            {'front': 'Apa fungsi aerator?', 'back': 'Memasok oksigen ke dalam air.'},
        ],
        'checkpoint': (
            'Agar air Budikdamber tidak cepat memburuk, pemberian pakan harus…',
            [
                ('Teratur dan tidak berlebihan', True),
                ('Sebanyak mungkin setiap saat', False),
                ('Dihentikan selamanya', False),
                ('Diberikan hanya sekali seumur hidup', False),
            ],
            'Pakan yang berlebihan membusuk dan menurunkan kualitas air.',
        ),
        'challenge': challenge_block(
            'pra-9-tantangan',
            'Tantangan istilah Budikdamber',
            90,
            [
                ('Ikan dan sayur dalam ember', 'budikdamber'),
                ('Pemasok oksigen air', 'aerator'),
                ('Probiotik untuk air', 'EM4'),
                ('Ikan tahan oksigen rendah', 'lele'),
                ('Titik impas usaha', 'BEP'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa kepanjangan Budikdamber?', 'Budi Daya Ikan dan Sayuran dalam Ember', ['Budi Daya Ikan dan Sayuran dalam Bak', 'Budidaya Ikan dan Sayuran di Sawah', 'Budi Daya Tanaman dan Ikan di Kolam'], 'Budikdamber adalah budi daya ikan dan sayuran dalam ember.', 'Singkatannya berasal dari kata budi daya, ikan, dan ember.'),
        ('Kapasitas ember yang dianjurkan untuk Budikdamber adalah…', '60–80 liter', ['5–10 liter', '200–300 liter', '1.000 liter'], 'Ember yang dipakai berkapasitas 60–80 liter.', 'Ada juga yang memakai ember 15 liter.'),
        ('Air dalam ember Budikdamber diisi sebanyak…', 'Sekitar 80 persen', ['10 persen', '30 persen', 'Penuh sampai tumpah'], 'Ember diisi air sebanyak 80 persen dari kapasitas.', 'Biasanya sekitar 60 liter.'),
        ('Ikan yang tahan terhadap kadar oksigen rendah adalah…', 'Lele', ['Nila', 'Mas', 'Gurame'], 'Lele termasuk ikan yang tahan kadar oksigen rendah.', 'Lele juga omnivora dan mudah dirawat.'),
        ('Ikan yang membutuhkan tambahan aerator karena butuh banyak oksigen adalah…', 'Nila', ['Lele', 'Patin', 'Betok'], 'Nila membutuhkan pasokan oksigen cukup tinggi.', 'Ikan mas juga memerlukan aerator.'),
        ('Ikan yang bersifat kanibal sehingga kepadatannya perlu diatur adalah…', 'Lele', ['Nila', 'Patin', 'Gurame'], 'Lele mempunyai sifat kanibal.', 'Kepadatan terlalu tinggi membuat ikan saling memakan.'),
        ('Umur panen ikan lele dalam Budikdamber sekitar…', '3–4 bulan', ['1 minggu', '1 tahun', '5 tahun'], 'Lele dapat dipanen pada usia 3–4 bulan.', 'Patin juga sekitar 3–4 bulan.'),
        ('Sayuran yang dapat dipanen pada 20–25 hari adalah…', 'Kangkung dan bayam', ['Sawi dan pakcoy', 'Padi dan jagung', 'Tomat dan cabai'], 'Kangkung dan bayam berumur panen 20–25 hari.', 'Sawi dan pakcoy 25–30 hari.'),
        ('Sayuran yang dapat dipanen pada 25–30 hari adalah…', 'Sawi dan pakcoy', ['Kangkung dan bayam', 'Padi dan sorgum', 'Kedelai dan kacang tanah'], 'Sawi dan pakcoy dipanen setelah 25–30 hari.', 'Keduanya cocok untuk Budikdamber.'),
        ('Media tanam yang diletakkan di dalam gelas Budikdamber adalah…', 'Arang batok kelapa', ['Tanah liat', 'Pasir besi', 'Semen'], 'Gelas diisi arang batok kelapa sebagai media tanam.', 'Arang kayu juga dapat dipakai.'),
        ('Bahan yang ditambahkan ke air sebagai probiotik adalah…', 'EM4', ['Pestisida', 'Pupuk urea', 'Garam dapur'], 'EM4 adalah probiotik yang merangsang bakteri baik.', 'EM4 membantu menjaga kualitas air.'),
        ('Setelah diberi EM4, air didiamkan selama…', 'Dua hari', ['Dua jam', 'Dua minggu', 'Dua bulan'], 'Air yang diberi EM4 didiamkan dua hari sebelum ditebar benih.', 'Tujuannya memberi waktu bakteri bekerja.'),
        ('Jumlah benih ikan yang ditebar untuk ember 80 liter sekitar…', '60–100 ekor', ['5–10 ekor', '500–1.000 ekor', '2–3 ekor'], 'Benih ikan berukuran 5–12 cm ditebar 60–100 ekor.', 'Sesuaikan dengan kapasitas ember.'),
        ('Keunggulan utama Budikdamber adalah…', 'Tidak memerlukan lahan luas', ['Memerlukan lahan sangat luas', 'Modalnya sangat besar', 'Hanya bisa dilakukan di sawah'], 'Budikdamber tidak memerlukan lahan luas dan modal besar.', 'Cocok untuk pekarangan sempit.'),
    ],
    'multi': [
        ('Manakah keunggulan Budikdamber?', ['Tidak perlu lahan luas', 'Modal relatif kecil', 'Mudah dilakukan'], ['Wajib memakai lahan sawah', 'Memerlukan modal sangat besar'], 'Budikdamber hemat lahan, modal kecil, dan mudah dilakukan.', 'Tidak memerlukan sawah.'),
        ('Manakah ikan yang cocok untuk Budikdamber?', ['Lele', 'Nila', 'Patin'], ['Hiu', 'Paus'], 'Lele, nila, dan patin cocok untuk Budikdamber.', 'Hiu dan paus bukan ikan budi daya.'),
        ('Manakah sayuran yang cocok untuk Budikdamber?', ['Kangkung', 'Sawi', 'Pakcoy'], ['Jagung', 'Padi'], 'Kangkung, sawi, dan pakcoy cocok ditanam di Budikdamber.', 'Jagung dan padi bukan tanaman Budikdamber.'),
        ('Manakah alat yang dipakai membuat Budikdamber?', ['Ember', 'Solder', 'Gelas plastik'], ['Cangkul', 'Traktor'], 'Ember, solder, dan gelas plastik dipakai membuat Budikdamber.', 'Cangkul dan traktor untuk lahan.'),
        ('Manakah bahan Budikdamber?', ['Arang batok kelapa', 'Kawat', 'EM4'], ['Semen', 'Bata merah'], 'Arang batok, kawat, dan EM4 termasuk bahan Budikdamber.', 'Semen dan bata bukan bahan utamanya.'),
        ('Unsur yang terkandung dalam limbah air budi daya ikan adalah…', ['Nitrogen', 'Fosfor'], ['Plastik', 'Logam berat'], 'Limbah air kolam mengandung nitrogen dan fosfor.', 'Unsur itu dimanfaatkan tanaman.'),
        ('Manakah tindakan perawatan Budikdamber?', ['Memberi pakan teratur', 'Menjaga kualitas air'], ['Membiarkan air kotor', 'Menabur pestisida ke air'], 'Pakan teratur dan air bersih menjaga ikan serta sayuran.', 'Air kotor memicu penyakit.'),
        ('Manakah tahap Budikdamber?', ['Persiapan ember', 'Penebaran benih', 'Pemeliharaan', 'Panen'], ['Menghindari perencanaan', 'Membuang limbah ke sungai'], 'Budikdamber melalui persiapan, penebaran, pemeliharaan, dan panen.', 'Perencanaan tetap diperlukan.'),
    ],
    'pairs': [
        ('Budikdamber', 'budi daya ikan dan sayuran dalam ember'),
        ('Aerator', 'pemasok oksigen ke air'),
        ('EM4', 'probiotik untuk kualitas air'),
        ('Arang batok kelapa', 'media tanam sayuran'),
        ('Lele', 'ikan tahan oksigen rendah'),
        ('Kangkung', 'sayuran panen 20–25 hari'),
        ('Pakcoy', 'sayuran panen 25–30 hari'),
        ('BEP', 'titik impas usaha'),
    ],
    'steps': [
        ('Urutkan langkah membuat ember Budikdamber.', ['Lubangi tutup ember', 'Lubangi gelas plastik', 'Pasang kait kawat', 'Isi gelas dengan arang', 'Isi ember dengan air dan EM4'], 'Pembuatan dimulai dari pelubangan lalu pengisian media.', 'Air didiamkan dua hari sebelum ditebar benih.'),
        ('Urutkan langkah menyemai dan menanam sayuran.', ['Semai benih sayuran', 'Tunggu benih tumbuh', 'Pindahkan semaian ke gelas', 'Letakkan gelas di tepi ember'], 'Sayuran disemai lebih dahulu lalu dipindah ke gelas.', 'Media arang menjaga akar tetap lembap.'),
        ('Urutkan langkah memelihara Budikdamber.', ['Beri pakan teratur', 'Periksa kualitas air', 'Bersihkan kotoran', 'Amati pertumbuhan ikan dan sayur'], 'Pemeliharaan dimulai dari pakan lalu pemeriksaan air.', 'Jangan memberi pakan berlebihan.'),
        ('Urutkan langkah panen Budikdamber.', ['Panen sayuran lebih dahulu', 'Periksa ukuran ikan', 'Panen ikan sesuai umur', 'Catat hasil panen'], 'Sayuran dipanen lebih cepat daripada ikan.', 'Ikan dipanen pada usia 3–4 bulan.'),
        ('Urutkan langkah analisis usaha Budikdamber.', ['Catat biaya alat dan bahan', 'Hitung biaya pakan', 'Hitung hasil penjualan', 'Tentukan BEP', 'Nilai keuntungan'], 'Analisis usaha bergerak dari biaya menuju keuntungan.', 'BEP menunjukkan titik impas.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
