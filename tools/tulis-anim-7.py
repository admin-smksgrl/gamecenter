"""ANIM 7 — Aplikasi Berbasis Teknologi untuk Kebutuhan Industri Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 7',
    'slug': 'anim-7-aplikasi-teknologi',
    'title': 'Aplikasi Berbasis Teknologi untuk Kebutuhan Industri Animasi',
    'description': (
        'Mengenal beragam aplikasi animasi 2D dan 3D, memahami spesifikasi '
        'perangkat yang dibutuhkan, serta menguasai dasar Photoshop untuk '
        'animasi 2D dan Blender untuk animasi 3D.'
    ),
    'objectives': [
        'Mengidentifikasi aplikasi animasi 2D dan 3D beserta contoh karya.',
        'Membaca dan mencocokkan spesifikasi perangkat dengan aplikasi.',
        'Menguasai dasar antarmuka, inking, clean up, dan coloring di Photoshop.',
        'Menguasai dasar navigasi, modeling, material, lighting, dan rendering di Blender.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 7 Aplikasi Berbasis Teknologi untuk '
        'Kebutuhan Industri Animasi; CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Adobe Animate', 'definition': 'Aplikasi animasi 2D untuk kartun, iklan, dan game yang dapat dipublikasikan ke HTML5 dan WebGL.'},
        {'term': 'Toon Boom Harmony', 'definition': 'Aplikasi animasi seri TV dan film dengan fitur paperless dan cut-out.'},
        {'term': 'TVPaint', 'definition': 'Aplikasi animasi berbasis bitmap yang merepresentasikan media seni alami.'},
        {'term': 'After Effect', 'definition': 'Aplikasi untuk motion graphic, visual FX, dan compositing.'},
        {'term': 'Blender', 'definition': 'Aplikasi 3D gratis dengan fitur rendering, modeling, sculpting, animasi, dan VFX.'},
        {'term': 'Autodesk Maya', 'definition': 'Software 3D profesional untuk karakter realistik dan detail.'},
        {'term': 'Inking', 'definition': 'Menebalkan garis sketsa pada layer baru memakai brush tool.'},
        {'term': 'Clean up', 'definition': 'Membersihkan dan menebalkan garis akhir memakai brush yang lebih tebal.'},
        {'term': 'Viewport', 'definition': 'Area 3D untuk berinteraksi dengan scene saat membuat model dan animasi.'},
        {'term': 'Render engine', 'definition': 'Mesin render Blender: eevee, workbench, dan cycles.'},
    ],
    'intro': {
        'material_title': 'Aplikasi animasi 2D dan 3D',
        'title': 'Dari pensil ke perangkat digital',
        'paragraphs': [
            'Dulu animasi dibuat dengan pensil, cat, dan kertas. Kini perangkat digital dan berbagai aplikasi membuka peluang baru bagi animator sebagai digital artist.',
            'Aplikasi 2D populer antara lain Adobe Animate, Toon Boom Harmony, TVPaint, Adobe After Effect, serta versi web (Animaker, Powtoon) dan android (FlipaClip).',
            'Aplikasi 3D meliputi Autodesk Maya, 3ds Max, Blender (gratis), dan Cinema 4D, dengan versi web (Tinkercad) dan android (Toontastic 3D).',
            'Setiap aplikasi memiliki spesifikasi minimal perangkat agar berjalan baik, misalnya prosesor, RAM, GPU, dan resolusi layar.',
        ],
        'diagram': (
            'Gambaran ringkas aplikasi animasi',
            'flowchart LR\n'
            '  A[Animasi 2D] --> B[Adobe Animate, Toon Boom]\n'
            '  A --> C[TVPaint, After Effect]\n'
            '  D[Animasi 3D] --> E[Maya, 3ds Max]\n'
            '  D --> F[Blender, Cinema 4D]\n'
            '  B & C & E & F --> G[Perangkat sesuai spek minimal]',
        ),
        'callout': 'Cek dulu spesifikasi komputer (RAM, prosesor, GPU) sebelum menginstal aplikasi animasi agar hasil kerja maksimal.',
        'checkpoint': (
            'Aplikasi 3D yang gratis dan berfitur lengkap adalah…',
            [
                ('Blender', True),
                ('Photoshop', False),
                ('Toon Boom', False),
                ('Adobe Animate', False),
            ],
            'Blender gratis dengan fitur rendering dan modeling.',
        ),
    },
    'concept': {
        'material_title': 'Dasar Photoshop',
        'title': 'Antarmuka, inking, clean up, dan coloring',
        'paragraphs': [
            'Photoshop menyediakan fitur melukis dengan brush tool dan pencil tool serta mengedit warna gambar, berguna saat membuat aset gambar animasi 2D.',
            'Antarmuka Photoshop pada workspace painting mencakup document window, toolbar, option bar, status bar, expanding panels, dan panel groups.',
            'Proses membuat aset dilakukan berurutan: inking (menebalkan garis sketsa), clean up (membersihkan dan menebalkan garis akhir), lalu coloring (mewarnai pada layer di bawah clean up).',
            'Layer yang sudah jadi dapat digrup (Ctrl+G) dan digabung (Ctrl+E) sehingga memudahkan pengelolaan gambar.',
        ],
        'table': [
            ['Kegiatan', 'Langkah utama', 'Alat'],
            ['Inking', 'Buat layer baru di atas sketsa', 'Brush tool'],
            ['Clean up', 'Rename layer outline, tebalkan garis', 'Brush tebal atau pen'],
            ['Coloring', 'Layer di bawah clean up', 'Brush atau paint bucket'],
            ['Group/merge', 'Seleksi lalu Ctrl+G / Ctrl+E', 'Panel layers'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-7-fase-2d',
            'engine': 'mermaid',
            'title': 'Alur pembuatan aset 2D di Photoshop',
            'code': 'flowchart LR\n'
                    '  A[Sketsa dengan opacity rendah] --> B[Inking]\n'
                    '  B --> C[Clean up]\n'
                    '  C --> D[Coloring]\n'
                    '  D --> E[Group dan merge layer]\n'
                    '  E --> F[Aset animasi siap]',
        },
        'activity': categorize_block(
            'anim-7-klasifikasi',
            'Kelompokkan aplikasi ke kategori 2D atau 3D.',
            [('b1', 'Aplikasi 2D'), ('b2', 'Aplikasi 3D')],
            [
                ('i1', 'Adobe Animate', 'b1'),
                ('i2', 'Blender', 'b2'),
                ('i3', 'Toon Boom Harmony', 'b1'),
                ('i4', 'Autodesk Maya', 'b2'),
                ('i5', 'TVPaint', 'b1'),
                ('i6', 'Cinema 4D', 'b2'),
            ],
            'Tepat. 2D untuk kartun dan gambar datar; 3D untuk model berdimensi.',
            'Ingat: Animate dan Toon Boom 2D; Blender dan Maya 3D.',
        ),
        'subtitle': 'Dasar Blender',
        'list': [
            'Antarmuka Blender memiliki workspace layout dengan panel outliner, properties, 3D viewport, toolbar, dan timeline.',
            'Navigasi viewport: tombol tengah mouse untuk memutar, scroll untuk zoom, shift + tombol tengah untuk geser.',
            'Mode shading terdiri atas wire edges, solid, material, dan rendered; tekan Z untuk memilih.',
            'Memanipulasi objek dengan move, rotate, scale; memberi material, lighting, mengatur kamera, lalu rendering.',
            'Render engine Blender: eevee (realtime cepat), workbench (pratinjau cepat), dan cycles (raytrace dengan cahaya natural).',
        ],
        'checkpoint': (
            'Panel yang menampilkan pengaturan data aktif di Blender disebut…',
            [
                ('properties', True),
                ('outliner', False),
                ('toolbar', False),
                ('timeline', False),
            ],
            'Properties mengatur scene, material, dan modifier.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat aset dan merender',
        'paragraphs': [
            'Untuk membuat aset animasi, siapkan desain karakter, model sheet, storyboard, keyframe, dan inbetween sebagai bahan latihan.',
            'Di Blender, untuk menambahkan objek 3D gunakan menu Add, lalu manipulasi dengan move, rotate, dan scale pada objek tersebut.',
            'Rendering dilakukan setelah pengaturan kamera dan render properties; dijalankan dengan render image (F12) atau render animation (Ctrl+F12).',
        ],
        'scenario': scenario(
            'anim-7-skenario',
            'Komputer lemot saat merender',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Aplikasi 3D di komputermu berjalan lambat dan sering macet saat rendering. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Memeriksa spesifikasi dan menyesuaikan proyek dengan kemampuan perangkat', 'next': 'n2', 'score': 2, 'feedback': 'Menyesuaikan memastikan aplikasi berjalan optimal.'},
                        {'text': 'Terus memaksa rendering tanpa memperhatikan perangkat', 'next': 'n3', 'score': 0, 'feedback': 'Perangkat yang tidak sesuai membuat kerja macet dan tidak efisien.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Rendering tetap lambat. Solusinya?',
                    'choices': [
                        {'text': 'Menggunakan render engine realtime yang lebih ringan (eevee)', 'next': 'n4', 'score': 2, 'feedback': 'Eevee fokus pada kecepatan, cocok untuk pratinjau.'},
                        {'text': 'Menambah beban rendering tanpa mengatur pengaturan', 'next': 'n3', 'score': 0, 'feedback': 'Beban berlebih justru memperlambat dan menghabiskan sumber daya.'},
                    ],
                },
                {'id': 'n3', 'text': 'Proyek melambat dan deadline tidak tercapai.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Rendering selesai tepat waktu dan kualitas tetap terjaga.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan tiga aplikasi animasi 2D.', 'back': 'Adobe Animate, Toon Boom Harmony, TVPaint.'},
            {'front': 'Sebutkan empat aplikasi animasi 3D.', 'back': 'Autodesk Maya, 3ds Max, Blender, Cinema 4D.'},
            {'front': 'Apa fungsi render engine cycles?', 'back': 'Renderer raytrace yang memberi warna cahaya natural.'},
            {'front': 'Apa yang dimaksud inking?', 'back': 'Menebalkan garis sketsa pada layer baru menggunakan brush tool.'},
        ],
        'checkpoint': (
            'Urutan pembuatan aset gambar animasi 2D yang benar adalah…',
            [
                ('inking, clean up, coloring', True),
                ('coloring, inking, clean up', False),
                ('clean up, coloring, inking', False),
                ('coloring, clean up, inking', False),
            ],
            'Mulai dari menebalkan garis lalu membersihkan dan mewarnai.',
        ),
        'challenge': challenge_block(
            'anim-7-tantangan',
            'Tantangan aplikasi animasi',
            90,
            [
                ('Aplikasi animasi 2D kartun dan iklan', 'Adobe Animate'),
                ('Aplikasi 3D gratis berfitur lengkap', 'Blender'),
                ('Software 3D untuk karakter realistik', 'Autodesk Maya'),
                ('Menebalkan garis sketsa', 'Inking'),
                ('Mesin render raytrace Blender', 'Cycles'),
            ],
            'Lima istilah aplikasi animasi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Aplikasi untuk membuat animasi kartun, iklan, dan game yang dipublikasikan ke HTML5 adalah…', 'Adobe Animate', ['Blender', 'Maya', 'Tinkercad'], 'Animate juga ke Canvas dan WebGL.', 'Karya: My Little Pony.'),
        ('Aplikasi animasi berbasis bitmap yang menghadirkan media seni alami adalah…', 'TVPaint', ['Toon Boom', 'Photoshop', 'Cinema 4D'], 'Bitmap memudahkan media alami.', 'Karya Green Eggs and Ham.'),
        ('After Effect utamanya digunakan untuk…', 'motion graphic, efek, dan compositing', ['modeling 3D', 'mencetak poster', 'menulis naskah'], 'Setelah efek juga untuk konten online.', 'Kategori: animasi, efek, compositing.'),
        ('Aplikasi animasi 2D berbasis android antara lain…', 'FlipaClip dan Animation Desk', ['Blender dan Maya', '3ds Max dan Houdini', 'ZBrush dan Poser'], 'FlipaClip untuk perangkat android.', 'Dapat membuat di mana pun.'),
        ('Aplikasi 3D gratis yang berfitur lengkap adalah…', 'Blender', ['After Effect', 'TVPaint', 'Adobe Animate'], 'Fitur rendering, sculpting, dan VFX.', 'Juga video editing dan simulasi.'),
        ('Software 3D profesional untuk karakter realistik adalah…', 'Autodesk Maya', ['Toon Boom', 'Powtoon', 'Doodly'], 'Tools dan efek seperti ledakan dan kain.', 'Detail dan berkualitas.'),
        ('Render engine Blender yang berbasis raytrace adalah…', 'cycles', ['eevee', 'workbench', 'viewport'], 'Cahaya alami natural.', 'Workbench untuk pratinjau cepat.'),
        ('Render engine realtime Blender fokus pada kecepatan adalah…', 'eevee', ['cycles', 'workbench', 'outliner'], 'Dibangun dengan OpenGL.', 'Interaktif dan cepat.'),
        ('Pada antarmuka Blender, panel daftar data file .blend disebut…', 'outliner', ['properties', 'timeline', 'viewport'], 'Mengatur scene dan data.', 'Timeline untuk keyframe.'),
        ('Navigasi 3D viewport dengan tombol tengah mouse berfungsi untuk…', 'memutar area viewport', ['menghapus objek', 'mewarnai model', 'menyimpan file'], 'Shift + tombol tengah menggeser.', 'Scroll untuk zoom.'),
        ('Mode shading solid pada Blender menampilkan…', 'bentuk padat model', ['garis tepi saja', 'material terpasang', 'pratinjau render'], 'Solid bentuk padat.', 'Rendered menampilkan pratinjau render.'),
        ('Langkah pertama pembuatan aset animasi 2D di Photoshop adalah…', 'membuat sketsa dengan opacity rendah', ['langsung mewarnai', 'menggabungkan layer', 'membuat timeline'], 'Sketsa opacity 10–30%.', 'Lalu inking dan clean up.'),
        ('Shortcut untuk menggabungkan layer terpilih di Photoshop adalah…', 'Ctrl + E', ['Ctrl + G', 'Ctrl + A', 'Ctrl + T'], 'Ctrl+G untuk grup layer.', 'Ctrl+E merge layer.'),
        ('Membuat objek 3D baru di Blender dilakukan melalui…', 'menu Add', ['menu Render', 'menu Help', 'panel Timeline'], 'setelah itu manipulasi move dan scale.', 'Move, rotate, scale alat manipulasi.'),
    ],
    'multi': [
        ('Manakah aplikasi animasi 2D?', ['Adobe Animate', 'Toon Boom Harmony', 'TVPaint'], ['Autodesk Maya', 'Cinema 4D'], 'Animasi 2D untuk kartun dan gambar.', 'Maya dan Cinema 4D aplikasi 3D.'),
        ('Manakah aplikasi animasi 3D?', ['Blender', 'Autodesk Maya', 'Cinema 4D'], ['Powtoon', 'VideoScribe'], '3D untuk model berdimensi.', 'Powtoon dan VideoScribe berbasis web 2D.'),
        ('Manakah bagian antarmuka Photoshop?', ['Document window', 'Option bar', 'Panel groups'], ['Render engine', 'Viewport', 'Outliner'], 'Antarmuka photoshop untuk editing gambar.', 'Lainnya antarmuka Blender.'),
        ('Manakah panel antarmuka Blender?', ['Outliner', 'Properties', 'Timeline'], ['Status bar Photoshop', 'Brushes', 'Paint bucket'], 'Panel Blender untuk modeling 3D.', 'Sisanya fitur Photoshop.'),
        ('Manakah mode shading Blender?', ['Wire edges', 'Solid', 'Rendered'], ['Rgb slider', 'Layer set', 'Blend mode'], 'Empat view mode model 3D.', 'Bukan mode shading.'),
        ('Manakah contoh aplikasi animasi berbasis web?', ['Animaker', 'Powtoon', 'Doodly'], ['Autodesk Maya', 'ZBrush', 'Houdini'], 'Berbasis peramban web.', 'Sisanya aplikasi 3D profesional.'),
        ('Manakah langkah pembuatan aset 2D di Photoshop?', ['Inking', 'Clean up', 'Coloring'], ['Rendering', 'Sculpting', 'Lighting'], 'Urutan gambar aset 2D.', 'Sisanya proses 3D.'),
        ('Manakah spesifikasi yang perlu diperhatikan sebelum menginstal aplikasi animasi?', ['Prosesor dan RAM', 'GPU dan resolusi layar', 'Sistem operasi dan penyimpanan'], ['Jenis kertas', 'Warna tinta', 'Merek pensil'], 'Spesifikasi perangkat menentukan kelancaran.', 'Alat-alat menggambar manual bukan spesifikasi.'),
    ],
    'pairs': [
        ('Adobe Animate', 'animasi 2D ke HTML5'),
        ('Toon Boom', 'animasi seri dan film'),
        ('TVPaint', 'animasi berbasis bitmap'),
        ('Blender', '3D gratis dan lengkap'),
        ('Autodesk Maya', '3D karakter realistik'),
        ('Inking', 'menebalkan garis sketsa'),
        ('Clean up', 'membersihkan garis akhir'),
        ('Cycles', 'render raytrace Blender'),
    ],
    'steps': [
        ('Urutkan pembuatan aset 2D di Photoshop.', ['Membuat sketsa opacity rendah', 'Melakukan inking', 'Melakukan clean up', 'Melakukan coloring', 'Group dan merge layer'], 'Berawal dari sketsa.', 'Penggabungan layer menutupnya.'),
        ('Urutkan pengerjaan animasi 3D di Blender.', ['Menambahkan objek', 'Memanipulasi move, rotate, scale', 'Memasang material', 'Menambahkan lighting', 'Mengatur kamera dan rendering'], 'Objek dibuat dulu.', 'Rendering menghasilkan gambar.'),
        ('Urutkan memilih render engine Blender.', ['Menyiapkan scene', 'Mengatur kamera', 'Memilih render engine', 'Mengatur render properties', 'Menjalankan render image'], 'Scene disiapkan dulu.', 'Render image menutupnya.'),
        ('Urutkan langkah membersihkan gambar animasi.', ['Menyiapkan layer hasil inking', 'Buat layer baru bernama outline', 'Gunakan brush yang lebih tebal', 'Memakai pen tool untuk garis panjang', 'Menghapus garis bantu'], 'Bermula dari hasil inking.', 'Bersih siap diwarnai.'),
        ('Urutkan menginstal aplikasi animasi.', ['Memeriksa spesifikasi perangkat', 'Menyambungkan internet', 'Membuka laman pengunduhan', 'Masuk akun dan pilih aplikasi', 'Mengikuti instruksi install'], 'Cek perangkat dulu.', 'Instalasi menutupnya.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)