"""SEJ 1 — Sejarah: Manusia, Ruang, dan Waktu (Fase E)."""
from sejarah_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'SEJ 1',
    'slug': 'sej-1-manusia-ruang-waktu',
    'title': 'Sejarah: Manusia, Ruang, dan Waktu',
    'description': (
        'Memahami ilmu sejarah sebagai kajian manusia dalam ruang dan waktu, '
        'membedakan diakronik dan sinkronik, serta menyusun kronologi dan '
        'periodisasi peristiwa.'
    ),
    'objectives': [
        'Menjelaskan pengertian sejarah dan ilmu sejarah serta manfaat mempelajarinya.',
        'Menganalisis kedudukan manusia sebagai penggerak, pelaku, dan saksi sejarah.',
        'Membedakan cara berpikir diakronik (kronologi) dan sinkronik dalam kajian sejarah.',
        'Menyusun kronologi dan periodisasi peristiwa bersejarah di lingkungan terdekat.',
    ],
    'minutes': 180,
    'source': (
        'Sejarah-BG-KLS-X.pdf Bagian 2 materi Pengantar Ilmu Sejarah; '
        'CP Fase E Mata Pelajaran Sejarah'
    ),
    'glossary': [
        {'term': 'Sejarah', 'definition': 'Ilmu yang mengkaji manusia dalam ruang dan waktu pada masa lampau beserta maknanya bagi masa kini.'},
        {'term': 'Diakronik', 'definition': 'Cara berpikir memanjang dalam waktu, menelusuri peristiwa secara berurutan dari awal ke akhir.'},
        {'term': 'Sinkronik', 'definition': 'Cara berpikir meluas dalam ruang, mengkaji satu peristiwa pada satu masa secara mendalam.'},
        {'term': 'Kronologi', 'definition': 'Urutan peristiwa berdasarkan waktu terjadinya.'},
        {'term': 'Periodisasi', 'definition': 'Pembabakan waktu sejarah menjadi babak atau periode berdasarkan ciri khasnya.'},
        {'term': 'Anakronisme', 'definition': 'Kekeliruan menempatkan peristiwa atau benda pada zaman yang tidak sesuai.'},
        {'term': 'Historia magistra vitae', 'definition': 'Sejarah adalah guru kehidupan; pengalaman masa lalu menjadi pelajaran masa kini.'},
        {'term': 'Sumber sejarah', 'definition': 'Segala jejak yang dapat menjelaskan peristiwa masa lampau.'},
        {'term': 'Kausalitas', 'definition': 'Hubungan sebab akibat antarperistiwa dalam sejarah.'},
    ],
    'intro': {
        'material_title': 'Mengapa mempelajari sejarah?',
        'title': 'Sejarah dekat dengan kehidupan',
        'paragraphs': [
            'Sejarah adalah ilmu yang mengkaji manusia dalam ruang dan waktu. Manusia, masyarakat, dan peristiwa masa lampau menjadi fokus kajiannya, tetapi manfaatnya selalu berbicara tentang masa kini dan masa depan.',
            'Belajar sejarah bukan menghafal tahun. Sejarah melatih keterampilan berpikir: mengumpulkan sumber, menilai bukti, menyusun hubungan sebab akibat, dan mengambil hikmah. Karena itu masa lalu selalu aktual.',
            'Ungkapan historia magistra vitae mengingatkan bahwa sejarah adalah guru kehidupan. Kesalahan masa lalu dapat dihindari, keberhasilan masa lalu dapat ditiru, dan jati diri bangsa dapat dikenali.',
        ],
        'diagram': (
            'Tiga unsur pokok kajian sejarah',
            'flowchart LR\n'
            '  A[Manusia] --> D[Peristiwa sejarah]\n'
            '  B[Ruang] --> D\n'
            '  C[Waktu] --> D\n'
            '  D --> E[Makna bagi masa kini]\n'
            '  E --> F[Hikmah untuk masa depan]',
        ),
        'callout': 'Sejarah tanpa manusia hanyalah rangkaian tanggal; manusia memberi peristiwa itu makna.',
        'checkpoint': (
            'Unsur pokok yang dikaji dalam ilmu sejarah adalah…',
            [
                ('manusia, ruang, dan waktu', True),
                ('angka, tabel, dan grafik', False),
                ('tokoh, pahlawan, dan mitos', False),
                ('peta, cuaca, dan iklim', False),
            ],
            'Ilmu sejarah selalu mengikat tiga unsur: manusia sebagai pelaku, ruang sebagai tempat, dan waktu sebagai kapan.',
        ),
    },
    'concept': {
        'material_title': 'Berpikir diakronik dan sinkronik',
        'title': 'Memanjang dalam waktu, meluas dalam ruang',
        'paragraphs': [
            'Berpikir diakronik berarti menelusuri peristiwa memanjang dalam waktu: dari sebab, proses, hingga akibat. Cara ini menuntut kronologi yang tepat agar urutan peristiwa tidak tertukar.',
            'Berpikir sinkronik berarti meluas dalam ruang: satu peristiwa dikaji pada satu kurun waktu secara mendalam, mencakup berbagai aspek seperti politik, ekonomi, sosial, dan budaya.',
            'Keduanya saling melengkapi. Diakronik menjawab “bagaimana peristiwa itu berkembang”, sinkronik menjawab “mengapa keadaan itu sedemikian rupa pada suatu masa”.',
        ],
        'table': [
            ['Aspek', 'Diakronik', 'Sinkronik'],
            ['Arah kajian', 'Memanjang dalam waktu', 'Meluas dalam ruang'],
            ['Sifat', 'Kronologis dan berurutan', 'Mendalam pada satu masa'],
            ['Cakupan', 'Banyak periode berurutan', 'Satu periode, banyak aspek'],
            ['Contoh kajian', 'Perkembangan kereta api 1864–1945', 'Keadaan kota Batavia tahun 1930'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'sej-1-diakronik-sinkronik',
            'engine': 'mermaid',
            'title': 'Dua arah cara berpikir sejarah',
            'code': 'flowchart TB\n'
                    '  A[Cara berpikir sejarah] --> B[Diakronik]\n'
                    '  A --> C[Sinkronik]\n'
                    '  B --> D[Memanjang dalam waktu]\n'
                    '  B --> E[Kronologi dan periodisasi]\n'
                    '  C --> F[Meluas dalam ruang]\n'
                    '  C --> G[Analisis banyak aspek]',
        },
        'activity': categorize_block(
            'sej-1-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam cara berpikir diakronik atau sinkronik.',
            [('b1', 'Diakronik'), ('b2', 'Sinkronik')],
            [
                ('i1', 'Menelusuri peristiwa dari 1945 sampai 1965', 'b1'),
                ('i2', 'Mengkaji kehidupan ekonomi satu kota pada tahun 1950', 'b2'),
                ('i3', 'Menyusun urutan peristiwa berdasarkan tanggal', 'b1'),
                ('i4', 'Membandingkan politik, sosial, dan budaya pada satu masa', 'b2'),
                ('i5', 'Menjelaskan sebab dan akibat antarperistiwa berurutan', 'b1'),
                ('i6', 'Membahas satu peristiwa secara mendalam tanpa melompat waktu', 'b2'),
                ('i7', 'Membuat garis waktu perjalanan sebuah organisasi', 'b1'),
                ('i8', 'Menganalisis struktur masyarakat pada satu periode', 'b2'),
            ],
            'Tepat. Diakronik bergerak memanjang dalam waktu, sinkronik meluas dalam ruang pada satu masa.',
            'Periksa lagi: kata kunci diakronik adalah urutan waktu, sinkronik adalah kedalaman aspek.',
        ),
        'subtitle': 'Kronologi dan periodisasi',
        'list': [
            'Kronologi menyusun peristiwa menurut waktu terjadinya sehingga tampak hubungan sebab akibat.',
            'Periodisasi membagi waktu sejarah menjadi babak berdasarkan ciri khas, misalnya masa Hindu-Buddha, masa kolonial, dan masa kemerdekaan.',
            'Periodisasi memudahkan pemahaman, tetapi batas antarbabak tidak selalu tajam karena perubahan berlangsung bertahap.',
            'Anakronisme terjadi bila peristiwa atau benda ditempatkan pada zaman yang tidak sesuai; misalnya membayangkan pengirim pesan masa Majapahit memakai telepon.',
        ],
        'checkpoint': (
            'Pembabakan waktu sejarah berdasarkan ciri khas suatu masa disebut…',
            [
                ('periodisasi', True),
                ('kronologi', False),
                ('anakronisme', False),
                ('historiografi', False),
            ],
            'Periodisasi membagi sejarah menjadi periode; kronologi hanya mengurutkan berdasarkan waktu.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menyusun sejarah diri dan lingkungan',
        'paragraphs': [
            'Keterampilan sejarah dapat dilatih dari hal terdekat. Susun empat peristiwa penting dalam hidupmu: apa peristiwanya, di mana, kapan, siapa yang terlibat, dan sumber apa yang dapat membuktikannya.',
            'Setelah data terkumpul, buat lini masa. Dari lini masa itu kamu bisa melihat pola: peristiwa apa yang menjadi sebab, mana yang menjadi akibat, dan pelajaran apa yang bisa diambil.',
            'Cara yang sama dipakai untuk sejarah lingkungan sekitar: kapan sekolah berdiri, kapan jalan dibangun, bagaimana pasar berubah. Semua punya sumber, ruang, waktu, dan makna.',
        ],
        'scenario': scenario(
            'sej-1-skenario',
            'Dua versi cerita tentang berdirinya sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Dua narasumber memberi tahun berdiri sekolah yang berbeda. Apa sikapmu?',
                    'choices': [
                        {'text': 'Mencari sumber lain seperti dokumen atau arsip sekolah', 'next': 'n2', 'score': 2, 'feedback': 'Sumber tertulis dapat menguji dua versi lisan.'},
                        {'text': 'Memilih cerita yang paling seru', 'next': 'n3', 'score': 0, 'feedback': 'Keseruan bukan dasar penilaian sumber sejarah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Arsip menunjukkan tahun yang berbeda dari kedua cerita. Langkahmu?',
                    'choices': [
                        {'text': 'Menuliskan semua versi beserta sumbernya dan menilai keandalannya', 'next': 'n4', 'score': 2, 'feedback': 'Sejarawan menimbang sumber, bukan menyembunyikan versi lain.'},
                        {'text': 'Membuang arsip karena tidak sesuai cerita warga', 'next': 'n3', 'score': 0, 'feedback': 'Mengabaikan sumber hanya karena berbeda membuat kajian tidak jujur.'},
                    ],
                },
                {'id': 'n3', 'text': 'Laporanmu tidak dapat diuji dan kehilangan kepercayaan pembaca.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Laporanmu jujur, terbuka, dan dapat diperiksa ulang.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa tiga unsur pokok kajian sejarah?', 'back': 'Manusia, ruang, dan waktu.'},
            {'front': 'Apa perbedaan diakronik dan sinkronik?', 'back': 'Diakronik memanjang dalam waktu; sinkronik meluas dalam ruang pada satu masa.'},
            {'front': 'Apa itu anakronisme?', 'back': 'Kekeliruan menempatkan peristiwa atau benda pada zaman yang tidak sesuai.'},
            {'front': 'Mengapa kronologi penting?', 'back': 'Agar urutan peristiwa dan hubungan sebab akibatnya tampak jelas.'},
        ],
        'checkpoint': (
            'Manfaat utama mempelajari sejarah menurut CP adalah…',
            [
                ('mengambil hikmah dan mengembangkan keterampilan berpikir sejarah', True),
                ('menghafal seluruh tahun penting', False),
                ('mengumpulkan cerita rakyat', False),
                ('menilai tokoh tanpa bukti', False),
            ],
            'CP Sejarah menekankan hikmah dan keterampilan berpikir, bukan hafalan tahun.',
        ),
        'challenge': challenge_block(
            'sej-1-tantangan',
            'Tantangan istilah ilmu sejarah',
            90,
            [
                ('Memanjang dalam waktu', 'Diakronik'),
                ('Meluas dalam ruang', 'Sinkronik'),
                ('Urutan berdasarkan waktu', 'Kronologi'),
                ('Pembabakan masa', 'Periodisasi'),
                ('Peristiwa di zaman yang salah', 'Anakronisme'),
            ],
            'Lima istilah dasar ilmu sejarah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Ilmu sejarah mengkaji manusia dalam…', 'ruang dan waktu', ['angka dan rumus', 'iklim dan cuaca', 'mesin dan teknologi'], 'Sejarah mengikat manusia pada tempat dan waktu.', 'Tiga unsur pokok: manusia, ruang, waktu.'),
        ('Ungkapan “sejarah adalah guru kehidupan” berbunyi…', 'historia magistra vitae', ['cogito ergo sum', 'veni vidi vici', 'de gustibus'],
         'Masa lalu menjadi pelajaran bagi masa kini.', 'Sering dikutip Cicero.'),
        ('Cara berpikir memanjang dalam waktu disebut…', 'diakronik', ['sinkronik', 'kronologi', 'periodisasi'], 'Diakronik menelusuri peristiwa berurutan.', 'Sinkronik sebaliknya.'),
        ('Cara berpikir meluas dalam ruang pada satu masa disebut…', 'sinkronik', ['diakronik', 'anakronisme', 'kausalitas'], 'Sinkronik mengkaji banyak aspek pada satu kurun.', 'Diakronik memanjang dalam waktu.'),
        ('Urutan peristiwa berdasarkan waktu terjadinya disebut…', 'kronologi', ['periodisasi', 'historiografi', 'anakronisme'], 'Kronologi membantu melihat sebab akibat.', 'Periodisasi membagi babak.'),
        ('Kekeliruan menempatkan benda atau peristiwa pada zaman yang tidak sesuai disebut…', 'anakronisme', ['kronologi', 'kausalitas', 'sinkronik'], 'Contohnya telepon pada masa Majapahit.', 'Perhatikan konteks zaman.'),
        ('Hubungan sebab akibat antarperistiwa disebut…', 'kausalitas', ['periodisasi', 'anakronisme', 'kronologi'], 'Kausalitas menjelaskan mengapa peristiwa terjadi.', 'Bukan sekadar urutan waktu.'),
        ('Pembabakan sejarah menjadi periode berdasarkan ciri khas disebut…', 'periodisasi', ['kronologi', 'kausalitas', 'sinkronik'], 'Periodisasi memudahkan pemahaman.', 'Batas periode tidak selalu tajam.'),
        ('Manusia dalam sejarah berkedudukan sebagai…', 'penggerak, pelaku, dan saksi sejarah', ['objek tanpa peran', 'penonton pasif', 'penguasa alam'], 'Manusia menciptakan sejarah secara individu maupun kolektif.', 'Tindakan manusia meninggalkan jejak.'),
        ('Fokus utama kajian sejarah Indonesia menurut buku adalah…', 'manusia dalam ruang dan waktu dengan konteks Indonesia', ['alam semesta', 'bintang dan planet', 'teknologi digital'], 'Konteks Indonesia menjadi titik berat.', 'Tetap memakai konsep ilmu sejarah.'),
        ('Belajar sejarah paling tepat dilakukan dengan cara…', 'mencari, mengamati, dan menilai sumber', ['menghafal tahun', 'membaca satu buku saja', 'menonton film saja'], 'Sejarah adalah ilmu yang dinamis.', 'Sumber menentukan kualitas kajian.'),
        ('Segala jejak yang dapat menjelaskan peristiwa masa lampau disebut…', 'sumber sejarah', ['mitos', 'opini', 'ramalan'], 'Sumber menjadi dasar penelitian sejarah.', 'Bisa lisan, tulisan, atau benda.'),
        ('Sejarah disebut dekat dan relevan karena…', 'masa lalu selalu aktual bagi masa kini', ['semua peristiwa berulang tepat sama', 'sejarah hanya untuk sejarawan', 'sejarah hanya soal tokoh'], 'Nilai masa lalu terasa di kehidupan sekarang.', 'Hikmah sejarah bersifat aktual.'),
        ('Pernyataan yang menunjukkan berpikir diakronik adalah…', 'menelusuri perkembangan transportasi dari 1864 hingga 1945', ['mengkaji satu kota pada satu tahun', 'membandingkan lima aspek pada satu masa', 'menilai satu peristiwa tanpa waktu'], 'Diakronik memanjang dalam waktu.', 'Sinkronik meluas dalam ruang.'),
    ],
    'multi': [
        ('Manakah unsur pokok dalam kajian sejarah?', ['Manusia', 'Ruang', 'Waktu'], ['Cuaca', 'Angka'], 'Sejarah mengikat manusia, ruang, dan waktu.', 'Cuaca dan angka hanya alat bantu.'),
        ('Manakah ciri berpikir diakronik?', ['Memanjang dalam waktu', 'Berurutan secara kronologis', 'Menelusuri sebab dan akibat'], ['Meluas dalam ruang', 'Mendalam pada satu masa saja'], 'Diakronik bergerak menurut waktu.', 'Sinkronik yang meluas dalam ruang.'),
        ('Manakah ciri berpikir sinkronik?', ['Meluas dalam ruang', 'Mendalam pada satu masa', 'Membahas banyak aspek'], ['Memanjang dalam waktu', 'Menyusun urutan tanggal'], 'Sinkronik menganalisis satu kurun secara mendalam.', 'Bukan urutan waktu.'),
        ('Manakah manfaat mempelajari sejarah?', ['Mengambil hikmah', 'Mengenali jati diri bangsa', 'Melatih berpikir kritis'], ['Menghafal semua tahun', 'Menilai tokoh tanpa bukti'], 'Sejarah membentuk kesadaran dan kecakapan berpikir.', 'Hafalan bukan tujuan utama.'),
        ('Manakah contoh sumber sejarah?', ['Arsip sekolah', 'Foto lama', 'Kesaksian pelaku'], ['Ramalan', 'Dugaan tanpa dasar'], 'Sumber dapat berupa tulisan, gambar, benda, atau kesaksian.', 'Ramalan bukan sumber.'),
        ('Manakah pernyataan tentang kronologi?', ['Mengurutkan peristiwa menurut waktu', 'Membantu melihat sebab akibat', 'Menghindari kekacauan urutan'], ['Membagi zaman menjadi periode', 'Mengganti sumber sejarah'], 'Kronologi adalah urutan waktu.', 'Periodisasi yang membagi babak.'),
        ('Manakah yang termasuk periodisasi sejarah Indonesia?', ['Masa Hindu-Buddha', 'Masa kolonial', 'Masa kemerdekaan'], ['Masa libur sekolah', 'Masa panen raya'], 'Periodisasi memakai ciri khas zaman.', 'Bukan peristiwa harian.'),
        ('Manakah contoh anakronisme?', ['Menyebut telepon pada masa Majapahit', 'Menggunakan istilah presiden untuk raja abad ke-14', 'Membayangkan bus kota pada abad ke-9'], ['Menyebut candi sebagai peninggalan abad ke-9', 'Menyebut VOC sebagai kongsi dagang'], 'Anakronisme menempatkan hal modern di masa lalu.', 'Candi dan VOC sesuai zamannya.'),
    ],
    'pairs': [
        ('Diakronik', 'memanjang dalam waktu'),
        ('Sinkronik', 'meluas dalam ruang'),
        ('Kronologi', 'urutan menurut waktu'),
        ('Periodisasi', 'pembabakan masa'),
        ('Anakronisme', 'peristiwa pada zaman yang salah'),
        ('Kausalitas', 'hubungan sebab akibat'),
        ('Sumber sejarah', 'jejak peristiwa masa lampau'),
        ('Historia magistra vitae', 'sejarah guru kehidupan'),
    ],
    'steps': [
        ('Urutkan langkah menyusun sejarah diri.', ['Menentukan peristiwa penting', 'Mencatat waktu dan tempat', 'Mengumpulkan sumber bukti', 'Menyusun lini masa', 'Menuliskan makna dan pelajaran'], 'Langkah berjalan dari data menuju makna.', 'Lini masa membantu melihat pola.'),
        ('Urutkan langkah berpikir diakronik.', ['Menentukan batas waktu kajian', 'Mengumpulkan peristiwa sesuai urutan', 'Menghubungkan sebab dan akibat', 'Menarik kesimpulan perkembangan'], 'Diakronik menuntut urutan dan hubungan.', 'Kesimpulan menutup kajian.'),
        ('Urutkan langkah berpikir sinkronik.', ['Menentukan satu kurun waktu', 'Memilih aspek yang dikaji', 'Mengumpulkan data tiap aspek', 'Membandingkan antaraspek', 'Menyimpulkan keadaan masa itu'], 'Sinkronik menganalisis satu masa secara mendalam.', 'Perbandingan antaraspek menjadi kunci.'),
        ('Urutkan tahap kerja penelitian sejarah sederhana.', ['Memilih topik', 'Mengumpulkan sumber', 'Memverifikasi sumber', 'Menafsirkan data', 'Menuliskan laporan'], 'Penelitian bergerak dari topik ke laporan.', 'Verifikasi menjaga kejujuran.'),
        ('Urutkan manfaat belajar sejarah dari yang terdekat.', ['Mengenali sejarah diri', 'Memahami sejarah keluarga', 'Memahami sejarah lingkungan', 'Memahami sejarah bangsa', 'Mengambil hikmah untuk masa depan'], 'Kesadaran sejarah tumbuh dari lingkup terdekat.', 'Hikmah menjadi ujung tujuan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
