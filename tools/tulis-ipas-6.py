"""IPAS 6 — Ekonomi Kreatif Berbasis Projek IPAS Sesuai Program Keahlian SMK (Kelas X, Fase E)."""
from ipas_common import (
    categorize_block,
    challenge_block,
    scenario,
    timeline_block,
    write_chapter,
)

CH = {
    'code': 'IPAS 6',
    'slug': 'ipas-6-ekonomi-kreatif',
    'title': 'Ekonomi Kreatif Berbasis Projek IPAS Sesuai Program Keahlian SMK',
    'description': (
        'Memahami konsep, ciri, dan manfaat ekonomi kreatif, mengenal bidang-bidang '
        'ekraf menurut Inpres, menganalisis faktor pendorong dan penghambat, serta '
        'merancang projek ekraf sesuai program keahlian SMK.'
    ),
    'objectives': [
        'Menjelaskan konsep, ciri, dan manfaat ekonomi kreatif.',
        'Mengidentifikasi bidang-bidang ekonomi kreatif di Indonesia.',
        'Menganalisis faktor pendorong dan penghambat ekonomi kreatif.',
        'Memilih ide projek ekraf yang sesuai program keahlian SMK.',
        'Merancang, mengevaluasi, dan menindaklanjuti projek ekonomi kreatif.',
    ],
    'minutes': 180,
    'source': (
        'Projek-IPAS-BS-KLS-X.pdf Bab 6 Ekonomi Kreatif Berbasis Projek IPAS; '
        'UU No. 24 Tahun 2019 tentang Ekonomi Kreatif; Inpres No. 6 Tahun 2009; '
        'CP Fase E Projek IPAS'
    ),
    'glossary': [
        {'term': 'Ekonomi kreatif', 'definition': 'Perwujudan nilai tambah dari kekayaan intelektual yang bersumber pada kreativitas manusia.'},
        {'term': 'Kreativitas', 'definition': 'Kemampuan menciptakan atau menghasilkan sesuatu yang baru.'},
        {'term': 'Inovasi', 'definition': 'Ide, praktik, atau produk baru yang diterima sebagai hal baru oleh masyarakat.'},
        {'term': 'Kekayaan intelektual', 'definition': 'Hak yang timbul dari hasil olah pikir yang menghasilkan produk atau proses berguna.'},
        {'term': 'Kriya', 'definition': 'Kerajinan tangan bermuatan seni dari bahan seperti kayu, rotan, tanah liat, atau tekstil.'},
        {'term': 'PDB', 'definition': 'Produk Domestik Bruto, nilai seluruh produksi barang dan jasa suatu negara dalam kurun waktu tertentu.'},
        {'term': 'Labelling', 'definition': 'Memberikan label atau merek pada kemasan produk.'},
        {'term': 'Upscaling', 'definition': 'Usaha memperluas cakupan atau skala produksi sebuah produk.'},
    ],
    'intro': {
        'material_title': 'Mengapa ekonomi kreatif penting?',
        'title': 'Konsep dan ciri ekonomi kreatif',
        'paragraphs': [
            'Menurut UU No. 24 Tahun 2019, ekonomi kreatif adalah perwujudan nilai tambah dari kekayaan intelektual yang bersumber pada kreativitas manusia, berbasis warisan budaya, ilmu pengetahuan, dan atau teknologi. Modal utamanya adalah gagasan dan ide.',
            'Ciri ekonomi kreatif: berbasis ide dan kreativitas, hasil olah pikir intelektual, kolaboratif, tidak terbatas bentuk dan harga, mengandung nilai budaya, mudah berubah mengikuti zaman, serta menyesuaikan perkembangan kebutuhan.',
            'Manfaatnya meliputi penyediaan lapangan kerja, pengurangan pengangguran, pendorong inovasi, peningkatan pertumbuhan ekonomi, dan kenaikan kualitas produk. Pada 2017 pertumbuhan ekraf mencapai 5,06%, dan pada 2019 menghadirkan 18,1 juta lapangan kerja.',
        ],
        'diagram': (
            'Dari ide menjadi nilai ekonomi',
            'flowchart LR\n'
            '  A[Kreativitas] --> B[Inovasi]\n'
            '  B --> C[Produk barang atau jasa]\n'
            '  C --> D[Kekayaan intelektual]\n'
            '  D --> E[Nilai tambah]\n'
            '  E --> F[Lapangan kerja dan pertumbuhan ekonomi]',
        ),
        'callout': 'Ekonomi kreatif memadukan warisan budaya, ilmu pengetahuan, dan teknologi; tiga ranahnya adalah kreativitas, inovasi, dan penemuan.',
        'checkpoint': (
            'Menurut UU No. 24 Tahun 2019, ekonomi kreatif bersumber pada…',
            [
                ('kreativitas manusia berbasis budaya, ilmu pengetahuan, dan teknologi', True),
                ('kepemilikan tambang dan ladang', False),
                ('jumlah ekspor minyak bumi', False),
                ('besar kecilnya subsidi pemerintah', False),
            ],
            'Nilai tambah ekraf berasal dari kekayaan intelektual yang digerakkan kreativitas manusia.',
        ),
    },
    'concept': {
        'material_title': 'Bidang dan faktor perkembangan ekraf',
        'title': 'Subsektor ekraf serta pendorong dan penghambatnya',
        'paragraphs': [
            'Berdasarkan Inpres No. 6 Tahun 2009, bidang ekonomi kreatif meliputi periklanan, arsitektur, pasar seni dan barang antik, kerajinan (kriya), desain, fashion, film, video dan fotografi, serta game interaktif.',
            'Faktor pendorong perkembangan ekraf: kreativitas sebagai modal utama, ketersediaan modal, dukungan teknologi, kualitas sumber daya manusia, dan kebijakan pemerintah yang berpihak pada pelaku ekraf.',
            'Faktor penghambatnya: keterbatasan bahan baku, kekurangan modal, kualitas SDM yang belum sesuai pasar, pemanfaatan teknologi yang rendah, dan pemasaran yang lemah sehingga produk menumpuk.',
        ],
        'table': [
            ['Bidang ekraf', 'Contoh produk', 'Kaitannya dengan kreativitas'],
            ['Periklanan', 'Iklan di media cetak dan digital', 'Ide kreatif mengubah sudut pandang konsumen'],
            ['Arsitektur', 'Desain dan perawatan bangunan', 'Menciptakan ruang bernilai tinggi'],
            ['Pasar seni dan barang antik', 'Batik, lukisan, alat musik', 'Memadukan kerajinan dan pariwisata'],
            ['Kriya', 'Produk rotan, kayu, tanah liat', 'Nilai seni dan estetika tinggi'],
            ['Desain', 'Kemasan, grafis, interior', 'Tampilan produk menjadi menarik'],
            ['Fashion', 'Pakaian, alas kaki, aksesori', 'Identitas dan gaya hidup konsumen'],
            ['Film, video, fotografi', 'Tayangan dan konten visual', 'Skrip, editing, dan tata suara kreatif'],
            ['Game interaktif', 'Permainan dan aplikasi', 'Ide, imajinasi, dan teknologi'],
        ],
        'visual': timeline_block(
            'ipas-6-timeline-ekraf',
            [
                ('2009', 'Inpres No. 6 Tahun 2009', 'Bidang ekonomi kreatif dikelompokkan menjadi 17 subsektor.'),
                ('2016', 'Sumbangsih PDB terus meningkat', 'BPS mencatat kontribusi ekraf terhadap PDB naik setiap tahun.'),
                ('2017', 'Pertumbuhan 5,06%', 'Angka pertumbuhan ekonomi kreatif mencapai 5,06%.'),
                ('2019', '18,1 juta lapangan kerja', 'Ekraf menghadirkan lapangan kerja bagi masyarakat Indonesia.'),
                ('2019', 'UU No. 24 Tahun 2019', 'Definisi resmi ekonomi kreatif ditetapkan dalam undang-undang.'),
            ],
        ),
        'activity': categorize_block(
            'ipas-6-klasifikasi',
            'Kelompokkan faktor berikut menjadi pendorong atau penghambat ekraf.',
            [('b1', 'Pendorong'), ('b2', 'Penghambat')],
            [
                ('i1', 'Kreativitas masyarakat tinggi', 'b1'),
                ('i2', 'Kebijakan pemerintah yang mendukung', 'b1'),
                ('i3', 'Teknologi pemasaran yang memadai', 'b1'),
                ('i4', 'Bahan baku sulit didapat', 'b2'),
                ('i5', 'Modal usaha terbatas', 'b2'),
                ('i6', 'Pemasaran produk lemah', 'b2'),
                ('i7', 'SDM yang kreatif dan terampil', 'b1'),
                ('i8', 'Produk belum sesuai kualifikasi pasar', 'b2'),
            ],
            'Tepat. Pendorong mendukung pertumbuhan, penghambat menghambat produksi dan pemasaran.',
            'Periksa lagi: bahan baku sulit dan modal terbatas justru memperlambat ekraf.',
        ),
        'subtitle': 'Dari konsep menjadi projek ekraf',
        'list': [
            'Memilih ide projek yang sesuai program keahlian, misalnya olahan makanan, kriya kain, jasa penginapan, atau aplikasi digital.',
            'Membuat desain purwarupa yang terinci: komponen, bahan, biaya, dan cara penggunaan.',
            'Mencantumkan nilai tambah dan kebaruan (novelty) projek dibanding produk sejenis.',
            'Mengevaluasi produk lalu menyusun rencana tindak lanjut: perbaikan, pengembangan produksi, atau sosialisasi.',
        ],
        'checkpoint': (
            'Batik, lukisan, dan alat musik biasanya diperdagangkan di…',
            [
                ('pasar seni dan barang antik', True),
                ('pasar tradisional sayur', False),
                ('terminal bus', False),
                ('laboratorium riset', False),
            ],
            'Pasar seni menjadi pusat perdagangan hasil kreativitas bernilai estetika tinggi.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Projek ekraf sesuai program keahlian',
        'paragraphs': [
            'Projek ekonomi kreatif dijalankan dalam lima kegiatan: mendesain purwarupa, membangun, mengevaluasi, mendesain ulang berdasarkan hasil evaluasi, dan menyusun rencana tindak lanjut.',
            'Contoh projek: kerajinan bambu dengan kendala pemasaran diatasi lewat penjualan daring, olahan singkong dengan harga bahan baku mahal diatasi dengan mendatangkan bahan dari daerah penghasil, dan jasa penginapan kekurangan modal diatasi dengan homestay.',
            'Pada tahap pemasaran, pelaku dapat memakai media sosial, e-commerce, dan marketplace. Keberhasilan projek diukur dari penerimaan pasar, nilai tambah, serta keberlanjutannya setelah kegiatan selesai.',
        ],
        'scenario': scenario(
            'ipas-6-skenario',
            'Produk kriya yang belum laku',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Produk kriya sekolahmu berkualitas tetapi sulit laku. Apa diagnosis pertama?',
                    'choices': [
                        {'text': 'Menganalisis pemasaran, target pasar, dan harga', 'next': 'n2', 'score': 2, 'feedback': 'Diagnosis pemasaran sebelum memperbaiki produk.'},
                        {'text': 'Menghentikan produksi permanen', 'next': 'n3', 'score': 0, 'feedback': 'Berhenti tanpa diagnosis tidak menyelesaikan masalah.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Ternyata kemasan polos dan tidak ada label merek. Apa yang diperbaiki?',
                    'choices': [
                        {'text': 'Mendesain kemasan dan label, lalu memasarkan daring', 'next': 'n4', 'score': 2, 'feedback': 'Kemasan menarik dan pemasaran daring memperluas jangkauan.'},
                        {'text': 'Menurunkan harga jauh di bawah biaya produksi', 'next': 'n3', 'score': 0, 'feedback': 'Harga di bawah biaya membuat usaha rugi.'},
                    ],
                },
                {'id': 'n3', 'text': 'Usaha merugi atau berhenti karena keputusan yang tidak tepat.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Produk dikenal, laku, dan kelompok mendapat keuntungan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa modal utama ekonomi kreatif?', 'back': 'Ide, gagasan, dan kreativitas.'},
            {'front': 'Sebutkan tiga bidang ekraf.', 'back': 'Kriya, fashion, dan desain.'},
            {'front': 'Apa itu kekayaan intelektual?', 'back': 'Hak yang timbul dari hasil olah pikir yang berguna.'},
            {'front': 'Sebutkan dua faktor penghambat ekraf.', 'back': 'Keterbatasan modal dan lemahnya pemasaran.'},
        ],
        'checkpoint': (
            'Pemasaran produk ekraf dapat dilakukan melalui…',
            [
                ('media sosial, e-commerce, dan marketplace', True),
                ('hanya mengandalkan kios di sekolah', False),
                ('menyimpan produk di gudang', False),
                ('menghapus label produk', False),
            ],
            'Teknologi informasi membantu menjangkau pasar lebih luas dengan biaya kecil.',
        ),
        'challenge': challenge_block(
            'ipas-6-tantangan',
            'Tantangan istilah ekonomi kreatif',
            90,
            [
                ('Undang-undang ekonomi kreatif', 'UU 24/2019'),
                ('Nilai seluruh produksi barang dan jasa negara', 'PDB'),
                ('Kerajinan tangan bernilai seni', 'Kriya'),
                ('Label atau merek pada kemasan', 'Labelling'),
                ('Memperluas skala produksi', 'Upscaling'),
            ],
            'Lima istilah ekonomi kreatif terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Menurut UU No. 24 Tahun 2019, ekonomi kreatif adalah…', 'perwujudan nilai tambah dari kekayaan intelektual berbasis kreativitas', ['perdagangan hasil tambang', 'ekspor bahan baku hutan', 'produksi pangan massal'], 'Ekraf lahir dari kreativitas manusia berbasis budaya, IPTEK, dan teknologi.', 'Modal utamanya ide, bukan sumber daya alam.'),
        ('Apa modal utama ekonomi kreatif?', 'ide, gagasan, dan kreativitas', ['modal tambang', 'jumlah karyawan', 'luas gedung'], 'Ekonomi kreatif bersumber pada ide dan kreativitas manusia.', 'Input dan outputnya berupa gagasan.'),
        ('Berapa pertumbuhan ekonomi kreatif Indonesia pada 2017?', '5,06%', ['1,06%', '9,06%', '15,06%'], 'Pertumbuhan ekraf 2017 mencapai 5,06%.', 'Data ini menurut BPS.'),
        ('Berapa lapangan kerja yang dihadirkan ekonomi kreatif pada 2019?', '18,1 juta', ['8,1 juta', '28,1 juta', '1,81 juta'], 'Pada 2019 ekraf menghadirkan 18,1 juta lapangan kerja.', 'Menunjukkan besarnya kontribusi ekraf.'),
        ('Bidang ekonomi kreatif diatur dalam…', 'Inpres No. 6 Tahun 2009', ['UU No. 24 Tahun 2007', 'Inpres No. 6 Tahun 2019', 'Perpres No. 1 Tahun 2010'], 'Inpres 6/2009 mengelompokkan bidang ekonomi kreatif.', 'Meliputi 17 subsektor.'),
        ('Manakah yang termasuk bidang ekonomi kreatif?', 'kriya', ['pertambangan batu bara', 'perkebunan kelapa sawit', 'perikanan tangkap'], 'Kriya adalah kerajinan tangan bernilai seni.', 'Bidang lain seperti arsitektur dan desain juga bagian ekraf.'),
        ('Kegiatan produksi kerajinan pengrajin yang bernilai estetika disebut…', 'kriya', ['pabrikasi', 'distribusi', 'ekspedisi'], 'Kriya mencakup produksi dan distribusi produk pengrajin.', 'Bahan bakunya seperti rotan, kayu, dan tanah liat.'),
        ('Salah satu ciri ekonomi kreatif adalah…', 'berbasis ide dan kreativitas', ['bergantung pada cuaca', 'memakai tenaga mesin berat', 'terbatas pada satu kota'], 'Ciri utamanya berbasis ide dan kreativitas.', 'Hasilnya berupa olah intelektual.'),
        ('Manakah faktor pendorong ekonomi kreatif?', 'kebijakan pemerintah yang mendukung', ['bahan baku sulit didapat', 'pemasaran produk lemah', 'modal usaha terbatas'], 'Dukungan pemerintah memacu pertumbuhan ekraf.', 'Bahan baku sulit justru menghambat.'),
        ('Manakah faktor penghambat ekonomi kreatif?', 'pemasaran yang lemah', ['kreativitas tinggi', 'teknologi pemasaran memadai', 'SDM yang terampil'], 'Pemasaran lemah membuat produk menumpuk.', 'Produk tidak sampai ke konsumen.'),
        ('Batik, lukisan, dan alat musik diperdagangkan di…', 'pasar seni dan barang antik', ['pasar modal', 'bursa saham', 'pelelangan ikan'], 'Pasar seni menjual hasil kreativitas bernilai estetika tinggi.', 'Sekaligus menjadi ajang promosi wisata.'),
        ('Label atau merek pada kemasan produk disebut…', 'labelling', ['branding', 'marketing', 'budgeting'], 'Labelling memberi identitas pada kemasan produk.', 'Berbeda dengan strategi branding secara menyeluruh.'),
        ('Apa yang diukur dengan PDB?', 'nilai seluruh produksi barang dan jasa negara', ['jumlah penduduk', 'luas wilayah', 'jumlah kendaraan'], 'PDB menghitung nilai produksi barang dan jasa.', 'Kontribusi ekraf terlihat dari PDB.'),
        ('Kegiatan memperluas skala produksi produk disebut…', 'upscaling', ['downgrading', 'reboisasi', 'lokalisasi'], 'Upscaling memperluas cakupan atau skala produksi.', 'Misalnya dari skala kelompok menjadi sekolah.'),
    ],
    'multi': [
        ('Manakah ciri ekonomi kreatif?', ['Berbasis ide dan kreativitas', 'Mengandung nilai budaya', 'Mudah menyesuaikan zaman'], ['Mengandalkan cadangan fosil', 'Terikat satu musim'], 'Ciri ekraf berkaitan dengan ide, budaya, dan perubahan zaman.', 'Fosil dan musim bukan ciri ekraf.'),
        ('Manakah manfaat ekonomi kreatif?', ['Menyediakan lapangan kerja', 'Mengurangi pengangguran', 'Mendorong inovasi'], ['Menambah polusi udara', 'Meningkatkan impor minyak'], 'Ekraf membuka kerja dan menumbuhkan inovasi.', 'Berkontribusi pada pertumbuhan ekonomi.'),
        ('Manakah bidang ekonomi kreatif?', ['Periklanan', 'Arsitektur', 'Game interaktif'], ['Tambang emas', 'Sawit rakyat'], 'Periklanan, arsitektur, dan game termasuk subsektor ekraf.', 'Tambang dan sawit bukan subsektor ekraf.'),
        ('Manakah faktor pendorong ekraf?', ['Kreativitas', 'Teknologi', 'Kebijakan pemerintah'], ['Kelangkaan bahan', 'Pemasaran lemah'], 'Kreativitas, modal, teknologi, SDM, dan kebijakan mendorong ekraf.', 'Kelangkaan bahan justru menghambat.'),
        ('Manakah faktor penghambat ekraf?', ['Keterbatasan bahan baku', 'Kurang modal', 'Pemasaran lemah'], ['SDM kreatif', 'Kebijakan mendukung'], 'Bahan, modal, SDM, teknologi, dan pemasaran dapat menghambat ekraf.', 'SDM kreatif adalah pendorong.'),
        ('Manakah solusi mengatasi hambatan pemasaran?', ['Memanfaatkan media sosial', 'Memakai e-commerce', 'Memakai marketplace'], ['Menyimpan produk di gudang', 'Menghapus merek'], 'Teknologi informasi memperluas pasar ekraf.', 'Gudang tidak menjual produk.'),
        ('Manakah tahap projek ekonomi kreatif?', ['Mendesain purwarupa', 'Membangun purwarupa', 'Mengevaluasi purwarupa'], ['Menghentikan projek', 'Menghindari evaluasi'], 'Projek berjalan dari desain sampai evaluasi dan tindak lanjut.', 'Evaluasi menentukan perbaikan.'),
        ('Manakah bentuk rencana tindak lanjut ekraf?', ['Mendesain ulang produk', 'Pengembangan produksi', 'Sosialisasi kepada masyarakat'], ['Membuang produk', 'Menutup usaha'], 'RTL memperbaiki, mengembangkan, dan mensosialisasikan produk.', 'Semua menjaga keberlanjutan projek.'),
    ],
    'pairs': [
        ('Ekonomi kreatif', 'nilai tambah dari kekayaan intelektual'),
        ('Kreativitas', 'kemampuan menciptakan sesuatu yang baru'),
        ('Kriya', 'kerajinan tangan bernilai seni'),
        ('PDB', 'nilai seluruh produksi barang dan jasa'),
        ('Labelling', 'memberi label pada kemasan'),
        ('Upscaling', 'memperluas skala produksi'),
        ('Kekayaan intelektual', 'hak dari hasil olah pikir'),
        ('Pasar seni', 'pusat perdagangan karya kreatif'),
    ],
    'steps': [
        ('Urutkan alur dari ide menjadi nilai ekonomi.', ['Kreativitas', 'Inovasi', 'Produk barang atau jasa', 'Kekayaan intelektual', 'Nilai tambah'], 'Ekraf dimulai dari kreativitas lalu berujung pada nilai tambah.', 'Inovasi lahir dari kreativitas.'),
        ('Urutkan tahap projek ekonomi kreatif.', ['Mendesain purwarupa', 'Membangun purwarupa', 'Mengevaluasi purwarupa', 'Mendesain ulang bila perlu', 'Menyusun rencana tindak lanjut'], 'Projek berjalan dari desain sampai tindak lanjut.', 'Desain ulang dilakukan setelah evaluasi.'),
        ('Urutkan langkah memasarkan produk ekraf.', ['Menentukan target pasar', 'Menyiapkan produk dan kemasan', 'Memasang label dan merek', 'Mengunggah ke media sosial atau marketplace', 'Mencatat pesanan dan umpan balik'], 'Pemasaran dimulai dari target pasar sampai pencatatan umpan balik.', 'Umpan balik dipakai memperbaiki produk.'),
        ('Urutkan langkah mengatasi kendala pemasaran.', ['Menganalisis penyebab produk sulit laku', 'Memperbaiki kemasan dan label', 'Menentukan kanal pemasaran daring', 'Menjalankan promosi', 'Mengevaluasi penjualan'], 'Perbaikan dimulai dari analisis sampai evaluasi penjualan.', 'Promosi mengikuti kanal yang dipilih.'),
        ('Urutkan langkah menyusun desain purwarupa ekraf.', ['Menentukan ide dan konsep', 'Mengumpulkan referensi produk', 'Menggambar atau mendeskripsikan desain', 'Mencantumkan komponen, bahan, dan biaya', 'Menentukan nilai kebaruan'], 'Desain diawali konsep lalu diakhiri penegasan kebaruan.', 'Kebaruan menarik konsumen.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)