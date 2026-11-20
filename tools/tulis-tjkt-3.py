"""TJKT 3 — Profesi dan Kewirausahaan (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 3',
    'slug': 'tjkt-3-profesi-kewirausahaan',
    'title': 'Profesi dan Kewirausahaan di Bidang TJKT',
    'description': (
        'Mengenali profesi dan sertifikasi di bidang TJKT, menumbuhkan jiwa '
        'kewirausahaan dan technopreneurship, serta membangun vision dan passion '
        'sebagai bekal berwirausaha.'
    ),
    'objectives': [
        'Menjelaskan ciri-ciri profesi dan profesi di bidang TJKT beserta sertifikasinya.',
        'Menjelaskan jiwa kewirausahaan, technopreneurship, dan karakter wirausaha.',
        'Mengidentifikasi peluang usaha di bidang TJKT dan cara mengenalinya.',
        'Membangun vision dan passion untuk memulai usaha di bidang TJKT.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 3; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'Profesi', 'definition': 'Pekerjaan yang membutuhkan keterampilan khusus yang diperoleh melalui pendidikan dan memiliki kode etik.'},
        {'term': 'Kewirausahaan', 'definition': 'Aktivitas menciptakan atau mengembangkan usaha yang inovatif dan berkelanjutan.'},
        {'term': 'Wirausaha', 'definition': 'Orang yang menjalankan kewirausahaan dengan berani mengambil risiko dan melihat peluang.'},
        {'term': 'Technopreneur', 'definition': 'Pengusaha yang memanfaatkan teknologi informasi untuk menjalankan dan memperluas usaha.'},
        {'term': 'Sertifikasi', 'definition': 'Bukti legal kompetensi seseorang di bidang tertentu, pengakuan profesi secara nasional atau internasional.'},
        {'term': 'SKKNI', 'definition': 'Standar Kompetensi Kerja Nasional Indonesia yang merumuskan kemampuan kerja sesuai tugas dan jabatan.'},
        {'term': 'KKNI', 'definition': 'Kerangka Kualifikasi Nasional Indonesia yang menetapkan level kualifikasi dan jenjang jabatan.'},
        {'term': 'Etika bisnis', 'definition': 'Rambu-rambu dan sopan santun dalam menjalankan usaha untuk menjaga reputasi.'},
        {'term': 'Peluang usaha', 'definition': 'Kesempatan untuk memperoleh keuntungan dengan memanfaatkan sumber daya yang dimiliki.'},
        {'term': 'Passion', 'definition': 'Ketertarikan dan kegemaran mendalam yang menjadi pendorong bekerja dan berkarya.'},
    ],
    'intro': {
        'material_title': 'Apa itu profesi?',
        'title': 'Lebih dari sekadar pekerjaan',
        'paragraphs': [
            'Profesi berasal dari kata profession yang berarti ahli bidang tertentu. Profesi adalah pekerjaan yang membutuhkan keterampilan khusus yang diperoleh melalui pendidikan.',
            'Tidak semua pekerjaan adalah profesi. Profesi memiliki keahlian khusus, standar pelayanan dan kode etik, konsekuensi dan tanggung jawab, pengakuan masyarakat, sertifikasi, dan asosiasi profesi.',
            'Contoh profesi di bidang TJKT: network administrator, security engineer, arsitek jaringan, IT support, hardware engineer, dan teknisi instalasi fiber optik.',
        ],
        'diagram': (
            'Ciri-ciri sebuah profesi',
            'flowchart TB\n'
            '  A[Profesi] --> B[Keahlian khusus]\n'
            '  A --> C[Kode etik dan standar pelayanan]\n'
            '  A --> D[Tanggung jawab]\n'
            '  A --> E[Pengakuan masyarakat]\n'
            '  A --> F[Sertifikasi dan asosiasi]\n'
            '  A --> G[Imbalan sesuai pelayanan]',
        ),
        'callout': 'Sertifikasi menjadi bukti legal kompetensimu saat melamar pekerjaan di bidang jasa yang berbasis kepercayaan.',
        'checkpoint': (
            'Syarat agar sebuah pekerjaan dapat disebut profesi adalah…',
            [
                ('memiliki keahlian khusus dan kode etik', True),
                ('dapat dikerjakan siapa saja', False),
                ('tidak perlu sertifikasi', False),
                ('tanpa tanggung jawab', False),
            ],
            'Keahlian khusus, kode etik, dan sertifikasi adalah ciri profesi.',
        ),
    },
    'concept': {
        'material_title': 'Kewirausahaan dan technopreneurship',
        'title': 'Dari jiwa wirausaha ke teknopreneur',
        'paragraphs': [
            'Menurut Perpres No 2 Tahun 2022, kewirausahaan adalah aktivitas menciptakan atau mengembangkan usaha yang inovatif dan berkelanjutan. Wirausaha adalah orang yang melihat peluang dan berani mengambil risiko.',
            'Jiwa kewirausahaan tampak pada sikap kreatif dan inovatif: memiliki jiwa kepemimpinan, semangat tinggi, kemampuan menganalisis masalah, ide kreatif, dan totalitas dalam usaha.',
            'Technopreneur adalah pengusaha yang memanfaatkan teknologi informasi untuk memperoleh keuntungan. Contoh teknopreneur sukses: Bill Gates, Steve Jobs, Andrew Darwis, dan William Tanuwijaya.',
        ],
        'table': [
            ['10D kewirausahaan', 'Arti'],
            ['Dream', 'Memiliki mimpi untuk maju'],
            ['Decisiveness', 'Tegas mengambil keputusan'],
            ['Doers', 'Segera menindaklanjuti'],
            ['Determination', 'Ketetapan hati'],
            ['Dedication', 'Pengabdian dalam usaha'],
            ['Devotion', 'Kesetiaan menjalankan usaha'],
            ['Details', 'Memperhatikan hal rinci'],
            ['Destiny', 'Tanggung jawab atas tujuan'],
            ['Dollars', 'Mengarahkan kerja untuk keuntungan'],
            ['Distribute', 'Berbagi kepemilikan dengan orang kepercayaan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-3-tahapan',
            'engine': 'mermaid',
            'title': 'Tahapan menumbuhkan jiwa kewirausahaan',
            'code': 'flowchart LR\n'
                    '  A[Internalization] --> B[Paradigm alteration]\n'
                    '  B --> C[Spirit initiation]\n'
                    '  C --> D[Competition]\n'
                    '  D --> E[Usaha inovatif dan berkelanjutan]',
        },
        'activity': categorize_block(
            'tjkt-3-klasifikasi',
            'Kelompokkan kemampuan berikut ke dalam kemampuan wirausaha atau kemampuan teknopreneur.',
            [('b1', 'Wirausaha umum'), ('b2', 'Teknopreneur')],
            [
                ('i1', 'Melihat peluang usaha', 'b1'),
                ('i2', 'Menguasai teknologi informasi', 'b2'),
                ('i3', 'Berani mengambil risiko', 'b1'),
                ('i4', 'Membuat inovasi berbasis teknologi', 'b2'),
                ('i5', 'Kemampuan menganalisis masalah', 'b1'),
                ('i6', 'Mengidentifikasi peluang dari pasar digital', 'b2'),
                ('i7', 'Kepemimpinan dan totalitas', 'b1'),
                ('i8', 'Riset di bidang teknologi informasi', 'b2'),
            ],
            'Tepat. Wirausaha umum berfokus pada peluang dan risiko; teknopreneur menekankan teknologi dan inovasi digital.',
            'Periksa lagi: kata kunci teknopreneur adalah teknologi informasi dan inovasi digital.',
        ),
        'subtitle': 'Peluang usaha di bidang TJKT',
        'list': [
            'Peluang usaha dengan nilai jual tinggi dapat diambil bila idenya original, sesuai minat, antisipatif terhadap pasar, dan mampu mendatangkan keuntungan.',
            'Contoh usaha TJKT: jasa desain grafis, pembuat konten, servis perangkat keras, instalasi dan perawatan jaringan, serta toko komputer dan laptop.',
            'Jasa instalasi dan perawatan jaringan mencakup pemasangan Wi-Fi, CCTV, dan LAN di kantor, kampus, hotel, dan perumahan.',
            'Identifikasi peluang dilakukan dengan mengenali segmentasi pasar, modal, inovasi, dan menyusun rencana bisnis.',
        ],
        'checkpoint': (
            'Pengusaha yang memanfaatkan teknologi informasi untuk menjalankan usaha disebut…',
            [
                ('technopreneur', True),
                ('petugas server', False),
                ('accountant', False),
                ('satpam', False),
            ],
            'Technopreneur adalah gabungan technology dan entrepreneur.',
        ),
    },
    'practice': {
        'material_title': 'Etika dan vision-passion',
        'title': 'Menjaga reputasi, membangun mimpi',
        'paragraphs': [
            'Etika berwirausaha menjaga reputasi pribadi dan perusahaan. Reputasi dibangun lama dan menjadi aset; pelanggaran etika, misalnya menipu konsumen, meruntuhkan kepercayaan hingga usaha bangkrut.',
            'Vision adalah gambaran masa depan yang hendak dicapai usaha, sedangkan passion adalah kegemaran mendalam yang mendorongmu terus berkarya. Keduanya membuat usaha bertahan saat tantangan datang.',
            'Untuk memulai, pilih peluang yang sesuai minat, susun rencana sederhana, dan bangun kepercayaan lewat kualitas layanan yang jujur.',
        ],
        'scenario': scenario(
            'tjkt-3-skenario',
            'Tawaran pelanggan mencurigakan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Pelanggan minta kamu memasang hotspot yang mencuri akses tetangga dan memberi upah besar. Sikapmu?',
                    'choices': [
                        {'text': 'Menolak dan menjelaskan bahwa itu melanggar etika dan hukum', 'next': 'n2', 'score': 2, 'feedback': 'Etika bisnis melindungi reputasi jangka panjang.'},
                        {'text': 'Menerima karena upahnya besar', 'next': 'n3', 'score': 0, 'feedback': 'Keuntungan sesaat menghancurkan kepercayaan dan citra usaha.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana menawarkan solusi yang benar kepada pelanggan itu?',
                    'choices': [
                        {'text': 'Menawarkan pemasangan jaringan legal yang aman dan murah', 'next': 'n4', 'score': 2, 'feedback': 'Layanan jujur membangun reputasi dan pelanggan setia.'},
                        {'text': 'Merahasiakan penolakan lalu mengerjakan secara diam-diam', 'next': 'n3', 'score': 0, 'feedback': 'Tidak ada setengah jalan dalam etika bisnis.'},
                    ],
                },
                {'id': 'n3', 'text': 'Reputasi usahamu hancur dan kepercayaan pelanggan hilang.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Usahamu dipercaya dan pelanggan makin banyak.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan dua ciri profesi.', 'back': 'Keahlian khusus dan kode etik; sertifikasi dan pengakuan masyarakat.'},
            {'front': 'Apa itu technopreneur?', 'back': 'Pengusaha yang memanfaatkan teknologi informasi untuk menjalankan usaha.'},
            {'front': 'Sebutkan dua contoh usaha di bidang TJKT.', 'back': 'Instalasi dan perawatan jaringan; servis perangkat keras.'},
            {'front': 'Apa fungsi etika bisnis?', 'back': 'Menjaga reputasi perusahaan dan menghindari kecurangan.'},
        ],
        'checkpoint': (
            'Contoh profesi di bidang TJKT adalah…',
            [
                ('network administrator', True),
                ('peternak ayam', False),
                ('penjahit', False),
                ('nelayan', False),
            ],
            'Network administrator mengelola jaringan dalam lingkup TJKT.',
        ),
        'challenge': challenge_block(
            'tjkt-3-tantangan',
            'Tantangan istilah profesi dan wirausaha',
            90,
            [
                ('Pekerjaan dengan keahlian khusus', 'Profesi'),
                ('Usaha inovatif dan berkelanjutan', 'Kewirausahaan'),
                ('Pengusaha berbasis teknologi', 'Technopreneur'),
                ('Bukti kompetensi legal', 'Sertifikasi'),
                ('Peluang memperoleh keuntungan', 'Peluang usaha'),
            ],
            'Lima istilah profesi dan wirausaha terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Profesi berasal dari kata profession yang berarti…', 'ahli bidang tertentu', ['karyawan', 'bos', 'pelanggan'], 'Profesi menuntut keahlian khusus.', 'Diperoleh melalui pendidikan.'),
        ('Salah satu ciri profesi adalah…', 'memiliki sertifikasi dan kode etik', ['dikerjakan tanpa keahlian', 'tanpa imbalan', 'tanpa tanggung jawab'], 'Sertifikasi membuktikan kompetensi legal.', 'Asosiasi profesi menyatukan anggotanya.'),
        ('Menurut Perpres No 2 Tahun 2022, kewirausahaan adalah…', 'aktivitas menciptakan atau mengembangkan usaha inovatif dan berkelanjutan', ['pekerjaan tetap di perusahaan', 'hobi tanpa tujuan', 'kegiatan sosial'], 'Kewirausahaan menekankan inovasi.', 'Berlangsung berkelanjutan.'),
        ('Ciri-ciri sehat jiwa kewirausahaan, antara lain…', 'kepemimpinan dan ide kreatif inovatif', ['menunggu perintah', 'meniru terus-menerus', 'menghindari risiko'], 'Wirausaha berani mengambil risiko.', 'Totalitas menjalankan usaha.'),
        ('Tahap menanamkan jiwa kewirausahaan dari dalam diri disebut…', 'internalization', ['competition', 'spirit initiation', 'paradigm alteration'], 'Internalisasi menanamkan jiwa kewirausahaan.', 'Diikuti perubahan paradigma.'),
        ('Karakter kewirausahaan 10D dari Bygrave meliputi…', 'dream, decisiveness, doers', ['dingin, diam, dengar', 'desa, danau, darat', 'debit, devisa, dolar'], '10D berawal dari dream hingga distribute.', 'Decisiveness berarti tegas.'),
        ('D dalam 10D yang berarti segera menindaklanjuti keputusan adalah…', 'doers', ['dream', 'details', 'destiny'], 'Doers artinya pelaku.', 'Tidak menunda kesempatan.'),
        ('Technopreneur adalah pengusaha yang…', 'memanfaatkan teknologi informasi dalam usaha', ['menjual hasil tani', 'berjualan pasar tradisional', 'menggambar manual'], 'Gabungan technology dan entrepreneur.', 'Memperluas bisnis dengan teknologi.'),
        ('Contoh teknopreneur sukses yang disebut buku adalah…', 'Bill Gates dan William Tanuwijaya', ['Albert Einstein', 'R.A. Kartini', 'Ki Hajar Dewantara'], 'Keduanya membangun usaha berbasis teknologi.', 'Steve Jobs dan Andrew Darwis juga dicontohkan.'),
        ('Sertifikasi nasional Indonesia berbasis KKNI disebut…', 'Sertifikat Kompetensi', ['KTP', 'SIM', 'paspor'], 'Sertifikat Kompetensi sesuai level KKNI.', 'Disusun berdasarkan SKKNI.'),
        ('Salah satu contoh peluang usaha di bidang TJKT adalah…', 'jasa instalasi dan perawatan jaringan', ['jasa jahit baju', 'warung nasi', 'angkutan kota'], 'Mencakup Wi-Fi, CCTV, dan instalasi LAN.', 'Menjadi peluang usaha potensial.'),
        ('Fungsi etika dalam usaha adalah…', 'menjaga reputasi perusahaan', ['menaikkan harga semaunya', 'menipu konsumen', 'menghindari pajak'], 'Reputasi adalah aset jangka panjang.', 'Pelanggaran etika berujung bangkrut.'),
        ('Kegemaran mendalam yang mendorong seseorang berkarya disebut…', 'passion', ['gaji', 'seragam', 'jabatan'], 'Passion menjadi pendorong berkarya.', 'Vision adalah gambaran masa depan.'),
        ('Cara mengenali peluang usaha yang baik adalah…', 'mengenali segmentasi pasar dan pesaing', ['menunggu tawaran', 'menyalin usaha orang tanpa berpikir', 'menghindari inovasi'], 'Pasar yang dikenali memudahkan rencana.', 'Inovasi mengatasi ancaman.'),
    ],
    'multi': [
        ('Manakah ciri profesi?', ['Keahlian khusus', 'Kode etik', 'Sertifikasi'], ['Dikerjakan siapa saja', 'Tanpa tanggung jawab'], 'Profesi menuntut keahlian dan etika.', 'Bukan pekerjaan sembarangan.'),
        ('Manakah ciri jiwa kewirausahaan?', ['Berani mengambil risiko', 'Ide kreatif inovatif', 'Totalitas dalam usaha'], ['Menunggu perintah', 'Menolak perubahan'], 'Wirausaha melihat peluang dan bertindak.', 'Pasif bukan ciri wirausaha.'),
        ('Manakah contoh teknopreneur?', ['Pemilik toko daring', 'Penyedia jasa aplikasi', 'Content creator'], ['Pedagang keliling', 'Tukang kayu'], 'Teknopreneur memakai teknologi informasi.', 'Tanpa teknologi informasi.'),
        ('Manakah peluang usaha di bidang TJKT?', ['Instalasi Wi-Fi', 'Servis perangkat keras', 'Pemasangan CCTV'], ['Jasa potong rambut', 'Kebun sayur'], 'Ketiganya memakai keahlian jaringan.', 'Potong rambut dan kebun bukan TJKT.'),
        ('Manakah sikap menjaga etika bisnis?', ['Jujur pada konsumen', 'Menghindari kecurangan', 'Melayani dengan sopan'], ['Menipu demi untung', 'Merahasiakan cacat produk'], 'Etika menjaga reputasi jangka panjang.', 'Kecurangan menghancurkan usaha.'),
        ('Manakah kemampuan yang dibutuhkan teknopreneur?', ['Pengetahuan teknologi', 'Mengelola risiko', 'Menemukan solusi inovasi'], ['Menghafal hukum pidana', 'Menjauh dari teknologi'], 'Teknopreneur menguasai teknologi dan risiko.', 'Menjauh dari teknologi bertentangan.'),
        ('Manakah manfaat teknopreneurship?', ['Menciptakan lapangan kerja', 'Mendorong UMKM', 'Meningkatkan ekonomi'], ['Menambah pengangguran', 'Menghentikan inovasi'], 'Teknopreneur berkontribusi pada ekonomi.', 'Bukan menambah pengangguran.'),
        ('Manakah contoh tindakan membangun vision dan passion?', ['Menulis tujuan usaha', 'Belajar hal yang disukai', 'Mencoba kegagalan dan bangkit'], ['Menunda semua pekerjaan', 'Mengabaikan minat'], 'Vision dan passion lahir dari tujuan dan minat.', 'Menunda bukan cara membangunnya.'),
    ],
    'pairs': [
        ('Profesi', 'pekerjaan dengan keahlian khusus'),
        ('Kewirausahaan', 'usaha inovatif dan berkelanjutan'),
        ('Technopreneur', 'pengusaha berbasis teknologi informasi'),
        ('Sertifikasi', 'bukti kompetensi legal'),
        ('SKKNI', 'standar kompetensi kerja nasional'),
        ('Etika bisnis', 'rambu menjaga reputasi usaha'),
        ('Peluang usaha', 'kesempatan memperoleh keuntungan'),
        ('Passion', 'kegemaran mendalam untuk berkarya'),
    ],
    'steps': [
        ('Urutkan tahap menumbuhkan jiwa kewirausahaan.', ['Internalization', 'Paradigm alteration', 'Spirit initiation', 'Competition'], 'Jiwa ditanam lalu diubah pola pikirnya.', 'Kompetisi menutup tahapan.'),
        ('Urutkan langkah memulai usaha jasa instalasi jaringan.', ['Belajar keterampilan jaringan', 'Menyusun rencana usaha', 'Menentukan target pasar', 'Menawarkan layanan contoh gratis', 'Menagih layanan sesuai kesepakatan'], 'Usaha berawal dari keterampilan.', 'Pelayanan yang baik menambah pelanggan.'),
        ('Urutkan proses mendapatkan sertifikasi profesi.', ['Mengikuti pendidikan atau pelatihan', 'Mempelajari unit kompetensi SKKNI', 'Mengikuti uji kompetensi', 'Mendapat Sertifikat Kompetensi', 'Memakai sertifikat untuk melamar kerja'], 'Sertifikasi dimulai dari pendidikan.', 'Sertifikat menjadi syarat melamar.'),
        ('Urutkan identifikasi peluang usaha.', ['Mengenali pasar dan pesaing', 'Mengenali modal yang dimiliki', 'Mencari ide inovatif', 'Menyusun rencana bisnis', 'Menjalankan dan mengevaluasi'], 'Identifikasi berawal dari pasar.', 'Evaluasi menutup siklus usaha.'),
        ('Urutkan cara menjaga reputasi usaha.', ['Memberi layanan terbaik', 'Bersikap jujur', 'Menepati janji', 'Menangani keluhan pelanggan', 'Memperbaiki layanan'], 'Reputasi dibangun dari pelayanan.', 'Perbaikan berkelanjutan menjaga kepercayaan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)