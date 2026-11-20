"""PRA 3 — Produk Aksesoris Eksterior dengan Bahan Lokal (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 3',
    'slug': 'prakarya-3-aksesoris-eksterior',
    'title': 'Produk Aksesoris Eksterior dengan Memanfaatkan Bahan Lokal',
    'description': (
        'Merancang aksesoris eksterior dari bahan lokal yang tahan cuaca, '
        'menerapkan konstruksi yang kuat, serta mengevaluasi produk secara '
        'berkelompok.'
    ),
    'objectives': [
        'Menganalisis potensi bahan lokal untuk aksesoris eksterior.',
        'Merancang produk aksesoris eksterior yang kuat, aman, dan ergonomis.',
        'Membuat produk aksesoris eksterior secara berkelompok.',
        'Menerapkan pengawetan dan finishing agar produk tahan cuaca.',
        'Mengevaluasi kekuatan, keindahan, dan dampak lingkungan produk.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Kerajinan-BG-KLS-X.pdf Unit 3 Produk Aksesoris Eksterior dengan Memanfaatkan Bahan Lokal',
    'glossary': [
        {'term': 'Aksesoris eksterior', 'definition': 'Benda penghias dan pelengkap area luar ruangan seperti taman dan teras.'},
        {'term': 'Bahan lokal', 'definition': 'Bahan yang tersedia di daerah sekitar tempat tinggal atau sekolah.'},
        {'term': 'Tahan cuaca', 'definition': 'Sifat bahan atau produk yang tidak cepat rusak akibat hujan dan panas.'},
        {'term': 'Pengawetan', 'definition': 'Proses melindungi bahan alami dari jamur, serangga, dan pembusukan.'},
        {'term': 'Anti karat', 'definition': 'Lapisan pelindung pada logam agar tidak berkarat.'},
        {'term': 'Konstruksi', 'definition': 'Susunan dan sambungan bagian produk agar kuat dan stabil.'},
        {'term': 'Ramah lingkungan', 'definition': 'Produk yang memanfaatkan bahan sekitar dan tidak menimbulkan pencemaran berlebihan.'},
        {'term': 'Evaluasi', 'definition': 'Penilaian terhadap kekuatan, keindahan, fungsi, dan dampak produk.'},
    ],
    'intro': {
        'material_title': 'Mengapa aksesoris eksterior menantang?',
        'title': 'Menghias ruang luar dengan bahan sekitar',
        'paragraphs': [
            'Aksesoris eksterior adalah benda yang memperindah area luar ruangan, seperti taman, teras, dan halaman. Contohnya lampu taman, pot tanaman, hiasan pagar, angin-angin, dan tempat duduk sederhana.',
            'Produk eksterior menghadapi cuaca yang lebih keras daripada produk interior. Hujan, panas matahari, dan angin dapat merusak bahan jika tidak dipilih dan dirawat dengan benar. Karena itu, bahan lokal perlu diolah dan dilapisi agar tahan lama.',
            'Memanfaatkan bahan lokal mengurangi biaya dan mendukung ekonomi daerah. Dengan rancangan yang baik, aksesoris eksterior dapat menjadi produk bernilai jual sekaligus memperkuat identitas lingkungan.',
        ],
        'diagram': (
            'Alur proyek aksesoris eksterior',
            'flowchart LR\n'
            '  A[Observasi area luar] --> B[Pemilihan bahan lokal]\n'
            '  B --> C[Perancangan konstruksi]\n'
            '  C --> D[Pembuatan kelompok]\n'
            '  D --> E[Pengawetan dan finishing]\n'
            '  E --> F[Evaluasi produk]',
        ),
        'callout': 'Gunakan sarung tangan dan kacamata pelindung saat memotong bambu, mengampelas kayu, atau mengelas logam.',
        'checkpoint': (
            'Apa yang dimaksud aksesoris eksterior?',
            [
                ('Benda penghias area luar ruangan', True),
                ('Benda penghias kamar tidur', False),
                ('Alat tulis sekolah', False),
                ('Pakaian yang dipakai di tubuh', False),
            ],
            'Aksesoris eksterior memperindah area luar seperti taman dan teras.',
        ),
    },
    'concept': {
        'material_title': 'Bahan, konstruksi, dan perawatan',
        'title': 'Memilih bahan yang tahan cuaca',
        'paragraphs': [
            'Bahan lokal yang umum dipakai untuk aksesoris eksterior adalah bambu, kayu, batu, dan logam. Bambu ringan dan lentur, kayu kuat dan mudah dibentuk, batu tahan lama, sedangkan logam cocok untuk rangka dan lampu.',
            'Bahan alami perlu diawetkan sebelum dipakai. Bambu dikeringkan dan dilapisi anti jamur, kayu diamplas lalu dicat atau dipelitur, sedangkan logam dilapisi cat anti karat. Pengawetan memperpanjang usia produk.',
            'Konstruksi produk harus stabil karena menahan beban dan terpapar angin. Sambungan diperkuat dengan paku, sekrup, ikatan, atau las sesuai bahan. Produk juga harus diberi alas atau ditanam dengan baik agar tidak mudah roboh.',
        ],
        'table': [
            ['Bahan', 'Kelebihan', 'Perawatan'],
            ['Bambu', 'Ringan dan lentur', 'Keringkan, lapisi anti jamur'],
            ['Kayu', 'Kuat dan mudah dibentuk', 'Ampelas, cat atau pelitur'],
            ['Batu', 'Tahan lama', 'Bersihkan lumut secara berkala'],
            ['Logam', 'Kokoh untuk rangka', 'Lapisi cat anti karat'],
        ],
        'visual': chart_block(
            'pra-3-daya-tahan',
            'Perkiraan daya tahan bahan tanpa perawatan (tahun)',
            'bar',
            [('Bambu', 2), ('Kayu', 5), ('Logam', 8), ('Batu', 15)],
        ),
        'activity': categorize_block(
            'pra-3-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam bahan tahan cuaca atau bahan mudah rusak.',
            [('b1', 'Tahan cuaca'), ('b2', 'Mudah rusak')],
            [
                ('i1', 'Batu alam', 'b1'),
                ('i2', 'Logam berlapis anti karat', 'b1'),
                ('i3', 'Kayu yang dicat', 'b1'),
                ('i4', 'Bambu basah tanpa perawatan', 'b2'),
                ('i5', 'Kertas tanpa pelapis', 'b2'),
                ('i6', 'Kain tipis tanpa pelindung', 'b2'),
            ],
            'Tepat. Batu, logam berlapis, dan kayu bercat lebih tahan cuaca; bahan tanpa perawatan mudah rusak.',
            'Periksa lagi: pengawetan dan pelapisan menentukan ketahanan.',
        ),
        'subtitle': 'Keselamatan dan kerja kelompok',
        'list': [
            'Bagikan tugas sesuai kemampuan: pengukuran, pemotongan, perakitan, dan finishing.',
            'Periksa alat sebelum dipakai dan simpan kembali setelah selesai.',
            'Gunakan alas kerja agar serpihan tidak berserakan dan melukai kaki.',
            'Buang sisa bahan dengan rapi dan pisahkan yang masih dapat didaur ulang.',
        ],
        'checkpoint': (
            'Mengapa logam perlu dilapisi cat anti karat?',
            [
                ('Agar tidak berkarat akibat air dan udara', True),
                ('Agar warnanya berubah setiap hari', False),
                ('Agar menjadi lebih berat', False),
                ('Agar mudah dipotong', False),
            ],
            'Cat anti karat melindungi logam dari air dan udara yang memicu karat.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Membangun produk eksterior bersama',
        'paragraphs': [
            'Amati area luar sekolah atau rumah. Tentukan satu kebutuhan, misalnya pot tanaman untuk teras atau lampu taman sederhana. Ukur ruang agar produk tidak menghalangi jalan.',
            'Bagi kelompok menjadi beberapa peran: pencatat ukuran, pemotong bahan, perakit, dan penanggung jawab finishing. Setiap peran bertanggung jawab pada mutu bagiannya.',
            'Uji produk setelah selesai: goyangkan untuk memeriksa kestabilan, siram sedikit air untuk melihat reaksi lapisan, dan periksa apakah ada bagian tajam yang membahayakan.',
        ],
        'scenario': scenario(
            'pra-3-skenario',
            'Lampu taman untuk sekolah',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kelompokmu membuat lampu taman dari bambu. Bagian mana yang perlu diperkuat?',
                    'choices': [
                        {'text': 'Sambungan dan alas agar tidak roboh', 'next': 'n2', 'score': 2, 'feedback': 'Konstruksi stabil mencegah produk tumbang.'},
                        {'text': 'Warna cat saja', 'next': 'n3', 'score': 0, 'feedback': 'Warna tidak menjamin kekuatan konstruksi.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Hujan deras mengguyur setiap hari. Apa perawatan yang tepat?',
                    'choices': [
                        {'text': 'Melapisi ulang dengan pelindung anti jamur', 'next': 'n4', 'score': 2, 'feedback': 'Pelapisan ulang menjaga bambu tetap awet.'},
                        {'text': 'Membiarkan air menggenang di sambungan', 'next': 'n3', 'score': 0, 'feedback': 'Air menggenang mempercepat pembusukan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Produk cepat rusak dan tidak aman dipakai.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Lampu taman bertahan lama dan memperindah halaman.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan bahan lokal untuk aksesoris eksterior.', 'back': 'Bambu, kayu, batu, dan logam.'},
            {'front': 'Apa fungsi pengawetan?', 'back': 'Melindungi bahan dari jamur, serangga, dan pembusukan.'},
            {'front': 'Bagaimana merawat logam eksterior?', 'back': 'Melapisi dengan cat anti karat.'},
            {'front': 'Apa yang dievaluasi dari produk eksterior?', 'back': 'Kekuatan, keindahan, fungsi, dan dampak lingkungan.'},
        ],
        'checkpoint': (
            'Sebelum produk eksterior dipasang, hal yang wajib diperiksa adalah…',
            [
                ('Kestabilan dan tidak ada bagian tajam', True),
                ('Jumlah warna cat', False),
                ('Nama pembuat produk', False),
                ('Harga bahan termahal', False),
            ],
            'Kestabilan dan keamanan harus diperiksa agar produk tidak melukai atau roboh.',
        ),
        'challenge': challenge_block(
            'pra-3-tantangan',
            'Tantangan istilah aksesoris eksterior',
            90,
            [
                ('Benda penghias area luar', 'aksesoris eksterior'),
                ('Bahan pipih beruas', 'bambu'),
                ('Lapisan pelindung logam', 'anti karat'),
                ('Proses melindungi bahan alami', 'pengawetan'),
                ('Penilaian produk', 'evaluasi'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa yang dimaksud aksesoris eksterior?', 'Benda penghias area luar ruangan', ['Benda penghias kamar', 'Alat tulis', 'Pakaian olahraga'], 'Aksesoris eksterior memperindah area luar seperti taman dan teras.', 'Contohnya lampu taman dan pot.'),
        ('Manakah contoh aksesoris eksterior?', 'Lampu taman', ['Vas ruang tamu', 'Hiasan dinding kamar', 'Bantal sofa'], 'Lampu taman dipakai di area luar ruangan.', 'Vas dan bantal termasuk interior.'),
        ('Manakah bahan yang tahan cuaca?', 'Batu alam', ['Kertas', 'Kain tipis', 'Rumput kering'], 'Batu alam tahan terhadap hujan dan panas.', 'Bahan lain mudah rusak.'),
        ('Mengapa bambu perlu dikeringkan sebelum dipakai?', 'Agar tidak mudah berjamur', ['Agar menjadi lebih berat', 'Agar warnanya hilang', 'Agar mudah patah'], 'Bambu basah mudah berjamur dan berubah bentuk.', 'Pengeringan meningkatkan ketahanan.'),
        ('Apa lapisan pelindung untuk logam?', 'Cat anti karat', ['Lem kertas', 'Air gula', 'Minyak wangi'], 'Cat anti karat melindungi logam dari korosi.', 'Air dan udara memicu karat.'),
        ('Apa fungsi konstruksi yang kuat pada produk eksterior?', 'Agar produk stabil dan tidak mudah roboh', ['Agar produk lebih ringan', 'Agar warna lebih cerah', 'Agar bahan cepat rusak'], 'Konstruksi kuat menahan beban dan terpaan angin.', 'Sambungan harus diperkuat.'),
        ('Mengapa bahan lokal menguntungkan?', 'Mengurangi biaya dan mendukung ekonomi daerah', ['Menambah biaya transportasi', 'Membuat produk cepat rusak', 'Menghilangkan ciri daerah'], 'Bahan lokal lebih murah dan memperkuat identitas daerah.', 'Pemanfaatannya juga lebih ramah lingkungan.'),
        ('Apa tujuan pengawetan bahan alami?', 'Melindungi dari jamur dan serangga', ['Mengubah warna menjadi putih', 'Menambah berat produk', 'Membuat bahan mudah pecah'], 'Pengawetan memperpanjang usia bahan alami.', 'Bambu dan kayu perlu diawetkan.'),
        ('Bagaimana merawat produk batu dari lumut?', 'Membersihkannya secara berkala', ['Membiarkannya berlumut', 'Menyiram dengan minyak', 'Membakarnya'], 'Lumut dibersihkan agar permukaan tidak licin dan tetap indah.', 'Perawatan rutin menjaga penampilan.'),
        ('Apa yang meningkatkan nilai jual produk eksterior?', 'Desain unik dan kualitas konstruksi', ['Bagian tajam yang berbahaya', 'Bahan yang mudah lapuk', 'Kemasan rusak'], 'Desain unik dan konstruksi kuat membuat produk bernilai.', 'Keamanan juga meningkatkan kepercayaan pembeli.'),
        ('Mengapa kerja kelompok membutuhkan pembagian tugas?', 'Agar pekerjaan selesai efisien dan teratur', ['Agar semua bekerja pada bagian yang sama', 'Agar tidak ada yang bertanggung jawab', 'Agar produk cepat rusak'], 'Pembagian tugas membuat pekerjaan lebih efisien.', 'Setiap anggota bertanggung jawab pada bagiannya.'),
        ('Apa alat pelindung saat memotong bambu?', 'Sarung tangan', ['Cermin', 'Payung', 'Sisir'], 'Sarung tangan melindungi tangan dari serpihan tajam.', 'Kacamata juga dianjurkan.'),
        ('Apa yang dievaluasi dari produk eksterior?', 'Kekuatan, keindahan, dan fungsi', ['Nama pembuat saja', 'Warna kemasan saja', 'Harga alat saja'], 'Evaluasi menilai kekuatan, keindahan, fungsi, dan dampak.', 'Masukan dipakai untuk perbaikan.'),
        ('Apa dampak positif memakai bahan lokal?', 'Mengurangi jejak transportasi dan mendukung daerah', ['Menambah pencemaran', 'Menghilangkan lapangan kerja', 'Membuat bahan impor lebih mahal'], 'Bahan lokal mengurangi transportasi dan memberdayakan daerah.', 'Pemanfaatan harus tetap memperhatikan kelestarian.'),
    ],
    'multi': [
        ('Manakah yang termasuk aksesoris eksterior?', ['Lampu taman', 'Pot tanaman', 'Hiasan pagar'], ['Vas ruang tamu', 'Bantal sofa'], 'Lampu taman, pot, dan hiasan pagar dipakai di luar ruangan.', 'Vas dan bantal termasuk interior.'),
        ('Manakah bahan yang tahan cuaca?', ['Batu', 'Logam berlapis', 'Kayu dicat'], ['Kertas', 'Kain tipis'], 'Batu, logam berlapis, dan kayu dicat lebih tahan cuaca.', 'Kertas dan kain tipis mudah rusak.'),
        ('Bagaimana merawat produk eksterior?', ['Membersihkan secara berkala', 'Melapisi ulang pelindung'], ['Membiarkan air menggenang', 'Membiarkan lumut menutupi'], 'Pembersihan dan pelapisan ulang menjaga produk.', 'Air menggenang mempercepat kerusakan.'),
        ('Manakah prinsip keselamatan kerja?', ['Memakai sarung tangan', 'Memakai kacamata pelindung'], ['Bekerja tanpa alas', 'Membiarkan serpihan berserakan'], 'Sarung tangan dan kacamata melindungi dari cedera.', 'Alas kerja mengurangi risiko terpeleset.'),
        ('Manakah faktor nilai ekonomis?', ['Keunikan desain', 'Kualitas konstruksi'], ['Bagian tajam', 'Bahan mudah lapuk'], 'Desain unik dan konstruksi kuat meningkatkan nilai.', 'Kualitas menjaga kepercayaan pembeli.'),
        ('Manakah tahap proyek kelompok?', ['Perencanaan', 'Pembuatan', 'Evaluasi'], ['Menghindari pembagian tugas', 'Membuang bahan sembarangan'], 'Proyek melalui perencanaan, pembuatan, dan evaluasi.', 'Pembagian tugas membuat pekerjaan efisien.'),
        ('Manakah sifat bahan yang benar?', ['Bambu ringan dan lentur', 'Batu tahan lama'], ['Bambu lebih berat dari batu', 'Batu mudah larut dalam air hujan'], 'Bambu ringan dan lentur; batu tahan lama.', 'Setiap bahan punya kelebihan dan perawatan berbeda.'),
        ('Manakah ciri produk eksterior berkualitas?', ['Konstruksi stabil', 'Tidak ada bagian tajam'], ['Mudah roboh', 'Cepat berjamur'], 'Konstruksi stabil dan tidak ada bagian tajam menandakan kualitas.', 'Perawatan juga menentukan ketahanan.'),
    ],
    'pairs': [
        ('Aksesoris eksterior', 'benda penghias area luar ruangan'),
        ('Bahan lokal', 'bahan yang tersedia di daerah sekitar'),
        ('Pengawetan', 'melindungi bahan dari jamur dan serangga'),
        ('Anti karat', 'lapisan pelindung logam'),
        ('Konstruksi', 'susunan sambungan agar produk stabil'),
        ('Ramah lingkungan', 'memanfaatkan bahan sekitar tanpa pencemaran berlebih'),
        ('Evaluasi', 'menilai kekuatan, keindahan, dan fungsi'),
        ('Finishing', 'tahap akhir pelapisan produk'),
    ],
    'steps': [
        ('Urutkan alur proyek aksesoris eksterior.', ['Observasi area luar', 'Pemilihan bahan lokal', 'Perancangan konstruksi', 'Pembuatan kelompok', 'Evaluasi produk'], 'Proyek bergerak dari observasi menuju evaluasi.', 'Konstruksi dirancang sebelum pembuatan.'),
        ('Urutkan langkah mengawetkan bambu.', ['Bersihkan bambu', 'Keringkan di tempat teduh', 'Lapisi anti jamur', 'Keringkan kembali sebelum dipakai'], 'Pengawetan bambu dimulai dari pembersihan dan pengeringan.', 'Jangan menjemur langsung di bawah matahari terik.'),
        ('Urutkan langkah membuat pot kayu sederhana.', ['Ukur dan potong kayu', 'Rakit sisi pot', 'Ampelas permukaan', 'Lapisi cat atau pelitur'], 'Pot kayu dibuat dari pemotongan lalu perakitan dan finishing.', 'Ampelas sebelum melapisi agar hasil rata.'),
        ('Urutkan langkah merawat produk logam eksterior.', ['Bersihkan debu dan air', 'Periksa bagian berkarat', 'Ampelas karat', 'Lapisi cat anti karat'], 'Perawatan logam dimulai dari pembersihan lalu pelapisan ulang.', 'Karat dibersihkan sebelum dicat.'),
        ('Urutkan langkah evaluasi produk kelompok.', ['Uji kestabilan', 'Periksa keamanan', 'Nilai keindahan', 'Catat perbaikan yang diperlukan'], 'Evaluasi menguji kekuatan, keamanan, dan keindahan.', 'Hasil evaluasi menjadi dasar perbaikan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
