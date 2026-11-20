"""KEP 7 — Mencermati Larangan dan Kewajiban (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 7',
    'slug': 'kep-7-larangan-dan-kewajiban',
    'title': 'Mencermati Larangan dan Kewajiban',
    'description': (
        'Mengamalkan empat kewajiban penghayat—kerja keras, cinta sesama, memelihara '
        'alam, dan manembah—serta menjauhi larangan sebagai rambu hidup di jalan '
        'kebenaran dan cinta.'
    ),
    'objectives': [
        'Mengamalkan perbuatan baik sebagai cerminan sikap religius dan spiritual dalam kehidupan nyata.',
        'Menganalisis dan menyajikan larangan dan kewajiban dalam kepercayaan berkaitan dengan ketaatan atas perintah Tuhan.',
        'Menjelaskan keterkaitan nilai kearifan lokal, adat, dan tradisi dengan larangan dalam kepercayaan.',
        'Menjelaskan tahapan prosedural menjalankan kewajiban dan menghindari larangan.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 8 Mencermati Larangan dan Kewajiban; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Kewajiban', 'definition': 'Ketentuan yang harus ditunaikan penghayat sebagai bentuk ketundukan pada perintah Tuhan.'},
        {'term': 'Larangan', 'definition': 'Rambu hidup di jalan suci yang memandu pelaksanaan kewajiban agar syarat terpenuhi.'},
        {'term': 'Tabu', 'definition': 'Pantangan dalam ritual dan kehidupan komunitas yang tidak boleh dilanggar.'},
        {'term': 'Mawas diri', 'definition': 'Sikap mengendapkan hawa nafsu dan mengendalikan hati, pikiran, ucapan, serta tindakan.'},
        {'term': 'Mamayu hayuning bawana', 'definition': 'Kewajiban memelihara alam sebagai wujud syukur kepada Tuhan.'},
        {'term': 'Pasahat Tondi', 'definition': 'Persembahan ritual pada Parmalim, menyerahkan roh atau hidup kepada Tuhan.'},
        {'term': 'Perbuatan tercela', 'definition': 'Perbuatan yang melanggar norma tertulis maupun tidak tertulis di masyarakat.'},
        {'term': 'Tenggang rasa', 'definition': 'Sikap mawas sesama dengan menghormati martabat dan hak orang lain.'},
    ],
    'intro': {
        'material_title': 'Apa kewajiban penghayat?',
        'title': 'Empat orientasi kewajiban manusia',
        'paragraphs': [
            'Kepercayaan adalah ketundukan menyembah dan berserah diri kepada Tuhan dengan syarat sikap budi luhur, yaitu cinta dan kebenaran sejati. Dari sikap itu lahir kewajiban-kewajiban manusia.',
            'Kewajiban pertama: bekerja keras dalam kebenaran untuk menghidupi diri dan keluarga, lalu sebagian hasilnya dipakai untuk kebajikan. Kewajiban kedua: mencintai sesama dan menghormati pemimpin.',
            'Kewajiban ketiga: aktif menjaga dan memelihara alam sebagai wujud mamayu hayuning bawana. Kewajiban keempat, manembah dengan sujud syukur, menjadi puncak keyakinan dan ketundukan kepada Sang Pencipta.',
        ],
        'diagram': (
            'Empat kewajiban menuju manembah',
            'flowchart TB\n'
            '  A[Kewajiban 1: kerja keras dalam kebenaran] --> B[Kewajiban 2: cinta sesama dan hormat pemimpin]\n'
            '  B --> C[Kewajiban 3: memelihara alam]\n'
            '  C --> D[Kewajiban 4: manembah dengan sujud syukur]\n'
            '  D --> E[Puncak ketundukan kepada Tuhan]',
        ),
        'callout': 'Menyembah Tuhan sebagai puncak kewajiban tidak boleh mengabaikan tiga kewajiban sebelumnya.',
        'checkpoint': (
            'Kewajiban yang menjadi puncak berkeyakinan menurut buku adalah…',
            [
                ('manembah dengan sujud syukur', True),
                ('menumpuk kekayaan', False),
                ('menguasai wilayah', False),
                ('menghindari pergaulan', False),
            ],
            'Manembah menjadi puncak karena menghimpun ketundukan, syukur, dan kesucian.',
        ),
    },
    'concept': {
        'material_title': 'Larangan sebagai rambu jalan suci',
        'title': 'Boleh dan tidak boleh',
        'paragraphs': [
            'Perintah mulanya satu: menyembah Pencipta dan tunduk pada kehendak-Nya. Karena hidup atau roh sedang dipertaruhkan, syarat persembahan harus agung dan suci, sehingga ketentuan selalu berpasangan: yang boleh dan yang tidak boleh.',
            'Larangan memandu pelaksanaan kewajiban agar semua syarat terpenuhi. Contoh sederhana: saat berdoa ada larangan gerak-gerik liar, pandangan tidak fokus, suasana gaduh, atau larangan tertentu bagi wanita yang sedang haid dan baru melahirkan.',
            'Larangan umum terkait martabat kemanusiaan: mencuri, berzina, membunuh, memfitnah, menghina atau merendahkan, menyesatkan atau bertipu daya, serta mengurangi hak orang lain.',
        ],
        'table': [
            ['Orientasi kewajiban', 'Wujud kewajiban', 'Contoh larangan terkait'],
            ['Diri sendiri dan keluarga', 'Mawas diri', 'Menuruti nafsu dan sikap sombong'],
            ['Sesama manusia', 'Tenggang rasa', 'Memfitnah, menghina, mengurangi hak'],
            ['Alam dan lingkungan', 'Memelihara alam', 'Merusak sumber air dan hutan'],
            ['Tuhan', 'Manembah dengan syukur', 'Meninggalkan ibadah dan larangan ritual'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-7-ritual',
            'engine': 'mermaid',
            'title': 'Tiga nuansa ritual kehidupan',
            'code': 'flowchart TB\n'
                    '  A[Ritual kehidupan] --> B[Nuansa kepercayaan ketuhanan]\n'
                    '  A --> C[Nuansa kekerabatan dan interaksi sosial]\n'
                    '  A --> D[Nuansa memanfaatkan alam]\n'
                    '  B --> E[Idealisme dan kesucian]\n'
                    '  C --> F[Aturan dan larangan sosial]\n'
                    '  D --> G[Aturan ekologi dan ekonomi]\n'
                    '  E --> H[Perbuatan baik]\n'
                    '  F --> H\n'
                    '  G --> H',
        },
        'activity': categorize_block(
            'kep-7-klasifikasi',
            'Kelompokkan perbuatan berikut sebagai perbuatan baik atau perbuatan tercela.',
            [('b1', 'Perbuatan baik'), ('b2', 'Perbuatan tercela')],
            [
                ('i1', 'Mengembalikan barang temuan', 'b1'),
                ('i2', 'Menolong teman yang kesusahan', 'b1'),
                ('i3', 'Menjaga kebersihan lingkungan', 'b1'),
                ('i4', 'Menyebar kabar bohong', 'b2'),
                ('i5', 'Mengambil hak orang lain', 'b2'),
                ('i6', 'Menghina keyakinan teman', 'b2'),
                ('i7', 'Meminta maaf setelah berbuat salah', 'b1'),
                ('i8', 'Menipu demi keuntungan', 'b2'),
            ],
            'Tepat. Perbuatan baik sesuai norma kewajiban, perbuatan tercela melanggar rambu larangan.',
            'Periksa lagi: menipu, menghina, dan memfitnah termasuk perbuatan tercela.',
        ),
        'subtitle': 'Tiga dimensi hubungan kehidupan',
        'list': [
            'Tiga dimensi hubungan manusia: terhadap Tuhan, terhadap sesama (diri, kerabat, dan manusia lain), serta terhadap alam penghidupan.',
            'Setiap ritual mencakup norma ketentuan dari ketiga bentuk hubungan sekaligus.',
            'Larangan dan tabu dalam nuansa kepercayaan dianggap paling utama karena berkaitan dengan idealisme.',
            'Tindakan sesuai norma disebut perbuatan baik dan beradat; pelanggaran larangan disebut perbuatan tercela.',
        ],
        'checkpoint': (
            'Pelanggaran larangan kepercayaan dipercaya membawa akibat…',
            [
                ('tidak selamat atau celaka di dunia dan kehidupan rohaniah', True),
                ('keuntungan duniawi', False),
                ('kebebasan berperilaku', False),
                ('pujian masyarakat', False),
            ],
            'Ganjaran atas pelanggaran adalah ketidakselamatan di dunia maupun kehidupan rohaniah.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menjauhi larangan, mendekat kepada Tuhan',
        'paragraphs': [
            'Fungsi perintah dan larangan ibarat rambu lalu lintas: tanpa rambu terjadi kekacauan dan kecelakaan. Keselarasan, keseimbangan, dan harmonisasi kehidupan adalah target utama perintah dan larangan Tuhan.',
            'Cara menjauhi larangan ada tiga. Pertama, bersyukur dalam keadaan apa pun, sebab semua adalah kehendak dan rencana agung Tuhan. Kedua, berserah diri sepenuh hati: suka cita jangan dianggap keberhasilan sendiri, kesedihan jangan ditanggung berlarut-larut.',
            'Ketiga, mawas diri: mengendapkan hawa nafsu, mengendalikan hati, pikiran, ucapan, dan tindakan. Melawan nafsu berlaku bagi siapa pun; semakin tinggi pohon semakin kencang angin menerpanya.',
        ],
        'scenario': scenario(
            'kep-7-skenario',
            'Godaan mencontek di ulangan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Saat ulangan, temanmu menawarkan kunci jawaban. Apa keputusanmu?',
                    'choices': [
                        {'text': 'Menolak dan mengerjakan dengan kemampuan sendiri', 'next': 'n2', 'score': 2, 'feedback': 'Menolak mencontek menjaga kejujuran dan martabat.'},
                        {'text': 'Menerimanya karena semua teman melakukannya', 'next': 'n3', 'score': 0, 'feedback': 'Mengikuti arus tetap melanggar larangan menipu.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Nilai ulanganmu lebih rendah dari teman yang mencontek. Bagaimana sikapmu?',
                    'choices': [
                        {'text': 'Menerimanya sebagai pelajaran dan belajar lebih giat', 'next': 'n4', 'score': 2, 'feedback': 'Menerima hasil dengan mawas diri adalah sikap berbudi luhur.'},
                        {'text': 'Menyesal tidak ikut mencontek', 'next': 'n3', 'score': 0, 'feedback': 'Penyesalan itu justru melemahkan tekad kebenaran.'},
                    ],
                },
                {'id': 'n3', 'text': 'Kebiasaan mencontek merusak kejujuran dan kepercayaan orang lain.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kamu tetap dipercaya dan hasil belajarmu terus membaik.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan empat kewajiban penghayat.', 'back': 'Kerja keras, cinta sesama, memelihara alam, dan manembah.'},
            {'front': 'Sebutkan tiga cara menjauhi larangan.', 'back': 'Bersyukur, berserah diri sepenuh hati, dan mawas diri.'},
            {'front': 'Mengapa larangan diperlukan?', 'back': 'Agar semua syarat kewajiban terpenuhi dan kehidupan selaras.'},
            {'front': 'Apa tiga dimensi hubungan kehidupan manusia?', 'back': 'Dengan Tuhan, sesama manusia, dan alam penghidupan.'},
        ],
        'checkpoint': (
            'Menurut buku, larangan memandu…',
            [
                ('pelaksanaan kewajiban agar syarat terpenuhi', True),
                ('pembagian harta warisan', False),
                ('pemilihan pemimpin politik', False),
                ('penentuan harga barang', False),
            ],
            'Larangan adalah rambu agar kewajiban dilaksanakan dengan syarat yang lengkap.',
        ),
        'challenge': challenge_block(
            'kep-7-tantangan',
            'Tantangan istilah larangan dan kewajiban',
            90,
            [
                ('Rambu hidup di jalan suci', 'Larangan'),
                ('Menjaga alam sebagai syukur', 'Mamayu hayuning bawana'),
                ('Mengendalikan hati, pikiran, ucapan', 'Mawas diri'),
                ('Pantangan dalam ritual', 'Tabu'),
                ('Menghormati martabat sesama', 'Tenggang rasa'),
            ],
            'Lima istilah larangan dan kewajiban terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Kewajiban pertama penghayat menurut buku adalah…', 'bekerja keras dalam kebenaran', ['menambah harta', 'menguasai wilayah', 'berhenti belajar'], 'Kerja keras menghidupi diri dan keluarga di jalan kebenaran.', 'Sebagian hasilnya dipakai berbuat kebajikan.'),
        ('Kewajiban memelihara alam disebut wujud…', 'mamayu hayuning bawana', ['sangkan paraning dumadi', 'manunggaling kawulo gusti', 'tepa selira'], 'Dari alamlah manusia memperoleh penghidupan dan perlengkapan ibadah.', 'Memelihara alam adalah bentuk syukur.'),
        ('Puncak berkeyakinan dalam kepercayaan adalah…', 'manembah dengan sujud syukur', ['menimbun kekayaan', 'menjadi penguasa', 'mengumpulkan pengikut'], 'Manembah menjadi puncak ketundukan kepada Pencipta.', 'Disertai kesucian fisik dan psikis.'),
        ('Ketentuan dalam kepercayaan selalu berpasangan, yaitu…', 'yang boleh dan yang tidak boleh', ['yang mahal dan yang murah', 'yang lama dan yang baru', 'yang besar dan yang kecil'], 'Satu kewajiban dan satu larangan.', 'Keduanya saling melengkapi.'),
        ('Fungsi larangan menurut buku adalah…', 'memandu pelaksanaan kewajiban', ['membatasi kebebasan tanpa alasan', 'mengumpulkan denda', 'menambah aturan', ], 'Larangan memastikan syarat kewajiban terpenuhi.', 'Contohnya larangan saat berdoa.'),
        ('Salah satu larangan umum terkait martabat kemanusiaan adalah…', 'mencuri', ['berbagi makanan', 'menolong orang', 'memberi salam'], 'Larangan umum meliputi mencuri, berzina, dan membunuh.', 'Serta memfitnah dan menghina.'),
        ('Perbuatan yang melanggar rambu larangan disebut…', 'perbuatan tercela', ['perbuatan baik', 'perbuatan biasa', 'perbuatan netral'], 'Pelanggaran norma disebut perbuatan tercela.', 'Ganjarannya ketidakselamatan.'),
        ('Fungsi perintah dan larangan diibaratkan seperti…', 'rambu lalu lintas', ['pajak negara', 'iklan produk', 'jadwal pelajaran'], 'Tanpa rambu terjadi kekacauan dan kecelakaan.', 'Menjaga keselarasan kehidupan.'),
        ('Cara pertama menjauhi larangan adalah…', 'bersyukur dalam keadaan apa pun', ['mengeluh', 'menyalahkan orang lain', 'menunda kewajiban'], 'Bersyukur dilakukan sekalipun dalam duka.', 'Semua adalah kehendak Tuhan.'),
        ('Sikap berserah diri sepenuh hati berarti…', 'menempatkan hidup pada kehendak Tuhan', ['menyerah tanpa usaha', 'mengikuti keinginan sendiri', 'menghindari tanggung jawab'], 'Suka dan duka dikendalikan Tuhan.', 'Kesedihan jangan berlarut-larut.'),
        ('Mawas diri menurut buku adalah…', 'mengendapkan hawa nafsu dan mengendalikan diri', ['mencurigai orang lain', 'menahan semua perasaan', 'menghindari pergaulan'], 'Mawas diri mengendalikan hati, pikiran, ucapan, dan tindakan.', 'Berlaku bagi siapa pun.'),
        ('Ungkapan “semakin tinggi pohon semakin kencang angin menerpanya” mengingatkan…', 'semua orang sama-sama berperang melawan nafsu', ['pohon besar untuk ditebang', 'angin selalu kencang di gunung', 'orang tinggi lebih kuat', ], 'Orang kaya, terhormat, dan berilmu juga melawan nafsu.', 'Kedudukan tidak mengecualikan ujian.'),
        ('Larangan dalam doa dan ritual tertentu mencakup…', 'tidak saling bicara dan larangan tertentu bagi wanita haid atau baru melahirkan', ['membawa makanan', 'memakai pakaian', 'duduk di kursi', ], 'Ketentuan itu bagian kesucian ritual.', 'Sesuai adat masing-masing komunitas.'),
        ('Perbuatan yang sesuai norma kewajiban disebut…', 'perbuatan baik', ['perbuatan tercela', 'perbuatan biasa', 'perbuatan bebas'], 'Orang yang melakukannya disebut orang baik dan beradat.', 'Kebalikan dari perbuatan tercela.'),
    ],
    'multi': [
        ('Manakah kewajiban penghayat menurut buku?', ['Bekerja keras dalam kebenaran', 'Mencintai sesama', 'Memelihara alam'], ['Menambah harta pribadi', 'Menguasai orang lain'], 'Empat kewajiban berpusat pada kebenaran dan cinta.', 'Harta dan kekuasaan bukan kewajiban.'),
        ('Manakah larangan terkait martabat kemanusiaan?', ['Mencuri', 'Memfitnah', 'Mengurangi hak orang lain'], ['Berbagi makanan', 'Menolong orang sakit'], 'Larangan itu melindungi hak asasi hidup, harkat, dan moral.', 'Berbagi dan menolong adalah kebaikan.'),
        ('Manakah cara menjauhi larangan?', ['Bersyukur', 'Berserah diri sepenuh hati', 'Mawas diri'], ['Menunda kewajiban', 'Menyalahkan keadaan'], 'Tiga cara itu mendekatkan diri kepada Tuhan.', 'Menunda justru menjauhkan.'),
        ('Manakah dimensi hubungan kehidupan manusia?', ['Dengan Tuhan', 'Dengan sesama manusia', 'Dengan alam penghidupan'], ['Dengan media sosial', 'Dengan pasar modal'], 'Tiga dimensi hubungan mencakup ketuhanan, kemanusiaan, dan alam.', 'Media dan pasar bukan dimensi buku.'),
        ('Manakah contoh perbuatan baik?', ['Mengembalikan barang temuan', 'Menolong yang kesusahan', 'Menjaga kebersihan lingkungan'], ['Menipu demi keuntungan', 'Menghina orang lain'], 'Perbuatan baik sesuai norma kewajiban.', 'Menipu dan menghina tercela.'),
        ('Manakah larangan yang berkaitan dengan ritual?', ['Gerak-gerik liar saat berdoa', 'Pandangan tidak fokus', 'Suasana sekitar yang gaduh'], ['Membaca dengan tenang', 'Duduk dengan rapi'], 'Larangan ritual menjaga kesucian dan kekhusyukan.', 'Sikap tenang justru dianjurkan.'),
        ('Manakah pernyataan tentang manembah?', ['Puncak berkeyakinan', 'Bentuk sujud syukur', 'Mempersembahkan yang terbaik'], ['Cara mencari kekayaan', 'Acara hiburan massal'], 'Manembah adalah puncak ketundukan dengan puja-puji.', 'Bukan acara hiburan.'),
        ('Manakah sikap menghadapi penderitaan menurut buku?', ['Menerima sebagai pelajaran berharga', 'Bersyukur dan manembah', 'Menjadikannya penawar keangkuhan'], ['Menyalahkan Tuhan', 'Putus asa berlarut-larut'], 'Orang yang percaya belajar dari penderitaan.', 'Menyalahkan Tuhan menjauhkan dari jalan-Nya.'),
    ],
    'pairs': [
        ('Kewajiban', 'ketentuan yang harus ditunaikan'),
        ('Larangan', 'rambu hidup di jalan suci'),
        ('Tabu', 'pantangan dalam ritual'),
        ('Mawas diri', 'mengendalikan hati, pikiran, ucapan'),
        ('Mamayu hayuning bawana', 'memelihara alam'),
        ('Tenggang rasa', 'menghormati martabat sesama'),
        ('Pasahat Tondi', 'persembahan ritual Parmalim'),
        ('Perbuatan tercela', 'pelanggaran norma masyarakat'),
    ],
    'steps': [
        ('Urutkan empat kewajiban penghayat.', ['Kerja keras dalam kebenaran', 'Cinta sesama dan hormat pemimpin', 'Memelihara alam', 'Manembah dengan sujud syukur'], 'Kewajiban berjenjang menuju manembah sebagai puncak.', 'Manembah menuntut tiga kewajiban terdahulu.'),
        ('Urutkan cara menjauhi larangan.', ['Menyadari diri kecil di hadapan Tuhan', 'Bersyukur dalam keadaan apa pun', 'Berserah diri sepenuh hati', 'Mawas diri melawan nafsu', 'Menjalankan kewajiban dengan tulus'], 'Cara itu berawal dari kesadaran lalu kebiasaan.', 'Mawas diri menjadi inti.'),
        ('Urutkan terbentuknya larangan dalam kepercayaan.', ['Perintah Tuhan', 'Aturan norma kehidupan', 'Rambu larangan', 'Menjadi tradisi dan adat', 'Menjadi pedoman semua aspek hidup'], 'Larangan berakar dari perintah Tuhan lalu menjadi tradisi.', 'Tradisi menjaga keberlakuan larangan.'),
        ('Urutkan langkah memenuhi kewajiban kerja keras.', ['Belajar keras sejak awal', 'Bekerja keras menghidupi diri', 'Menghidupi keluarga', 'Menyisihkan hasil untuk kebajikan', 'Mencintai sesama lebih luas'], 'Kerja keras berawal dari belajar lalu berbuah kebajikan.', 'Hasil kerja dipakai berbagi.'),
        ('Urutkan sikap menghadapi suka dan duka.', ['Menerima kenyataan hidup', 'Tidak merayakan suka berlebihan', 'Tidak berlarut dalam sedih', 'Pasrah berserah kepada Tuhan', 'Mengambil pelajaran dari keduanya'], 'Suka dan duka dihadapi dengan keseimbangan dan syukur.', 'Pelajaran menutup sikap.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
