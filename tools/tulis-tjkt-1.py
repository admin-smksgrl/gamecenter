"""TJKT 1 — Proses Bisnis di Bidang TJKT (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 1',
    'slug': 'tjkt-1-proses-bisnis',
    'title': 'Proses Bisnis di Bidang Teknik Jaringan Komputer dan Telekomunikasi',
    'description': (
        'Memahami proses bisnis pelaku usaha perorangan dan organisasi, '
        'menganalisis kebutuhan pengguna dalam perencanaan jaringan, dan '
        'mengimplementasikan perencanaan jaringan sesuai proses bisnis perusahaan.'
    ),
    'objectives': [
        'Menjelaskan pengertian proses bisnis dan aktivitas utama (core business) pelaku usaha.',
        'Membandingkan proses bisnis pelaku usaha perorangan dan organisasi.',
        'Menganalisis kebutuhan pengguna dalam perencanaan jaringan komputer dan telekomunikasi.',
        'Mengimplementasikan perencanaan jaringan berdasarkan proses bisnis perusahaan.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 1; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'Proses bisnis', 'definition': 'Rangkaian tahapan kegiatan terstruktur yang menghasilkan barang atau jasa dengan tujuan ekonomi.'},
        {'term': 'Core business', 'definition': 'Aktivitas utama bisnis yang menjadi sumber utama nilai dan pendapatan perusahaan.'},
        {'term': 'Analisis kebutuhan', 'definition': 'Kajian terhadap kebutuhan pengguna seperti jumlah pengguna, perangkat, dan layanan jaringan.'},
        {'term': 'Grup kerja', 'definition': 'Kelompok dalam organisasi dengan fungsi dan tanggung jawab yang terbagi terstruktur.'},
        {'term': 'ISP', 'definition': 'Penyedia layanan internet (Internet Service Provider) yang menghubungkan pelanggan ke internet.'},
        {'term': 'Jaringan komputer', 'definition': 'Kumpulan perangkat yang saling terhubung untuk berbagi sumber daya dan data.'},
        {'term': 'Media koneksi', 'definition': 'Sarana penghubung antarderangkat jaringan, seperti kabel tembaga, serat optik, atau nirkabel.'},
        {'term': 'Pengalamatan IP', 'definition': 'Pemberian alamat unik pada perangkat agar dapat berkomunikasi dalam jaringan.'},
        {'term': 'Firewall', 'definition': 'Sistem keamanan yang mengatur izin lalu lintas data masuk dan keluar jaringan.'},
    ],
    'intro': {
        'material_title': 'Apa itu proses bisnis?',
        'title': 'Tahapan terstruktur menuju tujuan ekonomi',
        'paragraphs': [
            'Di pasar, kamu dapat melihat manusia berusaha memenuhi kebutuhan hidupnya. Usaha itu tersusun dalam tahapan: memperoleh bahan, mengolah, menjual, hingga menghasilkan pendapatan.',
            'Proses bisnis adalah serangkaian tahapan kegiatan terstruktur yang menghasilkan barang atau jasa sebagai tujuan ekonomi. Setiap tahap memiliki peran dan pengaruh terhadap tahap berikutnya.',
            'Pelaku usaha dapat dijalankan perorangan ataupun organisasi. Ketika usaha berkembang, pembagian tugas menjadi semakin terstruktur dengan grup kerja yang memiliki fungsi dan tanggung jawab masing-masing.',
        ],
        'diagram': (
            'Alur proses bisnis sederhana',
            'flowchart LR\n'
            '  A[Bahan dan modal] --> B[Produksi / pengolahan]\n'
            '  B --> C[Kualitas dan kemasan]\n'
            '  C --> D[Pemasaran dan penjualan]\n'
            '  D --> E[Pendapatan dan keuangan]\n'
            '  E --> A',
        ),
        'callout': 'Bagi teknisi jaringan, memahami proses bisnis penting karena jaringan yang dibangun harus mendukung alur kerja dan target perusahaan.',
        'checkpoint': (
            'Aktivitas utama bisnis yang menjadi sumber nilai perusahaan disebut…',
            [
                ('core business', True),
                ('firewall', False),
                ('grup kerja', False),
                ('pengalamatan IP', False),
            ],
            'Core business adalah aktivitas utama yang menghasilkan nilai dan pendapatan.',
        ),
    },
    'concept': {
        'material_title': 'Dari perorangan ke organisasi',
        'title': 'Perubahan proses bisnis saat usaha berkembang',
        'paragraphs': [
            'Pelaku usaha perorangan mengerjakan seluruh tahap sendiri: membeli bahan, membuat, menjual, dan mengelola uang. Skalanya kecil dan keputusannya cepat.',
            'Ketika usaha berkembang menjadi organisasi, muncul grup kerja dengan fungsi terpisah: pimpinan (CEO), pembelian, gudang, produksi, pengendalian mutu, pemasaran, hingga keuangan.',
            'Dengan struktur itu, proses bisnis menjadi lebih besar dan kompleks sehingga membutuhkan dukungan teknologi, termasuk jaringan komputer dan telekomunikasi untuk mempercepat alur kerja.',
        ],
        'table': [
            ['Perorangan', 'Organisasi'],
            ['Semua tahap dikerjakan sendiri', 'Tugas terbagi dalam grup kerja'],
            ['Keputusan cepat', 'Keputusan melalui koordinasi'],
            ['Skala usaha kecil', 'Skala dan volume produksi besar'],
            ['Alur kerja sederhana', 'Alur kerja terstruktur dan terdokumentasi'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-1-organisasi',
            'engine': 'mermaid',
            'title': 'Grup kerja pada pelaku usaha organisasi',
            'code': 'flowchart TB\n'
                    '  A[CEO] --> B[Purchasing]\n'
                    '  A --> C[Storage / gudang]\n'
                    '  A --> D[Production]\n'
                    '  A --> E[Quality control]\n'
                    '  A --> F[Marketing dan sales]\n'
                    '  A --> G[Accounting dan payroll]',
        },
        'activity': categorize_block(
            'tjkt-1-klasifikasi',
            'Kelompokkan ciri berikut ke dalam pelaku usaha perorangan atau organisasi.',
            [('b1', 'Perorangan'), ('b2', 'Organisasi')],
            [
                ('i1', 'Semua tahap dikerjakan sendiri', 'b1'),
                ('i2', 'Ada divisi purchasing dan produksi', 'b2'),
                ('i3', 'Keputusan cepat tanpa koordinasi', 'b1'),
                ('i4', 'Tugas terbagi dalam grup kerja', 'b2'),
                ('i5', 'Skala usaha kecil', 'b1'),
                ('i6', 'Produksi massal dengan mesin otomatisasi', 'b2'),
                ('i7', 'Pemasaran dilakukan pemilik langsung', 'b1'),
                ('i8', 'Ada pengendalian mutu terpisah', 'b2'),
            ],
            'Tepat. Perorangan mengerjakan segalanya; organisasi membagi tugas terstruktur.',
            'Periksa lagi: kata “divisi”, “grup kerja”, dan “massal” menandai organisasi.',
        ),
        'subtitle': 'Bisnis ISP sebagai contoh',
        'list': [
            'ISP (Internet Service Provider) menjual layanan internet kepada pelanggan rumah tangga dan perusahaan.',
            'Proses bisnis ISP mencakup pemasaran, pemasangan akses, layanan pelanggan, dan pemeliharaan jaringan.',
            'Teknisi jaringan bekerja di divisi seperti Networking Design yang merancang jaringan sesuai kebutuhan pelanggan.',
            'Informasi proses bisnis menentukan segmen jaringan, layanan, alur akses, dan jumlah pengguna yang dilayani.',
        ],
        'checkpoint': (
            'Contoh perusahaan yang menghasilkan jasa layanan internet adalah…',
            [
                ('ISP', True),
                ('pabrik kue', False),
                ('toko sembako', False),
                ('perusahaan tekstil', False),
            ],
            'ISP adalah penyedia jasa layanan internet.',
        ),
    },
    'practice': {
        'material_title': 'Perencanaan jaringan untuk bisnis',
        'title': 'Analisis kebutuhan pengguna',
        'paragraphs': [
            'Perencanaan jaringan dimulai dari analisis kebutuhan pengguna. Informasi yang dikumpulkan lewat survei: jumlah pengguna, jumlah perangkat keras, informasi grup kerja, dan alur kerja perusahaan.',
            'Informasi lain yang penting: keberadaan cabang, jarak antargedung, dan layanan yang dibutuhkan. Semua data itu menentukan pilihan perangkat, media koneksi, dan pengalamatan IP.',
            'Implementasi dapat diuji di media simulasi seperti Cisco Packet Tracer: memilih perangkat, menyambung media, memberikan alamat IP, hingga menguji koneksi antarpengguna.',
        ],
        'scenario': scenario(
            'tjkt-1-skenario',
            'Survei kebutuhan jaringan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Perusahaan kue ingin jaringan untuk 30 karyawan di dua lantai. Langkah pertamamu?',
                    'choices': [
                        {'text': 'Menilai kebutuhan: jumlah pengguna, perangkat, dan alur kerja', 'next': 'n2', 'score': 2, 'feedback': 'Analisis kebutuhan mendahului pemilihan perangkat.'},
                        {'text': 'Langsung membeli switch dan kabel terbanyak', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa analisis, pembelian bisa mubazir dan tidak cocok.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana cara mendapat data kebutuhan itu?',
                    'choices': [
                        {'text': 'Wawancara dan formulir survei ke tiap divisi', 'next': 'n4', 'score': 2, 'feedback': 'Survei menggali kebutuhan nyata dari pengguna jaringan.'},
                        {'text': 'Menebak dari ukuran perusahaan', 'next': 'n3', 'score': 0, 'feedback': 'Tebakan tanpa data besar kemungkinannya keliru.'},
                    ],
                },
                {'id': 'n3', 'text': 'Jaringan tidak sesuai kebutuhan dan biaya membengkak.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Desain jaringan sesuai kebutuhan dan mudah dikembangkan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu proses bisnis?', 'back': 'Rangkaian tahapan terstruktur yang menghasilkan barang atau jasa dengan tujuan ekonomi.'},
            {'front': 'Apa yang dimaksud core business?', 'back': 'Aktivitas utama bisnis yang menjadi sumber nilai dan pendapatan.'},
            {'front': 'Sebutkan dua bentuk pelaku usaha.', 'back': 'Perorangan dan organisasi/kelompok.'},
            {'front': 'Apa saja data kebutuhan jaringan dari survei?', 'back': 'Jumlah pengguna, perangkat, grup kerja, alur kerja, cabang, jarak, dan layanan.'},
        ],
        'checkpoint': (
            'Alat yang tepat untuk mengumpulkan kebutuhan pengguna jaringan adalah…',
            [
                ('survei melalui wawancara dan formulir', True),
                ('membeli perangkat secara acak', False),
                ('menyalin desain perusahaan lain', False),
                ('mengabaikan jumlah pengguna', False),
            ],
            'Wawancara dan formulir survei mengungkap kebutuhan nyata pengguna.',
        ),
        'challenge': challenge_block(
            'tjkt-1-tantangan',
            'Tantangan istilah proses bisnis',
            90,
            [
                ('Tahapan terstruktur untuk tujuan ekonomi', 'Proses bisnis'),
                ('Aktivitas utama yang bernilai', 'Core business'),
                ('Penghubung antarderangkat', 'Media koneksi'),
                ('Penyedia layanan internet', 'ISP'),
                ('Sistem pengatur izin lalu lintas data', 'Firewall'),
            ],
            'Lima istilah proses bisnis terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Proses bisnis adalah…', 'rangkaian tahapan terstruktur yang menghasilkan barang atau jasa', ['acara sekali waktu', 'hobi individu', 'kegiatan amal'], 'Proses bisnis bertujuan ekonomi.', 'Terdiri atas tahapan yang saling menunjang.'),
        ('Aktivitas utama bisnis yang menjadi sumber nilai disebut…', 'core business', ['firewall', 'switch', 'router'], 'Core business menghasilkan nilai dan pendapatan utama.', 'Istilah ini muncul pada Tabel 1.1 dan 1.2.'),
        ('Pelaku usaha perorangan mengerjakan…', 'seluruh tahap proses bisnis sendiri', ['hanya pemasaran', 'hanya produksi', 'hanya keuangan'], 'Skala kecil dan keputusan cepat.', 'Pemasaran, produksi, dan keuangan di tangannya.'),
        ('Saat usaha berkembang menjadi organisasi, yang bertanggung jawab memimpin adalah…', 'CEO', ['kasir', 'kurir', 'satpam'], 'CEO memimpin dan mengoordinasikan grup kerja.', 'Di bawahnya ada divisi pembelian, produksi, dan lainnya.'),
        ('Divisi yang mengurus pengendalian mutu produk disebut…', 'quality control', ['purchasing', 'payroll', 'storage'], 'QC memastikan produk sesuai standar.', 'Purchasing mengurus pembelian.'),
        ('Penyedia jasa layanan internet kepada pelanggan disebut…', 'ISP', ['QC', 'CEO', 'DTE'], 'ISP menghubungkan pelanggan ke internet.', 'Contohnya perusahaan MyTelco dalam buku.'),
        ('Langkah pertama perencanaan jaringan adalah…', 'analisis kebutuhan pengguna', ['membeli switch', 'memasang kabel', 'membuat akun'], 'Kebutuhan menentukan desain jaringan.', 'Dikumpulkan lewat survei.'),
        ('Informasi yang tidak termasuk kebutuhan survei jaringan adalah…', 'harga saham perusahaan lain', ['jumlah pengguna', 'jumlah perangkat keras', 'layanan yang dibutuhkan'], 'Survei menggali kebutuhan nyata pengguna.', 'Harga saham tidak menentukan desain jaringan.'),
        ('Salah satu aplikasi simulasi jaringan yang dipakai buku adalah…', 'Cisco Packet Tracer', ['Microsoft Word', 'Adobe Photoshop', 'Paint'], 'Packet Tracer merancang dan menguji jaringan.', 'Bisa memilih perangkat dan mengatur alamat IP.'),
        ('Pemberian identitas unik pada perangkat agar dapat berkomunikasi disebut…', 'pengalamatan IP', ['firewall', 'storage', 'payroll'], 'Alamat IP memungkinkan perangkat saling mengenal.', 'Diatur saat implementasi jaringan.'),
        ('Sistem yang mengatur izin lalu lintas data masuk dan keluar jaringan disebut…', 'firewall', ['survei', 'produksi', 'kemasan'], 'Firewall menjaga keamanan jaringan.', 'Arah akses antargrup kerja diatur lewatnya.'),
        ('Perusahaan yang memproduksi kue dalam contoh buku bernama…', 'MyCakes', ['MyTelco', 'PT PAL', 'Garuda'], 'MyCakes adalah perusahaan kue yang disurvei.', 'MyTelco adalah perusahaan ISP.'),
        ('Media yang menghubungkan komputer di laboratorium sekolah termasuk…', 'media koneksi', ['core business', 'proses bisnis', 'divisi QC'], 'Media koneksi dapat berupa kabel atau nirkabel.', 'Menghubungkan perangkat akhir pengguna.'),
        ('Tujuan mempelajari proses bisnis bagi teknisi jaringan adalah…', 'merancang jaringan yang mendukung alur kerja perusahaan', ['menghafal nama pemilik', 'menentukan gaji karyawan', 'membuat iklan produk'], 'Jaringan dibangun demi target perusahaan.', 'Proses bisnis menjadi acuan desain.'),
    ],
    'multi': [
        ('Manakah ciri pelaku usaha perorangan?', ['Semua tahap dikerjakan sendiri', 'Keputusan cepat', 'Skala usaha kecil'], ['Ada divisi terpisah', 'Produksi massal'], 'Perorangan sederhana dan cepat.', 'Divisi dan produksi massal ciri organisasi.'),
        ('Manakah divisi pada pelaku usaha organisasi?', ['Purchasing', 'Production', 'Marketing dan sales'], ['Firewall', 'IP address'], 'Divisi menjalankan fungsi terpisah.', 'Firewall dan IP adalah konsep jaringan.'),
        ('Manakah informasi kebutuhan pengguna pada survei jaringan?', ['Jumlah pengguna', 'Jumlah perangkat keras', 'Layanan yang dibutuhkan'], ['Warna seragam kantor', 'Menu kantin'], 'Data itu menentukan desain jaringan.', 'Seragam dan kantin tidak relevan.'),
        ('Manakah manfaat memahami proses bisnis bagi teknisi jaringan?', ['Menentukan segmen jaringan', 'Menentukan layanan jaringan', 'Menentukan jumlah pengguna'], ['Menghafal struktur gaji', 'Memilih warna logo'], 'Proses bisnis menjadi acuan desain.', 'Gaji dan logo bukan urusan desain.'),
        ('Manakah perangkat keras jaringan?', ['Switch', 'Router', 'Kabel media koneksi'], ['Kalkulator', 'Papan tulis'], 'Perangkat itu menghubungkan dan mengarahkan data.', 'Kalkulator dan papan tulis bukan perangkat jaringan.'),
        ('Manakah contoh perusahaan jasa?', ['ISP', 'Penyedia jasa instalasi jaringan'], ['Pabrik kue', 'Toko sembako'], 'Jasa tidak menghasilkan barang fisik.', 'Pabrik dan toko menghasilkan barang.'),
        ('Manakah langkah implementasi perencanaan jaringan?', ['Memilih perangkat jaringan', 'Memilih media koneksi', 'Mengatur alamat IP dan menguji'], ['Menentukan harga produk', 'Mendesain kemasan'], 'Implementasi merakit dan menguji jaringan.', 'Harga dan kemasan urusan bisnis lain.'),
        ('Manakah alasan jaringan dibangun sesuai proses bisnis?', ['Menunjang kecepatan proses bisnis', 'Menghubungkan semua divisi', 'Mendukung layanan ke pelanggan'], ['Sekadar mengikuti tren', 'Menghabiskan anggaran'], 'Jaringan adalah alat menunjang bisnis.', 'Bukan proyek tanpa manfaat.'),
    ],
    'pairs': [
        ('Proses bisnis', 'tahapan terstruktur menghasilkan nilai'),
        ('Core business', 'aktivitas utama yang bernilai'),
        ('Grup kerja', 'pembagian tugas terstruktur'),
        ('ISP', 'penyedia layanan internet'),
        ('Media koneksi', 'penghubung antarderangkat'),
        ('Pengalamatan IP', 'identitas unik perangkat'),
        ('Firewall', 'pengatur izin lalu lintas data'),
        ('Analisis kebutuhan', 'survei jumlah pengguna dan layanan'),
    ],
    'steps': [
        ('Urutkan proses bisnis pelaku usaha perorangan.', ['Membeli bahan', 'Memproduksi barang atau jasa', 'Mengendalikan mutu', 'Menjual ke pelanggan', 'Mengelola keuangan'], 'Tahapan berurutan dari bahan ke uang.', 'Perorangan menangani seluruh tahap ini.'),
        ('Urutkan pembagian organisasi usaha.', ['CEO', 'Purchasing dan storage', 'Production', 'Quality control', 'Marketing dan accounting'], 'Struktur berjenjang dari pimpinan ke penunjang.', 'Accounting menutup alur keuangan.'),
        ('Urutkan alur layanan ISP ke pelanggan.', ['Pemasaran layanan', 'Pendaftaran pelanggan', 'Pemasangan akses', 'Aktivasi layanan', 'Pemeliharaan dan dukungan'], 'ISP melayani dari promosi hingga dukungan.', 'Pemeliharaan menjaga kualitas layanan.'),
        ('Urutkan langkah perencanaan jaringan.', ['Analisis proses bisnis', 'Survei kebutuhan pengguna', 'Memilih perangkat dan media', 'Mengatur pengalamatan IP', 'Menguji koneksi'], 'Perencanaan bermula dari bisnis lalu diuji.', 'Pengujian memastikan desain berfungsi.'),
        ('Urutkan kerja simulasi jaringan di Packet Tracer.', ['Membuka proyek LabActivity', 'Menempatkan perangkat jaringan', 'Menghubungkan dengan media koneksi', 'Memberi alamat IP tiap perangkat', 'Menguji koneksi antarpengguna'], 'Simulasi mengikuti langkah implementasi nyata.', 'Pengujian menjadi langkah akhir.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)