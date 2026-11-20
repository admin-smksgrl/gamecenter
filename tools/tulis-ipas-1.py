"""IPAS 1 — Mengatasi Masalah Lingkungan Melalui Projek IPAS (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'IPAS 1',
    'slug': 'ipas-1-masalah-lingkungan',
    'title': 'Mengatasi Masalah Lingkungan Melalui Projek IPAS',
    'description': (
        'Mengenali gejala kerusakan lingkungan, menyusun bukti ilmiah kuantitatif '
        'dan kualitatif, menempuh sepuluh langkah penyelesaian masalah, hingga '
        'membuat purwarupa kompos dan mengomunikasikan hasilnya.'
    ),
    'objectives': [
        'Mengidentifikasi masalah dan bukti ilmiah berdasarkan fenomena yang diamati.',
        'Menerapkan konsep IPAS untuk menentukan pemecahan masalah lingkungan di sekitar.',
        'Merancang dan membuat purwarupa sebagai solusi masalah lingkungan.',
        'Mengomunikasikan purwarupa secara lisan, tulisan, dan kegiatan.',
        'Merefleksi kegiatan projek IPAS yang telah dilakukan.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 1 Mengatasi Masalah Lingkungan Melalui '
        'Projek IPAS; CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'Projek IPAS', 'definition': 'Pembelajaran berbasis projek yang memadukan sains dan sosial untuk menyelesaikan masalah nyata di sekitar.'},
        {'term': 'Bukti ilmiah', 'definition': 'Bukti yang diperoleh dengan prosedur baku dan diukur memakai alat ukur sesuai standar.'},
        {'term': 'Data kuantitatif', 'definition': 'Data yang disajikan dalam bentuk angka, grafik, atau persamaan matematis.'},
        {'term': 'Data kualitatif', 'definition': 'Data yang berbentuk kata, skema, atau gambar.'},
        {'term': 'Zat pencemar', 'definition': 'Bahan atau makhluk hidup yang masuk ke lingkungan sehingga mengubah fungsi lingkungan tersebut.'},
        {'term': 'Purwarupa', 'definition': 'Gambaran awal produk yang sedang dikembangkan sebelum diproduksi sebenarnya.'},
        {'term': 'Composting', 'definition': 'Proses daur ulang secara alami bahan organik menjadi pupuk atau kompos.'},
        {'term': 'Quality control', 'definition': 'Proses memastikan kualitas produk sesuai kriteria yang telah ditetapkan.'},
    ],
    'intro': {
        'material_title': 'Mengapa masalah lingkungan perlu bukti ilmiah?',
        'title': 'Gejala kerusakan lingkungan dan bukti ilmiahnya',
        'paragraphs': [
            'Indonesia hampir setiap tahun mengalami banjir, kekeringan, kebakaran hutan, dan pencemaran sungai oleh limbah rumah tangga serta industri. Kejadian itu bukan sekadar kabar: ia gejala kerusakan lingkungan yang berkaitan erat dengan aktivitas manusia.',
            'Untuk memutuskan tindakan, kebijakan, bahkan undang-undang, kita memerlukan bukti ilmiah. Bukti ilmiah adalah bukti yang diukur dengan prosedur baku dan alat ukur sesuai standar, sehingga kesimpulannya tidak dapat dibantah sembarangan.',
            'Projek IPAS memberi jalan yang runtut: mengamati gejala, mengumpulkan bukti, memilih solusi, lalu membuat purwarupa. Setiap langkah menghasilkan catatan yang dapat diperiksa ulang.',
        ],
        'diagram': (
            'Sepuluh langkah menyelesaikan masalah lingkungan',
            'flowchart LR\n'
            '  A[Identifikasi masalah] --> B[Identifikasi konsep]\n'
            '  B --> C[Identifikasi kebutuhan]\n'
            '  C --> D[Alternatif penyelesaian]\n'
            '  D --> E[Evaluasi dan pilih]\n'
            '  E --> F[Desain purwarupa]\n'
            '  F --> G[Bangun purwarupa]\n'
            '  G --> H[Evaluasi dan desain ulang]\n'
            '  H --> I[Komunikasikan hasil]\n'
            '  I --> J[Rencana tindak lanjut]',
        ),
        'callout': 'Bukti ilmiah diambil dari sumber terpercaya atau diukur sendiri dengan alat dan metode yang tepat, bukan dari dugaan atau kabar tanpa data.',
        'checkpoint': (
            'Data yang disajikan dalam bentuk angka, grafik, atau persamaan disebut…',
            [
                ('data kuantitatif', True),
                ('data kualitatif', False),
                ('data sekunder', False),
                ('data nominal', False),
            ],
            'Data kuantitatif berupa angka atau bentuk matematis; data kualitatif berbentuk kata, skema, atau gambar.',
        ),
    },
    'concept': {
        'material_title': 'Ciri pencemaran, parameter, dan pemilihan solusi',
        'title': 'Membaca pencemaran dan memilih solusi terbaik',
        'paragraphs': [
            'Suatu kejadian disebut pencemaran jika ada zat pencemar yang masuk ke lingkungan dan mengubah fungsinya. Pada sungai yang penuh sampah, lingkungannya adalah sungai dan zat pencemarnya adalah sampah. Pada air berminyak yang membuat ikan mati, minyak berperan sebagai zat pencemar.',
            'Ciri pencemaran meliputi masuknya zat atau makhluk hidup yang tidak seharusnya, perubahan fungsi lingkungan, perubahan warna, bau, atau rasa, munculnya mikroorganisme berlebih, serta banyaknya hewan atau tumbuhan yang tidak dapat bertahan hidup.',
            'Pencemaran juga dapat diukur melalui parameter kimia (karbon dioksida, pH, alkalinitas, fosfor), parameter fisik (temperatur, warna, rasa, bau, kejernihan, bahan radioaktif), dan parameter biologi (bakteri coli, virus, plankton).',
        ],
        'table': [
            ['Parameter', 'Contoh', 'Alat atau cara memeriksa'],
            ['Kimia', 'pH, alkalinitas, fosfor, karbon dioksida', 'pH meter, titrasi, uji laboratorium'],
            ['Fisik', 'Temperatur, warna, bau, kejernihan', 'Termometer, pengamatan, alat ukur kekeruhan'],
            ['Biologi', 'Bakteri E. coli, virus, plankton', 'Uji mikrobiologi sampel air'],
        ],
        'visual': chart_block(
            'ipas-1-mikroplastik',
            'Sumber mikroplastik di perairan Jakarta (%)',
            'bar',
            [('Permukiman', 72.7), ('Perkantoran', 17.3), ('Industri', 9.9)],
        ),
        'activity': categorize_block(
            'ipas-1-klasifikasi',
            'Kelompokkan pernyataan pada wacana pembakaran jerami ke dalam aspek yang tepat.',
            [('b1', 'Dampak primer'), ('b2', 'Dampak sekunder'), ('b3', 'Penyebab')],
            [
                ('i1', 'Udara tercemar dan kadar oksigen turun', 'b1'),
                ('i2', 'Unsur hara tanah hilang', 'b1'),
                ('i3', 'Warga sesak napas', 'b2'),
                ('i4', 'Pakaian dan perabot menjadi kotor serta berbau', 'b2'),
                ('i5', 'Sawah perlu bebas dari tumpukan jerami', 'b3'),
                ('i6', 'Kebiasaan turun-temurun membakar jerami', 'b3'),
            ],
            'Tepat. Dampak primer bersifat langsung, dampak sekunder muncul kemudian, dan penyebab menjelaskan asal masalah.',
            'Periksa lagi: sesak napas dan perabot kotor adalah akibat lanjutan, bukan sebab maupun dampak langsung.',
        ),
        'subtitle': 'Mengevaluasi alternatif dan memilih solusi',
        'list': [
            'Menentukan kriteria evaluasi dari analisis kebutuhan, lalu menambah kriteria seperti kemudahan bahan, harga, legalitas, dan kekuatan.',
            'Memperkirakan apakah kebutuhan benar-benar terpenuhi, dengan bukti dari literatur, wawancara, pengamatan, atau testimoni pengguna.',
            'Mengurutkan alternatif berdasarkan prioritas agar pilihan dapat dipertanggungjawabkan.',
            'Pada wacana jerami, kompos memenuhi tujuh kriteria, edukasi masyarakat lima kriteria, sedangkan air purifier hanya tiga kriteria.',
        ],
        'checkpoint': (
            'Mengapa pembuatan kompos dipilih daripada air purifier pada wacana pembakaran jerami?',
            [
                ('Kompos memenuhi lebih banyak kriteria kebutuhan petani', True),
                ('Air purifier lebih murah dan mudah dibuat', False),
                ('Kompos tidak memerlukan bahan tambahan', False),
                ('Air purifier tidak dianggap legal', False),
            ],
            'Kompos memenuhi tujuh kriteria (termasuk murah, mudah, dan menambah pendapatan), sedangkan air purifier hanya tiga.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Dari purwarupa kompos sampai rencana tindak lanjut',
        'paragraphs': [
            'Setelah desain reaktor composting dibuat, tahap berikutnya adalah membangun purwarupa. Perencanaannya memuat jadwal waktu, deskripsi pekerjaan anggota kelompok, prosedur kerja, dan manajemen risiko agar hambatan tidak menghentikan projek.',
            'Hasil purwarupa dievaluasi dengan rubrik. Kompos yang matang berwarna coklat-hitam, ber-pH 5–8,5, jeraminya terurai sempurna, beraroma seperti tanah, dan memiliki rasio C/N di atas 25. Bagian yang belum sesuai diperbaiki melalui desain ulang.',
            'Hasil projek dikomunikasikan sebagai laporan tertulis, infografis, atau video. Setelah itu disusun rencana tindak lanjut: memperbaiki rancangan, sosialisasi melalui pameran karya, atau upscaling menjadi projek Teaching Factory.',
        ],
        'scenario': scenario(
            'ipas-1-skenario',
            'Asap jerami di pinggir jalan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Petani di dekat sekolahmu membakar jerami setiap musim panen sehingga asap menutup jalan. Apa langkah pertamamu?',
                    'choices': [
                        {'text': 'Mengumpulkan bukti dan merumuskan pernyataan masalah', 'next': 'n2', 'score': 2, 'feedback': 'Masalah yang terukur lebih mudah diselesaikan.'},
                        {'text': 'Langsung menegur petani tanpa data', 'next': 'n3', 'score': 0, 'feedback': 'Teguran tanpa bukti mudah ditolak.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bukti menunjukkan volume jerami tinggi dan petani ingin tambahan pendapatan. Solusi apa yang kamu ajukan?',
                    'choices': [
                        {'text': 'Mengolah jerami menjadi kompos yang dapat dijual', 'next': 'n4', 'score': 2, 'feedback': 'Solusi ini murah, memakai bahan sekitar, dan menambah penghasilan.'},
                        {'text': 'Membeli air purifier untuk setiap rumah', 'next': 'n3', 'score': 0, 'feedback': 'Air purifier mahal, sulit dibuat, dan tidak mengurangi jerami.'},
                    ],
                },
                {'id': 'n3', 'text': 'Masalah berlanjut karena solusi tidak sesuai kebutuhan warga.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kompos terjual, jerami berkurang, dan asap tidak lagi menutup jalan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu bukti ilmiah?', 'back': 'Bukti dari prosedur baku dan alat ukur sesuai standar.'},
            {'front': 'Sebutkan tiga parameter pencemaran.', 'back': 'Parameter kimia, fisik, dan biologi.'},
            {'front': 'Apa fungsi quality control?', 'back': 'Memastikan produk sesuai kriteria yang ditetapkan.'},
            {'front': 'Apa itu upscaling?', 'back': 'Memperluas cakupan atau skala produksi projek.'},
        ],
        'checkpoint': (
            'Dokumen yang menyajikan data projek secara singkat dengan bantuan visual disebut…',
            [
                ('infografis', True),
                ('laporan keuangan', False),
                ('jadwal waktu', False),
                ('manajemen risiko', False),
            ],
            'Infografis memadukan data ringkas dengan gambar, grafik, dan tipografi agar mudah dipahami audiens.',
        ),
        'challenge': challenge_block(
            'ipas-1-tantangan',
            'Tantangan istilah projek lingkungan',
            90,
            [
                ('Alat pengubah limbah menjadi kompos', 'Reaktor composting'),
                ('Data berbentuk angka', 'Kuantitatif'),
                ('Bakteri penanda pencemaran tinja', 'E. coli'),
                ('Bahan tambahan pengomposan jerami', 'EM4'),
                ('Kegiatan memperkenalkan produk kepada masyarakat', 'Sosialisasi'),
            ],
            'Lima istilah projek lingkungan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa yang dimaksud bukti ilmiah?', 'Bukti yang diukur dengan prosedur baku dan alat sesuai standar', ['Pendapat tokoh masyarakat', 'Dugaan tanpa pengukuran', 'Cerita pengalaman pribadi'], 'Bukti ilmiah diperoleh melalui prosedur ilmiah dan alat ukur yang sesuai standar.', 'Bukti selalu dapat diperiksa ulang oleh orang lain.'),
        ('Data yang disajikan dalam bentuk angka, grafik, atau persamaan disebut…', 'data kuantitatif', ['data kualitatif', 'data primer', 'data sekunder'], 'Data kuantitatif berbentuk angka atau bentuk matematis lainnya.', 'Kuantitas berarti jumlah.'),
        ('Menurut Christ dan Arañas, masalah diartikan sebagai…', 'hal-hal yang belum sesuai dengan yang diharapkan', ['kegagalan alat ukur', 'perbedaan pendapat ahli', 'peristiwa alam yang tidak terduga'], 'Masalah adalah hal-hal yang belum sesuai dengan harapan atau standar yang berlaku.', 'Sesuatu menjadi masalah ketika ada jarak antara kenyataan dan harapan.'),
        ('Berapa persen mikroplastik di sungai Jakarta berasal dari limbah permukiman?', '72,7%', ['17,3%', '9,9%', '50%'], 'Limbah permukiman menyumbang 72,7% mikroplastik, perkantoran 17,3%, dan industri 9,9%.', 'Penyumbang terbesar adalah permukiman.'),
        ('Bakteri yang menandakan pencemaran tinja pada sungai Jakarta adalah…', 'Escherichia coli', ['Salmonella typhi', 'Lactobacillus casei', 'Rhizobium leguminosarum'], 'E. coli hidup di usus manusia dan ditemukan pada sungai yang tercemar tinja.', 'Bakteri ini menjadi indikator sanitasi air.'),
        ('Bahan yang masuk ke lingkungan dan mengubah fungsinya disebut…', 'zat pencemar', ['zat hara', 'bahan baku', 'purwarupa'], 'Zat pencemar adalah bahan yang menyebabkan pencemaran lingkungan.', 'Bandingkan dengan unsur hara yang justru dibutuhkan tanaman.'),
        ('Parameter pH, alkalinitas, dan fosfor termasuk parameter…', 'kimia', ['fisik', 'biologi', 'mekanik'], 'Ketiganya termasuk parameter kimia pencemaran air.', 'Parameter fisik mencakup suhu, warna, dan bau.'),
        ('Alat yang membersihkan udara di dalam ruangan disebut…', 'air purifier', ['multimeter', 'kalorimeter', 'biodigester'], 'Air purifier mengurangi partikel kecil seperti asap dan debu di ruangan.', 'Kata purifier berasal dari pure yang berarti bersih.'),
        ('Proses daur ulang bahan organik menjadi pupuk disebut…', 'composting', ['upscaling', 'sosialisasi', 'quality control'], 'Composting mengubah bahan organik menjadi kompos.', 'Hasilnya dipakai menyuburkan lahan.'),
        ('Bahan yang ditambahkan saat mengompos jerami menurut buku adalah…', 'bokashi, air, dan bakteri EM4', ['semen dan pasir', 'garam dan gula', 'bensin dan solar'], 'Kompos jerami memakai bokashi, air, dan bakteri EM4 yang mudah dibeli di toko pertanian.', 'Dekomposer mempercepat penguraian.'),
        ('Proses memastikan produk sesuai kriteria yang ditetapkan disebut…', 'quality control', ['brainstorming', 'prototyping', 'sosialisasi'], 'Quality control dilakukan pada tahap akhir produksi untuk menjaga kualitas.', 'Dilakukan sebelum produk dipasarkan.'),
        ('Berapa kisaran pH kompos matang menurut rubrik evaluasi?', '5–8,5', ['1–3', '9–12', '12–14'], 'Kompos matang memiliki pH 5–8,5, warna coklat-hitam, dan aroma seperti tanah.', 'Tanah pertanian umumnya mendekati netral.'),
        ('Media laporan projek yang memadukan data ringkas dengan visual disebut…', 'infografis', ['time schedule', 'job desk', 'rubrik'], 'Infografis menyajikan data secara singkat, padat, dan mudah dipahami audiens.', 'Cocok untuk presentasi.'),
        ('Kegiatan memperluas skala produksi projek menjadi Teaching Factory disebut…', 'upscaling', ['sosialisasi', 'evaluasi', 'refleksi'], 'Upscaling memperluas cakupan produksi, misalnya menjadi projek TEFA berskala sekolah.', 'Skala berubah dari kelompok menjadi sekolah.'),
    ],
    'multi': [
        ('Manakah yang termasuk bukti kuantitatif?', ['Indeks kualitas udara 180', 'Grafik penyumbang mikroplastik'], ['Kutipan wawancara warga', 'Deskripsi bau sungai'], 'Angka indeks dan grafik termasuk data kuantitatif.', 'Kutipan dan deskripsi termasuk data kualitatif.'),
        ('Manakah yang termasuk parameter fisik pencemaran?', ['Temperatur', 'Kekeruhan', 'Bau'], ['pH', 'Alkalinitas'], 'Temperatur, kekeruhan, dan bau termasuk parameter fisik.', 'pH dan alkalinitas termasuk parameter kimia.'),
        ('Manakah yang termasuk ciri pencemaran lingkungan?', ['Masuknya zat yang tidak seharusnya', 'Perubahan fungsi lingkungan', 'Munculnya mikroorganisme berlebih'], ['Bertambahnya jumlah penduduk', 'Naiknya harga bahan bakar'], 'Ciri pencemaran berkaitan dengan perubahan zat, fungsi, dan makhluk hidup di lingkungan.', 'Penduduk dan harga bukan penanda pencemaran.'),
        ('Manakah yang termasuk dampak primer pembakaran jerami?', ['Udara tercemar', 'Kadar oksigen menurun', 'Unsur hara tanah hilang'], ['Warga sesak napas', 'Perabot rumah berbau'], 'Dampak primer terjadi langsung, sedangkan sesak napas dan perabot berbau adalah dampak sekunder.', 'Dampak sekunder muncul karena dampak primer.'),
        ('Manakah yang menjadi penyebab pembakaran jerami?', ['Kebutuhan sawah bebas jerami', 'Ketidaktahuan tentang dampaknya'], ['Harga kompos yang mahal', 'Larangan pemerintah'], 'Penyebab utamanya kebutuhan lahan bersih dan kurangnya pengetahuan.', 'Kebiasaan turun-temurun menjadi penyebab sekunder.'),
        ('Manakah cara mengomunikasikan hasil purwarupa?', ['Laporan tertulis', 'Infografis', 'Video'], ['Sertifikat penghargaan', 'Rapat internal'], 'Laporan tertulis, infografis, dan video adalah bentuk komunikasi hasil projek.', 'Ketiganya menyampaikan proses dan data projek.'),
        ('Manakah yang termasuk kegiatan rencana tindak lanjut?', ['Memperbaiki rancangan', 'Sosialisasi produk', 'Upscaling produksi'], ['Membakar jerami', 'Menghentikan projek'], 'RTL berisi perbaikan rancangan, sosialisasi, dan upscaling.', 'Semua bertujuan menyempurnakan projek.'),
        ('Apa yang perlu disiapkan dalam pameran karya?', ['Karya terbaik', 'Perlengkapan pameran', 'Lokasi strategis'], ['Tiket pesawat', 'Izin mendirikan bank'], 'Pameran memerlukan karya, perlengkapan, lokasi strategis, penataan ruang, dan keamanan.', 'Semua berhubungan langsung dengan penyajian karya.'),
    ],
    'pairs': [
        ('Bukti ilmiah', 'bukti dari prosedur baku dan alat sesuai standar'),
        ('Data kuantitatif', 'data berbentuk angka atau grafik'),
        ('Data kualitatif', 'data berbentuk kata, skema, atau gambar'),
        ('Zat pencemar', 'bahan yang mengubah fungsi lingkungan'),
        ('Parameter kimia', 'pH, alkalinitas, dan fosfor'),
        ('Purwarupa', 'gambaran awal produk yang dikembangkan'),
        ('Composting', 'daur ulang bahan organik menjadi pupuk'),
        ('Quality control', 'memastikan produk sesuai kriteria'),
    ],
    'steps': [
        ('Urutkan alur penyelesaian masalah lingkungan menurut buku.', ['Identifikasi masalah', 'Identifikasi konsep', 'Identifikasi kebutuhan', 'Menyusun alternatif solusi', 'Mengevaluasi dan memilih alternatif'], 'Alur dimulai dari mengenali masalah sampai memilih solusi terbaik.', 'Konsep dipelajari setelah masalah dikenali.'),
        ('Urutkan langkah mengevaluasi alternatif solusi.', ['Menentukan kriteria evaluasi', 'Memperkirakan pemenuhan kebutuhan', 'Mengurutkan prioritas alternatif', 'Memilih satu alternatif'], 'Evaluasi bergerak dari kriteria, perkiraan, prioritas, lalu keputusan.', 'Keputusan diambil paling akhir.'),
        ('Urutkan langkah membuat kompos jerami.', ['Mengumpulkan jerami', 'Mencacah jerami', 'Mencampur jerami dengan dekomposer', 'Memantau pengomposan', 'Memanen dan mengemas kompos'], 'Kompos dibuat dari jerami cacah yang dicampur dekomposer lalu dipantau sampai matang.', 'Pencacahan mempercepat penguraian.'),
        ('Urutkan langkah menyusun infografis.', ['Menentukan topik', 'Menentukan audiens', 'Mengumpulkan data', 'Memvisualisasikan data', 'Merancang tata letak', 'Membuat template'], 'Infografis disusun dari topik dan audiens, lalu data, visual, dan tata letak.', 'Tanpa audiens yang jelas, visual mudah salah sasaran.'),
        ('Urutkan langkah menyusun rencana tindak lanjut.', ['Mengevaluasi seluruh langkah projek', 'Mendata kelemahan dan kekurangan', 'Menyusun ulang langkah dan desain', 'Menentukan jenis kegiatan tindak lanjut', 'Menetapkan pelaksana dan batas waktu'], 'RTL berangkat dari evaluasi, lalu daftar perbaikan, jenis kegiatan, dan penanggung jawab.', 'RTL tanpa pelaksana dan tenggat sulit dijalankan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
