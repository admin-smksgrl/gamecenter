"""PRA 5 — Alat Pendeteksi Hujan (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 5',
    'slug': 'prakarya-5-pendeteksi-hujan',
    'title': 'Alat Pendeteksi Hujan',
    'description': (
        'Merancang alat pendeteksi hujan sederhana: memahami pemanasan global, '
        'curah hujan, sensor hujan, buzzer, mitigasi bencana, dan keselamatan listrik.'
    ),
    'objectives': [
        'Menganalisis kebutuhan alat pendeteksi hujan di lingkungan sekitar.',
        'Mengidentifikasi bahan, alat, dan komponen alat pendeteksi hujan.',
        'Merancang rangkaian dan konstruksi alat pendeteksi hujan.',
        'Membuat serta menguji alat pendeteksi hujan yang berfungsi.',
        'Mempresentasikan produk dan menyusun rencana pengembangan.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Rekayasa-BG-KLS-X.pdf Unit 2 Alat Pendeteksi Hujan',
    'glossary': [
        {'term': 'Sensor hujan', 'definition': 'Komponen yang mendeteksi keberadaan air hujan pada permukaannya.'},
        {'term': 'Buzzer', 'definition': 'Komponen listrik yang menghasilkan bunyi sebagai tanda peringatan.'},
        {'term': 'Mitigasi', 'definition': 'Upaya pencegahan dan pengurangan risiko sebelum bencana terjadi.'},
        {'term': 'Curah hujan', 'definition': 'Jumlah air hujan yang jatuh pada suatu area dalam waktu tertentu.'},
        {'term': 'BMKG', 'definition': 'Badan Meteorologi, Klimatologi, dan Geofisika yang mengukur cuaca di Indonesia.'},
        {'term': 'Pemanasan global', 'definition': 'Kenaikan suhu bumi akibat menumpuknya gas rumah kaca di atmosfer.'},
        {'term': 'Peringatan dini', 'definition': 'Tanda atau informasi yang diberikan sebelum bencana terjadi.'},
        {'term': 'Otomatisasi', 'definition': 'Sistem yang bekerja sendiri berdasarkan masukan sensor.'},
    ],
    'intro': {
        'material_title': 'Mengapa alat pendeteksi hujan penting?',
        'title': 'Waspada sebelum hujan turun',
        'paragraphs': [
            'Alat pendeteksi hujan adalah produk rekayasa sederhana yang memberi peringatan ketika hujan mulai turun. Alat ini memakai sensor hujan yang mengirim sinyal listrik saat terkena air, lalu rangkaian membunyikan buzzer atau menyalakan lampu.',
            'Indonesia memiliki dua musim, yaitu musim kemarau dan musim hujan. Perubahan iklim membuat datangnya musim makin sulit diprediksi. Hujan lebat yang berlangsung lama dapat memicu banjir dan longsor, sehingga masyarakat membutuhkan peringatan dini.',
            'Alat pendeteksi hujan dapat dipasang di rumah, sekolah, atau pos ronda. Dengan peringatan sederhana, warga punya waktu untuk menyelamatkan barang, memeriksa saluran air, dan bersiap menghadapi kemungkinan banjir.',
        ],
        'diagram': (
            'Alur kerja alat pendeteksi hujan',
            'flowchart LR\n'
            '  A[Hujan turun] --> B[Sensor hujan terkena air]\n'
            '  B --> C[Sinyal listrik dikirim]\n'
            '  C --> D[Rangkaian memproses sinyal]\n'
            '  D --> E[Buzzer berbunyi]\n'
            '  E --> F[Warga waspada]',
        ),
        'callout': 'Gunakan sumber daya bertegangan rendah dan lindungi rangkaian dari air. Jangan menyentuh komponen saat alat masih tersambung listrik.',
        'checkpoint': (
            'Apa fungsi utama alat pendeteksi hujan?',
            [
                ('Memberi peringatan saat hujan turun', True),
                ('Menyaring air hujan menjadi air minum', False),
                ('Menghentikan hujan', False),
                ('Menghitung jumlah tanaman', False),
            ],
            'Alat pendeteksi hujan memberi peringatan ketika sensor mendeteksi air hujan.',
        ),
    },
    'concept': {
        'material_title': 'Sensor, rangkaian, dan curah hujan',
        'title': 'Cara kerja dan komponen alat',
        'paragraphs': [
            'Sensor hujan bekerja seperti saklar yang aktif ketika air mengenai pelat sensornya. Air menghantarkan arus listrik di antara jalur pelat, sehingga rangkaian mendeteksi adanya hujan. Sinyal itu kemudian mengaktifkan buzzer atau lampu indikator.',
            'Komponen pendukung alat antara lain resistor, transistor, buzzer, LED, kabel, dan sumber daya. Resistor membatasi arus, transistor memperkuat sinyal, buzzer menghasilkan bunyi, sedangkan LED memberi tanda visual. Semua komponen dirangkai pada papan agar mudah diperiksa.',
            'BMKG mengelompokkan curah hujan harian menjadi sangat ringan (<5 mm), ringan (5–20 mm), sedang (21–50 mm), lebat (51–100 mm), dan sangat lebat (>100 mm). Kategori ini membantu menentukan tingkat kewaspadaan terhadap banjir.',
        ],
        'table': [
            ['Komponen', 'Fungsi', 'Catatan'],
            ['Sensor hujan', 'Mendeteksi air hujan', 'Letakkan di area terbuka'],
            ['Resistor', 'Membatasi arus listrik', 'Nilai sesuai rancangan'],
            ['Transistor', 'Memperkuat sinyal', 'Perhatikan susunan kaki'],
            ['Buzzer', 'Menghasilkan bunyi peringatan', 'Pilih tegangan kerja sesuai sumber'],
            ['LED', 'Memberi tanda visual', 'Perhatikan kutub positif dan negatif'],
        ],
        'visual': chart_block(
            'pra-5-curah-hujan',
            'Batas atas kategori curah hujan harian (mm)',
            'bar',
            [('Sangat ringan', 5), ('Ringan', 20), ('Sedang', 50), ('Lebat', 100), ('Sangat lebat', 150)],
        ),
        'activity': categorize_block(
            'pra-5-klasifikasi',
            'Kelompokkan komponen berikut ke dalam masukan atau keluaran rangkaian.',
            [('b1', 'Masukan'), ('b2', 'Keluaran')],
            [
                ('i1', 'Sensor hujan', 'b1'),
                ('i2', 'Pelat sensor', 'b1'),
                ('i3', 'Buzzer', 'b2'),
                ('i4', 'LED indikator', 'b2'),
                ('i5', 'Speaker kecil', 'b2'),
                ('i6', 'Lampu peringatan', 'b2'),
            ],
            'Tepat. Sensor hujan dan pelat sensor menjadi masukan; buzzer, LED, speaker, dan lampu adalah keluaran.',
            'Periksa lagi: masukan membaca kondisi, keluaran memberi tanda kepada pengguna.',
        ),
        'subtitle': 'Mitigasi dan keselamatan',
        'list': [
            'Bersihkan saluran air dan selokan sebelum musim hujan agar air tidak menggenang.',
            'Simpan dokumen penting di tempat yang tinggi dan tahan air.',
            'Pasang alat pada tempat yang aman dari jangkauan anak kecil dan air tergenang.',
            'Periksa sensor secara berkala karena debu dan daun dapat menutupi pelat.',
        ],
        'checkpoint': (
            'Curah hujan 51–100 mm per 24 jam termasuk kategori…',
            [
                ('Lebat', True),
                ('Ringan', False),
                ('Sedang', False),
                ('Sangat ringan', False),
            ],
            'BMKG menetapkan curah hujan 51–100 mm/24 jam sebagai kategori lebat.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat peringatan dini sederhana',
        'paragraphs': [
            'Amati lingkungan sekolah atau rumah. Tentukan lokasi yang sering tergenang dan jauh dari suara bising agar bunyi buzzer terdengar jelas. Ukur ketinggian tempat pemasangan supaya sensor mudah terkena hujan tetapi tidak terendam.',
            'Rakit rangkaian pada papan, lalu hubungkan sensor, buzzer, dan sumber daya. Periksa kembali sambungan sebelum diberi daya. Uji dengan meneteskan air bersih pada pelat sensor dan amati apakah buzzer berbunyi.',
            'Setelah alat bekerja, pasang pada kotak pelindung yang memiliki lubang untuk sensor. Hitung biaya bahan, lalu presentasikan cara kerja dan manfaat alat kepada warga sekolah.',
        ],
        'scenario': scenario(
            'pra-5-skenario',
            'Peringatan dini di sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Sekolahmu sering tergenang saat hujan lebat. Apa langkah paling tepat?',
                    'choices': [
                        {'text': 'Membuat alat pendeteksi hujan dan membersihkan saluran air', 'next': 'n2', 'score': 2, 'feedback': 'Peringatan dini disertai mitigasi mengurangi risiko banjir.'},
                        {'text': 'Menunggu sampai air masuk ke kelas', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa persiapan, kerugian akan lebih besar.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Buzzer sering berbunyi karena tetesan embun pagi. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menempatkan sensor agar mudah kering dan dijemur sinar matahari', 'next': 'n4', 'score': 2, 'feedback': 'Penempatan yang tepat mengurangi peringatan palsu.'},
                        {'text': 'Mematikan alat selamanya', 'next': 'n3', 'score': 0, 'feedback': 'Alat yang dimatikan tidak berguna saat hujan sebenarnya.'},
                    ],
                },
                {'id': 'n3', 'text': 'Barang di sekolah basah dan kegiatan terganggu.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Peringatan bekerja tepat dan warga sekolah lebih siap.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa fungsi sensor hujan?', 'back': 'Mendeteksi air hujan dan mengirim sinyal listrik.'},
            {'front': 'Apa itu mitigasi bencana?', 'back': 'Upaya pencegahan dan pengurangan risiko sebelum bencana.'},
            {'front': 'Berapa kategori curah hujan BMKG?', 'back': 'Lima: sangat ringan, ringan, sedang, lebat, dan sangat lebat.'},
            {'front': 'Mengapa sensor perlu dibersihkan?', 'back': 'Debu dan daun dapat menghalangi deteksi air hujan.'},
        ],
        'checkpoint': (
            'Agar alat pendeteksi hujan tidak sering memberi peringatan palsu, hal yang perlu diperhatikan adalah…',
            [
                ('Penempatan sensor dan kebersihannya', True),
                ('Warna kotak alat', False),
                ('Jumlah kabel yang dipakai', False),
                ('Merek sumber daya', False),
            ],
            'Sensor yang bersih dan ditempatkan dengan tepat mengurangi peringatan palsu.',
        ),
        'challenge': challenge_block(
            'pra-5-tantangan',
            'Tantangan istilah pendeteksi hujan',
            90,
            [
                ('Komponen pendeteksi air', 'sensor hujan'),
                ('Komponen penghasil bunyi', 'buzzer'),
                ('Upaya pencegahan bencana', 'mitigasi'),
                ('Lembaga pengukur cuaca', 'BMKG'),
                ('Peringatan sebelum bencana', 'peringatan dini'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa fungsi utama alat pendeteksi hujan?', 'Memberi peringatan saat hujan turun', ['Menyaring air hujan', 'Menghentikan hujan', 'Menghitung tanaman'], 'Alat pendeteksi hujan memberi peringatan ketika sensor mendeteksi air.', 'Peringatan membantu warga bersiap.'),
        ('Komponen utama pendeteksi hujan adalah…', 'Sensor hujan', ['Pompa air', 'Motor servo', 'Panel surya'], 'Sensor hujan mendeteksi keberadaan air hujan.', 'Sensor menjadi masukan bagi rangkaian.'),
        ('Apa yang terjadi pada sensor hujan saat terkena air?', 'Mengirim sinyal listrik', ['Mengeluarkan asap', 'Berubah menjadi es', 'Menghasilkan air bersih'], 'Air menghantarkan arus sehingga sensor mengirim sinyal.', 'Sinyal memicu buzzer.'),
        ('Apa fungsi buzzer?', 'Menghasilkan bunyi peringatan', ['Membatasi arus', 'Menyimpan daya', 'Mendinginkan alat'], 'Buzzer menghasilkan bunyi sebagai tanda peringatan.', 'Bunyi harus terdengar jelas.'),
        ('Lembaga yang mengukur curah hujan di Indonesia adalah…', 'BMKG', ['BNPB', 'Kemendikbud', 'WHO'], 'BMKG mengukur dan mengumumkan data cuaca serta curah hujan.', 'Data BMKG menjadi acuan kewaspadaan.'),
        ('Curah hujan 51–100 mm per 24 jam termasuk kategori…', 'Lebat', ['Ringan', 'Sedang', 'Sangat ringan'], 'Kategori lebat berada pada rentang 51–100 mm/24 jam.', 'Di atas 100 mm disebut sangat lebat.'),
        ('Curah hujan lebih dari 100 mm per 24 jam termasuk kategori…', 'Sangat lebat', ['Lebat', 'Sedang', 'Ringan'], 'Curah hujan di atas 100 mm/24 jam disebut sangat lebat.', 'Kategori ini berpotensi memicu banjir.'),
        ('Curah hujan kurang dari 5 mm per 24 jam termasuk kategori…', 'Sangat ringan', ['Ringan', 'Sedang', 'Lebat'], 'Curah hujan di bawah 5 mm/24 jam termasuk sangat ringan.', 'Kategorinya paling rendah.'),
        ('Musim hujan di Indonesia umumnya terjadi pada…', 'Oktober–April', ['April–Oktober', 'Juni–September', 'Januari–Maret'], 'Musim hujan umumnya berlangsung Oktober–April, sedangkan kemarau April–Oktober.', 'Musim bergantian sepanjang tahun.'),
        ('Upaya pencegahan dan pengurangan risiko bencana disebut…', 'Mitigasi', ['Evakuasi', 'Rehabilitasi', 'Relokasi'], 'Mitigasi adalah upaya pencegahan sebelum bencana terjadi.', 'Contohnya membuat peringatan dini.'),
        ('Dampak pemanasan global terhadap cuaca adalah…', 'Iklim menjadi tidak stabil', ['Cuaca selalu dingin', 'Hujan berhenti selamanya', 'Angin tidak pernah bertiup'], 'Pemanasan global membuat iklim dan cuaca tidak stabil.', 'Musim datang tidak menentu.'),
        ('Mengapa alat pendeteksi hujan penting bagi daerah rawan banjir?', 'Memberi waktu bersiap sebelum banjir', ['Menambah tinggi air', 'Mempercepat banjir', 'Menghilangkan saluran air'], 'Peringatan dini memberi waktu untuk menyelamatkan barang dan bersiap.', 'Warga dapat waspada lebih awal.'),
        ('Saat peringatan hujan lebat berbunyi, tindakan yang tepat adalah…', 'Waspada dan memeriksa saluran air', ['Bermain di air genangan', 'Membuang sampah ke selokan', 'Membiarkan jendela terbuka'], 'Kewaspadaan dan pemeriksaan saluran air mengurangi risiko banjir.', 'Jangan bermain di air genangan.'),
        ('Alat pendeteksi hujan sebaiknya dipasang di…', 'Area terbuka yang terkena hujan', ['Dalam lemari tertutup', 'Di bawah meja', 'Dalam ruangan ber-AC'], 'Sensor harus terkena hujan agar dapat mendeteksi.', 'Namun rangkaian tetap harus terlindungi air.'),
    ],
    'multi': [
        ('Manakah komponen alat pendeteksi hujan?', ['Sensor hujan', 'Buzzer', 'LED'], ['Pompa air', 'Motor servo'], 'Sensor hujan, buzzer, dan LED adalah komponen alat pendeteksi hujan.', 'Pompa dan servo bukan komponen utamanya.'),
        ('Manakah kategori curah hujan BMKG?', ['Ringan', 'Sedang', 'Lebat'], ['Berat', 'Ekstrem'], 'BMKG memakai kategori sangat ringan, ringan, sedang, lebat, dan sangat lebat.', 'Istilah “berat” dan “ekstrem” bukan kategori resminya.'),
        ('Manakah dampak pemanasan global?', ['Iklim tidak stabil', 'Permukaan air laut naik', 'Kekeringan berkepanjangan'], ['Hujan salju di seluruh Indonesia', 'Suhu bumi turun drastis'], 'Pemanasan global membuat iklim tidak stabil, air laut naik, dan kekeringan.', 'Suhu bumi justru cenderung naik.'),
        ('Apa fungsi sensor hujan pada alat?', ['Mendeteksi air', 'Memicu peringatan'], ['Menyalakan pompa', 'Mengubah suhu ruangan'], 'Sensor mendeteksi air lalu memicu peringatan.', 'Pompa bukan bagian alat ini.'),
        ('Manakah tindakan mitigasi banjir?', ['Membersihkan saluran air', 'Membuat peringatan dini'], ['Membuang sampah ke sungai', 'Menebang pohon sembarangan'], 'Membersihkan saluran dan membuat peringatan dini mengurangi risiko banjir.', 'Membuang sampah justru memperparah banjir.'),
        ('Manakah bahan atau alat yang dipakai?', ['Pelat sensor', 'Kabel', 'Baterai'], ['Tanah liat', 'Benang sulam'], 'Pelat sensor, kabel, dan baterai dipakai pada rangkaian.', 'Tanah liat dan benang sulam untuk kerajinan.'),
        ('Manakah ciri alat pendeteksi hujan bekerja baik?', ['Berbunyi saat ada air', 'Bunyi terdengar jelas'], ['Menyala terus tanpa air', 'Tidak pernah berbunyi'], 'Alat yang baik merespons air dan bunyinya jelas.', 'Nyala terus tanpa air menandakan gangguan.'),
        ('Manakah tahap proyek alat pendeteksi hujan?', ['Observasi', 'Perancangan', 'Produksi', 'Evaluasi'], ['Menghindari uji coba', 'Membuang bahan sembarangan'], 'Proyek melalui observasi, perancangan, produksi, dan evaluasi.', 'Uji coba bagian penting dari produksi.'),
    ],
    'pairs': [
        ('Sensor hujan', 'mendeteksi air hujan'),
        ('Buzzer', 'menghasilkan bunyi peringatan'),
        ('Mitigasi', 'upaya pencegahan bencana'),
        ('BMKG', 'lembaga pengukur cuaca'),
        ('Curah hujan lebat', '51–100 mm per 24 jam'),
        ('Pemanasan global', 'kenaikan suhu bumi'),
        ('Peringatan dini', 'tanda sebelum bencana terjadi'),
        ('HPP', 'total biaya pembuatan produk'),
    ],
    'steps': [
        ('Urutkan alur proyek alat pendeteksi hujan.', ['Observasi kebutuhan', 'Perancangan rangkaian', 'Persiapan alat dan bahan', 'Perakitan dan uji coba', 'Evaluasi produk'], 'Proyek bergerak dari observasi menuju evaluasi.', 'Rancangan dibuat sebelum perakitan.'),
        ('Urutkan langkah merakit alat.', ['Siapkan papan rangkaian', 'Pasang sensor hujan', 'Pasang resistor dan transistor', 'Pasang buzzer dan LED', 'Periksa sambungan'], 'Perakitan dimulai dari masukan menuju keluaran.', 'Periksa sambungan sebelum diberi daya.'),
        ('Urutkan langkah menguji alat.', ['Pastikan rangkaian kering', 'Hubungkan sumber daya', 'Tetesi pelat sensor dengan air', 'Amati bunyi dan lampu', 'Catat hasil pengujian'], 'Pengujian dilakukan setelah rangkaian siap dan aman.', 'Catat hasil untuk perbaikan.'),
        ('Urutkan langkah mitigasi banjir.', ['Bersihkan saluran air', 'Simpan dokumen di tempat tinggi', 'Pasang peringatan dini', 'Pantau informasi cuaca'], 'Mitigasi dimulai dari kebersihan saluran lalu kesiapan warga.', 'Pantau informasi BMKG secara berkala.'),
        ('Urutkan langkah presentasi produk.', ['Siapkan produk', 'Jelaskan cara kerja', 'Tunjukkan hasil uji', 'Terima masukan', 'Susun rencana perbaikan'], 'Presentasi menjelaskan produk dan membuka masukan.', 'Masukan dipakai untuk pengembangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
