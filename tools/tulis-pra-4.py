"""PRA 4 — Lampu Sensor Suara (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 4',
    'slug': 'prakarya-4-lampu-sensor-suara',
    'title': 'Lampu Sensor Suara',
    'description': (
        'Merancang dan membuat lampu sensor suara sederhana: mengenal jenis '
        'lampu, komponen elektronika, rangkaian, keselamatan listrik, dan HPP.'
    ),
    'objectives': [
        'Mengidentifikasi karakteristik bahan, alat, dan teknik lampu sensor suara.',
        'Membuat rancangan rangkaian lampu sensor suara berdasarkan kebutuhan.',
        'Merakit produk lampu sensor suara yang berfungsi dengan aman.',
        'Menghitung harga pokok produksi dan mengevaluasi produk.',
        'Mempresentasikan produk serta memberi saran pengembangan.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Rekayasa-BG-KLS-X.pdf Unit 1 Lampu Sensor Suara',
    'glossary': [
        {'term': 'Sensor suara', 'definition': 'Komponen yang mengubah suara menjadi sinyal listrik.'},
        {'term': 'Relay', 'definition': 'Komponen yang berfungsi sebagai saklar otomatis dalam rangkaian listrik.'},
        {'term': 'Resistor', 'definition': 'Komponen yang membatasi aliran arus listrik.'},
        {'term': 'Transistor', 'definition': 'Komponen yang memperkuat atau menyaklarkan sinyal listrik.'},
        {'term': 'LED', 'definition': 'Lampu dioda yang hemat energi dan berumur panjang.'},
        {'term': 'Otomatisasi', 'definition': 'Sistem yang bekerja sendiri berdasarkan masukan sensor tanpa campur tangan manusia.'},
        {'term': 'HPP', 'definition': 'Harga pokok produksi, yaitu total biaya yang dikeluarkan untuk membuat produk.'},
        {'term': 'Rangkaian', 'definition': 'Susunan komponen listrik yang saling terhubung agar membentuk fungsi tertentu.'},
    ],
    'intro': {
        'material_title': 'Mengapa lampu sensor suara bermanfaat?',
        'title': 'Lampu yang merespons suara',
        'paragraphs': [
            'Lampu sensor suara adalah produk rekayasa sederhana yang menyalakan lampu ketika mendeteksi suara, misalnya tepukan. Produk ini menggabungkan sensor suara, rangkaian elektronika, dan sumber cahaya.',
            'Teknologi terapan seperti ini membantu pekerjaan sehari-hari menjadi lebih mudah. Lampu dapat menyala tanpa harus mencari saklar, sehingga cocok untuk ruang gelap, gudang, atau area yang sulit dijangkau.',
            'Membuat lampu sensor suara melatih pemahaman rangkaian, ketelitian, dan keselamatan kerja. Produk juga dapat menjadi peluang usaha jika dikemas dan dipasarkan dengan baik.',
        ],
        'diagram': (
            'Alur kerja lampu sensor suara',
            'flowchart LR\n'
            '  A[Suara/tepukan] --> B[Sensor suara]\n'
            '  B --> C[Sinyal listrik diperkuat]\n'
            '  C --> D[Relay aktif]\n'
            '  D --> E[Lampu menyala]\n'
            '  E --> F[Lampu mati setelah jeda]',
        ),
        'callout': 'Jangan menyentuh rangkaian saat masih tersambung ke listrik. Lepaskan sumber daya sebelum memeriksa komponen.',
        'checkpoint': (
            'Apa fungsi sensor suara pada lampu sensor suara?',
            [
                ('Mengubah suara menjadi sinyal listrik', True),
                ('Menghasilkan cahaya', False),
                ('Menyimpan energi listrik', False),
                ('Mendinginkan lampu', False),
            ],
            'Sensor suara mengubah suara menjadi sinyal listrik yang diproses rangkaian.',
        ),
    },
    'concept': {
        'material_title': 'Lampu dan komponen elektronika',
        'title': 'Jenis lampu dan rangkaian dasar',
        'paragraphs': [
            'Lampu pijar menghasilkan cahaya dari filamen tungsten yang berpijar. Lampu neon memakai gas neon, sedangkan LED memakai dioda. LED paling hemat energi dan berumur panjang, sehingga banyak dipakai pada produk rekayasa.',
            'Rangkaian lampu sensor suara terdiri atas sensor suara, resistor, transistor, relay, dan sumber daya. Resistor membatasi arus, transistor memperkuat sinyal, dan relay bertindak sebagai saklar yang menghubungkan lampu ke sumber listrik.',
            'Setiap komponen memiliki nilai dan polaritas yang harus diperhatikan. Kesalahan pemasangan dapat membuat rangkaian tidak bekerja atau merusak komponen. Periksa kembali sebelum menghubungkan sumber daya.',
        ],
        'table': [
            ['Komponen', 'Fungsi', 'Catatan'],
            ['Sensor suara', 'Menangkap suara', 'Letakkan menghadap sumber suara'],
            ['Resistor', 'Membatasi arus', 'Nilai sesuai rancangan'],
            ['Transistor', 'Memperkuat sinyal', 'Perhatikan kaki basis, kolektor, emitor'],
            ['Relay', 'Saklar otomatis', 'Perhatikan tegangan kerja'],
            ['LED', 'Sumber cahaya', 'Perhatikan kutub positif dan negatif'],
        ],
        'visual': chart_block(
            'pra-4-daya-lampu',
            'Perkiraan konsumsi daya lampu (watt)',
            'bar',
            [('LED', 10), ('Neon kompak', 20), ('Halogen', 50), ('Pijar', 60)],
        ),
        'activity': categorize_block(
            'pra-4-klasifikasi',
            'Kelompokkan komponen berikut ke dalam sensor atau pengendali rangkaian.',
            [('b1', 'Sensor'), ('b2', 'Pengendali rangkaian')],
            [
                ('i1', 'Sensor suara', 'b1'),
                ('i2', 'Mikrofon', 'b1'),
                ('i3', 'Resistor', 'b2'),
                ('i4', 'Transistor', 'b2'),
                ('i5', 'Relay', 'b2'),
                ('i6', 'LED', 'b2'),
            ],
            'Tepat. Sensor suara dan mikrofon menangkap suara; resistor, transistor, relay, dan LED adalah bagian pengendali/keluaran.',
            'Periksa lagi: sensor menjadi masukan, komponen lain memproses atau mengeluarkan hasil.',
        ),
        'subtitle': 'Keselamatan dan HPP',
        'list': [
            'Gunakan sumber daya bertegangan rendah untuk latihan, misalnya baterai atau adaptor sesuai rancangan.',
            'Lepaskan sumber daya sebelum menyolder atau mengganti komponen.',
            'Jangan menyentuh bagian logam yang terbuka saat rangkaian aktif.',
            'Hitung HPP dari bahan, tenaga kerja, dan biaya lain agar harga jual tidak merugi.',
        ],
        'checkpoint': (
            'Komponen yang berfungsi sebagai saklar otomatis adalah…',
            [
                ('Relay', True),
                ('Resistor', False),
                ('LED', False),
                ('Mikrofon', False),
            ],
            'Relay menghubungkan atau memutus arus listrik secara otomatis berdasarkan sinyal kendali.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merakit lampu sensor suara',
        'paragraphs': [
            'Mulailah dari sketsa rangkaian. Tentukan letak sensor, relay, dan lampu. Pastikan jalur positif dan negatif tidak tertukar. Gunakan papan rangkaian agar komponen mudah dipasang dan diperiksa.',
            'Rakit komponen satu per satu, lalu periksa sambungan sebelum diberi daya. Uji dengan tepukan ringan dan amati apakah lampu menyala sesuai rancangan. Jika tidak bekerja, periksa kembali nilai resistor dan polaritas LED.',
            'Setelah rangkaian bekerja, pasang pada kotak yang aman. Beri lubang untuk sensor dan ventilasi. Hitung HPP, lalu presentasikan produk beserta cara kerjanya.',
        ],
        'scenario': scenario(
            'pra-4-skenario',
            'Lampu gudang yang gelap',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Gudang sekolah gelap dan saklar jauh dari pintu. Apa solusi yang paling tepat?',
                    'choices': [
                        {'text': 'Membuat lampu sensor suara di dekat pintu', 'next': 'n2', 'score': 2, 'feedback': 'Sensor suara memudahkan menyalakan lampu tanpa mencari saklar.'},
                        {'text': 'Menambah jumlah saklar di tempat yang sama', 'next': 'n3', 'score': 0, 'feedback': 'Saklar tetap sulit dijangkau dari pintu.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Lampu sering menyala karena suara kendaraan luar. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Mengatur sensitivitas sensor', 'next': 'n4', 'score': 2, 'feedback': 'Sensitivitas yang tepat mengurangi nyala palsu.'},
                        {'text': 'Membiarkannya agar lampu selalu menyala', 'next': 'n3', 'score': 0, 'feedback': 'Lampu menyala terus membuang energi.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk tidak nyaman dipakai dan boros energi.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Lampu menyala tepat saat dibutuhkan dan hemat energi.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa fungsi relay?', 'back': 'Saklar otomatis yang menghubungkan atau memutus arus listrik.'},
            {'front': 'Mengapa LED lebih hemat energi?', 'back': 'LED mengubah sebagian besar energi menjadi cahaya, bukan panas.'},
            {'front': 'Apa itu HPP?', 'back': 'Harga pokok produksi, yaitu total biaya pembuatan produk.'},
            {'front': 'Apa yang harus dilakukan sebelum menyolder?', 'back': 'Melepaskan sumber daya listrik.'},
        ],
        'checkpoint': (
            'Sebelum memberi daya pada rangkaian, langkah yang wajib dilakukan adalah…',
            [
                ('Memeriksa sambungan dan polaritas komponen', True),
                ('Menyentuh semua kabel', False),
                ('Menambah tegangan setinggi mungkin', False),
                ('Melepas resistor', False),
            ],
            'Pemeriksaan sambungan dan polaritas mencegah korsleting serta kerusakan komponen.',
        ),
        'challenge': challenge_block(
            'pra-4-tantangan',
            'Tantangan istilah lampu sensor suara',
            90,
            [
                ('Komponen pengubah suara menjadi sinyal', 'sensor suara'),
                ('Saklar otomatis', 'relay'),
                ('Lampu hemat energi', 'LED'),
                ('Total biaya produksi', 'HPP'),
                ('Penemu bola lampu pijar', 'Thomas Alva Edison'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Siapa penemu bola lampu pijar?', 'Thomas Alva Edison', ['James Watt', 'Nikola Tesla', 'Alexander Graham Bell'], 'Edison berhasil mengembangkan bola lampu pijar pada 1879.', 'Ia melakukan banyak percobaan sebelum berhasil.'),
        ('Lampu yang paling hemat energi adalah…', 'LED', ['Lampu pijar', 'Lampu halogen', 'Lampu HID'], 'LED mengubah energi menjadi cahaya lebih efisien daripada lampu lain.', 'LED juga berumur panjang.'),
        ('Lampu pijar menghasilkan cahaya dari filamen…', 'Tungsten', ['Tembaga', 'Aluminium', 'Karbon'], 'Filamen tungsten berpijar ketika dialiri listrik.', 'Filamen mudah putus karena panas.'),
        ('Apa fungsi sensor suara?', 'Mengubah suara menjadi sinyal listrik', ['Menghasilkan cahaya', 'Menyimpan daya', 'Mendinginkan rangkaian'], 'Sensor suara menangkap suara dan mengubahnya menjadi sinyal listrik.', 'Sinyal kemudian diproses rangkaian.'),
        ('Apa fungsi relay?', 'Saklar otomatis', ['Pembatas arus', 'Sumber cahaya', 'Penyimpan energi'], 'Relay menghubungkan atau memutus arus secara otomatis.', 'Relay dikendalikan sinyal listrik kecil.'),
        ('Apa fungsi resistor?', 'Membatasi arus listrik', ['Memperbesar cahaya', 'Menyimpan suara', 'Mengubah arus menjadi suara'], 'Resistor membatasi aliran arus agar komponen aman.', 'Nilai resistor diukur dalam ohm.'),
        ('Apa satuan hambatan listrik?', 'Ohm', ['Volt', 'Ampere', 'Watt'], 'Hambatan listrik diukur dalam ohm.', 'Simbolnya Ω.'),
        ('Apa fungsi transistor dalam rangkaian?', 'Memperkuat atau menyaklarkan sinyal', ['Menghasilkan cahaya', 'Menyimpan air', 'Mengubah warna'], 'Transistor memperkuat sinyal dari sensor agar relay aktif.', 'Transistor memiliki tiga kaki.'),
        ('Lampu neon menghasilkan cahaya dari gas…', 'Neon', ['Oksigen', 'Nitrogen', 'Helium'], 'Lampu neon berisi gas neon yang berpendar saat dialiri listrik.', 'Lampu ini lebih terang dari lampu pijar.'),
        ('Lampu LED menggunakan komponen…', 'Dioda', ['Filamen tungsten', 'Gas neon', 'Kawat karbon'], 'LED adalah light emitting diode yang memakai dioda.', 'Kutub LED harus dipasang benar.'),
        ('Apa yang dimaksud otomatisasi?', 'Sistem bekerja sendiri berdasarkan sensor', ['Sistem yang selalu manual', 'Sistem tanpa listrik', 'Sistem yang hanya dinyalakan tangan'], 'Otomatisasi membuat alat bekerja sendiri setelah mendapat masukan sensor.', 'Contohnya lampu menyala saat ada suara.'),
        ('Apa itu HPP?', 'Harga pokok produksi', ['Harga jual akhir', 'Laba bersih', 'Pajak penjualan'], 'HPP adalah total biaya yang dikeluarkan untuk membuat produk.', 'HPP menjadi dasar penentuan harga jual.'),
        ('Apa yang harus dilakukan sebelum menyolder rangkaian?', 'Melepaskan sumber daya listrik', ['Menambah tegangan', 'Menyentuh kabel terbuka', 'Membasahi rangkaian'], 'Sumber daya harus dilepas agar aman saat menyolder.', 'Gunakan alat solder dengan hati-hati.'),
        ('Mengapa lampu LED cocok untuk produk rekayasa?', 'Hemat energi dan berumur panjang', ['Cepat panas dan mudah putus', 'Membutuhkan gas neon', 'Tidak dapat dipasang pada rangkaian'], 'LED hemat energi, terang, dan tahan lama.', 'LED juga tersedia dalam berbagai warna.'),
    ],
    'multi': [
        ('Manakah yang termasuk komponen rangkaian lampu sensor suara?', ['Sensor suara', 'Relay', 'Resistor'], ['Pompa air', 'Tanah liat'], 'Sensor suara, relay, dan resistor adalah komponen rangkaian.', 'Pompa air dan tanah liat bukan komponen rangkaian ini.'),
        ('Manakah yang termasuk jenis lampu?', ['Lampu pijar', 'Lampu neon', 'LED'], ['Lampu taman', 'Lampu lalu lintas'], 'Lampu pijar, neon, dan LED adalah jenis lampu.', 'Lampu taman dan lalu lintas adalah penerapan.'),
        ('Apa fungsi sensor suara pada produk?', ['Menangkap suara', 'Memicu rangkaian'], ['Menghasilkan air', 'Menghitung HPP'], 'Sensor menangkap suara dan memicu rangkaian.', 'HPP dihitung terpisah.'),
        ('Manakah prinsip keselamatan listrik?', ['Melepas sumber daya sebelum memeriksa', 'Tidak menyentuh bagian terbuka saat aktif'], ['Bekerja dengan tangan basah', 'Menambah tegangan tanpa alat ukur'], 'Sumber daya dilepas dan bagian terbuka tidak disentuh saat aktif.', 'Tangan basah sangat berbahaya.'),
        ('Manakah tahap proyek rekayasa?', ['Observasi', 'Perancangan', 'Produksi', 'Evaluasi'], ['Menghindari uji coba', 'Membuang bahan sembarangan'], 'Proyek melalui observasi, perancangan, produksi, dan evaluasi.', 'Uji coba bagian penting dari produksi.'),
        ('Manakah komponen biaya HPP?', ['Bahan', 'Tenaga kerja'], ['Keuntungan penjual', 'Pajak konsumen'], 'HPP mencakup bahan dan tenaga kerja serta biaya produksi lain.', 'Keuntungan ditambahkan setelah HPP.'),
        ('Manakah ciri lampu hemat energi?', ['Daya listrik kecil', 'Umur pakai panjang'], ['Cepat panas', 'Mudah putus'], 'Lampu hemat energi memakai daya kecil dan tahan lama.', 'LED memenuhi ciri ini.'),
        ('Manakah urutan perakitan yang benar?', ['Menyiapkan komponen', 'Merakit rangkaian', 'Memeriksa sambungan', 'Menguji produk'], ['Langsung memberi daya tanpa memeriksa', 'Membongkar produk setelah jadi'], 'Perakitan dimulai dari persiapan lalu pemeriksaan sebelum uji.', 'Pemeriksaan mencegah kerusakan.'),
    ],
    'pairs': [
        ('Sensor suara', 'mengubah suara menjadi sinyal listrik'),
        ('Relay', 'saklar otomatis'),
        ('Resistor', 'membatasi arus listrik'),
        ('Transistor', 'memperkuat sinyal'),
        ('LED', 'lampu dioda hemat energi'),
        ('HPP', 'total biaya pembuatan produk'),
        ('Otomatisasi', 'bekerja sendiri berdasarkan sensor'),
        ('Edison', 'penemu bola lampu pijar'),
    ],
    'steps': [
        ('Urutkan alur proyek lampu sensor suara.', ['Observasi kebutuhan', 'Perancangan rangkaian', 'Persiapan alat dan bahan', 'Perakitan dan uji coba', 'Evaluasi produk'], 'Proyek bergerak dari observasi menuju evaluasi.', 'Rancangan dibuat sebelum perakitan.'),
        ('Urutkan langkah merakit rangkaian.', ['Siapkan papan rangkaian', 'Pasang sensor suara', 'Pasang resistor dan transistor', 'Pasang relay dan lampu', 'Periksa sambungan'], 'Perakitan dimulai dari komponen masukan menuju keluaran.', 'Periksa sambungan sebelum diberi daya.'),
        ('Urutkan langkah menguji produk.', ['Pastikan rangkaian kering', 'Hubungkan sumber daya', 'Beri suara/tepukan', 'Amati respons lampu', 'Catat hasil pengujian'], 'Pengujian dilakukan setelah rangkaian siap dan aman.', 'Catat hasil untuk perbaikan.'),
        ('Urutkan langkah menghitung HPP.', ['Catat biaya bahan', 'Hitung biaya tenaga kerja', 'Tambahkan biaya lain', 'Jumlahkan seluruh biaya'], 'HPP dihitung dari seluruh biaya produksi.', 'HPP menjadi dasar harga jual.'),
        ('Urutkan langkah presentasi produk.', ['Siapkan produk', 'Jelaskan cara kerja', 'Tunjukkan hasil uji', 'Terima masukan', 'Susun rencana perbaikan'], 'Presentasi menjelaskan produk dan membuka masukan.', 'Masukan dipakai untuk pengembangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
