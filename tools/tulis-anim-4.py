"""ANIM 4 — Teknik Dasar Proses Produksi pada Industri Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 4',
    'slug': 'anim-4-teknik-proses-produksi',
    'title': 'Teknik Dasar Proses Produksi pada Industri Animasi',
    'description': (
        'Memahami pipeline produksi animasi 2D dan 3D, mengenal ekosistem '
        'industri animasi Indonesia, serta menerapkan sikap kerja tim, budaya '
        'kerja, kode etik, dan unit kerja di studio animasi.'
    ),
    'objectives': [
        'Menjelaskan tahapan pipeline produksi animasi 2 dimensi dan 3 dimensi.',
        'Menguraikan enam elemen ekosistem industri animasi.',
        'Menerapkan kerja tim dengan model Bruce Tuckman.',
        'Mengenali budaya kerja, kode etik, dan unit kerja studio animasi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 4 Teknik Dasar Proses Produksi pada Industri '
        'Animasi; CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Pipeline', 'definition': 'Sistem manusia, perangkat keras, dan perangkat lunak yang selaras untuk menyelesaikan produksi secara berurutan.'},
        {'term': 'Script', 'definition': 'Versi tertulis proyek berisi alur cerita, deskripsi, lokasi, dialog, dan efek suara.'},
        {'term': 'Storyboard', 'definition': 'Versi visual dari script berupa rangkaian gambar adegan.'},
        {'term': 'Key animator', 'definition': 'Animator utama yang menggambar gerakan kunci (keyframe) karakter.'},
        {'term': 'Inbetweener', 'definition': 'Animator yang mengisi frame antara keyframe agar gerakan halus.'},
        {'term': 'Clean up', 'definition': 'Membuat gambar raw menjadi tampilan akhir, membersihkan garis bantu.'},
        {'term': 'Inking and coloring', 'definition': 'Menebalkan garis pinggir dan memberi warna pada gambar.'},
        {'term': 'Dubbing', 'definition': 'Perekaman suara atau dialog oleh voice actor, termasuk penambahan bahasa dan soundtrack.'},
        {'term': 'Ekosistem', 'definition': 'Jaringan unit yang saling bergantung: ide, produksi, distribusi, pameran, apresiasi, dan pendidikan.'},
        {'term': 'Pencil test', 'definition': 'Cara memeriksa gerakan dengan memeriksa gambar-gambar berturut-turut.'},
    ],
    'intro': {
        'material_title': 'Pipeline produksi animasi',
        'title': 'Alur kerja yang terstruktur',
        'paragraphs': [
            'Proses mewujudkan film animasi disebut pipeline animasi atau alur kerja animasi: sebuah sistem yang terdiri atas manusia, perangkat keras, dan perangkat lunak yang bekerja terurut sesuai jadwal.',
            'Pipeline setiap film tidak selalu sama; bergantung pada kebutuhan, jenis animasi, biaya, dan kualitas yang diharapkan.',
            'Kedua jenis produksi, 2 dimensi dan 3 dimensi, selalu melewati lima tahap inti: praproduksi, produksi, dan pascaproduksi agar kualitas terjaga.',
        ],
        'diagram': (
            'Pipeline produksi animasi 2D',
            'flowchart LR\n'
            '  A[Praproduksi: ide, script, storyboard] --> B[Produksi: animating]\n'
            '  B --> C[Clean up]\n'
            '  C --> D[Inking and coloring]\n'
            '  D --> E[Pascaproduksi: compositing]\n'
            '  E --> F[Dubbing, export/rendering]',
        ),
        'callout': 'Pada tahap produksi 2D, key animator menggambar gerakan kunci dan inbetweener mengisi frame antara agar gerakan tampak mulus.',
        'checkpoint': (
            'Tahap pertama yang dipikirkan dalam membuat film animasi adalah…',
            [
                ('cerita atau ide', True),
                ('anggaran biaya', False),
                ('iklan film', False),
                ('jadwal rilis', False),
            ],
            'Cerita yang bagus lahir dari ide yang inspiratif.',
        ),
    },
    'concept': {
        'material_title': 'Pipeline 3D dan ekosistem',
        'title': 'Produksi 3D dan ekosistem industri animasi',
        'paragraphs': [
            'Pipeline produksi 3D mengikuti urutan modeling, rigging, texturing, animation, lighting, dan rendering, diakhiri compositing serta editing.',
            'Ekosistem industri animasi Indonesia merupakan penggabungan unit yang saling bergantung: konsep ide, produksi, distribusi dan promosi, pameran, apresiasi, serta pendidikan.',
            'Sekitar 86% orang Indonesia masih menonton televisi, sehingga televisi menjadi media distribusi dan promosi utama bagi studio animasi.',
            'Pameran seperti Indonesia Comic Con dan INAMAFEST menjadi media apresiasi, prestasi, dan edukasi bagi pelaku animasi.',
        ],
        'table': [
            ['Elemen ekosistem', 'Peran'],
            ['Konsep ide', 'Sumber cerita dari adaptasi, komik, atau buku'],
            ['Produksi', 'Praproduksi hingga pascaproduksi'],
            ['Distribusi dan promosi', 'Televisi, bioskop, media sosial, layanan streaming'],
            ['Pameran', 'Media apresiasi, prestasi, dan edukasi'],
            ['Apresiasi', 'Menumbuhkan jiwa kompetisi sehat'],
            ['Pendidikan', 'Formal dan nonformal, dari SMK hingga perguruan tinggi'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-4-3d',
            'engine': 'mermaid',
            'title': 'Pipeline produksi animasi 3D',
            'code': 'flowchart LR\n'
                    '  A[Modeling] --> B[Rigging]\n'
                    '  B --> C[Texturing]\n'
                    '  C --> D[Animation]\n'
                    '  D --> E[Lighting]\n'
                    '  E --> F[Rendering]\n'
                    '  F --> G[Compositing dan editing]',
        },
        'activity': categorize_block(
            'anim-4-klasifikasi',
            'Kelompokkan kegiatan ke dalam tahap produksi 2D atau pascaproduksi 2D.',
            [('b1', 'Produksi 2D'), ('b2', 'Pascaproduksi 2D')],
            [
                ('i1', 'Menggambar keyframe gerakan kunci', 'b1'),
                ('i2', 'Mengisi frame antara (inbetween)', 'b1'),
                ('i3', 'Menebalkan garis dan memberi warna', 'b1'),
                ('i4', 'Menyatukan scene dan audio (compositing)', 'b2'),
                ('i5', 'Rekaman suara oleh voice actor', 'b2'),
                ('i6', 'Export video dengan resolusi tertentu', 'b2'),
            ],
            'Tepat. Produksi membuat gambar; pascaproduksi merapikan dan mengekspor.',
            'Ingat: menggambar dan mewarnai produksi; compositing dan dubbing pascaproduksi.',
        ),
        'subtitle': 'Sikap kerja di studio',
        'list': [
            'Kerja tim membuat ide lebih kreatif, beban lebih ringan, pekerjaan lebih efisien, dan cepat menemukan solusi saat ada hambatan.',
            'Model Bruce Tuckman menggambarkan lima tahap: forming, storming, norming, performing, dan adjourning.',
            'Budaya kerja, kode etik, dan unit-unit kerja membantu pembagian tugas dan tanggung jawab di studio animasi.',
            'Studio seperti Walt Disney membagi unit produksi menjadi production teams, technology teams, dan studio teams.',
        ],
        'checkpoint': (
            'Studio animasi Walt Disney membagi devisinya menjadi…',
            [
                ('production, technology, dan studio teams', True),
                ('animasi, iklan, dan berita', False),
                ('akuntansi, hukum, dan pajak', False),
                ('video, audio, dan teks', False),
            ],
            'Pembagian unit memudahkan pembagian tugas.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bekerja dalam tim produksi',
        'paragraphs': [
            'Pada tahap storming, perbedaan kepribadian dan cara bekerja memicu konflik; pemimpin perlu berkomunikasi, menegaskan tugas, dan membina anggota.',
            'Pada tahap norming, tim menyetujui rencana, jadwal, dan tugas sesuai kompetensi, lalu kepercayaan dan saling membantu tumbuh.',
            'Tweening dilakukan dengan 24 gambar per detik sehingga gerakan tampak halus dan nyata.',
        ],
        'scenario': scenario(
            'anim-4-skenario',
            'Konflik di tengah produksi',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Studio animasimu baru memulai proyek. Bagaimana agar tim bekerja efektif?',
                    'choices': [
                        {'text': 'Menggelar forming: saling mengenal dan membagi tugas', 'next': 'n2', 'score': 2, 'feedback': 'Forming membantu anggota memahami tujuan dan perannya.'},
                        {'text': 'Langsung bekerja masing-masing tanpa koordinasi', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa pembagian peran tim mudah kacau.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Di tengah jalan muncul konflik karena perbedaan cara bekerja. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Pemimpin berkomunikasi, menegaskan tugas, dan menyelesaikan konflik', 'next': 'n4', 'score': 2, 'feedback': 'Penanganan storming menjaga performa tim.'},
                        {'text': 'Membiarkan konflik hingga tim pecah', 'next': 'n3', 'score': 0, 'feedback': 'Konflik yang tidak ditangani menghancurkan produksi.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tim kacau, produksi molor, dan proyek gagal.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tim mencapai norming dan performing, proyek selesai sesuai jadwal.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu pipeline animasi?', 'back': 'Sistem manusia, perangkat keras, dan lunak yang bekerja terurut sesuai jadwal.'},
            {'front': 'Sebutkan tiga tahap utama produksi animasi.', 'back': 'Praproduksi, produksi, pascaproduksi.'},
            {'front': 'Sebutkan elemen ekosistem animasi Indonesia.', 'back': 'Ide, produksi, distribusi, pameran, apresiasi, pendidikan.'},
            {'front': 'Sebutkan lima tahap model Tuckman.', 'back': 'Forming, storming, norming, performing, adjourning.'},
        ],
        'checkpoint': (
            'Proses perekaman suara atau dialog oleh voice actor disebut…',
            [
                ('dubbing', True),
                ('compositing', False),
                ('clean up', False),
                ('inking', False),
            ],
            'Dubbing adalah pengisian suara dan dialog.',
        ),
        'challenge': challenge_block(
            'anim-4-tantangan',
            'Tantangan istilah proses produksi',
            90,
            [
                ('Sistem alur kerja produksi animasi', 'Pipeline'),
                ('Gambar gerakan kunci karakter', 'Keyframe'),
                ('Animasi pengisi frame antara', 'Inbetweener'),
                ('Perekaman suara voice actor', 'Dubbing'),
                ('Versi visual dari script', 'Storyboard'),
            ],
            'Lima istilah proses produksi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Pipeline animasi adalah sistem yang terdiri atas…', 'manusia, perangkat keras, dan perangkat lunak yang selaras', ['manusia dan ponsel saja', 'perangkat keras saja', 'kamera saja'], 'Pipeline menyelesaikan tugas produksi berurutan.', 'Sesuai jadwal perencanaan.'),
        ('Tahapan utama produksi animasi adalah…', 'praproduksi, produksi, dan pascaproduksi', ['konsep dan iklan', 'sketsa dan warna', 'rekaman dan cetak'], 'Ketiga tahap wajib diterapkan.', 'Berlaku 2D maupun 3D.'),
        ('Script berisi…', 'alur cerita, lokasi, dialog, dan efek suara', ['hanya gambaran warna', 'daftar harga', 'jadwal kursus'], 'Script adalah versi tertulis proyek.', 'Dibuat penulis skenario.'),
        ('Pembuat gerakan kunci (keyframe) disebut…', 'key animator', ['inbetweener', 'colorist', 'editor'], 'Animator utama mendesain gerakan.', 'Menjadi acuan gerak karakter.'),
        ('Inbetweener bertugas…', 'mengisi frame antara agar gerakan halus', ['menulis naskah', 'membuat musik', 'mengatur anggaran'], 'Tweening 24 gambar per detik.', 'Menambah kelancaran gerak.'),
        ('Animation clean up adalah…', 'menjadikan gambar raw bersih menjadi tampilan akhir', ['merusak gambar', 'menghapus adegan', 'mengulang produksi'], 'Garis bantu yang tidak perlu dibersihkan.', 'Diserahkan pada inking.'),
        ('Proses menebalkan garis dan memberi warna disebut…', 'inking and coloring', ['dubbing', 'compositing', 'rendering'], 'Garis ditebalkan di atas celluloid.', 'Diberi warna.'),
        ('Compositing dalam pascaproduksi 2D adalah…', 'menyatukan scene, audio, efek, dan teks', ['menggambar karakter', 'menulis dialog', 'merekrut staf'], 'Komponen disatukan menjadi film utuh.', 'Jika perlu diikuti final editing.'),
        ('Dubbing adalah…', 'proses perekaman suara atau dialog oleh voice actor', ['menggambar latar', 'memilih kamera', 'mencetak poster'], 'Voice actor mengisi dialog.', 'Menambah bahasa dan soundtrack.'),
        ('Model Bruce Tuckman tentang kerja tim meliputi…', 'forming, storming, norming, performing, adjourning', ['memancing, memutar, melukis', 'masak, makan, cuci', 'belajar, ulangan, libur'], 'Lima tahap evolusi tim.', 'Dari perkenalan hingga pembubaran.'),
        ('Pada tahap storming, anggota tim…', 'menghadapi konflik akibat perbedaan cara bekerja', ['bersikap sopan dan menghindari konflik', 'membubarkan studio', 'mengganti semua staf'], 'Perbedaan memicu konflik.', 'Pemimpin menegaskan tugas.'),
        ('Ekosistem animasi Indonesia meliputi…', 'ide, produksi, distribusi, pameran, apresiasi, dan pendidikan', ['tanah, air, udara', 'harga, promo, diskon', 'tenaga, modal, pasar'], 'Unit saling bergantung terus-menerus.', 'Mendukung keberlangsungan industri.'),
        ('Media distribusi utama animasi di Indonesia adalah…', 'televisi', ['koran', 'radio FM', 'cerita rakyat'], 'Sekitar 86% orang menonton televisi.', 'Juga bioskop dan media sosial.'),
        ('Walt Disney membagi unit menjadi…', 'production, technology, dan studio teams', ['keuangan, hukum, pajak', 'lokal, nasional, global', 'senin, rabu, jumat'], 'Production teams berisi banyak tim khusus.', 'Memudahkan pembagian tugas.'),
    ],
    'multi': [
        ('Manakah tahapan praproduksi animasi?', ['Membuat ide', 'Menyusun script', 'Membuat storyboard'], ['Melakukan clean up', 'Melakukan dubbing'], 'Praproduksi merencanakan cerita.', 'Clean up dan dubbing bukan praproduksi.'),
        ('Manakah tahapan produksi animasi 2D?', ['Animating', 'Clean up', 'Inking and coloring'], ['Compositing', 'Pameran'], 'Produksi membuat dan mewarnai gambar.', 'Compositing pascaproduksi.'),
        ('Manakah tahapan pascaproduksi animasi 2D?', ['Compositing', 'Dubbing', 'Export/rendering'], ['Storyboard', 'Ink and coloring'], 'Pascaproduksi merapikan hasil akhir.', 'Storyboard praproduksi.'),
        ('Manakah urutan pipeline produksi 3D?', ['Modeling', 'Rigging', 'Texturing'], ['Dubbing', 'Iklan'], 'Modeling hingga texturing awal 3D.', 'Diakhiri lighting dan rendering.'),
        ('Manakah contoh pameran animasi?', ['Indonesia Comic Con', 'Festival Film Indonesia', 'INAMAFEST'], ['Pertandingan sepak bola', 'Konser musik rock'], 'Pameran wadah apresiasi dan edukasi.', 'Bukan ajang animasi.'),
        ('Manakah manfaat bekerja dalam tim?', ['Ide lebih kreatif', 'Beban lebih ringan', 'Cepat menemukan solusi'], ['Memperlambat pekerjaan', 'Menambah beban', 'Menyembunyikan masalah'], 'Kolaborasi menguatkan hasil.', 'Tim mempercepat penyelesaian masalah.'),
        ('Manakah sikap baik dalam kerja tim produksi?', ['Saling membantu', 'Menghargai perbedaan', 'Berkomunikasi terbuka'], ['Menolak memberi tahu', 'Bekerja sendiri-sendiri', 'Mengabaikan anggota lain'], 'Tim sinergi demi misi studio.', 'Perpecahan merugikan produksi.'),
        ('Manakah tugas key animator?', ['Menggambar gerakan kunci', 'Membuat catatan penempatan inbetween', 'Menentukan jarak gerakan'], ['Menulis iklan', 'Mencetak poster', 'Menghitung harga karcis'], 'Key animator mengatur gerak utama.', 'Bekerja dengan inbetweener.'),
    ],
    'pairs': [
        ('Script', 'versi tertulis proyek'),
        ('Storyboard', 'versi visual script'),
        ('Key animator', 'menggambar keyframe'),
        ('Inbetweener', 'mengisi frame antara'),
        ('Clean up', 'membersihkan gambar'),
        ('Compositing', 'menyatukan komponen'),
        ('Dubbing', 'perekaman dialog'),
        ('Pencil test', 'memeriksa gerakan animasi'),
    ],
    'steps': [
        ('Urutkan pipeline produksi animasi 2D.', ['Ide dan script', 'Storyboard', 'Animating', 'Clean up', 'Ink and coloring'], 'Berawal dari cerita.', 'Warna menutup produksi 2D.'),
        ('Urutkan pipeline produksi animasi 3D.', ['Modeling', 'Rigging', 'Texturing', 'Animation dan lighting', 'Rendering'], 'Model dibuat terlebih dahulu.', 'Rendering menghasilkan gambar final.'),
        ('Urutkan tahap kerja tim Tuckman.', ['Forming', 'Storming', 'Norming', 'Performing', 'Adjourning'], 'Tim dimulai dari pembentukan.', 'Diakhiri pembubaran atau penutupan.'),
        ('Urutkan pascaproduksi animasi 2D.', ['Compositing', 'Final editing', 'Dubbing', 'Export/rendering', 'Distribusi'], 'Komponen disatukan dulu.', 'Distribusi menutup alur.'),
        ('Urutkan alur distribusi karya animasi.', ['Selesai produksi', 'Compositing dan editing', 'Pembuatan media promosi', 'Tayang di televisi dan bioskop', 'Apresiasi dan pameran'], 'Diawali hasil produksi.', 'Apresiasi menutup siklus ekosistem.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)