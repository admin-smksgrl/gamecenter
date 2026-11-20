"""KEP 2 — Menumbuhkan Budi Pekerti Luhur dalam Diri (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 2',
    'slug': 'kep-2-budi-pekerti-luhur',
    'title': 'Menumbuhkan Budi Pekerti Luhur dalam Diri',
    'description': (
        'Menghayati lima aspek budi pekerti pribadi—kedudukan, memandang, makan, '
        'berbicara, dan berjalan—serta menyeimbangkan kewajiban dan hak melalui '
        'kerja keras, ikhlas berbagi, dan berbakti.'
    ),
    'objectives': [
        'Menghayati sikap jujur mencintai kebenaran sesuai kehendak Tuhan Yang Maha Esa.',
        'Mengamalkan sikap bertanggung jawab terhadap kewajiban yang diemban serta santun, pemaaf, dan adi luhung.',
        'Mengomunikasikan manfaat budi luhur pribadi dalam interaksi dengan keluarga, teman, dan masyarakat.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 2 Menumbuhkan Budi Pekerti Luhur Dalam Diri; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Budi pekerti luhur', 'definition': 'Sikap moral dan kelakuan baik yang lahir dari kebenaran dan nilai kemanusiaan.'},
        {'term': 'Mawas diri', 'definition': 'Sikap meninjau dan menilai diri sendiri sebelum menilai orang lain.'},
        {'term': 'Hawa nafsu', 'definition': 'Dorongan keinginan diri yang cenderung mengarah pada keburukan bila dituruti.'},
        {'term': 'Kedudukan', 'definition': 'Posisi seseorang dalam lingkungan yang melekatkan kewajiban dan tanggung jawab.'},
        {'term': 'Kesantunan', 'definition': 'Sikap sopan dan menghargai orang lain melalui tutur kata serta perilaku.'},
        {'term': 'Integritas', 'definition': 'Kesesuaian antara pikiran, ucapan, dan tindakan dalam kebenaran.'},
        {'term': 'Proporsional', 'definition': 'Sesuai dengan bobot, porsi, dan tanggung jawab masing-masing.'},
        {'term': 'Kebajikan', 'definition': 'Perbuatan baik yang dilakukan dengan tulus tanpa pamrih.'},
    ],
    'intro': {
        'material_title': 'Apa itu budi pekerti luhur?',
        'title': 'Kejujuran sebagai dasar semua sikap',
        'paragraphs': [
            'Budi pekerti luhur berarti sikap moral dan kelakuan baik dalam menjalani kehidupan. Ia tampak pada orang yang tepat janji, sopan, bertutur lembut, menghargai orang lain, serta jujur, adil, dan terpercaya.',
            'Ciri pokok budi luhur di berbagai suku Nusantara adalah kejujuran, hati yang lurus, tulus, dan kebenaran. Sifat itu hadir dalam pikiran dan perasaan, ucapan, serta tampak pada tindakan.',
            'Kejujuran bukan sekadar tidak berbohong. Ia adalah kesesuaian pikiran, ucapan, dan tindakan dengan sifat lurus serta tulus hati, yang didorong oleh kuasa jalan kebenaran.',
        ],
        'diagram': (
            'Alur terjadinya perilaku berbudi luhur',
            'flowchart LR\n'
            '  A[Berpikir jujur] --> B[Berbicara benar]\n'
            '  B --> C[Bertindak benar]\n'
            '  C --> D[Kebiasaan budi luhur]\n'
            '  D --> E[Mendarah daging menjadi tabiat]\n'
            '  E --> A',
        ),
        'callout': 'Budi luhur tidak cukup dipelajari dari ucapan; ia dipelajari dengan melakukan kebajikan setiap hari.',
        'checkpoint': (
            'Alur terjadinya perilaku menurut buku adalah…',
            [
                ('berpikir – berbicara – bertindak', True),
                ('bertindak – berpikir – berbicara', False),
                ('berbicara – bertindak – berpikir', False),
                ('berpikir – bertindak – berbicara', False),
            ],
            'Perilaku berbudi luhur dimulai dari pikiran jujur, lalu ucapan, kemudian tindakan.',
        ),
    },
    'concept': {
        'material_title': 'Lima aspek budi pekerti pribadi',
        'title': 'Duduk, memandang, makan, berbicara, dan berjalan',
        'paragraphs': [
            'Aspek pertama, sikap duduk dan kedudukan benar: tahu diri dalam mengambil tempat, peran, dan bagian. Kedudukan yang tinggi justru memikul kewajiban serta tanggung jawab yang lebih besar, bukan menuntut hak yang lebih banyak.',
            'Aspek kedua, memandang dan dilihat: mata adalah jendela hidup, tetapi pandangan dapat tertipu nafsu. Peribahasa mengingatkan, “lalat di seberang terlihat jelas, gajah di depan mata tak terlihat”, karena nafsu meninggikan diri.',
            'Aspek ketiga, makan dan nafkah: kecukupan gizi, pantangan, dan puasa melatih mengekang selera. Aspek keempat, berbicara dan mendengar: santun berarti bersamaan dengan martabat dan penghargaan, terbiasa dengan kata tolong, maaf, dan terima kasih.',
            'Aspek kelima, berjalan dan berperilaku benar: bertindak dalam batas wajar menurut hukum, norma, dan aturan, tidak kurang dan tidak lebih dari kepatutan.',
        ],
        'table': [
            ['Aspek', 'Inti sikap', 'Contoh penerapan'],
            ['Duduk dan kedudukan', 'Tahu diri dan memikul kewajiban', 'Tidak mengambil bagian melebihi kepatutan'],
            ['Memandang dan dilihat', 'Menahan pandangan merendahkan', 'Tidak menilai orang dari penampilan'],
            ['Makan dan nafkah', 'Sederhana dan halal', 'Tidak boros, berbagi kepada yang lemah'],
            ['Berbicara dan mendengar', 'Santun, terbuka, cerdas mendengar', 'Meminta maaf dan berterima kasih'],
            ['Berjalan dan berperilaku', 'Taat asas dan batas wajar', 'Mematuhi aturan sekolah dan lalu lintas'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-2-aspek',
            'engine': 'mermaid',
            'title': 'Lima aspek budi pekerti pribadi',
            'code': 'flowchart LR\n'
                    '  A[Budi pekerti luhur] --> B[Duduk & kedudukan benar]\n'
                    '  A --> C[Memandang & dilihat benar]\n'
                    '  A --> D[Makan & nafkah benar]\n'
                    '  A --> E[Berbicara & mendengar benar]\n'
                    '  A --> F[Berjalan & berperilaku benar]\n'
                    '  F --> G[Landasan hidup berbudi luhur]',
        },
        'activity': categorize_block(
            'kep-2-klasifikasi',
            'Kelompokkan perilaku berikut sesuai atau tidak sesuai budi pekerti luhur.',
            [('b1', 'Sesuai budi luhur'), ('b2', 'Tidak sesuai')],
            [
                ('i1', 'Meminta maaf setelah berbuat salah', 'b1'),
                ('i2', 'Mendengarkan pendapat teman sampai selesai', 'b1'),
                ('i3', 'Berbagi bekal kepada teman yang tidak membawa', 'b1'),
                ('i4', 'Mengambil bagian lebih banyak tanpa memikul tugas', 'b2'),
                ('i5', 'Menertawakan kekurangan fisik teman', 'b2'),
                ('i6', 'Mencontek saat ulangan', 'b2'),
                ('i7', 'Mengembalikan uang kembalian yang berlebih', 'b1'),
                ('i8', 'Membuang makanan karena tidak suka', 'b2'),
            ],
            'Tepat. Perilaku budi luhur berpangkal pada kejujuran dan penghargaan kepada sesama.',
            'Periksa lagi: perilaku yang merugikan orang lain dan melanggar kejujuran tidak sesuai budi luhur.',
        ),
        'subtitle': 'Keseimbangan kewajiban dan hak',
        'list': [
            'Kedudukan setiap orang sama di depan hukum, tetapi pembagian hak dan kewajiban bersifat proporsional sesuai bobot tanggung jawab.',
            'Keseimbangan itu ibarat dua sisi dacing: memikul kewajiban dengan tulus membuat sisi hak tidak menjungkal ke atas.',
            'Budi luhur menuntun kehati-hatian serta menahan diri terhadap wewenang dan hak, dengan mengutamakan kebenaran.',
            'Wujudnya: rendah hati sambil menjaga martabat, mengejar kualitas sambil introspeksi, berprestasi sambil ikhlas berbagi.',
        ],
        'checkpoint': (
            'Menurut buku, kedudukan yang tinggi berarti…',
            [
                ('memikul kewajiban dan tanggung jawab yang besar', True),
                ('berhak memperoleh bagian paling banyak', False),
                ('bebas dari aturan yang berlaku', False),
                ('tidak perlu memberi contoh', False),
            ],
            'Kedudukan tinggi adalah amanah untuk memikul tugas yang lebih besar.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Kerja keras, ikhlas berbagi, dan berbakti',
        'paragraphs': [
            'Tuhan menyediakan alam sebagai sumber penghidupan dan menganugerahkan akal budi. Bekerja keras adalah sikap untuk menghidupi diri secara mandiri sekaligus membekali diri mewujudkan budi luhur.',
            'Penghidupan apa pun bentuknya adalah karunia yang diperoleh melalui kerja keras. Cara bersyukur atasnya adalah berbagi kepada yang lemah: hemat, menabung, menyumbang korban bencana, dan menolong teman yang kesusahan.',
            'Berbakti tampak pada kepatuhan dan upaya meringankan beban orang tua, termasuk saat mereka sakit atau menua. Berbakti juga diberikan kepada guru, pembimbing rohani, dan pemimpin yang baik, serta diwujudkan lewat gotong royong di lingkungan.',
        ],
        'scenario': scenario(
            'kep-2-skenario',
            'Uang kembalian yang berlebih',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu menerima uang kembalian Rp10.000 lebih dari seharusnya. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Mengembalikan kelebihan itu kepada penjual', 'next': 'n2', 'score': 2, 'feedback': 'Mengembalikan hak orang lain adalah wujud kejujuran.'},
                        {'text': 'Menyimpannya karena penjual tidak sadar', 'next': 'n3', 'score': 0, 'feedback': 'Mengambil yang bukan hak termasuk perbuatan tercela.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Temanmu mengejek, “Ah, cuma sepuluh ribu.” Bagaimana sikapmu?',
                    'choices': [
                        {'text': 'Menjelaskan bahwa jumlah kecil tetap soal kejujuran', 'next': 'n4', 'score': 2, 'feedback': 'Kejujuran tidak diukur dari besar kecilnya nilai.'},
                        {'text': 'Ikut menertawakan diri karena dianggap bodoh', 'next': 'n3', 'score': 0, 'feedback': 'Menyerah pada ejekan melemahkan integritas.'},
                    ],
                },
                {'id': 'n3', 'text': 'Kebiasaan mengambil yang bukan hak menjadi bibit ketidakpercayaan.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kamu dipercaya karena konsisten jujur dalam hal kecil.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan lima aspek budi pekerti pribadi.', 'back': 'Kedudukan, memandang, makan, berbicara, dan berjalan benar.'},
            {'front': 'Apa makna dacing dalam bab ini?', 'back': 'Keseimbangan proporsional antara kewajiban dan hak.'},
            {'front': 'Bagaimana cara bersyukur atas penghidupan?', 'back': 'Berbagi kepada yang lemah dan bekerja keras.'},
            {'front': 'Mengapa pandangan bisa menipu?', 'back': 'Karena nafsu meninggikan diri dan merendahkan orang lain.'},
        ],
        'checkpoint': (
            'Tiga kata yang dibiasakan dalam berbicara santun adalah…',
            [
                ('tolong, maaf, terima kasih', True),
                ('cepat, singkat, tegas', False),
                ('keras, lantang, panjang', False),
                ('diam, diam, diam', False),
            ],
            'Kesantunan dibangun dari kebiasaan meminta tolong, memohon maaf, dan berterima kasih.',
        ),
        'challenge': challenge_block(
            'kep-2-tantangan',
            'Tantangan istilah budi pekerti',
            90,
            [
                ('Perilaku baik yang tulus tanpa pamrih', 'Kebajikan'),
                ('Menilai diri sebelum menilai orang', 'Mawas diri'),
                ('Kesesuaian pikiran, ucapan, tindakan', 'Integritas'),
                ('Dorongan diri yang cenderung buruk', 'Hawa nafsu'),
                ('Sesuai bobot dan tanggung jawab', 'Proporsional'),
            ],
            'Lima istilah budi pekerti terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Budi pekerti luhur berarti…', 'sikap moral dan kelakuan baik dalam menjalani kehidupan', ['kemampuan menghafal ajaran', 'kekayaan harta benda', 'kekuasaan atas orang lain'], 'Budi pekerti luhur adalah sikap moral dan kelakuan baik.', 'Lahir dari kebenaran dan nilai kemanusiaan.'),
        ('Kunci semua sikap berbudi pekerti luhur adalah…', 'kejujuran', ['kepandaian', 'kekayaan', 'kekuatan'], 'Kejujuran menjadi dasar seluruh sikap budi luhur.', 'Mengalah untuk mengendalikan nafsu.'),
        ('Alur perilaku berbudi luhur menurut buku adalah…', 'berpikir – berbicara – bertindak', ['bertindak – berpikir – berbicara', 'berbicara – berpikir – bertindak', 'berpikir – bertindak – berbicara'], 'Perilaku dimulai dari pikiran, lalu ucapan, lalu tindakan.', 'Semua dilandasi kejujuran.'),
        ('Sikap duduk yang benar juga mencakup…', 'mengenali kedudukan diri dalam lingkungan', ['memilih kursi paling depan', 'duduk paling lama', 'duduk tanpa bicara'], 'Kedudukan menentukan tugas dan tanggung jawab.', 'Ada tata krama pergaulan.'),
        ('Menurut buku, kedudukan yang tinggi adalah untuk…', 'memikul kewajiban dan tanggung jawab yang besar', ['memperoleh hak paling banyak', 'mendapat pujian', 'bebas dari tugas'], 'Kedudukan tinggi berarti amanah yang lebih berat.', 'Bukan untuk menuntut hak lebih.'),
        ('Peribahasa “lalat di seberang terlihat jelas, gajah di depan mata tak terlihat” menggambarkan…', 'nafsu meninggikan diri', ['ketajaman penglihatan', 'keindahan alam', 'kepandaian berburu'], 'Nafsu membuat orang jeli pada kesalahan orang lain.', 'Sekaligus buta pada kekurangan sendiri.'),
        ('Mata disebut sebagai…', 'jendela hidup', ['cermin hati', 'pintu rezeki', 'sumber tenaga'], 'Mata adalah jendela hidup kita.', 'Melalui mata kita memandang dan dilihat.'),
        ('Puasa dan pantangan makanan dalam ajaran kepercayaan bertujuan…', 'melatih mengekang hawa nafsu', ['menambah berat badan', 'menghemat biaya', 'menghindari pekerjaan'], 'Pantangan dan puasa melatih diri mengekang selera.', 'Termasuk menahan lapar dan dahaga.'),
        ('Peribahasa “manis jangan keburu ditelan, pahit jangan keburu dimuntahkan” mengajarkan…', 'menahan diri terhadap selera', ['memilih makanan manis', 'menolak obat pahit', 'makan dengan cepat'], 'Nasihat itu tentang mengendalikan selera.', 'Sakit pun obat tetap diminum.'),
        ('Tiga kata yang dibiasakan dalam berbicara santun adalah…', 'tolong, maaf, terima kasih', ['cepat, tepat, hemat', 'keras, tegas, lantang', 'diam, dengar, diam'], 'Kesantunan dibangun dari tiga kata itu.', 'Berlaku untuk hal kecil sekalipun.'),
        ('Aspek kelima budi pekerti pribadi adalah…', 'berjalan dan berperilaku benar', ['berbicara dengan lantang', 'mengumpulkan harta', 'menghafal ajaran'], 'Aspek kelima adalah berjalan dengan tindakan benar.', 'Merupakan puncak belajar budi pekerti pribadi.'),
        ('Keseimbangan kewajiban dan hak diibaratkan…', 'dua sisi dacing', ['satu roda berputar', 'tiang bendera', 'anak panah'], 'Kewajiban dan hak seperti dua sisi timbangan.', 'Bila satu sisi berat, sisi lain menjungkal.'),
        ('Menurut buku, hak dan kewajiban bersifat…', 'proporsional', ['sama rata untuk semua', 'berdasarkan usia saja', 'berdasarkan kekayaan'], 'Pembagiannya proporsional sesuai bobot tanggung jawab.', 'Orang dewasa memikul tugas lebih besar.'),
        ('Wujud bersyukur atas penghidupan menurut buku adalah…', 'berbagi kepada yang lemah', ['menyimpan semua hasil', 'menambah harta', 'membandingkan dengan orang lain'], 'Cara bersyukur adalah berbagi kepada yang lemah.', 'Termasuk menolong teman yang kesusahan.'),
    ],
    'multi': [
        ('Manakah aspek budi pekerti pribadi menurut buku?', ['Duduk dan kedudukan', 'Memandang dan dilihat', 'Makan dan nafkah'], ['Menimbun harta', 'Mencari pujian'], 'Lima aspeknya: kedudukan, memandang, makan, berbicara, berjalan.', 'Harta dan pujian bukan aspek budi pekerti.'),
        ('Manakah ciri pokok budi luhur di suku Nusantara?', ['Kejujuran', 'Hati yang lurus', 'Tulus'], ['Kekayaan', 'Kekuasaan'], 'Ciri pokoknya kejujuran, hati lurus, tulus, dan kebenaran.', 'Kekayaan tidak menjadi ukuran.'),
        ('Manakah wujud kerja keras dan ikhlas berbagi?', ['Rajin belajar', 'Hemat dan menabung', 'Menolong teman yang kesusahan'], ['Menghindari tugas', 'Memboroskan uang'], 'Kerja keras disertai kepedulian kepada sesama.', 'Pemborosan bertentangan dengan ajaran.'),
        ('Manakah sikap berbakti menurut buku?', ['Mematuhi orang tua', 'Meringankan beban orang tua', 'Menghormati guru'], ['Membiarkan orang tua bekerja sendiri', 'Mengabaikan nasihat guru'], 'Bakti tampak pada kepatuhan dan upaya meringankan beban.', 'Berlaku juga kepada guru dan pembimbing.'),
        ('Manakah perilaku berbicara yang santun?', ['Mengucapkan terima kasih', 'Meminta maaf bila salah', 'Mendengarkan dengan sungguh-sungguh'], ['Menyela pembicaraan orang', 'Membentak teman'], 'Santun berarti berbicara bermartabat dan menghargai.', 'Menyela dan membentak tidak santun.'),
        ('Manakah contoh gotong royong di lingkungan?', ['Membantu korban bencana', 'Menjadi panitia hari kemerdekaan', 'Mengikuti kerja bakti'], ['Menonton dari rumah', 'Menyebar berita bohong'], 'Gotong royong diwujudkan dengan hadir dan aktif.', 'Kehadiran menjadi kuncinya.'),
        ('Manakah tanda orang mengenal dan mengendalikan diri?', ['Mengenali baik dan buruk pada diri', 'Membiasakan perbuatan baik', 'Menerima kebenaran dengan tekad kuat'], ['Selalu membenarkan diri', 'Menutup hati dari nasihat'], 'Pengendalian diri dilatih dengan kesadaran dan pembiasaan.', 'Membenarkan diri justru melemahkan.'),
        ('Manakah manfaat budi luhur pribadi dalam pergaulan?', ['Mudah dipercaya', 'Menjaga kerukunan', 'Menjadi teladan'], ['Menimbulkan permusuhan', 'Membuat orang menjauh'], 'Budi luhur membangun kepercayaan dan kerukunan.', 'Permusuhan lahir dari perilaku tercela.'),
    ],
    'pairs': [
        ('Budi pekerti luhur', 'sikap moral dan kelakuan baik'),
        ('Mawas diri', 'menilai diri sendiri'),
        ('Hawa nafsu', 'dorongan diri yang cenderung buruk'),
        ('Proporsional', 'sesuai bobot tanggung jawab'),
        ('Kebajikan', 'perbuatan baik tanpa pamrih'),
        ('Integritas', 'kesesuaian pikiran, ucapan, tindakan'),
        ('Kesantunan', 'sopan dan menghargai orang lain'),
        ('Dacing', 'ibarat keseimbangan kewajiban dan hak'),
    ],
    'steps': [
        ('Urutkan alur perilaku berbudi luhur.', ['Berpikir jujur', 'Berbicara benar', 'Bertindak benar', 'Membiasakan kebajikan', 'Menjadi tabiat'], 'Perilaku dimulai dari pikiran sampai menjadi kebiasaan.', 'Kebiasaan membentuk tabiat.'),
        ('Urutkan lima aspek budi pekerti pribadi sesuai buku.', ['Sikap duduk dan kedudukan', 'Memandang dan dilihat', 'Makan dan nafkah', 'Berbicara dan mendengar', 'Berjalan dan berperilaku'], 'Urutan aspek mengikuti pembahasan bab.', 'Berjalan benar menjadi aspek kelima.'),
        ('Urutkan langkah mengendalikan nafsu diri.', ['Mengenali diri sebenar-benarnya', 'Menyadari baik dan buruk', 'Membiasakan meneladani perbuatan baik', 'Memohon pencerahan Tuhan', 'Menjalankan ajaran dengan tekad kuat'], 'Pengendalian diri dimulai dari kesadaran lalu pembiasaan.', 'Doa menyertai usaha.'),
        ('Urutkan wujud keseimbangan kewajiban dan hak.', ['Memahami kedudukan diri', 'Mengetahui kewajiban yang melekat', 'Memikul tugas dengan tulus', 'Menahan diri terhadap hak berlebih', 'Bertindak adil kepada sesama'], 'Keseimbangan dimulai dari pemahaman kedudukan sampai keadilan tindakan.', 'Menahan diri menjadi kuncinya.'),
        ('Urutkan langkah membiasakan kebajikan harian.', ['Menetapkan niat berbuat baik', 'Memilih kebajikan yang bisa dilakukan', 'Melakukan setiap hari', 'Mencatat capaian perilaku', 'Meninjau dan memperbaiki diri'], 'Kebajikan dibiasakan lewat niat, tindakan, dan peninjauan.', 'Pencatatan membantu perbaikan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
