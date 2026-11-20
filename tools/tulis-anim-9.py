"""ANIM 9 — Pembuatan Gerak Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 9',
    'slug': 'anim-9-pembuatan-gerak',
    'title': 'Pembuatan Gerak Animasi',
    'description': (
        'Memahami objek karakter dan nonkarakter, menguasai 12 prinsip '
        'animasi warisan Frank Thomas dan Ollie Johnston, serta membuat '
        'keypose dan in between untuk gerakan yang realistis.'
    ),
    'objectives': [
        'Membedakan objek karakter dan nonkarakter serta jenis geraknya.',
        'Menjelaskan dan menerapkan 12 prinsip animasi.',
        'Membuat keypose gerakan karakter.',
        'Membuat gambar in between yang konsisten dengan keypose.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 9 Pembuatan Gerak Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Gerak lokomotor', 'definition': 'Perpindahan gerak objek karakter dari satu titik ke titik lain.'},
        {'term': 'Squash and stretch', 'definition': 'Prinsip elastisitas yang memberi efek plastis pada objek.'},
        {'term': 'Anticipation', 'definition': 'Gerakan persiapan atau ancang-ancang sebelum gerakan utama.'},
        {'term': 'Staging', 'definition': 'Penempatan karakter pada kamera agar suasana adegan jelas.'},
        {'term': 'Straight ahead action', 'definition': 'Menggambar frame demi frame berurutan seorang diri.'},
        {'term': 'Pose to pose', 'definition': 'Metode kerja key animator dan inbetweener secara terpisah.'},
        {'term': 'Follow through', 'definition': 'Bagian tubuh yang masih bergerak setelah karakter berhenti.'},
        {'term': 'Slow in dan slow out', 'definition': 'Perubahan kecepatan gerakan saat mulai dan berhenti.'},
        {'term': 'Exaggeration', 'definition': 'Mendramatisasi gerakan secara hiperbolis untuk menegaskan aksi.'},
        {'term': 'Keypose', 'definition': 'Gambar posisi kunci atau ekstrem dari gerakan karakter.'},
        {'term': 'In between', 'definition': 'Gambar pengisi antara dua keypose agar gerakan tampak halus.'},
    ],
    'intro': {
        'material_title': 'Objek dan gerak animasi',
        'title': 'Karakter, nonkarakter, dan jenis geraknya',
        'paragraphs': [
            'Gerakan dalam animasi adalah gerakan buatan yang meniru gerakan nyata; animator harus memahami sendi-sendi yang dapat digerakkan dan kaitannya satu sama lain.',
            'Objek karakter adalah objek yang seolah hidup dan bergerak atas inisiatif sendiri, misalnya manusia, hewan, dan tumbuhan.',
            'Objek nonkarakter bergerak karena stimulus objek lain, misalnya kamera, lighting, dan properti mekanik seperti sepeda atau mobil.',
            'Objek karakter memiliki tiga jenis gerak: lokomotor (berpindah tempat), nonlokomotor (tanpa perpindahan), dan manipulatif (menggunakan alat atau objek).',
        ],
        'diagram': (
            'Pembagian objek dalam animasi',
            'flowchart TB\n'
            '  A[Objek animasi] --> B[Objek karakter]\n'
            '  A --> C[Objek nonkarakter]\n'
            '  B --> D[Gerak lokomotor]\n'
            '  B --> E[Gerak nonlokomotor]\n'
            '  B --> F[Gerak manipulatif]\n'
            '  C --> G[Kamera, lighting, properti mekanik]',
        ),
        'callout': 'Gerak lokomotor berpindah tempat, nonlokomotor bergerak di tempat, manipulatif melibatkan objek lain seperti bola atau alat.',
        'checkpoint': (
            'Objek yang bergerak karena stimulus objek lain disebut…',
            [
                ('objek nonkarakter', True),
                ('objek karakter', False),
                ('objek utama', False),
                ('objek statis', False),
            ],
            'Contohnya kamera, lighting, dan properti mekanik.',
        ),
    },
    'concept': {
        'material_title': '12 prinsip animasi',
        'title': 'Warisan Frank Thomas dan Ollie Johnston',
        'paragraphs': [
            '12 prinsip animasi dirumuskan sekitar tahun 1930 oleh Frank Thomas dan Ollie Johnston dari Walt Disney Studio dalam buku The Illusion of Life.',
            'Prinsip tersebut meliputi squash and stretch, anticipation, staging, straight ahead action and pose to pose, follow through and overlapping action, dan slow in and slow out.',
            'Prinsip lainnya adalah arch (gerak melengkung), secondary action, timing and spacing, appeal, exaggeration, dan solid drawing.',
            'Prinsip-prinsip ini membantu animator mempertegas ekspresi, gestur, dan kepribadian karakter sehingga gerakan terasa realistis, dinamis, dan dramatis.',
        ],
        'table': [
            ['Prinsip', 'Inti'],
            ['Squash and stretch', 'Elastisitas dan efek plastis objek'],
            ['Anticipation', 'Gerakan persiapan sebelum aksi utama'],
            ['Staging', 'Penempatan karakter agar adegan terbaca'],
            ['Follow through', 'Bagian tubuh yang masih bergerak setelah berhenti'],
            ['Slow in slow out', 'Gerakan melambat lalu mempercepat dan sebaliknya'],
            ['Exaggeration', 'Gerakan hiperbolis untuk menegaskan aksi'],
            ['Solid drawing', 'Kemampuan menggambar: proporsi, anatomi, komposisi'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-9-prinsip',
            'engine': 'mermaid',
            'title': 'Kelompok penerapan 12 prinsip animasi',
            'code': 'flowchart TB\n'
                    '  A[12 prinsip animasi] --> B[Dasar pergerakan: squash dan anticipation]\n'
                    '  A --> C[Pengaturan adegan: staging dan timing]\n'
                    '  A --> D[Pengayaan visual: follow through dan secondary action]\n'
                    '  A --> E[Teknik gerak: pose to pose dan in between]',
        },
        'activity': categorize_block(
            'anim-9-klasifikasi',
            'Kelompokkan contoh gerak sesuai jenis gerak objek karakter.',
            [('b1', 'Lokomotor'), ('b2', 'Nonlokomotor'), ('b3', 'Manipulatif')],
            [
                ('i1', 'Berjalan dan berlari', 'b1'),
                ('i2', 'Melompat ke depan', 'b1'),
                ('i3', 'Menekuk lutut di tempat', 'b2'),
                ('i4', 'Memutar badan tanpa berpindah', 'b2'),
                ('i5', 'Menendang bola', 'b3'),
                ('i6', 'Melempar dan menangkap', 'b3'),
            ],
            'Tepat. Lokomotor berpindah, nonlokomotor di tempat, manipulatif memakai objek.',
            'Ingat: berpindah tempat = lokomotor; pakai objek = manipulatif.',
        ),
        'subtitle': 'Keypose dan in between',
        'list': [
            'Keypose adalah gambar posisi kunci atau ekstrem: gerakan awal, gerakan ekstrem, dan gerakan terakhir.',
            'Key animator membuat keypose dengan memperhatikan 12 prinsip animasi.',
            'In between adalah gambar pengisi antara keypose; jumlahnya bergantung durasi gerakan.',
            'Keberhasilan adegan terjadi bila key animator dan inbetweener menerjemahkan gerakan secara konsisten sehingga hasilnya realistis dan mudah diperbaiki.',
        ],
        'checkpoint': (
            '12 prinsip animasi dirumuskan oleh…',
            [
                ('Frank Thomas dan Ollie Johnston', True),
                ('Walt Disney dan Ub Iwerks', False),
                ('Nick Park dan Peter Lord', False),
                ('Earl Hurd dan Stuart Blackton', False),
            ],
            'Keduanya animator Disney, menulis The Illusion of Life.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menghidupkan gerakan',
        'paragraphs': [
            'Contoh squash and stretch: bola bulat yang jatuh menjadi lonjong horizontal lalu berubah lonjong diagonal saat memantul.',
            'Metode straight ahead action punya kelebihan gambar konsisten karena dikerjakan satu animator, tetapi sulit merencanakan akhir adegan dan memakan waktu.',
            'Metode pose to pose dipakai industri karena melibatkan banyak anggota tim sehingga waktu pengerjaan lebih cepat.',
        ],
        'scenario': scenario(
            'anim-9-skenario',
            'Gerakan kaku dan tidak meyakinkan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Animasi berjalan karaktermu terasa kaku. Apa yang kamu perbaiki?',
                    'choices': [
                        {'text': 'Menambah in between dan menerapkan slow in slow out', 'next': 'n2', 'score': 2, 'feedback': 'Kecepatan bertahap dan frame pengisi membuat gerak halus.'},
                        {'text': 'Menghapus semua gambar antara agar cepat selesai', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa in between gerakan menjadi patah-patah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Agar gerakan terasa hidup, prinsip apa yang perlu ditambahkan?',
                    'choices': [
                        {'text': 'Anticipation sebelum gerak dan follow through sesudahnya', 'next': 'n4', 'score': 2, 'feedback': 'Ancang-ancang dan gerak lanjutan membuat aksi realistis.'},
                        {'text': 'Menghilangkan gerakan persiapan agar langsung', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa anticipation gerakan terasa mendadak.'},
                    ],
                },
                {'id': 'n3', 'text': 'Gerakan tetap kaku dan penonton tidak tertarik.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Gerakan tampak hidup, dinamis, dan meyakinkan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan 12 prinsip animasi.', 'back': 'Squash and stretch, anticipation, staging, straight ahead and pose to pose, follow through, slow in slow out, arch, secondary action, timing and spacing, appeal, exaggeration, solid drawing.'},
            {'front': 'Apa itu keypose?', 'back': 'Gambar posisi kunci atau ekstrem dari gerakan karakter.'},
            {'front': 'Siapa pembuat in between?', 'back': 'Inbetweener.'},
            {'front': 'Apa kelebihan pose to pose?', 'back': 'Waktu pengerjaan lebih cepat karena melibatkan banyak anggota tim.'},
        ],
        'checkpoint': (
            'Bagian tubuh yang masih bergerak setelah karakter berhenti disebut…',
            [
                ('follow through', True),
                ('anticipation', False),
                ('staging', False),
                ('solid drawing', False),
            ],
            'Contohnya rambut yang masih bergerak setelah berlari.',
        ),
        'challenge': challenge_block(
            'anim-9-tantangan',
            'Tantangan prinsip animasi',
            90,
            [
                ('Prinsip elastisitas pada objek', 'Squash and stretch'),
                ('Gerakan persiapan sebelum aksi', 'Anticipation'),
                ('Metode menggambar frame demi frame', 'Straight ahead action'),
                ('Gambar posisi kunci gerakan', 'Keypose'),
                ('Gambar pengisi antara keypose', 'In between'),
            ],
            'Lima istilah prinsip animasi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('12 prinsip animasi dirumuskan sekitar tahun 1930 oleh…', 'Frank Thomas dan Ollie Johnston', ['Walt Disney dan Earl Hurd', 'Nick Park dan Peter Lord', 'Stuart Blackton dan Winsor McCay'], 'Keduanya animator Disney.', 'Buku The Illusion of Life.'),
        ('Prinsip yang menambahkan efek plastis pada objek disebut…', 'squash and stretch', ['anticipation', 'staging', 'appeal'], 'Disebut juga prinsip elastisitas.', 'Bola memantul jadi lonjong.'),
        ('Gerakan persiapan atau ancang-ancang disebut…', 'anticipation', ['follow through', 'arch', 'timing'], 'Contoh: menekuk lutut sebelum melompat.', 'Membuat gerak meyakinkan.'),
        ('Prinsip menempatkan karakter pada kamera agar adegan jelas adalah…', 'staging', ['solid drawing', 'appeal', 'secondary action'], 'Siluet memperjelas interaksi.', 'Penonton mudah mengikuti cerita.'),
        ('Metode menggambar frame by frame berurutan seorang diri disebut…', 'straight ahead action', ['pose to pose', 'in between', 'staging'], 'Disebut metode tradisional.', 'Gambar konsisten tetapi lama.'),
        ('Metode yang melibatkan key animator dan inbetweener disebut…', 'pose to pose', ['straight ahead action', 'rotoscoping', 'motion capture'], 'Dipakai industri karena lebih cepat.', 'Melibatkan banyak orang.'),
        ('Rambut yang masih bergerak setelah karakter berhenti adalah contoh…', 'follow through', ['anticipation', 'exaggeration', 'appeal'], 'Overlapping action gerakan bertindihan.', 'Menambah realisme gerak.'),
        ('Prinsip slow in slow out menjelaskan bahwa…', 'objek mempercepat dan memperlambat gerakan secara bertahap', ['objek bergerak konstan', 'objek selalu diam', 'objek bergerak mundur'], 'Gerakan tidak instan.', 'Menghindari gerak kaku.'),
        ('Prinsip yang menitikberatkan kemampuan menggambar animator adalah…', 'solid drawing', ['appeal', 'staging', 'timing'], 'Mencakup proporsi dan anatomi.', 'Memperkuat karakteristik tokoh.'),
        ('Prinsip untuk mendramatisasi gerakan secara hiperbolis adalah…', 'exaggeration', ['anticipation', 'arch', 'follow through'], 'Sering dipakai film komedi.', 'Menegaskan ekspresi.'),
        ('Prinsip yang membuat film punya gaya khas dan karakter unik adalah…', 'appeal', ['solid drawing', 'staging', 'slow out'], 'Appeal sebagai gaya visual.', 'Juga pembeda penokohan.'),
        ('Keypose berada pada…', 'gerakan kunci awal, ekstrem, dan terakhir', ['setiap frame gerakan', 'hanya frame pertama', 'hanya frame akhir'], 'Keypose menandai posisi penting.', 'Dibuat key animator.'),
        ('Jumlah gambar in between bergantung pada…', 'durasi gerakan dari satu keypose ke keypose berikutnya', ['jumlah karakter', 'warna latar', 'panjang dialog'], 'Semakin lama makin banyak frame.', 'Dibuat inbetweener.'),
        ('Penerapan squash and stretch pada benda mati membuat benda…', 'tampak seperti benda hidup', ['tidak bergerak', 'berubah warna', 'menghilang'], 'Efek dinamis pada gerakan.', 'Menambah daya tarik visual.'),
    ],
    'multi': [
        ('Manakah prinsip animasi?', ['Squash and stretch', 'Anticipation', 'Staging'], ['Rendering', 'Compositing', 'Dubbing'], '12 prinsip membangun gerak.', 'Sisanya tahap produksi.'),
        ('Manakah jenis gerak objek karakter?', ['Lokomotor', 'Nonlokomotor', 'Manipulatif'], ['Mekanik', 'Statis', 'Alami'], 'Tiga jenis gerak karakter.', 'Mekanik untuk objek nonkarakter.'),
        ('Manakah contoh objek nonkarakter?', ['Kamera', 'Lighting', 'Sepeda'], ['Manusia', 'Hewan', 'Tumbuhan'], 'Objek nonkarakter digerakkan stimulus.', 'Manusia dan hewan adalah karakter.'),
        ('Manakah ciri straight ahead action?', ['Digambar frame by frame', 'Dikerjakan seorang diri', 'Hasilnya konsisten'], ['Melibatkan dua orang', 'Selalu cepat', 'Tidak butuh perencanaan'], 'Metode ini konsisten tetapi lama.', 'Kesulitan merencanakan akhir adegan.'),
        ('Manakah ciri pose to pose?', ['Dibuat key animator dan inbetweener', 'Waktu lebih cepat', 'Melibatkan tim lebih banyak'], ['Dikerjakan satu orang', 'Tanpa keypose', 'Tanpa in between'], 'Metode industri yang efisien.', 'Kerja dibagi dua peran.'),
        ('Manakah prinsip yang memengaruhi ekspresi gerak?', ['Exaggeration', 'Appeal', 'Anticipation'], ['Rendering', 'Compositing', 'Modelling'], 'Prinsip membentuk ekspresi karakter.', 'Sisanya tahap teknis produksi.'),
        ('Manakah yang termasuk susunan gerakan tiga bagian?', ['Gerakan persiapan', 'Gerakan inti', 'Gerakan akhir'], ['Gerakan lambat', 'Gerakan cepat', 'Gerakan diam'], 'Anticipation bagian dari rangkaian.', 'Tiga bagian itu persiapan, inti, akhir.'),
        ('Manakah manfaat prinsip animasi bagi animator?', ['Gerakan lebih realistis', 'Karakter lebih ekspresif', 'Adegan lebih dramatis'], ['Menghapus kebutuhan menggambar', 'Menggantikan naskah', 'Menghapus storyboard'], 'Prinsip memperkuat gerak dan ekspresi.', 'Tidak menggantikan dokumen produksi.'),
    ],
    'pairs': [
        ('Squash and stretch', 'elastisitas objek'),
        ('Anticipation', 'gerakan ancang-ancang'),
        ('Staging', 'penempatan karakter di kamera'),
        ('Straight ahead action', 'menggambar frame berurutan'),
        ('Follow through', 'gerak lanjutan setelah berhenti'),
        ('Exaggeration', 'gerakan hiperbolis'),
        ('Solid drawing', 'kemampuan menggambar'),
        ('Keypose', 'gambar posisi kunci'),
    ],
    'steps': [
        ('Urutkan tiga bagian gerakan melompat.', ['Anticipation menekuk lutut', 'Gerakan inti melompat', 'Gerakan akhir mendarat', 'Follow through bagian tubuh', 'Kembali ke posisi diam'], 'Persiapan mendahului aksi.', 'Posisi diam menutup gerakan.'),
        ('Urutkan pekerjaan pose to pose.', ['Key animator membuat keypose', 'Menulis catatan gerak', 'Inbetweener membuat gambar antara', 'Pemeriksaan konsistensi', 'Penyempurnaan gerakan'], 'Keypose dibuat lebih dahulu.', 'Penyempurnaan akhir.'),
        ('Urutkan gerak bola memantul dengan squash and stretch.', ['Bola bulat di udara', 'Menjadi lonjong horizontal saat menyentuh tanah', 'Berubah lonjong diagonal saat memantul', 'Kembali bulat di puncak', 'Berulang sampai berhenti'], 'Bentuk berubah sesuai tekanan.', 'Gerak berulang lalu berhenti.'),
        ('Urutkan langkah membuat gerakan berjalan karakter.', ['Merekam video referensi gerak', 'Menentukan keypose', 'Membuat gambar in between', 'Menambahkan follow through', 'Memeriksa dengan pencil test'], 'Referensi menjadi dasar.', 'Pemeriksaan menutup proses.'),
        ('Urutkan pengembangan gaya animasi.', ['Memahami 12 prinsip', 'Melatih solid drawing', 'Menentukan appeal karakter', 'Menerapkan exaggeration sesuai genre', 'Evaluasi hasil gerak'], 'Prinsip dipahami dulu.', 'Evaluasi menutup pengembangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)