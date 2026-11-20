"""TJKT 5 — Alat Ukur dan Pengukuran (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 5',
    'slug': 'tjkt-5-alat-ukur-pengukuran',
    'title': 'Alat Ukur dan Pengukuran Teknik Jaringan Akses Telekomunikasi',
    'description': (
        'Mengenali fungsi alat ukur jaringan dan telekomunikasi, memilih alat '
        'ukur yang tepat untuk setiap masalah, menggunakan alat ukur dengan '
        'benar, serta memeliharanya agar tetap akurat.'
    ),
    'objectives': [
        'Menjelaskan fungsi berbagai alat ukur jaringan komputer dan telekomunikasi.',
        'Menganalisis penggunaan alat ukur yang tepat sesuai masalah jaringan.',
        'Menggunakan alat ukur sesuai prosedur untuk pekerjaan jaringan.',
        'Melakukan pemeliharaan preventif, korektif, dan kualitatif alat ukur.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 5; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'LAN tester', 'definition': 'Alat untuk mengecek koneksi kabel LAN RJ45 dan RJ11, termasuk kabel cross dan straight.'},
        {'term': 'Multimeter', 'definition': 'Alat ukur tegangan listrik, arus, dan hambatan; ada tipe analog dan digital.'},
        {'term': 'Earth tester', 'definition': 'Alat untuk mengukur nilai instalasi grounding pada gedung dan perangkat elektronik.'},
        {'term': 'OPM', 'definition': 'Optical Power Meter, alat untuk mengetahui level daya sinyal optik pada serat optik.'},
        {'term': 'OTDR', 'definition': 'Optical Time Domain Reflectometer, mengukur redaman dan letak gangguan saluran optik.'},
        {'term': 'Redaman', 'definition': 'Selisih daya pada saluran optik yang menunjukkan kekuatan sinyal yang hilang.'},
        {'term': 'Speed test', 'definition': 'Aplikasi untuk menguji kecepatan koneksi internet pada pengunggahan dan pengunduhan.'},
        {'term': 'Ping', 'definition': 'Packet Internet Network Groper, perintah menguji kecepatan koneksi dan respons host.'},
        {'term': 'Wi-Fi analyzer', 'definition': 'Aplikasi untuk mengetahui kekuatan sinyal Wi-Fi pada suatu lokasi.'},
        {'term': 'Kalibrasi', 'definition': 'Penyesuaian alat ukur agar hasil pengukurannya tepat dan teliti.'},
    ],
    'intro': {
        'material_title': 'Mengapa alat ukur penting?',
        'title': 'Menjaga media transmisi tetap prima',
        'paragraphs': [
            'Infrastruktur jaringan komputer dan telekomunikasi harus selalu dalam kondisi prima. Pengecekan berkala membutuhkan alat ukur, baik perangkat keras seperti multimeter dan LAN tester, maupun perangkat lunak seperti speed test dan Wi-Fi analyzer.',
            'Pemeliharaan berkala dapat mendeteksi gangguan sejak awal sehingga tidak menjadi gangguan yang bersifat mayor.',
            'Sebelum menggunakan alat ukur, pahami dulu fungsinya agar tidak salah penggunaan. Pemilihan alat yang sesuai memberikan hasil pembacaan maksimal.',
        ],
        'diagram': (
            'Alat ukur jaringan dan fungsinya',
            'flowchart LR\n'
            '  A[Alat ukur] --> B[LAN tester: cek kabel LAN]\n'
            '  A --> C[Multimeter: tegangan, arus, hambatan]\n'
            '  A --> D[Earth tester: nilai grounding]\n'
            '  A --> E[OPM: level daya optik]\n'
            '  A --> F[OTDR: redaman dan gangguan optik]\n'
            '  A --> G[Speed test dan Wi-Fi analyzer]',
        ),
        'callout': 'Peralatan yang selalu siap pakai akan menjaga produktivitas pekerjaan jaringan.',
        'checkpoint': (
            'Alat yang berfungsi mengecek koneksi kabel LAN RJ45 adalah…',
            [
                ('LAN tester', True),
                ('OTDR', False),
                ('speed test', False),
                ('Wi-Fi analyzer', False),
            ],
            'LAN tester memeriksa kabel LAN, termasuk jenis cross dan straight.',
        ),
    },
    'concept': {
        'material_title': 'Mengenal fungsi alat ukur',
        'title': 'Dari multimeter sampai OTDR',
        'paragraphs': [
            'Multimeter mengukur tegangan, arus, dan hambatan listrik. Multimeter analog memakai jarum penunjuk dan dihitung manual, sedangkan multimeter digital langsung menampilkan angka di layar.',
            'Earth tester mengukur nilai instalasi grounding. OPM mengukur level daya sinyal optik dengan satuan dBm, sedangkan OTDR menampilkan visualisasi redaman optik sepanjang saluran dengan sumbu X jarak dan sumbu Y level daya.',
            'Speed test mengukur kecepatan koneksi internet, Wi-Fi analyzer mengukur kekuatan sinyal Wi-Fi, dan ping mengukur seberapa cepat host merespons sebagai petunjuk kendala jaringan.',
        ],
        'table': [
            ['Alat ukur', 'Fungsi utama', 'Jenis'],
            ['LAN tester', 'Cek kontinuitas kabel LAN', 'Hardware'],
            ['Multimeter', 'Tegangan, arus, hambatan', 'Hardware'],
            ['Earth tester', 'Nilai grounding', 'Hardware'],
            ['OPM', 'Level daya optik (dBm)', 'Hardware'],
            ['OTDR', 'Redaman dan letak gangguan optik', 'Hardware'],
            ['Speed test', 'Kecepatan koneksi internet', 'Software'],
            ['Ping', 'Respons host', 'Software'],
            ['Wi-Fi analyzer', 'Kekuatan sinyal Wi-Fi', 'Software'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-5-redaman',
            'engine': 'mermaid',
            'title': 'Redaman pada saluran optik',
            'code': 'flowchart LR\n'
                    '  A[Sumber optik LED/LASER] --> B[Saluran fiber optik]\n'
                    '  B --> C[Redaman sepanjang saluran]\n'
                    '  C --> D[Sinyal diterima]\n'
                    '  D --> E[Level daya dBm dikur OPM/OTDR]\n'
                    '  E --> F{Sesuai standar?}\n'
                    '  F -- Tidak --> G[Perbaikan sambungan]\n'
                    '  F -- Ya --> H[Saluran prima]',
        },
        'activity': categorize_block(
            'tjkt-5-klasifikasi',
            'Kelompokkan alat berikut ke dalam alat ukur perangkat keras atau perangkat lunak.',
            [('b1', 'Perangkat keras'), ('b2', 'Perangkat lunak')],
            [
                ('i1', 'LAN tester', 'b1'),
                ('i2', 'Speed test', 'b2'),
                ('i3', 'Multimeter digital', 'b1'),
                ('i4', 'Wi-Fi analyzer', 'b2'),
                ('i5', 'Earth tester', 'b1'),
                ('i6', 'Aplikasi ping', 'b2'),
                ('i7', 'OTDR', 'b1'),
                ('i8', 'OPM', 'b1'),
            ],
            'Tepat. Perangkat keras berupa alat fisik; perangkat lunak berupa aplikasi.',
            'Periksa lagi: speed test dan Wi-Fi analyzer adalah aplikasi.',
        ),
        'subtitle': 'Memilih alat ukur yang tepat',
        'list': [
            'Pemilihan alat ukur mengikuti jenis masalah: kabel tembaga dicek dengan LAN tester, saluran optik dengan OPM atau OTDR.',
            'Tegangan listrik pada stopkontak diukur dengan multimeter sesuai batas ukur yang benar.',
            'Spesifikasi alat seperti panjang kabel maksimal dan panjang gelombang menentukan kesesuaian alat.',
            'Hasil pengukuran yang akurat menjadi dasar laporan tanggung jawab kepada perusahaan.',
        ],
        'checkpoint': (
            'Satuan level daya pada sistem komunikasi serat optik adalah…',
            [
                ('dBm', True),
                ('meter', False),
                ('volt', False),
                ('ohm', False),
            ],
            'Level daya optik diukur dalam dBm (desibel miliwatt).',
        ),
    },
    'practice': {
        'material_title': 'Menggunakan dan merawat alat ukur',
        'title': 'Prosedur pengukuran dan pemeliharaan',
        'paragraphs': [
            'Pemeliharaan alat ukur dibedakan menjadi tiga: preventif (sebelum rusak, berkala), korektif (sesudah gangguan), dan kualitatif (meningkatkan kualitas hasil, misalnya memperbarui perangkat lunak OTDR).',
            'Simpan alat ukur di tempat yang tepat: matikan sakelar pemilih multimeter sebelum disimpan, hindari suhu ekstrem, kelembapan tinggi, medan magnet kuat, dan getaran berlebihan.',
            'Sebelum digunakan, periksa kondisi probe dan pastikan kabel tidak terkelupas, serta pastikan kalibrasi alat sudah dilakukan dengan benar. Cermat saat mengukur tegangan dan arus listrik.',
        ],
        'scenario': scenario(
            'tjkt-5-skenario',
            'Internet lemot tapi sinyal penuh',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Pelanggan mengeluh internet lemot padahal sinyal Wi-Fi penuh. Langkah pertama?',
                    'choices': [
                        {'text': 'Menjalankan speed test dan ping untuk memeriksa bandwidth dan respons', 'next': 'n2', 'score': 2, 'feedback': 'Speed test dan ping mengukur kualitas koneksi sebenarnya.'},
                        {'text': 'Langsung mengganti semua perangkat', 'next': 'n3', 'score': 0, 'feedback': 'Mengganti tanpa pengukuran boros dan tidak pasti.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Ping menunjukkan respons lambat dan banyak paket hilang. Apa kecurigaanmu?',
                    'choices': [
                        {'text': 'Memeriksa kabel dan perangkat jaringan dengan LAN tester', 'next': 'n4', 'score': 2, 'feedback': 'Kabel rusak atau koneksi longgar dapat dideteksi LAN tester.'},
                        {'text': 'Menyalahkan kecepatan paket internet pelanggan', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa data tidak bisa menyimpulkan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Masalah tidak selesai dan pelanggan kecewa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Masalah ditemukan dan jaringan normal kembali.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa fungsi LAN tester?', 'back': 'Mengecek koneksi kabel LAN RJ45 dan RJ11.'},
            {'front': 'Apa perbedaan multimeter analog dan digital?', 'back': 'Analog memakai jarum dan dihitung manual; digital langsung menampilkan angka.'},
            {'front': 'Apa fungsi OTDR?', 'back': 'Mengukur redaman dan letak gangguan saluran optik.'},
            {'front': 'Sebutkan tiga jenis pemeliharaan alat ukur.', 'back': 'Preventif, korektif, dan kualitatif.'},
        ],
        'checkpoint': (
            'Pemeliharaan yang dilakukan sebelum kerusakan terjadi disebut…',
            [
                ('preventif', True),
                ('korektif', False),
                ('kualitatif', False),
                ('reduktif', False),
            ],
            'Preventif dilakukan berkala sebelum rusak, misalnya mingguan atau bulanan.',
        ),
        'challenge': challenge_block(
            'tjkt-5-tantangan',
            'Tantangan istilah alat ukur',
            90,
            [
                ('Cek kabel LAN', 'LAN tester'),
                ('Tegangan, arus, hambatan', 'Multimeter'),
                ('Level daya optik', 'OPM'),
                ('Redaman saluran optik', 'OTDR'),
                ('Kecepatan koneksi internet', 'Speed test'),
            ],
            'Lima istilah alat ukur terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Alat yang berfungsi mengecek koneksi kabel LAN RJ45 dan RJ11 adalah…', 'LAN tester', ['OTDR', 'OPM', 'speed test'], 'LAN tester memeriksa kabel cross dan straight.', 'Dapat dilengkapi tone checker.'),
        ('Multimeter digunakan untuk mengukur besaran…', 'tegangan, arus, dan hambatan listrik', ['kecepatan internet', 'suhu udara', 'kekuatan sinyal Wi-Fi'], 'Multimeter umum dipakai dalam elektronika.', 'Ada tipe analog dan digital.'),
        ('Multimeter yang memakai jarum penunjuk dan perhitungan manual adalah…', 'multimeter analog', ['multimeter digital', 'OPM', 'speed test'], 'Analog memakai meter berjarum.', 'Digital langsung menampilkan angka.'),
        ('Alat untuk mengukur nilai instalasi grounding disebut…', 'earth tester', ['LAN tester', 'OTDR', 'ping'], 'Grounding dipasang di gedung dan perangkat elektronik.', 'Menunjukkan keamanan instalasi.'),
        ('Satuan level daya pada sistem komunikasi serat optik adalah…', 'dBm', ['volt', 'hertz', 'byte'], 'dBm adalah desibel miliwatt.', 'Dipakai pada OPM.'),
        ('Alat yang memvisualkan redaman optik sepanjang saluran adalah…', 'OTDR', ['LAN tester', 'earth tester', 'multimeter'], 'OTDR menampilkan jarak pada sumbu X dan level daya pada sumbu Y.', 'Bisa mengukur dari satu ujung.'),
        ('Redaman pada saluran optik berarti…', 'selisih daya sinyal optik', ['panjang kabel', 'suhu kabel', 'warna kabel'], 'Redaman menunjukkan kekuatan sinyal yang hilang.', 'Diukur sepanjang saluran.'),
        ('Perintah ping digunakan untuk…', 'menguji kecepatan koneksi dan respons host', ['mencari alamat Wi-Fi', 'mengukur tegangan', 'menguji grounding'], 'Ping singkatan Packet Internet Network Groper.', 'Bisa dilakukan tanpa internet.'),
        ('Aplikasi untuk mengukur kecepatan koneksi internet adalah…', 'speed test', ['Wi-Fi analyzer', 'LAN tester', 'earth tester'], 'Speed test menguji unggah dan unduh.', 'Mengetahui besarnya bandwidth.'),
        ('Aplikasi untuk mengetahui kekuatan sinyal Wi-Fi disebut…', 'Wi-Fi analyzer', ['speed test', 'OTDR', 'OPM'], 'Wi-Fi analyzer memeriksa kualitas jaringan nirkabel.', 'Dapat diunduh di ponsel.'),
        ('Pemeliharaan yang dilakukan sebelum kerusakan terjadi disebut…', 'preventif', ['korektif', 'kualitatif', 'reduktif'], 'Preventif dilakukan berkala.', 'Mingguan, bulanan, atau tahunan.'),
        ('Pemeliharaan setelah muncul gangguan pada alat ukur disebut…', 'korektif', ['preventif', 'kualitatif', 'proaktif'], 'Korektif memperbaiki alat yang rusak.', 'Segera diperbaiki bila diperlukan.'),
        ('Memperbarui perangkat lunak OTDR termasuk pemeliharaan…', 'kualitatif', ['preventif', 'korektif', 'harian'], 'Kualitatif meningkatkan kualitas hasil pengukuran.', 'Misalnya update software.'),
        ('Saat menyimpan multimeter, yang harus dilakukan adalah…', 'mematikan sakelar pemilih', ['mencabut baterai', 'memasang probe', 'menyimpan di tempat basah'], 'Mematikan sakelar menjaga alat.', 'Hindari suhu ekstrem dan kelembapan tinggi.'),
    ],
    'multi': [
        ('Manakah alat ukur perangkat keras?', ['LAN tester', 'Multimeter', 'OTDR'], ['Speed test', 'Wi-Fi analyzer'], 'Ketiganya alat fisik.', 'Dua lainnya aplikasi.'),
        ('Manakah alat ukur perangkat lunak?', ['Speed test', 'Wi-Fi analyzer', 'Aplikasi ping'], ['Earth tester', 'OPM'], 'Ketiganya berbentuk aplikasi.', 'Earth tester dan OPM adalah alat fisik.'),
        ('Manakah fungsi multimeter?', ['Mengukur tegangan', 'Mengukur arus', 'Mengukur hambatan'], ['Mengukur kecepatan internet', 'Mencari sinyal Wi-Fi'], 'Multimeter mengukur besaran listrik.', 'Bukan soal jaringan nirkabel.'),
        ('Manakah kegunaan OTDR?', ['Mengukur redaman optik', 'Menangani gangguan fiber', 'Mengukur panjang saluran optik'], ['Mengukur grounding', 'Mengecek kabel UTP'], 'OTDR bekerja pada saluran optik.', 'Kabel UTP urusan LAN tester.'),
        ('Manakah fungsi speed test?', ['Mengetahui bandwidth', 'Mengukur kecepatan unggah', 'Mengukur kecepatan unduh'], ['Mengukur nilai grounding', 'Mengecek kabel'], 'Speed test menguji koneksi internet.', 'Grounding urusan earth tester.'),
        ('Manakah cara pemeliharaan preventif?', ['Pengecekan berkala', 'Membersihkan alat', 'Menyimpan di tempat kering'], ['Menunggu alat rusak dulu', 'Membiarkan probe terkelupas'], 'Pencegahan dilakukan teratur.', 'Menunggu rusak adalah korektif.'),
        ('Manakah sikap kerja yang benar saat mengukur?', ['Cermat saat mengukur listrik', 'Mengecek kondisi probe', 'Memastikan kalibrasi benar'], ['Menyentuh bagian bertegangan', 'Memakai probe terkelupas'], 'Keamanan menjaga alat dan diri.', 'Probe rusak berbahaya.'),
        ('Manakah informasi spesifikasi alat ukur?', ['Panjang kabel maksimal', 'Kompatibilitas konektor', 'Catu daya baterai'], ['Warna kemasan', 'Harga jual'], 'Spesifikasi menentukan kesesuaian alat.', 'Warna dan harga bukan spesifikasi teknis.'),
    ],
    'pairs': [
        ('LAN tester', 'cek kabel LAN'),
        ('Multimeter', 'tegangan, arus, hambatan'),
        ('Earth tester', 'nilai grounding'),
        ('OPM', 'level daya optik'),
        ('OTDR', 'redaman saluran optik'),
        ('Speed test', 'kecepatan internet'),
        ('Ping', 'respons host'),
        ('Kalibrasi', 'penyesuaian ketepatan alat'),
    ],
    'steps': [
        ('Urutkan pemeriksaan masalah internet lemot.', ['Menjalankan speed test', 'Melakukan ping ke host', 'Memeriksa kabel dengan LAN tester', 'Menemukan sumber masalah', 'Memperbaiki dan menguji ulang'], 'Pemeriksaan dimulai dari perangkat lunak.', 'Pengujian ulang menutup perbaikan.'),
        ('Urutkan penggunaan multimeter digital mengukur tegangan.', ['Mengetahui batas ukur', 'Menetapkan selektor pada posisi tegangan', 'Menempelkan probe ke titik ukur', 'Membaca nilai di layar', 'Mematikan sakelar setelah selesai'], 'Pengukuran dimulai dengan pengaturan selektor.', 'Mematikan sakelar menjaga alat.'),
        ('Urutkan pengukuran saluran optik dengan OPM.', ['Menyiapkan OPM dan konektor', 'Memilih panjang gelombang', 'Menghubungkan ke saluran aktif', 'Membaca level daya dalam dBm', 'Membandingkan dengan standar'], 'Pengukuran dimulai dari persiapan.', 'Perbandingan dengan standar menutup.'),
        ('Urutkan pemeliharaan preventif alat ukur.', ['Memeriksa kondisi fisik', 'Membersihkan alat dan probe', 'Memeriksa kalibrasi', 'Menyimpan di tempat kering', 'Mencatat jadwal perawatan'], 'Perawatan dimulai dari pemeriksaan.', 'Pencatatan menjaga rutinitas.'),
        ('Urutkan langkah memilih alat ukur yang tepat.', ['Mengidentifikasi masalah jaringan', 'Menentukan besaran yang diukur', 'Mencocokkan dengan fungsi alat', 'Memeriksa spesifikasi alat', 'Melakukan pengukuran'], 'Pemilihan berawal dari masalah.', 'Pengukuran menutup proses.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)