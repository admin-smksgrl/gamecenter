"""KEP 8 — Kearifan Lingkungan dan Teknologi Kekinian (Fase E)."""
from kepercayaan_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'KEP 8',
    'slug': 'kep-8-kearifan-lingkungan-teknologi',
    'title': 'Kearifan Lingkungan dan Teknologi Kekinian',
    'description': (
        'Berguru pada alam sebagai wujud mamayu hayuning bawana, memahami '
        'eko-spiritualitas masyarakat adat, menelaah kerusakan lingkungan dan '
        'bahaya sampah plastik, serta menerapkan bioteknologi pertanian organik.'
    ),
    'objectives': [
        'Mengamalkan sikap memelihara lingkungan dan kebersihan sebagai bagian ketaatan kepercayaan.',
        'Menjelaskan konsep berguru pada alam sebagai nilai memelihara lingkungan dalam kepercayaan.',
        'Menganalisis bahaya sampah plastik dan mempromosikan penanganannya dengan 3R.',
        'Menyajikan laporan penerapan bioteknologi sederhana pengelolaan limbah organik.',
    ],
    'minutes': 180,
    'source': (
        'Kepercayaan-BS-KLS-X.pdf Bab 9 Kearifan Lingkungan dan Teknologi Kekinian; '
        'CP Fase E Pendidikan Kepercayaan'
    ),
    'glossary': [
        {'term': 'Mamayu hayuning bawana', 'definition': 'Kewajiban memelihara alam, sama artinya dengan wicaksana atau bijaksana.'},
        {'term': 'Eko-spiritualitas', 'definition': 'Paradigma religius yang memandang cinta lingkungan sebagai ibadah suci kepada Tuhan.'},
        {'term': 'Fotosintesis', 'definition': 'Proses tumbuhan mengubah energi matahari, air, dan CO2 menjadi senyawa gula.'},
        {'term': 'Pemali', 'definition': 'Pantangan atau tabu lingkungan yang disertai keyakinan akan ganjaran bila dilanggar.'},
        {'term': '3R', 'definition': 'Reduce, reuse, recycle: mengurangi, memakai ulang, dan mendaur ulang sampah.'},
        {'term': 'MOL', 'definition': 'Mikroorganisme lokal yang diperbanyak sederhana untuk kompos dan pupuk cair.'},
        {'term': 'PGPR', 'definition': 'Plant Growth Promoting Rhizosphere, mikroba penggiat pertumbuhan yang diperbanyak di laboratorium.'},
        {'term': 'POC', 'definition': 'Pupuk organik cair yang dibuat dari bahan organik melalui bantuan mikroorganisme.'},
        {'term': 'Termoplastik', 'definition': 'Jenis plastik yang melunak karena panas dan dapat dibentuk ulang.'},
    ],
    'intro': {
        'material_title': 'Berguru pada alam',
        'title': 'Belajar dari alam, bukan sekadar tentang alam',
        'paragraphs': [
            'Dalam filosofi kepercayaan, mamayu hayuning bawana sama artinya dengan wicaksana atau bijaksana. Manusia berkewajiban memelihara alam karena alam adalah tempat berdiam, sumber karunia penghidupan, dan pemberi seluruh persembahan suci.',
            'Ada perbedaan besar antara belajar dari alam dan belajar tentang alam. Belajar tentang alam menjadikan alam objek studi yang cenderung dieksploitasi, sedangkan belajar dari alam menjalin hubungan dekat, disertai kerendahan hati dan penghormatan pada misteri proses alam.',
            'Ketika kita menyelami pengalaman bersama alam, tumbuh empati dan cinta. Yang kita cintai akan kita rawat, lestarikan, dan lindungi. Mengamati pohon menyadarkan bahwa segala sesuatu saling tersambung.',
        ],
        'diagram': (
            'Aliran energi dari matahari ke makhluk hidup',
            'flowchart LR\n'
            '  A[Energi matahari] --> B[Daun melakukan fotosintesis]\n'
            '  B --> C[Gula dan glukosa]\n'
            '  C --> D[Tumbuhan dan tiap sel hidup]\n'
            '  D --> E[Herbivor memakan tumbuhan]\n'
            '  E --> F[Karnivor memakan hewan]\n'
            '  F --> G[Pengurai menguraikan sisa]\n'
            '  G --> H[Molekul sederhana kembali ke alam]',
        ),
        'callout': 'Bernafas dan makan adalah belajar dari alam: setiap sel hidup mengolah makanan untuk memperoleh energi.',
        'checkpoint': (
            'Belajar “dari” alam menurut buku menghasilkan…',
            [
                ('hubungan dekat, kerendahan hati, dan penghormatan', True),
                ('penguasaan dan eksploitasi sumber daya', False),
                ('pengubahan alam menjadi produk komersial', False),
                ('pengukuran daya dukung semata', False),
            ],
            'Belajar dari alam menjalin hubungan dekat dan menghormati proses alam.',
        ),
    },
    'concept': {
        'material_title': 'Eko-spiritualitas masyarakat adat',
        'title': 'Alam suci, larangan, dan tabu',
        'paragraphs': [
            'Komunitas adat mengembangkan kearifan lingkungan melalui norma, adat istiadat, mitologi, sistem kepercayaan, serta penataan peran. Karena alam dipandang suci, masyarakat tradisional menganut pantangan dan larangan dalam memeliharanya.',
            'Eko-spiritualitas adalah paradigma hidup religius: cinta lingkungan menjadi bagian ibadah suci kepada Tuhan. Ia bukan sekadar program perbaikan lingkungan, melainkan tatanan hidup yang mempertanyakan apa yang boleh dan tidak boleh dilakukan pada alam.',
            'Larangan dan tabu disertai pemali, yaitu keyakinan akan ganjaran berupa kesialan atau celaka bagi yang melanggarnya. Contohnya keharusan memelihara mata air, menata pengunaan lahan, dan tidak sembarangan memasuki kawasan hutan.',
        ],
        'table': [
            ['Kearifan lingkungan adat', 'Wujud larangan', 'Tujuan'],
            ['Memelihara mata air', 'Tidak mengotori sumber air', 'Menjaga ketersediaan air'],
            ['Menata penggunaan lahan', 'Tidak menggarap area larangan', 'Menjaga kesuburan tanah'],
            ['Menghormati hutan', 'Tidak sembarangan masuk kawasan hutan', 'Menjaga keutuhan ekosistem'],
            ['Kesadaran bersyukur', 'Ritual syukur atas alam', 'Mempertahankan kesakralan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'kep-8-metabolisme',
            'engine': 'mermaid',
            'title': 'Fotosintesis dan respirasi: dua arah daur materi',
            'code': 'flowchart LR\n'
                    '  A[Energi matahari] --> B[Fotosintesis di kloroplas]\n'
                    '  B --> C[Air, CO4 --- air dan CO2]\n'
                    '  C --> D[Senyawa gula sederhana dan glukosa]\n'
                    '  D --> E[Respirasi sel melepas energi]\n'
                    '  E --> F[Karbohidrat, lemak, protein]',
        },
        'activity': categorize_block(
            'kep-8-klasifikasi',
            'Kelompokkan sampah berikut ke dalam cara penanganan yang sesuai.',
            [('b1', 'Bisa didaur ulang'), ('b2', 'Bisa diurai alam')],
            [
                ('i1', 'Botol plastik', 'b1'),
                ('i2', 'Kertas bekas', 'b1'),
                ('i3', 'Kaleng minuman', 'b1'),
                ('i4', 'Daun kering', 'b2'),
                ('i5', 'Sisa buah dan sayur', 'b2'),
                ('i6', 'Kulit telur', 'b2'),
                ('i7', 'Kardus kemasan', 'b1'),
                ('i8', 'Pelepah pisang', 'b2'),
            ],
            'Tepat. Benda yang dapat dilebur atau dipakai lagi, dan bahan organik yang terurai secara alami, dikelola berbeda.',
            'Periksa lagi: bahan organik mudah terurai, sedangkan plastik dan logam tidak.',
        ),
        'subtitle': 'Krisis lingkungan',
        'list': [
            'Masalah lingkungan Indonesia mencakup kerusakan hutan dan emisi CO2, limbah industri, limbah plastik domestik, serta pertanian dan perkebunan.',
            'Indonesia menempati peringkat tertinggi di dunia untuk pengelolaan limbah domestik dan pencemaran plastik ke lautan.',
            'Pertanian dalam negeri kurang efektif: sawah terluas tetapi masih impor beras, ubi, jagung, dan kedelai; pupuk kimia dan pestisida dipakai tidak terkendali.',
            'Plastik bersifat sukar terurai di alam dan sejak 2005 menjadi limbah pencemar lautan yang mengkhawatirkan hampir seluruh dunia.',
        ],
        'checkpoint': (
            'Prinsip reduce, reuse, recycle dikenal dengan sebutan…',
            [
                ('3R', True),
                ('2K', False),
                ('HTML', False),
                ('PGPR', False),
            ],
            '3R adalah reduce (mengurangi), reuse (memakai ulang), dan recycle (mendaur ulang).',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bioteknologi pertanian organik',
        'paragraphs': [
            'Pertanian organik adalah sistem bertani selaras alam yang mengembalikan siklus ekologi dalam areal pertanian. Prinsipnya meminimalkan bahan kimia, memperbaiki sifat fisik dan kimia tanah, serta mengembalikan unsur hara organik ke lahan.',
            'MOL atau mikroorganisme lokal adalah mikroba daerah tertentu yang diperbanyak secara sederhana, dipakai untuk kompos, pupuk cair, perbaikan tanah, dan mengurangi serangan penyakit. Bahannya limbah air cucian beras atau air kelapa dengan sedikit gula, difermentasi 7–21 hari.',
            'PGPR menggunakan mikroba teridentifikasi oleh ahli yang diperbanyak dengan metode laboratorium steril secara aerob. Prinsipnya sama dengan MOL, tetapi pengerjaannya lebih kompleks.',
        ],
        'scenario': scenario(
            'kep-8-skenario',
            'Limbah rumah yang menumpuk',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Sampah dapur organik dan plastik menumpuk di rumah. Apa langkah pertamamu?',
                    'choices': [
                        {'text': 'Memisahkan sampah organik dan anorganik', 'next': 'n2', 'score': 2, 'feedback': 'Pemisahan memudahkan pengelolaan: organik jadi kompos, anorganik didaur ulang.'},
                        {'text': 'Membuang semuanya ke sungai', 'next': 'n3', 'score': 0, 'feedback': 'Membuang ke sungai mencemari air dan lingkungan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana mengelola sampah organik yang menumpuk?',
                    'choices': [
                        {'text': 'Membuat kompos dengan bantuan MOL', 'next': 'n4', 'score': 2, 'feedback': 'Kompos memanfaatkan limbah organik untuk menyuburkan tanah.'},
                        {'text': 'Menimbun plastik bersama bahan organik', 'next': 'n3', 'score': 0, 'feedback': 'Mencampur plastik merusak proses pembuatan kompos.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pencemaran makin parah, air dan tanah tercemar.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Limbah menjadi kompos berguna dan lingkungan bersih.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa arti mamayu hayuning bawana?', 'back': 'Memelihara alam, sama dengan wicaksana atau bijaksana.'},
            {'front': 'Apa bahan utama pembuatan MOL?', 'back': 'Air cucian beras atau air kelapa dengan sedikit gula.'},
            {'front': 'Sebutkan golongan plastik menurut sifatnya.', 'back': 'Termostatik dan termoplastik.'},
            {'front': 'Apa perbedaan MOL dan PGPR?', 'back': 'MOL dari mikroba lokal sederhana; PGPR dari mikroba teridentifikasi yang diperbanyak di laboratorium.'},
        ],
        'checkpoint': (
            'MOL difermentasi selama…',
            [
                ('7–21 hari', True),
                ('1–2 hari', False),
                ('30–40 hari', False),
                ('3–5 bulan', False),
            ],
            'Bahan MOL difermentasi selama 7–21 hari.',
        ),
        'challenge': challenge_block(
            'kep-8-tantangan',
            'Tantangan istilah lingkungan dan teknologi',
            90,
            [
                ('Prinsip kurangi, pakai ulang, daur ulang', '3R'),
                ('Mikroba lokal untuk kompos', 'MOL'),
                ('Pupuk organik cair', 'POC'),
                ('Mikroba diperbanyak di laboratorium', 'PGPR'),
                ('Pantangan lingkungan dengan ganjaran', 'Pemali'),
            ],
            'Lima istilah lingkungan dan teknologi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Mamayu hayuning bawana sama artinya dengan…', 'wicaksana atau bijaksana', ['kekuasaan', 'keberanian', 'kekayaan'], 'Memelihara alam adalah wujud kebijaksanaan.', 'Manusia ditadbirkan sebagai ciptaan yang bijaksana.'),
        ('Belajar “dari” alam menghasilkan…', 'hubungan dekat dan kerendahan hati', ['eksploitasi sumber daya', 'objek studi', 'keuntungan ekonomi'], 'Belajar dari alam menjalin hubungan dekat dengan alam.', 'Menghormati misteri proses alam.'),
        ('Proses tumbuhan mengubah energi matahari menjadi senyawa gula disebut…', 'fotosintesis', ['respirasi', 'ekstraksi', 'fermentasi'], 'Fotosintesis terjadi di daun dengan energi matahari.', 'Kebalikannya adalah respirasi sel.'),
        ('Hewan yang memakan tumbuhan disebut…', 'herbivor', ['karnivor', 'omnivor', 'mikroba'], 'Herbivor memakan tumbuhan.', 'Karnivor memakan hewan lain.'),
        ('Golongan pengurai sisa makhluk hidup meliputi…', 'jamur, bakteri, dan serangga', ['harimau dan elang', 'sapi dan kambing', 'ikan dan udang'], 'Pengurai memecah bangkai menjadi molekul sederhana.', 'Mengembalikan unsur ke alam.'),
        ('Paradigma religius yang memandang cinta lingkungan sebagai ibadah disebut…', 'eko-spiritualitas', ['materialisme', 'humanisme', 'sekularisme'], 'Eko-spiritual adalah tatanan hidup religius.', 'Menyertakan cinta lingkungan sebagai ibadah suci.'),
        ('Keyakinan akan ganjaran bagi yang melanggar larangan lingkungan disebut…', 'pemali', ['pahala', 'sembah', 'sila'], 'Pemali disertai larangan dan tabu lingkungan.', 'Ganjaran berupa kesialan atau celaka.'),
        ('Salah satu larangan lingkungan masyarakat adat adalah…', 'tidak sembarangan memasuki kawasan hutan', ['menebang semua pohon', 'membuang sampah ke sungai', 'menguras mata air'], 'Alam dipandang suci dan sakral.', 'Ada tempat larangan yang tidak boleh digarap.'),
        ('Masalah lingkungan Indonesia mencakup…', 'kerusakan hutan, limbah industri, limbah plastik', ['kekurangan air bersih saja', 'polusi suara saja', 'hanya kemacetan'], 'Empat bidang masalah lingkungan disebut buku.', 'Indonesia berada di klaster tertinggi.'),
        ('Indonesia dinilai paling bermasalah dalam hal…', 'pengelolaan limbah domestik dan sampah plastik', ['ekspor mineral', 'produksi tekstil', 'pariwisata'], 'Sampah plastik mencemari darat hingga lautan.', 'Menempati peringkat klaster tertinggi dunia.'),
        ('Sejak tahun berapa plastik menjadi perhatian dunia sebagai pencemar lautan?', '2005', ['1995', '2015', '2020'], 'Sejak 2005 sampah plastik menjadi limbah pencemar lautan.', 'Mengkhawatirkan daerah pantai dunia.'),
        ('Prinsip reduce, reuse, recycle dikenal sebagai…', '3R', ['MOL', 'POC', 'PGPR'], '3R adalah kurangi, pakai ulang, daur ulang.', 'Mengatasi sampah plastik.'),
        ('Kegiatan yang meminimalkan bahan kimia dalam lahan pertanian adalah…', 'pertanian organik', ['pertanian intensif', 'monokultur', 'agrokimia'], 'Pertanian organik selaras alam dan mengembalikan siklus ekologi.', 'Menuju penggunaan pupuk kimia titik nol.'),
        ('Bahan baku pembuatan MOL adalah…', 'limbah air cucian beras atau air kelapa dengan gula', ['minyak goreng', 'air laut', 'semen'], 'MOL dibuat dari limbah cair organik dengan gula.', 'Difermentasi 7–21 hari.'),
    ],
    'multi': [
        ('Manakah masalah lingkungan yang disebut buku?', ['Kerusakan hutan dan emisi CO2', 'Limbah industri', 'Sampah plastik domestik'], ['Minimnya media sosial', 'Kurangnya wisata', 'Mahalnya ponsel'], 'Empat bidang masalah lingkungan dicatat dalam bab ini.', 'Media sosial bukan masalah lingkungan.'),
        ('Manakah golongan plastik menurut sifatnya?', ['Termostatik', 'Termoplastik'], ['Biofilik', 'Hidrofilik'], 'Plastik dibedakan menjadi termostatik dan termoplastik.', 'Berdasarkan perubahan terhadap panas.'),
        ('Manakah prinsip pertanian organik?', ['Meminimalkan bahan kimia', 'Memperbaiki sifat tanah', 'Mengembalikan unsur hara'], ['Memakai pupuk kimia berlebihan', 'Menebas hutan'], 'Pertanian organik selaras alam dan siklus ekolologi.', 'Pupuk kimia berlebihan merusak tanah.'),
        ('Manakah manfaat MOL?', ['Membuat kompos', 'Membuat pupuk cair', 'Menambah produksi tanah'], ['Menutup rapat limbah plastik', 'Mengganti air minum'], 'MOL dipakai untuk kompos, POC, dan perbaikan tanah.', 'MOL tidak untuk membuang plastik.'),
        ('Manakah jenis MOL yang disebut buku?', ['MOL air beras', 'MOL air kelapa', 'MOL bongkol pisang'], ['MOL minyak', 'MOL semen'], 'MOL dibuat dari bahan organik daerah setempat.', 'Minyak dan semen bukan bahan MOL.'),
        ('Manakah cara penanganan sampah plastik?', ['Mengurangi pemakaian plastik', 'Memakai ulang kantong', 'Mendaur ulang'], ['Membuang ke laut', 'Membakar sembarangan'], '3R mengurangi, memakai ulang, dan mendaur ulang.', 'Membuang dan membakar mencemari.'),
        ('Manakah sikap eko-spiritual?', ['Menjaga mata air', 'Melestarikan hutan', 'Bersyukur atas alam'], ['Mengeksploitasi hutan', 'Mengotori sungai'], 'Eko-spiritual mencintai alam sebagai ibadah.', 'Eksploitasi bertentangan dengannya.'),
        ('Manakah pernyataan tentang fotosintesis?', ['Menggunakan energi matahari', 'Membentuk gula dan glukosa', 'Memerlukan air dan CO2'], ['Melepaskan energi tanpa makanan', 'Hanya terjadi di hewan'], 'Fotosintesis terjadi di daun dan memerlukan cahaya, air, CO2.', 'Senyawa gula menjadi makanan.'),
    ],
    'pairs': [
        ('Mamayu hayuning bawana', 'memelihara alam'),
        ('Eko-spiritualitas', 'cinta lingkungan sebagai ibadah'),
        ('Fotosintesis', 'mengubah energi matahari menjadi gula'),
        ('Pemali', 'pantangan lingkungan dengan ganjaran'),
        ('3R', 'kurangi, pakai ulang, daur ulang'),
        ('MOL', 'mikroorganisme lokal'),
        ('PGPR', 'mikroba diperbanyak di laboratorium'),
        ('POC', 'pupuk organik cair'),
    ],
    'steps': [
        ('Urutkan aliran energi di rantai makanan.', ['Energi matahari', 'Fotosintesis di daun', 'Tumbuhan', 'Herbivor', 'Karnivor', 'Pengurai'], 'Energi mengalir dari matahari ke pengurai.', 'Pengurai mengembalikan unsur ke alam.'),
        ('Urutkan proses fotosintesis.', ['Energi matahari diserap daun', 'Akar menyerap air dan mineral', 'Daun menyedot CO2', 'Air terpecah jadi hidrogen dan oksigen', 'Membentuk gula sederhana dan glukosa'], 'Fotosintesis memadukan cahaya, air, dan CO2.', 'Hasilnya senyawa gula dan oksigen.'),
        ('Urutkan langkah membuat MOL sederhana.', ['Membersihkan wadah', 'Menghaluskan gula merah', 'Melarutkan gula dengan air mendidih', 'Menambahkan bahan cair hingga 2/3 wadah', 'Menutup rapat dan memfermentasi 7–21 hari'], 'MOL dibuat dari gula dan bahan cair lalu difermentasi.', 'Fermentasi menutup proses pembuatan.'),
        ('Urutkan langkah mengelola sampah dengan 3R.', ['Memisahkan sampah organik dan anorganik', 'Mengurangi pemakaian plastik', 'Memakai ulang barang yang layak', 'Mendaur ulang anorganik', 'Membuat kompos dari organik'], 'Pengelolaan dimulai dari pemisahan lalu 3R.', 'Kompos menangani sampah organik.'),
        ('Urutkan sikap menjaga lingkungan menurut buku.', ['Menyadari alam sebagai karunia', 'Mengenali larangan dan tabu adat', 'Memelihara air, tanah, dan hutan', 'Menerapkan pertanian organik', 'Mensyukuri alam dalam ritual'], 'Sikap berjalan dari kesadaran sampai praktik syukur.', 'Praktik nyata menjadi kunci.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)