"""KEP 6 — Mencintai Keberagaman Budaya Spiritual Nusantara (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 6',
    'slug': 'kep-6-keberagaman-budaya-spiritual',
    'title': 'Mencintai Keberagaman Budaya Spiritual Nusantara',
    'description': (
        'Menghayati kearifan lokal sebagai warisan nilai religius dan spiritual, '
        'menggali makna karya leluhur seperti aksara dan tradisi, serta mengambil '
        'peran sebagai penjaga budaya spiritual Nusantara.'
    ),
    'objectives': [
        'Menghayati nilai budaya Nusantara dan kearifan lokal sebagai cerminan nilai spiritualitas religius.',
        'Menghargai budaya dan kearifan lokal sebagai nilai sosial dari masing-masing daerah.',
        'Mengekspresikan nilai kearifan lokal melalui aktivitas atraksi seni secara kreatif.',
        'Menjelaskan hasil analisis tentang kesesuaian nilai kearifan lokal di era global.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 7 Mencintai Keberagaman Budaya Spiritual '
        'Nusantara; CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Kearifan lokal', 'definition': 'Nilai kehidupan tradisi masyarakat lama yang teruji dan dianut dari generasi ke generasi.'},
        {'term': 'Local wisdom', 'definition': 'Istilah asing untuk kearifan lokal, kebijaksanaan yang melampaui kecerdasan rata-rata.'},
        {'term': 'Abugida', 'definition': 'Sistem tulisan yang didasarkan pada konsonan dengan notasi vokal, seperti aksara Nusantara.'},
        {'term': 'Seren Taun', 'definition': 'Ritual syukuran panen komunitas budaya spiritual Sunda Buhun.'},
        {'term': 'Eko-spiritual', 'definition': 'Nilai menghormati dan menyucikan alam sebagai ciptaan Tuhan.'},
        {'term': 'Tepa selira', 'definition': 'Sikap mawas kebersamaan dengan merasakan apa yang dirasakan orang lain.'},
        {'term': 'Pemali', 'definition': 'Larangan adat yang berlaku dalam komunitas budaya spiritual.'},
        {'term': 'Rohani', 'definition': 'Aspek batin manusia yang menjadi sasaran pendidikan budi luhur.'},
    ],
    'intro': {
        'material_title': 'Apa itu kearifan lokal?',
        'title': 'Nilai yang diwariskan lintas generasi',
        'paragraphs': [
            'Kearifan lokal mencakup nilai kehidupan yang berlaku pada tradisi masyarakat lama atau suku asli, dianggap sangat bernilai, telah teruji, dan dianut dari generasi ke generasi.',
            'Kearifan lokal sering dikaitkan dengan kebijaksanaan yang melampaui kecerdasan rata-rata manusia sekarang, sehingga disebut local wisdom. Ajaran budi luhur masa lampau masih memengaruhi sikap generasi kini.',
            'Nilai kearifan itu terpatri dalam adat, hukum, norma, dan pantangan, terutama diwariskan melalui ritual kehidupan, ritual penghidupan, dan ritual penghormatan kepada leluhur serta pahlawan.',
        ],
        'diagram': (
            'Empat klasifikasi nilai kearifan lokal',
            'flowchart TB\n'
            '  A[Kearifan lokal] --> B[Kesatuan dan persatuan]\n'
            '  A --> C[Moralitas sosial]\n'
            '  A --> D[Nilai spiritual]\n'
            '  A --> E[Kelestarian alam]\n'
            '  B --> F[Kerukunan komunitas]\n'
            '  C --> F\n'
            '  D --> G[Kebijaksanaan dan ketuhanan]\n'
            '  E --> G',
        ),
        'callout': 'Nilai kearifan lokal perlu dijaga agar tidak terkikis menjadi sekadar transaksi sosial “take and give”.',
        'checkpoint': (
            'Sistem tulisan yang didasarkan pada konsonan dengan notasi vokal disebut…',
            [
                ('abugida', True),
                ('alfabet', False),
                ('silabis murni', False),
                ('hieroglif', False),
            ],
            'Aksara Nusantara umumnya abugida atau alfasilabis, misalnya Ha Na Ca Ra Ka.',
        ),
    },
    'concept': {
        'material_title': 'Karya leluhur warisan monumental',
        'title': 'Aksara, mitos, dan tradisi',
        'paragraphs': [
            'Kebudayaan terus berkembang karena pelajaran dari peristiwa alam, dinamika internal manusia, dan interaksi antarbudaya. Karya yang meninggalkan tanda bermakna hingga kini menjadi warisan monumental.',
            'Leluhur menyiratkan nilai melalui mitos, cerita, umpama, dan sastra karena daya jangkauannya melampaui ingatan orang yang memulai cerita. Nilai itu digali kembali oleh generasi penerus.',
            'Aksara Nusantara menurut banyak ahli mulai dikenal sekitar abad ke-4 Masehi dan masih kerabat aksara Pallawa serta Kawi Jawa. Contoh notasinya: Ha Na Ca Ra Ka; Ba Wa Ma Nga; La Pa Sa Da Ga Ja Ya Nya.',
        ],
        'table': [
            ['Warisan', 'Bentuk', 'Nilai yang disiratkan'],
            ['Aksara Jawa', 'Ha Na Ca Ra Ka', 'Falsafah sangkan paraning dumadi'],
            ['Aksara Batak', 'Font Uli Kozok 2001', 'Silsilah, pengobatan, hukum, moral'],
            ['Mitos dan cerita', 'Cerita rakyat lisan', 'Pesan moral lintas generasi'],
            ['Ritual syukuran', 'Seren Taun, Sipaha Lima', 'Syukur atas karunia dan panen'],
            ['Media tulis', 'Daun lontar dan batu tulis', 'Serat, hikayat, dan pokok hukum'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-6-pendidikan',
            'engine': 'mermaid',
            'title': 'Jalur pewarisan kearifan lokal',
            'code': 'flowchart LR\n'
                    '  A[Sistem kepercayaan leluhur] --> B[Tokoh dan leluhur pencerah]\n'
                    '  B --> C[Tradisi dan kearifan lokal]\n'
                    '  C --> D[Ekspresi budaya: seni, ritual, arsitektur]\n'
                    '  D --> E[Pendidikan karakter generasi muda]\n'
                    '  E --> F[Penjaga kearifan masa depan]',
        },
        'activity': categorize_block(
            'kep-6-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam nilai kearifan lokal yang sesuai.',
            [('b1', 'Nilai spiritual'), ('b2', 'Nilai kelestarian alam')],
            [
                ('i1', 'Ketundukan pada kehendak Tuhan', 'b1'),
                ('i2', 'Kebijaksanaan dan budi luhur', 'b1'),
                ('i3', 'Kecerdasan spiritual pemimpin', 'b1'),
                ('i4', 'Menghormati dan menyucikan alam', 'b2'),
                ('i5', 'Menjaga hutan dan sumber air', 'b2'),
                ('i6', 'Ritual syukur atas hasil bumi', 'b2'),
            ],
            'Tepat. Nilai spiritual berkaitan dengan ketuhanan dan kebijaksanaan, nilai kelestarian alam dengan eko-spiritual.',
            'Periksa lagi: sikap menyucikan alam termasuk nilai kelestarian alam.',
        ),
        'subtitle': 'Tradisi menjaga moralitas',
        'list': [
            'Kearifan lokal menjadi sumber nilai dan penjaga sikap moral serta karakter kebijaksanaan masyarakat.',
            'Nilai moral masyarakat tradisional terjaga melalui penilaian sosial berupa norma kepantasan dan kepatutan.',
            'Otoritas adat sebagai penjaga moral kini melemah, terutama di masyarakat urban modern.',
            'Pendidikan karakter menumbuhkan budi luhur melalui keteladanan, teguran, dan pembiasaan dalam konteks nyata.',
        ],
        'checkpoint': (
            'Ritual syukuran panen komunitas Sunda Buhun disebut…',
            [
                ('Seren Taun', True),
                ('Sipaha Lima', False),
                ('Wulla Poddu', False),
                ('Marakka Bola', False),
            ],
            'Seren Taun adalah ritual syukuran panen komunitas budaya spiritual Sunda Buhun.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menjadi pamong kearifan lokal',
        'paragraphs': [
            'Meski jumlah penghayat relatif kecil, perannya besar karena komunitas penghayat dinilai paling konsisten menyerap dan menerapkan nilai budi luhur yang berkorelasi dengan ritual tradisinya.',
            'Penghayat yang berkualitas siap memberi sumbangsih sebagai penyuluh nilai budi luhur dan spiritualitas berbasis kearifan lokal. Penguatan nilai itu juga menjadi filter terhadap pengaruh negatif globalisasi budaya.',
            'Pewarisan berlangsung alami dalam konteks kehidupan: ketika menari seseorang belajar nilai dan norma, ketika bekerja di ladang ia dibimbing kearifan terhadap alam, ketika beritual ia menerima nasehat tata upacara. Semangatnya belajar sepanjang hayat.',
        ],
        'scenario': scenario(
            'kep-6-skenario',
            'Tradisi yang mulai ditinggalkan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Warga muda mulai meninggalkan ritual syukuran panen di desamu. Apa langkah awalmu?',
                    'choices': [
                        {'text': 'Mempelajari makna ritual dan melibatkan pemuda dalam persiapannya', 'next': 'n2', 'score': 2, 'feedback': 'Pemahaman makna dan keterlibatan menumbuhkan rasa memiliki.'},
                        {'text': 'Membiarkannya karena tradisi dianggap kuno', 'next': 'n3', 'score': 0, 'feedback': 'Membiarkan berarti membiarkan kearifan lokal terkikis.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Pemuda mengusulkan ritual ditampilkan sebagai atraksi seni. Bagaimana sikapmu?',
                    'choices': [
                        {'text': 'Mendukung dengan tetap menjaga nilai dan tata cara yang sakral', 'next': 'n4', 'score': 2, 'feedback': 'Kreativitas boleh, asal nilai dan kesakralan terjaga.'},
                        {'text': 'Menolak semua kegiatan seni karena bukan ritual', 'next': 'n3', 'score': 0, 'feedback': 'Menolak kreativitas membuat tradisi makin jauh dari generasi muda.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tradisi melemah dan nilai kearifan lokal makin terkikis.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tradisi hidup kembali dan dikenal generasi muda.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan empat klasifikasi nilai kearifan lokal.', 'back': 'Kesatuan dan persatuan, moralitas sosial, nilai spiritual, dan kelestarian alam.'},
            {'front': 'Sejak abad berapa aksara Nusantara dikenal?', 'back': 'Sekitar abad ke-4 Masehi, kerabat aksara Pallawa dan Kawi.'},
            {'front': 'Apa makna “mata do guru, roha sisean”?', 'back': 'Mata adalah guru, hati dan pikiran menjadi murid.'},
            {'front': 'Mengapa ritual dianggap suci?', 'back': 'Karena berhubungan dengan Yang Maha Suci sehingga menuntut kesucian diri.'},
        ],
        'checkpoint': (
            'Peribahasa Batak Toba “tuhe sigaton batange dapoton” bermakna…',
            [
                ('patok pancang tertanam yang harus ditilik, pematang lurus sesuai patok', True),
                ('tanah luas harus dijual', False),
                ('hujan turun membawa berkah', False),
                ('batu besar menjadi tempat duduk', False),
            ],
            'Peribahasa itu menegaskan pentingnya keteladanan dan patokan nilai yang dijaga.',
        ),
        'challenge': challenge_block(
            'kep-6-tantangan',
            'Tantangan istilah budaya spiritual',
            90,
            [
                ('Nilai kehidupan tradisi yang teruji', 'Kearifan lokal'),
                ('Sistem tulisan konsonan dengan notasi vokal', 'Abugida'),
                ('Ritual syukuran panen Sunda Buhun', 'Seren Taun'),
                ('Merasakan yang dirasakan orang lain', 'Tepa selira'),
                ('Larangan adat dalam komunitas', 'Pemali'),
            ],
            'Lima istilah budaya spiritual terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Nilai kehidupan tradisi masyarakat lama yang teruji dan dianut lintas generasi disebut…', 'kearifan lokal', ['globalisasi', 'modernisasi', 'industrialisasi'], 'Kearifan lokal adalah nilai tradisi yang teruji dan diwariskan.', 'Istilah asingnya local wisdom.'),
        ('Kearifan lokal sering disebut dengan istilah asing…', 'local wisdom', ['global culture', 'social norm', 'mass culture'], 'Local wisdom menunjuk kebijaksanaan lokal.', 'Melampaui kecerdasan rata-rata.'),
        ('Salah satu klasifikasi nilai kearifan lokal adalah…', 'nilai spiritual', ['nilai komersial', 'nilai hiburan', 'nilai politik praktis'], 'Klasifikasi meliputi kesatuan, moralitas sosial, spiritual, dan kelestarian alam.', 'Nilai spiritual berkaitan dengan ketuhanan.'),
        ('Menghormati dan menyucikan alam termasuk nilai…', 'kelestarian alam', ['kesatuan dan persatuan', 'moralitas sosial', 'nilai spiritual'], 'Nilai kelestarian alam bersifat eko-spiritual.', 'Menjaga hubungan manusia dengan alam.'),
        ('Aksara Nusantara menurut banyak ahli mulai dikenal sekitar…', 'abad ke-4 Masehi', ['abad ke-10 Masehi', 'abad ke-16 Masehi', 'abad ke-20 Masehi'], 'Aksara Nusantara mulai dikenal sekitar abad ke-4 Masehi.', 'Masih kerabat Pallawa dan Kawi.'),
        ('Sistem tulisan aksara Nusantara umumnya berbentuk…', 'abugida atau alfasilabis', ['alfabet Latin murni', 'hieroglif', 'huruf paku'], 'Aksara Nusantara berbasis konsonan dengan notasi vokal.', 'Contohnya Ha Na Ca Ra Ka.'),
        ('Leluhur menyiratkan nilai melalui mitos, cerita, umpama, dan sastra karena…', 'daya jangkauannya melampaui ingatan penutur awal', ['lebih murah biayanya', 'lebih singkat', 'lebih modern'], 'Cerita bertahan melampaui ingatan orang yang memulainya.', 'Nilai diwariskan turun-temurun.'),
        ('Media tulis tradisional yang disebut buku adalah…', 'daun lontar dan batu tulis', ['kertas HVS', 'papan tulis', 'layar digital'], 'Naskah ditulis pada daun lontar dan batu tulis.', 'Berisi serat, hikayat, dan hukum.'),
        ('Ritual syukuran panen komunitas Sunda Buhun disebut…', 'Seren Taun', ['Sipaha Lima', 'Wulla Poddu', 'Ngaben'], 'Seren Taun adalah ritual syukuran panen.', 'Menjadi wujud syukur atas karunia.'),
        ('Pendidikan karakter menumbuhkan nilai budi luhur melalui…', 'keteladanan, teguran, dan pembiasaan', ['hukuman berat', 'hafalan panjang', 'ujian tertulis'], 'Nilai kearifan lokal dijelaskan dalam konteks praktik.', 'Belajar dari melihat lalu mencoba.'),
        ('Menurut buku, penghayat kepercayaan berperan sebagai…', 'penyuluh nilai budi luhur berbasis kearifan lokal', ['penjaga rahasia adat', 'pemimpin politik', 'pelaku perdagangan budaya'], 'Penghayat menjadi rujukan nilai luhur kearifan lokal.', 'Sekaligus penjaga tradisi.'),
        ('Sikap “tepa selira” berarti…', 'mawas kebersamaan dengan merasakan perasaan orang lain', ['menonjolkan diri', 'menuntut hak', 'menjauhi pergaulan'], 'Tepa selira adalah memayu hayu sesama.', 'Menjadi dasar tenggang rasa.'),
        ('Aksara Batak Toba pertama kali dibuat fontnya oleh…', 'Uli Kozok', ['Marubat Sitorus', 'Poltak Sirait', 'Suharto'], 'Prof. Uli Kozok membuat font aksara Batak Toba pada 2001.', 'Berlisensi Microsoft Batak Unicode.'),
        ('Ungkapan “mata do guru, roha sisean” bermakna…', 'mata adalah guru, hati dan pikiran menjadi murid', ['mata harus ditutup saat belajar', 'guru harus melihat murid', 'murid wajib menatap guru'], 'Pepatah itu mengajarkan belajar dari pengamatan.', 'Pengalaman menjadi bahan pelajaran.'),
    ],
    'multi': [
        ('Manakah klasifikasi nilai kearifan lokal?', ['Nilai kesatuan dan persatuan', 'Moralitas sosial', 'Nilai spiritual'], ['Nilai komersial', 'Nilai hiburan massal'], 'Klasifikasi menurut buku ada empat.', 'Nilai komersial tidak termasuk.'),
        ('Manakah warisan monumental leluhur?', ['Aksara daerah', 'Mitos dan cerita', 'Ritual tradisi'], ['Iklan digital', 'Aplikasi pesan'], 'Warisan leluhur berupa aksara, cerita, ritual, dan karya budaya.', 'Iklan digital bukan warisan leluhur.'),
        ('Manakah manfaat mempelajari budaya Nusantara?', ['Membangun martabat sebagai pewaris budaya', 'Meningkatkan rasa percaya diri bangsa', 'Menjaga nama baik keluarga dan bangsa'], ['Merendahkan budaya lain', 'Menolak keberagaman'], 'Manfaatnya membangun martabat dan percaya diri.', 'Merendahkan budaya lain bertentangan.'),
        ('Manakah bentuk ritual yang disebut buku?', ['Ritual kehidupan dan penghidupan', 'Ritual penghormatan leluhur', 'Upacara syukuran panen'], ['Ritual hiburan komersial', 'Ritual politik'], 'Ritual mewariskan nilai budi luhur.', 'Ritual komersial bukan tradisi.'),
        ('Manakah nilai yang perlu dipegang masyarakat menurut buku?', ['Keberagaman', 'Toleransi', 'Kebersamaan'], ['Dominasi satu budaya', 'Permusuhan antarsuku'], 'Nilai itu menjaga persatuan dan kesatuan.', 'Dominasi merusak keberagaman.'),
        ('Manakah media tulis tradisional Nusantara?', ['Daun lontar', 'Batu tulis', 'Kulit kayu'], ['Papan ketik', 'Layar sentuh'], 'Naskah lama ditulis di lontar, batu, dan kulit kayu.', 'Papan ketik adalah teknologi modern.'),
        ('Manakah contoh ekspresi budaya yang lahir dari sistem kepercayaan?', ['Tarian ritual', 'Arsitektur rumah adat', 'Sistem kalender kuno'], ['Iklan televisi', 'Permainan daring'], 'Ekspresi budaya tumbuh dari nilai kepercayaan.', 'Iklan bukan warisan ritual.'),
        ('Manakah sikap penjaga kearifan lokal?', ['Mempelajari makna tradisi', 'Melibatkan generasi muda', 'Menjaga kesakralan ritual'], ['Meninggalkan ritual', 'Mengubah ritual tanpa pemahaman'], 'Penjaga kearifan memahami dan melibatkan generasi muda.', 'Meninggalkan tradisi melemahkan kearifan.'),
    ],
    'pairs': [
        ('Kearifan lokal', 'nilai tradisi yang teruji'),
        ('Local wisdom', 'istilah asing kearifan lokal'),
        ('Abugida', 'tulisan konsonan dengan notasi vokal'),
        ('Seren Taun', 'syukuran panen Sunda Buhun'),
        ('Tepa selira', 'merasakan perasaan orang lain'),
        ('Pemali', 'larangan adat komunitas'),
        ('Eko-spiritual', 'menyucikan alam ciptaan Tuhan'),
        ('Uli Kozok', 'pembuat font aksara Batak'),
    ],
    'steps': [
        ('Urutkan jalur pewarisan kearifan lokal.', ['Sistem kepercayaan leluhur', 'Tokoh dan leluhur pencerah', 'Tradisi dan kearifan lokal', 'Ekspresi budaya', 'Pendidikan karakter generasi muda'], 'Pewarisan berjalan dari kepercayaan sampai pendidikan generasi.', 'Pendidikan menjadi ujung rantai.'),
        ('Urutkan langkah menggali makna warisan leluhur.', ['Mengenali bentuk warisan', 'Mempelajari konteks budayanya', 'Menemukan nilai yang disiratkan', 'Mempraktikkan dalam kehidupan', 'Mewariskan kepada generasi muda'], 'Penggalian makna bergerak dari bentuk ke praktik.', 'Pewarisan menutup langkah.'),
        ('Urutkan langkah menyiapkan atraksi seni berbasis kearifan lokal.', ['Memilih tradisi yang akan diangkat', 'Mempelajari nilai dan tata caranya', 'Menyusun kreasi pertunjukan', 'Berlatih bersama warga', 'Menampilkan dengan menjaga kesakralan'], 'Kreasi seni tetap berpijak pada nilai tradisi.', 'Kesakralan wajib dijaga.'),
        ('Urutkan sikap menjaga moralitas masyarakat.', ['Mengenali norma kepantasan', 'Memberi keteladanan', 'Menegur dengan santun', 'Membiasakan perilaku baik', 'Menjaga tradisi bersama'], 'Penjagaan moral dimulai dari pengenalan norma sampai kebiasaan.', 'Keteladanan menjadi kunci.'),
        ('Urutkan langkah belajar sepanjang hayat menurut buku.', ['Mengamati peristiwa di sekitar', 'Menanyakan kepada yang lebih tahu', 'Mengalami dan menjalani sendiri', 'Mengambil pelajaran', 'Menerapkan pada kehidupan berikutnya'], 'Belajar berjalan dari pengamatan sampai penerapan.', 'Pengalaman menjadi guru.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
