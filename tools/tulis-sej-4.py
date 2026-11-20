"""SEJ 4 — Sejarah dan Teori Sosial (Fase E)."""
from sejarah_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'SEJ 4',
    'slug': 'sej-4-sejarah-teori-sosial',
    'title': 'Sejarah dan Teori Sosial',
    'description': (
        'Menggunakan teori sosial untuk menjelaskan peristiwa sejarah: perubahan '
        'dan kesinambungan, struktur dan agensi, konflik dan integrasi, serta '
        'membaca fenomena masa kini dengan konsep ilmu sejarah.'
    ),
    'objectives': [
        'Menjelaskan fungsi teori sosial dalam analisis peristiwa sejarah.',
        'Membedakan konsep perubahan, kesinambungan, pengulangan, dan perkembangan.',
        'Menggunakan konsep struktur, agensi, konflik, dan integrasi untuk membaca peristiwa.',
        'Menganalisis fenomena sosial masa kini dengan konsep dasar ilmu sejarah.',
    ],
    'minutes': 180,
    'source': (
        'Sejarah-BG-KLS-X.pdf materi Sejarah dan Teori Sosial; '
        'CP Fase E Mata Pelajaran Sejarah'
    ),
    'glossary': [
        {'term': 'Teori sosial', 'definition': 'Kerangka berpikir dari ilmu sosial yang dipakai untuk menjelaskan peristiwa sejarah.'},
        {'term': 'Perubahan', 'definition': 'Keadaan yang berbeda dari sebelumnya dalam kurun waktu tertentu.'},
        {'term': 'Kesinambungan', 'definition': 'Unsur masa lalu yang tetap berlangsung hingga masa kini.'},
        {'term': 'Pengulangan', 'definition': 'Pola peristiwa yang muncul kembali dengan bentuk berbeda.'},
        {'term': 'Perkembangan', 'definition': 'Perubahan yang berjalan bertahap menuju bentuk yang lebih kompleks.'},
        {'term': 'Struktur', 'definition': 'Tatanan sosial yang membatasi dan membentuk tindakan manusia, misalnya lembaga dan aturan.'},
        {'term': 'Agensi', 'definition': 'Kemampuan manusia bertindak dan mengubah keadaan di tengah struktur.'},
        {'term': 'Konflik', 'definition': 'Pertentangan kepentingan antarkelompok dalam masyarakat.'},
        {'term': 'Integrasi', 'definition': 'Proses menyatukan bagian masyarakat sehingga terbentuk kesatuan sosial.'},
    ],
    'intro': {
        'material_title': 'Mengapa sejarah butuh teori sosial?',
        'title': 'Menjelaskan, bukan sekadar menceritakan',
        'paragraphs': [
            'Sejarah menceritakan apa yang terjadi; teori sosial membantu menjelaskan mengapa hal itu terjadi dan bagaimana pola yang serupa bisa muncul lagi. Teori berfungsi sebagai alat bantu berpikir, bukan pengganti bukti.',
            'Konsep dasar seperti perubahan, kesinambungan, pengulangan, dan perkembangan membantu sejarawan membaca arah suatu zaman tanpa kehilangan detail peristiwa.',
            'Sejarah juga meminjam konsep struktur dan agensi: manusia bertindak, tetapi tindakannya dibatasi atau didukung oleh aturan, lembaga, dan keadaan sosial pada zamannya.',
        ],
        'diagram': (
            'Empat pola dalam membaca waktu',
            'flowchart LR\n'
            '  A[Waktu sejarah] --> B[Perubahan]\n'
            '  A --> C[Kesinambungan]\n'
            '  A --> D[Pengulangan]\n'
            '  A --> E[Perkembangan]\n'
            '  B --> F[Berbeda dari sebelumnya]\n'
            '  C --> G[Masih berlangsung kini]\n'
            '  D --> H[Pola muncul kembali]\n'
            '  E --> I[Bertahap makin kompleks]',
        ),
        'callout': 'Teori yang tidak didukung bukti hanya menjadi dugaan; sejarawan tetap berpijak pada sumber.',
        'checkpoint': (
            'Unsur masa lalu yang masih berlangsung hingga kini disebut…',
            [
                ('kesinambungan', True),
                ('perubahan', False),
                ('pengulangan', False),
                ('anakronisme', False),
            ],
            'Kesinambungan menunjukkan unsur masa lalu yang bertahan.',
        ),
    },
    'concept': {
        'material_title': 'Struktur, agensi, konflik, integrasi',
        'title': 'Alat bantu membaca masyarakat',
        'paragraphs': [
            'Struktur adalah tatanan yang membatasi dan membentuk tindakan: aturan sekolah, sistem pemerintahan, adat, dan ekonomi. Struktur tidak selalu terlihat, tetapi pengaruhnya terasa dalam pilihan hidup manusia.',
            'Agensi adalah kemampuan manusia bertindak. Meski struktur membatasi, manusia dapat menegosiasi, melawan, atau mengubahnya. Keberhasilan suatu gerakan biasanya lahir dari pertemuan agensi dan peluang yang dibuka struktur.',
            'Konflik dan integrasi sama-sama nyata. Masyarakat tidak pernah sepenuhnya damai atau sepenuhnya berkonflik; keduanya berlangsung bersamaan. Sejarah mencatat bagaimana keduanya diatur lewat hukum, adat, atau kesepakatan.',
        ],
        'table': [
            ['Konsep', 'Pengertian', 'Contoh dalam sejarah'],
            ['Struktur', 'Tatanan yang membatasi tindakan', 'Sistem tanam paksa membatasi pilihan petani'],
            ['Agensi', 'Kemampuan bertindak manusia', 'Pergerakan buruh menuntut upah layak'],
            ['Konflik', 'Pertentangan kepentingan', 'Perselisihan antarkelompok dagang'],
            ['Integrasi', 'Penyatuan masyarakat', 'Sumpah Pemuda menyatukan organisasi pemuda'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'sej-4-struktur-agensi',
            'engine': 'mermaid',
            'title': 'Struktur dan agensi membentuk hasil sejarah',
            'code': 'flowchart TB\n'
                    '  A[Struktur sosial] --> C{Medan tindakan}\n'
                    '  B[Agensi manusia] --> C\n'
                    '  C --> D[Tindakan kolektif]\n'
                    '  D --> E{Hasil}\n'
                    '  E --> F[Perubahan]\n'
                    '  E --> G[Kesinambungan]\n'
                    '  F --> H[Struktur baru]\n'
                    '  H --> A',
        },
        'activity': categorize_block(
            'sej-4-klasifikasi',
            'Kelompokkan gejala berikut sebagai perubahan atau kesinambungan.',
            [('b1', 'Perubahan'), ('b2', 'Kesinambungan')],
            [
                ('i1', 'Pasar tradisional beralih ke belanja daring', 'b1'),
                ('i2', 'Tradisi gotong royong masih dilakukan warga', 'b2'),
                ('i3', 'Surat kabar cetak digantikan berita digital', 'b1'),
                ('i4', 'Upacara adat tetap dijalankan setiap tahun', 'b2'),
                ('i5', 'Alat pembayaran berubah dari tunai ke digital', 'b1'),
                ('i6', 'Bahasa daerah tetap dipakai di rumah', 'b2'),
                ('i7', 'Sistem kerja berubah dari manual ke mesin', 'b1'),
                ('i8', 'Sekolah tetap memakai seragam', 'b2'),
            ],
            'Tepat. Perubahan menandai keadaan yang berbeda; kesinambungan menandai unsur yang bertahan.',
            'Periksa lagi: kata “beralih”, “digantikan”, dan “berubah” menandai perubahan.',
        ),
        'subtitle': 'Sejarah dan fenomena masa kini',
        'list': [
            'Perubahan bisa cepat (revolusi) atau Lambat (evolusi); keduanya bagian dari sejarah.',
            'Pengulangan tidak berarti peristiwa sama persis, melainkan polanya menyerupai karena sebab yang mirip.',
            'Struktur yang tidak adil cenderung memicu konflik; integrasi lahir dari kesepakatan yang mengakui perbedaan.',
            'Fenomena masa kini seperti urbanisasi, media sosial, dan krisis iklim dapat dianalisis dengan konsep sejarah.',
        ],
        'checkpoint': (
            'Kemampuan manusia bertindak di tengah batasan struktur disebut…',
            [
                ('agensi', True),
                ('konflik', False),
                ('integrasi', False),
                ('periodisasi', False),
            ],
            'Agensi adalah kemampuan manusia bertindak dan mengubah keadaan.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membaca masa kini dengan konsep sejarah',
        'paragraphs': [
            'Ambil satu gejala: warga desa pindah ke kota. Dengan konsep perubahan, lihat apa yang berbeda dibanding dua puluh tahun lalu. Dengan kesinambungan, cari tradisi yang tetap dibawa pindah.',
            'Gunakan konsep struktur dan agensi: struktur apa yang mendorong orang merantau, dan bagaimana mereka bertindak menghadapi keadaan itu? Lalu tanyakan, konflik atau integrasi apa yang muncul di kota tujuan.',
            'Tuliskan hasilnya dalam paragraf pendek yang menyebut konsep, bukti, dan kesimpulan. Cara ini melatih kebiasaan berpikir yang dipakai sejarawan.',
        ],
        'scenario': scenario(
            'sej-4-skenario',
            'Pasar lama yang mulai sepi',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Pasar lama di kampungmu mulai sepi karena belanja daring. Bagaimana kamu menjelaskannya?',
                    'choices': [
                        {'text': 'Menganalisis perubahan teknologi dan kebiasaan pembeli', 'next': 'n2', 'score': 2, 'feedback': 'Perubahan dapat dijelaskan dengan sebab sosial dan teknologi.'},
                        {'text': 'Menyalahkan pedagang tanpa data', 'next': 'n3', 'score': 0, 'feedback': 'Menyalahkan tanpa bukti bukan analisis sejarah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Apa yang bisa dilakukan warga berdasarkan analisismu?',
                    'choices': [
                        {'text': 'Menggabungkan dagangan dengan layanan pesan antar dan menjaga ciri khas pasar', 'next': 'n4', 'score': 2, 'feedback': 'Agensi warga dan struktur pasar baru bisa dipadukan.'},
                        {'text': 'Membiarkan pasar tutup karena perubahan pasti terjadi', 'next': 'n3', 'score': 0, 'feedback': 'Perubahan bukan alasan menyerah tanpa tindakan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pasar tutup, warga kehilangan tempat usaha dan ruang sosial.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Pasar bertahan dengan wajah baru dan warga tetap berdaya.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa fungsi teori sosial dalam sejarah?', 'back': 'Membantu menjelaskan mengapa peristiwa terjadi, bukan menggantikan bukti.'},
            {'front': 'Apa beda perubahan dan kesinambungan?', 'back': 'Perubahan menandai keadaan berbeda; kesinambungan menandai unsur yang bertahan.'},
            {'front': 'Apa itu agensi?', 'back': 'Kemampuan manusia bertindak di tengah batasan struktur.'},
            {'front': 'Apa itu integrasi?', 'back': 'Proses menyatukan bagian masyarakat menjadi satu kesatuan.'},
        ],
        'checkpoint': (
            'Pola peristiwa yang muncul kembali dengan bentuk berbeda disebut…',
            [
                ('pengulangan', True),
                ('kesinambungan', False),
                ('perkembangan', False),
                ('periodisasi', False),
            ],
            'Pengulangan menunjukkan pola serupa, bukan peristiwa yang identik.',
        ),
        'challenge': challenge_block(
            'sej-4-tantangan',
            'Tantangan istilah teori sosial',
            90,
            [
                ('Tatanan yang membatasi tindakan', 'Struktur'),
                ('Kemampuan manusia bertindak', 'Agensi'),
                ('Pertentangan kepentingan', 'Konflik'),
                ('Proses penyatuan masyarakat', 'Integrasi'),
                ('Unsur masa lalu yang bertahan', 'Kesinambungan'),
            ],
            'Lima istilah teori sosial terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Kerangka berpikir ilmu sosial untuk menjelaskan peristiwa sejarah disebut…', 'teori sosial', ['kronologi', 'periodisasi', 'anakronisme'], 'Teori sosial menjadi alat bantu penjelasan.', 'Tetap berpijak pada bukti.'),
        ('Keadaan yang berbeda dari sebelumnya disebut…', 'perubahan', ['kesinambungan', 'pengulangan', 'perkembangan'], 'Perubahan dapat cepat atau lambat.', 'Kesinambungan adalah sebaliknya.'),
        ('Unsur masa lalu yang tetap berlangsung hingga kini disebut…', 'kesinambungan', ['perubahan', 'konflik', 'agensi'], 'Kesinambungan menunjukkan unsur yang bertahan.', 'Misalnya tradisi gotong royong.'),
        ('Pola peristiwa yang muncul kembali menyerupai masa lalu disebut…', 'pengulangan', ['kesinambungan', 'integrasi', 'periodisasi'], 'Pengulangan tidak berarti sama persis.', 'Sebabnya bisa serupa.'),
        ('Perubahan bertahap menuju bentuk yang lebih kompleks disebut…', 'perkembangan', ['pengulangan', 'konflik', 'agensi'], 'Perkembangan berlangsung bertahap.', 'Berbeda dari revolusi yang cepat.'),
        ('Tatanan sosial yang membatasi tindakan manusia disebut…', 'struktur', ['agensi', 'integrasi', 'konflik'], 'Struktur meliputi aturan, lembaga, dan adat.', 'Pengaruhnya terasa dalam pilihan hidup.'),
        ('Kemampuan manusia bertindak dan mengubah keadaan disebut…', 'agensi', ['struktur', 'konflik', 'periodisasi'], 'Agensi membuat manusia bukan sekadar korban keadaan.', 'Bisa berupa perlawanan atau negosiasi.'),
        ('Pertentangan kepentingan antarkelompok disebut…', 'konflik', ['integrasi', 'kesinambungan', 'perkembangan'], 'Konflik lahir dari kepentingan yang berbeda.', 'Sering dipicu struktur tidak adil.'),
        ('Proses menyatukan bagian masyarakat menjadi kesatuan disebut…', 'integrasi', ['konflik', 'agensi', 'pengulangan'], 'Integrasi lahir dari kesepakatan yang mengakui perbedaan.', 'Contohnya Sumpah Pemuda.'),
        ('Perubahan sosial yang berlangsung cepat dan mendasar disebut…', 'revolusi', ['evolusi', 'kesinambungan', 'pengulangan'], 'Revolusi berlangsung cepat.', 'Evolusi berlangsung lambat.'),
        ('Struktur yang tidak adil cenderung…', 'memicu konflik', ['menghapus perbedaan', 'menjamin integrasi', 'menghentikan sejarah'], 'Ketidakadilan mendorong perlawanan.', 'Integrasi menuntut keadilan.'),
        ('Contoh integrasi dalam sejarah Indonesia adalah…', 'Sumpah Pemuda 1928', ['tanam paksa', 'perang dagang', 'pajak ganda'], 'Sumpah Pemuda menyatukan organisasi pemuda.', 'Menjadi dasar persatuan.'),
        ('Fenomena masa kini yang dapat dianalisis dengan konsep sejarah adalah…', 'urbanisasi dan perubahan pola kerja', ['ramalan cuaca harian', 'harga cabai pekan ini', 'jadwal pertandingan'], 'Sejarah menganalisis gejala sosial berjangka panjang.', 'Bukan fluktuasi harian.'),
        ('Sikap yang tepat terhadap teori sosial dalam kajian sejarah adalah…', 'memakainya sebagai alat bantu yang diuji dengan bukti', ['menganggapnya bukti', 'menolak semua teori', 'memakai teori tanpa data'], 'Teori tanpa bukti hanyalah dugaan.', 'Bukti tetap yang utama.'),
    ],
    'multi': [
        ('Manakah pola dalam membaca waktu sejarah?', ['Perubahan', 'Kesinambungan', 'Pengulangan'], ['Anakronisme', 'Eurocentrisme'], 'Empat pola termasuk perkembangan.', 'Anakronisme adalah kesalahan.'),
        ('Manakah ciri perubahan?', ['Berbeda dari keadaan sebelumnya', 'Dapat berlangsung cepat', 'Dapat berlangsung lambat'], ['Selalu sama sepanjang masa', 'Tidak dapat dijelaskan'], 'Perubahan bisa revolusi atau evolusi.', 'Sejarah mencatat keduanya.'),
        ('Manakah contoh kesinambungan?', ['Tradisi gotong royong', 'Bahasa daerah di rumah', 'Upacara adat tahunan'], ['Peralihan surat kabar ke berita digital', 'Pembayaran tunai ke digital'], 'Kesinambungan adalah unsur yang bertahan.', 'Peralihan menandai perubahan.'),
        ('Manakah contoh struktur?', ['Aturan sekolah', 'Sistem pemerintahan', 'Adat masyarakat'], ['Keberanian seorang tokoh', 'Pilihan pribadi'], 'Struktur adalah tatanan yang membatasi tindakan.', 'Keberanian termasuk agensi.'),
        ('Manakah contoh agensi?', ['Pergerakan buruh menuntut upah', 'Warga menolak penggusuran', 'Pelajar menggalang bantuan'], ['Sistem tanam paksa', 'Aturan kolonial'], 'Agensi adalah tindakan manusia.', 'Tanam paksa adalah struktur.'),
        ('Manakah penyebab konflik sosial?', ['Kepentingan yang bertentangan', 'Ketidakadilan struktur', 'Perebutan sumber daya'], ['Kesepakatan bersama', 'Saling pengertian'], 'Konflik lahir dari pertentangan kepentingan.', 'Kesepakatan menghasilkan integrasi.'),
        ('Manakah cara menganalisis fenomena masa kini dengan konsep sejarah?', ['Menentukan batas waktu', 'Mencari sumber dan bukti', 'Menghubungkan sebab dan akibat'], ['Menebak tanpa data', 'Mengikuti kabar bohong'], 'Analisis sejarah menuntut bukti dan batas waktu.', 'Dugaan tanpa data bukan analisis.'),
        ('Manakah pernyataan tentang teori sosial?', ['Membantu menjelaskan', 'Bukan pengganti bukti', 'Perlu diuji dengan data'], ['Selalu benar', 'Menghapus kebutuhan sumber'], 'Teori adalah alat bantu.', 'Bukti tetap menjadi dasar.'),
    ],
    'pairs': [
        ('Struktur', 'tatanan yang membatasi tindakan'),
        ('Agensi', 'kemampuan manusia bertindak'),
        ('Konflik', 'pertentangan kepentingan'),
        ('Integrasi', 'penyatuan masyarakat'),
        ('Perubahan', 'keadaan berbeda dari sebelumnya'),
        ('Kesinambungan', 'unsur yang tetap bertahan'),
        ('Pengulangan', 'pola muncul kembali'),
        ('Perkembangan', 'perubahan bertahap makin kompleks'),
    ],
    'steps': [
        ('Urutkan langkah menganalisis fenomena dengan konsep sejarah.', ['Memilih fenomena', 'Menetapkan batas waktu', 'Mengumpulkan bukti', 'Menerapkan konsep perubahan dan kesinambungan', 'Menuliskan kesimpulan'], 'Analisis bergerak dari fenomena ke kesimpulan.', 'Konsep dipakai setelah bukti terkumpul.'),
        ('Urutkan proses perubahan sosial.', ['Gejala baru muncul', 'Sebagian warga menerima', 'Terjadi pertentangan', 'Kesepakatan atau aturan dibuat', 'Kebiasaan baru menguat'], 'Perubahan melewati penerimaan dan pertentangan.', 'Kebiasaan baru menandai hasil.'),
        ('Urutkan hubungan struktur dan agensi.', ['Struktur membatasi pilihan', 'Manusia menilai keadaan', 'Manusia bertindak bersama', 'Struktur memberi peluang atau hambatan', 'Hasil berupa perubahan atau kesinambungan'], 'Tindakan lahir di tengah batasan struktur.', 'Hasilnya bisa mengubah struktur.'),
        ('Urutkan langkah membaca gejala urbanisasi secara historis.', ['Mencatat keadaan desa dua puluh tahun lalu', 'Mengumpulkan data perpindahan warga', 'Mengidentifikasi pendorong ekonomi', 'Melihat dampak di kota tujuan', 'Menyimpulkan pola perubahan'], 'Gejala dibaca dengan pembandingan waktu.', 'Pola adalah hasil akhir.'),
        ('Urutkan langkah menjaga analisis tetap berbasis bukti.', ['Menentukan pertanyaan', 'Mengumpulkan sumber', 'Memilih konsep yang sesuai', 'Menguji konsep dengan bukti', 'Menuliskan temuan dan keterbatasan'], 'Konsep dipilih setelah pertanyaan dan sumber jelas.', 'Pengujian menjaga analisis tidak mengawang.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
