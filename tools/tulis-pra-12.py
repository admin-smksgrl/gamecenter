"""PRA 12 — Wangi Alami dengan Produk Nabati (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 12',
    'slug': 'prakarya-12-wangi-alami-produk-nabati',
    'title': 'Wangi Alami dengan Produk Nabati',
    'description': (
        'Mengolah bahan nabati menjadi produk nonpangan seperti kosmetik, '
        'perawatan tubuh, dan aromaterapi kopi, serta menyusun kemasan, promosi, '
        'dan analisis usaha dengan SWOT.'
    ),
    'objectives': [
        'Mengeksplorasi produk olahan nonpangan dari bahan nabati yang bernilai ekonomis.',
        'Menganalisis karakteristik bahan, alat, teknik, dan prosedur pengolahan nonpangan nabati.',
        'Mengembangkan desain produk dan kemasan nonpangan nabati.',
        'Merancang pemasaran dan analisis usaha produk nonpangan nabati secara sederhana.',
        'Membuat, mengemas, dan mempromosikan produk nonpangan nabati.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Pengolahan-BG-KLS-X.pdf Unit 2 Wangi Alami dengan Produk Nabati',
    'glossary': [
        {'term': 'Produk nonpangan nabati', 'definition': 'Produk dari bahan tumbuhan yang bukan untuk dimakan, misalnya kosmetik dan perawatan tubuh.'},
        {'term': 'Aromaterapi', 'definition': 'Terapi atau pengharum ruangan yang memanfaatkan aroma bahan alami.'},
        {'term': 'SWOT', 'definition': 'Analisis kekuatan, kelemahan, peluang, dan ancaman sebuah usaha.'},
        {'term': 'Biaya tetap', 'definition': 'Biaya yang jumlahnya tidak bergantung pada jumlah produksi, seperti gaji dan sewa.'},
        {'term': 'Biaya variabel', 'definition': 'Biaya yang berubah mengikuti kegiatan produksi, seperti bahan baku dan lembur.'},
        {'term': 'HPP', 'definition': 'Harga pokok penjualan, yaitu dasar untuk menentukan harga jual produk.'},
        {'term': 'Laba bersih', 'definition': 'Laba kotor dikurangi beban usaha.'},
        {'term': 'Penjualan bersih', 'definition': 'Penjualan kotor setelah dikurangi retur, potongan, dan pengurangan harga.'},
    ],
    'intro': {
        'material_title': 'Mengapa bahan nabati bisa menjadi produk nonpangan?',
        'title': 'Kecantikan alami dari buah dan sayur',
        'paragraphs': [
            'Produk nonpangan berbahan nabati banyak memanfaatkan khasiat buah dan sayuran sebagai bahan kosmetik atau produk perawatan tubuh yang menghasilkan kecantikan alami. Produk ini tidak membuat iritasi kulit dan dapat dipakai untuk semua jenis kulit. Nenek moyang kita sudah memakai buah dan sayur sebagai rahasia kecantikan.',
            'Beberapa khasiat bahan nabati antara lain bengkuang sebagai pencerah wajah, alpukat untuk melembapkan kulit, pisang untuk menghaluskan kulit wajah bahkan menghilangkan bekas cacar atau jerawat, serta lidah aloe yang mendinginkan kulit dan mencegah kerontokan rambut.',
            'Teknologi modern mengadaptasi khasiat itu, terutama melalui pengeringan bahan nabati. Setelah kering, bahan nabati lebih mudah diolah menjadi banyak variasi. Diperlukan ketekunan dan ketelitian agar produk yang dihasilkan baik dan bermanfaat.',
        ],
        'diagram': (
            'Dari bahan nabati menjadi produk nonpangan',
            'flowchart LR\n'
            '  A[Buah dan sayur] --> B[Pengeringan]\n'
            '  B --> C[Ekstraksi atau pencampuran]\n'
            '  C --> D[Produk nonpangan]\n'
            '  D --> E[Kemasan dan label]\n'
            '  E --> F[Promosi dan penjualan]',
        ),
        'callout': 'Lakukan uji kecil pada kulit sebelum memakai produk perawatan tubuh buatan sendiri. Hentikan pemakaian bila timbul gatal atau kemerahan.',
        'checkpoint': (
            'Bahan nabati yang bermanfaat sebagai pencerah wajah adalah…',
            [
                ('Bengkuang', True),
                ('Alpukat', False),
                ('Pisang', False),
                ('Lidah buaya', False),
            ],
            'Bengkuang bermanfaat sebagai pencerah wajah, sedangkan alpukat melembapkan kulit.',
        ),
    },
    'concept': {
        'material_title': 'Pemanfaatan kopi dan bagian padi',
        'title': 'Wangi alami dan nilai tambah',
        'paragraphs': [
            'Kopi merupakan komoditas perkebunan bernilai ekonomi tinggi dan menjadi sumber penghasilan bagi masyarakat di daerah penghasil kopi. Perkembangan kopi di Indonesia naik sejak tahun 2007 seiring perluasan pasar hingga mancanegara. Kopi juga menjadi sumber daya alam yang menghasilkan devisa negara.',
            'Selain diseduh, kopi dimanfaatkan sebagai pengharum ruangan karena aromanya menghilangkan bau tidak sedap, mengusir serangga, mengilapkan furnitur kayu, membersihkan noda, dan ampasnya menjadi pupuk tanaman. Aromaterapi kopi dibuat dari lilin kecil, sumbu lilin, gelas kaca, dan kopi bubuk.',
            'Bagian padi juga dapat dimanfaatkan. Beras menjadi makanan pokok dan dapat diolah menjadi bahan kosmetik, sekam menjadi media tanam, batang dan daun kering menjadi bahan bakar tungku, serta dedak menjadi pakan ternak. Pemanfaatan ini mengurangi limbah dan menambah nilai ekonomi.',
        ],
        'table': [
            ['Bahan', 'Manfaat nonpangan'],
            ['Bengkuang', 'Pencerah wajah'],
            ['Alpukat', 'Pelembap kulit'],
            ['Pisang', 'Penghalus kulit wajah'],
            ['Lidah buaya', 'Pendingin kulit dan pencegah kerontokan rambut'],
            ['Kopi', 'Pengharum ruangan dan aromaterapi'],
            ['Sekam padi', 'Media tanam'],
            ['Dedak padi', 'Pakan ternak'],
        ],
        'visual': chart_block(
            'pra-12-pemanfaatan-kopi',
            'Lima pemanfaatan kopi dan ampasnya',
            'bar',
            [('Pengharum ruangan', 5), ('Mengusir serangga', 4), ('Mengilapkan furnitur', 3), ('Membersihkan noda', 3), ('Pupuk tanaman', 4)],
        ),
        'activity': categorize_block(
            'pra-12-klasifikasi',
            'Kelompokkan bahan berikut sesuai manfaat nonpangannya.',
            [('b1', 'Perawatan kulit'), ('b2', 'Pengharum dan kebersihan'), ('b3', 'Pemanfaatan limbah padi')],
            [
                ('i1', 'Bengkuang', 'b1'),
                ('i2', 'Alpukat', 'b1'),
                ('i3', 'Kopi bubuk', 'b2'),
                ('i4', 'Ampas kopi', 'b2'),
                ('i5', 'Sekam padi', 'b3'),
                ('i6', 'Dedak padi', 'b3'),
            ],
            'Tepat. Bengkuang dan alpukat untuk perawatan kulit; kopi untuk pengharum dan kebersihan; sekam serta dedak berasal dari limbah padi.',
            'Periksa lagi: cocokkan bahan dengan manfaat yang disebut buku.',
        ),
        'subtitle': 'Analisis usaha dengan SWOT',
        'list': [
            'Analisis usaha memperlihatkan kelayakan usaha dan dipengaruhi faktor internal serta eksternal.',
            'Faktor internal meliputi proses produksi, penentuan harga, dan bahan baku.',
            'Faktor eksternal meliputi pemasaran, distribusi, geopolitik, dan lain-lain.',
            'SWOT berarti strengths, weaknesses, opportunities, dan threats.',
            'Target pasar dapat dikategorikan berdasarkan rentang umur, pekerjaan, dan minat.',
        ],
        'checkpoint': (
            'SWOT adalah singkatan dari…',
            [
                ('Strengths, weaknesses, opportunities, threats', True),
                ('Sales, wages, orders, taxes', False),
                ('Strength, work, output, time', False),
                ('Supply, warehouse, owner, transport', False),
            ],
            'SWOT berarti kekuatan, kelemahan, peluang, dan ancaman.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat aromaterapi kopi dan laporan usaha',
        'paragraphs': [
            'Untuk membuat aromaterapi kopi, iris tipis lilin lalu lelehkan di tempat tahan panas atau di atas api kecil. Letakkan sumbu di dalam gelas kaca, tuang sedikit lilin cair, lalu tuang kopi bubuk. Ulangi berselang-seling hingga gelas penuh, kemudian nyalakan sumbu saat digunakan.',
            'Kemasan perlu didesain agar bentuk dan penampilannya indah serta menarik. Produsen sebaiknya mengurangi berat kemasan agar anggaran transportasi dan harga jual ikut turun. Kemasan juga harus melindungi produk, mudah dibuka dan ditutup, serta labelnya jelas.',
            'Susun laporan usaha dengan mencatat pendapatan, biaya tetap seperti gaji dan sewa, serta biaya variabel seperti bahan baku dan lembur. Laba bersih dihitung dari laba kotor dikurangi beban usaha. Penjualan bersih adalah penjualan setelah dikurangi retur, potongan, dan pengurangan harga.',
        ],
        'scenario': scenario(
            'pra-12-skenario',
            'Aromaterapi kopi di bazar sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kelompokmu ingin menjual aromaterapi kopi. Langkah awal apa yang tepat?',
                    'choices': [
                        {'text': 'Menentukan target pasar dan menghitung biaya produksi', 'next': 'n2', 'score': 2, 'feedback': 'Target pasar dan biaya produksi menjadi dasar harga jual.'},
                        {'text': 'Langsung menetapkan harga paling mahal', 'next': 'n3', 'score': 0, 'feedback': 'Harga tanpa perhitungan membuat produk sulit bersaing.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Produk sudah jadi, tetapi kemasannya berat dan mudah rusak. Apa tindakanmu?',
                    'choices': [
                        {'text': 'Memilih kemasan ringan yang tetap melindungi produk', 'next': 'n4', 'score': 2, 'feedback': 'Kemasan ringan menghemat transportasi dan tetap melindungi produk.'},
                        {'text': 'Menambah lapisan semen agar kokoh', 'next': 'n3', 'score': 0, 'feedback': 'Semen membuat kemasan berat dan tidak sesuai untuk produk.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk tidak laku dan usaha merugi.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk diminati dan usaha memperoleh laba.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa khasiat pisang untuk kulit?', 'back': 'Menghaluskan kulit wajah dan menghilangkan bekas cacar atau jerawat.'},
            {'front': 'Apa bahan aromaterapi kopi?', 'back': 'Lilin kecil, sumbu lilin, gelas kaca, dan kopi bubuk.'},
            {'front': 'Apa itu SWOT?', 'back': 'Kekuatan, kelemahan, peluang, dan ancaman.'},
            {'front': 'Apa rumus laba bersih?', 'back': 'Laba kotor dikurangi beban usaha.'},
        ],
        'checkpoint': (
            'Rumus laba bersih adalah…',
            [
                ('Laba kotor – beban usaha', True),
                ('Laba kotor + beban usaha', False),
                ('Penjualan + retur', False),
                ('Biaya tetap × biaya variabel', False),
            ],
            'Laba bersih diperoleh dari laba kotor dikurangi beban usaha.',
        ),
        'challenge': challenge_block(
            'pra-12-tantangan',
            'Tantangan istilah produk nabati',
            90,
            [
                ('Pencerah wajah alami', 'bengkuang'),
                ('Pelembap kulit alami', 'alpukat'),
                ('Analisis kekuatan dan kelemahan usaha', 'SWOT'),
                ('Harga pokok penjualan', 'HPP'),
                ('Penjualan setelah dikurangi retur', 'penjualan bersih'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Produk nonpangan nabati banyak memanfaatkan khasiat…', 'Buah dan sayuran', ['Daging dan ikan', 'Susu dan telur', 'Bulu dan sisik'], 'Produk nonpangan nabati memanfaatkan khasiat buah dan sayuran.', 'Dipakai untuk kosmetik dan perawatan tubuh.'),
        ('Bahan nabati yang bermanfaat sebagai pencerah wajah adalah…', 'Bengkuang', ['Alpukat', 'Pisang', 'Lidah buaya'], 'Bengkuang dimanfaatkan sebagai pencerah wajah.', 'Alpukat untuk melembapkan kulit.'),
        ('Bahan nabati yang bermanfaat melembapkan kulit adalah…', 'Alpukat', ['Bengkuang', 'Pisang', 'Lidah buaya'], 'Alpukat dapat melembapkan kulit.', 'Pisang menghaluskan kulit wajah.'),
        ('Pisang bermanfaat untuk…', 'Menghaluskan kulit wajah dan menghilangkan bekas cacar', ['Memutihkan gigi', 'Menebalkan rambut', 'Menghilangkan bau badan'], 'Pisang menghaluskan kulit wajah dan menghilangkan bekas cacar atau jerawat.', 'Dipakai sebagai bahan masker.'),
        ('Lidah buaya bermanfaat untuk…', 'Mendinginkan kulit dan mencegah kerontokan rambut', ['Mencerahkan wajah', 'Melembapkan kulit', 'Menghilangkan noda', 'Mengilapkan furnitur'], 'Lidah buaya mendinginkan kulit serta mencegah kerontokan rambut.', 'Banyak dipakai pada produk perawatan.'),
        ('Salah satu pemanfaatan kopi selain diseduh adalah…', 'Pengharum ruangan', ['Bahan bakar pesawat', 'Obat keras', 'Bahan bangunan'], 'Aroma kopi dipakai sebagai pengharum ruangan.', 'Juga dapat mengusir serangga.'),
        ('Ampas kopi dapat dimanfaatkan sebagai…', 'Pupuk tanaman', ['Pewarna kain', 'Bahan peledak', 'Pengganti air'], 'Ampas kopi dapat menjadi pupuk tanaman.', 'Selain itu untuk membersihkan noda.'),
        ('SWOT merupakan singkatan dari…', 'Strengths, weaknesses, opportunities, threats', ['Sales, wages, orders, taxes', 'Strength, work, output, time', 'Supply, warehouse, owner, transport'], 'SWOT berarti kekuatan, kelemahan, peluang, dan ancaman.', 'Dipakai untuk menganalisis usaha.'),
        ('Contoh biaya tetap dalam usaha adalah…', 'Gaji karyawan, sewa gedung, dan penyusutan', ['Pembelian bahan baku', 'Biaya lembur', 'Biaya kerja harian'], 'Biaya tetap meliputi gaji, sewa gedung, dan penyusutan.', 'Jumlahnya tidak bergantung produksi.'),
        ('Contoh biaya variabel dalam usaha adalah…', 'Pembelian alat, lembur, dan kerja harian', ['Gaji karyawan', 'Sewa gedung', 'Penyusutan'], 'Biaya variabel meliputi pembelian alat, lembur, dan kerja harian.', 'Berubah mengikuti kegiatan produksi.'),
        ('Rumus laba bersih adalah…', 'Laba kotor – beban usaha', ['Laba kotor + beban usaha', 'Penjualan – retur', 'Biaya tetap × biaya variabel'], 'Laba bersih = laba kotor dikurangi beban usaha.', 'Beban usaha perlu dihitung teliti.'),
        ('Sekam padi dapat dimanfaatkan sebagai…', 'Media tanam', ['Pakan ternak', 'Bahan kosmetik', 'Bahan bakar tungku'], 'Sekam padi dapat digunakan sebagai media tanam.', 'Dedak dipakai sebagai pakan ternak.'),
        ('Dedak padi dapat dimanfaatkan sebagai…', 'Pakan ternak', ['Media tanam', 'Bahan kosmetik', 'Bahan bakar tungku'], 'Dedak merupakan sisa penggilingan yang dapat menjadi pakan ternak.', 'Batang dan daun kering menjadi bahan bakar.'),
        ('Bahan utama aromaterapi kopi selain kopi bubuk adalah…', 'Lilin, sumbu, dan gelas kaca', ['Semen, pasir, dan batu', 'Tepung, gula, dan telur', 'Kayu, paku, dan cat'], 'Aromaterapi kopi memerlukan lilin kecil, sumbu lilin, gelas kaca, dan kopi bubuk.', 'Lilin dilelehkan lalu dituang berselang-seling.'),
    ],
    'multi': [
        ('Manakah khasiat bahan nabati untuk kecantikan?', ['Bengkuang mencerahkan wajah', 'Alpukat melembapkan kulit', 'Pisang menghaluskan kulit wajah'], ['Bengkuang memutihkan rambut', 'Alpukat mengeraskan kulit'], 'Bengkuang, alpukat, dan pisang bermanfaat untuk kecantikan kulit.', 'Semuanya diolah menjadi masker atau perawatan.'),
        ('Manakah pemanfaatan kopi?', ['Pengharum ruangan', 'Mengusir serangga', 'Mengilapkan furnitur kayu'], ['Bahan bakar pesawat', 'Obat keras'], 'Kopi dipakai sebagai pengharum, pengusir serangga, dan pengilap furnitur.', 'Ampasnya menjadi pupuk tanaman.'),
        ('Manakah bagian padi yang dimanfaatkan?', ['Beras', 'Sekam', 'Dedak'], ['Bulu', 'Sisik'], 'Beras, sekam, dan dedak berasal dari padi dan dapat dimanfaatkan.', 'Bulu dan sisik berasal dari hewan.'),
        ('Manakah alat dan bahan membuat aromaterapi kopi?', ['Lilin', 'Sumbu lilin', 'Gelas kaca', 'Kopi bubuk'], ['Semen', 'Paku'], 'Aromaterapi kopi memakai lilin, sumbu, gelas kaca, dan kopi bubuk.', 'Semen dan paku bukan bahan aromaterapi.'),
        ('Manakah unsur SWOT?', ['Strengths', 'Weaknesses', 'Opportunities'], ['Salary', 'Warehouse'], 'SWOT terdiri atas strengths, weaknesses, opportunities, dan threats.', 'Salary dan warehouse bukan unsur SWOT.'),
        ('Manakah faktor internal analisis usaha?', ['Proses produksi', 'Penentuan harga', 'Bahan baku'], ['Geopolitik', 'Distribusi'], 'Faktor internal meliputi proses produksi, penentuan harga, dan bahan baku.', 'Geopolitik dan distribusi termasuk eksternal.'),
        ('Manakah komponen biaya produksi?', ['Biaya tetap', 'Biaya variabel'], ['Laba bersih', 'Penjualan bersih'], 'Biaya produksi terdiri atas biaya tetap dan biaya variabel.', 'Laba dan penjualan bersih adalah hasil, bukan biaya.'),
        ('Manakah kategori target pasar?', ['Rentang umur', 'Pekerjaan', 'Minat'], ['Golongan darah', 'Warna favorit'], 'Target pasar dikategorikan berdasarkan umur, pekerjaan, dan minat.', 'Golongan darah tidak relevan.'),
    ],
    'pairs': [
        ('Bengkuang', 'pencerah wajah'),
        ('Alpukat', 'pelembap kulit'),
        ('Pisang', 'penghalus kulit wajah'),
        ('Lidah buaya', 'pendingin kulit dan pencegah kerontokan rambut'),
        ('Kopi', 'pengharum ruangan alami'),
        ('Sekam padi', 'media tanam'),
        ('SWOT', 'analisis kekuatan, kelemahan, peluang, ancaman'),
        ('HPP', 'harga pokok penjualan'),
    ],
    'steps': [
        ('Urutkan langkah membuat aromaterapi kopi.', ['Iris tipis lilin', 'Lelehkan lilin', 'Letakkan sumbu di gelas kaca', 'Tuang lilin cair dan kopi bergantian', 'Nyalakan sumbu saat digunakan'], 'Aromaterapi dibuat dengan menuang lilin dan kopi berselang-seling.', 'Lilin dilelehkan sebelum dituang.'),
        ('Urutkan langkah analisis SWOT.', ['Identifikasi kekuatan', 'Identifikasi kelemahan', 'Identifikasi peluang', 'Identifikasi ancaman', 'Susun strategi usaha'], 'SWOT dimulai dari empat identifikasi lalu disusun strategi.', 'Keempat unsur dianalisis berurutan.'),
        ('Urutkan langkah menentukan harga jual.', ['Hitung HPP', 'Tambahkan biaya lain', 'Tentukan target laba', 'Tetapkan harga jual', 'Bandingkan dengan harga pesaing'], 'Harga jual ditetapkan setelah HPP dan biaya lain diketahui.', 'Harga tetap harus bersaing.'),
        ('Urutkan langkah menyusun laporan penjualan.', ['Catat pendapatan', 'Catat beban usaha', 'Hitung laba kotor', 'Kurangi beban usaha', 'Tentukan laba bersih'], 'Laporan disusun dari pendapatan menuju laba bersih.', 'Laba bersih = laba kotor – beban usaha.'),
        ('Urutkan pemanfaatan bagian padi.', ['Panen gabah', 'Pisahkan gabah dari sekam', 'Giling gabah menjadi beras', 'Manfaatkan dedak', 'Olah sekam menjadi media tanam'], 'Padi diolah bertahap dari gabah hingga menjadi beras dan hasil samping.', 'Setiap bagian memberi manfaat berbeda.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
