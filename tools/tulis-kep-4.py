"""KEP 4 — Keagungan Tuhan Yang Maha Esa (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 4',
    'slug': 'kep-4-keagungan-tuhan',
    'title': 'Keagungan Tuhan Yang Maha Esa',
    'description': (
        'Menganalisis keberadaan dan sifat Tuhan melalui akal serta ajaran '
        'kepercayaan, memahami Tuhan sebagai Pencipta alam dan manusia, serta '
        'menata empat hubungan kewajiban manusia.'
    ),
    'objectives': [
        'Menghayati dan mengamalkan ajaran Kepercayaan terhadap Tuhan Yang Maha Esa.',
        'Menghayati serta mengamalkan sikap toleransi dan kepedulian antarsesama.',
        'Menganalisis konsep Tuhan dan menyembah dalam beragam kepercayaan.',
        'Menyajikan manfaat sikap toleransi dalam keluarga, masyarakat, berbangsa, dan keragaman global.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 4 Keagungan Tuhan Yang Maha Esa; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Causa prima', 'definition': 'Sebab pertama dari segala sebab, yaitu Tuhan Yang Maha Kuasa.'},
        {'term': 'Adi-kodrati', 'definition': 'Sifat yang melampaui kodrat alam, kekal, dan tak berwujud.'},
        {'term': 'Roh', 'definition': 'Zat hidup pemberian Tuhan yang bersifat antara ada dan tiada.'},
        {'term': 'Akal budi', 'definition': 'Karunia Tuhan berupa hati dan pikiran yang mengendalikan kehendak serta perilaku.'},
        {'term': 'Cipta, Karsa, Rasa', 'definition': 'Tiga eksistensi manusia menurut kepercayaan Jawa: pikiran, kehendak, dan perasaan.'},
        {'term': 'Tetralogi kewajiban', 'definition': 'Empat hubungan kewajiban manusia: dengan Tuhan, sesama, alam, dan diri sendiri.'},
        {'term': 'Eko-spiritual', 'definition': 'Sikap spiritual dalam menjaga hubungan dengan lingkungan alam.'},
        {'term': 'Toleransi', 'definition': 'Sikap menghargai perbedaan keyakinan dan cara beribadah orang lain.'},
    ],
    'intro': {
        'material_title': 'Bagaimana manusia mengenal Tuhan?',
        'title': 'Tuhan itu ada',
        'paragraphs': [
            'Manusia sangat terbatas ketika hendak menjelaskan keberadaan Tuhan. Kita tidak dapat menggambarkan sosok, rupa, atau bentuk-Nya, sebagaimana kita tahu ada perasaan dan pikiran orang lain meski tak melihat wujudnya.',
            'Tuhan berada jauh di tempat yang maha tinggi dan maha rahasia, tetapi juga dekat: hadir dalam hati orang yang sungguh-sungguh meyakini-Nya. Tuhan adalah Sang Pencipta, awal dari segala yang wujud maupun tidak wujud.',
            'Keberadaan Tuhan dapat dipahami lewat akal sehat: rasa ingin tahu akan asal-usul segala yang ada, keteraturan alam, hukum sebab akibat yang berujung pada causa prima, serta kode genetik yang bekerja seperti program dalam sel makhluk hidup.',
        ],
        'diagram': (
            'Empat hubungan kewajiban manusia',
            'flowchart TB\n'
            '  A[Diri pribadi] --> B[Hubungan dengan Tuhan: laku menyembah]\n'
            '  A --> C[Hubungan dengan sesama manusia: laku sosial]\n'
            '  A --> D[Hubungan dengan alam: laku eko-spiritual]\n'
            '  A --> E[Hubungan dengan diri sendiri: komunikasi batin]\n'
            '  C --> F[Kesetaraan sesama ciptaan]\n'
            '  D --> F',
        ),
        'callout': 'Esensi kepercayaan adalah keyakinan dan berserah diri, bukan pada ritus yang tampak seperti sesaji atau doa semata.',
        'checkpoint': (
            'Sebab pertama dari segala sebab dalam buku disebut…',
            [
                ('causa prima', True),
                ('causa materialis', False),
                ('efek domino', False),
                ('hukum bioproses', False),
            ],
            'Causa prima adalah kuasa pertama yang lebih awal daripada alam semesta, yaitu Tuhan.',
        ),
    },
    'concept': {
        'material_title': 'Tuhan Pencipta alam dan manusia',
        'title': 'Sifat, kuasa, dan ciptaan',
        'paragraphs': [
            'Tuhan ada dan terdahulu, bersifat mutlak serta abadi. Manusia hanya tahu bahwa Tuhan maha rahasia; sedikit pengetahuan yang kita miliki pun merupakan karunia-Nya.',
            'Alam semesta diciptakan bersama hukum alamnya: kekuatan atau daya, gerakan, dan perubahan. Segala yang berubah itu berbeda dari Sang Pencipta yang kekal.',
            'Makhluk hidup bergantung pada alam namun diberi kemampuan meneruskan kehidupan. Sifat hidup tersimpan dalam DNA dan RNA, lalu virus, bakteri, alga, dan sel hidup mendahului bentuk hewan serta tumbuhan melalui bioproses.',
            'Manusia terikat tiga hukum alam: hukum alam yang berubah, hukum bioproses, dan hukum hidup yang sifatnya ada tetapi tiada. Konsep manusia Jawa menyebut Cipta, Karsa, dan Rasa; konsep Batak menekankan roh atau nyawa, akal budi, rasa, dan tubuh.',
        ],
        'table': [
            ['Aspek', 'Penjelasan', 'Kaitan dengan keagungan Tuhan'],
            ['Sifat Tuhan', 'Mutlak, abadi, maha rahasia', 'Manusia tidak mampu menyibak keberadaan-Nya'],
            ['Hukum alam', 'Daya, gerakan, perubahan', 'Keteraturan menunjukkan adanya Pemelihara'],
            ['Makhluk hidup', 'DNA dan RNA menyimpan sifat hidup', 'Kode genetik diibaratkan ketetapan Tuhan'],
            ['Manusia', 'Tubuh, roh, dan akal budi', 'Roh menjadi penghubung kehendak Tuhan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-4-struktur',
            'engine': 'mermaid',
            'title': 'Struktur manusia menurut kepercayaan Nusantara',
            'code': 'flowchart TB\n'
                    '  A[Manusia] --> B[Bagian tak berwujud: jiwa dan roh]\n'
                    '  A --> C[Bagian berwujud: tubuh dari unsur alam]\n'
                    '  B --> D[Zat hidup pemberian Tuhan]\n'
                    '  A --> E[Akal budi: hati dan pikiran]\n'
                    '  E --> F[Kehendak]\n'
                    '  E --> G[Perbuatan]\n'
                    '  D --> H[Kembali kepada Pemberi hidup]',
        },
        'activity': categorize_block(
            'kep-4-klasifikasi',
            'Kelompokkan unsur berikut sebagai bagian tak berwujud atau bagian berwujud pada manusia.',
            [('b1', 'Tak berwujud (adi-kodrati)'), ('b2', 'Berwujud (fisik)')],
            [
                ('i1', 'Roh atau nyawa', 'b1'),
                ('i2', 'Zat hidup pemberian Tuhan', 'b1'),
                ('i3', 'Hati dan pikiran', 'b1'),
                ('i4', 'Kehendak dan rasa', 'b1'),
                ('i5', 'Tubuh dari unsur tanah', 'b2'),
                ('i6', 'Air dan udara penyusun tubuh', 'b2'),
                ('i7', 'Api atau panas tubuh', 'b2'),
                ('i8', 'Jasad yang dapat diraba', 'b2'),
            ],
            'Tepat. Bagian adi-kodrati bersifat kekal, sedangkan tubuh berasal dari unsur alam yang berubah.',
            'Periksa lagi: unsur tanah, air, udara, dan api menyusun tubuh yang berubah.',
        ),
        'subtitle': 'Mengenal karunia Tuhan',
        'list': [
            'Tuhan menciptakan manusia berbeda dari ciptaan lain dan memberi hidup berdimensi roh.',
            'Manusia dikaruniai akal budi yang lebih tinggi daripada kesadaran hewan, serta hati dan rasa.',
            'Manusia hidup sebagai makhluk sosial bersama manusia lain, tumbuhan, hewan, dan jasad renik.',
            'Kecerdasan spiritual membawa manusia memahami sebagian rahasia Tuhan yang tidak mudah dijelaskan logika tampak.',
        ],
        'checkpoint': (
            'Tiga eksistensi manusia menurut kepercayaan Jawa adalah…',
            [
                ('Cipta, Karsa, Rasa', True),
                ('Budi, Kersa, Satya', False),
                ('Karya, Daya, Raga', False),
                ('Akal, Hati, Raga', False),
            ],
            'Cipta (pikiran), Karsa (kehendak), dan Rasa (perasaan) adalah eksistensi manusia dalam kepercayaan Jawa.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menyembah melalui hidup berbudi luhur',
        'paragraphs': [
            'Penghayat memaknai kepercayaan sebagai hubungan antara yang dicipta dan Sang Pencipta. Kewajiban menyembah dan memuliakan Tuhan diwujudkan melalui hidup berbudi pekerti luhur yang diwariskan kepada generasi berikutnya.',
            'Tuhan memelihara setiap kaum dan memberi pencerahan melalui sosok bijaksana, tanpa ada yang terlewat. Karena semua adalah milik Tuhan, manusia berakal sehat memahami kesetaraan sesama ciptaan di hadapan-Nya.',
            'Pengamalan budi luhur mengikuti tangga bertingkat: rumah tangga, lingkup sosial budaya bersama sesama dan alam, lalu lingkup pengamalan spiritual kepada Tuhan. Dari situlah tumbuh sikap toleran dan peduli.',
        ],
        'scenario': scenario(
            'kep-4-skenario',
            'Teman bertanya tentang cara menyembah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Temanmu bertanya, “Apakah kamu menyembah matahari atau batu?” Bagaimana jawabanmu?',
                    'choices': [
                        {'text': 'Menyembah Tuhan Yang Maha Esa; alam hanya ciptaan-Nya', 'next': 'n2', 'score': 2, 'feedback': 'Jawaban itu tepat: alam adalah ciptaan, bukan yang disembah.'},
                        {'text': 'Membiarkan saja karena ia tak akan paham', 'next': 'n3', 'score': 0, 'feedback': 'Membiarkan salah paham membuat prasangka berlanjut.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Ia bertanya lagi, “Mengapa ritualmu memakai sesaji?” Bagaimana menjelaskannya?',
                    'choices': [
                        {'text': 'Sesaji bagian budaya penghormatan; esensi iman ada di hati', 'next': 'n4', 'score': 2, 'feedback': 'Penjelasan memisahkan esensi keimanan dari ungkapan budaya.'},
                        {'text': 'Mengatakan sesaji yang menyelamatkan manusia', 'next': 'n3', 'score': 0, 'feedback': 'Itu keliru; keselamatan bersumber dari Tuhan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Salah paham tumbuh menjadi prasangka terhadap penghayat.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Teman memahami dan menghargai cara beribadah yang berbeda.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu causa prima?', 'back': 'Sebab pertama dari segala sebab, yaitu Tuhan Yang Maha Kuasa.'},
            {'front': 'Sebutkan tiga hukum alam yang mengikat manusia.', 'back': 'Hukum alam berubah, hukum bioproses, dan hukum hidup yang ada-tiada.'},
            {'front': 'Apa empat hubungan kewajiban manusia?', 'back': 'Dengan Tuhan, sesama, alam, dan diri sendiri.'},
            {'front': 'Mengapa manusia tidak dapat menggambarkan Tuhan?', 'back': 'Karena keterbatasan manusia; Tuhan maha rahasia.'},
        ],
        'checkpoint': (
            'Kewajiban menyembah Tuhan menurut buku diwujudkan melalui…',
            [
                ('hidup berbudi pekerti luhur', True),
                ('memberi sesaji sebanyak mungkin', False),
                ('menghafal mantra', False),
                ('menjauhi pergaulan', False),
            ],
            'Penyembahan diwujudkan melalui hidup berbudi luhur yang diwariskan kepada generasi berikutnya.',
        ),
        'challenge': challenge_block(
            'kep-4-tantangan',
            'Tantangan istilah keagungan Tuhan',
            90,
            [
                ('Sebab pertama segala sebab', 'Causa prima'),
                ('Sifat melampaui kodrat alam', 'Adi-kodrati'),
                ('Eksistensi manusia Jawa', 'Cipta Karsa Rasa'),
                ('Empat hubungan kewajiban', 'Tetralogi kewajiban'),
                ('Sikap spiritual pada alam', 'Eko-spiritual'),
            ],
            'Lima istilah keagungan Tuhan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Menurut buku, Tuhan berada…', 'jauh di tempat maha tinggi sekaligus dekat dalam hati yang meyakini', ['hanya di tempat ibadah', 'hanya di langit', 'hanya dalam kitab'], 'Tuhan maha tinggi dan maha rahasia, tetapi dekat bagi yang meyakini.', 'Kedekatan itu dirasakan dalam hati.'),
        ('Sebab pertama dari segala sebab disebut…', 'causa prima', ['causa materialis', 'hukum alam', 'bioproses'], 'Causa prima adalah kuasa pertama, yaitu Tuhan.', 'Lebih awal daripada alam semesta.'),
        ('Salah satu bukti keberadaan Tuhan melalui akal sehat adalah…', 'keteraturan alam semesta', ['banyaknya bencana', 'perbedaan bahasa', 'kemajuan teknologi'], 'Keteraturan peredaran benda langit menunjukkan adanya Pemelihara.', 'Hukum sebab akibat berpangkal pada causa prima.'),
        ('Kode genetik dalam sel diibaratkan sebagai…', 'ketetapan Tuhan', ['kesalahan alam', 'hasil kebetulan', 'ciptaan manusia'], 'Kode sandi gen bekerja seperti program dan dianggap ketetapan Tuhan.', 'Terdiri dari empat senyawa khas.'),
        ('Tiga hukum alam yang mengikat manusia adalah…', 'hukum alam berubah, bioproses, dan hidup ada-tiada', ['hukum adat, pidana, perdata', 'hukum fisika, kimia, biologi', 'hukum karma, dosa, pahala'], 'Manusia terikat tiga hukum alam menurut buku.', 'Ketiganya berbeda sifat.'),
        ('Sifat Tuhan menurut buku adalah…', 'mutlak dan abadi', ['berubah-ubah', 'terbatas', 'sementara'], 'Tuhan bersifat mutlak dan abadi, berbeda dari ciptaan yang berubah.', 'Tiada yang menyamai-Nya.'),
        ('Menurut kepercayaan Jawa, manusia memiliki eksistensi…', 'Cipta, Karsa, dan Rasa', ['roh, nyawa, dan tubuh', 'akal, hati, dan nafas', 'tubuh, harta, dan tahta'], 'Cipta, Karsa, dan Rasa merupakan eksistensi manusia Jawa.', 'Ketiganya interaksi unsur fisik dan nonfisik.'),
        ('Bagian manusia yang bersifat kekal dan tak berwujud disebut…', 'adi-kodrati', ['biologis', 'fisik', 'material'], 'Bagian jiwa bersifat adi-kodrati dan kekal.', 'Tubuh bersifat berubah.'),
        ('Empat hubungan kewajiban manusia meliputi hubungan dengan…', 'Tuhan, sesama manusia, alam, dan diri sendiri', ['Tuhan, harta, tahta, keluarga', 'alam, hewan, tumbuhan, benda', 'guru, teman, tetangga, kerabat'], 'Tetralogi kewajiban mencakup empat hubungan.', 'Hubungan keempat berupa komunikasi batin.'),
        ('Menurut buku, semua ciptaan Tuhan memiliki kedudukan…', 'setara di hadapan Penciptanya', ['bertingkat menurut kekayaan', 'berbeda menurut suku', 'sama persis dalam wujud'], 'Kesetaraan sesama ciptaan lahir dari kesadaran bahwa semua milik Tuhan.', 'Tidak ada yang lebih mulia karena harta.'),
        ('Esensi kepercayaan menurut Samad adalah…', 'taraf kepercayaan dan berserah diri pada kuasa Tuhan', ['banyaknya sesaji', 'panjangnya doa', 'besarnya persembahan'], 'Esensi kepercayaan bukan pada ritus yang tampak.', 'Keyakinan bersifat batiniah.'),
        ('Pater W. Schmidt menyatakan bahwa Tuhan Yang Maha Tinggi…', 'telah ada sebelum penyembahan dan magisme', ['baru dikenal setelah tulisan', 'diciptakan manusia', 'hanya dikenal bangsa modern'], 'Konsepsi Satu Tuhan ada pada orang pra-aksara.', 'Mendahului teori evolusi keagamaan.'),
        ('Tangga pengamalan budi luhur dimulai dari…', 'rumah tangga', ['lingkup global', 'organisasi', 'pemerintahan'], 'Pengamalan dimulai dari rumah tangga, lalu sosial budaya, lalu spiritual.', 'Rumah menjadi dasar.'),
        ('Kemampuan memahami sebagian rahasia Tuhan disebut…', 'kecerdasan spiritual', ['kecerdasan buatan', 'kecerdasan kinestetik', 'kecerdasan linguistik'], 'Kecerdasan spiritual bersifat rohaniah.', 'Tidak mudah dijelaskan logika tampak.'),
    ],
    'multi': [
        ('Manakah argumen akal sehat tentang keberadaan Tuhan?', ['Rasa ingin tahu asal-usul segala yang ada', 'Keteraturan alam semesta', 'Hukum sebab akibat berpangkal pada causa prima'], ['Banyaknya mitos', 'Kebetulan semata'], 'Buku menyebut empat argumen berbasis akal sehat.', 'Kebetulan bukan argumen buku.'),
        ('Manakah unsur yang menyusun tubuh manusia?', ['Tanah', 'Air', 'Udara'], ['Roh', 'Akal budi'], 'Tubuh tersusun dari unsur alam: tanah, air, udara, api.', 'Roh dan akal budi bukan unsur fisik.'),
        ('Manakah karunia Tuhan kepada manusia?', ['Hidup berdimensi roh', 'Akal budi', 'Hati dan rasa'], ['Kekayaan mutlak', 'Kekuasaan tanpa batas'], 'Karunia itu berupa hidup, akal budi, hati, dan rasa.', 'Kekayaan bukan karunia yang disebut.'),
        ('Manakah ciptaan Tuhan yang disebut buku?', ['Matahari dan bintang', 'Virus dan bakteri', 'Tumbuhan dan hewan'], ['Robot buatan manusia', 'Aplikasi digital'], 'Alam dan makhluk hidup adalah ciptaan Tuhan.', 'Robot dan aplikasi buatan manusia.'),
        ('Manakah wujud laku menyembah menurut buku?', ['Hidup berbudi pekerti luhur', 'Berserah diri kepada Tuhan', 'Bersyukur atas karunia'], ['Menghina keyakinan lain', 'Memaksa orang beribadah'], 'Penyembahan diwujudkan dalam budi luhur dan syukur.', 'Memaksa melanggar toleransi.'),
        ('Manakah sikap toleransi beragama?', ['Menghargai cara ibadah orang lain', 'Tidak mencela keyakinan berbeda', 'Menjaga kerukunan'], ['Memaksa orang pindah keyakinan', 'Menghina ritual orang lain'], 'Toleransi menjaga kerukunan tanpa memaksa.', 'Memaksa bertentangan dengan hak beragama.'),
        ('Manakah hukum yang mengikat manusia menurut buku?', ['Hukum alam yang berubah', 'Hukum bioproses', 'Hukum hidup ada-tiada'], ['Hukum dagang', 'Hukum waris'], 'Tiga hukum alam itu mengikat manusia.', 'Hukum dagang dan waris buatan manusia.'),
        ('Manakah yang termasuk sikap eko-spiritual?', ['Memelihara tanaman', 'Menjaga kebersihan sungai', 'Menghemat air'], ['Membuang sampah sembarangan', 'Menebang hutan tanpa aturan'], 'Eko-spiritual menjaga hubungan dengan alam ciptaan Tuhan.', 'Perusakan alam bertentangan dengannya.'),
    ],
    'pairs': [
        ('Causa prima', 'sebab pertama segala sebab'),
        ('Adi-kodrati', 'kekal dan tak berwujud'),
        ('Roh', 'zat hidup pemberian Tuhan'),
        ('Akal budi', 'hati dan pikiran dari Tuhan'),
        ('Cipta', 'pikiran dalam konsep Jawa'),
        ('Karsa', 'kehendak dalam konsep Jawa'),
        ('Rasa', 'perasaan dalam konsep Jawa'),
        ('Tetralogi kewajiban', 'empat hubungan kewajiban manusia'),
    ],
    'steps': [
        ('Urutkan argumen akal tentang keberadaan Tuhan.', ['Rasa ingin tahu asal-usul', 'Keteraturan alam semesta', 'Hukum sebab akibat', 'Causa prima', 'Keyakinan akan Sang Pencipta'], 'Argumen bergerak dari pertanyaan asal sampai kesimpulan adanya Pencipta.', 'Causa prima menjadi puncak argumen.'),
        ('Urutkan proses penciptaan menurut buku.', ['Awang-awang', 'Langit dengan matahari dan bintang', 'Bumi berisi hawa dan air', 'Bebatuan, logam, dan tanah', 'Makhluk hidup'], 'Penciptaan berjalan dari langit, bumi, benda mati, lalu makhluk hidup.', 'Makhluk hidup muncul setelah bumi siap.'),
        ('Urutkan tingkat pengamalan budi luhur.', ['Rumah tangga', 'Lingkup sosial budaya', 'Lingkup pengamalan spiritual'], 'Pengamalan berjenjang dari rumah sampai spiritual.', 'Spiritual menjadi puncak tangga.'),
        ('Urutkan langkah menjaga hubungan dengan alam.', ['Mengakui alam sebagai ciptaan Tuhan', 'Memanfaatkan secara bijak', 'Memelihara dan memulihkan', 'Berbagi manfaat dengan sesama', 'Bersyukur kepada Tuhan'], 'Hubungan dengan alam dimulai dari pengakuan lalu pemeliharaan.', 'Syukur menutup rangkaian.'),
        ('Urutkan unsur manusia dari yang tak berwujud ke berwujud.', ['Zat hidup adi-kodrati', 'Roh atau nyawa', 'Akal budi', 'Tubuh dari unsur alam'], 'Unsur tak berwujud mendahului tubuh fisik.', 'Tubuh menjadi wadah.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
