"""ANIM 2 — Perkembangan Teknologi Industri Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 2',
    'slug': 'anim-2-perkembangan-teknologi',
    'title': 'Perkembangan Teknologi Industri Animasi',
    'description': (
        'Menelusuri sejarah animasi dunia, mengenal teknik animasi '
        '(stop-motion, claymation, pixilation), memahami teknologi digital '
        'dalam industri film, dan membaca product life cycle produk animasi.'
    ),
    'objectives': [
        'Menjelaskan sejarah perkembangan animasi dunia secara kronologis.',
        'Membedakan teknik animasi stop-motion, claymation, dan pixilation.',
        'Memahami peran teknologi digital dalam produksi dan distribusi film.',
        'Menguraikan empat tahap product life cycle produk animasi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 2 Perkembangan Teknologi Industri Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Animasi', 'definition': 'Proses merekam lalu memutar kembali rangkaian gambar diam untuk menciptakan ilusi gerak.'},
        {'term': 'Praxinoscope', 'definition': 'Alat proyeksi gambar berputar yang dikembangkan Charles Émile Reynaud.'},
        {'term': 'Cell animation', 'definition': 'Teknik memisahkan latar diam dan bagian bergerak pada seluloid transparan, ditemukan Earl Hurd (1914).'},
        {'term': 'Stop-motion', 'definition': 'Teknik memindahkan objek secara fisik sedikit demi sedikit lalu direkam per frame.'},
        {'term': 'Claymation', 'definition': 'Stop-motion yang memakai bahan lunak seperti tanah liat atau plastisin, disangga armature.'},
        {'term': 'Object-motion', 'definition': 'Stop-motion yang menggerakkan benda padat seperti mainan atau balok.'},
        {'term': 'Pixilation', 'definition': 'Stop-motion yang menggunakan manusia sebagai objek yang digerakkan per frame.'},
        {'term': 'CGI', 'definition': 'Computer-Generated Imagery, gambar yang dibuat dengan komputer dalam film.'},
        {'term': 'DCP', 'definition': 'Digital Cinema Package, format standar pengiriman dan pemutaran film di bioskop digital.'},
        {'term': 'KDM', 'definition': 'Key Delivery Message, kunci untuk membuka DCP yang terenkripsi.'},
        {'term': 'Product life cycle', 'definition': 'Siklus hidup produk: introduksi, pertumbuhan, kematangan, dan penurunan.'},
    ],
    'intro': {
        'material_title': 'Sejarah animasi',
        'title': 'Dari praxinoscope sampai Steamboat Willie',
        'paragraphs': [
            'Animasi berasal dari kata animation yang bermakna menggerakkan. Menurut Fernandez (2002), animasi adalah proses merekam dan memutar kembali rangkaian gambar diam sehingga tampak hidup.',
            'Pada abad XVII–XIX, peralatan animasi sederhana telah ditemukan. Charles Émile Reynaud membuat Praxinoscope (1877) dan Teater Optik (1888), lalu pada 1892 memproyeksikan Pauvre Pierrot di depan umum.',
            'J. Stuart Blackton membuat Humorous Phases of Funny Faces (1906) dengan teknik stop-motion, lalu Earl Hurd menemukan cell animation (1914) yang memisahkan latar diam dan bagian bergerak.',
            'Tahun 1928 Walt Disney memadukan animasi dan suara melalui Steamboat Willie, yang melahirkan karakter Mickey Mouse.',
        ],
        'diagram': (
            'Garis waktu tonggak sejarah animasi',
            'flowchart LR\n'
            '  A[1877 Praxinoscope] --> B[1892 Pauvre Pierrot]\n'
            '  B --> C[1906 Humorous Phases of Funny Faces]\n'
            '  C --> D[1914 Cell animation]\n'
            '  D --> E[1928 Steamboat Willie]\n'
            '  E --> F[1995 Toy Story animasi CGI]',
        ),
        'callout': 'Perubahan teknologi selalu mengubah cara animasi dibuat: dari papan tulis, seluloid, sampai komputer dan CGI.',
        'checkpoint': (
            'Film animasi pertama yang memadukan gambar dan suara adalah…',
            [
                ('Steamboat Willie (1928)', True),
                ('Humorous Phases of Funny Faces (1906)', False),
                ('Fantasmagorie (1908)', False),
                ('Pauvre Pierrot (1892)', False),
            ],
            'Steamboat Willie memunculkan Mickey Mouse dan suara.',
        ),
    },
    'concept': {
        'material_title': 'Teknik animasi',
        'title': 'Stop-motion, claymation, dan pixilation',
        'paragraphs': [
            'Dilihat dari teknik pembuatannya, animasi dapat dikategorikan menjadi stop-motion, claymation, dan pixilation. Ketiganya menggerakkan objek secara fisik lalu merekamnya per frame.',
            'Stop-motion adalah pengambilan gambar objek yang dipindahkan setahap demi setahap; bila tiap frame digabung, objek seolah bergerak hidup.',
            'Claymation memakai bahan yang dapat dibentuk seperti tanah liat, plastisin, atau lilin, dengan kerangka kawat bernama armature agar mudah digerakkan.',
            'Pixilation menggunakan manusia sebagai objek yang diposisikan ulang setiap frame sehingga tampak bergerak tidak wajar dan jenaka.',
        ],
        'table': [
            ['Teknik', 'Objek', 'Contoh karya'],
            ['Object-motion', 'Benda padat: mainan, balok, boneka', 'Lego the Movie'],
            ['Claymation', 'Tanah liat atau plastisin', 'Chicken Run, Wallace and Gromit'],
            ['Pixilation', 'Manusia sebagai objek', 'Video eksperimen dan iklan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-2-teknik',
            'engine': 'mermaid',
            'title': 'Pembagian teknik animasi stop-motion',
            'code': 'flowchart TB\n'
                    '  A[Stop-motion] --> B[Object-motion: benda padat]\n'
                    '  A --> C[Claymation: tanah liat]\n'
                    '  A --> D[Pixilation: manusia]\n'
                    '  C --> E[Armature sebagai kerangka]\n'
                    '  A --> F[Direkam per frame lalu digabung]',
        },
        'activity': categorize_block(
            'anim-2-klasifikasi',
            'Kelompokkan ciri berikut sesuai teknik animasinya.',
            [('b1', 'Stop-motion benda'), ('b2', 'Claymation'), ('b3', 'Pixilation')],
            [
                ('i1', 'Menggerakkan mainan dan balok', 'b1'),
                ('i2', 'Memakai plastisin dan tanah liat', 'b2'),
                ('i3', 'Manusia menjadi objek yang digerakkan', 'b3'),
                ('i4', 'Boneka disangga kerangka kawat', 'b2'),
                ('i5', 'Contoh karyanya Lego the Movie', 'b1'),
                ('i6', 'Gerakan tampak lucu dan tidak wajar', 'b3'),
            ],
            'Tepat. Setiap teknik berbeda pada objek dan alat yang digerakkan.',
            'Ingat: benda padat object-motion, bahan lunak claymation, manusia pixilation.',
        ),
        'subtitle': 'Teknologi digital dan siklus produk',
        'list': [
            'Teknologi film dimulai dari cinematographe Lumiere Brothers (1895) dan berkembang menjadi film berwarna serta bersuara.',
            'Sejak awal 2000-an Hollywood merekam film secara digital; CGI dan VFX menjadi inovasi utama, misalnya Toy Story (1995) dan The Matrix (1999).',
            'Bioskop digital memutar film melalui Digital Cinema Package (DCP) dengan bitrate sekitar 250 Mbps; DCP terenkripsi dibuka dengan Key Delivery Message (KDM).',
            'Product life cycle terdiri atas introduksi, pertumbuhan, kematangan, dan penurunan. Pada titik jenuh, produsen harus berinovasi ulang.',
        ],
        'checkpoint': (
            'Alat proyeksi gambar berputar karya Charles Émile Reynaud adalah…',
            [
                ('praxinoscope', True),
                ('cinematographe', False),
                ('mutoscope', False),
                ('kinescope', False),
            ],
            'Reynaud menciptakan praxinoscope dan teater optik.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membaca siklus hidup produk animasi',
        'paragraphs': [
            'Siklus hidup produk dipengaruhi perkembangan teknologi, permintaan pasar, stabilitas ekonomi, munculnya kompetitor, penurunan keuntungan, dan kemunduran organisasi.',
            'Pada tahap introduksi, studio beriklan lewat poster, media cetak, dan trailer di media sosial untuk memperkenalkan produk baru.',
            'Tahap kematangan paling menguntungkan karena produk sudah dikenal, tetapi mulai muncul produk serupa dari kompetitor sehingga inovasi ulang menjadi keharusan.',
        ],
        'scenario': scenario(
            'anim-2-skenario',
            'Serial animasi yang mulai ditinggalkan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Serial animasi studimu dulu populer, kini penonton menurun dan kompetitor muncul dengan kualitas lebih baik. Sikapmu?',
                    'choices': [
                        {'text': 'Melakukan inovasi ulang cerita dan tampilan visual', 'next': 'n2', 'score': 2, 'feedback': 'Titik jenuh harus dijawab dengan inovasi, bukan diam.'},
                        {'text': 'Membiarkan saja karena dulu pernah sukses', 'next': 'n3', 'score': 0, 'feedback': 'Produk yang tidak berinovasi akan masuk tahap penurunan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Apa langkah berikutnya agar produk kembali diminati?',
                    'choices': [
                        {'text': 'Memperluas pasar dan mengembangkan lisensi produk', 'next': 'n4', 'score': 2, 'feedback': 'Pengembangan potensi produk memperpanjang siklus hidup.'},
                        {'text': 'Menaikkan harga tanpa perbaikan kualitas', 'next': 'n3', 'score': 0, 'feedback': 'Harga naik tanpa nilai tambah mempercepat penurunan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk berhenti diproduksi dan studio kehilangan pasar.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk diperbarui dan kembali diminati pasar.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Siapa pencipta praxinoscope?', 'back': 'Charles Émile Reynaud.'},
            {'front': 'Apa fungsi armature pada claymation?', 'back': 'Kerangka kawat agar karakter mudah digerakkan dan stabil.'},
            {'front': 'Apa itu DCP?', 'back': 'Digital Cinema Package, format standar pengiriman dan pemutaran film bioskop digital.'},
            {'front': 'Sebutkan empat tahap product life cycle.', 'back': 'Introduksi, pertumbuhan, kematangan, penurunan.'},
        ],
        'checkpoint': (
            'Teknik animasi yang menggunakan manusia sebagai objek disebut…',
            [
                ('pixilation', True),
                ('claymation', False),
                ('object-motion', False),
                ('cell animation', False),
            ],
            'Pixilation menggerakkan manusia per frame.',
        ),
        'challenge': challenge_block(
            'anim-2-tantangan',
            'Tantangan istilah teknologi animasi',
            90,
            [
                ('Alat proyeksi Reynaud', 'Praxinoscope'),
                ('Animasi stop-motion berbahan tanah liat', 'Claymation'),
                ('Kerangka kawat penyangga karakter clay', 'Armature'),
                ('Format standar film bioskop digital', 'Digital Cinema Package'),
                ('Kunci pembuka DCP terenkripsi', 'Key Delivery Message'),
            ],
            'Lima istilah teknologi animasi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Animasi berasal dari kata animation yang bermakna…', 'menggerakkan', ['menggambar', 'mewarnai', 'menyunting'], 'Animasi menggerakkan gambar atau objek diam.', 'Akar kata to animate.'),
        ('Film animasi pertama yang dikenal publik dibuat oleh…', 'J. Stuart Blackton', ['Walt Disney', 'Earl Hurd', 'Lumiere Brothers'], 'Blackton membuat Humorous Phases of Funny Faces (1906).', 'Berteknik stop-motion.'),
        ('Teknik cell animation ditemukan pada tahun 1914 oleh…', 'Earl Hurd', ['Walt Disney', 'Nick Park', 'Winsor McCay'], 'Cell animation memisahkan latar diam dan bagian bergerak.', 'Menjadi acuan animasi abad XX.'),
        ('Film yang pertama memadukan animasi dan suara adalah…', 'Steamboat Willie', ['Fantasmagorie', 'Gertie the Dinosaur', 'Toy Story'], 'Steamboat Willie dirilis 1928.', 'Melahirkan Mickey Mouse.'),
        ('Teknik animasi yang memakai tanah liat atau plastisin disebut…', 'claymation', ['pixilation', 'object-motion', 'rotoscoping'], 'Bahan lunak dibentuk menjadi karakter.', 'Disangga armature.'),
        ('Kerangka kawat pada karakter claymation disebut…', 'armature', ['rigging', 'skeleton', 'wireframe'], 'Armature memudahkan perpindahan gerakan.', 'Menjaga bentuk karakter.'),
        ('Contoh film dengan teknik object-motion adalah…', 'Lego the Movie', ['Chicken Run', 'Toy Story', 'The Matrix'], 'Object-motion menggerakkan benda padat.', 'Mainan dan balok menjadi karakter.'),
        ('Animasi yang menggunakan manusia sebagai objek disebut…', 'pixilation', ['claymation', 'object-motion', 'cell animation'], 'Manusia diposisikan ulang tiap frame.', 'Gerakan tampak jenaka.'),
        ('Alat Lumiere Brothers untuk merekam gambar bergerak bernama…', 'cinematographe', ['praxinoscope', 'mutoscope', 'vitascope'], 'Cinematographe dipakai sejak 1895.', 'Cikal bakal teknologi film.'),
        ('Format standar pengiriman film ke bioskop digital adalah…', 'Digital Cinema Package', ['Blu-ray disc', 'VHS tape', 'MPEG-1'], 'DCP diputar proyektor digital.', 'Bitrate sekitar 250 Mbps.'),
        ('DCP yang terenkripsi dibuka menggunakan…', 'Key Delivery Message', ['password bioskop', 'QR code tiket', 'serial number proyektor'], 'KDM menjadi kunci pemutaran.', 'Mencegah pemutaran tanpa izin.'),
        ('Tahap siklus hidup produk yang paling menguntungkan adalah…', 'kematangan', ['introduksi', 'pertumbuhan', 'penurunan'], 'Produk sudah dikenal dan biaya menurun.', 'Namun kompetitor mulai muncul.'),
        ('Tahap siklus hidup saat produk tergantikan produk lain adalah…', 'penurunan', ['introduksi', 'pertumbuhan', 'kematangan'], 'Decline terjadi saat produk jenuh.', 'Perlu inovasi ulang.'),
        ('Animasi dianggap ilusi gerak karena…', 'rangkaian gambar diam diputar kembali secara cepat', ['gambar dibuat berwarna', 'suara ditambahkan', 'film diputar lambat'], 'Mata melihat perubahan posisi sebagai gerak.', 'Prinsip dasar animasi.'),
    ],
    'multi': [
        ('Manakah tonggak sejarah animasi dunia?', ['Humorous Phases of Funny Faces (1906)', 'Steamboat Willie (1928)', 'Cell animation (1914)'], ['Lego the Movie (2014)', 'Chicken Run (2000)', 'Toy Story (1995)'], 'Ketiganya penanda awal sejarah animasi.', 'Sisanya karya modern.'),
        ('Manakah ciri animasi stop-motion?', ['Objek dipindahkan bertahap', 'Direkam per frame', 'Frame digabung menjadi gerak'], ['Digambar langsung di komputer', 'Tanpa perekaman gambar'], 'Stop-motion bersifat fisik.', 'Frame dirangkai menghasilkan ilusi gerak.'),
        ('Manakah bahan yang dipakai claymation?', ['Tanah liat', 'Plastisin', 'Lilin'], ['Besi', 'Kaca', 'Air'], 'Claymation memakai bahan lunak.', 'Bahan lunak mudah dibentuk.'),
        ('Manakah tahap product life cycle?', ['Introduksi', 'Pertumbuhan', 'Kematangan'], ['Produksi massal', 'Distribusi kabel', 'Audisi'], 'Siklus hidup produk empat tahap.', 'Ditutup tahap penurunan.'),
        ('Manakah contoh penggunaan CGI/VFX dalam film?', ['Toy Story (1995)', 'The Matrix (1999)', 'Tron (1982)'], ['Pauvre Pierrot (1892)', 'Humorous Phases of Funny Faces (1906)'], 'CGI dan VFX inovasi film digital.', 'Film 1892–1906 belum memakai CGI.'),
        ('Manakah media penyimpanan DCP fisik?', ['Flash drive', 'USB drive eksternal', 'CRU Solo'], ['Pita kaset', 'Disket', 'Kartu memori kamera'], 'DCP dikirim dalam media penyimpanan.', 'Pita dan disket sudah usang.'),
        ('Manakah faktor yang memengaruhi siklus hidup produk animasi?', ['Perkembangan teknologi', 'Permintaan pasar', 'Munculnya kompetitor'], ['Jumlah kursi bioskop', 'Warna poster', 'Nama studio'], 'Siklus dipengaruhi pasar dan teknologi.', 'Warna poster bukan faktor utama.'),
        ('Manakah yang perlu dilakukan pada tahap introduksi?', ['Beriklan di media cetak', 'Membuat poster', 'Menayangkan trailer'], ['Menurunkan kualitas', 'Menghapus produk', 'Menutup studio'], 'Introduksi bertujuan memperkenalkan produk.', 'Promosi membangun kesadaran pasar.'),
    ],
    'pairs': [
        ('Praxinoscope', 'alat proyeksi Reynaud'),
        ('Cell animation', 'Earl Hurd, 1914'),
        ('Steamboat Willie', 'animasi pertama bersuara'),
        ('Claymation', 'stop-motion berbahan tanah liat'),
        ('Armature', 'kerangka kawat karakter clay'),
        ('Pixilation', 'manusia sebagai objek animasi'),
        ('DCP', 'format film bioskop digital'),
        ('KDM', 'kunci pembuka DCP'),
    ],
    'steps': [
        ('Urutkan tonggak sejarah animasi.', ['Praxinoscope karya Reynaud', 'Humorous Phases of Funny Faces', 'Cell animation Earl Hurd', 'Steamboat Willie', 'Toy Story dengan CGI'], 'Sejarah dimulai dari alat proyeksi sederhana.', 'CGI menutup rangkaian tonggak.'),
        ('Urutkan tahap product life cycle.', ['Introduksi', 'Pertumbuhan', 'Kematangan', 'Penurunan'], 'Produk dimulai dari perkenalan.', 'Siklus ditutup penurunan.'),
        ('Urutkan proses pembuatan animasi stop-motion.', ['Menyiapkan objek dan set', 'Memindahkan objek setahap', 'Merekam tiap frame', 'Menggabungkan frame', 'Menambahkan suara dan efek'], 'Stop-motion dikerjakan bertahap.', 'Suara menutup proses.'),
        ('Urutkan perkembangan teknologi film.', ['Cinematographe 1895', 'Film berwarna three-colour system', 'Perekaman digital 2000-an', 'Proyektor dan DCP bioskop digital'], 'Teknologi film terus berkembang.', 'DCP menjadi standar bioskop digital.'),
        ('Urutkan langkah memperpanjang siklus hidup produk animasi.', ['Membaca data penonton', 'Melakukan inovasi cerita', 'Memperluas pasar', 'Mengembangkan lisensi', 'Mengevaluasi hasil'], 'Inovasi berawal dari data.', 'Evaluasi menutup siklus perbaikan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)