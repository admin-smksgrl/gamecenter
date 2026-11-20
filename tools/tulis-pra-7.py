"""PRA 7 — Alat Pakan Otomatis (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 7',
    'slug': 'prakarya-7-pakan-otomatis',
    'title': 'Alat Pakan Otomatis',
    'description': (
        'Merancang alat pakan otomatis untuk hewan piaraan: memahami jenis pakan, '
        'wadah pakan, timer, motor penggerak, jadwal pemberian, dan perhitungan HPP.'
    ),
    'objectives': [
        'Mengamati cara pemberian pakan hewan di lingkungan sekitar.',
        'Mengidentifikasi bahan, alat, dan komponen alat pakan otomatis.',
        'Merancang alat pakan otomatis sesuai jenis hewan dan pakan.',
        'Membuat serta menguji alat pakan otomatis.',
        'Mempresentasikan produk dan menghitung harga pokok produksi.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Rekayasa-BG-KLS-X.pdf Unit 4 Alat Pakan Otomatis',
    'glossary': [
        {'term': 'Alat pakan otomatis', 'definition': 'Alat yang mengeluarkan pakan hewan sesuai jadwal tanpa bantuan manusia.'},
        {'term': 'Pakan', 'definition': 'Makanan yang diberikan kepada hewan piaraan agar tumbuh sehat.'},
        {'term': 'Wadah pakan', 'definition': 'Tempat menyimpan pakan sebelum dikeluarkan oleh alat.'},
        {'term': 'Timer', 'definition': 'Pengatur waktu yang menentukan kapan pakan dikeluarkan.'},
        {'term': 'Motor penggerak', 'definition': 'Komponen yang membuka atau menutup saluran pakan.'},
        {'term': 'HPP', 'definition': 'Harga pokok produksi, yaitu total biaya pembuatan produk.'},
        {'term': 'Prototipe', 'definition': 'Model awal produk yang dibuat untuk diuji sebelum produksi.'},
        {'term': 'Pameran', 'definition': 'Kegiatan mempresentasikan produk kepada masyarakat.'},
    ],
    'intro': {
        'material_title': 'Mengapa pakan perlu otomatis?',
        'title': 'Memberi pakan tepat waktu',
        'paragraphs': [
            'Pemberian pakan adalah kegiatan rutin dalam memelihara hewan seperti ayam, burung, ikan, dan kelinci. Pakan yang berkualitas dan diberikan tepat waktu memengaruhi pertumbuhan serta perkembangan hewan.',
            'Pemberian pakan biasanya dilakukan tiga kali sehari secara manual. Namun, pemilik kadang tidak berada di rumah atau tempat budi daya. Menitipkan hewan kepada tetangga juga merepotkan orang lain, sehingga dibutuhkan alat pakan otomatis.',
            'Alat pakan otomatis dapat dibuat secara sederhana maupun modern. Kelebihannya adalah mudah dibuat dan digunakan serta dapat mengeluarkan pakan tepat waktu sesuai jadwal yang diatur.',
        ],
        'diagram': (
            'Alur kerja alat pakan otomatis',
            'flowchart LR\n'
            '  A[Jadwal pakan tiba] --> B[Timer aktif]\n'
            '  B --> C[Motor penggerak berputar]\n'
            '  C --> D[Saluran pakan terbuka]\n'
            '  D --> E[Pakan jatuh ke wadah]\n'
            '  E --> F[Saluran menutup kembali]',
        ),
        'callout': 'Jauhkan rangkaian listrik dari air dan pakan basah. Periksa wadah pakan agar tidak lembap atau berjamur.',
        'checkpoint': (
            'Berapa kali pemberian pakan biasanya dilakukan dalam sehari?',
            [
                ('Tiga kali', True),
                ('Satu kali', False),
                ('Lima kali', False),
                ('Tujuh kali', False),
            ],
            'Buku menyebut pemberian pakan biasanya dilakukan tiga kali sehari.',
        ),
    },
    'concept': {
        'material_title': 'Jenis pakan dan komponen alat',
        'title': 'Menyusun alat pakan sederhana',
        'paragraphs': [
            'Pakan harus sesuai dengan jenis hewan yang dipelihara. Ayam dan burung memakan biji-bijian, ikan memakan pelet, sedangkan kelinci memakan sayuran dan hijauan. Ukuran pakan juga perlu disesuaikan agar tidak menyumbat saluran.',
            'Alat pakan otomatis terdiri atas wadah pakan, saluran pengeluaran, motor penggerak, timer, dan rangka. Timer menentukan waktu, motor membuka saluran, lalu pakan jatuh ke tempat makan. Rangka harus kokoh agar alat tidak mudah roboh.',
            'Alat dapat dibuat dari bahan sederhana seperti botol, pipa, kayu, atau ember. Untuk versi modern, Arduino Uno dapat dipakai mengatur jadwal dan mengendalikan motor. Semua sambungan harus diperiksa agar pakan tidak tumpah.',
        ],
        'table': [
            ['Komponen', 'Fungsi', 'Catatan'],
            ['Wadah pakan', 'Menyimpan pakan', 'Tutup rapat agar tidak lembap'],
            ['Saluran', 'Mengalirkan pakan', 'Sesuaikan ukuran dengan butiran'],
            ['Motor penggerak', 'Membuka dan menutup saluran', 'Perhatikan tegangan kerja'],
            ['Timer', 'Mengatur jadwal', 'Atur sesuai kebutuhan hewan'],
            ['Rangka', 'Menopang alat', 'Kokoh dan tidak mudah roboh'],
        ],
        'visual': chart_block(
            'pra-7-jadwal-pakan',
            'Perkiraan jumlah pemberian pakan per hari',
            'bar',
            [('Ikan', 3), ('Ayam', 3), ('Burung', 2), ('Kelinci', 2)],
        ),
        'activity': categorize_block(
            'pra-7-klasifikasi',
            'Kelompokkan komponen berikut ke dalam penyimpan pakan atau pengendali alat.',
            [('b1', 'Penyimpan pakan'), ('b2', 'Pengendali alat')],
            [
                ('i1', 'Wadah pakan', 'b1'),
                ('i2', 'Ember', 'b1'),
                ('i3', 'Botol', 'b1'),
                ('i4', 'Timer', 'b2'),
                ('i5', 'Motor penggerak', 'b2'),
                ('i6', 'Arduino Uno', 'b2'),
            ],
            'Tepat. Wadah, ember, dan botol menyimpan pakan; timer, motor, dan Arduino mengendalikan alat.',
            'Periksa lagi: penyimpan menampung pakan, pengendali mengatur pengeluaran.',
        ),
        'subtitle': 'Kebersihan dan keselamatan',
        'list': [
            'Bersihkan wadah pakan secara berkala agar tidak berjamur.',
            'Simpan pakan di tempat kering dan tertutup.',
            'Jauhkan kabel dan sumber listrik dari air serta pakan basah.',
            'Periksa alat sebelum ditinggal agar pakan tidak menumpuk atau tersumbat.',
        ],
        'checkpoint': (
            'Komponen yang mengatur jadwal pemberian pakan adalah…',
            [
                ('Timer', True),
                ('Wadah pakan', False),
                ('Rangka', False),
                ('Saluran', False),
            ],
            'Timer menentukan kapan motor penggerak aktif mengeluarkan pakan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat pakan otomatis sederhana',
        'paragraphs': [
            'Tentukan hewan yang akan diberi pakan dan jenis pakannya. Ukur jumlah pakan per sekali makan agar porsi tidak berlebihan. Pilih wadah yang mudah dibuka dan dibersihkan.',
            'Rancang saluran pengeluaran yang tidak mudah tersumbat. Jika memakai motor, uji putarannya sebelum dipasang. Atur timer sesuai jadwal, misalnya tiga kali sehari pada pagi, siang, dan sore.',
            'Uji alat dengan pakan sesungguhnya. Amati apakah pakan jatuh dengan jumlah yang tepat dan tidak tersisa di saluran. Hitung HPP dan presentasikan produk beserta cara perawatannya.',
        ],
        'scenario': scenario(
            'pra-7-skenario',
            'Pakan ayam saat pemilik pergi',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Keluargamu akan pergi dua hari dan ayam perlu diberi pakan tiga kali sehari. Apa solusinya?',
                    'choices': [
                        {'text': 'Membuat alat pakan otomatis dengan timer', 'next': 'n2', 'score': 2, 'feedback': 'Timer menjaga pakan keluar sesuai jadwal.'},
                        {'text': 'Menumpuk semua pakan sekaligus', 'next': 'n3', 'score': 0, 'feedback': 'Pakan menumpuk dapat rusak dan tidak sehat.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Pakan sering tersumbat di saluran. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menyesuaikan ukuran saluran dengan butiran pakan', 'next': 'n4', 'score': 2, 'feedback': 'Ukuran saluran yang tepat mencegah sumbatan.'},
                        {'text': 'Memperkecil saluran agar pakan cepat habis', 'next': 'n3', 'score': 0, 'feedback': 'Saluran terlalu kecil justru mudah tersumbat.'},
                    ],
                },
                {'id': 'n3', 'text': 'Ayam kelaparan dan pakan banyak terbuang.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Pakan keluar tepat waktu dan ayam tetap sehat.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Berapa kali pakan biasanya diberikan?', 'back': 'Tiga kali sehari.'},
            {'front': 'Apa fungsi timer pada alat pakan?', 'back': 'Mengatur jadwal pengeluaran pakan.'},
            {'front': 'Mengapa pakan harus sesuai jenis hewan?', 'back': 'Agar hewan mendapat gizi yang tepat dan tumbuh sehat.'},
            {'front': 'Apa itu prototipe?', 'back': 'Model awal produk untuk diuji sebelum produksi.'},
        ],
        'checkpoint': (
            'Agar pakan tidak berjamur, wadah pakan harus…',
            [
                ('Bersih dan tertutup rapat', True),
                ('Terbuka dan lembap', False),
                ('Diisi air', False),
                ('Dibiarkan terkena hujan', False),
            ],
            'Wadah yang bersih dan tertutup rapat menjaga pakan tetap kering dan tidak berjamur.',
        ),
        'challenge': challenge_block(
            'pra-7-tantangan',
            'Tantangan istilah pakan otomatis',
            90,
            [
                ('Makanan hewan piaraan', 'pakan'),
                ('Pengatur jadwal', 'timer'),
                ('Komponen pembuka saluran', 'motor penggerak'),
                ('Model awal produk', 'prototipe'),
                ('Total biaya produksi', 'HPP'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Berapa kali pemberian pakan biasanya dilakukan dalam sehari?', 'Tiga kali', ['Satu kali', 'Lima kali', 'Tujuh kali'], 'Pemberian pakan biasanya dilakukan tiga kali sehari.', 'Jadwalnya pagi, siang, dan sore.'),
        ('Pakan harus disesuaikan dengan…', 'Jenis hewan', ['Warna kandang', 'Nama pemilik', 'Ukuran rumah'], 'Setiap hewan membutuhkan jenis pakan yang berbeda.', 'Ayam, ikan, dan kelinci berbeda pakannya.'),
        ('Apa kelebihan alat pakan otomatis?', 'Tepat waktu dan mudah digunakan', ['Membuat hewan sakit', 'Menambah pekerjaan', 'Mempercepat pakan rusak'], 'Alat pakan otomatis mengeluarkan pakan tepat waktu.', 'Pemilik tidak perlu selalu hadir.'),
        ('Alat pakan otomatis membantu saat…', 'Pemilik tidak berada di rumah', ['Hewan sedang tidur', 'Pakan habis selamanya', 'Kandang sedang dibersihkan'], 'Alat bekerja saat pemilik tidak ada di tempat.', 'Pakan tetap keluar sesuai jadwal.'),
        ('Komponen yang mengatur waktu pemberian pakan adalah…', 'Timer', ['Wadah pakan', 'Rangka', 'Saluran'], 'Timer menentukan kapan pakan dikeluarkan.', 'Timer dapat diatur sesuai jadwal.'),
        ('Tempat menyimpan pakan sebelum dikeluarkan disebut…', 'Wadah pakan', ['Timer', 'Motor', 'Rangka'], 'Wadah pakan menampung pakan sebelum jatuh ke tempat makan.', 'Wadah harus bersih dan tertutup.'),
        ('Manakah hewan yang biasa diberi pakan otomatis?', 'Ayam', ['Harimau', 'Gajah liar', 'Ikan hiu'], 'Ayam termasuk hewan piaraan yang umum diberi pakan otomatis.', 'Ikan dan kelinci juga umum.'),
        ('Pakan berkualitas memengaruhi…', 'Pertumbuhan dan perkembangan hewan', ['Warna kandang', 'Jumlah pemilik', 'Harga tanah'], 'Pakan berkualitas mendukung pertumbuhan hewan.', 'Gizi harus sesuai kebutuhan.'),
        ('Pemberian pakan secara manual berarti…', 'Diberikan langsung oleh pemilik', ['Diberikan oleh mesin', 'Diberikan tanpa jadwal', 'Diberikan oleh hewan lain'], 'Pakan manual diberikan langsung oleh pemilik.', 'Otomatis memakai alat.'),
        ('Mengapa menitipkan hewan kepada tetangga kurang ideal?', 'Merepotkan orang lain', ['Membuat hewan cepat besar', 'Menambah pakan', 'Mengurangi biaya'], 'Menitipkan hewan dapat merepotkan tetangga.', 'Alat otomatis menjadi alternatif.'),
        ('Alat pakan otomatis dapat dibuat secara…', 'Sederhana atau modern', ['Hanya modern', 'Hanya sederhana', 'Tidak mungkin dibuat'], 'Alat dapat dibuat sederhana maupun modern.', 'Sesuaikan dengan kebutuhan dan bahan.'),
        ('Komponen yang membuka dan menutup saluran pakan adalah…', 'Motor penggerak', ['Timer', 'Wadah', 'Rangka'], 'Motor penggerak menggerakkan mekanisme buka-tutup saluran.', 'Motor dikendalikan timer.'),
        ('Apa itu HPP?', 'Total biaya pembuatan produk', ['Harga jual akhir', 'Laba bersih', 'Pajak penjualan'], 'HPP adalah harga pokok produksi.', 'HPP menjadi dasar harga jual.'),
        ('Tahap akhir proyek alat pakan otomatis adalah…', 'Pameran dan evaluasi', ['Membuang produk', 'Membeli hewan baru', 'Menutup kandang'], 'Produk dipamerkan lalu dievaluasi untuk perbaikan.', 'Masukan membantu pengembangan.'),
    ],
    'multi': [
        ('Manakah hewan yang dapat memakai alat pakan otomatis?', ['Ayam', 'Ikan', 'Kelinci'], ['Harimau liar', 'Gajah'], 'Ayam, ikan, dan kelinci adalah hewan piaraan yang umum.', 'Harimau dan gajah bukan hewan piaraan rumah.'),
        ('Manakah komponen alat pakan otomatis?', ['Wadah pakan', 'Timer', 'Motor penggerak'], ['Gunting', 'Kuas'], 'Wadah, timer, dan motor adalah komponen alat pakan.', 'Gunting dan kuas bukan komponennya.'),
        ('Manakah ciri alat pakan otomatis yang baik?', ['Pakan keluar tepat waktu', 'Pakan tidak tersumbat'], ['Pakan menumpuk', 'Alat mudah roboh'], 'Alat yang baik menjaga jadwal dan kelancaran pakan.', 'Sumbatan dan rangka lemah merugikan.'),
        ('Apa manfaat alat pakan otomatis?', ['Menghemat waktu', 'Memberi pakan saat pemilik pergi'], ['Membuat pakan berjamur', 'Menambah pekerjaan manual'], 'Alat menghemat waktu dan bekerja saat pemilik tidak ada.', 'Pakan tetap terjadwal.'),
        ('Manakah bahan yang dapat dipakai membuat alat sederhana?', ['Botol', 'Pipa', 'Ember'], ['Kaca jendela', 'Cermin'], 'Botol, pipa, dan ember dapat dipakai sebagai wadah atau saluran.', 'Kaca dan cermin tidak cocok.'),
        ('Manakah prinsip kebersihan pakan?', ['Wadah ditutup rapat', 'Wadah dibersihkan berkala'], ['Wadah dibiarkan lembap', 'Pakan disimpan di tempat berair'], 'Wadah tertutup dan bersih mencegah jamur.', 'Kelembapan merusak pakan.'),
        ('Manakah komponen biaya HPP?', ['Bahan', 'Tenaga kerja'], ['Keuntungan penjual', 'Pajak konsumen'], 'HPP mencakup bahan dan tenaga kerja serta biaya produksi lain.', 'Keuntungan ditambahkan setelah HPP.'),
        ('Manakah tahap proyek alat pakan otomatis?', ['Observasi', 'Perancangan', 'Produksi', 'Evaluasi'], ['Menghindari uji coba', 'Membuang bahan sembarangan'], 'Proyek melalui observasi, perancangan, produksi, dan evaluasi.', 'Uji coba memastikan alat bekerja.'),
    ],
    'pairs': [
        ('Pakan', 'makanan untuk hewan piaraan'),
        ('Wadah pakan', 'tempat menyimpan pakan'),
        ('Timer', 'pengatur jadwal pemberian'),
        ('Motor penggerak', 'membuka dan menutup saluran'),
        ('Prototipe', 'model awal produk'),
        ('HPP', 'total biaya pembuatan produk'),
        ('Pameran', 'kegiatan mempresentasikan produk'),
        ('Otomatisasi', 'bekerja sendiri sesuai jadwal'),
    ],
    'steps': [
        ('Urutkan alur proyek alat pakan otomatis.', ['Observasi cara pemberian pakan', 'Perancangan alat', 'Persiapan alat dan bahan', 'Perakitan dan uji coba', 'Evaluasi produk'], 'Proyek bergerak dari observasi menuju evaluasi.', 'Rancangan dibuat sebelum perakitan.'),
        ('Urutkan langkah membuat alat pakan sederhana.', ['Siapkan wadah pakan', 'Buat saluran pengeluaran', 'Pasang motor penggerak', 'Pasang timer', 'Uji pengeluaran pakan'], 'Pembuatan dimulai dari wadah lalu pengujian.', 'Uji dengan pakan sesungguhnya.'),
        ('Urutkan langkah mengatur jadwal pakan.', ['Tentukan frekuensi pakan', 'Atur timer sesuai jam', 'Isi wadah pakan', 'Amati pakan keluar'], 'Jadwal disusun dari kebutuhan hewan lalu diatur pada timer.', 'Sesuaikan dengan kebiasaan hewan.'),
        ('Urutkan langkah merawat alat pakan.', ['Bersihkan wadah pakan', 'Periksa saluran', 'Periksa sambungan listrik', 'Ganti pakan basah'], 'Perawatan dimulai dari kebersihan wadah lalu pemeriksaan saluran.', 'Pakan basah harus segera diganti.'),
        ('Urutkan langkah presentasi produk.', ['Siapkan produk', 'Jelaskan cara kerja', 'Tunjukkan hasil uji', 'Terima masukan', 'Susun rencana perbaikan'], 'Presentasi menjelaskan produk dan membuka masukan.', 'Masukan dipakai untuk pengembangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
