"""TJKT 2 — Perkembangan Teknologi di Bidang TJKT (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 2',
    'slug': 'tjkt-2-perkembangan-teknologi',
    'title': 'Perkembangan Teknologi di Bidang Teknik Jaringan Komputer dan Telekomunikasi',
    'description': (
        'Menelusuri perkembangan jaringan dedicated menjadi converged, media '
        'komunikasi 3G/4G/5G, VSAT, dan microwave link, pengalamatan IPv6, '
        'perangkat data center, layanan IoT dan cloud, serta keamanan jaringan.'
    ),
    'objectives': [
        'Menjelaskan perbedaan jaringan dedicated dan jaringan converged.',
        'Menjelaskan perkembangan media komunikasi jaringan komputer dan telekomunikasi.',
        'Menjelaskan pengalamatan IPv6 dan perbedaannya dengan IPv4.',
        'Menjelaskan perangkat data center, layanan jaringan, serta keamanan jaringan.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 2; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'Protokol', 'definition': 'Aturan yang disepakati bersama agar perangkat dapat saling berkomunikasi.'},
        {'term': 'Jaringan dedicated', 'definition': 'Jaringan yang memisahkan layanan komputer, telepon, dan broadcast dengan protokol masing-masing.'},
        {'term': 'Jaringan converged', 'definition': 'Jaringan yang menyatukan semua layanan komunikasi dalam satu protokol utama, yaitu TCP/IP.'},
        {'term': 'VSAT', 'definition': 'Very Small Aperture Terminal, media nirkabel berbasis satelit untuk daerah terpencil.'},
        {'term': 'Microwave link', 'definition': 'Penghubung nirkabel antartitik dengan gelombang mikro untuk jarak pandang langsung.'},
        {'term': 'IPv6', 'definition': 'Pengalamatan internet generasi baru berukuran 128 bit yang menyediakan alamat jauh lebih banyak.'},
        {'term': 'Data center', 'definition': 'Pusat penyimpanan dan pengolahan data berisi server, switch, dan sistem pendingin.'},
        {'term': 'Cloud computing', 'definition': 'Layanan komputasi yang disewa melalui jaringan sehingga pengguna tidak perlu memiliki perangkat sendiri.'},
        {'term': 'Sniffing', 'definition': 'Penyadapan lalu lintas data pada jaringan, dapat bersifat pasif maupun aktif.'},
        {'term': 'IoT', 'definition': 'Internet of Things, perangkat sehari-hari yang terhubung jaringan dan saling bertukar data.'},
    ],
    'intro': {
        'material_title': 'Dari dedicated ke converged',
        'title': 'Satu protokol untuk semua layanan',
        'paragraphs': [
            'Pada akhir tahun 1990-an, layanan komputer, telepon, dan siaran memiliki jaringan sendiri-sendiri. Jaringan seperti itu disebut jaringan dedicated karena tiap layanan memakai protokol berbeda.',
            'Saat ini semua layanan menyatu dalam jaringan converged dengan satu protokol utama, yaitu TCP/IP. Suara, video, dan data berjalan pada jaringan yang sama.',
            'Penyatuan itu mungkin karena media komunikasi dan pengalamatan IP terus berkembang, sehingga kecepatan jaringan meningkat dan layanan baru dapat lahir.',
        ],
        'diagram': (
            'Perbandingan jaringan dedicated dan converged',
            'flowchart TB\n'
            '  A[Jaringan dedicated] --> B[Jaringan komputer: TCP/IP]\n'
            '  A --> C[Jaringan telepon: PSTN]\n'
            '  A --> D[Jaringan broadcast: PAL/NTSC]\n'
            '  E[Jaringan converged] --> F[Satu protokol: TCP/IP]\n'
            '  F --> G[Data, suara, dan video menyatu]',
        ),
        'callout': 'Protokol adalah kesepakatan bersama; tanpa protokol yang sama, dua perangkat tidak dapat saling memahami.',
        'checkpoint': (
            'Jaringan yang menyatukan semua layanan dalam satu protokol TCP/IP disebut…',
            [
                ('converged', True),
                ('dedicated', False),
                ('terisolasi', False),
                ('analog', False),
            ],
            'Jaringan converged memakai TCP/IP untuk semua jenis layanan.',
        ),
    },
    'concept': {
        'material_title': 'Media, pengalamatan, dan data center',
        'title': 'Perkembangan yang mempercepat jaringan',
        'paragraphs': [
            'Media nirkabel berkembang dari 3G, 4G, hingga 5G. Kecepatan 5G secara teori mencapai beberapa gigabit per detik, jauh di atas 4G sehingga layanan berat seperti video dan otomatisasi menjadi mungkin.',
            'Untuk daerah tanpa infrastruktur, dipakai VSAT berbasis satelit. Bandwidth-nya tidak sebesar 4G, tetapi mampu menjangkau hutan, pegunungan, dan perkebunan. Microwave link menghubungkan dua titik dengan gelombang mikro.',
            'Pengalamatan berkembang dari IPv4 ke IPv6. IPv6 berukuran 128 bit sehingga menyediakan alamat jauh lebih banyak, termasuk alamat link local dan gateway untuk komunikasi lokal.',
            'Data center menampung server, switch, dan sistem pendukung seperti pendingin serta catu daya cadangan. Ketersediaan tinggi dicapai melalui redundansi perangkat.',
        ],
        'table': [
            ['Teknologi', 'Kegunaan', 'Catatan'],
            ['3G/4G/5G', 'Akses seluler bergerak', '5G paling cepat, orde gigabit'],
            ['VSAT', 'Daerah tanpa infrastruktur', 'Bergantung satelit, bandwidth terbatas'],
            ['Microwave link', 'Penghubung dua titik', 'Perlu jalur pandang langsung'],
            ['IPv6', 'Pengalamatan internet baru', '128 bit, alamat sangat banyak'],
            ['Cloud computing', 'Layanan komputasi sewa', 'Mengurangi perangkat di sisi pengguna'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-2-layanan',
            'engine': 'mermaid',
            'title': 'Perkembangan layanan di atas jaringan converged',
            'code': 'flowchart LR\n'
                    '  A[Media cepat dan IPv6] --> B[Layanan jaringan]\n'
                    '  B --> C[IoT dan otomatisasi]\n'
                    '  B --> D[Cloud computing]\n'
                    '  B --> E[Video dan konferensi]\n'
                    '  B --> F[Keamanan jaringan]\n'
                    '  F --> G[Sniffing pasif dan aktif]',
        },
        'activity': categorize_block(
            'tjkt-2-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam jaringan dedicated atau jaringan converged.',
            [('b1', 'Dedicated'), ('b2', 'Converged')],
            [
                ('i1', 'Layanan telepon memakai protokol PSTN', 'b1'),
                ('i2', 'Semua layanan memakai TCP/IP', 'b2'),
                ('i3', 'Jaringan komputer, telepon, dan broadcast terpisah', 'b1'),
                ('i4', 'Suara dan video berjalan pada jaringan yang sama', 'b2'),
                ('i5', 'Tiap layanan punya aturan sendiri', 'b1'),
                ('i6', 'Layanan baru mudah ditambahkan', 'b2'),
                ('i7', 'Siaran memakai standar PAL atau NTSC', 'b1'),
                ('i8', 'Data, suara, dan video menyatu', 'b2'),
            ],
            'Tepat. Dedicated memisahkan layanan, converged menyatukannya dalam TCP/IP.',
            'Periksa lagi: penyebutan protokol berbeda per layanan menandai jaringan dedicated.',
        ),
        'subtitle': 'Layanan dan keamanan jaringan',
        'list': [
            'Internet of Things menghubungkan perangkat sehari-hari agar dapat mengirim dan menerima data secara otomatis.',
            'Cloud computing memindahkan penyimpanan dan pengolahan ke penyedia layanan sehingga pengguna tidak perlu memiliki server sendiri.',
            'Keamanan jaringan menjadi makin penting seiring banyaknya perangkat terhubung; sniffing adalah contoh ancaman penyadapan data.',
            'Sniffing pasif hanya merekam lalu lintas data, sedangkan sniffing aktif dapat mengubah atau menyisipkan data.',
        ],
        'checkpoint': (
            'Pengalamatan IPv6 memiliki ukuran…',
            [
                ('128 bit', True),
                ('32 bit', False),
                ('64 bit', False),
                ('256 bit', False),
            ],
            'IPv4 berukuran 32 bit, sedangkan IPv6 berukuran 128 bit.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Memilih teknologi sesuai kebutuhan',
        'paragraphs': [
            'Sebuah kebun di pegunungan membutuhkan koneksi internet. Kabel tidak mungkin dipasang, sedangkan sinyal seluler lemah. VSAT menjadi pilihan meski bandwidth-nya terbatas.',
            'Sebuah kantor kota membutuhkan koneksi cepat dan stabil. Jaringan seluler 4G atau 5G serta serat optik lebih tepat karena kapasitasnya besar.',
            'Untuk menghemat perangkat, layanan cloud dapat dipakai sebagai penyimpanan dan server aplikasi. Namun keamanan perlu dijaga, misalnya dengan enkripsi dan pembatasan akses.',
        ],
        'scenario': scenario(
            'tjkt-2-skenario',
            'Memilih koneksi untuk kebun terpencil',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kebun di pegunungan tidak terjangkau kabel dan sinyal seluler lemah. Pilihanmu?',
                    'choices': [
                        {'text': 'VSAT karena berbasis satelit dan tidak butuh infrastruktur darat', 'next': 'n2', 'score': 2, 'feedback': 'VSAT dirancang untuk daerah tanpa infrastruktur.'},
                        {'text': '5G karena paling cepat', 'next': 'n3', 'score': 0, 'feedback': 'Kecepatan tidak berguna bila sinyalnya tidak tersedia.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Data kebun perlu dikirim tiap jam tetapi bandwidth terbatas. Bagaimana mengaturnya?',
                    'choices': [
                        {'text': 'Mengirim data ringkas secara terjadwal dan memakai sensor hemat data', 'next': 'n4', 'score': 2, 'feedback': 'Kebutuhan disesuaikan kemampuan media yang tersedia.'},
                        {'text': 'Mengirim video resolusi tinggi terus-menerus', 'next': 'n3', 'score': 0, 'feedback': 'Bandwidth VSAT terbatas; pengiriman berat akan gagal.'},
                    ],
                },
                {'id': 'n3', 'text': 'Koneksi tersendat dan biaya membengkak tanpa hasil memadai.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Data terkirim tepat waktu dengan biaya terkendali.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa perbedaan jaringan dedicated dan converged?', 'back': 'Dedicated memisahkan layanan; converged menyatukannya dalam TCP/IP.'},
            {'front': 'Kapan VSAT dipakai?', 'back': 'Di daerah tanpa infrastruktur seperti hutan, pegunungan, dan perkebunan.'},
            {'front': 'Berapa ukuran alamat IPv6?', 'back': '128 bit.'},
            {'front': 'Apa itu sniffing?', 'back': 'Penyadapan lalu lintas data pada jaringan, pasif atau aktif.'},
        ],
        'checkpoint': (
            'Layanan komputasi yang disewa melalui jaringan sehingga pengguna tidak perlu memiliki server sendiri disebut…',
            [
                ('cloud computing', True),
                ('microwave link', False),
                ('core business', False),
                ('sniffing', False),
            ],
            'Cloud computing memindahkan komputasi ke penyedia layanan.',
        ),
        'challenge': challenge_block(
            'tjkt-2-tantangan',
            'Tantangan istilah teknologi jaringan',
            90,
            [
                ('Aturan komunikasi yang disepakati', 'Protokol'),
                ('Jaringan dengan satu protokol TCP/IP', 'Converged'),
                ('Akses satelit untuk daerah terpencil', 'VSAT'),
                ('Pengalamatan 128 bit', 'IPv6'),
                ('Penyadapan lalu lintas data', 'Sniffing'),
            ],
            'Lima istilah teknologi jaringan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Jaringan yang memisahkan layanan komputer, telepon, dan broadcast disebut…', 'dedicated', ['converged', 'cloud', 'virtual'], 'Setiap layanan memakai protokol sendiri.', 'Banyak dipakai pada 1990-an.'),
        ('Jaringan yang menyatukan layanan dalam TCP/IP disebut…', 'converged', ['dedicated', 'analog', 'terisolasi'], 'Converged memakai satu protokol utama.', 'Data, suara, dan video menyatu.'),
        ('Aturan yang disepakati agar perangkat dapat berkomunikasi disebut…', 'protokol', ['topologi', 'bandwidth', 'firewall'], 'Protokol berisi standarisasi komunikasi.', 'Contohnya TCP/IP.'),
        ('Contoh standar jaringan nirkabel yang disebut buku adalah…', 'IEEE 802.11', ['PAL', 'NTSC', 'PSTN'], 'IEEE 802.11 adalah standar WLAN.', 'Beroperasi pada pita 2,4 GHz.'),
        ('Teknologi seluler yang kecepatan teoretisnya diuji hingga 5 Gbps adalah…', '5G', ['3G', '4G', '2G'], '5G jauh lebih cepat daripada 4G.', 'Memungkinkan unduhan besar dalam hitungan detik.'),
        ('Media yang mengirim data melalui satelit untuk daerah tanpa infrastruktur adalah…', 'VSAT', ['microwave link', 'serat optik', 'kabel UTP'], 'VSAT cocok untuk hutan, pegunungan, dan perkebunan.', 'Bandwidth-nya tidak sebesar 4G.'),
        ('Alamat IP versi baru yang berukuran 128 bit adalah…', 'IPv6', ['IPv4', 'MAC address', 'URL'], 'IPv6 menyediakan jumlah alamat jauh lebih banyak.', 'Menggantikan keterbatasan IPv4.'),
        ('Perangkat pada menara seluler yang berfungsi sebagai modem sekaligus router disebut…', 'indoor unit', ['outdoor unit', 'switch', 'access point'], 'Indoor unit punya dua pengalamatan IP.', 'Satu alamat untuk pengguna, satu untuk backbone.'),
        ('Pusat penyimpanan dan pengolahan data berisi server serta sistem pendukung disebut…', 'data center', ['core business', 'client', 'kios'], 'Data center menampung perangkat dan pendingin.', 'Menerapkan redundansi perangkat.'),
        ('Layanan komputasi yang disewa melalui jaringan disebut…', 'cloud computing', ['sniffing', 'firewall', 'VSAT'], 'Cloud mengurangi perangkat keras di sisi pengguna.', 'Contohnya penyimpanan daring.'),
        ('Perangkat sehari-hari yang terhubung jaringan dan saling bertukar data disebut…', 'IoT', ['IPv6', 'PSTN', 'PAL'], 'IoT adalah Internet of Things.', 'Contohnya sensor dan lampu pintar.'),
        ('Penyadapan lalu lintas data pada jaringan disebut…', 'sniffing', ['sniff test', 'routing', 'switching'], 'Sniffing dapat bersifat pasif atau aktif.', 'Merupakan ancaman keamanan jaringan.'),
        ('Sniffing yang hanya merekam lalu lintas data tanpa mengubahnya disebut…', 'sniffing pasif', ['sniffing aktif', 'spoofing', 'flooding'], 'Pasif hanya merekam.', 'Aktif dapat mengubah atau menyisipkan data.'),
        ('Layanan jaringan pada era converged memungkinkan…', 'otomatisasi pekerjaan dan cloud computing', ['hanya mengirim surel', 'hanya menelusuri web', 'hanya menelepon'], 'Jaringan cepat mendukung layanan baru.', 'Termasuk otomatisasi dan komputasi awan.'),
    ],
    'multi': [
        ('Manakah ciri jaringan dedicated?', ['Layanan terpisah', 'Protokol tiap layanan berbeda', 'Siaran memakai PAL atau NTSC'], ['Satu protokol TCP/IP', 'Suara dan data menyatu'], 'Dedicated memisahkan layanan.', 'Penyatuan adalah ciri converged.'),
        ('Manakah ciri jaringan converged?', ['Satu protokol TCP/IP', 'Layanan menyatu', 'Layanan baru mudah ditambah'], ['Layanan terpisah', 'Protokol berbeda per layanan'], 'Converged memakai satu protokol.', 'Dedicated yang memisahkan.'),
        ('Manakah media nirkabel yang disebut buku?', ['3G/4G/5G', 'VSAT', 'Microwave link'], ['Kabel UTP', 'Serat optik'], 'Ketiganya media nirkabel.', 'UTP dan serat optik berupa kabel.'),
        ('Manakah kelebihan IPv6?', ['Jumlah alamat sangat banyak', 'Ukuran 128 bit', 'Mendukung alamat link local'], ['Hanya 32 bit', 'Tidak punya gateway'], 'IPv6 memperluas ruang alamat.', 'IPv4 yang berukuran 32 bit.'),
        ('Manakah perangkat dalam data center?', ['Server', 'Switch', 'Sistem pendingin'], ['Meja makan', 'Papan tulis'], 'Data center berisi perangkat komputasi dan pendukung.', 'Furnitur bukan perangkat data center.'),
        ('Manakah contoh layanan pada jaringan converged?', ['IoT', 'Cloud computing', 'Video conference'], ['Surat pos biasa', 'Telegraf'], 'Layanan memanfaatkan jaringan cepat.', 'Surat pos dan telegraf bukan layanan jaringan modern.'),
        ('Manakah jenis sniffing?', ['Pasif', 'Aktif'], ['Statis', 'Dinamis'], 'Sniffing dibedakan pasif dan aktif.', 'Pasif merekam, aktif dapat mengubah.'),
        ('Manakah alasan perkembangan media dan pengalamatan penting?', ['Meningkatkan kecepatan jaringan', 'Memungkinkan layanan baru', 'Mengurangi jumlah perangkat pengguna'], ['Menghapus kebutuhan protokol', 'Membuat jaringan tanpa aturan'], 'Perkembangan menaikkan kapasitas dan layanan.', 'Protokol tetap diperlukan.'),
    ],
    'pairs': [
        ('Protokol', 'aturan komunikasi yang disepakati'),
        ('Jaringan dedicated', 'layanan terpisah per protokol'),
        ('Jaringan converged', 'semua layanan dalam TCP/IP'),
        ('VSAT', 'akses satelit daerah terpencil'),
        ('Microwave link', 'penghubung gelombang mikro'),
        ('IPv6', 'pengalamatan 128 bit'),
        ('Cloud computing', 'komputasi yang disewa'),
        ('Sniffing', 'penyadapan lalu lintas data'),
    ],
    'steps': [
        ('Urutkan perkembangan media seluler.', ['3G', '4G', '5G'], 'Setiap generasi meningkatkan kecepatan data.', '5G berada di puncak urutan.'),
        ('Urutkan alur koneksi ponsel ke internet.', ['Ponsel mengaktifkan data seluler', 'Menara seluler menerima sinyal', 'Indoor unit meneruskan ke backbone', 'Data mencapai jaringan ISP', 'Ponsel membuka halaman web'], 'Data bergerak dari perangkat ke jaringan ISP.', 'Backbone menghubungkan menara ke ISP.'),
        ('Urutkan langkah pengamatan simulasi jaringan seluler.', ['Membuka berkas LabActivity', 'Mengamati perangkat ponsel', 'Membuka web browser dan mengetik alamat', 'Mengamati menara seluler dan indoor unit', 'Mencatat alamat IP sumber dan tujuan'], 'Pengamatan berjalan dari perangkat ke jaringan.', 'Pencatatan alamat menutup kegiatan.'),
        ('Urutkan pemanfaatan VSAT pada daerah terpencil.', ['Menyiapkan antena dan ODU', 'Menghubungkan IDU ke jaringan lokal', 'Mengarahkan antena ke satelit', 'Mengaktifkan layanan', 'Menguji koneksi dan bandwidth'], 'VSAT dipasang dari perangkat luar ke pengujian.', 'Pengujian memastikan layanan berjalan.'),
        ('Urutkan pemeriksaan keamanan jaringan sederhana.', ['Mencatat perangkat yang terhubung', 'Memeriksa lalu lintas data mencurigakan', 'Mengidentifikasi potensi sniffing', 'Membatasi akses dengan kata sandi', 'Memantau secara berkala'], 'Keamanan dimulai dari inventaris perangkat.', 'Pemantauan menjaga keamanan berkelanjutan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)