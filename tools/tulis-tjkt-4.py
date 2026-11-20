"""TJKT 4 — K3LH dan Budaya Kerja Industri (Fase E, SMK)."""
from tjkt_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'TJKT 4',
    'slug': 'tjkt-4-k3lh-budaya-kerja',
    'title': 'K3LH dan Budaya Kerja Industri',
    'description': (
        'Menerapkan keselamatan dan kesehatan kerja lingkungan hidup (K3LH), '
        'mencegah kecelakaan kerja lewat rambu dan SOP, serta membiasakan budaya '
        'kerja 5R dan pengendalian visual.'
    ),
    'objectives': [
        'Menjelaskan pengertian dan empat komponen utama K3LH.',
        'Menerapkan hierarki pengendalian bahaya dan praktik kerja yang aman.',
        'Mengenali rambu keselamatan dan manfaat Standar Operasional Prosedur.',
        'Menerapkan budaya kerja 5R dan pengendalian visual di lingkungan kerja.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Teknik-Jaringan-Komputer-dan-Telekomunikasi-BS-KLS-X.pdf Bab 4; '
        'CP Fase E Mata Pelajaran Dasar-Dasar TJKT'
    ),
    'glossary': [
        {'term': 'K3LH', 'definition': 'Keselamatan dan Kesehatan Kerja Lingkungan Hidup untuk melindungi tenaga kerja dari kecelakaan dan penyakit akibat kerja.'},
        {'term': 'Antisipasi', 'definition': 'Upaya memprediksi bahaya dan risiko yang mungkin terjadi di tempat kerja.'},
        {'term': 'Rekognisi', 'definition': 'Upaya mengenali bahaya lingkungan kerja dan pengaruhnya terhadap karyawan.'},
        {'term': 'Evaluasi', 'definition': 'Penilaian kuantitatif dan pemantauan dampak bahaya lingkungan kerja.'},
        {'term': 'Kendali', 'definition': 'Upaya menghilangkan atau mengurangi bahaya lingkungan kerja.'},
        {'term': 'Hierarki pengendalian', 'definition': 'Urutan prioritas pengendalian bahaya: eliminasi, substitusi, rekayasa, administrasi, sampai APD.'},
        {'term': 'Eliminasi', 'definition': 'Menghilangkan sumber bahaya sampai ke titik aman.'},
        {'term': 'Substitusi', 'definition': 'Mengganti peralatan atau bahan dengan yang lebih aman.'},
        {'term': 'APD', 'definition': 'Alat pelindung diri seperti helm, kacamata, sarung tangan, dan pelindung telinga.'},
        {'term': '5R', 'definition': 'Ringkas, Rapi, Resik, Rawat, dan Rajin untuk mengelola lingkungan kerja agar efisien.'},
    ],
    'intro': {
        'material_title': 'Apa itu K3LH?',
        'title': 'Melindungi tenaga kerja dari bahaya',
        'paragraphs': [
            'Menurut Permenaker No 5 Tahun 2018, K3LH adalah segala kegiatan untuk menjamin dan melindungi keselamatan serta kesehatan tenaga kerja melalui upaya pencegahan kecelakaan kerja dan penyakit akibat kerja.',
            'Keselamatan berarti keadaan terhindar dari bahaya. K3LH berhubungan dengan peralatan, tempat kerja, dan lingkungan. Pembiasaan memakai peralatan sesuai SOP adalah salah satu cara menerapkannya.',
            'Empat komponen utama K3LH adalah antisipasi, rekognisi, evaluasi, dan kendali. Keempatnya berjalan berurutan untuk mengendalikan lingkungan kerja.',
        ],
        'diagram': (
            'Empat komponen utama K3LH',
            'flowchart LR\n'
            '  A[Antisipasi] --> B[Rekognisi]\n'
            '  B --> C[Evaluasi]\n'
            '  C --> D[Kendali]\n'
            '  D --> E[Lingkungan kerja aman]',
        ),
        'callout': 'Kecelakaan kerja bukan nasib sial; hampir selalu punya penyebab yang dapat dicegah lebih awal.',
        'checkpoint': (
            'Upaya memprediksi bahaya yang mungkin terjadi di tempat kerja disebut…',
            [
                ('antisipasi', True),
                ('kendali', False),
                ('APD', False),
                ('rambu', False),
            ],
            'Antisipasi menyusun prediksi bahaya dan risiko, lalu menyiapkan keadaan darurat.',
        ),
    },
    'concept': {
        'material_title': 'Hierarki pengendalian bahaya',
        'title': 'Dari eliminasi sampai alat pelindung',
        'paragraphs': [
            'Saat melakukan K3LH, upaya kendali dijalankan berdasarkan prioritas yang disebut hierarki pengendalian. Urutannya dimulai dari yang paling efektif menghilangkan bahaya.',
            'Eliminasi menghilangkan sumber bahaya, substitusi mengganti dengan yang lebih aman, lalu rekayasa teknis memodifikasi aktivitas kerja. Setelah itu administrasi menerapkan tanda dan prosedur, dan terakhir APD melindungi tubuh.',
            'APD adalah perangkat akhir yang melindungi sebagian atau seluruh tubuh, seperti kacamata, pelindung telinga, sarung tangan, dan helm. APD dipakai setelah upaya lain belum cukup.',
        ],
        'table': [
            ['Tingkat', 'Tindakan', 'Contoh'],
            ['Eliminasi', 'Menghilangkan sumber bahaya', 'Menghilangkan bahan mudah terbakar'],
            ['Substitusi', 'Mengganti yang lebih aman', 'Mengganti bahan kimia berbahaya'],
            ['Rekayasa teknis', 'Memodifikasi aktivitas', 'Memindahkan pekerjaan dari area bising'],
            ['Administrasi', 'Tanda dan prosedur', 'Memasang rambu bahaya'],
            ['APD', 'Melindungi tubuh', 'Helm, kacamata, sarung tangan'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'tjkt-4-hierarki',
            'engine': 'mermaid',
            'title': 'Hierarki pengendalian dari paling efektif',
            'code': 'flowchart TB\n'
                    '  E[Eliminasi 1] --> S[Substitusi 2]\n'
                    '  S --> R[Rekayasa teknis 3]\n'
                    '  R --> A[Administrasi 4]\n'
                    '  A --> P[APD 5]',
        },
        'activity': categorize_block(
            'tjkt-4-klasifikasi',
            'Kelompokkan tindakan berikut ke dalam tingkat pengendalian yang sesuai.',
            [('b1', 'Eliminasi/Substitusi'), ('b2', 'Administrasi/APD')],
            [
                ('i1', 'Menghilangkan bahan mudah terbakar dari area kerja', 'b1'),
                ('i2', 'Memakai helm keselamatan', 'b2'),
                ('i3', 'Mengganti bahan kimia dengan yang aman', 'b1'),
                ('i4', 'Memasang rambu larangan merokok', 'b2'),
                ('i5', 'Memindahkan pekerjaan dari area bising', 'b1'),
                ('i6', 'Memakai kacamata pelindung', 'b2'),
                ('i7', 'Mengganti peralatan yang berbahaya', 'b1'),
                ('i8', 'Membuat prosedur penggunaan peralatan', 'b2'),
            ],
            'Tepat. Eliminasi dan substitusi menghilangkan atau mengganti bahaya; administrasi dan APD memproteksi setelah itu.',
            'Periksa lagi: memakai perlindungan adalah APD, memasang rambu adalah administrasi.',
        ),
        'subtitle': 'Praktik kerja yang aman',
        'list': [
            'Sebelum bekerja, identifikasi potensi bahaya dari peralatan yang digunakan dan rancang rencana tanggap darurat.',
            'Saat merakit komputer, cuci tangan, gunakan gelang antistatis, dan pastikan aliran listrik mati saat memasang sumber daya.',
            'Posisi duduk dan posisi layar komputer perlu diatur agar tidak menimbulkan gangguan kesehatan.',
            'Kecelakaan dapat dicegah dengan mengenali sumber masalah dan menyusun langkah antisipasi.',
        ],
        'checkpoint': (
            'Urutan prioritas pengendalian bahaya dari yang paling dulu adalah…',
            [
                ('eliminasi, substitusi, rekayasa, administrasi, APD', True),
                ('APD, admin, rekayasa, substitusi, eliminasi', False),
                ('substitusi, eliminasi, APD, admin, rekayasa', False),
                ('administrasi, APD, eliminasi, rekayasa, substitusi', False),
            ],
            'Hierarki dimulai dari yang paling efektif menghilangkan bahaya hingga APD.',
        ),
    },
    'practice': {
        'material_title': 'Rambu, SOP, dan budaya 5R',
        'title': 'Mencegah kecelakaan dan keteraturan kerja',
        'paragraphs': [
            'Rambu keselamatan atau safety sign menginformasikan area bahaya dan area aman. Warna merah berarti larangan atau pemadam api, kuning tanda waspada, hijau zona aman dan pertolongan pertama, biru kewajiban, dan putih informasi umum.',
            'Standar Operasional Prosedur (SOP) adalah tata cara penggunaan peralatan. SOP menjaga pengguna dan peralatan tetap aman, peralatan lebih awet, dan performanya terjaga.',
            'Budaya kerja 5R meliputi Ringkas (memilah), Rapi (menata), Resik (membersihkan), Rawat (mempertahankan), dan Rajin (disiplin menjalankan). 5R juga dikenal sebagai 5S: Seiri, Seiton, Seiso, Seiketsu, dan Shitsuke.',
        ],
        'scenario': scenario(
            'tjkt-4-skenario',
            'Kabel berserakan di lab',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Di lab, kabel jaringan dan listrik berserakan di lantai. Tindakan awal yang benar?',
                    'choices': [
                        {'text': 'Mengidentifikasi area kritis dan memasang cable duct agar rapi', 'next': 'n2', 'score': 2, 'feedback': 'Merapikan kabel dengan duct mengurangi risiko tersandung dan kebakaran.'},
                        {'text': 'Membiarkan hingga nanti ada petugas', 'next': 'n3', 'score': 0, 'feedback': 'Menunda penanganan bahaya membiarkan kecelakaan terjadi.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Bagaimana menjaga keteraturan itu berkelanjutan?',
                    'choices': [
                        {'text': 'Menerapkan 5R dan menjadwalkan perawatan rutin', 'next': 'n4', 'score': 2, 'feedback': '5R membuat keteraturan menjadi budaya.'},
                        {'text': 'Sekali rapi lalu tidak dicek lagi', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa rawat dan rajin, kekacauan muncul kembali.'},
                    ],
                },
                {'id': 'n3', 'text': 'Kecelakaan terulang dan kerja terganggu.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Lab aman, rapi, dan nyaman untuk belajar.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan empat komponen K3LH.', 'back': 'Antisipasi, rekognisi, evaluasi, kendali.'},
            {'front': 'Sebutkan hierarki pengendalian.', 'back': 'Eliminasi, substitusi, rekayasa, administrasi, APD.'},
            {'front': 'Apa makna rambu berwarna hijau?', 'back': 'Zona aman dan pertolongan pertama.'},
            {'front': 'Sebutkan 5R.', 'back': 'Ringkas, Rapi, Resik, Rawat, Rajin.'},
        ],
        'checkpoint': (
            'Manfaat utama SOP saat menggunakan peralatan adalah…',
            [
                ('menjaga pengguna dan peralatan tetap aman', True),
                ('menambah waktu kerja', False),
                ('mengganti peralatan yang rusak', False),
                ('menaikkan harga peralatan', False),
            ],
            'SOP menjaga keselamatan pengguna, keawetan, dan performa peralatan.',
        ),
        'challenge': challenge_block(
            'tjkt-4-tantangan',
            'Tantangan istilah K3LH',
            90,
            [
                ('Menghilangkan sumber bahaya', 'Eliminasi'),
                ('Mengganti dengan yang lebih aman', 'Substitusi'),
                ('Alat pelindung diri', 'APD'),
                ('Memilah barang yang diperlukan', 'Ringkas'),
                ('Rambu untuk zona aman', 'Hijau'),
            ],
            'Lima istilah K3LH terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('K3LH menurut Permenaker No 5 Tahun 2018 adalah…', 'upaya menjamin dan melindungi keselamatan serta kesehatan tenaga kerja', ['kegiatan hiburan karyawan', 'peringkat perusahaan', 'promosi karyawan'], 'K3LH mencegah kecelakaan dan penyakit akibat kerja.', 'Melindungi tenaga kerja.'),
        ('Upaya memprediksi bahaya dan risiko di tempat kerja disebut…', 'antisipasi', ['rekognisi', 'evaluasi', 'kendali'], 'Antisipasi menyusun prediksi bahaya.', 'Menentukan tingkat risiko.'),
        ('Upaya mengenali bahaya lingkungan kerja disebut…', 'rekognisi', ['antisipasi', 'APD', 'rambu'], 'Rekognisi memahami pengaruh bahaya terhadap karyawan.', 'Tahap kedua komponen K3LH.'),
        ('Tingkat pengendalian yang menghilangkan sumber bahaya disebut…', 'eliminasi', ['substitusi', 'administrasi', 'APD'], 'Eliminasi menurunkan bahaya ke titik aman.', 'Paling efektif dalam hierarki.'),
        ('Mengganti peralatan berbahaya dengan yang lebih aman disebut…', 'substitusi', ['eliminasi', 'rekayasa teknis', 'APD'], 'Substitusi mengganti bahan atau sistem.', 'Urutan kedua hierarki.'),
        ('Contoh alat pelindung diri adalah…', 'helm dan kacamata keselamatan', ['kabel dan switch', 'router dan server', 'firewall dan VPN'], 'APD melindungi sebagian atau seluruh tubuh.', 'Bukan perangkat jaringan.'),
        ('Rambu pemadam api dan larangan ditandai warna…', 'merah', ['hijau', 'biru', 'kuning'], 'Merah berarti larangan atau pemadam api.', 'Hijau zona aman.'),
        ('Rambu tanda waspada dan potensi risiko ditandai warna…', 'kuning', ['merah', 'hijau', 'putih'], 'Kuning berarti perhatian atau waspada.', 'Sesuai BS ISO 3864-1.'),
        ('Tata cara penggunaan peralatan kerja disebut…', 'Standar Operasional Prosedur (SOP)', ['core business', 'firewall', 'switch'], 'SOP menjaga keamanan dan performa peralatan.', 'Membiasakan kerja yang baik.'),
        ('Budaya kerja untuk mengelola lingkungan kerja agar efisien disebut…', '5R', ['5G', '3G', 'TCP/IP'], '5R: Ringkas, Rapi, Resik, Rawat, Rajin.', 'Juga dikenal sebagai 5S.'),
        ('5S yang berarti menata barang berdasarkan alur kerja disebut…', 'seiton / rapi', ['seiri', 'seiso', 'shitsuke'], 'Rapi menata agar mudah ditemukan.', 'Seiri adalah ringkas.'),
        ('Kunci keberhasilan penerapan 5R di sekolah adalah…', 'komitmen seluruh warga sekolah', ['anggota saja', 'karyawan asing', 'alat saja'], 'Komitmen menjaga konsistensi.', 'Dilakukan bersama dan berkelanjutan.'),
        ('Saat merakit komputer, sebelum memasang sumber daya sebaiknya…', 'memastikan aliran listrik dalam keadaan mati', ['menyalakan semua daya', 'menghubungkan langsung ke stopkontak', 'mengabaikan listrik'], 'Keamanan listrik mencegah kejutan.', 'Gunakan gelang antistatis.'),
        ('Kegiatan yang termasuk prinsip Resik (3R kedua) adalah…', 'menjaga kebersihan tempat kerja dan cepat memperbaiki alat rusak', ['menumpuk barang tak dipakai', 'menyimpan sampah', 'mengabaikan alat rusak'], 'Resik menjaga kebersihan.', 'Segera perbaiki yang rusak.'),
    ],
    'multi': [
        ('Manakah komponen utama K3LH?', ['Antisipasi', 'Rekognisi', 'Kendali'], ['Promosi', 'Hiburan'], 'Empat komponen: antisipasi, rekognisi, evaluasi, kendali.', 'Promosi bukan komponen K3LH.'),
        ('Manakah level hierarki pengendalian?', ['Eliminasi', 'Substitusi', 'APD'], ['Reklame', 'Dekorasi'], 'Urutannya dari eliminasi hingga APD.', 'Reklame bukan level pengendalian.'),
        ('Manakah contoh APD?', ['Helm', 'Sarung tangan', 'Kacamata pelindung'], ['Mouse', 'Kabel'], 'APD melindungi tubuh dari bahaya.', 'Mouse dan kabel bukan pelindung tubuh.'),
        ('Manakah contoh rambu keselamatan?', ['Larangan merokok', 'Zona aman', 'Pintu darurat'], ['Harga produk', 'Menu makan'], 'Rambu menginformasikan bahaya dan aman.', 'Bukan informasi bisnis.'),
        ('Manakah langkah 5R?', ['Ringkas', 'Rapi', 'Rajin'], ['Reklame', 'Remote'], '5R: Ringkas, Rapi, Resik, Rawat, Rajin.', 'Reklame bukan bagian 5R.'),
        ('Manakah tujuan penerapan 5R?', ['Meningkatkan efisiensi', 'Mengurangi risiko bahaya', 'Menghilangkan pemborosan'], ['Menambah kekacauan', 'Menimbun sampah'], '5R membuat kerja efisien dan aman.', 'Bukan menciptakan kekacauan.'),
        ('Manakah manfaat SOP?', ['Menjaga keamanan pengguna', 'Peralatan lebih awet', 'Performa terjaga'], ['Mengurangi keselamatan', 'Membiarkan bahaya'], 'SOP menstandarkan kerja yang aman.', 'Bukan mengabaikan keselamatan.'),
        ('Manakah tindakan praktik kerja yang aman?', ['Cuci tangan sebelum bekerja', 'Gunakan gelang antistatis', 'Matikan listrik saat memasang daya'], ['Mencabut kabel saat menyala', 'Mengabaikan posisi duduk'], 'Tindakan aman mencegah cedera.', 'Mengabaikan keselamatan berisiko.'),
    ],
    'pairs': [
        ('Antisipasi', 'memprediksi bahaya'),
        ('Rekognisi', 'mengenali bahaya lingkungan'),
        ('Eliminasi', 'menghilangkan sumber bahaya'),
        ('Substitusi', 'mengganti dengan yang lebih aman'),
        ('APD', 'alat pelindung diri'),
        ('5R', 'ringkas, rapi, resik, rawat, rajin'),
        ('SOP', 'tata cara penggunaan peralatan'),
        ('Evaluasi', 'menilai besarnya bahaya'),
    ],
    'steps': [
        ('Urutkan komponen K3LH.', ['Antisipasi', 'Rekognisi', 'Evaluasi', 'Kendali'], 'K3LH berjalan dari prediksi ke pengendalian.', 'Kendali menutup proses.'),
        ('Urutkan hierarki pengendalian.', ['Eliminasi', 'Substitusi', 'Rekayasa teknis', 'Administrasi', 'APD'], 'Dari paling efektif hingga pelindung tubuh.', 'APD dipakai setelah upaya lain.'),
        ('Urutkan penyusunan rencana tanggap darurat.', ['Mengidentifikasi potensi bahaya', 'Membayangkan keadaan darurat', 'Menentukan cara melindungi diri', 'Menyusun rencana prakejadian, saat, dan pascakejadian', 'Berlatih menghadapi darurat'], 'Perencanaan dari identifikasi ke latihan.', 'Latihan menguji kesiapan.'),
        ('Urutkan penerapan 5R.', ['Ringkas', 'Rapi', 'Resik', 'Rawat', 'Rajin'], '5R berjalan bertahap sesuai urutan.', 'Rajin menjaga konsistensi.'),
        ('Urutkan prosedur merakit komputer yang aman.', ['Mencuci dan mengeringkan tangan', 'Memakai gelang antistatis', 'Memilih alat sesuai fungsi', 'Memasang komponen dengan hati-hati', 'Memastikan listrik mati saat memasang daya'], 'Rakit dimulai dari kebersihan dan antistatis.', 'Cabut daya menjadi langkah aman terakhir.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)