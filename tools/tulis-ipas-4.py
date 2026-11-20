"""IPAS 4 — Membangun Komunikasi dengan Bantuan Teknologi (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    scenario,
    timeline_block,
    write_chapter,
)

CH = {
    'code': 'IPAS 4',
    'slug': 'ipas-4-komunikasi-teknologi',
    'title': 'Membangun Komunikasi dengan Bantuan Teknologi',
    'description': (
        'Menelusuri perkembangan teknologi informasi dan komunikasi, memahami '
        'internet, Internet of Things, dan sensor, serta merancang purwarupa '
        'solusi berbasis TIK sesuai bidang keahlian.'
    ),
    'objectives': [
        'Menjelaskan peranan TIK dalam kehidupan sehari-hari.',
        'Menelusuri perkembangan TIK dari telepon kabel sampai Internet of Things.',
        'Menjelaskan fungsi sensor dan komponen pendukung IoT.',
        'Mengidentifikasi masalah di sekitar yang dapat diselesaikan dengan TIK.',
        'Merancang dan mengevaluasi purwarupa solusi berbasis IoT.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 4 Membangun Komunikasi dengan Bantuan '
        'Teknologi; CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'TIK', 'definition': 'Teknologi informasi dan komunikasi, yaitu perangkat dan sistem untuk mengolah serta menyebarkan informasi.'},
        {'term': 'Internet', 'definition': 'Jaringan komunikasi elektronik yang menghubungkan jaringan komputer di seluruh dunia.'},
        {'term': 'Media sosial', 'definition': 'Platform digital yang memungkinkan pengguna berkomunikasi dan membagikan konten tanpa batas ruang dan waktu.'},
        {'term': 'IoT', 'definition': 'Internet of Things, jaringan kolektif perangkat yang terhubung dan bertukar data melalui internet.'},
        {'term': 'Sensor', 'definition': 'Perangkat yang menerima dan menanggapi sinyal atau stimulus dari lingkungan.'},
        {'term': 'Cloud', 'definition': 'Layanan komputasi yang menyediakan server, penyimpanan, basis data, dan perangkat lunak melalui internet.'},
        {'term': 'Otomasi', 'definition': 'Penggunaan alat, mesin, dan komputer untuk menjalankan pekerjaan dengan sedikit campur tangan manusia.'},
        {'term': 'E-commerce', 'definition': 'Sistem pemasaran dan perdagangan yang berbasis internet.'},
    ],
    'intro': {
        'material_title': 'Mengapa komunikasi berubah cepat?',
        'title': 'Era digital dan peranan TIK',
        'paragraphs': [
            'Telepon rumah, mesin faks, radio, dan televisi tabung pernah menjadi peralatan utama komunikasi. Kini ponsel pintar memuat semuanya sekaligus: pesan, panggilan video, kamera, dan aplikasi kerja.',
            'Teknologi informasi dan komunikasi mempercepat hubungan antarmanusia. Surel (email) sejak 1990-an mengubah cara berkirim pesan, lalu media sosial membuat penyebaran informasi berlangsung dalam hitungan detik.',
            'Perubahan ini juga mengubah perilaku: belajar bisa dilakukan daring, berdagang lewat e-commerce, dan peralatan rumah dapat dikendalikan dari jauh melalui Internet of Things.',
        ],
        'diagram': (
            'Alur kerja perangkat IoT',
            'flowchart LR\n'
            '  A[Sensor membaca kondisi] --> B[Mikrokontroler mengolah data]\n'
            '  B --> C[Data dikirim lewat internet]\n'
            '  C --> D[Cloud menyimpan dan menganalisis]\n'
            '  D --> E[Aplikasi menampilkan informasi]\n'
            '  E --> F[Pengguna mengendalikan perangkat]',
        ),
        'callout': 'Gunakan data pribadi secara bijak: unggahan dan lokasi yang tersebar di internet sulit ditarik kembali.',
        'checkpoint': (
            'Jaringan perangkat yang saling terhubung dan bertukar data melalui internet disebut…',
            [
                ('Internet of Things', True),
                ('e-commerce', False),
                ('cloud storage', False),
                ('media sosial', False),
            ],
            'IoT menghubungkan perangkat agar dapat mengirim data dan menerima perintah melalui internet.',
        ),
    },
    'concept': {
        'material_title': 'Internet, IoT, dan sensor',
        'title': 'Dari internet sampai perangkat yang berpikir',
        'paragraphs': [
            'Internet mendistribusikan informasi dengan cepat antartempat yang berjauhan. Pemanfaatannya mencakup mencari informasi, belajar, mengirim surel, hingga mengunduh musik dan film. Alat pemindai barcode di kasir adalah contoh kecil pemanfaatan data digital.',
            'IoT memperluas manfaat koneksi internet. Lampu menyala saat mendeteksi manusia, komputer menyala ketika pegawai absen, dan lemari pendingin dapat memesan kebutuhan yang habis karena terhubung ke cloud.',
            'Sensor menjadi komponen penting IoT. Ada sensor suhu, cahaya, sentuhan, gerak, kelembapan udara, kelembapan tanah, asap, detak jantung, ultrasonik, hujan, dan aliran air, dipilih sesuai kebutuhan.',
        ],
        'table': [
            ['Komponen', 'Fungsi', 'Contoh penerapan'],
            ['Sensor', 'Mendeteksi kondisi lingkungan', 'Sensor kelembapan tanah di kebun'],
            ['Mikrokontroler', 'Mengolah data sensor dan menjalankan perintah', 'Papan pengendali lampu otomatis'],
            ['Koneksi internet', 'Mengirim data ke server', 'Wi-Fi pada alat penyiram tanaman'],
            ['Cloud', 'Menyimpan dan menganalisis data', 'Riwayat suhu tersimpan daring'],
            ['Aplikasi', 'Menampilkan data dan kendali', 'Dasbor pemantauan di ponsel'],
        ],
        'visual': timeline_block(
            'ipas-4-timeline-tik',
            [
                ('1980-an', 'Telepon kabel dan mesin faks', 'Komunikasi jarak jauh masih memakai kabel dan kertas.'),
                ('1990-an', 'Surel dan ponsel awal', 'Pesan tertulis berpindah secara digital; ponsel mulai dibawa bepergian.'),
                ('2000-an', 'Internet dan media sosial', 'Informasi menyebar cepat melalui laman dan jejaring sosial.'),
                ('2010-an', 'Ponsel pintar', 'Satu perangkat memuat kamera, aplikasi, dan akses internet.'),
                ('2020-an', 'IoT, cloud, dan kecerdasan buatan', 'Perangkat saling terhubung dan mengambil keputusan otomatis.'),
            ],
        ),
        'activity': categorize_block(
            'ipas-4-klasifikasi',
            'Kelompokkan perangkat berikut berdasarkan penggunaan teknologi IoT.',
            [('b1', 'Menggunakan IoT'), ('b2', 'Bukan IoT')],
            [
                ('i1', 'Lampu taman yang menyala saat mendeteksi gerak', 'b1'),
                ('i2', 'Kamera tilang elektronik di perempatan', 'b1'),
                ('i3', 'Penyiram tanaman otomatis dengan sensor kelembapan', 'b1'),
                ('i4', 'Lemari pendingin yang memesan bahan yang habis', 'b1'),
                ('i5', 'Papan tulis whiteboard', 'b2'),
                ('i6', 'Kursi kayu tanpa komponen elektronik', 'b2'),
                ('i7', 'Sepeda ontel tanpa sensor', 'b2'),
                ('i8', 'Mesin ketik manual', 'b2'),
            ],
            'Tepat. Perangkat IoT memakai sensor dan koneksi internet untuk bekerja otomatis.',
            'Periksa lagi: tanpa sensor dan koneksi internet, perangkat bukan bagian dari IoT.',
        ),
        'subtitle': 'Dari masalah menjadi solusi berbasis TIK',
        'list': [
            'Mengidentifikasi masalah di sekolah atau rumah yang penyelesaiannya memerlukan bantuan teknologi.',
            'Memilih solusi yang memiliki nilai kebaruan dan kemanfaatan tinggi, sesuai bidang keahlian.',
            'Membuat desain berskala yang menunjukkan prosedur, alat, bahan, dan model.',
            'Mengevaluasi purwarupa dengan uji coba terukur, misalnya mengukur fungsi sensor dan keluaran alat.',
        ],
        'checkpoint': (
            'Komponen IoT yang berfungsi mendeteksi kondisi lingkungan adalah…',
            [
                ('sensor', True),
                ('baterai', False),
                ('kabel', False),
                ('casing', False),
            ],
            'Sensor menerima dan menanggapi stimulus seperti suhu, cahaya, gerak, atau kelembapan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Projek TIK: dari masalah ke purwarupa',
        'paragraphs': [
            'Contoh masalah nyata: sekolah berarea luas dengan banyak lampu sehingga petugas harus menyalakan dan mematikannya. Solusinya, instalasi lampu otomatis memakai sensor cahaya dan gerak.',
            'Pada bidang pertanian, sensor suhu, kelembapan, dan kamera mengirim data ke perangkat lunak sehingga petani dapat menentukan kapan menyiram, memupuk, atau memanen tanpa harus mendatangi setiap petak.',
            'Setelah purwarupa dibuat, lakukan uji coba dan catat variabel yang terukur. Hasil evaluasi dipakai menyusun rencana tindak lanjut: memperbaiki desain, mengembangkan produksi, atau mensosialisasikan produk.',
        ],
        'scenario': scenario(
            'ipas-4-skenario',
            'Lampu kelas yang terus menyala',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Lampu di sekolah sering menyala meski ruang kosong. Apa langkah awal projekmu?',
                    'choices': [
                        {'text': 'Mencatat masalah dan mengukur pemakaian lampu', 'next': 'n2', 'score': 2, 'feedback': 'Data pemakaian membantu memilih solusi yang tepat.'},
                        {'text': 'Mengganti semua lampu tanpa perhitungan', 'next': 'n3', 'score': 0, 'feedback': 'Penggantian tanpa data bisa memboroskan biaya.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Hasil pengukuran menunjukkan lampu menyala 4 jam tanpa pengguna. Solusi apa yang dipilih?',
                    'choices': [
                        {'text': 'Sensor gerak dan cahaya yang mematikan lampu otomatis', 'next': 'n4', 'score': 2, 'feedback': 'Sensor langsung mengatasi penyebab pemborosan.'},
                        {'text': 'Menambah poster imbauan hemat listrik', 'next': 'n3', 'score': 0, 'feedback': 'Imbauan tidak selalu diikuti, sedangkan sensor bekerja otomatis.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pemborosan listrik berlanjut karena solusi tidak menyentuh penyebabnya.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Lampu hanya menyala saat diperlukan sehingga tagihan listrik turun.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu IoT?', 'back': 'Jaringan perangkat terhubung yang bertukar data lewat internet.'},
            {'front': 'Sebutkan tiga jenis sensor.', 'back': 'Sensor suhu, kelembapan tanah, dan gerak.'},
            {'front': 'Apa fungsi cloud pada IoT?', 'back': 'Menyimpan dan mengolah data dari perangkat.'},
            {'front': 'Apa itu otomasi?', 'back': 'Pekerjaan dijalankan mesin dan komputer dengan sedikit campur tangan manusia.'},
        ],
        'checkpoint': (
            'Langkah pertama menyusun projek berbasis TIK adalah…',
            [
                ('mengidentifikasi masalah dan kebutuhan', True),
                ('membeli komponen termahal', False),
                ('membuat video promosi', False),
                ('menghitung keuntungan penjualan', False),
            ],
            'Projek dimulai dari masalah yang teridentifikasi, lalu kebutuhan, solusi, desain, dan purwarupa.',
        ),
        'challenge': challenge_block(
            'ipas-4-tantangan',
            'Tantangan istilah teknologi komunikasi',
            90,
            [
                ('Jaringan perangkat terhubung', 'IoT'),
                ('Alat pendeteksi stimulus', 'Sensor'),
                ('Penyimpanan dan layanan lewat internet', 'Cloud'),
                ('Surat elektronik', 'Email'),
                ('Perdagangan berbasis internet', 'E-commerce'),
            ],
            'Lima istilah teknologi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa kepanjangan TIK?', 'teknologi informasi dan komunikasi', ['teknik industri kreatif', 'teknologi industri kimia', 'tata informasi komputer'], 'TIK atau ICT adalah teknologi informasi dan komunikasi.', 'Berhubungan dengan pengolahan dan penyebaran informasi.'),
        ('Jaringan komunikasi elektronik yang menghubungkan komputer di seluruh dunia disebut…', 'internet', ['intranet', 'bluetooth', 'hotspot'], 'Internet menghubungkan jaringan komputer di seluruh dunia.', 'Awalan inter berarti antar.'),
        ('Sejak dekade apa surel mengubah cara berkomunikasi?', '1990-an', ['1970-an', '2005-an', '2015-an'], 'Surel mengubah cara berinteraksi sejak 1990-an.', 'Sezaman dengan ponsel awal.'),
        ('Platform digital untuk berkomunikasi dan membagikan konten disebut…', 'media sosial', ['mesin pencari', 'sistem operasi', 'peramban'], 'Media sosial memungkinkan interaksi tanpa batas ruang dan waktu.', 'Contohnya Instagram, Facebook, dan Twitter.'),
        ('Apa itu IoT?', 'jaringan perangkat terhubung yang bertukar data lewat internet', ['aplikasi pengolah kata', 'jenis kabel jaringan', 'perangkat penyimpanan luar'], 'IoT memperluas manfaat koneksi internet ke berbagai perangkat.', 'Perangkat bekerja otomatis sesuai program.'),
        ('Perangkat yang menerima dan menanggapi stimulus disebut…', 'sensor', ['aktuator', 'router', 'server'], 'Sensor mendeteksi perubahan seperti suhu, gerak, atau kelembapan.', 'Menjadi mata dan telinga perangkat IoT.'),
        ('Alat pemindai di kasir supermarket membaca…', 'barcode', ['sidik jari', 'suara', 'wajah'], 'Barcode berisi data optik berupa garis dengan ketebalan berbeda.', 'Tertera pada kemasan barang.'),
        ('Layanan komputasi penyedia server dan penyimpanan lewat internet disebut…', 'cloud', ['hard disk', 'flashdisk', 'komputer desktop'], 'Cloud menyediakan server, media penyimpanan, basis data, dan perangkat lunak.', 'Data diakses tanpa perangkat penyimpanan lokal.'),
        ('Kamera di perempatan yang memotret pelanggar lalu lintas memanfaatkan…', 'IoT', ['radio analog', 'mesin faks', 'telepon kabel'], 'Kamera tilang elektronik terhubung jaringan dan mengenali pelanggaran.', 'Termasuk penerapan IoT di bidang transportasi.'),
        ('Penerapan IoT di bidang pertanian memungkinkan petani…', 'memantau kelembapan, suhu, dan keasaman tanah dari jauh', ['membajak sawah tanpa alat', 'menghapus kebutuhan air', 'menanam tanpa benih'], 'Sensor dan kamera mengirim data sehingga petani dapat memantau dari jarak jauh.', 'Data dikirim melalui internet ke perangkat lunak.'),
        ('Apa fungsi mikrokontroler pada perangkat IoT?', 'mengolah data sensor dan menjalankan perintah', ['menyimpan video berdurasi panjang', 'mencetak dokumen', 'menampilkan iklan'], 'Mikrokontroler menjadi pengolah data dan pengendali kerja perangkat.', 'Berada di antara sensor dan koneksi internet.'),
        ('Contoh otomasi di rumah adalah…', 'lampu menyala saat mendeteksi manusia', ['menyapu lantai dengan sapu', 'mencuci piring manual', 'membuka jendela dengan tangan'], 'Otomasi menjalankan pekerjaan dengan sedikit campur tangan manusia.', 'Sensor menjadi pemicunya.'),
        ('Aplikasi yang memfasilitasi banyak penjual dalam satu platform disebut…', 'marketplace', ['mesin pencari', 'surel', 'sistem operasi'], 'Marketplace menyediakan fasilitas berbelanja dari banyak penjual.', 'Berbeda dari toko daring tunggal.'),
        ('Tujuan utama membuat desain purwarupa berskala adalah…', 'memastikan ukuran produk sesuai rencana', ['memperindah laporan', 'menambah biaya', 'mempercepat pemasaran'], 'Desain berskala menunjukkan perbandingan ukuran gambar dengan produk asli.', 'Skala membantu menghitung bahan.'),
    ],
    'multi': [
        ('Manakah contoh penerapan IoT?', ['Lampu otomatis dengan sensor gerak', 'Kamera tilang elektronik', 'Lemari pendingin yang memesan bahan'], ['Papan tulis whiteboard', 'Kursi kayu'], 'Perangkat IoT memakai sensor dan koneksi internet.', 'Perabot tanpa elektronik bukan IoT.'),
        ('Manakah termasuk media sosial?', ['Instagram', 'Facebook', 'Twitter'], ['Kalkulator', 'Mesin faks'], 'Ketiganya platform komunikasi dan berbagi konten.', 'Media sosial berbasis internet.'),
        ('Manakah pemanfaatan internet dalam kehidupan sehari-hari?', ['Mencari informasi kesehatan', 'Mengirim surel', 'Belajar daring'], ['Menanam padi tanpa air', 'Membuat kayu dari plastik'], 'Internet memudahkan akses informasi dan komunikasi.', 'Semua berkaitan dengan pertukaran data.'),
        ('Manakah jenis sensor yang disebut dalam buku?', ['Sensor suhu', 'Sensor kelembapan tanah', 'Sensor asap'], ['Sensor rasa', 'Sensor warna rambut'], 'Buku menyebut sensor suhu, kelembapan, asap, gerak, dan lainnya.', 'Sensor dipilih sesuai kebutuhan.'),
        ('Manakah manfaat IoT di bidang pertanian?', ['Memantau suhu dan kelembapan dari jauh', 'Menentukan waktu menyiram', 'Mengenali jenis hama'], ['Menghapus kebutuhan benih', 'Menggantikan tanah sepenuhnya'], 'Data sensor membantu keputusan perawatan tanaman.', 'Semua berkaitan dengan pemantauan.'),
        ('Manakah komponen pendukung kerja IoT?', ['Sensor', 'Koneksi internet', 'Cloud'], ['Mesin ketik', 'Papan pengumuman'], 'IoT memerlukan sensor, koneksi, dan layanan pengolahan data.', 'Tanpa koneksi, data tidak terkirim.'),
        ('Manakah tahap projek solusi berbasis TIK?', ['Mengidentifikasi masalah', 'Memilih solusi dan merancang desain', 'Membuat purwarupa'], ['Menghindari evaluasi', 'Menutup projek tanpa laporan'], 'Tahapan projek berjalan dari masalah sampai purwarupa dan tindak lanjut.', 'Evaluasi tetap diperlukan.'),
        ('Manakah rencana tindak lanjut projek TIK?', ['Mendesain ulang produk yang belum sesuai', 'Mengembangkan produksi', 'Mensosialisasikan produk'], ['Membuang data uji coba', 'Menghentikan perawatan alat'], 'RTL menyempurnakan produk dan menyebarkan manfaatnya.', 'Semua bertujuan keberlanjutan projek.'),
    ],
    'pairs': [
        ('Internet', 'jaringan komputer seluruh dunia'),
        ('IoT', 'perangkat terhubung yang bertukar data'),
        ('Sensor', 'pendeteksi stimulus lingkungan'),
        ('Cloud', 'layanan penyimpanan dan komputasi daring'),
        ('Otomasi', 'kerja mesin dengan sedikit campur tangan manusia'),
        ('E-commerce', 'perdagangan berbasis internet'),
        ('Media sosial', 'platform berbagi konten dan interaksi'),
        ('Barcode', 'data optik pada kemasan barang'),
    ],
    'steps': [
        ('Urutkan alur kerja perangkat IoT.', ['Sensor membaca kondisi', 'Mikrokontroler mengolah data', 'Data dikirim melalui internet', 'Cloud menganalisis data', 'Aplikasi menampilkan informasi'], 'Alur bergerak dari pembacaan sensor sampai tampilan aplikasi.', 'Data diolah sebelum dikirim.'),
        ('Urutkan tahap projek solusi berbasis TIK.', ['Mengidentifikasi masalah', 'Memilih solusi dan merancang desain', 'Membuat purwarupa', 'Mengevaluasi purwarupa', 'Menyusun rencana tindak lanjut'], 'Projek dimulai dari masalah sampai tindak lanjut.', 'Evaluasi sebelum tindak lanjut.'),
        ('Urutkan langkah uji coba purwarupa IoT.', ['Menyiapkan alat ukur', 'Mengoperasikan purwarupa', 'Mencatat variabel terukur', 'Membandingkan dengan kriteria', 'Memperbaiki bagian yang gagal'], 'Uji coba mencatat data lalu membandingkannya dengan kriteria.', 'Perbaikan mengikuti hasil perbandingan.'),
        ('Urutkan langkah membuat desain purwarupa.', ['Mencari referensi prosedur dan bahan', 'Menyiapkan alat gambar', 'Menggambar desain berskala', 'Menentukan variabel yang memengaruhi'], 'Desain dibuat setelah referensi dan alat siap, lalu variabel diidentifikasi.', 'Variabel membantu memahami faktor keberhasilan.'),
        ('Urutkan langkah menelusuri perubahan teknologi komunikasi.', ['Telepon kabel dan faks', 'Surel dan ponsel awal', 'Internet dan media sosial', 'Ponsel pintar', 'IoT dan kecerdasan buatan'], 'Perubahan teknologi bergerak dari kabel, surel, media sosial, ponsel pintar, sampai IoT.', 'Setiap tahap mempercepat komunikasi.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
