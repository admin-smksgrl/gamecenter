"""PRA 10 — Pemanfaatan Limbah Budi Daya Ternak (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 10',
    'slug': 'prakarya-10-limbah-ternak',
    'title': 'Pemanfaatan Limbah Budi Daya Ternak',
    'description': (
        'Mengenal jenis dan sumber limbah ternak, dampaknya bagi lingkungan, '
        'pengolahan menjadi kompos, pupuk organik cair, dan maggot, serta '
        'analisis usaha dan budi daya ternak unggas.'
    ),
    'objectives': [
        'Mengidentifikasi industri dan jenis limbah ternak.',
        'Menganalisis dampak lingkungan serta nilai ekonomis limbah ternak.',
        'Merencanakan budi daya ternak dan pemanfaatan limbahnya.',
        'Mempraktikkan pengolahan limbah menjadi kompos dan pupuk organik cair.',
        'Menganalisis usaha pemanfaatan limbah ternak secara finansial dan nonfinansial.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Budi-Daya-BG-KLS-X.pdf Unit III Pemanfaatan Limbah Budi Daya Ternak',
    'glossary': [
        {'term': 'Limbah ternak', 'definition': 'Hasil akhir atau hasil samping dari pemeliharaan ternak, rumah potong hewan, dan pabrik pakan.'},
        {'term': 'Limbah padat', 'definition': 'Limbah berupa kotoran, sisa pakan, tulang, bulu, dan bagian tubuh yang tidak dikonsumsi.'},
        {'term': 'Limbah cair', 'definition': 'Limbah berupa urine dan air cucian kandang atau peralatan.'},
        {'term': 'Pupuk kompos', 'definition': 'Pupuk hasil dekomposisi bahan organik oleh mikroorganisme.'},
        {'term': 'Pupuk organik cair', 'definition': 'Pupuk cair dengan kandungan bahan kimia maksimum 5 persen.'},
        {'term': 'Maggot', 'definition': 'Larva lalat tentara hitam yang dapat menjadi pakan ternak atau ikan.'},
        {'term': 'Biosekuriti', 'definition': 'Upaya pencegahan penyakit melalui kebersihan dan pengendalian lingkungan kandang.'},
        {'term': 'BEP', 'definition': 'Titik impas, yaitu jumlah produksi atau penjualan yang menutup seluruh biaya.'},
    ],
    'intro': {
        'material_title': 'Mengapa limbah ternak harus diolah?',
        'title': 'Dari limbah menjadi sumber nilai',
        'paragraphs': [
            'Limbah ternak adalah hasil akhir atau hasil samping dari pemeliharaan ternak, rumah potong hewan, dan pabrik pakan. Limbah ini tidak dapat dicegah, tetapi dapat dimanfaatkan. Jika dibiarkan, limbah mencemari udara, air, dan tanah.',
            'Limbah peternakan dapat berupa padat dan cair. Limbah padat meliputi kotoran, sisa pakan, tulang, bulu, tanduk, dan kuku. Limbah cair meliputi urine serta air cucian kandang dan peralatan.',
            'Dengan pengolahan yang tepat, limbah ternak berubah menjadi pupuk kompos, pupuk organik cair, atau media tumbuh maggot. Produk ini bernilai ekonomi, mengurangi pencemaran, dan mendukung pertanian berkelanjutan.',
        ],
        'diagram': (
            'Alur pemanfaatan limbah ternak',
            'flowchart LR\n'
            '  A[Limbah ternak] --> B[Pemisahan padat dan cair]\n'
            '  B --> C[Pengomposan]\n'
            '  B --> D[Pupuk organik cair]\n'
            '  C --> E[Pupuk tanaman]\n'
            '  D --> E\n'
            '  B --> F[Media maggot]',
        ),
        'callout': 'Gunakan masker dan sarung tangan saat menangani kotoran ternak. Cuci tangan dengan sabun setelah selesai bekerja.',
        'checkpoint': (
            'Manakah contoh limbah cair ternak?',
            [
                ('Urine dan air cucian kandang', True),
                ('Tulang dan bulu', False),
                ('Sisa pakan kering', False),
                ('Tanduk dan kuku', False),
            ],
            'Limbah cair berupa urine dan air cucian kandang atau peralatan.',
        ),
    },
    'concept': {
        'material_title': 'Jenis limbah dan produk olahannya',
        'title': 'Mengolah limbah menjadi pupuk',
        'paragraphs': [
            'Sumber limbah ternak meliputi peternakan, rumah potong hewan, dan pabrik pakan. Peternakan menghasilkan kotoran, urine, sisa pakan, dan air cucian kandang. Rumah potong hewan menghasilkan darah, tulang, jeroan, bulu, kulit, tanduk, dan kuku. Pabrik pakan menghasilkan sisa bahan baku dan pakan olahan.',
            'Limbah ternak yang tidak diolah mencemari udara melalui gas amoniak, mencemari air hingga merusak ekosistem, dan merusak tanah bila digunakan terus-menerus tanpa perlakuan. Karena itu, limbah perlu diolah sebelum dimanfaatkan.',
            'Pupuk kompos dibuat melalui dekomposisi kotoran ternak dengan bantuan mikroorganisme. Bahan tambahan seperti serbuk gergaji, sekam, jerami, abu, atau kapur memperkaya kandungan kompos. Pupuk organik cair berasal dari urine ternak dan mengandung bahan kimia maksimum 5 persen.',
        ],
        'table': [
            ['Produk', 'Bahan', 'Manfaat'],
            ['Pupuk kompos', 'Kotoran ternak dan bahan organik', 'Menyuburkan tanah'],
            ['Pupuk organik cair', 'Urine ternak', 'Mengaktifkan unsur hara'],
            ['Maggot', 'Limbah organik ternak', 'Pakan ternak dan ikan'],
            ['Biogas', 'Limbah dan kotoran ternak', 'Sumber energi'],
        ],
        'visual': chart_block(
            'pra-10-kandungan-unsur',
            'Perkiraan kandungan unsur hara kompos (%)',
            'bar',
            [('Nitrogen', 2), ('Fosfor', 1), ('Kalium', 2), ('Bahan organik', 30)],
        ),
        'activity': categorize_block(
            'pra-10-klasifikasi',
            'Kelompokkan limbah berikut ke dalam limbah padat atau limbah cair.',
            [('b1', 'Limbah padat'), ('b2', 'Limbah cair')],
            [
                ('i1', 'Kotoran ternak', 'b1'),
                ('i2', 'Tulang', 'b1'),
                ('i3', 'Bulu', 'b1'),
                ('i4', 'Urine', 'b2'),
                ('i5', 'Air cucian kandang', 'b2'),
                ('i6', 'Air cucian peralatan', 'b2'),
            ],
            'Tepat. Kotoran, tulang, dan bulu termasuk limbah padat; urine dan air cucian termasuk limbah cair.',
            'Periksa lagi: limbah cair berbentuk air, limbah padat berbentuk bahan.',
        ),
        'subtitle': 'Budi daya ternak dan analisis usaha',
        'list': [
            'Lima teknik budi daya ternak: lokasi kandang, bibit, pakan, pengendalian penyakit, serta panen dan pascapanen.',
            'Lokasi kandang sebaiknya mudah diakses, jauh dari pemukiman, dan dekat sumber air.',
            'Bibit sehat aktif, mata dan hidung bersih, bulu bersih, tali pusar kering, dan kloaka tidak kotor.',
            'Analisis usaha mencakup aspek finansial (investasi, biaya produksi, BEP) dan nonfinansial (pasar, teknis, manajemen, hukum).',
        ],
        'checkpoint': (
            'Pupuk organik cair memiliki kandungan bahan kimia maksimum…',
            [
                ('5 persen', True),
                ('50 persen', False),
                ('95 persen', False),
                ('100 persen', False),
            ],
            'Pupuk organik cair mengandung bahan kimia maksimum 5 persen.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membuat kompos dan merencanakan usaha',
        'paragraphs': [
            'Kumpulkan kotoran ternak dan bahan organik seperti sekam, jerami, atau serbuk gergaji. Cacah bahan agar mudah terurai, lalu campurkan bahan pemacu mikroorganisme. Tumpuk bahan, tutup, dan balik secara berkala hingga kompos matang dan berbau tanah.',
            'Untuk pupuk organik cair, tampung urine ternak dan simpan dalam wadah tertutup. Fermentasikan dengan bantuan mikroorganisme, lalu encerkan sebelum digunakan. Jangan menyimpan pupuk cair di tempat yang terkena panas langsung.',
            'Susun rencana usaha dengan menghitung biaya investasi, biaya produksi, dan perkiraan pendapatan. Tentukan BEP dan nilai keuntungan. Lengkapi dengan analisis pasar, teknis, manajemen, dan hukum agar usaha layak dijalankan.',
        ],
        'scenario': scenario(
            'pra-10-skenario',
            'Kandang ayam dekat pemukiman',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kandang ayam sekolah menimbulkan bau yang mengganggu warga. Apa langkah pertama?',
                    'choices': [
                        {'text': 'Mengumpulkan kotoran dan mengolahnya menjadi kompos', 'next': 'n2', 'score': 2, 'feedback': 'Pengolahan mengurangi bau dan memberi nilai tambah.'},
                        {'text': 'Membuang kotoran ke sungai', 'next': 'n3', 'score': 0, 'feedback': 'Membuang ke sungai mencemari air dan ekosistem.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Kompos belum matang dan masih berbau. Apa yang dilakukan?',
                    'choices': [
                        {'text': 'Membalik tumpukan dan menambah bahan pemacu', 'next': 'n4', 'score': 2, 'feedback': 'Pembalikan dan bahan pemacu mempercepat pematangan.'},
                        {'text': 'Langsung menjual kompos mentah', 'next': 'n3', 'score': 0, 'feedback': 'Kompos mentah dapat merusak tanaman.'},
                    ],
                },
                {'id': 'n3', 'text': 'Pencemaran meningkat dan usaha merugi.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kompos matang, bau berkurang, dan usaha untung.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan sumber limbah ternak.', 'back': 'Peternakan, rumah potong hewan, dan pabrik pakan.'},
            {'front': 'Apa perbedaan limbah padat dan cair?', 'back': 'Padat berupa kotoran/tulang; cair berupa urine dan air cucian.'},
            {'front': 'Apa bahan kimia maksimum pupuk organik cair?', 'back': '5 persen.'},
            {'front': 'Apa itu biosekuriti?', 'back': 'Upaya pencegahan penyakit melalui kebersihan kandang.'},
        ],
        'checkpoint': (
            'Agar kandang tidak mencemari pemukiman, lokasi kandang sebaiknya…',
            [
                ('Jauh dari pemukiman dan dekat sumber air', True),
                ('Di tengah pemukiman padat', False),
                ('Di atas sungai', False),
                ('Di ruang kelas', False),
            ],
            'Kandang sebaiknya jauh dari pemukiman, mudah diakses, dan dekat sumber air.',
        ),
        'challenge': challenge_block(
            'pra-10-tantangan',
            'Tantangan istilah limbah ternak',
            90,
            [
                ('Hasil samping pemeliharaan ternak', 'limbah ternak'),
                ('Pupuk dari dekomposisi organik', 'kompos'),
                ('Pupuk cair bahan kimia maks 5%', 'pupuk organik cair'),
                ('Larva untuk pakan ikan', 'maggot'),
                ('Titik impas usaha', 'BEP'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Limbah ternak berasal dari…', 'Peternakan, rumah potong hewan, dan pabrik pakan', ['Sekolah dan kantor', 'Pasar dan toko', 'Rumah sakit dan apotek'], 'Limbah ternak dihasilkan peternakan, RPH, dan pabrik pakan.', 'Semua kegiatan yang berhubungan dengan ternak.'),
        ('Manakah contoh limbah padat ternak?', 'Kotoran dan tulang', ['Urine', 'Air cucian kandang', 'Air hujan'], 'Kotoran, tulang, bulu, dan kuku termasuk limbah padat.', 'Limbah cair berbentuk air.'),
        ('Manakah contoh limbah cair ternak?', 'Urine dan air cucian kandang', ['Kotoran', 'Tulang', 'Bulu'], 'Urine dan air cucian kandang termasuk limbah cair.', 'Berasal dari cairan tubuh dan pencucian.'),
        ('Gas yang menimbulkan bau tidak sedap dari kotoran ternak adalah…', 'Amoniak', ['Oksigen', 'Helium', 'Nitrogen cair'], 'Gas amoniak dari kotoran ternak menimbulkan bau menyengat.', 'Bau mengganggu pemukiman sekitar.'),
        ('Pupuk hasil dekomposisi bahan organik oleh mikroorganisme disebut…', 'Kompos', ['Pestisida', 'Biogas', 'Silase'], 'Kompos adalah hasil dekomposisi bahan organik.', 'Bahan dasarnya kotoran ternak.'),
        ('Pupuk organik cair mengandung bahan kimia maksimum…', '5 persen', ['25 persen', '50 persen', '100 persen'], 'Kandungan bahan kimia pupuk organik cair maksimum 5 persen.', 'Sebagian besar berupa bahan organik.'),
        ('Semua urine ternak dapat dimanfaatkan menjadi…', 'Pupuk organik cair', ['Pupuk kompos padat', 'Pakan ternak', 'Biogas'], 'Urine ternak dapat diolah menjadi pupuk organik cair.', 'Pupuk cair mengaktifkan unsur hara.'),
        ('Larva yang dapat dijadikan pakan ikan dari limbah ternak adalah…', 'Maggot', ['Jentik nyamuk', 'Cacing tanah', 'Belalang'], 'Maggot adalah larva yang dibudidayakan dari limbah organik.', 'Maggot kaya protein untuk pakan.'),
        ('Lokasi kandang sebaiknya…', 'Jauh dari pemukiman dan dekat sumber air', ['Di tengah pemukiman', 'Di atas sungai', 'Di dalam kelas'], 'Kandang dijauhkan dari pemukiman agar polusi berkurang.', 'Namun tetap mudah diakses.'),
        ('Ciri bibit ternak yang sehat adalah…', 'Aktif dan mata bersih', ['Lesu dan kotor', 'Tidak mau makan', 'Cacat dan lemah'], 'Bibit sehat aktif, mata dan hidung bersih, serta tidak cacat.', 'Tali pusar kering juga menjadi tanda sehat.'),
        ('Pengendalian penyakit ternak dengan menjaga kebersihan kandang disebut…', 'Biosekuriti', ['Biogas', 'Kompos', 'Fermentasi'], 'Biosekuriti mencegah penyakit melalui kebersihan dan pengendalian lingkungan.', 'Desinfektan dipakai pada area kandang.'),
        ('Hasil panen peternakan antara lain…', 'Ternak hidup, daging, telur, dan susu', ['Padi dan jagung', 'Kain dan benang', 'Kayu dan batu'], 'Hasil peternakan berupa ternak hidup, daging, telur, susu, kulit, dan jeroan.', 'Kotoran juga menjadi hasil samping.'),
        ('Aspek kelayakan usaha limbah ternak meliputi…', 'Finansial dan nonfinansial', ['Hanya finansial', 'Hanya hukum', 'Hanya pemasaran'], 'Kelayakan usaha mencakup aspek finansial dan nonfinansial.', 'Nonfinansial meliputi pasar, teknis, manajemen, hukum.'),
        ('BEP adalah…', 'Titik impas usaha', ['Keuntungan maksimal', 'Biaya investasi', 'Jumlah karyawan'], 'BEP atau Break Even Point adalah titik impas.', 'Pada BEP pendapatan sama dengan biaya.'),
    ],
    'multi': [
        ('Manakah sumber limbah ternak?', ['Peternakan', 'Rumah potong hewan', 'Pabrik pakan'], ['Sekolah', 'Kantor pos'], 'Limbah ternak berasal dari peternakan, RPH, dan pabrik pakan.', 'Sekolah dan kantor bukan sumber limbah ternak.'),
        ('Manakah limbah padat ternak?', ['Kotoran', 'Tulang', 'Bulu'], ['Urine', 'Air cucian kandang'], 'Kotoran, tulang, dan bulu termasuk limbah padat.', 'Urine dan air cucian termasuk limbah cair.'),
        ('Manakah produk bernilai dari limbah ternak?', ['Kompos', 'Pupuk organik cair', 'Maggot'], ['Asap', 'Plastik'], 'Limbah ternak dapat menjadi kompos, pupuk cair, dan maggot.', 'Asap dan plastik bukan produk olahannya.'),
        ('Manakah dampak limbah ternak yang tidak diolah?', ['Pencemaran udara', 'Pencemaran air', 'Pencemaran tanah'], ['Udara menjadi segar', 'Tanah menjadi subur'], 'Limbah yang tidak diolah mencemari udara, air, dan tanah.', 'Pengolahan yang tepat mencegah pencemaran.'),
        ('Manakah teknik budi daya ternak?', ['Penentuan lokasi kandang', 'Penyediaan bibit', 'Pemberian pakan', 'Pengendalian penyakit'], ['Menanam padi', 'Memancing ikan'], 'Teknik budi daya ternak meliputi kandang, bibit, pakan, penyakit, dan panen.', 'Menanam padi bukan budi daya ternak.'),
        ('Manakah aspek nonfinansial usaha?', ['Aspek pasar', 'Aspek teknis', 'Aspek hukum'], ['BEP', 'Biaya investasi'], 'Aspek nonfinansial meliputi pasar, teknis, manajemen, dan hukum.', 'BEP dan biaya investasi termasuk finansial.'),
        ('Manakah ciri bibit ternak sehat?', ['Aktif', 'Mata dan hidung bersih', 'Tidak cacat'], ['Lesu', 'Kotor', 'Cacat'], 'Bibit sehat aktif, bersih, dan tidak cacat.', 'Bibit lemah mudah terserang penyakit.'),
        ('Manakah tahap pengelolaan limbah ternak?', ['Pengumpulan', 'Pengolahan', 'Pemanfaatan'], ['Dibuang ke sungai', 'Dibiarkan menumpuk'], 'Limbah dikumpulkan, diolah, lalu dimanfaatkan.', 'Dibuang ke sungai mencemari lingkungan.'),
    ],
    'pairs': [
        ('Limbah ternak', 'hasil samping pemeliharaan ternak'),
        ('Limbah padat', 'kotoran dan sisa pakan'),
        ('Limbah cair', 'urine dan air cucian kandang'),
        ('Kompos', 'dekomposisi bahan organik'),
        ('Pupuk organik cair', 'pupuk cair bahan kimia maks 5%'),
        ('Maggot', 'larva untuk pakan ikan'),
        ('Biosekuriti', 'pencegahan penyakit ternak'),
        ('BEP', 'titik impas usaha'),
    ],
    'steps': [
        ('Urutkan langkah membuat kompos.', ['Kumpulkan kotoran dan bahan organik', 'Cacah bahan', 'Campur bahan pemacu', 'Tumpuk dan tutup', 'Balik hingga matang'], 'Pengomposan dimulai dari pengumpulan lalu pemeraman.', 'Pembalikan mempercepat pematangan.'),
        ('Urutkan langkah membuat pupuk organik cair.', ['Tampung urine ternak', 'Masukkan ke wadah tertutup', 'Tambahkan mikroorganisme', 'Fermentasikan', 'Encerkan sebelum dipakai'], 'Pupuk cair dibuat melalui fermentasi urine.', 'Wadah harus tertutup.'),
        ('Urutkan langkah budi daya maggot.', ['Siapkan wadah', 'Masukkan limbah organik', 'Letakkan telur lalat tentara hitam', 'Biarkan larva tumbuh', 'Panen maggot'], 'Budi daya maggot dimulai dari penyiapan media.', 'Maggot dipanen saat berukuran cukup.'),
        ('Urutkan langkah memelihara ternak unggas.', ['Siapkan kandang', 'Pilih bibit sehat', 'Beri pakan dan minum', 'Jaga kebersihan kandang', 'Panen sesuai umur'], 'Pemeliharaan dimulai dari kandang dan bibit.', 'Kebersihan mencegah penyakit.'),
        ('Urutkan langkah analisis usaha limbah ternak.', ['Hitung biaya investasi', 'Hitung biaya produksi', 'Perkirakan pendapatan', 'Tentukan BEP', 'Nilai kelayakan usaha'], 'Analisis usaha bergerak dari biaya menuju kelayakan.', 'BEP menunjukkan titik impas.'),
        ('Urutkan langkah evaluasi produk limbah ternak.', ['Uji mutu produk', 'Catat hasil produksi', 'Hitung keuntungan', 'Kumpulkan masukan', 'Susun rencana perbaikan'], 'Evaluasi dimulai dari uji mutu lalu perbaikan.', 'Masukan dipakai untuk pengembangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
