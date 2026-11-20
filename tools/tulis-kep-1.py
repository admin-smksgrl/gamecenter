"""KEP 1 — Sejarah Kepercayaan terhadap Tuhan Yang Maha Esa (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    timeline_block,
    write_chapter,
)

CH = {
    'code': 'KEP 1',
    'slug': 'kep-1-sejarah-kepercayaan',
    'title': 'Sejarah Kepercayaan terhadap Tuhan Yang Maha Esa',
    'description': (
        'Menelusuri asal-usul hidup dan kehidupan, keberagaman sistem kepercayaan '
        'Nusantara, serta perjuangan penghayat dalam memperoleh pengakuan dan hak '
        'sipil sebelum dan sesudah kemerdekaan.'
    ),
    'objectives': [
        'Memberikan argumentasi tentang asal-usul hidup dan kehidupan dengan beberapa teori asal mula alam semesta.',
        'Menuliskan sejarah Kepercayaan terhadap Tuhan Yang Maha Esa meliputi konsep kepercayaan, konsep Ketuhanan, dan ajaran budi luhurnya.',
        'Meneladani perjuangan kepercayaan sebagai nilai sikap dalam kehidupan hingga pergaulan global.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 1 Sejarah Kepercayaan Terhadap Tuhan Yang '
        'Maha Esa; CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Kepercayaan', 'definition': 'Pernyataan dan pelaksanaan hubungan manusia dengan Tuhan Yang Maha Esa melalui tata laku tertentu disertai pengamalan budi luhur.'},
        {'term': 'Tondi', 'definition': 'Sebutan roh atau hidup dalam bahasa Batak, yaitu dzat Tuhan yang diberikan kepada manusia.'},
        {'term': 'Urip', 'definition': 'Sebutan hidup atau roh dalam bahasa Jawa.'},
        {'term': 'Teori nebula', 'definition': 'Teori asal tata surya dari pusaran kabut gas panas yang memadat selama jutaan tahun.'},
        {'term': 'The Missing Link', 'definition': 'Istilah untuk mata rantai evolusi manusia yang belum ditemukan bukti gamblangnya.'},
        {'term': 'Animisme', 'definition': 'Paham dalam kebudayaan tentang kepercayaan pada roh, bukan bentuk kepercayaan keagamaan tersendiri.'},
        {'term': 'Mulajadi Nabolon', 'definition': 'Sebutan Tuhan Yang Maha Pencipta dalam kepercayaan Parmalim, Batak Toba.'},
        {'term': 'Marapu', 'definition': 'Kepercayaan masyarakat Sumba; surga roh disebut Prai Marapu.'},
        {'term': 'Hak sipil', 'definition': 'Hak sebagai warga negara, termasuk pencatatan sipil dan layanan pendidikan.'},
        {'term': 'Sangkan paraning dumadi', 'definition': 'Falsafah Jawa: asal dan tujuan akhir segala yang menjadi, yaitu Tuhan.'},
    ],
    'intro': {
        'material_title': 'Mengapa perlu mengenal asal-usul?',
        'title': 'Kepercayaan dan asal-usul hidup',
        'paragraphs': [
            'Kepercayaan terhadap Tuhan Yang Maha Esa secara etimologi berarti mengakui dengan sungguh, meyakini, serta tunduk berserah diri kepada Tuhan Yang Maha Esa, Pencipta yang Maha Besar (Usman Pelly dalam Gultom, 2010).',
            'Inti ajarannya ada dua. Pertama, Tuhan Maha Esa dan Maha Kuasa melampaui semua daya yang dikenali manusia. Kedua, tujuan hidup adalah kembali ke asal: roh suci menjadi penghubung kehendak Tuhan, disebut tondi dalam bahasa Batak dan urip dalam bahasa Jawa.',
            'Manusia bukan sekadar tubuh biologis. Ada tiga elemen hidup: tubuh sebagai wadah, roh dalam batin sebagai hidup yang hakiki, dan akal sebagai alat berpikir dan merasa yang menyeimbangkan hidup ragawi serta rohani.',
        ],
        'diagram': (
            'Tiga elemen manusia hidup',
            'flowchart TB\n'
            '  A[Manusia hidup] --> B[Tubuh biologis: raga sebagai wadah]\n'
            '  A --> C[Roh dalam batin: hidup yang hakiki]\n'
            '  A --> D[Akal: pikiran dan hati]\n'
            '  C --> E[Terhubung pada Tuhan sumber hidup]\n'
            '  D --> F[Kebijaksanaan dan keseimbangan hidup]',
        ),
        'callout': 'Animisme dan dinamisme bukan bentuk kepercayaan keagamaan, melainkan paham dalam kebudayaan; penghayat menyembah Tuhan Yang Maha Esa.',
        'checkpoint': (
            'Sebutan roh atau hidup dalam bahasa Batak adalah…',
            [
                ('tondi', True),
                ('urip', False),
                ('marapu', False),
                ('kaharingan', False),
            ],
            'Tondi (Batak) dan urip (Jawa) sama-sama menunjuk roh atau hidup pemberian Tuhan.',
        ),
    },
    'concept': {
        'material_title': 'Keberagaman sistem kepercayaan',
        'title': 'Sebutan Tuhan dan tipe penghayat',
        'paragraphs': [
            'Penyebutan Sang Pencipta berbeda menurut bahasa dan budaya: Mulajadi Nabolon pada Parmalim Batak Toba, Mori atau Magholo-Marawi pada Marapu Sumba, Eyang Gusti Agung, Sang Hyang, dan Sangkan Paran pada budaya spiritual Jawa, serta Pangeran di Sunda.',
            'Dari sisi pribadi ada dua tipe penghayat: yang menyembah hanya kepada Tuhan Yang Maha Esa, dan yang menyembah Tuhan namun juga menerima kekuatan alam atau astral sebagai tuntunan hidup.',
            'Dari sisi komunitas ada dua tipe: komunitas tertutup yang terpusat pada satu daerah etnis, dan komunitas terbuka yang penghayatnya terpencar serta hidup berdampingan dengan pemeluk agama besar.',
        ],
        'table': [
            ['Daerah atau komunitas', 'Sebutan Tuhan', 'Keterangan'],
            ['Batak Toba (Parmalim)', 'Mulajadi Nabolon', 'Mula berarti awal, Nabolon berarti maha besar'],
            ['Sumba (Marapu)', 'Mori atau Magholo-Marawi', 'Surga roh disebut Prai Marapu'],
            ['Jawa (budaya spiritual)', 'Sangkan Paran, Gusti Pangeran', 'Falsafah sangkan paraning dumadi'],
            ['Sunda', 'Pangeran', 'Berkembang dalam Sunda Wiwitan'],
            ['Kalimantan (Kaharingan)', 'Ranying Hatalla Langit', 'Menyatu dengan adat Dayak'],
        ],
        'visual': timeline_block(
            'kep-1-timeline',
            [
                ('1908', 'Budi Utomo berdiri', 'Kesadaran berorganisasi penduduk pribumi tumbuh.'),
                ('1928', 'Sumpah Pemuda', 'Tonggak nasionalisme Indonesia; Indonesia Raya dinyanyikan dua stanza.'),
                ('1945', 'Pasal 29 UUD 1945', 'Kata “kepercayaan” masuk berkat perjuangan tokoh kepercayaan.'),
                ('1973', 'TAP MPR IV/1973', 'Pembinaan penghayat kepercayaan diamanatkan negara.'),
                ('2006', 'UU No. 23/2006', 'Administrasi kependudukan mengakui kolom kepercayaan.'),
                ('2016', 'Putusan MK 97/PUU-XIV/2016', 'Agama dan kepercayaan dinyatakan setara kedudukannya.'),
            ],
        ),
        'activity': categorize_block(
            'kep-1-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam tipe penghayat atau tipe komunitas yang sesuai.',
            [('b1', 'Tipe pribadi'), ('b2', 'Tipe komunitas')],
            [
                ('i1', 'Menyembah hanya kepada Tuhan Yang Maha Esa', 'b1'),
                ('i2', 'Menyembah Tuhan dan menerima kekuatan astral', 'b1'),
                ('i3', 'Penghayat terpusat pada satu daerah etnis', 'b2'),
                ('i4', 'Penghayat terpencar dan berdampingan dengan agama besar', 'b2'),
                ('i5', 'Lembaga menjadi wadah pemersatu, bukan wilayah', 'b2'),
                ('i6', 'Pemimpin tidak berwenang sebagai penguasa politis', 'b2'),
            ],
            'Tepat. Tipe pribadi menyangkut cara menyembah, tipe komunitas menyangkut sebaran dan kelembagaan.',
            'Periksa lagi: ciri kelembagaan dan sebaran penghayat termasuk tipe komunitas.',
        ),
        'subtitle': 'Jalan perjuangan penghayat',
        'list': [
            'Masa pergerakan: paguyuban kebatinan tumbuh tanpa tendensi politik, seperti Sumarah, Subud, Hardo Pusara, dan Purba Jati.',
            'Tokoh nasional dari kalangan penghayat antara lain Sudirman (Paguyuban Sumarah) dan KMRT Wongsonegoro yang duduk di BPUPKI.',
            'Setelah kemerdekaan, rentetan aturan memperkuat hak sipil: PP 37/2007, Perpres 25/2008, Peraturan Bersama Mendagri dan Menbudpar 43 dan 41/2009, serta Permendiknas 27/2016.',
            'Putusan MK 97/PUU-XIV/2016 menegaskan agama dan kepercayaan setara, sesuai Pasal 29 UUD 1945 dan Pasal 28E ayat (1)–(2).',
        ],
        'checkpoint': (
            'Tokoh penghayat yang ikut merumuskan Pasal 29 UUD 1945 adalah…',
            [
                ('KMRT Wongsonegoro', True),
                ('Charles Darwin', False),
                ('Pater W. Schmidt', False),
                ('Usman Pelly', False),
            ],
            'Wongsonegoro adalah tokoh kepercayaan nasional yang duduk di BPUPKI dan pernah menjabat Menteri Pendidikan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Dari teori asal-usul sampai hak sipil',
        'paragraphs': [
            'Ilmu pengetahuan menjelaskan asal benda fisik lewat teori nebula dan evolusi, sedangkan kepercayaan menjelaskan asal hidup dan kehidupan rohaniah. Keduanya berbeda titik pandang sehingga tidak dapat diperbandingkan secara langsung.',
            'Teori nebula menyebut tata surya berasal dari pusaran kabut gas panas yang mendingin jutaan tahun. Evolusi berlanjut hingga terbentuk DNA dan RNA, virus, mitokondria, kloroplast, bakteri, lalu tumbuhan dan hewan.',
            'Charles Darwin dalam On the Origin of Species by Means of Natural Selection menyatakan spesies sekarang berasal dari perubahan perlahan spesies sebelumnya, dan individu yang mampu beradaptasi akan bertahan. Namun Darwin tidak membahas asal-usul manusia; celah itulah yang disebut The Missing Link.',
        ],
        'scenario': scenario(
            'kep-1-skenario',
            'Menjelaskan kepercayaan kepada teman',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Temanmu bertanya, “Kepercayaanmu menyembah apa?” Apa jawaban terbaik?',
                    'choices': [
                        {'text': 'Menyembah Tuhan Yang Maha Esa, Pencipta alam semesta', 'next': 'n2', 'score': 2, 'feedback': 'Jawaban itu sesuai inti ajaran kepercayaan.'},
                        {'text': 'Menyembah roh leluhur dan benda keramat', 'next': 'n3', 'score': 0, 'feedback': 'Penghayat menyembah Tuhan; penghormatan leluhur bukan penyembahan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Temanmu menyebut kepercayaan sebagai animisme. Bagaimana sikapmu?',
                    'choices': [
                        {'text': 'Menjelaskan bahwa animisme adalah paham budaya, bukan bentuk kepercayaan', 'next': 'n4', 'score': 2, 'feedback': 'Penjelasan itu meluruskan istilah secara tepat.'},
                        {'text': 'Diam dan menjauhi teman tersebut', 'next': 'n3', 'score': 0, 'feedback': 'Menjauh tidak membangun saling pengertian.'},
                    ],
                },
                {'id': 'n3', 'text': 'Salah paham berlanjut dan pergaulan menjadi renggang.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Teman memahami dan menghormati kepercayaanmu.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa dua inti ajaran kepercayaan?', 'back': 'Tuhan Maha Esa dan Maha Kuasa; tujuan hidup kembali ke asal.'},
            {'front': 'Apa isi teori nebula?', 'back': 'Tata surya terbentuk dari pusaran kabut gas panas yang mendingin.'},
            {'front': 'Mengapa Darwin tidak menjelaskan asal manusia?', 'back': 'Ia tidak membahasnya; celah bukti itu disebut The Missing Link.'},
            {'front': 'Apa isi Putusan MK 97/PUU-XIV/2016?', 'back': 'Agama dan kepercayaan setara kedudukannya sebagai hak konstitusional.'},
        ],
        'checkpoint': (
            'Fosil Homo erectus sebagian ditemukan di pulau…',
            [
                ('Jawa', True),
                ('Sumatra', False),
                ('Bali', False),
                ('Sulawesi', False),
            ],
            'Homo erectus berusia sekitar 2–2,5 juta tahun dan sebagian fosilnya ditemukan di Jawa.',
        ),
        'challenge': challenge_block(
            'kep-1-tantangan',
            'Tantangan istilah sejarah kepercayaan',
            90,
            [
                ('Roh dalam bahasa Batak', 'Tondi'),
                ('Roh dalam bahasa Jawa', 'Urip'),
                ('Sebutan Tuhan pada Parmalim', 'Mulajadi Nabolon'),
                ('Celah bukti evolusi manusia', 'The Missing Link'),
                ('Penulis On the Origin of Species', 'Charles Darwin'),
            ],
            'Lima istilah sejarah kepercayaan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Secara etimologi, kepercayaan berarti…', 'mengakui, meyakini, dan berserah diri kepada Tuhan Yang Maha Esa', ['menolak semua kekuatan gaib', 'menyembah benda-benda pusaka', 'mengikuti adat tanpa keyakinan'], 'Kepercayaan berarti mengakui sungguh, meyakini, dan tunduk berserah kepada Tuhan.', 'Disertai pengamalan nilai budi luhur.'),
        ('Sebutan roh kehidupan dalam bahasa Jawa adalah…', 'urip', ['tondi', 'marapu', 'kaharingan'], 'Urip (Jawa) dan tondi (Batak) bermakna hidup atau roh.', 'Keduanya dzat Tuhan dalam diri manusia.'),
        ('Tiga elemen manusia hidup menurut buku adalah…', 'tubuh biologis, roh, dan akal', ['tubuh, harta, dan tahta', 'roh, alam, dan leluhur', 'akal, nafsu, dan tenaga'], 'Manusia terdiri atas raga, roh dalam batin, dan akal.', 'Akal menyeimbangkan hidup ragawi dan rohani.'),
        ('Teori asal tata surya dari kabut gas panas disebut teori…', 'nebula', ['relativitas', 'big bang', 'seleksi alam'], 'Teori nebula menyebut tata surya berasal dari pusaran kabut gas.', 'Gas mendingin selama jutaan tahun.'),
        ('Buku Darwin yang membahas seleksi alam berjudul…', 'On the Origin of Species by Means of Natural Selection', ['The Descent of Man', 'Das Kapital', 'Leviathan'], 'Darwin menulis On the Origin of Species by Means of Natural Selection.', 'Buku itu tidak membahas asal usul manusia.'),
        ('Istilah untuk mata rantai evolusi manusia yang belum ditemukan adalah…', 'The Missing Link', ['Homo erectus', 'Natural Selection', 'Pithecanthropus'], 'Celah bukti itu dikenal sebagai The Missing Link.', 'Diisi penelitian geologi dan paleontologi.'),
        ('Sebutan Tuhan Yang Pencipta pada Parmalim Batak Toba adalah…', 'Mulajadi Nabolon', ['Mori', 'Sangkan Paran', 'Pangeran'], 'Mulajadi Nabolon berarti awal yang maha besar.', 'Diajarkan dalam kepercayaan Parmalim.'),
        ('Surga roh dalam kepercayaan Marapu disebut…', 'Prai Marapu', ['Praja Marapu', 'Sorga Mori', 'Kaharingan'], 'Penghayat Marapu meyakini hidup kekal di Prai Marapu.', 'Marapu dianut masyarakat Sumba.'),
        ('Paham kepercayaan pada roh yang ada dalam kebudayaan disebut…', 'animisme', ['monoteisme', 'panteisme', 'ateisme'], 'Animisme adalah paham budaya, bukan bentuk kepercayaan keagamaan.', 'Sering disalahgunakan untuk melabeli penghayat.'),
        ('Falsafah Jawa tentang asal dan tujuan hidup adalah…', 'sangkan paraning dumadi', ['mamayu hayuning bawana', 'manunggaling kawula gusti', 'eling lan waspada'], 'Sangkan berarti asal, paran tujuan akhir, dumadi menjadi.', 'Menegaskan Tuhan sebagai asal dan tujuan.'),
        ('Organisasi yang berdiri tahun 1908 sebagai awal kesadaran berorganisasi adalah…', 'Budi Utomo', ['Sumpah Pemuda', 'Paguyuban Sumarah', 'BPUPKI'], 'Budi Utomo berdiri pada 1908.', 'Menandai tumbuhnya perkumpulan pribumi.'),
        ('Tokoh penghayat dari Paguyuban Sumarah yang menjadi Panglima Besar adalah…', 'Sudirman', ['Wongsonegoro', 'Usman Pelly', 'W. Schmidt'], 'Sudirman berasal dari Paguyuban Sumarah.', 'Ia menjadi Panglima Besar tentara Indonesia.'),
        ('Kata “kepercayaan” dalam Pasal 29 UUD 1945 merupakan hasil perjuangan…', 'para tokoh pendiri bangsa', ['peneliti Barat', 'pemerintah kolonial', 'organisasi internasional'], 'Perumusan pasal itu buah perjuangan intelektual tokoh bangsa.', 'Salah satu perumusnya Wongsonegoro.'),
        ('Putusan MK yang menyatakan agama dan kepercayaan setara adalah…', 'Putusan MK 97/PUU-XIV/2016', ['Putusan MK 97/PUU-XIV/2006', 'TAP MPR IV/1973', 'UU No. 23/2006'], 'Putusan itu mengabulkan gugatan atas UU Adminduk.', 'Menegaskan kesetaraan kedudukan.'),
    ],
    'multi': [
        ('Manakah elemen manusia hidup menurut buku?', ['Tubuh biologis', 'Roh dalam batin', 'Akal'], ['Harta warisan', 'Kekuasaan politik'], 'Manusia terdiri atas raga, roh, dan akal.', 'Harta dan kekuasaan bukan elemen hidup.'),
        ('Manakah sebutan Tuhan dalam budaya spiritual Nusantara?', ['Mulajadi Nabolon', 'Sangkan Paran', 'Pangeran'], ['Zeus', 'Odin'], 'Sebutan Tuhan menyesuaikan bahasa dan budaya setempat.', 'Zeus dan Odin berasal dari mitologi Eropa.'),
        ('Manakah peraturan yang memperkuat hak sipil penghayat?', ['UU No. 23 Tahun 2006', 'PP No. 37 Tahun 2007', 'Permendiknas No. 27 Tahun 2016'], ['UU No. 1 Tahun 1970', 'PP No. 10 Tahun 1980'], 'Ketiganya mengatur adminduk dan layanan pendidikan penghayat.', 'Peraturan itu menjamin layanan negara.'),
        ('Manakah isi ajaran kepercayaan menurut buku?', ['Hubungan dengan Tuhan Yang Maha Esa', 'Penghayatan tulus dan ikhlas', 'Pengamalan budi pekerti luhur'], ['Penyembahan kepada benda', 'Permusuhan antar keyakinan'], 'Ajaran kepercayaan menekankan hubungan dengan Tuhan dan budi luhur.', 'Penghayat menyembah Tuhan, bukan benda.'),
        ('Manakah teori asal usul kehidupan yang dibahas?', ['Teori nebula', 'Teori evolusi Darwin', 'Teori seleksi alam'], ['Teori relativitas umum', 'Teori kuantum warna'], 'Buku membahas nebula, evolusi, dan seleksi alam.', 'Relativitas bukan teori asal kehidupan.'),
        ('Manakah tipe komunitas penghayat?', ['Komunitas tertutup', 'Komunitas terbuka'], ['Komunitas politik', 'Komunitas dagang'], 'Buku menyebut komunitas tertutup dan terbuka.', 'Keduanya dibedakan oleh sebaran penghayat.'),
        ('Manakah tokoh yang berperan dalam perjuangan kepercayaan?', ['Sudirman', 'KMRT Wongsonegoro', 'Mr. Wongsonegoro di BPUPKI'], ['Charles Darwin', 'Pater W. Schmidt'], 'Sudirman dan Wongsonegoro berperan pada masa perjuangan.', 'Darwin dan Schmidt adalah peneliti.'),
        ('Manakah hak yang diperjuangkan penghayat?', ['Pencatatan sipil', 'Layanan pendidikan kepercayaan', 'Kolom kepercayaan di KTP'], ['Pembebasan pajak penuh', 'Hak memilih tanpa syarat usia'], 'Perjuangan itu berbuah layanan adminduk dan pendidikan.', 'Hak politik tetap mengikuti aturan umum.'),
    ],
    'pairs': [
        ('Tondi', 'roh dalam bahasa Batak'),
        ('Urip', 'hidup dalam bahasa Jawa'),
        ('Teori nebula', 'asal tata surya dari kabut gas'),
        ('The Missing Link', 'celah bukti evolusi manusia'),
        ('Mulajadi Nabolon', 'sebutan Tuhan pada Parmalim'),
        ('Prai Marapu', 'surga roh dalam kepercayaan Sumba'),
        ('Sangkan paraning dumadi', 'falsafah asal dan tujuan hidup Jawa'),
        ('Budi Utomo', 'organisasi pribumi tahun 1908'),
    ],
    'steps': [
        ('Urutkan alur pembentukan tata surya menurut teori nebula.', ['Kabut gas panas berputar', 'Pendinginan selama jutaan tahun', 'Pembentukan planet', 'Pusat pusaran menjadi matahari', 'Bumi memiliki lautan, daratan, dan atmosfer'], 'Kabut gas mendingin lalu membentuk planet dan matahari.', 'Pusat pusaran menjadi bintang.'),
        ('Urutkan tahap evolusi molekul kehidupan.', ['Asam amino dan gula sederhana', 'DNA dan RNA', 'Virus, mitokondria, kloroplast', 'Sel bakteri dan protozoa', 'Tumbuhan dan hewan'], 'Kehidupan bergerak dari molekul sederhana ke makhluk kompleks.', 'DNA dan RNA dianggap ciri kehidupan paling awal.'),
        ('Urutkan peristiwa perjuangan kepercayaan.', ['Budi Utomo 1908', 'Sumpah Pemuda 1928', 'Pasal 29 UUD 1945', 'TAP MPR IV/1973', 'UU Adminduk 2006', 'Putusan MK 2016'], 'Perjuangan bergerak dari organisasi, deklarasi, konstitusi, sampai putusan MK.', 'Putusan MK menjadi tonggak terakhir dalam urutan ini.'),
        ('Urutkan langkah menjelaskan kepercayaan kepada orang lain.', ['Mengenali inti ajaran sendiri', 'Memilih kata yang mudah dipahami', 'Menjelaskan perbedaan istilah animisme', 'Membuka ruang dialog', 'Menghormati perbedaan keyakinan'], 'Penjelasan dimulai dari pemahaman diri lalu dialog yang saling menghormati.', 'Dialog menutup rangkaian penjelasan.'),
        ('Urutkan lapisan bukti asal-usul manusia menurut buku.', ['Fosil manusia purba', 'Perunutan fosil peradaban', 'Hipotesis geologi dan antropologi', 'Celah The Missing Link'], 'Bukti fosil menuntun hipotesis, namun celah masih ada.', 'Celah itulah yang belum terisi.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
