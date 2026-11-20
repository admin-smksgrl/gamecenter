"""KEP 3 — Budi Pekerti Luhur dalam Kehidupan (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 3',
    'slug': 'kep-3-budi-pekerti-kehidupan',
    'title': 'Budi Pekerti Luhur dalam Kehidupan',
    'description': (
        'Menerapkan budi pekerti luhur di lingkup keluarga, masyarakat, bangsa, dan '
        'pergaulan global melalui lima landasan: ketulusan, kemandirian, welas asih, '
        'cinta kebenaran, dan kedamaian.'
    ),
    'objectives': [
        'Menghayati serta mengamalkan makna pemaaf, toleransi, dan kepedulian antarsesama.',
        'Menghayati sikap jujur, gotong royong, welas asih, serta cinta damai dalam lingkungan sosial yang luas.',
        'Menganalisis manfaat budi pekerti pribadi dalam keluarga, teman, masyarakat, berbangsa, dan keragaman global.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 3 Budi Pekerti Luhur Dalam Kehidupan; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Ketulusan', 'definition': 'Melakukan kebaikan tanpa mengharapkan hasil atau imbalan apa pun.'},
        {'term': 'Kemandirian', 'definition': 'Kemampuan menata penghidupan sendiri dengan usaha yang bersih dan halal.'},
        {'term': 'Welas asih', 'definition': 'Belas kasih yang diwujudkan dalam tindakan berbagi harta, ilmu, dan kecakapan.'},
        {'term': 'Integritas', 'definition': 'Kejujuran yang terpercaya, selaras dengan budi luhur yang terpancar dari roh suci.'},
        {'term': 'Toleransi', 'definition': 'Sikap menerima perbedaan latar belakang, keyakinan, dan cara pandang.'},
        {'term': 'Gotong royong', 'definition': 'Kerja bersama secara sukarela untuk kepentingan bersama.'},
        {'term': 'Mamayu hayuning sasama', 'definition': 'Falsafah Jawa: memelihara keselamatan sesama manusia.'},
        {'term': 'Mamayu hayuning bawana', 'definition': 'Falsafah Jawa: memelihara keselamatan alam semesta.'},
        {'term': 'Marakka’ Bola', 'definition': 'Tradisi Bugis memindahkan rumah secara bergotong royong.'},
    ],
    'intro': {
        'material_title': 'Belajar dengan mempraktikkan',
        'title': 'Kehidupan adalah belajar',
        'paragraphs': [
            'Selagi hidup, kita terus belajar dan berusaha melakukan yang terbaik. Budi pekerti luhur tidak perlu menunggu kematangan pribadi; ia dipelajari dengan jalan dipraktikkan.',
            'Belajar budi pekerti berlangsung langsung: mengetahui dengan akal, meyakini dengan hati, menuruti dalam ucapan, dan melakukannya. Tidak ada hasil belajar budi pekerti kecuali setelah diwujudkan dalam tindakan.',
            'Kejujuran di sini lebih dalam daripada berkata benar. Ia adalah integritas, yaitu kepercayaan yang selaras dengan budi luhur dari roh suci dalam diri. Oprah Winfrey menyebut integritas sebagai melakukan hal yang benar meski tak ada yang tahu.',
        ],
        'diagram': (
            'Lima landasan budi pekerti dalam kehidupan',
            'flowchart TB\n'
            '  A[Budi pekerti luhur kehidupan] --> B[Ketulusan]\n'
            '  A --> C[Kemandirian dan berbakti]\n'
            '  A --> D[Welas asih berbagi]\n'
            '  A --> E[Cinta kebenaran]\n'
            '  A --> F[Cinta damai]\n'
            '  B --> G[Kerukunan dan kedamaian]\n'
            '  F --> G',
        ),
        'callout': 'Semboyan budi pekerti luhur: keras pada diri sendiri, lembut kepada orang lain.',
        'checkpoint': (
            'Urutan belajar budi pekerti menurut buku adalah…',
            [
                ('mengetahui dengan akal – meyakini dengan hati – menuruti dalam ucapan – melakukannya', True),
                ('melakukannya – mengetahui – meyakini – mengucapkan', False),
                ('meyakini – melakukannya – mengetahui – mengucapkan', False),
                ('mengucapkan – mengetahui – melakukannya – meyakini', False),
            ],
            'Belajar budi pekerti berjalan dari pengetahuan, keyakinan, ucapan, lalu tindakan.',
        ),
    },
    'concept': {
        'material_title': 'Hidup dalam kebersamaan',
        'title': 'Ramah-tamah, kerja keras, dan peduli sesama',
        'paragraphs': [
            'Manusia adalah makhluk sosial yang hidup bersama manusia lain dan alam sekitarnya. Budi luhur pribadi teruji justru ketika dipraktikkan dalam kehidupan bersama dengan norma adat, aturan, hukum, dan budaya yang berlaku.',
            'Perilaku budi luhur sosial dibangun atas norma keramahtamahan, norma penghidupan, adat dan kepedulian, serta gotong royong dan kebersamaan. Kebiasaan senyum, salam, dan sapa dilakukan dengan tulus, bukan basa-basi.',
            'Kerja keras dilengkapi kerja cerdas: mengenali potensi, menyegerakan kemauan, tabah menghadapi kegagalan, mandiri, berpikir kritis, kreatif, bekerja sama, menghargai prestasi, berbakti, dan hidup sederhana.',
        ],
        'table': [
            ['Norma sosial', 'Wujud perilaku', 'Contoh di sekolah'],
            ['Keramahtamahan', 'Senyum, salam, sapa, sopan santun', 'Menyapa guru dan petugas sekolah'],
            ['Penghidupan', 'Kerja keras dan kerja cerdas', 'Belajar tekun dan berwirausaha kecil'],
            ['Adat dan kepedulian', 'Hadir dalam acara adat dan sosial', 'Melayat dan membantu tetangga'],
            ['Gotong royong', 'Kerja bersama tanpa pamrih', 'Kerja bakti dan Marakka’ Bola'],
            ['Toleransi', 'Menerima perbedaan', 'Berteman tanpa membedakan keyakinan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-3-lingkup',
            'engine': 'mermaid',
            'title': 'Lingkup penerapan budi pekerti luhur',
            'code': 'flowchart LR\n'
                    '  A[Diri sendiri] --> B[Keluarga inti]\n'
                    '  B --> C[Keluarga besar dan tetangga]\n'
                    '  C --> D[Komunitas dan masyarakat]\n'
                    '  D --> E[Bangsa dan negara]\n'
                    '  E --> F[Pergaulan global]\n'
                    '  A --> G[Hubungan dengan alam]\n'
                    '  C --> G',
        },
        'activity': categorize_block(
            'kep-3-klasifikasi',
            'Kelompokkan perilaku berikut sebagai penerapan budi luhur atau perilaku tercela di lingkungan sosial.',
            [('b1', 'Budi luhur'), ('b2', 'Tercela')],
            [
                ('i1', 'Aktif gotong royong membersihkan lingkungan', 'b1'),
                ('i2', 'Rela mengundur waktu bermain demi kerja kelompok', 'b1'),
                ('i3', 'Membantu anggota kelompok yang belum paham', 'b1'),
                ('i4', 'Menerima perbedaan pendapat', 'b1'),
                ('i5', 'Mengejek teman yang rajin berbuat baik', 'b2'),
                ('i6', 'Mengerjakan tugas teman agar ia dipuji', 'b2'),
                ('i7', 'Memberi jawaban saat ulangan', 'b2'),
                ('i8', 'Hanya berteman dengan yang kaya', 'b2'),
            ],
            'Tepat. Budi luhur menolong dengan cara benar, bukan dengan melanggar kejujuran.',
            'Periksa lagi: menolong sambil melanggar aturan tetap termasuk perilaku tercela.',
        ),
        'subtitle': 'Penerapan di keluarga dan masyarakat',
        'list': [
            'Penerapan dimulai dari diri sendiri, lalu keluarga inti, keluarga besar, tetangga, masyarakat, bangsa, dan pergaulan global.',
            'Asas hubungan keluarga: pembiasaan perilaku baik, keteladanan, keterbukaan saling percaya, saling mengingatkan, kebersamaan, dan saling mengisi.',
            'Rumah menjadi tempat pertama belajar budi pekerti melalui pembiasaan dan peniruan perilaku, lalu diperkuat kecerdasan spiritual.',
            'Di tengah masyarakat, budi luhur tampak pada sikap pemaaf, toleran, peduli, dan cinta damai.',
        ],
        'checkpoint': (
            'Falsafah Jawa yang berarti memelihara keselamatan alam semesta adalah…',
            [
                ('mamayu hayuning bawana', True),
                ('mamayu hayuning sasama', False),
                ('sangkan paraning dumadi', False),
                ('manunggaling kawula gusti', False),
            ],
            'Mamayu hayuning sasama untuk sesama manusia, mamayu hayuning bawana untuk alam semesta.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Budi luhur teruji dalam kebersamaan',
        'paragraphs': [
            'Tradisi Marakka’ Bola dari Bugis menunjukkan gotong royong memindahkan rumah bersama-sama. Nilai itu sejalan dengan norma kebersamaan dan toleransi yang hidup di masyarakat Nusantara.',
            'Ketulusan teruji bukan saat dibalas kebaikan, melainkan saat menghadapi situasi sebaliknya. Ketulusan menjaga martabat orang lain, berani meminta maaf, memaafkan, serta memperbaiki dampak kesalahan sendiri maupun orang lain.',
            'Hanya pribadi mandiri yang layak berbagi dan pantas berbakti. Penghidupan yang bersih—diperoleh di jalan kebenaran—yang pantas menjadi bakti, dan dari situlah tumbuh cinta serta kedamaian sejati.',
        ],
        'scenario': scenario(
            'kep-3-skenario',
            'Teman yang berbeda keyakinan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Ada siswa baru berbeda keyakinan yang dijauhi teman sekelas. Apa tindakanmu?',
                    'choices': [
                        {'text': 'Mengajaknya bergabung dalam kerja kelompok', 'next': 'n2', 'score': 2, 'feedback': 'Toleransi diwujudkan dengan menerima dan melibatkan.'},
                        {'text': 'Ikut menjauh agar tidak dikucilkan', 'next': 'n3', 'score': 0, 'feedback': 'Mengikuti arus justru melanggengkan ketidakadilan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Seorang teman menegur, “Kenapa bergaul dengan dia?” Bagaimana jawabanmu?',
                    'choices': [
                        {'text': 'Menjelaskan bahwa perbedaan keyakinan tidak menghalangi persahabatan', 'next': 'n4', 'score': 2, 'feedback': 'Penjelasan itu menegakkan toleransi dan martabat sesama.'},
                        {'text': 'Meninggalkan teman baru itu demi ketenangan', 'next': 'n3', 'score': 0, 'feedback': 'Meninggalkannya berarti membiarkan diskriminasi.'},
                    ],
                },
                {'id': 'n3', 'text': 'Ketidakpedulian membuat suasana kelas tidak damai.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kelas menjadi rukun dan saling menghargai perbedaan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan lima landasan budi luhur kehidupan.', 'back': 'Ketulusan, kemandirian, welas asih, cinta kebenaran, dan kedamaian.'},
            {'front': 'Apa makna integritas menurut Oprah Winfrey?', 'back': 'Melakukan hal benar meski tak ada yang tahu.'},
            {'front': 'Apa asas hubungan dalam keluarga?', 'back': 'Pembiasaan, keteladanan, keterbukaan, saling mengingatkan, kebersamaan, saling mengisi.'},
            {'front': 'Apa itu Marakka’ Bola?', 'back': 'Tradisi Bugis gotong royong memindahkan rumah.'},
        ],
        'checkpoint': (
            'Menurut buku, hanya pribadi yang layak berbagi dan pantas berbakti adalah pribadi yang…',
            [
                ('mandiri dengan penghidupan bersih', True),
                ('memiliki banyak harta warisan', False),
                ('populer di lingkungannya', False),
                ('paling pandai berbicara', False),
            ],
            'Kemandirian dan penghidupan yang bersih menjadi dasar bakti yang layak.',
        ),
        'challenge': challenge_block(
            'kep-3-tantangan',
            'Tantangan istilah budi pekerti sosial',
            90,
            [
                ('Berbuat baik tanpa mengharap hasil', 'Ketulusan'),
                ('Belas kasih yang berbagi', 'Welas asih'),
                ('Menerima perbedaan', 'Toleransi'),
                ('Kerja bersama tanpa pamrih', 'Gotong royong'),
                ('Memelihara keselamatan sesama', 'Mamayu hayuning sasama'),
            ],
            'Lima istilah budi pekerti sosial terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Menurut buku, budi pekerti luhur dipelajari dengan jalan…', 'dipraktikkan langsung', ['dihafalkan', 'didengar dari ceramah', 'ditulis berulang'], 'Budi pekerti dipelajari dengan mempraktikkannya, bukan sekadar mengetahui.', 'Tidak ada hasil belajar tanpa tindakan.'),
        ('Lima landasan budi pekerti luhur kehidupan adalah…', 'ketulusan, kemandirian, welas asih, cinta kebenaran, kedamaian', ['kekayaan, kekuasaan, kepandaian, ketenaran, keberanian', 'kejujuran, keberanian, kekuatan, kecepatan, ketepatan', 'sopan, ramah, rajin, rapi, rapat'], 'Kelima landasan itu menjadi jalan kemurnian hati.', 'Sejalan dengan mamayu hayuning sasama.'),
        ('Semboyan budi pekerti luhur menurut buku adalah…', 'keras pada diri sendiri, lembut kepada orang lain', ['keras kepada semua orang', 'lembut kepada diri sendiri', 'tegas kepada siapa pun'], 'Semboyan itu menuntut pengendalian diri dan kasih kepada sesama.', 'Menjadi kunci belajar budi pekerti.'),
        ('Menurut Oprah Winfrey, integritas adalah…', 'melakukan hal benar meski tak ada yang tahu', ['melakukan hal benar agar dipuji', 'berbicara benar di depan orang', 'menghindari kesalahan orang lain'], 'Integritas diuji tanpa saksi.', 'Ia bekerja dari dalam diri.'),
        ('Hanya pribadi yang layak berbagi dan pantas berbakti adalah pribadi yang…', 'mandiri dengan penghidupan bersih', ['kaya raya', 'terkenal', 'berpendidikan tinggi'], 'Kemandirian dan penghidupan bersih menjadi dasarnya.', 'Buah penghidupan bersih itulah bakti.'),
        ('Tradisi Bugis memindahkan rumah secara bergotong royong disebut…', 'Marakka’ Bola', ['Mappalili', 'Ngaben', 'Sekaten'], 'Marakka’ Bola adalah gotong royong memindahkan rumah.', 'Menunjukkan kebersamaan masyarakat.'),
        ('Sikap menerima perbedaan latar belakang dan keyakinan disebut…', 'toleransi', ['konformitas', 'kompetisi', 'isolasi'], 'Toleransi menjadi norma kebersamaan.', 'Menjaga kerukunan hidup.'),
        ('Kebiasaan senyum, salam, dan sapa termasuk norma…', 'keramahtamahan', ['penghidupan', 'hukum pidana', 'perdagangan'], 'Keramahtamahan adalah warisan leluhur Nusantara.', 'Dilakukan dengan tulus.'),
        ('Falsafah Jawa “mamayu hayuning sasama” berarti…', 'memelihara keselamatan sesama manusia', ['memelihara alam semesta', 'mencari kekayaan', 'menuntut ilmu tinggi'], 'Sasama berarti sesama manusia.', 'Bawana berarti alam semesta.'),
        ('Salah satu asas hubungan dalam keluarga adalah…', 'keteladanan', ['persaingan', 'kerahasiaan mutlak', 'pengabaian'], 'Keluarga dibangun dengan keteladanan dan pembiasaan.', 'Anak belajar dari contoh.'),
        ('Salah satu sikap kerja keras menurut buku adalah…', 'berpikir kritis', ['menunda pekerjaan', 'bergantung pada orang lain', 'cepat puas diri'], 'Kerja cerdas memerlukan pikiran kritis dan kreatif.', 'Tenaga kalah dibanding cara.'),
        ('Menurut buku, hidup sederhana merupakan bentuk…', 'rasa syukur kepada Tuhan', ['kekurangan harta', 'ketakutan sosial', 'keterpaksaan'], 'Hidup seperlunya adalah wujud syukur.', 'Bukan karena terpaksa.'),
        ('Penerapan budi luhur pertama-tama dimulai dari…', 'diri sendiri dan keluarga inti', ['lingkungan global', 'organisasi internasional', 'pemerintah'], 'Penerapan berawal dari diri lalu keluarga.', 'Keluarga menjadi pendidikan paling dasar.'),
        ('Sikap berbagi kepada yang membutuhkan menurut buku disebut…', 'welas asih berbagi', ['simpati pasif', 'transaksi sosial', 'kewajiban hukum'], 'Welas asih diwujudkan dalam tindakan berbagi.', 'Bukan sekadar perasaan kasihan.'),
    ],
    'multi': [
        ('Manakah landasan budi pekerti luhur kehidupan?', ['Ketulusan', 'Kemandirian', 'Welas asih'], ['Kekayaan', 'Keternamaan'], 'Kelima landasan berpusat pada hati dan tindakan.', 'Kekayaan bukan landasan budi luhur.'),
        ('Manakah norma sosio-kultural yang disebut buku?', ['Keramahtamahan', 'Gotong royong', 'Kepedulian'], ['Permusuhan', 'Persaingan tidak sehat'], 'Norma itu membangun kebersamaan.', 'Permusuhan merusak kebersamaan.'),
        ('Manakah sikap kerja keras dan cerdas?', ['Mengenali potensi diri', 'Tabah menghadapi kegagalan', 'Bekerja sama dengan mitra'], ['Menunda pekerjaan', 'Bergantung penuh pada orang lain'], 'Kerja cerdas menuntut potensi, ketabahan, dan kerja sama.', 'Menunda melemahkan usaha.'),
        ('Manakah wujud peduli sesama?', ['Membantu korban musibah', 'Menghibur teman yang sedih', 'Berbagi bekal'], ['Mengejek kekurangan teman', 'Menyebar gosip'], 'Kepedulian diwujudkan dalam tindakan nyata.', 'Gosip merusak kerukunan.'),
        ('Manakah asas hubungan keluarga menurut buku?', ['Pembiasaan perilaku baik', 'Keterbukaan saling percaya', 'Saling mengingatkan'], ['Menutup diri', 'Saling menjatuhkan'], 'Keluarga dibangun dengan kebiasaan, kepercayaan, dan nasihat.', 'Menutup diri menghambat pembelajaran.'),
        ('Manakah contoh toleransi di sekolah?', ['Berteman tanpa membedakan keyakinan', 'Menghormati teman yang berbeda suku', 'Menerima pendapat berbeda'], ['Menolak teman beda agama', 'Memaksakan pendapat sendiri'], 'Toleransi menerima perbedaan.', 'Memaksakan pendapat melanggar toleransi.'),
        ('Manakah perilaku ramah lingkungan?', ['Memelihara tanaman', 'Mengurangi sampah plastik', 'Memulihkan lingkungan rusak'], ['Membuang sampah ke sungai', 'Menebang pohon sembarangan'], 'Ramah lingkungan berarti memelihara dan memulihkan.', 'Membuang sampah merusak alam.'),
        ('Manakah manfaat menerapkan budi luhur dalam kebersamaan?', ['Tercipta kerukunan', 'Tumbuh saling percaya', 'Lingkungan menjadi damai'], ['Muncul permusuhan', 'Hilangnya kepedulian'], 'Budi luhur membangun kerukunan dan kedamaian.', 'Permusuhan lahir dari perilaku tercela.'),
    ],
    'pairs': [
        ('Ketulusan', 'berbuat baik tanpa mengharap hasil'),
        ('Kemandirian', 'menata penghidupan sendiri'),
        ('Welas asih', 'belas kasih dalam tindakan'),
        ('Integritas', 'jujur meski tak ada yang tahu'),
        ('Toleransi', 'menerima perbedaan'),
        ('Marakka’ Bola', 'gotong royong memindahkan rumah'),
        ('Mamayu hayuning sasama', 'memelihara keselamatan sesama'),
        ('Mamayu hayuning bawana', 'memelihara keselamatan alam'),
    ],
    'steps': [
        ('Urutkan tahap belajar budi pekerti luhur.', ['Mengetahui dengan akal', 'Meyakini dengan hati', 'Menuruti dalam ucapan', 'Melakukannya dalam tindakan', 'Menjadi kebiasaan hidup'], 'Belajar bergerak dari pengetahuan sampai kebiasaan.', 'Tindakan menjadi bukti belajar.'),
        ('Urutkan lingkup penerapan budi luhur.', ['Diri sendiri', 'Keluarga inti', 'Keluarga besar dan tetangga', 'Masyarakat', 'Bangsa dan pergaulan global'], 'Penerapan meluas dari diri ke lingkup global.', 'Keluarga menjadi tahap kedua.'),
        ('Urutkan langkah membangun kebiasaan ramah-tamah.', ['Membiasakan senyum', 'Memberi salam', 'Menyapa dengan santun', 'Membantu tamu atau warga baru', 'Menjaga ketulusan dalam kebiasaan'], 'Kebiasaan dimulai dari yang sederhana sampai ketulusan.', 'Ketulusan menjaga kebiasaan tetap hidup.'),
        ('Urutkan sikap menghadapi kegagalan menurut buku.', ['Menyadari risiko sebagai tantangan', 'Menerima kegagalan', 'Mengambil pelajaran', 'Bangkit mencoba lagi', 'Bersyukur atas hasil kecil'], 'Kegagalan dihadapi dengan belajar lalu bangkit.', 'Syukur menutup rangkaian sikap.'),
        ('Urutkan wujud kepedulian sosial di lingkungan.', ['Mengenali kebutuhan warga', 'Menawarkan bantuan', 'Bergotong royong', 'Menjaga keberlanjutan bantuan', 'Mensyukuri hasil bersama'], 'Kepedulian bergerak dari mengenali kebutuhan sampai keberlanjutan.', 'Gotong royong menjadi intinya.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
