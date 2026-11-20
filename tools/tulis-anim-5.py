"""ANIM 5 — Kekayaan Intelektual pada Produksi Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 5',
    'slug': 'anim-5-kekayaan-intelektual',
    'title': 'Kekayaan Intelektual pada Produksi Animasi',
    'description': (
        'Memahami kekayaan intelektual (hak cipta, merek, desain industri, '
        'paten), penerapan IP dalam industri animasi, lisensi IP, dan produk '
        'turunan sebagai sumber pendapatan animasi.'
    ),
    'objectives': [
        'Menjelaskan konsep kekayaan intelektual dan manfaat pendaftarannya.',
        'Membedakan hak cipta, merek, desain industri, dan paten.',
        'Menerapkan IP dalam dua model bisnis studio animasi (jasa dan IP).',
        'Mengenal lisensi IP dan produk turunan industri animasi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 5 Kekayaan Intelektual pada Produksi Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Kekayaan intelektual', 'definition': 'Hak yang muncul dari hasil pemikiran dalam menciptakan produk yang bermanfaat dan menguntungkan.'},
        {'term': 'Hak cipta', 'definition': 'Hak khusus pencipta yang muncul otomatis setelah karya direalisasikan dan diumumkan.'},
        {'term': 'Merek', 'definition': 'Tanda pembeda produk atau jasa: logo, nama, kata, angka, suara, atau hologram.'},
        {'term': 'Desain industri', 'definition': 'Tampilan estetis produk berupa bentuk, konfigurasi, komposisi garis, dan warna.'},
        {'term': 'Paten', 'definition': 'Hak yang diberikan kepada penemu atas invensi di bidang teknologi.'},
        {'term': 'Paten sederhana', 'definition': 'Penemuan praktis dan simpel, misalnya tusuk gigi, paper clip, dan sticky note.'},
        {'term': 'Lisensi', 'definition': 'Proses menyewakan IP yang dilindungi hukum untuk dikombinasikan dengan produk penyewa.'},
        {'term': 'Produk turunan', 'definition': 'Produk berbasis karakter IP, misalnya buku, mainan, baju, dan theme park.'},
        {'term': 'Licensing show', 'definition': 'Pameran produk IP berlisensi untuk bertemu agen lisensi, mitra, dan jaringan internasional.'},
    ],
    'intro': {
        'material_title': 'Kekayaan intelektual',
        'title': 'Hak atas karya cipta dan invensi',
        'paragraphs': [
            'Menurut DJKI Kemenkumham (2020), kekayaan intelektual adalah hak yang muncul dari hasil pemikiran dalam menciptakan produk yang bermanfaat bagi manusia, misalnya karya seni, penemuan, program komputer, dan merek dagang.',
            'Perlindungan kekayaan intelektual penting agar penemu, seniman, ilmuwan, dan pebisnis diakui sebagai pencipta dan karyanya terlindungi secara legal.',
            'Manfaat mendaftarkan IP: perlindungan hukum, antisipasi pelanggaran, menumbuhkan jiwa kompetitif, memperluas segmen pasar, berkolaborasi dengan industri pasangan, dan mempromosikan penelitian.',
            'Tipe kekayaan intelektual terbagi menjadi properti industri (paten, desain industri, merek dagang, indikasi geografi) dan hak cipta (sastra, karya seni, karya ilmiah, pertunjukan, penyiaran).',
        ],
        'diagram': (
            'Bagan jenis kekayaan intelektual',
            'flowchart TB\n'
            '  A[Kekayaan Intelektual] --> B[Properti industri]\n'
            '  A --> C[Hak cipta]\n'
            '  B --> D[Paten, desain industri, merek, indikasi geografi]\n'
            '  C --> E[Sastra, seni, karya ilmiah, pertunjukan]',
        ),
        'callout': 'Hak cipta diatur UU No. 28 Tahun 2014; hak cipta muncul otomatis setelah karya diwujudkan secara riil dan diumumkan.',
        'checkpoint': (
            'Hak kekayaan intelektual atas invensi di bidang teknologi disebut…',
            [
                ('paten', True),
                ('hak cipta', False),
                ('merek', False),
                ('desain industri', False),
            ],
            'Paten melindungi penemuan teknologi.',
        ),
    },
    'concept': {
        'material_title': 'Jenis-jenis kekayaan intelektual',
        'title': 'Hak cipta, merek, desain, dan paten',
        'paragraphs': [
            'Hak cipta melindungi buku, ceramah, lagu, drama, tari, seni rupa, arsitektur, peta, dan seni batik. Masa perlindungannya diatur UU No. 28 Tahun 2014.',
            'Merek adalah tanda yang membedakan produk atau jasa, berupa gambar, logo, nama, kata, angka, suara, atau hologram. Merek terdaftar dilindungi 10 tahun dan dapat diperpanjang.',
            'Desain industri adalah tampilan estetis produk dari kreasi bentuk, konfigurasi, komposisi garis, dan warna; dilindungi 10 tahun tanpa perpanjangan.',
            'Paten diberikan atas invensi teknologi; paten kompleks dilindungi 20 tahun, paten sederhana 10 tahun. Contoh paten Indonesia: broadband 4G LTE karya Prof. Khoirul Anwar.',
        ],
        'table': [
            ['Jenis KI', 'Obyek yang dilindungi', 'Masa perlindungan'],
            ['Hak cipta', 'Karya tulis, seni, lagu, program', 'Menurut UU Hak Cipta'],
            ['Merek', 'Logo, nama, suara, hologram', '10 tahun, bisa diperpanjang'],
            ['Desain industri', 'Bentuk dan tampilan estetis', '10 tahun, tidak diperpanjang'],
            ['Paten', 'Invensi teknologi', '20 tahun (sederhana 10)'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-5-ip',
            'engine': 'mermaid',
            'title': 'Model bisnis studio animasi',
            'code': 'flowchart TB\n'
                    '  A[Studio animasi] --> B[Model jasa: proyek pesanan]\n'
                    '  A --> C[Model IP: karakter dan cerita]\n'
                    '  C --> D[Lisensi karakter]\n'
                    '  D --> E[Merchandise, game, mainan]\n'
                    '  D --> F[Royalti dan pendapatan lisensi]',
        },
        'activity': categorize_block(
            'anim-5-klasifikasi',
            'Kelompokkan pernyataan ke jenis kekayaan intelektual yang tepat.',
            [('b1', 'Hak cipta'), ('b2', 'Merek'), ('b3', 'Paten')],
            [
                ('i1', 'Melindungi novel dan ceramah', 'b1'),
                ('i2', 'Tanda pembeda logo dan nama produk', 'b2'),
                ('i3', 'Melindungi invensi teknologi 4G LTE', 'b3'),
                ('i4', 'Muncul otomatis setelah karya diumumkan', 'b1'),
                ('i5', 'Sertifikat berlaku 10 tahun dan bisa diperpanjang', 'b2'),
                ('i6', 'Melindungi paper clip dan tusuk gigi', 'b3'),
            ],
            'Tepat. Hak cipta karya; merek pembeda; paten invensi.',
            'Periksa lagi: ciptaan=hak cipta, tanda=merek, teknologi=paten.',
        ),
        'subtitle': 'IP pada produksi animasi',
        'list': [
            'Studio animasi menjalankan dua model bisnis: model jasa (outsourcing sesuai pesanan) dan model IP (mengembangkan karakter sendiri).',
            'Di Jepang, 89,7% pendapatan industri animasi tahun 2018 berasal dari lisensi IP lokal; Pokemon menjadi waralaba dengan pendapatan sangat besar.',
            'Lisensi IP adalah menyewakan karakter berhak cipta untuk dikombinasikan dengan produk penyewa, misalnya baju dan mainan.',
            'Produk turunan IP meliputi buku, video game, suvenir, baju, action figur, makanan, cosplay, hingga theme park.',
        ],
        'checkpoint': (
            'Merek terdaftar mendapatkan perlindungan selama…',
            [
                ('10 tahun dan dapat diperpanjang', True),
                ('5 tahun tanpa perpanjangan', False),
                ('20 tahun', False),
                ('seumur hidup', False),
            ],
            'Merek bisa diperbarui setelah 10 tahun.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menjual dan melindungi karakter',
        'paragraphs': [
            'Bisnis model IP memperlihatkan perusahaan membeli lisensi karakter untuk membantu menjual barang dagangan atau membuat produk turunan.',
            'Licensing show seperti Hong Kong International Licensing Show menjadi tempat pemilik IP bertemu agen lisensi, mitra, dan jaringan internasional.',
            'Pendapatan industri animasi tidak hanya dari film; produk turunan IP Indonesia melampaui nilai tinggi, bahkan di Jepang animasi melampaui industri otomotif.',
        ],
        'scenario': scenario(
            'anim-5-skenario',
            'Karakter karyamu dijual tanpa izin',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu membuat karakter animasi populer. Suatu hari ada toko menjual baju dengan karakter tersebut tanpa izinmu. Tindakanmu?',
                    'choices': [
                        {'text': 'Mengurus pendaftaran IP dan menegakkan hak ciptamu', 'next': 'n2', 'score': 2, 'feedback': 'IP terdaftar memberi perlindungan hukum dan hak gugat.'},
                        {'text': 'Membiarkan saja karena merasa kasihan pada penjual', 'next': 'n3', 'score': 0, 'feedback': 'Pembajakan merugikan kreator dan industri.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Karaktermu sudah terdaftar. Bagaimana mengembangkan pendapatan?',
                    'choices': [
                        {'text': 'Menawarkan lisensi resmi kepada mitra untuk produk turunan', 'next': 'n4', 'score': 2, 'feedback': 'Lisensi memberi royalti dan menjaga kualitas produk.'},
                        {'text': 'Menutup semua kerja sama agar karakter tidak dipakai', 'next': 'n3', 'score': 0, 'feedback': 'IP justru berkembang lewat lisensi yang sehat.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pembajakan merajalela dan pendapatanmu terus tergerus.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Karakter dilisensikan ke banyak produk; royalti meningkat pesat.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa manfaat mendaftarkan kekayaan intelektual?', 'back': 'Perlindungan hukum, antisipasi pelanggaran, dan perluasan pasar.'},
            {'front': 'Sebutkan empat tipe KI utama.', 'back': 'Hak cipta, merek, desain industri, paten.'},
            {'front': 'Apa itu lisensi IP?', 'back': 'Menyewakan IP berlisensi untuk dikombinasikan dengan produk penyewa.'},
            {'front': 'Sebutkan contoh produk turunan IP animasi.', 'back': 'Buku, video game, suvenir, baju, action figur, dan theme park.'},
        ],
        'checkpoint': (
            'Lisensi IP dalam industri animasi berarti…',
            [
                ('menyewakan karakter berhak cipta untuk produk lain', True),
                ('menjual kaos murah tanpa izin', False),
                ('menghapus hak pencipta', False),
                ('mencetak uang', False),
            ],
            'Lisensi memberi royalti kepada pemilik IP.',
        ),
        'challenge': challenge_block(
            'anim-5-tantangan',
            'Tantangan istilah kekayaan intelektual',
            90,
            [
                ('Hak atas invensi teknologi', 'Paten'),
                ('Tanda pembeda produk atau jasa', 'Merek'),
                ('Hak atas karya tulis dan seni', 'Hak cipta'),
                ('Menyewakan karakter untuk produk lain', 'Lisensi'),
                ('Baju, mainan, dan theme park dari karakter', 'Produk turunan'),
            ],
            'Lima istilah kekayaan intelektual terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Kekayaan intelektual adalah…', 'hak yang muncul dari hasil pemikiran dalam menciptakan produk', ['harta berupa uang tunai', 'surat izin mengemudi', 'sertifikat tanah'], 'Karya cipta dan invensi dilindungi hukum.', 'Menguntungkan bagi manusia.'),
        ('Tipe kekayaan intelektual terbagi menjadi…', 'properti industri dan hak cipta', ['properti tanah dan bangunan', 'uang dan saham', 'mobil dan rumah'], 'Paten, merek, desain di properti industri.', 'Sastra dan seni di hak cipta.'),
        ('Hak cipta diatur dalam…', 'UU No. 28 Tahun 2014', ['UU No. 1 Tahun 1970', 'PP No. 50 Tahun 2012', 'UU No. 13 Tahun 2003'], 'UU 28/2014 tentang Hak Cipta.', 'Muncul otomatis setelah diumumkan.'),
        ('Merek terdaftar dilindungi selama…', '10 tahun dan dapat diperpanjang', ['5 tahun sekali', '20 tahun tetap', '2 tahun saja'], 'Sertifikat merek bukti kepemilikan.', 'Bisa diperpanjang terus.'),
        ('Merek nontradisional berupa…', 'bentuk 3 dimensi, hologram, dan suara', ['kata dan logo', 'hanya warna', 'hanya angka'], 'Bentuk, hologram, suara termasuk.', 'Merek tradisional kata dan logo.'),
        ('Desain industri adalah…', 'tampilan estetis produk dari bentuk, garis, dan warna', ['ide bisnis abstrak', 'strategi pemasaran', 'jadwal produksi'], 'Hasil kreasi tampilan produk.', 'Dilindungi 10 tahun.'),
        ('Perlindungan desain industri berlangsung…', '10 tahun tanpa perpanjangan', ['20 tahun', '5 tahun', 'seumur hidup'], 'Berbeda dengan merek.', 'Sertifikat sebagai bukti.'),
        ('Contoh paten penemu Indonesia adalah…', 'teknologi broadband 4G LTE Prof. Khoirul Anwar', ['radio pertama dunia', 'mesin uap', 'jam atom'], '4G LTE dipatenkan ilmuwan Indonesia.', 'Juga fondasi cakar ayam Sedyatmo.'),
        ('Paten hasil invensi kompleks dilindungi selama…', '20 tahun', ['10 tahun', '5 tahun', '50 tahun'], 'Paten sederhana 10 tahun.', 'Melindungi penemu teknologi.'),
        ('Contoh paten sederhana adalah…', 'tusuk gigi dan paper clip', ['telepon pintar', 'pesawat jet', 'mobil listrik'], 'Penemuan praktis dan simpel.', 'Berkegunaan praktis.'),
        ('Model jasa dalam studio animasi adalah…', 'mengerjakan proyek dari perusahaan lain', ['mengembangkan karakter sendiri', 'menjual merchandise', 'membangun theme park'], 'Outsourcing sesuai pesanan.', 'Model IP mengembangkan karakter.'),
        ('Bisnis model IP berarti studio…', 'mengembangkan karakter dan cerita sendiri', ['hanya menerima pesanan', 'tidak punya hak cipta', 'menjual jasa tenaga'], 'Karakter dilindungi dan dilisensikan.', 'Pendapatan dari royalti.'),
        ('Lisensi IP adalah…', 'menyewakan IP yang dilindungi hukum untuk produk lain', ['membeli hak orang lain', 'menghapus hak cipta', 'menyalin karya bebas'], 'Penyewa membayar royalti.', 'Contoh: baju dan mainan karakter.'),
        ('Produk turunan IP animasi meliputi…', 'buku, video game, action figur, dan theme park', ['bahan bakar, baja, semen', 'padi, jagung, singkong', 'paspal, beton, aspal'], 'Karakter dipakai di banyak produk.', 'Menambah nilai industri.'),
    ],
    'multi': [
        ('Manakah jenis kekayaan intelektual?', ['Hak cipta', 'Merek', 'Paten'], ['Pajak kendaraan', 'Asuransi jiwa', 'Sewa rumah'], 'KI melindungi ciptaan dan invensi.', 'Bukan bagian KI.'),
        ('Manakah karya yang dilindungi hak cipta?', ['Buku dan ceramah', 'Lagu dan drama', 'Seni rupa dan peta'], ['Resep rahasia warung', 'Jadwal kereta', 'Harga sembako'], 'Karya cipta dilindungi UU 28/2014.', 'Bukan karya cipta.'),
        ('Manakah ciri merek?', ['Tanda pembeda produk', 'Berupa logo atau nama', 'Bisa berbentuk suara'], ['Berupa ide abstrak', 'Tanpa dokumen', 'Berlaku selamanya'], 'Merek membedakan produk atau jasa.', 'Tanda wajib didaftar.'),
        ('Manakah contoh paten?', ['Penerangan listrik', 'Broadband 4G LTE', 'Fondasi cakar ayam'], ['Baju kaos polos', 'Makanan ringan', 'Pena biasa'], 'Paten melindungi invensi teknologi.', 'Barang biasa bukan invensi.'),
        ('Manakah manfaat mendaftarkan KI?', ['Perlindungan hukum', 'Antisipasi pelanggaran', 'Perluasan segmen pasar'], ['Menaikkan harga sembarang', 'Mengurangi kualitas', 'Menghapus merek'], 'Pendaftaran memberi perlindungan.', 'Bukan untuk menaikkan harga sewenang-wenang.'),
        ('Manakah model bisnis studio animasi?', ['Model jasa', 'Model IP', 'Model investasi saham'], ['Model koperasi konsumsi', 'Model angkutan umum'], 'Jasa dan IP dua model utama.', 'Bukan model bisnis studio.'),
        ('Manakah produk turunan IP animasi?', ['Video game', 'Action figur', 'Theme park'], ['Bahan bakar', 'Obat-obatan', 'Pupuk'], 'Karakter dipakai produk turunan.', 'Bukan turunan karakter animasi.'),
        ('Manakah kegiatan yang tepat terkait IP?', ['Mendaftarkan karya', 'Membeli lisensi resmi', 'Menghargai hak pencipta'], ['Membeli produk bajakan', 'Menyalin bebas', 'Mengambil tanpa izin'], 'Apresiasi KI menjaga industri.', 'Pembajakan merugikan.'),
    ],
    'pairs': [
        ('Hak cipta', 'UU No. 28 Tahun 2014'),
        ('Merek', 'tanda pembeda produk'),
        ('Desain industri', 'tampilan estetis produk'),
        ('Paten', 'invensi teknologi'),
        ('Paten sederhana', 'tusuk gigi dan paper clip'),
        ('Lisensi', 'menyewakan IP'),
        ('Produk turunan', 'merchandise dan theme park'),
        ('Licensing show', 'pameran produk berlisensi'),
    ],
    'steps': [
        ('Urutkan langkah melindungi karya animasi.', ['Menyelesaikan karya cipta', 'Mendaftarkan kekayaan intelektual', 'Mendapat sertifikat', 'Menegakkan hak atas pelanggaran', 'Mengomersialkan lewat lisensi'], 'Karya diselesaikan dulu.', 'Komersialisasi menutup langkah.'),
        ('Urutkan pengembangan bisnis model IP.', ['Membuat karakter unik', 'Mendaftarkan hak cipta', 'Membuat produk turunan', 'Menawarkan lisensi', 'Menerima royalti'], 'Berawal dari karakter.', 'Royalti menutup pengembangan.'),
        ('Urutkan proses lisensi IP.', ['Pemilik IP mendaftar karya', 'Menemukan mitra lisensi', 'Menandatangani perjanjian', 'Produk turunan diproduksi', 'Royalti dibayarkan'], 'Pendaftaran melindungi IP.', 'Royalti menutup siklus.'),
        ('Urutkan manfaat pendaftaran KI.', ['Perlindungan hukum', 'Antisipasi pelanggaran', 'Menumbuhkan jiwa kompetitif', 'Memperluas pasar', 'Kolaborasi industri'], 'Hukum jadi dasar perlindungan.', 'Kolaborasi menutup manfaat.'),
        ('Urutkan pengembangan karakter dari ide sampai pasar.', ['Ide karakter', 'Desain karakter', 'Pendaftaran IP', 'Lisensi produk', 'Distribusi ke pasar'], 'Ide menjadi awal.', 'Pasar menutup rangkaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)