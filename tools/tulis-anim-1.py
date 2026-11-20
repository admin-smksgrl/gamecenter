"""ANIM 1 — Proses Bisnis Kreatif di Bidang Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 1',
    'slug': 'anim-1-proses-bisnis-kreatif',
    'title': 'Proses Bisnis Kreatif di Bidang Animasi',
    'description': (
        'Memahami K3 di bidang animasi, alur produksi industri animasi '
        '(praproduksi, produksi, pascaproduksi), membentuk pola pikir kreatif, '
        'dan menghasilkan desain yang tepat sasaran untuk klien.'
    ),
    'objectives': [
        'Memahami dan menerapkan K3 dalam industri animasi.',
        'Memahami alur produksi dari praproduksi, produksi, hingga pascaproduksi.',
        'Mengembangkan pola pikir kreatif dalam menciptakan karya animasi.',
        'Menghasilkan solusi desain yang tepat sasaran berdasar riset dan kebutuhan klien.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 1 Proses Bisnis Kreatif di Bidang Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'K3', 'definition': 'Keselamatan dan Kesehatan Kerja, upaya memastikan pekerja bekerja aman dan sehat.'},
        {'term': 'Alur produksi', 'definition': 'Serangkaian tahap produksi terorganisasi dari praproduksi, produksi, hingga pascaproduksi.'},
        {'term': '3D production pipeline', 'definition': 'Jalur produksi animasi 3D dari konsep hingga output akhir dengan urutan terstruktur.'},
        {'term': 'Praproduksi', 'definition': 'Tahap merencanakan konsep, menyusun cerita, storyboard, animatic, dan desain.'},
        {'term': 'Animatic', 'definition': 'Versi kasar animasi yang dirangkai dengan gambar, suara, dan efek suara.'},
        {'term': 'Rendering', 'definition': 'Tahap menggabungkan dan menghasilkan gambar final dari data 3D.'},
        {'term': 'Pascaproduksi', 'definition': 'Tahap compositing, koreksi warna, editing, dan finishing.'},
        {'term': 'Ergonomi', 'definition': 'Penyesuaian posisi kerja agar nyaman dan mencegah cedera.'},
        {'term': 'Pola pikir kreatif', 'definition': 'Kemampuan menghasilkan ide baru dan inovatif, didukung pribadi, proses, pendorong, dan produk. (4P)'},
    ],
    'intro': {
        'material_title': 'K3 di bidang animasi',
        'title': 'Bekerja aman dan sehat di depan komputer',
        'paragraphs': [
            'K3 adalah keselamatan dan kesehatan kerja, yaitu upaya memastikan pekerja dapat bekerja dengan aman dan sehat di tempat kerja, termasuk mencegah cedera, kecelakaan, dan masalah kesehatan akibat lingkungan kerja.',
            'Pekerja animasi sering duduk lama di depan komputer sehingga berisiko mengalami cedera tangan atau pergelangan, kelelahan mata, hingga kecelakaan listrik. Karena itu K3 sangat penting.',
            'Penerapan K3 meliputi menjaga ventilasi dan kualitas udara, memberi pelatihan dan alat pelindung diri, merawat peralatan teratur, serta memperhatikan kesejahteraan pekerja dan lingkungan sekitar.',
        ],
        'diagram': (
            'Beberapa contoh kecelakaan kerja di industri animasi',
            'flowchart TB\n'
            '  A[Kecelakaan kerja animasi] --> B[Cedera tangan, pergelangan, lengan]\n'
            '  A --> C[Kecelakaan jatuh di ketinggian]\n'
            '  A --> D[Cedera mata karena layar]\n'
            '  A --> E[Kecelakaan listrik]\n'
            '  A --> F[Kerusakan perangkat dan hilangnya fail]',
        ),
        'callout': 'Atur posisi ergonomis: monitor sejajar mata, punggung tegak, kaki ditopang, dan istirahat cukup untuk mencegah kelelahan.',
        'checkpoint': (
            'K3 adalah singkatan dari…',
            [
                ('keselamatan dan kesehatan kerja', True),
                ('keuangan dan kualitas kerja', False),
                ('kepuasan dan kecepatan', False),
                ('kompetensi dan karakter', False),
            ],
            'K3 berarti keselamatan dan kesehatan kerja.',
        ),
    },
    'concept': {
        'material_title': 'Alur produksi animasi',
        'title': 'Praproduksi, produksi, pascaproduksi',
        'paragraphs': [
            'Alur produksi animasi adalah rangkaian tahap terorganisasi yang mengatur produksi secara sistematis agar hemat waktu, biaya, dan sumber daya, serta menjamin kualitas sesuai standar.',
            'Untuk animasi 3D, alur ini disebut 3D production pipeline: dimulai dari konsep dan skrip, lalu modeling, rigging, texturing, animation, lighting, VFX, dan rendering, kemudian compositing.',
            'Praproduksi menjadi dasar seluruh proses: menentukan ide, menyusun cerita, membuat storyboard, animatic, dan desain karakter serta lingkungan sebelum produksi dimulai.',
        ],
        'table': [
            ['Tahap', 'Kegiatan utama', 'Contoh tugas'],
            ['Praproduksi', 'Ide, cerita, storyboard', 'Menulis skenario dan desain karakter'],
            ['Produksi', 'Membuat aset dan animasi', 'Modelling, rigging, texturing, rendering'],
            ['Pascaproduksi', 'Merapikan hasil akhir', 'Compositing, koreksi warna, editing'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-1-pipeline',
            'engine': 'mermaid',
            'title': 'Alur produksi animasi 3D',
            'code': 'flowchart LR\n'
                    '  A[Praproduksi: ide, skrip, storyboard] --> B[Produksi: modeling dan rigging]\n'
                    '  B --> C[Produksi: texturing, animation, lighting]\n'
                    '  C --> D[VFX dan rendering]\n'
                    '  D --> E[Pascaproduksi: compositing]\n'
                    '  E --> F[Koreksi warna, editing, final output]',
        },
        'activity': categorize_block(
            'anim-1-klasifikasi',
            'Kelompokkan kegiatan berikut ke dalam tahap praproduksi atau produksi.',
            [('b1', 'Praproduksi'), ('b2', 'Produksi')],
            [
                ('i1', 'Menulis skenario cerita', 'b1'),
                ('i2', 'Membuat model karakter 3D', 'b2'),
                ('i3', 'Menghasilkan ide dari curah gagasan', 'b1'),
                ('i4', 'Memberi rigging pada karakter', 'b2'),
                ('i5', 'Membuat storyboard adegan', 'b1'),
                ('i6', 'Animasi pergerakan karakter', 'b2'),
                ('i7', 'Membuat animatic kasar', 'b1'),
                ('i8', 'Melakukan rendering', 'b2'),
            ],
            'Tepat. Praproduksi merencanakan; produksi membuat aset dan gerak.',
            'Periksa lagi: ide, skrip, storyboard, dan animatic adalah praproduksi.',
        ),
        'subtitle': 'Pola pikir kreatif dan desain',
        'list': [
            'Kreativitas dibangun dari empat komponen 4P: pribadi (person), proses (process), pendorong (press), dan produk kreatif (product).',
            'Pola pikir kreatif mendorong pencarian ide baru yang inovatif dan unik dalam karya animasi.',
            'Desain yang tepat sasaran mengikuti alur good story (riset cerita), good design (riset target pasar), dan good business (potensi pengembangan produk).',
            'Memahami audiens, warna, bentuk, font, serta fungsi dan konteks produk membuat desain menarik dan efektif bagi klien.',
        ],
        'checkpoint': (
            'Urutan alur produksi animasi yang benar adalah…',
            [
                ('praproduksi, produksi, pascaproduksi', True),
                ('produksi, praproduksi, pascaproduksi', False),
                ('pascaproduksi, praproduksi, produksi', False),
                ('produksi, pascaproduksi, praproduksi', False),
            ],
            'Produksi dimulai dari perencanaan, lalu pembuatan, dan diakhiri perapihan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merencanakan produksi animasi',
        'paragraphs': [
            'Perencanaan produksi memastikan seluruh proses berjalan efektif dan efisien dengan memperhitungkan anggaran, tim, dan tenggat waktu (deadline).',
            'Dari riset cerita dan karakter, tim menyusun konsep, lalu membuat storyboard untuk memvisualisasikan urutan adegan, aksi, dan arah kamera.',
            'Desain mock up membantu tim melihat produk sebelum diproduksi penuh, termasuk potensi pengembangannya melalui lisensi atau kemitraan.',
        ],
        'scenario': scenario(
            'anim-1-skenario',
            'Deadline ketat dan mulai lelah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Tim produksimu bekerja berjam-jam dan beberapa anggota mengeluh sakit mata serta pergelangan tangan. Sikapmu?',
                    'choices': [
                        {'text': 'Memberi jadwal istirahat dan memperbaiki posisi kerja ergonomis', 'next': 'n2', 'score': 2, 'feedback': 'K3 menjaga kesehatan dan produktivitas tim jangka panjang.'},
                        {'text': 'Memaksa lanjut bekerja tanpa istirahat demi mengejar deadline', 'next': 'n3', 'score': 0, 'feedback': 'Memaksa bekerja berisiko cedera dan menurunkan kualitas.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana memastikan pekerjaan tetap selesai tepat waktu?',
                    'choices': [
                        {'text': 'Menyusun ulang jadwal dengan membagi tugas sesuai kemampuan', 'next': 'n4', 'score': 2, 'feedback': 'Perencanaan dan pembagian tugas menjaga kualitas serta tenggat.'},
                        {'text': 'Menyerahkan semua pekerjaan kepada satu orang', 'next': 'n3', 'score': 0, 'feedback': 'Beban berlebih pada satu orang memperlambat dan memancing kesalahan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tim jatuh sakit, kualitas anjlok, dan klien kecewa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Proyek selesai tepat waktu dengan tim yang sehat dan karya berkualitas.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa kepanjangan K3?', 'back': 'Keselamatan dan kesehatan kerja.'},
            {'front': 'Sebutkan alur produksi animasi.', 'back': 'Praproduksi, produksi, pascaproduksi.'},
            {'front': 'Apa itu animatic?', 'back': 'Versi kasar animasi yang dirangkai dengan gambar, suara, dan efek suara.'},
            {'front': 'Apa komponen 4P kreativitas?', 'back': 'Pribadi, proses, pendorong, dan produk kreatif.'},
        ],
        'checkpoint': (
            'Alur desain yang tepat sasaran meliputi…',
            [
                ('good story, good design, good business', True),
                ('harga, warna, ukuran', False),
                ('pemasaran, iklan, hadiah', False),
                ('kamera, suara, efek', False),
            ],
            'Desain tepat sasaran berdasar riset cerita, riset pasar, dan potensi bisnis.',
        ),
        'challenge': challenge_block(
            'anim-1-tantangan',
            'Tantangan istilah proses bisnis animasi',
            90,
            [
                ('Keselamatan dan kesehatan kerja', 'K3'),
                ('Versi kasar animasi', 'Animatic'),
                ('Jalur produksi animasi 3D', '3D production pipeline'),
                ('Tahap menggabungkan hasil menjadi gambar final', 'Rendering'),
                ('Posisi kerja yang nyaman dan aman', 'Ergonomi'),
            ],
            'Lima istilah proses bisnis animasi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('K3 dalam bidang animasi adalah…', 'keselamatan dan kesehatan kerja untuk mencegah cedera dan penyakit akibat kerja', ['kepemimpinan dan ketepatan', 'keuangan dan keterampilan', 'kecepatan dan keindahan'], 'K3 melindungi tenaga kerja.', 'Mencakup bahan kimia, alat, dan lingkungan.'),
        ('Peraturan yang mengatur keselamatan kerja di Indonesia adalah…', 'UU No. 1 Tahun 1970', ['UU No. 13 Tahun 2005', 'PP No. 5 Tahun 1999', 'UU No. 20 Tahun 2003'], 'UU 1/1970 mengatur keselamatan kerja.', 'Juga ada UU 13/2003 dan PP 50/2012.'),
        ('Alur produksi animasi yang benar adalah…', 'praproduksi, produksi, pascaproduksi', ['produksi, praproduksi, pascaproduksi', 'pascaproduksi, produksi, praproduksi', 'produksi, pascaproduksi, praproduksi'], 'Produksi dimulai dari perencanaan.', 'Diakhiri perapihan akhir.'),
        ('Versi kasar animasi yang dirangkai dengan gambar dan suara disebut…', 'animatic', ['storyboard', 'rendering', 'compositing'], 'Animatic memvisualkan susunan adegan.', 'Menjadi gambaran bagi klien.'),
        ('Rangkaian gambar kasar urutan cerita disebut…', 'storyboard', ['animatic', 'skenario', 'texture'], 'Storyboard memuat deskripsi adegan dan arah kamera.', 'Dasar visualisasi cerita.'),
        ('Tahap produksi yang membuat model dasar karakter 3D adalah…', 'modeling', ['rigging', 'texturing', 'rendering'], 'Modeler membuat model dasar.', 'Rigging memberi tulang/gerak.'),
        ('Cedera akibat bekerja terlalu lama dengan mouse terjadi jika…', 'posisi tangan tidak ergonomis', ['posisi duduk rapi', 'layar terlalu gelap', 'musik keras'], 'Posisi tangan dan pergelangan harus ergonomis.', 'Tegakkan posisi yang nyaman.'),
        ('Salah satu usaha preventif kecelakaan kerja animasi adalah…', 'mengatur posisi kerja ergonomis dan istirahat cukup', ['menatap layar terus-menerus', 'mempercepat deadline', 'menghilangkan ventilasi'], 'Pencegahan menjaga kesehatan dan produktivitas.', 'Istirahat cukup mencegah kelelahan mata.'),
        ('Tahap pascaproduksi meliputi…', 'compositing, koreksi warna, editing, dan finishing', ['modeling dan rigging', 'storyboard dan skrip', 'curah gagasan'], 'Pascaproduksi merapikan hasil akhir.', 'Sebelum output final.'),
        ('Komponen 4P kreativitas meliputi…', 'pribadi, proses, pendorong, dan produk kreatif', ['pemilu, perdamaian, prestasi', 'pasar, promosi, produk', 'pikiran, perasaan, perilaku'], '4P membangun kreativitas.', 'Person, process, press, product.'),
        ('Desain tepat sasaran diawali dari…', 'good story berdasar riset dan data', ['harga murah', 'warna mencolok', 'efek khusus'], 'Cerita yang baik komunikatif dan menyentuh audiens.', 'Diikuti good design dan good business.'),
        ('Memahami audiens target membantu desain…', 'menghasilkan pengalaman visual yang menarik', ['menyamakan semua gaya', 'mengabaikan pengguna', 'menghilangkan warna'], 'Riset audiens membuat desain efektif.', 'Menarik dan menggugah perasaan.'),
        ('Rendering dalam produksi animasi adalah…', 'tahap menggabungkan dan menghasilkan gambar final', ['tahap menulis skrip', 'tahap ide awal', 'tahap pemasaran'], 'Rendering dari data 3D menjadi gambar.', 'Bagian tahap produksi.'),
        ('Tujuan dibuatnya alur produksi adalah…', 'mengatur produksi sistematis agar hemat waktu, biaya, dan sumber daya', ['memperlambat kerja', 'menaikkan biaya', 'menyembunyikan kesalahan'], 'Alur menjaga efisiensi dan kualitas.', 'Memantau progres keseluruhan.'),
    ],
    'multi': [
        ('Manakah risiko kerja di industri animasi?', ['Cedera tangan karena mouse', 'Kelelahan mata', 'Kecelakaan listrik'], ['Keracunan makanan laut', 'Sengatan matahari'], 'Risiko berkaitan dengan komputer dan listrik.', 'Bukan risiko khas studio animasi.'),
        ('Manakah tahapan praproduksi?', ['Penentuan ide', 'Penyusunan cerita', 'Pembuatan storyboard'], ['Rendering', 'Compositing'], 'Praproduksi merencanakan konsep.', 'Rendering dan compositing bagian produksi.'),
        ('Manakah tahapan produksi animasi 3D?', ['Modeling', 'Rigging', 'Texturing'], ['Menulis skenario', 'Koreksi warna'], 'Produksi membuat aset dan gerak.', 'Skenario praproduksi, koreksi warna pascaproduksi.'),
        ('Manakah contoh penerapan K3 bidang animasi?', ['Menjaga kualitas udara', 'Memberi alat pelindung diri', 'Merawat peralatan teratur'], ['Menghilangkan istirahat', 'Mengurangi ventilasi'], 'K3 menjaga keamanan dan kesehatan.', 'Menghilangkan istirahat bertentangan dengan K3.'),
        ('Manakah alasan K3 penting bagi animator?', ['Sering duduk lama di depan komputer', 'Berisiko cedera tangan dan mata', 'Menghadapi deadline ketat'], ['Tidak memakai alat apa pun', 'Bekerja tanpa istirahat'], 'Bahaya berasal dari komputer dan tekanan kerja.', 'K3 menjaga kesejahteraan pekerja.'),
        ('Manakah tahapan pascaproduksi?', ['Compositing', 'Koreksi warna', 'Editing'], ['Curah gagasan', 'Storyboard'], 'Pascaproduksi merapikan hasil final.', 'Curah gagasan dan storyboard praproduksi.'),
        ('Manakah ciri desain yang baik?', ['Berdasar riset dan target pasar', 'Fungsi dan konteks produk', 'Potensi pengembangan bisnis'], ['Menyalin desain orang lain', 'Mengabaikan audiens'], 'Desain baik mempertimbangkan pasar.', 'Menyalin tak tepat sasaran.'),
        ('Manakah pola pikir kreatif yang sehat?', ['Mencari ide baru inovatif', 'Terbuka pada umpan balik', 'Berdasar riset'], ['Menolak perubahan', 'Menunggu perintah', 'Meniru terus-menerus'], 'Kreativitas butuh eksplorasi.', 'Meniru tidak menghasilkan ide baru.'),
    ],
    'pairs': [
        ('K3', 'keselamatan dan kesehatan kerja'),
        ('Animatic', 'versi kasar animasi'),
        ('Storyboard', 'gambar kasar urutan cerita'),
        ('Rendering', 'menghasilkan gambar final'),
        ('Pascaproduksi', 'compositing dan editing'),
        ('4P', 'pribadi, proses, pendorong, produk'),
        ('Ergonomi', 'posisi kerja nyaman dan aman'),
        ('3D production pipeline', 'jalur produksi animasi 3D'),
    ],
    'steps': [
        ('Urutkan tahap praproduksi animasi.', ['Menentukan ide', 'Menyusun cerita dan skenario', 'Membuat storyboard', 'Membuat animatic', 'Membuat desain karakter dan lingkungan'], 'Praproduksi berawal dari ide.', 'Desain menutup persiapan.'),
        ('Urutkan tahap produksi animasi 3D.', ['Modeling', 'Rigging', 'Texturing', 'Animation dan lighting', 'Rendering'], 'Produksi membuat aset lalu menggerakkan.', 'Rendering menghasilkan gambar final.'),
        ('Urutkan tahap pascaproduksi.', ['Compositing', 'Koreksi warna', 'Editing', 'Finishing', 'Final output'], 'Pascaproduksi menyempurnakan hasil.', 'Output final menutup proses.'),
        ('Urutkan alur desain yang tepat sasaran.', ['Riset cerita dan audiens', 'Memahami target pasar', 'Merancang visual desain', 'Menguji fungsi dan konteks', 'Mengembangkan potensi bisnis'], 'Desain berawal dari riset.', 'Potensi bisnis menutup alur.'),
        ('Urutkan usaha pencegahan kecelakaan kerja animasi.', ['Mengatur posisi ergonomis', 'Menyediakan ventilasi yang baik', 'Memberi jadwal istirahat', 'Merawat peralatan', 'Mencadangkan data fail'], 'Pencegahan dari posisi hingga data.', 'Cadangan data mencegah hilangnya fail.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)