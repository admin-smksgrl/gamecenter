"""IPAS 2 — Mengembangkan Projek Mitigasi Bencana (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    scenario,
    timeline_block,
    write_chapter,
)

CH = {
    'code': 'IPAS 2',
    'slug': 'ipas-2-mitigasi-bencana',
    'title': 'Mengembangkan Projek Mitigasi Bencana',
    'description': (
        'Mengenali potensi kebencanaan Indonesia, membedakan bencana alam, '
        'nonalam, dan sosial, memahami tahap mitigasi sebelum–saat–sesudah, '
        'serta merancang projek mitigasi sederhana sesuai bidang keahlian.'
    ),
    'objectives': [
        'Mengidentifikasi jenis dan penyebab bencana di Indonesia.',
        'Menganalisis dampak bencana terhadap lingkungan dan kehidupan manusia.',
        'Menjelaskan tahapan mitigasi bencana sebelum, pada saat, dan sesudah kejadian.',
        'Merancang projek mitigasi bencana yang sederhana, murah, dan sesuai kebutuhan.',
        'Mengomunikasikan rancangan projek mitigasi secara lisan dan tertulis.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 2 Mengembangkan Projek Mitigasi Bencana; '
        'UU No. 24 Tahun 2007; CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'Bencana', 'definition': 'Peristiwa yang mengancam dan mengganggu kehidupan manusia akibat faktor alam, nonalam, dan manusia.'},
        {'term': 'Mitigasi', 'definition': 'Serangkaian upaya untuk mengurangi risiko bencana melalui pembangunan fisik serta peningkatan kemampuan menghadapi ancaman.'},
        {'term': 'Bencana geologi', 'definition': 'Bencana akibat aktivitas geologi seperti gempa bumi tektonik, tsunami, dan letusan gunung api.'},
        {'term': 'Bencana hidrometeorologi', 'definition': 'Bencana yang dipicu perubahan cuaca atau iklim, misalnya banjir, kekeringan, dan angin puting beliung.'},
        {'term': 'Bencana ekstraterestrial', 'definition': 'Bencana akibat jatuhnya benda angkasa atau gangguan badai matahari.'},
        {'term': 'Bencana nonalam', 'definition': 'Bencana akibat gagal teknologi, gagal modernisasi, epidemi, atau wabah penyakit.'},
        {'term': 'Bencana sosial', 'definition': 'Bencana akibat peristiwa yang melibatkan manusia, seperti konflik, terorisme, dan tawuran.'},
        {'term': 'Trauma healing', 'definition': 'Tindakan untuk mengatasi trauma psikologis akibat sebuah peristiwa bencana.'},
    ],
    'intro': {
        'material_title': 'Mengapa Indonesia rawan bencana?',
        'title': 'Potensi kebencanaan dan jenis bencananya',
        'paragraphs': [
            'Indonesia berada pada pertemuan tiga lempeng besar dunia, yaitu lempeng Samudra Pasifik, lempeng Samudra Hindia, dan lempeng Eurasia. Pertemuan itu membuat Indonesia rawan gempa bumi tektonik dan letusan gunung api. Kondisi iklim dan topografi menambah risiko banjir, kekeringan, dan tanah longsor.',
            'World Risk Report 2022 menempatkan Indonesia di posisi ketiga sebagai negara dengan risiko bencana terbesar di dunia setelah Filipina dan India. BNPB mencatat 2.277 kejadian bencana sepanjang 2022, didominasi bencana hidrometeorologi.',
            'Bencana tidak hanya datang dari alam. Kegagalan teknologi, wabah penyakit, konflik sosial, dan perilaku manusia juga menimbulkan bencana. Karena itu kesiapsiagaan harus dibangun bersama.',
        ],
        'diagram': (
            'Tiga penyebab bencana menurut UU No. 24 Tahun 2007',
            'flowchart TD\n'
            '  A[Bencana] --> B[Faktor alam]\n'
            '  A --> C[Faktor nonalam]\n'
            '  A --> D[Faktor manusia]\n'
            '  B --> B1[Geologi: gempa, tsunami, gunung api]\n'
            '  B --> B2[Hidrometeorologi: banjir, kekeringan, puting beliung]\n'
            '  B --> B3[Ekstraterestrial: meteor, badai matahari]\n'
            '  C --> C1[Gagal teknologi dan modernisasi]\n'
            '  C --> C2[Epidemi dan wabah penyakit]\n'
            '  D --> D1[Konflik, terorisme, tawuran]',
        ),
        'callout': 'Tas siaga bencana yang disiapkan sebelum bencana jauh lebih berguna daripada kepanikan saat bencana terjadi.',
        'checkpoint': (
            'Menurut UU No. 24 Tahun 2007, bencana dapat disebabkan oleh…',
            [
                ('faktor alam, nonalam, dan manusia', True),
                ('faktor alam dan cuaca saja', False),
                ('faktor ekonomi dan politik', False),
                ('faktor geologi dan vulkanologi saja', False),
            ],
            'Undang-undang membagi penyebab bencana menjadi faktor alam, nonalam, dan manusia.',
        ),
    },
    'concept': {
        'material_title': 'Jenis, penyebab, dan tahap mitigasi',
        'title': 'Membedakan bencana dan merancang mitigasi',
        'paragraphs': [
            'Berdasarkan penyebabnya, bencana alam dibagi menjadi bencana geologi (gempa bumi tektonik, tsunami, gunung meletus), hidrometeorologi (banjir, kekeringan, angin puting beliung), dan ekstraterestrial (jatuhnya meteor, badai matahari).',
            'Bencana nonalam muncul dari kegagalan teknologi atau modernisasi, epidemi, dan wabah penyakit. Contohnya kecelakaan lalu lintas, wabah flu burung, jatuhnya alat berat, dan pandemi Covid-19 yang melanda dunia sejak 2019.',
            'Bencana sosial berasal dari peristiwa yang melibatkan manusia: konflik antarindividu, antarkelompok, terorisme, dan radikalisme. Contoh sederhana adalah perdebatan pemilik sawah karena pembagian air irigasi.',
        ],
        'table': [
            ['Jenis bencana', 'Penyebab', 'Contoh'],
            ['Geologi', 'Aktivitas lempeng dan gunung api', 'Gempa tektonik, tsunami, letusan gunung'],
            ['Hidrometeorologi', 'Cuaca, iklim, dan siklus hidrologi', 'Banjir, kekeringan, angin puting beliung'],
            ['Ekstraterestrial', 'Benda angkasa', 'Jatuhnya meteor, badai matahari'],
            ['Nonalam', 'Gagal teknologi, epidemi, wabah', 'Kecelakaan kerja, flu burung, Covid-19'],
            ['Sosial', 'Konflik dan perilaku manusia', 'Tawuran, konflik irigasi, terorisme'],
        ],
        'visual': timeline_block(
            'ipas-2-timeline-bencana',
            [
                ('2004', 'Tsunami Aceh', 'Gempa besar di dasar Samudra Hindia memicu tsunami yang melanda Aceh.'),
                ('2006', 'Letusan Gunung Merapi', 'Aktivitas vulkanik Merapi menimbulkan korban dan pengungsian.'),
                ('2009', 'Gempa Tasikmalaya', 'Gempa tektonik merusak bangunan di Jawa Barat.'),
                ('2010', 'Letusan Gunung Sinabung', 'Letusan memaksa warga sekitar gunung mengungsi.'),
                ('2018', 'Tsunami Donggala', 'Gempa dan tsunami melanda Palu-Donggala, Sulawesi Tengah.'),
                ('2022', 'Gempa Cianjur', 'Gempa tektonik merusak rumah dan fasilitas umum di Cianjur.'),
            ],
        ),
        'activity': categorize_block(
            'ipas-2-klasifikasi',
            'Kelompokkan peristiwa berikut ke dalam jenis bencananya.',
            [('b1', 'Geologi'), ('b2', 'Hidrometeorologi'), ('b3', 'Nonalam'), ('b4', 'Sosial')],
            [
                ('i1', 'Gempa bumi tektonik', 'b1'),
                ('i2', 'Letusan gunung api', 'b1'),
                ('i3', 'Banjir bandang', 'b2'),
                ('i4', 'Angin puting beliung', 'b2'),
                ('i5', 'Wabah flu burung', 'b3'),
                ('i6', 'Kecelakaan kerja di pabrik', 'b3'),
                ('i7', 'Tawuran antarpelajar', 'b4'),
                ('i8', 'Konflik pembagian air irigasi', 'b4'),
            ],
            'Tepat. Gempa dan letusan termasuk geologi, banjir dan puting beliung termasuk hidrometeorologi, wabah dan kecelakaan termasuk nonalam, konflik termasuk sosial.',
            'Periksa lagi: bencana sosial selalu melibatkan konflik atau perilaku manusia, sedangkan nonalam berkaitan dengan teknologi dan penyakit.',
        ),
        'subtitle': 'Tahapan mitigasi bencana',
        'list': [
            'Sebelum bencana: menyiapkan tas siaga, mengenali jalur evakuasi, mengikuti simulasi, dan memperkuat bangunan (retrofitting).',
            'Pada saat bencana: tidak panik, menyelamatkan diri ke tempat aman, dan mengikuti arahan petugas.',
            'Sesudah bencana: rekonstruksi bangunan, penyediaan fasilitas umum, pengobatan korban, dan trauma healing.',
            'Mitigasi bertujuan mengurangi risiko, meningkatkan pengetahuan, menyadarkan masyarakat, menjadi acuan perencanaan, dan menentukan penanganan pascabencana.',
        ],
        'checkpoint': (
            'Kegiatan memperkuat struktur bangunan agar tahan gempa disebut…',
            [
                ('retrofitting', True),
                ('reboisasi', False),
                ('relokasi', False),
                ('rekonstruksi', False),
            ],
            'Retrofitting adalah penguatan struktur bangunan lama agar lebih tahan terhadap guncangan gempa.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merancang projek mitigasi di sekolah',
        'paragraphs': [
            'Projek mitigasi dimulai dari identifikasi jenis bencana yang paling mungkin terjadi di sekitar, analisis penyebab dan dampak, lalu penyusunan solusi. Solusi dipilih dengan kriteria sederhana, murah, mudah dibuat, mudah dipahami, dan sesuai kebutuhan warga sekolah.',
            'Contoh nyata: membuat petunjuk jalur evakuasi dari kayu bekas untuk sekolah rawan gempa, atau memproduksi masker kain perca saat pandemi. Keduanya murah, cepat dibuat, dan langsung digunakan.',
            'Setelah projek berjalan, hasilnya dievaluasi dan dikomunikasikan. Cara paling sederhana adalah menyampaikan laporan singkat, poster jalur evakuasi, atau video simulasi yang diunggah ke media sosial sekolah.',
        ],
        'scenario': scenario(
            'ipas-2-skenario',
            'Getaran gempa saat jam pelajaran',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Gempa mengguncang kelasmu. Apa tindakan pertamamu?',
                    'choices': [
                        {'text': 'Berlindung di bawah meja kokoh dan melindungi kepala', 'next': 'n2', 'score': 2, 'feedback': 'Benar. Berlindung mengurangi risiko terkena reruntuhan.'},
                        {'text': 'Berlari turun lewat lift', 'next': 'n3', 'score': 0, 'feedback': 'Lift tidak boleh dipakai saat gempa.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Guncangan berhenti. Ke mana kamu menuju?',
                    'choices': [
                        {'text': 'Titik kumpul di tempat terbuka mengikuti jalur evakuasi', 'next': 'n4', 'score': 2, 'feedback': 'Titik kumpul memudahkan pemeriksaan dan pertolongan.'},
                        {'text': 'Kembali ke kelas mengambil tas dan telepon', 'next': 'n3', 'score': 0, 'feedback': 'Kembali ke dalam bangunan berisiko saat gempa susulan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Keputusan berbahaya menimbulkan risiko cedera.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Seluruh kelas berkumpul aman dan dicek keadaannya.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa tiga tahap mitigasi?', 'back': 'Sebelum, pada saat, dan sesudah bencana.'},
            {'front': 'Apa isi tas siaga bencana?', 'back': 'Air, makanan ringan, obat, senter, dokumen penting, dan peluit.'},
            {'front': 'Apa itu bencana ekstraterestrial?', 'back': 'Bencana akibat benda angkasa, misalnya jatuhnya meteor.'},
            {'front': 'Apa tujuan mitigasi?', 'back': 'Mengurangi risiko dan dampak bencana bagi masyarakat.'},
        ],
        'checkpoint': (
            'Bencana yang timbul akibat pandemi Covid-19 digolongkan sebagai bencana…',
            [
                ('nonalam', True),
                ('alam', False),
                ('sosial', False),
                ('ekstraterestrial', False),
            ],
            'Pandemi termasuk bencana nonalam karena disebabkan wabah penyakit, bukan faktor alam maupun konflik sosial.',
        ),
        'challenge': challenge_block(
            'ipas-2-tantangan',
            'Tantangan istilah kebencanaan',
            90,
            [
                ('Peringkat risiko bencana Indonesia 2022', 'Ketiga'),
                ('Undang-undang penanggulangan bencana', 'UU 24/2007'),
                ('Lembaga penanggulangan bencana nasional', 'BNPB'),
                ('Bencana akibat cuaca dan iklim', 'Hidrometeorologi'),
                ('Tiga lempeng di Indonesia', 'Pasifik, Hindia, Eurasia'),
            ],
            'Lima istilah kebencanaan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Di posisi berapa Indonesia dalam World Risk Report 2022?', 'ketiga', ['pertama', 'kedua', 'kesepuluh'], 'Indonesia berada di posisi ketiga sebagai negara berisiko bencana terbesar dunia.', 'Filipina dan India berada di atas Indonesia.'),
        ('Berapa kejadian bencana yang dicatat BNPB sepanjang 2022?', '2.277 kejadian', ['1.277 kejadian', '3.277 kejadian', '477 kejadian'], 'BNPB mencatat 2.277 bencana pada 2022, didominasi bencana hidrometeorologi.', 'Angka ini lebih kecil daripada catatan 2021 yang mencapai tiga ribu.'),
        ('Menurut UU No. 24 Tahun 2007, bencana disebabkan oleh…', 'faktor alam, nonalam, dan manusia', ['faktor alam dan cuaca', 'faktor ekonomi dan politik', 'faktor geologi saja'], 'Undang-undang membagi penyebab bencana menjadi tiga faktor.', 'Setiap faktor punya contoh berbeda.'),
        ('Tiga lempeng besar yang bertemu di wilayah Indonesia adalah…', 'Pasifik, Hindia, dan Eurasia', ['Pasifik, Atlantik, dan Afrika', 'Hindia, Arab, dan Nazca', 'Eurasia, Amerika, dan Antartika'], 'Indonesia berada pada pertemuan lempeng Pasifik, Hindia, dan Eurasia.', 'Dua di antaranya berupa lempeng dasar samudra.'),
        ('Bencana akibat aktivitas geologi seperti gempa tektonik dan letusan gunung disebut…', 'bencana geologi', ['bencana hidrometeorologi', 'bencana ekstraterestrial', 'bencana sosial'], 'Bencana geologi berasal dari aktivitas di dalam bumi.', 'Gempa dan gunung api adalah contoh utamanya.'),
        ('Banjir, kekeringan, dan angin puting beliung termasuk bencana…', 'hidrometeorologi', ['geologi', 'ekstraterestrial', 'nonalam'], 'Bencana hidrometeorologi dipicu perubahan cuaca dan iklim.', 'Kata hidro berarti air dan meteo berarti cuaca.'),
        ('Bencana akibat jatuhnya benda angkasa disebut…', 'ekstraterestrial', ['geologi', 'hidrometeorologi', 'sosial'], 'Bencana ekstraterestrial berasal dari luar bumi, misalnya meteor.', 'Berasal dari kata extra yang berarti luar.'),
        ('Manakah contoh bencana nonalam?', 'pandemi Covid-19', ['tsunami Aceh', 'tawuran antarpelajar', 'letusan Gunung Merapi'], 'Pandemi termasuk bencana nonalam karena disebabkan wabah penyakit.', 'Bencana nonalam berkaitan dengan teknologi atau penyakit.'),
        ('Konflik antarwarga karena pembagian air irigasi termasuk bencana…', 'sosial', ['alam', 'nonalam', 'geologi'], 'Bencana sosial muncul dari peristiwa yang melibatkan manusia.', 'Pelakunya manusia, bukan alam.'),
        ('Menurut UU No. 24 Tahun 2007, mitigasi adalah…', 'upaya mengurangi risiko bencana melalui pembangunan fisik dan penyadaran', ['bantuan dana setelah bencana', 'pemindahan seluruh warga', 'pembangunan gedung baru'], 'Mitigasi mencakup pembangunan fisik serta peningkatan kemampuan menghadapi ancaman.', 'Mitigasi dilakukan sebelum, saat, dan sesudah bencana.'),
        ('Apa tahapan mitigasi bencana?', 'sebelum, pada saat, dan sesudah bencana', ['perencanaan, pelaksanaan, pengawasan', 'hulu, tengah, hilir', 'pagi, siang, malam'], 'Mitigasi dibagi menjadi tiga tahap waktu kejadian bencana.', 'Setiap tahap memiliki kegiatan berbeda.'),
        ('Benda yang perlu disiapkan sebelum bencana adalah…', 'tas siaga bencana', ['traktor', 'mesin fotokopi', 'papan tulis'], 'Tas siaga berisi kebutuhan dasar saat mengungsi.', 'Isinya ringan dan mudah dibawa.'),
        ('Saat gempa terjadi di sekolah, tindakan yang tepat adalah…', 'menyelamatkan diri ke tempat terbuka', ['berlindung di dalam lift', 'tetap duduk di kelas', 'berlari ke atap gedung'], 'Buku menyarankan menyelamatkan diri ke tempat terbuka setelah guncangan mereda.', 'Hindari bangunan dan benda yang mudah jatuh.'),
        ('Tindakan mengatasi trauma korban bencana disebut…', 'trauma healing', ['retrofitting', 'reboisasi', 'relokasi'], 'Trauma healing membantu memulihkan kondisi psikologis korban.', 'Dilakukan pada tahap pascabencana.'),
    ],
    'multi': [
        ('Manakah yang termasuk bencana geologi?', ['Gempa bumi tektonik', 'Tsunami', 'Letusan gunung api'], ['Banjir bandang', 'Kekeringan'], 'Gempa, tsunami, dan letusan gunung berasal dari aktivitas geologi.', 'Banjir dan kekeringan termasuk hidrometeorologi.'),
        ('Manakah yang termasuk bencana hidrometeorologi?', ['Banjir', 'Kekeringan', 'Angin puting beliung'], ['Gempa tektonik', 'Jatuhnya meteor'], 'Ketiganya dipicu cuaca dan iklim.', 'Gempa dan meteor bukan bencana cuaca.'),
        ('Manakah yang termasuk bencana nonalam?', ['Wabah flu burung', 'Kecelakaan lalu lintas', 'Pandemi Covid-19'], ['Tawuran pelajar', 'Tsunami'], 'Wabah dan kecelakaan termasuk bencana nonalam.', 'Tawuran termasuk sosial, tsunami termasuk alam.'),
        ('Manakah yang termasuk bencana sosial?', ['Tawuran antarpelajar', 'Konflik pembagian air', 'Terorisme'], ['Banjir bandang', 'Letusan gunung'], 'Bencana sosial melibatkan konflik dan tindakan manusia.', 'Banjir dan letusan berasal dari alam.'),
        ('Manakah kegiatan mitigasi sebelum bencana?', ['Menyiapkan tas siaga', 'Mengenali jalur evakuasi', 'Mengikuti simulasi'], ['Menyalakan lilin saat gempa', 'Menggunakan lift untuk turun'], 'Persiapan sebelum bencana menyelamatkan banyak nyawa.', 'Saat gempa, lift tidak boleh dipakai.'),
        ('Manakah kegiatan mitigasi sesudah bencana?', ['Rekonstruksi bangunan', 'Trauma healing', 'Menyediakan fasilitas umum'], ['Membakar puing di jalan', 'Membiarkan korban tanpa bantuan'], 'Pascabencana berfokus pada pemulihan fisik dan psikologis.', 'Kerja sama pemerintah dan masyarakat mempercepat pemulihan.'),
        ('Manakah kriteria pemilihan solusi mitigasi?', ['Sederhana dan murah', 'Mudah dibuat', 'Sesuai kebutuhan masyarakat'], ['Sulit dipahami warga', 'Memerlukan biaya besar'], 'Solusi dipilih bila sederhana, murah, mudah, dan sesuai kebutuhan.', 'Solusi rumit sulit diterapkan warga.'),
        ('Manakah yang termasuk catatan refleksi BNPB 2021?', ['Pentingnya literasi kebencanaan', 'Penguatan bangunan tahan gempa', 'Mitigasi kultural dan simulasi'], ['Menghapus jalur evakuasi', 'Melarang simulasi bencana'], 'BNPB menekankan literasi, penguatan bangunan, dan mitigasi kultural.', 'Semua bertujuan menurunkan risiko.'),
    ],
    'pairs': [
        ('Mitigasi', 'upaya mengurangi risiko bencana'),
        ('Bencana alam', 'peristiwa yang disebabkan alam'),
        ('Bencana nonalam', 'gagal teknologi, epidemi, dan wabah'),
        ('Bencana sosial', 'konflik dan tindakan manusia'),
        ('Hidrometeorologi', 'banjir, kekeringan, puting beliung'),
        ('Ekstraterestrial', 'jatuhnya meteor dan badai matahari'),
        ('Retrofitting', 'penguatan struktur bangunan'),
        ('Trauma healing', 'pemulihan kondisi psikologis korban'),
    ],
    'steps': [
        ('Urutkan langkah mitigasi banjir menurut buku.', ['Menyiapkan tas siaga bencana', 'Mengungsi ke tempat yang lebih tinggi', 'Membuat penyaringan air bersih'], 'Tas siaga disiapkan sebelum, mengungsi saat banjir, dan penyaringan air dibuat sesudahnya.', 'Urutan mengikuti waktu kejadian.'),
        ('Urutkan alur analisis masalah kebencanaan.', ['Menentukan jenis bencana', 'Menganalisis penyebab', 'Menganalisis dampak', 'Menyusun solusi', 'Memilih solusi terbaik'], 'Analisis bergerak dari jenis, penyebab, dampak, sampai solusi.', 'Solusi disusun setelah dampak diketahui.'),
        ('Urutkan langkah penyelamatan saat gempa di sekolah.', ['Berlindung di bawah meja kokoh', 'Melindungi kepala', 'Menunggu guncangan berhenti', 'Menuju titik kumpul melalui jalur evakuasi', 'Melakukan pemeriksaan dan pendataan'], 'Penyelamatan berurutan dari berlindung, menunggu, evakuasi, sampai pendataan.', 'Jangan kembali ke bangunan sebelum dinyatakan aman.'),
        ('Urutkan langkah menyusun projek mitigasi bencana.', ['Mengidentifikasi alternatif mitigasi', 'Memilih solusi sesuai kriteria', 'Mendesain projek', 'Membangun projek', 'Mengevaluasi dan melaporkan hasil'], 'Projek dimulai dari alternatif, pemilihan solusi, desain, pembuatan, lalu evaluasi.', 'Evaluasi dilakukan setelah projek terbangun.'),
        ('Urutkan pemulihan pascabencana.', ['Menyelamatkan korban', 'Mengobati korban luka', 'Menyediakan fasilitas umum', 'Membangun kembali infrastruktur', 'Pendampingan trauma healing'], 'Pemulihan bergerak dari penyelamatan, pengobatan, fasilitas, rekonstruksi, sampai pendampingan psikologis.', 'Korban diselamatkan lebih dahulu.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
