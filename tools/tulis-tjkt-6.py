"""TJKT 6 — Media dan Jaringan Telekomunikasi (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 6',
    'slug': 'tjkt-6-media-jaringan-telekomunikasi',
    'title': 'Media dan Jaringan Telekomunikasi',
    'description': (
        'Memahami prinsip TCP/IP dan pengalamatan IP, cara kerja layanan jaringan '
        'seperti HTTP, DHCP, DNS, FTP, dan email, serta prinsip dasar keamanan '
        'jaringan komputer dan telekomunikasi.'
    ),
    'objectives': [
        'Menjelaskan prinsip kerja TCP/IP, encapsulation, sequence number, dan three way handshake.',
        'Menjelaskan pengalamatan IP dan pembagian jaringan pada TCP/IP.',
        'Menjelaskan prinsip kerja layanan jaringan HTTP, DHCP, DNS, FTP, dan email.',
        'Menjelaskan prinsip dasar keamanan jaringan beserta celah dan cara pengamanannya.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 6; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'TCP', 'definition': 'Transmission Control Protocol, mengatur bagaimana paket data dikirim, diurutkan, dan diterima.'},
        {'term': 'IP', 'definition': 'Internet Protocol, mengatur pengalamatan paket data yang dikirimkan.'},
        {'term': 'Encapsulation', 'definition': 'Proses membungkus data dengan header yang berisi alamat dan informasi kendali.'},
        {'term': 'Decapsulation', 'definition': 'Proses membuka bungkus paket dan membuang header setelah data diterima.'},
        {'term': 'Sequence number', 'definition': 'Nomor urut paket yang memungkinkan data disusun kembali dan bagian hilang dikirim ulang.'},
        {'term': 'Three way handshake', 'definition': 'Tiga langkah jabat tangan SYN, SYN-ACK, dan ACK sebelum dua perangkat berkomunikasi.'},
        {'term': 'DHCP', 'definition': 'Layanan yang memberikan alamat IP secara otomatis kepada perangkat dalam jaringan.'},
        {'term': 'DNS', 'definition': 'Layanan yang menerjemahkan nama domain menjadi alamat IP.'},
        {'term': 'FTP', 'definition': 'File Transfer Protocol, layanan pengiriman dan pengambilan berkas antarperangkat.'},
        {'term': 'ARP', 'definition': 'Address Resolution Protocol, mencari alamat MAC dari alamat IP dalam jaringan lokal.'},
        {'term': 'Ciphertext', 'definition': 'Teks hasil penyandian yang hanya dapat dibaca dengan kunci tertentu.'},
    ],
    'intro': {
        'material_title': 'Prinsip dasar TCP/IP',
        'title': 'Membungkus, mengurutkan, menyusun',
        'paragraphs': [
            'TCP/IP adalah protokol utama dalam jaringan komputer dan telekomunikasi. TCP mengatur bagaimana paket data dikirim dan diterima, sedangkan IP mengatur pengalamatan paket data.',
            'Cara kerja TCP dapat diibaratkan mengirim paket barang: barang dimasukkan ke wadah (encapsulation), diberi alamat tujuan pada bungkus (TCP header), dikirim melalui jalur, lalu dibuka penerima (decapsulation).',
            'Data dipecah menjadi bagian kecil dan diberi sequence number agar dapat disusun kembali. Jika ada bagian hilang, penerima dapat meminta pengiriman ulang; inilah fitur error recovery pada TCP.',
        ],
        'diagram': (
            'Alur encapsulation dan decapsulation',
            'flowchart LR\n'
            '  A[Data pengirim] --> B[Encapsulation: dibungkus header]\n'
            '  B --> C[Header berisi alamat dan port]\n'
            '  C --> D[Media transmisi / kurir]\n'
            '  D --> E[Penerima menerima paket]\n'
            '  E --> F[Decapsulation: header dibuang]\n'
            '  F --> G[Data utuh diterima]',
        ),
        'callout': 'Setiap paket harus memiliki nomor pengenal (sequence number) yang bertambah sesuai jumlah byte yang dikirim.',
        'checkpoint': (
            'Bagian TCP/IP yang mengatur pengalamatan paket data adalah…',
            [
                ('IP', True),
                ('TCP', False),
                ('HTTP', False),
                ('FTP', False),
            ],
            'IP mengatur pengalamatan, TCP mengatur pengiriman dan penerimaan paket.',
        ),
    },
    'concept': {
        'material_title': 'Jabat tangan dan layanan jaringan',
        'title': 'Dari three way handshake ke DHCP dan DNS',
        'paragraphs': [
            'Sebelum berkomunikasi, dua perangkat melakukan three way handshake: pengirim mengirim SYN dengan sequence number, penerima membalas SYN-ACK dengan ACK, lalu pengirim mengirim ACK. Setelah itu data dapat mengalir.',
            'Model TCP/IP bekerja berlapis antara perangkat keras dan perangkat lunak. Pengujian di simulasi memperlihatkan lapisan, alamat IP, port, dan alamat MAC pada setiap paket.',
            'Layanan jaringan mencakup HTTP untuk halaman web, DHCP untuk pemberian alamat IP otomatis, DNS untuk menerjemahkan nama domain, FTP untuk pengiriman berkas, dan email untuk surat elektronik.',
        ],
        'table': [
            ['Layanan', 'Fungsi', 'Catatan'],
            ['HTTP', 'Menampilkan halaman web', 'HTTP 404 berarti berkas tidak ditemukan'],
            ['DHCP', 'Memberi alamat IP otomatis', 'Discover, Offering, Request, ACK'],
            ['DNS', 'Nama domain menjadi alamat IP', 'Memudahkan pengguna mengingat nama'],
            ['FTP', 'Mengirim dan mengambil berkas', 'Butuh koneksi dan autentikasi'],
            ['Email', 'Mengirim surat elektronik', 'Memakai server pengirim dan penerima'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-6-dhcp',
            'engine': 'mermaid',
            'title': 'Empat langkah layanan DHCP',
            'code': 'flowchart LR\n'
                    '  A[DHCP Discover] --> B[DHCP Offering]\n'
                    '  B --> C[DHCP Request]\n'
                    '  C --> D[DHCP ACK]\n'
                    '  D --> E[Klien memakai alamat IP]',
        },
        'activity': categorize_block(
            'tjkt-6-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pengalamatan IP atau layanan jaringan.',
            [('b1', 'Pengalamatan IP'), ('b2', 'Layanan jaringan')],
            [
                ('i1', 'Alamat 192.168.1.10 dengan prefix /24', 'b1'),
                ('i2', 'Memberi alamat otomatis kepada klien', 'b2'),
                ('i3', 'Alamat IP terdiri atas network dan host', 'b1'),
                ('i4', 'Menerjemahkan nama domain menjadi alamat', 'b2'),
                ('i5', 'Alamat IPv6 berukuran 128 bit', 'b1'),
                ('i6', 'Menampilkan halaman web lewat browser', 'b2'),
                ('i7', 'Range alamat host dalam satu jaringan', 'b1'),
                ('i8', 'Mengirim dan mengambil berkas dari server', 'b2'),
            ],
            'Tepat. Pengalamatan berkaitan dengan identitas perangkat; layanan berkaitan dengan fungsi yang disediakan jaringan.',
            'Periksa lagi: DHCP, DNS, HTTP, dan FTP termasuk layanan jaringan.',
        ),
        'subtitle': 'Keamanan jaringan',
        'list': [
            'Hub menyebarkan paket ke semua perangkat sehingga mudah disadap, sedangkan switch mencatat alamat MAC pada memori CAM dan hanya meneruskan ke port tujuan.',
            'ARP dipakai mencari alamat MAC dari alamat IP; jawaban palsu atas ARP dapat dipakai untuk menipu jaringan.',
            'Enkripsi mengubah plaintext menjadi ciphertext dengan kunci tertentu, misalnya shift cipher menggeser huruf sejumlah kunci.',
            'DHCP Server palsu dapat memberi alamat yang salah sehingga pengguna diarahkan ke jaringan penyerang; Wi-Fi juga perlu diamankan dengan autentikasi dan enkripsi.',
        ],
        'checkpoint': (
            'Layanan yang memberikan alamat IP secara otomatis adalah…',
            [
                ('DHCP', True),
                ('DNS', False),
                ('FTP', False),
                ('HTTP', False),
            ],
            'DHCP memberi alamat IP otomatis melalui Discover, Offering, Request, dan ACK.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membaca lalu lintas dan menjaga jaringan',
        'paragraphs': [
            'Saat membuka sebuah situs, browser mengirim HTTP Request. Server membalas HTTP Response berisi berkas halaman; bila berkas tidak ada, server mengirim kode 404.',
            'Pada jaringan lokal, switch mencatat MAC address dan port yang dipakai. Karena itu perangkat pengguna tidak perlu menerima seluruh lalu lintas jaringan seperti pada hub.',
            'Pengamanan sederhana dapat dimulai dengan kata sandi kuat, pembaruan perangkat, serta memeriksa perangkat asing yang terhubung ke jaringan.',
        ],
        'scenario': scenario(
            'tjkt-6-skenario',
            'Alamat IP mendadak berubah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Beberapa komputer di lab mendapat alamat IP aneh dan tidak bisa membuka situs internal. Dugaanmu?',
                    'choices': [
                        {'text': 'Ada DHCP Server tidak dikenal yang membagikan alamat salah', 'next': 'n2', 'score': 2, 'feedback': 'DHCP palsu memang dapat mengarahkan klien ke jaringan penyerang.'},
                        {'text': 'Kabel LAN semuanya putus', 'next': 'n3', 'score': 0, 'feedback': 'Jika semua kabel putus, perangkat tidak akan mendapat alamat sama sekali.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana menanganinya?',
                    'choices': [
                        {'text': 'Menonaktifkan port perangkat asing dan memakai DHCP Server resmi', 'next': 'n4', 'score': 2, 'feedback': 'Membatasi port dan memakai server resmi memulihkan keamanan jaringan.'},
                        {'text': 'Membiarkannya karena masih bisa internet', 'next': 'n3', 'score': 0, 'feedback': 'Lalu lintas bisa disadap melalui server palsu.'},
                    ],
                },
                {'id': 'n3', 'text': 'Data pengguna tersadap dan jaringan tidak stabil.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Jaringan kembali normal dan aman.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa fungsi TCP dan IP?', 'back': 'TCP mengatur pengiriman paket, IP mengatur pengalamatan.'},
            {'front': 'Apa itu encapsulation?', 'back': 'Membungkus data dengan header berisi alamat dan informasi kendali.'},
            {'front': 'Sebutkan empat langkah DHCP.', 'back': 'Discover, Offering, Request, ACK.'},
            {'front': 'Apa fungsi DNS?', 'back': 'Menerjemahkan nama domain menjadi alamat IP.'},
        ],
        'checkpoint': (
            'Kode balasan server web ketika berkas halaman tidak ditemukan adalah…',
            [
                ('HTTP 404', True),
                ('HTTP 200', False),
                ('DHCP ACK', False),
                ('FTP 21', False),
            ],
            'HTTP 404 menandakan berkas yang diminta tidak ditemukan.',
        ),
        'challenge': challenge_block(
            'tjkt-6-tantangan',
            'Tantangan istilah jaringan telekomunikasi',
            90,
            [
                ('Mengatur pengiriman paket', 'TCP'),
                ('Mengatur pengalamatan paket', 'IP'),
                ('Nomor urut paket', 'Sequence number'),
                ('Pemberi alamat IP otomatis', 'DHCP'),
                ('Nama domain menjadi alamat IP', 'DNS'),
            ],
            'Lima istilah jaringan telekomunikasi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Protokol yang mengatur bagaimana paket data dikirim dan diterima adalah…', 'TCP', ['IP', 'DNS', 'ARP'], 'TCP mengatur pengiriman dan penerimaan paket.', 'IP mengatur pengalamatan.'),
        ('Bagian TCP/IP yang mengatur pengalamatan paket data adalah…', 'IP', ['TCP', 'HTTP', 'FTP'], 'IP memberi alamat pada paket.', 'Bersama TCP membentuk TCP/IP.'),
        ('Proses membungkus data dengan header disebut…', 'encapsulation', ['decapsulation', 'enkripsi', 'fragmentasi'], 'Encapsulation menambahkan header alamat.', 'Analogi memasukkan barang ke wadah.'),
        ('Proses membuka bungkus paket dan membuang header setelah diterima disebut…', 'decapsulation', ['encapsulation', 'kompresi', 'routing'], 'Penerima membuang header lalu mengambil isi.', 'Kebalikan encapsulation.'),
        ('Nomor urut paket pada TCP disebut…', 'sequence number', ['checksum', 'port', 'gateway'], 'Sequence number memungkinkan penyusunan ulang.', 'Bagian hilang dapat dikirim ulang.'),
        ('Fitur TCP yang memungkinkan pengiriman ulang paket hilang disebut…', 'error recovery', ['broadcast', 'collision', 'routing'], 'Error recovery memulihkan data yang gagal.', 'Didukung sequence number.'),
        ('Tiga langkah jabat tangan sebelum berkomunikasi disebut…', 'three way handshake', ['broadcast storm', 'handover', 'flooding'], 'Urutannya SYN, SYN-ACK, ACK.', 'Sebagai salam perkenalan perangkat.'),
        ('Layanan yang memberi alamat IP secara otomatis adalah…', 'DHCP', ['DNS', 'FTP', 'ARP'], 'DHCP meminjamkan alamat IP sementara.', 'Ada batas waktu DHCP Lease.'),
        ('Urutan pesan DHCP yang benar adalah…', 'Discover, Offering, Request, ACK', ['Request, Offering, Discover, ACK', 'ACK, Discover, Offering, Request', 'Offering, ACK, Discover, Request'], 'Klien mencari, server menawarkan, klien meminta, server mengonfirmasi.', 'Empat langkah berurutan.'),
        ('Layanan yang menerjemahkan nama domain menjadi alamat IP adalah…', 'DNS', ['DHCP', 'HTTP', 'FTP'], 'DNS memudahkan pengguna memakai nama.', 'Tanpa DNS harus menghafal alamat IP.'),
        ('Kode HTTP yang menandakan berkas tidak ditemukan adalah…', '404', ['200', '301', '21'], 'HTTP reply 404 dikirim server bila berkas tidak ada.', 'Sering muncul saat alamat salah.'),
        ('Protokol yang mencari alamat MAC dari alamat IP adalah…', 'ARP', ['FTP', 'DNS', 'TCP'], 'ARP memakai broadcast dalam jaringan lokal.', 'Switch mencatat MAC pada memori CAM.'),
        ('Memori switch untuk menyimpan alamat MAC disebut…', 'CAM', ['RAM', 'ROM', 'DNS'], 'CAM menyimpan alamat MAC dan port.', 'Mengurangi broadcast berlebihan.'),
        ('Perangkat yang menyebarkan paket ke semua perangkat sehingga mudah disadap adalah…', 'hub', ['switch', 'router', 'modem'], 'Hub menyebar paket ke semua port.', 'Switch meneruskan ke port tujuan.'),
        ('Teks hasil penyandian yang hanya bisa dibaca dengan kunci disebut…', 'ciphertext', ['plaintext', 'header', 'footer'], 'Ciphertext dihasilkan dari enkripsi.', 'Untuk membacanya perlu kunci.'),
    ],
    'multi': [
        ('Manakah bagian dari TCP/IP?', ['TCP', 'IP'], ['DNS', 'HTTP'], 'TCP/IP terdiri atas TCP dan IP.', 'DNS dan HTTP adalah layanan.'),
        ('Manakah layanan jaringan pada bab ini?', ['HTTP', 'DHCP', 'DNS'], ['ARP', 'MAC'], 'HTTP, DHCP, dan DNS adalah layanan jaringan.', 'ARP protokol pencarian MAC.'),
        ('Manakah ciri encapsulation?', ['Menambahkan header', 'Menuliskan alamat tujuan', 'Menyiapkan port tujuan'], ['Membuang header', 'Mengubah isi data'], 'Encapsulation membungkus data dengan header.', 'Membuang header adalah decapsulation.'),
        ('Manakah manfaat sequence number?', ['Menyusun ulang paket', 'Mengetahui paket hilang', 'Memungkinkan pengiriman ulang'], ['Menghapus paket', 'Menggandakan data'], 'Sequence number menjaga urutan data.', 'Paket hilang bisa dikirim ulang.'),
        ('Manakah langkah three way handshake?', ['SYN', 'SYN-ACK', 'ACK'], ['Discover', 'Offering'], 'Handshake memakai SYN dan ACK.', 'Discover dan Offering bagian DHCP.'),
        ('Manakah pernyataan tentang DNS?', ['Menerjemahkan nama domain', 'Membantu membuka situs', 'Memakai alamat IP'], ['Memberi alamat otomatis', 'Mengirim berkas'], 'DNS memetakan nama ke alamat IP.', 'DHCP yang memberi alamat.'),
        ('Manakah cara mengurangi risiko penyadapan?', ['Memakai switch bukan hub', 'Mengaktifkan enkripsi', 'Memakai kata sandi kuat'], ['Membagikan kata sandi', 'Membiarkan port terbuka'], 'Ketiganya meningkatkan keamanan.', 'Membagi sandi menurunkan keamanan.'),
        ('Manakah pernyataan tentang switch?', ['Menyimpan alamat MAC di CAM', 'Meneruskan paket ke port tujuan', 'Mencatat port perangkat'], ['Menyebar paket ke semua port', 'Tidak mengenal MAC'], 'Switch lebih selektif daripada hub.', 'Menyebar ke semua port ciri hub.'),
    ],
    'pairs': [
        ('TCP', 'mengatur pengiriman paket'),
        ('IP', 'mengatur pengalamatan paket'),
        ('Encapsulation', 'membungkus data dengan header'),
        ('Sequence number', 'nomor urut paket'),
        ('Three way handshake', 'SYN, SYN-ACK, ACK'),
        ('DHCP', 'pemberi alamat IP otomatis'),
        ('DNS', 'nama domain menjadi alamat IP'),
        ('ARP', 'mencari alamat MAC'),
    ],
    'steps': [
        ('Urutkan proses pengiriman data dengan TCP.', ['Data dipecah menjadi paket kecil', 'Setiap paket diberi sequence number', 'Paket dikirim melalui media', 'Penerima menyusun ulang paket', 'Paket hilang dikirim ulang'], 'Pengiriman berurutan dari pemecahan ke pemulihan.', 'Pemulihan menjaga kelengkapan data.'),
        ('Urutkan langkah three way handshake.', ['Pengirim mengirim SYN dengan sequence number', 'Penerima membalas SYN-ACK', 'Pengirim mengirim ACK', 'Koneksi terbentuk', 'Data mulai dikirim'], 'Handshake terjadi sebelum data.', 'Koneksi terbentuk setelah ACK.'),
        ('Urutkan langkah kerja DHCP.', ['Klien mengirim DHCP Discover', 'Server mengirim DHCP Offering', 'Klien mengirim DHCP Request', 'Server mengirim DHCP ACK', 'Klien memakai alamat IP'], 'DHCP berjalan empat langkah.', 'Alamat dipakai setelah ACK.'),
        ('Urutkan proses membuka situs web.', ['Pengguna mengetik alamat situs', 'DNS menerjemahkan nama menjadi IP', 'Browser mengirim HTTP Request', 'Server mengirim HTTP Response', 'Halaman tampil di browser'], 'Situs tampil setelah DNS dan HTTP bekerja.', 'Respons server menampilkan halaman.'),
        ('Urutkan cara switch meneruskan paket.', ['PC mengirim paket broadcast ARP', 'Switch mencatat alamat MAC sumber dan portnya', 'Switch meneruskan ARP ke perangkat lain', 'PC tujuan membalas dengan alamat MAC', 'Switch menghubungkan port sumber dan tujuan'], 'Switch belajar alamat lalu meneruskan.', 'Pencatatan MAC membuat lalu lintas efisien.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)