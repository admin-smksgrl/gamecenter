"""SEJ 3 — Penulisan Sejarah (Historiografi) (Fase E)."""
from sejarah_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'SEJ 3',
    'slug': 'sej-3-penulisan-sejarah',
    'title': 'Penulisan Sejarah (Historiografi)',
    'description': (
        'Menulis sejarah berdasarkan fakta yang telah diuji, mengenali corak '
        'historiografi tradisional, kolonial, nasional, dan modern, serta '
        'menghindari bias dalam bercerita tentang masa lalu.'
    ),
    'objectives': [
        'Menjelaskan pengertian historiografi dan corak-coraknya di Indonesia.',
        'Membandingkan historiografi tradisional, kolonial, nasional, dan modern.',
        'Mengenali bentuk bias dalam penulisan sejarah dan cara menghindarinya.',
        'Menyusun tulisan sejarah pendek berdasarkan sumber yang telah diverifikasi.',
    ],
    'minutes': 180,
    'source': (
        'Sejarah-BG-KLS-X.pdf materi Penulisan Sejarah (Historiografi); '
        'CP Fase E Mata Pelajaran Sejarah'
    ),
    'glossary': [
        {'term': 'Historiografi', 'definition': 'Penulisan sejarah; juga berarti kajian atas karya-karya penulisan sejarah.'},
        {'term': 'Historiografi tradisional', 'definition': 'Penulisan sejarah bercorak istana dan religius-magis, berpusat pada raja dan dinasti.'},
        {'term': 'Historiografi kolonial', 'definition': 'Penulisan sejarah dari sudut pandang penjajah yang menempatkan Belanda sebagai tokoh utama.'},
        {'term': 'Historiografi nasional', 'definition': 'Penulisan sejarah berpusat pada bangsa Indonesia sebagai pelaku utama, tumbuh setelah kemerdekaan.'},
        {'term': 'Historiografi modern', 'definition': 'Penulisan sejarah yang kritis, memakai ilmu bantu, dan menguji sumber secara terbuka.'},
        {'term': 'Bias sejarah', 'definition': 'Kecenderungan berpihak yang membuat kisah sejarah tidak berimbang.'},
        {'term': 'Sudut pandang', 'definition': 'Posisi penulis dalam melihat peristiwa, menentukan siapa yang dianggap penting.'},
        {'term': 'Eurocentrisme', 'definition': 'Cara pandang yang menempatkan Eropa sebagai pusat dan ukuran segala peristiwa.'},
        {'term': 'Anonim', 'definition': 'Tanpa nama penulis, ciri banyak karya historiografi tradisional.'},
    ],
    'intro': {
        'material_title': 'Dari fakta menjadi kisah',
        'title': 'Mengapa penulisan sejarah berubah?',
        'paragraphs': [
            'Setelah fakta diuji, sejarawan menuliskan kisahnya. Penulisan sejarah atau historiografi bukan menyalin data, melainkan menyusun fakta menjadi cerita yang masuk akal dan dapat diperiksa.',
            'Karena penulisnya berbeda zaman dan kepentingan, kisah tentang peristiwa yang sama dapat berbeda. Historiografi tradisional memuja raja, historiografi kolonial memuji penjajah, historiografi nasional menempatkan bangsa Indonesia sebagai pelaku utama.',
            'Historiografi modern berusaha lebih kritis: memakai ilmu bantu seperti arkeologi, sosiologi, dan antropologi, serta menyebut sumber dan keterbatasannya secara terbuka.',
        ],
        'diagram': (
            'Perubahan corak historiografi Indonesia',
            'flowchart LR\n'
            '  A[Historiografi tradisional] --> B[Historiografi kolonial]\n'
            '  B --> C[Historiografi nasional]\n'
            '  C --> D[Historiografi modern]\n'
            '  A --> E[Pusat: raja dan istana]\n'
            '  B --> F[Pusat: penjajah]\n'
            '  C --> G[Pusat: bangsa Indonesia]\n'
            '  D --> H[Pusat: analisis kritis]',
        ),
        'callout': 'Karya historiografi yang baik menyebut sumbernya, sehingga pembaca dapat menilai sendiri dasar ceritanya.',
        'checkpoint': (
            'Penulisan sejarah disebut juga…',
            [
                ('historiografi', True),
                ('heuristik', False),
                ('kritik ekstern', False),
                ('periodisasi', False),
            ],
            'Historiografi adalah penulisan sejarah berdasarkan fakta yang telah diuji.',
        ),
    },
    'concept': {
        'material_title': 'Empat corak penulisan sejarah',
        'title': 'Tradisional, kolonial, nasional, modern',
        'paragraphs': [
            'Historiografi tradisional lahir di lingkungan istana. Karya seperti babad dan hikayat bersifat religius-magis, sering tanpa nama penulis, dan berpusat pada raja serta dinasti.',
            'Historiografi kolonial ditulis oleh pejabat dan sarjana Belanda. Peristiwa dilihat dari kepentingan penjajah, perlawanan rakyat disebut pemberontakan, dan peran bangsa Indonesia disederhanakan.',
            'Historiografi nasional muncul setelah kemerdekaan. Bangsa Indonesia ditempatkan sebagai pelaku utama, dengan tokoh dan pergerakan rakyat sebagai pusat cerita.',
            'Historiografi modern menekankan analisis kritis, penggunaan ilmu bantu, serta keterbukaan atas sumber dan sudut pandang penulis.',
        ],
        'table': [
            ['Corak', 'Pusat cerita', 'Ciri utama', 'Contoh'],
            ['Tradisional', 'Raja dan dinasti', 'Religius-magis, sering anonim', 'Babad Tanah Jawi, Hikayat Raja-raja Pasai'],
            ['Kolonial', 'Penjajah Belanda', 'Sudut pandang penjajah', 'Karya sejarah Hindia-Belanda'],
            ['Nasional', 'Bangsa Indonesia', 'Peran rakyat dan pergerakan', 'Sejarah nasional Indonesia'],
            ['Modern', 'Analisis kritis', 'Ilmu bantu dan sumber terbuka', 'Kajian sejarah tematik'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'sej-3-bias',
            'engine': 'mermaid',
            'title': 'Alur munculnya bias dalam penulisan sejarah',
            'code': 'flowchart TB\n'
                    '  A[Peristiwa] --> B[Pemilihan sumber]\n'
                    '  B --> C[Pemilihan sudut pandang]\n'
                    '  C --> D[Penafsiran]\n'
                    '  D --> E{Berimbang?}\n'
                    '  E -- Tidak --> F[Bias sejarah]\n'
                    '  E -- Ya --> G[Kisah yang dapat diuji]\n'
                    '  F --> H[Sumber diperiksa ulang]\n'
                    '  H --> C',
        },
        'activity': categorize_block(
            'sej-3-klasifikasi',
            'Kelompokkan ciri berikut ke dalam historiografi tradisional atau historiografi kolonial.',
            [('b1', 'Tradisional'), ('b2', 'Kolonial')],
            [
                ('i1', 'Berpusat pada raja dan dinasti', 'b1'),
                ('i2', 'Perlawanan rakyat disebut pemberontakan', 'b2'),
                ('i3', 'Bernuansa religius dan magis', 'b1'),
                ('i4', 'Ditulis pejabat dan sarjana Belanda', 'b2'),
                ('i5', 'Sering tanpa nama penulis', 'b1'),
                ('i6', 'Menempatkan Belanda sebagai tokoh utama', 'b2'),
                ('i7', 'Berbentuk babad dan hikayat', 'b1'),
                ('i8', 'Menilai peristiwa dari kepentingan penjajah', 'b2'),
            ],
            'Tepat. Tradisional berpusat pada istana, kolonial berpusat pada penjajah.',
            'Periksa lagi: kata “babad” dan “raja” menandai tradisional, “Belanda” menandai kolonial.',
        ),
        'subtitle': 'Menghindari bias sejarah',
        'list': [
            'Bias dapat muncul dari pemilihan sumber yang berat sebelah, sudut pandang yang sempit, atau kesimpulan yang didahulukan sebelum bukti.',
            'Cara menghindarinya: membaca lebih dari satu sudut pandang, termasuk sumber dari pihak yang berseberangan.',
            'Hindari bahasa yang menilai berlebihan seperti “pahlawan tanpa cela” atau “pengkhianat mutlak” tanpa bukti.',
            'Sebutkan siapa penulis, kapan ditulis, dan untuk siapa, agar pembaca memahami posisi karya itu.',
        ],
        'checkpoint': (
            'Historiografi yang menempatkan bangsa Indonesia sebagai pelaku utama disebut…',
            [
                ('nasional', True),
                ('kolonial', False),
                ('tradisional', False),
                ('modern', False),
            ],
            'Historiografi nasional lahir setelah kemerdekaan dan berpusat pada bangsa Indonesia.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menulis kisah pendek yang jujur',
        'paragraphs': [
            'Mulailah dari satu peristiwa kecil di lingkunganmu, misalnya berdirinya koperasi sekolah atau perubahan nama jalan. Tetapkan batas waktu, tempat, dan tokoh yang dibicarakan.',
            'Susun kerangka: pendahuluan berisi latar, bagian isi berisi urutan peristiwa dengan sumbernya, lalu penutup berisi makna dan keterbatasan kajian.',
            'Periksa kembali tulisannya: apakah ada sumber yang disebut, apakah ada pihak yang dilupakan, dan apakah ada kalimat yang menilai tanpa bukti.',
        ],
        'scenario': scenario(
            'sej-3-skenario',
            'Dua versi perlawanan daerah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Laporan Belanda menyebut peristiwa itu “pemberontakan”, sedangkan catatan warga menyebutnya “perlawanan”. Bagaimana menulisnya?',
                    'choices': [
                        {'text': 'Menjelaskan kedua istilah beserta sumber dan kepentingannya', 'next': 'n2', 'score': 2, 'feedback': 'Perbedaan istilah menunjukkan perbedaan sudut pandang dan kepentingan.'},
                        {'text': 'Memakai istilah Belanda karena sumbernya resmi', 'next': 'n3', 'score': 0, 'feedback': 'Sumber resmi pun memiliki kepentingan; bukan otomatis paling benar.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana menutup tulisanmu agar tidak bias?',
                    'choices': [
                        {'text': 'Menyebut bahwa penilaian bergantung sudut pandang dan sumber masih terbatas', 'next': 'n4', 'score': 2, 'feedback': 'Mengakui keterbatasan adalah tanda tulisan sejarah yang jujur.'},
                        {'text': 'Menyimpulkan satu pihak sepenuhnya bersalah', 'next': 'n3', 'score': 0, 'feedback': 'Kesimpulan sepihak tanpa pembanding termasuk bias.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tulisanmu dinilai berat sebelah dan tidak dapat dipertanggungjawabkan.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tulisanmu berimbang dan dapat dinilai pembaca sendiri.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu historiografi?', 'back': 'Penulisan sejarah berdasarkan fakta yang telah diuji.'},
            {'front': 'Apa ciri historiografi tradisional?', 'back': 'Berpusat pada raja, religius-magis, sering anonim.'},
            {'front': 'Apa ciri historiografi kolonial?', 'back': 'Sudut pandang penjajah, Belanda sebagai tokoh utama.'},
            {'front': 'Bagaimana menghindari bias?', 'back': 'Membaca banyak sudut pandang dan menyebut sumber serta keterbatasan.'},
        ],
        'checkpoint': (
            'Cara paling tepat menghindari bias sejarah adalah…',
            [
                ('membandingkan sumber dari beberapa sudut pandang', True),
                ('memilih sumber yang paling tebal', False),
                ('menulis tanpa menyebut sumber', False),
                ('mengikuti satu penulis favorit', False),
            ],
            'Perbandingan sudut pandang menjaga tulisan tetap berimbang.',
        ),
        'challenge': challenge_block(
            'sej-3-tantangan',
            'Tantangan istilah historiografi',
            90,
            [
                ('Penulisan sejarah', 'Historiografi'),
                ('Berpusat pada raja dan istana', 'Historiografi tradisional'),
                ('Sudut pandang penjajah', 'Historiografi kolonial'),
                ('Eropa sebagai pusat', 'Eurocentrisme'),
                ('Kecenderungan berpihak', 'Bias sejarah'),
            ],
            'Lima istilah historiografi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Penulisan sejarah disebut…', 'historiografi', ['heuristik', 'periodisasi', 'kritik intern'], 'Historiografi adalah tahap menuliskan kisah sejarah.', 'Juga berarti kajian atas karya sejarah.'),
        ('Historiografi yang berpusat pada raja dan bersifat religius-magis adalah…', 'tradisional', ['kolonial', 'nasional', 'modern'], 'Karya tradisional lahir di lingkungan istana.', 'Sering berbentuk babad dan hikayat.'),
        ('Salah satu contoh historiografi tradisional adalah…', 'Babad Tanah Jawi', ['buku teks sejarah', 'artikel jurnal', 'laporan penelitian'], 'Babad termasuk karya tradisional.', 'Bercorak istana.'),
        ('Ciri historiografi tradisional yang mencolok adalah…', 'sering tanpa nama penulis', ['selalu memakai catatan kaki', 'memakai ilmu bantu modern', 'menyebut semua sumber'], 'Banyak karya tradisional bersifat anonim.', 'Penulis tidak selalu tercatat.'),
        ('Historiografi kolonial ditulis terutama oleh…', 'pejabat dan sarjana Belanda', ['warga kampung', 'pelajar Indonesia', 'pedagang Arab'], 'Karya kolonial lahir dari kepentingan penjajah.', 'Sudut pandangnya berpihak.'),
        ('Dalam historiografi kolonial, perlawanan rakyat sering disebut…', 'pemberontakan', ['revolusi', 'demonstrasi', 'musyawarah'], 'Istilah itu menunjukkan sudut pandang penjajah.', 'Pilihan kata memuat penilaian.'),
        ('Historiografi nasional menempatkan pusat cerita pada…', 'bangsa Indonesia', ['penjajah Belanda', 'raja-raja Jawa', 'bangsa Eropa'], 'Historiografi nasional tumbuh setelah kemerdekaan.', 'Rakyat dan pergerakan jadi pusat.'),
        ('Ciri historiografi modern adalah…', 'kritis dan memakai ilmu bantu', ['selalu anonim', 'hanya memuji raja', 'menolak sumber'], 'Modern menekankan analisis dan keterbukaan.', 'Memakai arkeologi, sosiologi, antropologi.'),
        ('Cara pandang yang menempatkan Eropa sebagai pusat disebut…', 'eurocentrisme', ['nasionalisme', 'sinkronisme', 'anakronisme'], 'Eurocentrisme membuat sejarah daerah terpinggirkan.', 'Perlu dihindari dalam penulisan.'),
        ('Kecenderungan berpihak dalam penulisan sejarah disebut…', 'bias sejarah', ['kronologi', 'kausalitas', 'periodisasi'], 'Bias membuat kisah tidak berimbang.', 'Muncul dari pemilihan sumber dan sudut pandang.'),
        ('Salah satu cara menghindari bias adalah…', 'membandingkan sumber dari pihak yang berseberangan', ['memakai satu sumber resmi saja', 'menghapus keterangan yang berbeda', 'menulis tanpa sumber'], 'Perbandingan menjaga keseimbangan.', 'Sudut pandang berbeda perlu didengar.'),
        ('Bahasa yang perlu dihindari dalam tulisan sejarah adalah…', 'penilaian berlebihan tanpa bukti', ['penyebutan sumber', 'penjelasan latar', 'pengakuan keterbatasan'], 'Penilaian tanpa bukti melemahkan tulisan.', 'Sebutkan dasar penilaian.'),
        ('Karya sejarah yang baik seharusnya menyebutkan…', 'sumber, penulis, dan keterbatasan', ['hanya kesimpulan', 'hanya gambar', 'hanya tokoh favorit'], 'Keterbukaan membuat karya dapat diuji.', 'Pembaca menilai sendiri dasar cerita.'),
        ('Perbedaan kisah atas peristiwa yang sama dapat terjadi karena…', 'perbedaan zaman, sumber, dan kepentingan penulis', ['peristiwa berubah sendiri', 'sejarah tidak punya bukti', 'semua penulis sama'], 'Posisi penulis memengaruhi kisah.', 'Karena itu sumber harus diperiksa.'),
    ],
    'multi': [
        ('Manakah corak historiografi Indonesia?', ['Tradisional', 'Kolonial', 'Nasional'], ['Fiktif', 'Mistis modern'], 'Tiga corak itu ditambah historiografi modern.', 'Fiktif bukan corak historiografi.'),
        ('Manakah ciri historiografi tradisional?', ['Berpusat pada raja', 'Bersifat religius-magis', 'Sering anonim'], ['Memakai catatan kaki lengkap', 'Menolak unsur kepercayaan'], 'Ciri itu melekat pada karya istana.', 'Sebaliknya, karya modern memakai catatan.'),
        ('Manakah ciri historiografi kolonial?', ['Sudut pandang penjajah', 'Belanda sebagai tokoh utama', 'Perlawanan disebut pemberontakan'], ['Bangsa Indonesia sebagai pusat', 'Memakai sumber lisan warga'], 'Kolonial menilai dari kepentingan penjajah.', 'Nasional yang berpusat pada Indonesia.'),
        ('Manakah ciri historiografi modern?', ['Kritis terhadap sumber', 'Memakai ilmu bantu', 'Menyebut keterbatasan'], ['Selalu anonim', 'Menolak pembandingan sumber'], 'Modern terbuka dan analitis.', 'Anonim ciri tradisional.'),
        ('Manakah bentuk bias dalam penulisan sejarah?', ['Memilih satu sumber saja', 'Menghilangkan peran satu pihak', 'Menilai tanpa bukti'], ['Menyebut sumber', 'Membandingkan sumber'], 'Bias muncul dari ketidakseimbangan.', 'Menyebut sumber justru menghindari bias.'),
        ('Manakah cara menjaga tulisan tetap berimbang?', ['Membaca sumber dari dua pihak', 'Menyebut sumber', 'Mengakui keterbatasan'], ['Menghapus keterangan yang berbeda', 'Memakai kata menghina'], 'Keseimbangan dibangun dengan keterbukaan.', 'Menghina bukan bagian ilmu sejarah.'),
        ('Manakah contoh karya sejarah yang dapat diuji?', ['Artikel dengan catatan kaki', 'Laporan penelitian dengan daftar sumber', 'Buku dengan penjelasan metode'], ['Cerita tanpa sumber', 'Kisah dari mulut ke mulut tanpa pencatatan'], 'Karya dapat diuji bila sumbernya jelas.', 'Tanpa sumber, klaim tak terperiksa.'),
        ('Manakah pernyataan tentang sudut pandang?', ['Menentukan siapa yang dianggap penting', 'Memengaruhi pilihan kata', 'Perlu dijelaskan kepada pembaca'], ['Selalu sama pada setiap penulis', 'Tidak perlu disebut'], 'Sudut pandang membentuk kisah.', 'Pembaca berhak mengetahuinya.'),
    ],
    'pairs': [
        ('Historiografi', 'penulisan sejarah'),
        ('Historiografi tradisional', 'berpusat pada raja'),
        ('Historiografi kolonial', 'sudut pandang penjajah'),
        ('Historiografi nasional', 'bangsa Indonesia sebagai pusat'),
        ('Historiografi modern', 'analisis kritis'),
        ('Bias sejarah', 'kecenderungan berpihak'),
        ('Eurocentrisme', 'Eropa sebagai pusat'),
        ('Sudut pandang', 'posisi penulis melihat peristiwa'),
    ],
    'steps': [
        ('Urutkan langkah menulis kisah sejarah.', ['Menetapkan topik dan batas waktu', 'Menyusun kerangka', 'Memilih fakta yang relevan', 'Menulis draf dengan menyebut sumber', 'Menyunting dan memeriksa bias'], 'Penulisan bergerak dari kerangka ke penyuntingan.', 'Pemeriksaan bias menjadi langkah akhir.'),
        ('Urutkan perkembangan historiografi Indonesia.', ['Historiografi tradisional', 'Historiografi kolonial', 'Historiografi nasional', 'Historiografi modern'], 'Corak berubah mengikuti zaman dan kekuasaan.', 'Modern menekankan kritik.'),
        ('Urutkan langkah memeriksa bias tulisan sendiri.', ['Memeriksa daftar sumber', 'Memeriksa pihak yang dilupakan', 'Memeriksa pilihan kata', 'Memeriksa kesimpulan', 'Memperbaiki tulisan'], 'Pemeriksaan berjalan dari sumber ke kesimpulan.', 'Perbaikan menutup langkah.'),
        ('Urutkan bagian tulisan sejarah pendek.', ['Pendahuluan dan latar', 'Urutan peristiwa dengan sumber', 'Analisis sebab dan akibat', 'Makna bagi masa kini', 'Keterbatasan kajian'], 'Tulisan bergerak dari latar ke keterbatasan.', 'Keterbatasan menutup dengan jujur.'),
        ('Urutkan penyaringan karya sejarah yang layak dirujuk.', ['Memeriksa penulisnya', 'Memeriksa tahun terbit', 'Memeriksa sumber yang dipakai', 'Membandingkan dengan karya lain', 'Memutuskan kelayakan rujukan'], 'Kelayakan rujukan diperiksa berlapis.', 'Perbandingan menjadi penentu.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
