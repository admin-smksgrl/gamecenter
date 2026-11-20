"""IPAS 5 — Membangun Kota Bebas Polusi melalui Energi Ramah Lingkungan (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'IPAS 5',
    'slug': 'ipas-5-energi-ramah-lingkungan',
    'title': 'Membangun Kota Bebas Polusi melalui Energi Ramah Lingkungan',
    'description': (
        'Menelaah kebutuhan dan konsumsi energi nasional, memahami konsep, bentuk, '
        'sumber, dan transformasi energi, serta merancang purwarupa energi terbarukan '
        'yang diuji dengan pengukuran daya dan energi.'
    ),
    'objectives': [
        'Menjelaskan kebutuhan dan konsumsi energi di Indonesia.',
        'Membedakan bentuk dan sumber energi serta transformasinya.',
        'Menghitung daya dan energi listrik hasil purwarupa.',
        'Memilih sumber energi terbarukan yang sesuai potensi setempat.',
        'Merancang, menguji, dan mengevaluasi projek energi ramah lingkungan.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 5 Membangun Kota Bebas Polusi melalui Energi '
        'Ramah Lingkungan; CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'Energi', 'definition': 'Kemampuan melakukan kerja atau usaha dan mengalami perubahan.'},
        {'term': 'Transformasi energi', 'definition': 'Perubahan bentuk energi dari satu bentuk ke bentuk lainnya.'},
        {'term': 'Energi terbarukan', 'definition': 'Sumber energi yang berasal dari alam dan dapat dipakai terus-menerus.'},
        {'term': 'Panel surya', 'definition': 'Alat yang mengubah energi cahaya menjadi energi listrik melalui efek fotovoltaik.'},
        {'term': 'Biomassa', 'definition': 'Bahan organik dari makhluk hidup yang dapat diolah menjadi energi.'},
        {'term': 'Krisis energi', 'definition': 'Kondisi kekurangan cadangan energi fosil sehingga pasokan dan harga terganggu.'},
        {'term': 'Rasio elektrifikasi', 'definition': 'Perbandingan jumlah rumah tangga berlistrik dengan jumlah rumah tangga total.'},
        {'term': 'Multimeter', 'definition': 'Alat ukur listrik untuk mengukur arus, tegangan, dan hambatan.'},
    ],
    'intro': {
        'material_title': 'Mengapa energi menjadi persoalan kota?',
        'title': 'Kebutuhan energi dan krisis energi',
        'paragraphs': [
            'Konsumsi energi nasional tahun 2021 mencapai 909,24 juta barel setara minyak, naik 0,4% dari tahun sebelumnya. Angka ini lebih rendah daripada 2019 yang mencapai 1 miliar BOE karena pandemi, tetapi tetap tertinggi dalam satu dekade terakhir.',
            'Sektor transportasi adalah pengguna terbesar, yaitu 388,42 juta BOE atau 42,72% dari total konsumsi. Dari jenisnya, bensin mendominasi dengan 26%, diikuti solar/biodiesel 21,3%, dan listrik 18,5%.',
            'Ketergantungan pada bahan bakar fosil membuat pasokan menipis, harga melambung, dan emisi karbon meningkat. Rasio elektrifikasi 2022 sudah 99,63%, tetapi sebagian wilayah masih mengalami pemadaman bergilir.',
        ],
        'diagram': (
            'Dari sumber energi menjadi listrik',
            'flowchart LR\n'
            '  A[Sumber energi] --> B[Pembangkit]\n'
            '  B --> C[Generator menghasilkan listrik]\n'
            '  C --> D[Transmisi dan distribusi]\n'
            '  D --> E[Rumah, sekolah, industri]\n'
            '  E --> F[Transformasi menjadi energi lain]',
        ),
        'callout': 'Hemat energi adalah solusi tercepat: mematikan alat yang tidak dipakai menurunkan emisi tanpa perlu membangun pembangkit baru.',
        'checkpoint': (
            'Apa satuan energi dalam Sistem Internasional?',
            [
                ('joule', True),
                ('watt', False),
                ('ampere', False),
                ('newton', False),
            ],
            'Satuan SI energi adalah joule; watt adalah satuan daya.',
        ),
    },
    'concept': {
        'material_title': 'Konsep, bentuk, dan sumber energi',
        'title': 'Bentuk energi dan sumber terbarukan',
        'paragraphs': [
            'Energi tidak dapat diciptakan dan tidak dapat dimusnahkan, tetapi dapat berubah bentuk. Setrika mengubah energi listrik menjadi energi termal, sedangkan tubuh mengubah energi kimia makanan menjadi energi gerak.',
            'Bentuk energi meliputi listrik, kimia, cahaya, termal, mekanik (kinetik dan potensial), magnet, dan nuklir. Satuannya dapat dikonversi: 1 kalori = 4,2 joule, 1 joule = 0,24 kalori, dan 1 kWh = 3.600.000 joule.',
            'Sumber energi terbarukan di Indonesia mencakup matahari (PLTS, panel surya, CSP), angin, air (PLTA), panas bumi (PLTP), gelombang laut, dan biomassa yang diolah menjadi biogas, etanol, serta biodiesel.',
        ],
        'table': [
            ['Sumber energi', 'Cara memanfaatkan', 'Contoh pembangkit atau alat'],
            ['Matahari', 'Panel surya dan cermin konsentrator', 'PLTS, solar home system'],
            ['Angin', 'Turbin digerakkan embusan angin', 'Pembangkit listrik tenaga angin'],
            ['Air', 'Aliran air memutar turbin', 'PLTA'],
            ['Panas bumi', 'Uap panas memutar turbin', 'PLTP'],
            ['Gelombang laut', 'Naik turun ombak memutar turbin', 'Pembangkit gelombang'],
            ['Biomassa', 'Fermentasi atau pembakaran bahan organik', 'Biodigester biogas'],
        ],
        'visual': chart_block(
            'ipas-5-konsumsi',
            'Konsumsi energi Indonesia 2021 menurut jenis (%)',
            'bar',
            [('Bensin', 26.0), ('Solar/biodiesel', 21.3), ('Listrik', 18.5), ('Gas alam', 9.9), ('Batu bara', 9.7), ('LPG', 8.0), ('Biomassa', 6.6)],
        ),
        'activity': categorize_block(
            'ipas-5-klasifikasi',
            'Kelompokkan sumber energi berikut menjadi terbarukan atau tak terbarukan.',
            [('b1', 'Terbarukan'), ('b2', 'Tak terbarukan')],
            [
                ('i1', 'Matahari', 'b1'),
                ('i2', 'Angin', 'b1'),
                ('i3', 'Panas bumi', 'b1'),
                ('i4', 'Biomassa', 'b1'),
                ('i5', 'Minyak bumi', 'b2'),
                ('i6', 'Batu bara', 'b2'),
                ('i7', 'Gas alam', 'b2'),
                ('i8', 'Solar dan bensin', 'b2'),
            ],
            'Tepat. Matahari, angin, panas bumi, dan biomassa dapat diperbarui, sedangkan fosil akan habis.',
            'Periksa lagi: minyak, batu bara, dan gas terbentuk selama jutaan tahun sehingga tidak terbarukan.',
        ),
        'subtitle': 'Mengukur daya dan energi purwarupa',
        'list': [
            'Mengukur tegangan memakai multimeter pada posisi DCV atau ACV, dengan skala lebih besar bila nilai belum diketahui.',
            'Mengukur arus pada posisi DCA dengan memutus jalur catu daya lalu menghubungkan probe secara seri.',
            'Menghitung daya dengan P = I × V dan energi dengan W = P × t.',
            'Menentukan variabel yang memengaruhi purwarupa, misalnya luas penampang pipa memengaruhi debit air kincir.',
        ],
        'checkpoint': (
            'Rumus daya listrik pada buku adalah…',
            [
                ('P = I × V', True),
                ('P = V ÷ I', False),
                ('P = I × t', False),
                ('P = W × t', False),
            ],
            'Daya (watt) sama dengan arus (ampere) dikali tegangan (volt).',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Projek energi ramah lingkungan',
        'paragraphs': [
            'Projek dimulai dengan mengidentifikasi masalah energi di sekitar: pemakaian lampu berlebihan, harga listrik naik, atau tidak ada sumber listrik di area tertentu. Setelah itu ditentukan alternatif solusi sesuai potensi lokal.',
            'Desain purwarupa memuat referensi, alat dan bahan, skala gambar, serta variabel yang memengaruhi kerja alat. Pembangunan purwarupa wajib mengikuti prosedur, jadwal, pembagian tugas, dan manajemen risiko.',
            'Uji coba mencatat arus dan tegangan untuk menghitung daya dan energi. Bila hasil belum sesuai kriteria rubrik, produk diperbaiki melalui desain ulang, lalu disosialisasikan atau dikembangkan produksinya.',
        ],
        'scenario': scenario(
            'ipas-5-skenario',
            'Lampu taman sekolah tanpa listrik',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Taman sekolah gelap pada malam hari dan sambungan listrik jauh. Apa langkah awal projek?',
                    'choices': [
                        {'text': 'Mengukur kebutuhan penerangan dan potensi energi setempat', 'next': 'n2', 'score': 2, 'feedback': 'Data kebutuhan dan potensi menentukan pilihan sumber energi.'},
                        {'text': 'Membeli lampu termahal tanpa hitungan', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa hitungan, biaya bisa membengkak dan alat tidak sesuai.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Taman terkena sinar matahari 7 jam sehari. Solusi apa yang dipilih?',
                    'choices': [
                        {'text': 'Lampu LED dengan panel surya dan baterai', 'next': 'n4', 'score': 2, 'feedback': 'Energi matahari tersedia dan tidak menambah tagihan listrik.'},
                        {'text': 'Lampu minyak tanah', 'next': 'n3', 'score': 0, 'feedback': 'Lampu minyak menimbulkan asap dan risiko kebakaran.'},
                    ],
                },
                {'id': 'n3', 'text': 'Taman tetap gelap atau justru menimbulkan masalah baru.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Taman terang sepanjang malam tanpa menambah tagihan listrik.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu transformasi energi?', 'back': 'Perubahan bentuk energi, misalnya listrik menjadi termal pada setrika.'},
            {'front': 'Berapa 1 kWh dalam joule?', 'back': '3.600.000 joule.'},
            {'front': 'Apa fungsi kalorimeter?', 'back': 'Mengukur energi termal atau kalor.'},
            {'front': 'Apa itu rasio elektrifikasi?', 'back': 'Perbandingan rumah tangga berlistrik dengan seluruh rumah tangga.'},
        ],
        'checkpoint': (
            'Energi yang dihasilkan alat berdaya 10 watt selama 60 detik adalah…',
            [
                ('600 joule', True),
                ('10 joule', False),
                ('60 joule', False),
                ('6.000 joule', False),
            ],
            'W = P × t = 10 watt × 60 detik = 600 joule.',
        ),
        'challenge': challenge_block(
            'ipas-5-tantangan',
            'Tantangan istilah energi',
            90,
            [
                ('Satuan SI energi', 'Joule'),
                ('Alat ukur arus dan tegangan', 'Multimeter'),
                ('Pembangkit dari uap panas bumi', 'PLTP'),
                ('Bahan bakar dari limbah organik', 'Biogas'),
                ('Rumus daya listrik', 'P = I × V'),
            ],
            'Lima istilah energi terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Berapa konsumsi energi nasional Indonesia pada 2021?', '909,24 juta barel', ['809,24 juta barel', '1.009 juta barel', '500 juta barel'], 'Konsumsi energi 2021 mencapai 909,24 juta barel setara minyak.', 'Naik 0,4% dari tahun sebelumnya.'),
        ('Sektor dengan konsumsi energi terbesar di Indonesia adalah…', 'transportasi', ['industri', 'rumah tangga', 'komersial'], 'Transportasi mengonsumsi 388,42 juta BOE atau 42,72% total.', 'Kendaraan berbahan bakar minyak mendominasi.'),
        ('Berapa rasio elektrifikasi Indonesia pada 2022?', '99,63%', ['89,63%', '79,63%', '100%'], 'Rasio elektrifikasi 2022 mencapai 99,63%.', 'Masih ada wilayah tanpa akses listrik.'),
        ('Apa satuan SI untuk energi?', 'joule', ['watt', 'ampere', 'pascal'], 'Satuan energi menurut SI adalah joule.', 'Watt adalah satuan daya.'),
        ('Berapa nilai 1 kalori dalam joule?', '4,2 joule', ['0,24 joule', '42 joule', '3.600 joule'], '1 kalori setara 4,2 joule.', 'Kebalikannya, 1 joule = 0,24 kalori.'),
        ('Berapa nilai 1 kWh dalam joule?', '3.600.000 joule', ['3.600 joule', '36.000 joule', '360 joule'], '1 kWh setara 3.600.000 joule.', 'Satu jam sama dengan 3.600 detik.'),
        ('Perubahan bentuk energi disebut…', 'transformasi energi', ['konveksi energi', 'konduksi energi', 'radiasi energi'], 'Transformasi energi adalah perubahan bentuk energi.', 'Terjadi saat alat digunakan.'),
        ('Alat pengubah energi cahaya menjadi energi listrik adalah…', 'panel surya', ['kalorimeter', 'biodigester', 'turbin angin'], 'Panel surya bekerja melalui efek fotovoltaik.', 'Sering dipasang di atap rumah.'),
        ('Pembangkit yang memanfaatkan uap panas bumi disebut…', 'PLTP', ['PLTA', 'PLTS', 'PLTB'], 'PLTP adalah pembangkit listrik tenaga panas bumi.', 'Indonesia memiliki banyak gunung api.'),
        ('Pembangkit listrik tenaga air memutar turbin memakai…', 'aliran air', ['uap batu bara', 'angin laut', 'gas alam'], 'PLTA memanfaatkan gerakan air untuk memutar turbin dan generator.', 'Biasanya dibangun di bendungan.'),
        ('Energi yang berasal dari bahan organik makhluk hidup disebut…', 'biomassa', ['geotermal', 'nuklir', 'magnetik'], 'Biomassa berasal dari tumbuhan, hewan, dan mikroorganisme.', 'Dapat diolah menjadi biogas.'),
        ('Alat pengubah limbah organik menjadi biogas disebut…', 'biodigester', ['multimeter', 'kalorimeter', 'kompresor'], 'Biodigester mengolah limbah menjadi biogas.', 'Dipakai pada skala rumah tangga maupun peternakan.'),
        ('Alat untuk mengukur tegangan dan arus listrik adalah…', 'multimeter', ['termometer', 'higrometer', 'barometer'], 'Multimeter mengukur arus, tegangan, dan hambatan.', 'Dipakai saat menguji purwarupa listrik.'),
        ('Kondisi kekurangan cadangan energi fosil disebut…', 'krisis energi', ['krisis pangan', 'krisis air', 'krisis moneter'], 'Krisis energi terjadi ketika kebutuhan meningkat sementara cadangan menipis.', 'Memicu lonjakan harga energi.'),
    ],
    'multi': [
        ('Manakah sumber energi terbarukan?', ['Matahari', 'Angin', 'Panas bumi'], ['Batu bara', 'Minyak bumi'], 'Matahari, angin, dan panas bumi dapat diperbarui.', 'Fosil akan habis karena terbentuk jutaan tahun.'),
        ('Manakah bentuk energi yang disebut dalam buku?', ['Energi listrik', 'Energi kimia', 'Energi nuklir'], ['Energi warna', 'Energi rasa'], 'Bentuk energi meliputi listrik, kimia, cahaya, termal, mekanik, magnet, dan nuklir.', 'Bentuk energi berkaitan dengan perubahan yang terjadi.'),
        ('Manakah contoh transformasi energi?', ['Setrika: listrik menjadi termal', 'Kipas: listrik menjadi gerak', 'Panel surya: cahaya menjadi listrik'], ['Batu menjadi kayu', 'Air menjadi batu'], 'Transformasi mengubah satu bentuk energi menjadi bentuk lain.', 'Setiap alat listrik umumnya mengubah energi.'),
        ('Manakah pemanfaatan energi matahari menurut buku?', ['Panel surya fotovoltaik', 'Tenaga surya terkonsentrasi (CSP)', 'Solar home system'], ['Pembangkit uap panas bumi', 'Biodigester limbah'], 'Matahari dimanfaatkan lewat panel surya dan sistem konsentrator.', 'Panas bumi dan biogas berasal dari sumber lain.'),
        ('Manakah bahan bakar yang termasuk biofuel?', ['Biogas', 'Etanol', 'Biodiesel'], ['Bensin murni', 'Avtur fosil'], 'Biogas, etanol, dan biodiesel berasal dari biomassa.', 'Bio berarti berasal dari makhluk hidup.'),
        ('Manakah data yang dicatat saat uji coba purwarupa listrik?', ['Arus listrik', 'Tegangan', 'Waktu pemakaian'], ['Warna kabel', 'Merek lampu'], 'Daya dan energi dihitung dari arus, tegangan, dan waktu.', 'W = P × t memerlukan waktu.'),
        ('Manakah keuntungan energi panas bumi?', ['Tidak memerlukan bahan bakar', 'Residunya hanya air', 'Tidak mencemari udara'], ['Menghasilkan asap hitam pekat', 'Memerlukan batu bara setiap hari'], 'PLTP tidak membakar bahan bakar sehingga emisinya rendah.', 'Uap diambil dari dalam bumi.'),
        ('Manakah solusi masalah energi menurut buku?', ['Penghematan energi', 'Pemberdayaan energi terbarukan', 'Mengoptimalkan potensi lokal'], ['Menambah pembakaran sampah', 'Meningkatkan impor bahan bakar'], 'Solusi diarahkan pada penghematan dan energi terbarukan.', 'Potensi lokal menjadi kunci.'),
    ],
    'pairs': [
        ('Energi', 'kemampuan melakukan kerja'),
        ('Transformasi energi', 'perubahan bentuk energi'),
        ('Panel surya', 'mengubah cahaya menjadi listrik'),
        ('Biomassa', 'bahan organik sumber energi'),
        ('PLTA', 'pembangkit dari aliran air'),
        ('PLTP', 'pembangkit dari uap panas bumi'),
        ('Multimeter', 'alat ukur arus dan tegangan'),
        ('Krisis energi', 'kekurangan cadangan energi fosil'),
    ],
    'steps': [
        ('Urutkan alur sumber energi menjadi listrik.', ['Sumber energi', 'Pembangkit', 'Generator', 'Transmisi dan distribusi', 'Pemakaian di rumah dan industri'], 'Energi diubah di pembangkit, disalurkan, lalu dipakai.', 'Generator menghasilkan listrik sebelum distribusi.'),
        ('Urutkan langkah mengukur tegangan dengan multimeter.', ['Putar selektor ke DCV atau ACV', 'Pilih skala yang sesuai', 'Hubungkan probe ke terminal', 'Baca hasil di layar'], 'Pengukuran dimulai dari pemilihan mode dan skala, lalu pembacaan hasil.', 'Skala besar lebih aman bila nilai belum diketahui.'),
        ('Urutkan langkah mengukur arus listrik.', ['Putar selektor ke DCA', 'Pilih skala sesuai perkiraan', 'Putuskan jalur catu daya', 'Hubungkan probe secara seri', 'Baca hasil di layar'], 'Arus diukur dengan memutus jalur lalu menghubungkan multimeter seri.', 'Pengukuran arus berbeda dari tegangan.'),
        ('Urutkan langkah projek energi ramah lingkungan.', ['Mencari referensi dan bahan', 'Menggambar desain berskala', 'Menyusun jadwal dan pembagian tugas', 'Membangun purwarupa', 'Menguji dan menghitung daya', 'Mengevaluasi dan menindaklanjuti'], 'Projek bergerak dari referensi, desain, perencanaan, pembuatan, pengujian, sampai evaluasi.', 'Pengujian dilakukan setelah purwarupa selesai.'),
        ('Urutkan langkah mengevaluasi purwarupa.', ['Menyusun rubrik penilaian', 'Mengoperasikan purwarupa', 'Mencatat variabel terukur', 'Membandingkan hasil dengan kriteria', 'Memperbaiki bagian yang belum sesuai'], 'Evaluasi memakai rubrik dan data uji, lalu diakhiri perbaikan.', 'Data uji menjadi dasar perbaikan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
