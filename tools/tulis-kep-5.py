"""KEP 5 — Manembah Tuhan Yang Maha Kuasa (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 5',
    'slug': 'kep-5-manembah-tuhan',
    'title': 'Manembah Tuhan Yang Maha Kuasa',
    'description': (
        'Memahami tujuan dan tata cara manembah dalam budaya spiritual Nusantara, '
        'membedakan religiositas dan spiritualitas, serta menempuh empat tahap sujud '
        'dan tiga taraf kecerdasan spiritual.'
    ),
    'objectives': [
        'Menghayati keterbatasan diri manusia di hadapan Penciptanya.',
        'Mengamalkan penerapan nilai sujud syukur dalam kehidupan.',
        'Menganalisis bentuk dan tingkatan spiritualitas pada aktivitas manembah kepada Tuhan Yang Maha Esa.',
        'Menyajikan hasil analisis tentang mempersiapkan diri melaksanakan ritual sujud manembah.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 6 Manembah Tuhan Yang Maha Kuasa; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Manembah', 'definition': 'Ibadah menyembah dan berserah diri kepada Tuhan Yang Maha Esa dengan segenap hati, jiwa, dan raga.'},
        {'term': 'Religiositas', 'definition': 'Ketaatan melaksanakan ketentuan peribadatan serta mematuhi perintah dan larangan kepercayaan.'},
        {'term': 'Spiritualitas', 'definition': 'Sikap melepaskan keterikatan diri menuju kehendak kebenaran Tuhan, melampaui ritual.'},
        {'term': 'Bersuci', 'definition': 'Menyucikan diri, raga, dan jiwa sebelum melaksanakan ritual.'},
        {'term': 'Wulla Poddu', 'definition': 'Bulan suci pada komunitas Marapu di Sumba yang waktunya ditentukan para Rato.'},
        {'term': 'Sipaha Lima', 'definition': 'Perayaan syukuran umat Parmalim.'},
        {'term': 'Rato', 'definition': 'Pemuka adat Marapu yang bermusyawarah menentukan waktu upacara.'},
        {'term': 'Parsahataan', 'definition': 'Semboyan Parmalim tentang kesatuan bahasa roh dan jalan kebenaran Tuhan.'},
    ],
    'intro': {
        'material_title': 'Apa yang dapat manusia persembahkan?',
        'title': 'Tujuan dan sifat ritual manembah',
        'paragraphs': [
            'Bentuk manembah penghayat kepercayaan sangat beragam, tetapi prinsipnya sama: berserah diri dan mendekatkan hidup pada jalan kebenaran kehendak Tuhan, dengan perlengkapan ritual bernuansa budaya daerah masing-masing.',
            'Tujuannya menyembah Sang Pencipta serta mengumpulkan bekal perjalanan spiritual menuju kehidupan yang berguna, baik kesejahteraan duniawi maupun rohani yang berlangsung sebelum lahir, selama hidup, hingga setelah tubuh mati.',
            'Ritual bersifat suci dan sakral. Karena itu penghayat membersihkan serta menyucikan diri, pakaian, dan sarana ritual, disertai kesiapan hati, niat, dan ketulusan berkorban.',
        ],
        'diagram': (
            'Empat tahap sujud manembah',
            'flowchart TB\n'
            '  A[Sujud Raga: tenang, hening, atur nafas] --> B[Sujud Batin: tekad dan hati tunduk]\n'
            '  B --> C[Sujud Jiwa: puja dari hati tulus]\n'
            '  C --> D[Sujud Rohani: roh menyatu dengan cahaya-Nya]\n'
            '  D --> E[Kedamaian dan kesadaran seutuhnya]',
        ),
        'callout': 'Ritual yang dijalani hanya sebagai kewajiban tanpa penghayatan terasa hambar dan kehilangan maknanya.',
        'checkpoint': (
            'Sikap “kembali ke asal hidup” dalam falsafah Jawa disebut…',
            [
                ('sangkan paraning dumadi', True),
                ('mamayu hayuning bawana', False),
                ('manunggaling kawulo gusti', False),
                ('memayu hayuning pribadi', False),
            ],
            'Sangkan paraning dumadi berarti hidup akan kembali kepada Pemberi hidup.',
        ),
    },
    'concept': {
        'material_title': 'Religiositas dan spiritualitas',
        'title': 'Dua sisi nilai ritual',
        'paragraphs': [
            'Ritual memiliki dua sisi nilai. Sisi religiositas mengantar manusia pada ketundukan kepada Sang Khalik dan menghasilkan ketaatan menjalankan ketentuan peribadatan serta menjauhi pantangan.',
            'Sisi spiritualitas adalah sikap melepaskan keterikatan diri, bergerak menuju kemanfaatan bagi orang lain dan lingkungan, terutama menuju kehendak kebenaran Tuhan. Prosesnya pribadi, berdampak ke luar, dan tanpa pamrih.',
            'Spiritualitas melampaui ritual yang dilakukan dan tidak dilingkupi religiositas semata. Karena itu persiapan ritual mencakup bersuci, menyatukan tekad jiwa dan raga, serta bersujud berserah diri.',
        ],
        'table': [
            ['Tahap sujud', 'Cakupan', 'Wujud latihan'],
            ['Sujud raga', 'Tubuh dan indra', 'Sikap tenang, hening, menata nafas dan denyut nadi'],
            ['Sujud batin', 'Angan dan hati', 'Membulatkan tekad, menenangkan angan'],
            ['Sujud jiwa', 'Rasa', 'Mendaraskan puja dari hati yang tulus'],
            ['Sujud rohani', 'Roh atau hidup', 'Merasakan roh menyatu dan memperoleh pencerahan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-5-religiositas',
            'engine': 'mermaid',
            'title': 'Hubungan religiositas dan spiritualitas',
            'code': 'flowchart LR\n'
                    '  A[Ritual manembah] --> B[Religiositas: ketaatan pada ketentuan]\n'
                    '  A --> C[Spiritualitas: pelepasan keterikatan diri]\n'
                    '  B --> D[Taat aturan dan pantangan]\n'
                    '  C --> E[Bermanfaat bagi sesama dan alam]\n'
                    '  D --> F[Kebiasaan budi luhur]\n'
                    '  E --> F\n'
                    '  F --> G[Menyatu dengan kehendak Tuhan]',
        },
        'activity': categorize_block(
            'kep-5-klasifikasi',
            'Kelompokkan pernyataan berikut sebagai ciri religiositas atau spiritualitas.',
            [('b1', 'Religiositas'), ('b2', 'Spiritualitas')],
            [
                ('i1', 'Taat melaksanakan ketentuan peribadatan', 'b1'),
                ('i2', 'Menjauhi larangan dan pantangan kepercayaan', 'b1'),
                ('i3', 'Mengikuti tata urutan ritual sesuai aturan', 'b1'),
                ('i4', 'Melepaskan keterikatan kepentingan diri', 'b2'),
                ('i5', 'Bergerak menuju kehendak kebenaran Tuhan', 'b2'),
                ('i6', 'Bermanfaat bagi sesama dan lingkungan tanpa pamrih', 'b2'),
                ('i7', 'Mengendapkan hawa nafsu lahir dan batin', 'b2'),
                ('i8', 'Menyatukan cipta, rasa, dan karsa dalam sujud', 'b2'),
            ],
            'Tepat. Religiositas menekankan ketaatan aturan, spiritualitas menekankan pelepasan diri dan kebergunaan.',
            'Periksa lagi: ketaatan pada ketentuan ritual termasuk religiositas.',
        ),
        'subtitle': 'Taraf kecerdasan spiritual',
        'list': [
            'Taraf awal: menyadari keterbatasan diri, menyucikan diri, dan melepas ego untuk mohon ampun; ukurannya menjadi orang baik (mamayu hayuning pribadi).',
            'Taraf kedua: memuliakan Tuhan dengan berbuat baik karena tanggung jawab menghargai sesama; ia menjadi pamong pencerah (mamayu hayuning sasama).',
            'Taraf ketiga: membaktikan hidup bagi masyarakat luas dan kelestarian alam; ia menjadi bijaksana dan teladan (mamayu hayuning bawana).',
            'Kesatuan bahasa roh dan jalan kebenaran Tuhan dicapai lewat empat langkah: menyembah segenap hati, menanggalkan ego, memasuki jalan kebenaran, dan menyatu dalam cahaya kebenaran.',
        ],
        'checkpoint': (
            'Sujud yang mencakup sikap tenang, hening, dan penataan nafas adalah…',
            [
                ('sujud raga', True),
                ('sujud batin', False),
                ('sujud jiwa', False),
                ('sujud rohani', False),
            ],
            'Sujud raga menyangkut tubuh dan indra: tenang, hening, nafas serta denyut nadi tertata.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Persiapan dan penghayatan manembah',
        'paragraphs': [
            'Komunitas kepercayaan Nusantara antara lain Parmalim di Tanah Batak, Kaharingan di Kalimantan, Marapu di Nusa Tenggara, Sunda Wiwitan dan Badui di Jawa Barat, Mamasa, Mappurondo, serta Suku Anak Dalam.',
            'Setiap ritual memerlukan persiapan suci yang ditentukan adat: bersuci, menyatukan tekad jiwa dan raga, lalu bersujud berserah diri sambil menanggalkan kedudukan, kebesaran, dan keakuan duniawi.',
            'Ketaatan ritual menumbuhkan sikap budi luhur seperti rendah hati, taat aturan, tolong-menolong, dan gotong royong. Keselarasan semesta dipahami sebagai keseimbangan dinamis yang kembali pulih setelah sempat terganggu.',
        ],
        'scenario': scenario(
            'kep-5-skenario',
            'Mengikuti ritual tanpa penghayatan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu mengikuti ritual komunitas, tetapi pikiranmu melayang ke hal lain. Apa yang sebaiknya dilakukan?',
                    'choices': [
                        {'text': 'Menata nafas dan memusatkan perhatian pada tujuan berserah diri', 'next': 'n2', 'score': 2, 'feedback': 'Pemusatan indra dan nafas adalah bagian sujud raga.'},
                        {'text': 'Mengikuti urutan gerakan agar cepat selesai', 'next': 'n3', 'score': 0, 'feedback': 'Ritual tanpa penghayatan menjadi hambar dan kehilangan makna.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Setelah ritual, temanmu bertanya apa manfaatnya. Apa jawabanmu?',
                    'choices': [
                        {'text': 'Melatih mengendapkan nafsu dan menumbuhkan budi luhur', 'next': 'n4', 'score': 2, 'feedback': 'Ritual menumbuhkan ketaatan dan kepekaan budi luhur.'},
                        {'text': 'Sekadar memenuhi kewajiban adat agar tidak dicela', 'next': 'n3', 'score': 0, 'feedback': 'Motif itu berhenti pada religiositas tanpa penghayatan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Ritual menjadi formalitas tanpa perubahan sikap batin.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kamu memahami ritual sebagai jalan menuju kebenaran Tuhan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa dua sisi nilai ritual?', 'back': 'Religiositas (ketaatan aturan) dan spiritualitas (pelepasan diri menuju Tuhan).'},
            {'front': 'Sebutkan empat tahap sujud manembah.', 'back': 'Sujud raga, batin, jiwa, dan rohani.'},
            {'front': 'Apa itu Wulla Poddu?', 'back': 'Bulan suci komunitas Marapu di Sumba, ditentukan para Rato.'},
            {'front': 'Apa ukuran taraf spiritual kedua?', 'back': 'Bermanfaat bagi diri dan orang lain (mamayu hayuning sasama).'},
        ],
        'checkpoint': (
            'Semboyan Parmalim “parsahataan” bermakna…',
            [
                ('kesatuan bahasa roh dan jalan kebenaran Tuhan', True),
                ('kekuatan doa yang panjang', False),
                ('banyaknya sesaji dalam ritual', False),
                ('keberanian menolak adat', False),
            ],
            'Parsahataan berarti kesatuan bahasa roh dan jalan kebenaran Tuhan.',
        ),
        'challenge': challenge_block(
            'kep-5-tantangan',
            'Tantangan istilah manembah',
            90,
            [
                ('Ketaatan pada ketentuan peribadatan', 'Religiositas'),
                ('Pelepasan diri menuju kehendak Tuhan', 'Spiritualitas'),
                ('Bulan suci Marapu di Sumba', 'Wulla Poddu'),
                ('Perayaan syukuran Parmalim', 'Sipaha Lima'),
                ('Pemuka adat Marapu', 'Rato'),
            ],
            'Lima istilah manembah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Prinsip manembah penghayat kepercayaan Nusantara adalah…', 'berserah diri dan mendekatkan hidup pada jalan kebenaran Tuhan', ['mengumpulkan kekayaan', 'menghindari sesama', 'menolak adat'], 'Perbedaan bentuk ritual tetap berpijak pada prinsip berserah diri.', 'Perlengkapannya bernuansa budaya daerah.'),
        ('Tujuan manembah menurut buku adalah…', 'menyembah Pencipta dan mendekatkan diri kepada-Nya', ['memperoleh kekayaan', 'menambah pengikut', 'menghindari tugas'], 'Manembah bertujuan mendekatkan diri kepada Tuhan.', 'Sekaligus mengumpulkan bekal hidup spiritual.'),
        ('Sikap spiritual “kembali ke asal hidup” disebut…', 'sangkan paraning dumadi', ['mamayu hayuning sasama', 'manunggaling kawulo gusti', 'memayu hayuning pribadi'], 'Hidup akan kembali kepada Pemberi hidup.', 'Ungkapan ini berasal dari falsafah Jawa.'),
        ('Ritual kepercayaan bersifat…', 'suci dan sakral', ['hiburan semata', 'formalitas sosial', 'acara dagang'], 'Karena suci, peserta dan sarana ritual disucikan.', 'Ada persyaratan dan pantangan yang mengikat.'),
        ('Sebelum ritual, penghayat wajib…', 'bersuci diri, raga, dan jiwa', ['berpuasa sebulan', 'membawa sesaji termahal', 'menghafal seluruh doa'], 'Bersuci sendiri sudah merupakan bentuk ritus.', 'Pakaian dan sarana pun dijaga bersih.'),
        ('Sikap melepaskan keterikatan diri menuju kehendak Tuhan disebut…', 'spiritualitas', ['religiositas', 'ritualitas', 'formalitas'], 'Spiritualitas melampaui ritual dan religiositas.', 'Dampaknya terasa ke luar diri.'),
        ('Ketaatan melaksanakan ketentuan peribadatan disebut…', 'religiositas', ['spiritualitas', 'humanisme', 'materialisme'], 'Religiositas berkaitan dengan ketaatan aturan kepercayaan.', 'Sangat melekat pada norma komunitas.'),
        ('Sujud yang mencakup penataan nafas dan denyut nadi adalah…', 'sujud raga', ['sujud batin', 'sujud jiwa', 'sujud rohani'], 'Sujud raga menata tubuh, indra, dan nafas.', 'Menjadi tahap pertama.'),
        ('Sujud yang mendaraskan puja dari hati tulus adalah…', 'sujud jiwa', ['sujud raga', 'sujud batin', 'sujud rohani'], 'Sujud jiwa menggelar puja dari hati.', 'Tahap ketiga dalam urutan.'),
        ('Bulan suci pada komunitas Marapu di Sumba disebut…', 'Wulla Poddu', ['Sipaha Lima', 'Ngaben', 'Sekaten'], 'Wulla Poddu adalah bulan suci bulan pahit.', 'Waktunya ditentukan para Rato.'),
        ('Perayaan syukuran umat Parmalim disebut…', 'Sipaha Lima', ['Wulla Poddu', 'Marakka Bola', 'Mappalili'], 'Sipaha Lima merupakan perayaan syukuran Parmalim.', 'Digelar sebagai ungkapan syukur.'),
        ('Taraf spiritual “mamayu hayuning pribadi” ditandai oleh…', 'menjadi orang baik dan terhindar dari perbuatan tercela', ['menjadi pemimpin politik', 'memiliki banyak pengikut', 'menghafal sastra suci'], 'Taraf awal diukur dari kebaikan diri.', 'Motifnya memperoleh ampunan.'),
        ('Taraf spiritual yang bermanfaat bagi sesama disebut…', 'mamayu hayuning sasama', ['mamayu hayuning pribadi', 'mamayu hayuning bawana', 'manunggaling kawulo gusti'], 'Taraf kedua bermanfaat bagi diri dan orang lain.', 'Orangnya menjadi pamong pencerah.'),
        ('Orang bijaksana yang membaktikan hidup bagi kelestarian alam berada pada taraf…', 'mamayu hayuning bawana', ['mamayu hayuning pribadi', 'mamayu hayuning sasama', 'religiositas awal'], 'Taraf ketiga menjangkau masyarakat luas dan alam.', 'Ia menjadi teladan yang diikuti.'),
    ],
    'multi': [
        ('Manakah sikap spiritual menurut buku?', ['Sangkan paraning dumadi', 'Mamayu hayuning bawana', 'Manunggaling kawulo gusti'], ['Mengejar kekayaan', 'Menghindari ibadah'], 'Ketiganya adalah sikap spiritual dalam manembah.', 'Kekayaan bukan tujuan spiritual.'),
        ('Manakah persiapan ritual manembah?', ['Bersuci', 'Menyatukan tekad jiwa dan raga', 'Bersujud berserah diri'], ['Membawa banyak harta', 'Berdebat tentang keyakinan'], 'Persiapan ritual mencakup kesucian dan pemusatan tekad.', 'Harta bukan syarat utama.'),
        ('Manakah tahap sujud manembah?', ['Sujud raga', 'Sujud batin', 'Sujud rohani'], ['Sujud harta', 'Sujud jabatan'], 'Empat tahap sujud: raga, batin, jiwa, rohani.', 'Harta dan jabatan bukan tahap sujud.'),
        ('Manakah contoh komunitas kepercayaan Nusantara?', ['Parmalim', 'Kaharingan', 'Marapu'], ['Partai politik', 'Koperasi sekolah'], 'Ketiganya komunitas kepercayaan yang disebut buku.', 'Partai dan koperasi bukan komunitas kepercayaan.'),
        ('Manakah ciri religiositas dalam ritual?', ['Taat pada tata urutan', 'Menjauhi pantangan', 'Mengikuti ketentuan adat'], ['Melepas seluruh aturan', 'Menolak norma komunitas'], 'Religiositas berkaitan dengan ketaatan aturan.', 'Melepas aturan bertentangan dengannya.'),
        ('Manakah dampak ketaatan ritual menurut buku?', ['Rendah hati', 'Tolong-menolong', 'Gotong royong'], ['Sombong', 'Individualis'], 'Ketaatan ritual menumbuhkan sikap budi luhur.', 'Kesombongan bertentangan dengannya.'),
        ('Manakah unsur yang disatukan dalam sujud?', ['Cipta', 'Rasa', 'Karsa'], ['Harta', 'Tahta'], 'Sujud menyatukan cipta, rasa, dan karsa.', 'Harta tidak termasuk.'),
        ('Manakah kegunaan hidup menurut buku?', ['Berguna bagi diri sendiri', 'Berguna bagi sesama', 'Berguna bagi keseimbangan alam'], ['Menguasai orang lain', 'Menumpuk kekayaan'], 'Tujuan hidup adalah kebergunaan bagi diri, sesama, dan alam.', 'Penguasaan bukan tujuan hidup.'),
    ],
    'pairs': [
        ('Manembah', 'menyembah dengan segenap hati dan raga'),
        ('Religiositas', 'ketaatan pada ketentuan peribadatan'),
        ('Spiritualitas', 'pelepasan diri menuju kehendak Tuhan'),
        ('Wulla Poddu', 'bulan suci Marapu'),
        ('Sipaha Lima', 'syukuran umat Parmalim'),
        ('Rato', 'pemuka adat Marapu'),
        ('Parsahataan', 'kesatuan roh dan jalan kebenaran'),
        ('Bersuci', 'menyucikan diri sebelum ritual'),
    ],
    'steps': [
        ('Urutkan tahap sujud manembah.', ['Sujud raga', 'Sujud batin', 'Sujud jiwa', 'Sujud rohani', 'Menyatu dengan cahaya kebenaran'], 'Sujud bergerak dari tubuh sampai roh.', 'Sujud rohani menjadi tahap akhir.'),
        ('Urutkan persiapan ritual.', ['Menyucikan diri dan raga', 'Menyiapkan pakaian serta sarana bersih', 'Menyatukan tekad jiwa dan raga', 'Mengatur nafas dan menenangkan indra', 'Bersujud berserah diri'], 'Persiapan berjalan dari kesucian sampai sujud.', 'Bersuci menjadi langkah pertama.'),
        ('Urutkan taraf kecerdasan spiritual.', ['Mamayu hayuning pribadi', 'Mamayu hayuning sasama', 'Mamayu hayuning bawana'], 'Taraf meningkat dari diri, sesama, lalu alam semesta.', 'Taraf terakhir disebut bijaksana.'),
        ('Urutkan empat langkah kesatuan roh dan kebenaran.', ['Menyembah dengan segenap hati', 'Menanggalkan ego diri', 'Memasuki jalan kebenaran Tuhan', 'Menyatu dalam cahaya kebenaran'], 'Langkah dimulai dari penyembahan penuh hati sampai penyatuan.', 'Penanggalan ego menjadi langkah kedua.'),
        ('Urutkan langkah menyiapkan diri mengikuti ritual komunitas.', ['Mempelajari tata cara ritual', 'Menyiapkan pakaian adat yang bersih', 'Membersihkan sarana ritual', 'Hadir tepat waktu dengan hati tenang', 'Mengikuti seluruh prosesi dengan khusyuk'], 'Persiapan mencakup pengetahuan, kelengkapan, dan ketenangan hati.', 'Kekhusyukan menutup rangkaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
