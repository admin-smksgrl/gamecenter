"""ANIM 8 — Konsep Dasar Visual (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 8',
    'slug': 'anim-8-konsep-dasar-visual',
    'title': 'Konsep Dasar Visual',
    'description': (
        'Memahami unsur-unsur visual (titik, garis, bidang, ruang, warna, '
        'tekstur, gelap terang), mengorganisasikannya dengan prinsip desain '
        'dan perspektif, serta menguasai dasar teknik bervisual seperti '
        'anatomi manusia.'
    ),
    'objectives': [
        'Mengidentifikasi tujuh unsur visual dan maknanya.',
        'Menerapkan prinsip desain: kesatuan, keseimbangan, kontras, pengulangan, ritme, emphasis, dan proporsi.',
        'Menggambar dengan proyeksi perspektif satu, dua, dan tiga titik lenyap.',
        'Menggambar anatomi manusia dan anak sesuai proporsi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 8 Konsep Dasar Visual; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Titik', 'definition': 'Unsur visual paling dasar yang melahirkan garis, bentuk, dan bidang.'},
        {'term': 'Garis nyata', 'definition': 'Garis yang dihasilkan melalui goresan alat gambar.'},
        {'term': 'Garis semu', 'definition': 'Kesan batas objek yang bersinggungan, bukan goresan.'},
        {'term': 'Bidang geometris', 'definition': 'Bidang teratur dan terukur, misalnya segi empat dan lingkaran.'},
        {'term': 'Bidang organis', 'definition': 'Bidang bebas menyerupai bentuk kehidupan alam.'},
        {'term': 'Ruang positif', 'definition': 'Objek utama dalam gambar.'},
        {'term': 'Ruang negatif', 'definition': 'Ruang kosong di sekitar objek utama.'},
        {'term': 'Warna primer', 'definition': 'Merah, biru, kuning; warna utama tanpa pencampuran.'},
        {'term': 'Komposisi', 'definition': 'Pengorganisasian unsur visual menurut prinsip desain.'},
        {'term': 'Titik lenyap', 'definition': 'Titik pusat tempat garis-garis perspektif bertemu.'},
        {'term': 'Proporsi tubuh', 'definition': 'Perbandingan tinggi tubuh terhadap tinggi kepala, misalnya 7,5 atau 8 kepala.'},
    ],
    'intro': {
        'material_title': 'Unsur-unsur visual',
        'title': 'Titik, garis, bidang, ruang, warna, tekstur',
        'paragraphs': [
            'Unsur visual adalah komponen pembentuk karya visual: titik, garis, bidang, ruang, warna, tekstur, dan gelap terang. Setiap unsur memiliki potensi dan keterbatasannya.',
            'Titik mendasari terbentuknya unsur lain; ukurannya tidak terbatas karena bergantung pada alat dan jarak pandang. Garis lahir ketika titik ditarik melalui goresan.',
            'Bidang dibedakan menjadi bidang geometris (teratur, formal) dan bidang organis (bebas, fleksibel). Ruang terbagi menjadi ruang positif (objek utama) dan ruang negatif (ruang kosong).',
            'Warna dijelaskan lewat dua teori: spektrum cahaya Newton dan lingkaran warna pigmen Brewster (primer, sekunder, tersier, netral).',
        ],
        'diagram': (
            'Peta unsur visual',
            'flowchart TB\n'
            '  A[Titik] --> B[Garis]\n'
            '  B --> C[Bidang]\n'
            '  C --> D[Ruang]\n'
            '  D --> E[Warna, tekstur, gelap terang]\n'
            '  E --> F[Karya visual utuh]',
        ),
        'callout': 'Setiap jenis garis punya makna: horizontal tenang, vertikal kokoh, diagonal dinamis, zig-zag semangat, lengkung luwes, spiral kelahiran.',
        'checkpoint': (
            'Unsur visual yang mendasari terbentuknya garis, bentuk, dan bidang adalah…',
            [
                ('titik', True),
                ('warna', False),
                ('tekstur', False),
                ('ruang negatif', False),
            ],
            'Titik adalah unsur visual paling dasar.',
        ),
    },
    'concept': {
        'material_title': 'Mengorganisasikan unsur visual',
        'title': 'Prinsip desain dan perspektif',
        'paragraphs': [
            'Komposisi adalah penggabungan unsur visual menurut aturan yang disebut prinsip desain agar karya estetis dan efektif.',
            'Prinsip desain meliputi kesatuan (unity), keseimbangan (balance), kontras (contrast), pengulangan (repetition), ritme (rhythm), emphasis (point of interest), dan proporsi.',
            'Keseimbangan simetris membuat susunan terlihat merata horizontal maupun vertikal; keseimbangan asimetris memakai unsur berbeda dengan bobot sama.',
            'Proyeksi perspektif membuat benda tampak bervolume; makin jauh objek dari mata, makin kecil ukurannya. Perspektif dibedakan menjadi satu, dua, dan tiga titik lenyap.',
        ],
        'table': [
            ['Prinsip', 'Makna', 'Contoh penerapan'],
            ['Kesatuan', 'Unsur saling mendukung dan selaras', 'Kesamaan bentuk dan warna'],
            ['Keseimbangan', 'Susunan serasi dan stabil', 'Simetris atau asimetris'],
            ['Kontras', 'Perbedaan unsur agar menonjol', 'Teks gelap di latar terang'],
            ['Pengulangan', 'Menguatkan unsur dengan repetisi', 'Pola bentuk sama'],
            ['Ritme', 'Pola variatif dan konsisten', 'Garis berombak teratur'],
            ['Emphasis', 'Pusat perhatian', 'Satu bidang berbeda warna'],
            ['Proporsi', 'Perbandingan ukuran antarunsur', 'Hubungan panjang, lebar, tinggi'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-8-perspektif',
            'engine': 'mermaid',
            'title': 'Jenis proyeksi perspektif',
            'code': 'flowchart TB\n'
                    '  A[Proyeksi perspektif] --> B[Satu titik lenyap: interior dan rancang bangun]\n'
                    '  A --> C[Dua titik lenyap: sudut benda]\n'
                    '  A --> D[Tiga titik lenyap: tampak dramatis]\n'
                    '  B --> E[Garis batas langit dan tanah: horizon]',
        },
        'activity': categorize_block(
            'anim-8-klasifikasi',
            'Kelompokkan pernyataan sesuai prinsip desainnya.',
            [('b1', 'Kesatuan'), ('b2', 'Kontras'), ('b3', 'Ritme')],
            [
                ('i1', 'Unsur saling mendukung membentuk keselarasan', 'b1'),
                ('i2', 'Teks dibuat menonjol agar mudah dibaca', 'b2'),
                ('i3', 'Garis bergelombang teratur memberi kesan gerak', 'b3'),
                ('i4', 'Menyamakan bentuk dan warna objek', 'b1'),
                ('i5', 'Menghindari kesan monoton dengan perbedaan', 'b2'),
                ('i6', 'Pola berulang dengan variasi ukuran', 'b3'),
            ],
            'Tepat. Unity menyatukan, kontras menonjolkan, ritme menggerakkan.',
            'Periksa lagi: kesatuan=selaras, kontras=beda, ritme=pola.',
        ),
        'subtitle': 'Dasar teknik bervisual',
        'list': [
            'Proporsi tubuh manusia: normal 7,5 kepala, ideal 8 kepala, fashion 8,5 kepala, heroik 9 kepala.',
            'Anatomi anak: usia 1–3 tahun 4x tinggi kepala, 4–6 tahun 5x, 7–9 tahun 6x, dan 10–13 tahun 7x.',
            'Laki-laki digambarkan dengan bahu lebar dan dada bidang; perempuan dengan panggul besar dan bahu lebih kecil.',
            'Gelap terang (value) menciptakan efek volum pada bangun ruang dalam gambar.',
        ],
        'checkpoint': (
            'Proporsi tubuh manusia yang dianggap ideal adalah…',
            [
                ('8 kali tinggi kepala', True),
                ('7,5 kali tinggi kepala', False),
                ('6 kali tinggi kepala', False),
                ('9 kali tinggi kepala', False),
            ],
            'Normal 7,5; ideal 8; fashion 8,5; heroik 9.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Berlatih mengomposisikan gambar',
        'paragraphs': [
            'Titik lenyap dijadikan pusat penarikan garis untuk menggambarkan objek; garis batas antara langit dan tanah disebut garis cakrawala (horizon).',
            'Prinsip kontras juga berfungsi sebagai aksesibilitas, misalnya kontras teks dengan latar agar mudah dibaca.',
            'Pengulangan yang tidak tepat menimbulkan efek statis dan monoton sehingga perlu variasi agar terasa dinamis.',
        ],
        'scenario': scenario(
            'anim-8-skenario',
            'Poster yang kurang enak dilihat',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Poster karyamu dinilai ramai dan tidak nyaman dilihat. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menata ulang dengan prinsip desain: kesatuan, kontras, dan keseimbangan', 'next': 'n2', 'score': 2, 'feedback': 'Prinsip desain membuat karya estetis dan efektif.'},
                        {'text': 'Menambahkan lebih banyak unsur tanpa aturan', 'next': 'n3', 'score': 0, 'feedback': 'Menambah unsur tanpa komposisi justru makin membingungkan.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana membuat satu bagian menjadi pusat perhatian?',
                    'choices': [
                        {'text': 'Menerapkan emphasis dengan kontras warna atau ukuran', 'next': 'n4', 'score': 2, 'feedback': 'Emphasis mengarahkan pandangan penonton.'},
                        {'text': 'Menyamakan semua ukuran dan warna', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa perbedaan, tidak ada pusat perhatian.'},
                    ],
                },
                {'id': 'n3', 'text': 'Poster tetap tidak dipahami penonton.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Poster menjadi jelas, menarik, dan mudah dibaca.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan tujuh unsur visual.', 'back': 'Titik, garis, bidang, ruang, warna, tekstur, gelap terang.'},
            {'front': 'Apa beda ruang positif dan negatif?', 'back': 'Positif objek utama; negatif ruang kosong di sekitarnya.'},
            {'front': 'Sebutkan tujuh prinsip desain.', 'back': 'Kesatuan, keseimbangan, kontras, pengulangan, ritme, emphasis, proporsi.'},
            {'front': 'Apa itu titik lenyap?', 'back': 'Titik tempat garis perspektif bertemu.'},
        ],
        'checkpoint': (
            'Garis batas antara langit dan tanah dalam perspektif disebut…',
            [
                ('garis cakrawala', True),
                ('garis diagonal', False),
                ('garis semu', False),
                ('garis spiral', False),
            ],
            'Horizon menjadi acuan posisi objek.',
        ),
        'challenge': challenge_block(
            'anim-8-tantangan',
            'Tantangan istilah desain visual',
            90,
            [
                ('Unsur dasar pembentuk garis dan bidang', 'Titik'),
                ('Bidang teratur dan terukur', 'Bidang geometris'),
                ('Objek utama dalam gambar', 'Ruang positif'),
                ('Prinsip menyatukan unsur agar selaras', 'Kesatuan'),
                ('Titik tempat garis perspektif bertemu', 'Titik lenyap'),
            ],
            'Lima istilah desain visual terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Unsur visual yang menjadi dasar terbentuknya garis dan bidang adalah…', 'titik', ['warna', 'tekstur', 'gelap terang'], 'Gambar selalu diawali dari titik.', 'Ukuran titik tidak terbatas.'),
        ('Garis yang berupa kesan batas objek bersinggungan disebut…', 'garis semu', ['garis nyata', 'garis tegas', 'garis ganda'], 'Bukan hasil goresan.', 'Berbeda dari garis nyata.'),
        ('Garis horizontal memberi sugesti…', 'ketenangan dan kedamaian', ['kekuatan dan kekokohan', 'semangat dan kegembiraan', 'kelahiran'], 'Horisontal terasa tenang.', 'Vertikal terasa kokoh.'),
        ('Garis zig-zag memberi kesan…', 'semangat, ceria, dan gembira', ['tenang dan damai', 'luwes dan anggun', 'masif dan megah'], 'Zig-zag mengesankan semangat.', 'Spiral mengesankan kelahiran.'),
        ('Bidang yang teratur dan dapat diukur secara sistematis disebut…', 'bidang geometris', ['bidang organis', 'bidang semu', 'bidang negatif'], 'Misalnya segi empat dan lingkaran.', 'Kesan formal.'),
        ('Ruang kosong di sekitar objek utama disebut…', 'ruang negatif', ['ruang positif', 'ruang nyata', 'ruang tiga dimensi'], 'Ruang positif adalah objek utama.', 'Keduanya membentuk komposisi.'),
        ('Teori spektrum warna ditemukan oleh…', 'Sir Isaac Newton', ['Brewster', 'Einstein', 'Da Vinci'], 'Newton memakai prisma.', 'Menghasilkan merah hingga ungu.'),
        ('Warna primer menurut Brewster adalah…', 'merah, biru, kuning', ['hijau, oranye, ungu', 'merah-oranye dan biru-hijau', 'hitam dan putih'], 'Warna primer tanpa campuran.', 'Sekunder hasil campuran primer.'),
        ('Prinsip yang membuat susunan terasa tenang dan stabil disebut…', 'keseimbangan', ['kontras', 'ritme', 'pengulangan'], 'Simetris dan asimetris.', 'Memberi perasaan tenang.'),
        ('Prinsip untuk membuat bagian tertentu menjadi pusat perhatian adalah…', 'emphasis', ['repetition', 'unity', 'proporsi'], 'Point of interest dicapai dengan kontras.', 'Mengarahkan pandangan penonton.'),
        ('Kesan makin jauh makin kecil pada perspektif menunjukkan adanya…', 'titik lenyap', ['garis semu', 'bidang organis', 'warna tersier'], 'Garis menuju titik lenyap.', 'Garis cakrawala sebagai batas.'),
        ('Proporsi tubuh heroik berukuran…', 'sembilan kali kepala', ['tujuh setengah kepala', 'delapan kepala', 'delapan setengah kepala'], 'Heroik paling panjang.', 'Normal 7,5 kepala.'),
        ('Anak usia 1–3 tahun memiliki panjang anatomi…', '4 kali tinggi kepala', ['5 kali tinggi kepala', '6 kali tinggi kepala', '7 kali tinggi kepala'], 'Anak kecil kepalanya relatif besar.', 'Usia 10–13 tahun 7x kepala.'),
        ('Prinsip pengulangan yang tidak tepat menimbulkan efek…', 'statis dan monoton', ['dinamis dan hidup', 'seimbang dan stabil', 'megah dan masif'], 'Perlu variasi agar menarik.', 'Ritme memberi kesan gerak.'),
    ],
    'multi': [
        ('Manakah unsur visual?', ['Titik', 'Garis', 'Bidang'], ['Anggaran', 'Jadwal', 'Kontrak'], 'Unsur visual membentuk karya.', 'Sisanya administrasi.'),
        ('Manakah jenis garis dan maknanya?', ['Vertikal: kokoh', 'Diagonal: dinamis', 'Lengkung: luwes'], ['Bulat: tebal', 'Tipis: mahal', 'Panjang: lambat'], 'Setiap garis bermakna.', 'Makna disesuaikan arah dan bentuk.'),
        ('Manakah prinsip desain?', ['Kesatuan', 'Keseimbangan', 'Kontras'], ['Dubbing', 'Rendering', 'Compositing'], 'Prinsip mengorganisasi unsur visual.', 'Sisanya istilah produksi animasi.'),
        ('Manakah jenis perspektif?', ['Satu titik lenyap', 'Dua titik lenyap', 'Tiga titik lenyap'], ['Empat titik lenyap', 'Perspektif warna', 'Perspektif suara'], 'Perspektif digolongkan jumlah titik lenyap.', 'Tidak ada empat titik lenyap.'),
        ('Manakah kategori warna?', ['Warna primer', 'Warna sekunder', 'Warna tersier'], ['Warna produksi', 'Warna kontrak', 'Warna jadwal'], 'Pengelompokan menurut Brewster.', 'Sisanya bukan kategori warna.'),
        ('Manakah ciri bidang organis?', ['Menyerupai bentuk alam', 'Lengkungan bebas', 'Kesan fleksibel'], ['Terukur sistematis', 'Selalu segi empat', 'Kesan formal'], 'Bidang organis bebas.', 'Geometris yang teratur.'),
        ('Manakah fungsi kontras?', ['Memberi penekanan', 'Menjaga aksesibilitas teks', 'Menghindari kesan monoton'], ['Menghapus warna', 'Menghilangkan bentuk', 'Memperkecil gambar'], 'Kontras menonjolkan dan memudahkan baca.', 'Juga mencegah kebosanan.'),
        ('Manakah proporsi tubuh manusia?', ['Normal 7,5 kepala', 'Ideal 8 kepala', 'Fashion 8,5 kepala'], ['Normal 3 kepala', 'Ideal 4 kepala', 'Fashion 12 kepala'], 'Proporsi diukur dari tinggi kepala.', 'Makin tinggi rasio makin ramping.'),
    ],
    'pairs': [
        ('Titik', 'unsur visual paling dasar'),
        ('Garis semu', 'kesan batas objek'),
        ('Bidang geometris', 'teratur dan formal'),
        ('Ruang negatif', 'ruang kosong sekitar objek'),
        ('Warna primer', 'merah, biru, kuning'),
        ('Kesatuan', 'unsur saling selaras'),
        ('Emphasis', 'pusat perhatian'),
        ('Titik lenyap', 'pusat garis perspektif'),
    ],
    'steps': [
        ('Urutkan unsur visual dari yang paling dasar.', ['Titik', 'Garis', 'Bidang', 'Ruang dan bentuk', 'Warna, tekstur, gelap terang'], 'Titik menjadi awal.', 'Unsur lanjutan menutup rangkaian.'),
        ('Urutkan pembuatan gambar perspektif satu titik lenyap.', ['Menentukan garis cakrawala', 'Menentukan titik lenyap', 'Menarik garis bantu ke titik lenyap', 'Menggambar objek sesuai garis bantu', 'Merapikan dan memberi gelap terang'], 'Cakrawala ditentukan dulu.', 'Gelap terang menyelesaikan gambar.'),
        ('Urutkan langkah mengomposisikan karya visual.', ['Menentukan pusat perhatian', 'Menyusun unsur dengan keseimbangan', 'Menyamakan bentuk dan warna (unity)', 'Memberi kontras yang cukup', 'Memeriksa proporsi keseluruhan'], 'Pusat perhatian ditetapkan dulu.', 'Proporsi memeriksa hasil akhir.'),
        ('Urutkan proporsi tubuh dari yang paling pendek rasionya.', ['Normal 7,5 kepala', 'Ideal 8 kepala', 'Fashion 8,5 kepala', 'Heroik 9 kepala'], 'Normal paling pendek.', 'Heroik paling panjang.'),
        ('Urutkan menggambar anatomi anak dari usia termuda.', ['Usia 1–3 tahun 4x kepala', 'Usia 4–6 tahun 5x kepala', 'Usia 7–9 tahun 6x kepala', 'Usia 10–13 tahun 7x kepala'], 'Anak kecil rasionya paling kecil.', 'Makin besar makin mendekati dewasa.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)