"""PJOK 5 — Permainan Bulu Tangkis (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 5',
    'slug': 'pjok-5-bulu-tangkis',
    'title': 'Permainan Bulu Tangkis',
    'description': (
        'Mempelajari sejarah dan peraturan bulu tangkis, teknik pegangan raket, '
        'servis, forehand, backhand, smash, dan dropshot, serta taktik bermain.'
    ),
    'objectives': [
        'Menjelaskan sejarah dan peraturan dasar permainan bulu tangkis.',
        'Mempraktikkan pegangan raket, servis, forehand, backhand, smash, dan dropshot.',
        'Menerapkan taktik penempatan bola dan pergerakan kaki dalam permainan.',
        'Menunjukkan sportivitas, disiplin, dan kerja sama selama bermain.',
        'Menjaga keselamatan diri dan teman melalui pemanasan serta pendinginan.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 5 Permainan Bulu Tangkis; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Bulu tangkis', 'definition': 'Olahraga raket yang memukul shuttlecock melewati net ke daerah lawan.'},
        {'term': 'Shuttlecock', 'definition': 'Bola bulu tangkis berbentuk kerucut dengan bulu di bagian atas.'},
        {'term': 'Servis', 'definition': 'Pukulan pertama untuk memulai rally.'},
        {'term': 'Forehand', 'definition': 'Pukulan dengan sisi raket yang searah telapak tangan.'},
        {'term': 'Backhand', 'definition': 'Pukulan dengan sisi raket yang membelakangi telapak tangan.'},
        {'term': 'Smash', 'definition': 'Pukulan keras dan menukik ke bawah untuk menyerang.'},
        {'term': 'Dropshot', 'definition': 'Pukulan pelan yang menjatuhkan shuttlecock dekat net.'},
        {'term': 'Deuce', 'definition': 'Keadaan skor imbang 20-20 yang membuat permainan dilanjutkan hingga selisih dua poin.'},
    ],
    'intro': {
        'material_title': 'Mengapa bulu tangkis digemari?',
        'title': 'Permainan raket yang cepat',
        'paragraphs': [
            'Bulu tangkis adalah permainan raket yang dimainkan dua pemain (tunggal) atau dua pasangan (ganda). Setiap pihak berusaha menjatuhkan shuttlecock di daerah lawan melewati net. Permainan ini menuntut kelincahan, kecepatan reaksi, dan ketepatan penempatan.',
            'Permainan ini berkembang dari India dan Inggris. Di Indonesia, Persatuan Bulu Tangkis Seluruh Indonesia (PBSI) berdiri pada 5 Mei 1951. Indonesia dikenal sebagai salah satu negara kuat dalam bulu tangkis dunia.',
            'Bulu tangkis melatih kebugaran, konsentrasi, dan pengendalian diri. Pemain harus membaca arah shuttlecock dan posisi lawan sebelum memilih pukulan.',
        ],
        'diagram': (
            'Alur dasar permainan bulu tangkis',
            'flowchart LR\n'
            '  A[Servis] --> B[Terima shuttlecock]\n'
            '  B --> C[Pukul ke area lawan]\n'
            '  C --> D[Lawan mengembalikan]\n'
            '  D --> E[Cari peluang smash]\n'
            '  E --> F[Menang rally]',
        ),
        'callout': 'Lakukan pemanasan pergelangan tangan dan kaki, gunakan raket yang sesuai, serta periksa lantai agar tidak licin.',
        'checkpoint': (
            'Apa induk organisasi bulu tangkis Indonesia?',
            [
                ('PBSI', True),
                ('PSSI', False),
                ('PBVSI', False),
                ('PERBASI', False),
            ],
            'PBSI adalah Persatuan Bulu Tangkis Seluruh Indonesia.',
        ),
    },
    'concept': {
        'material_title': 'Peraturan dan teknik dasar',
        'title': 'Peraturan, teknik, dan taktik',
        'paragraphs': [
            'Lapangan bulu tangkis berukuran panjang 13,40 meter. Untuk permainan ganda lebarnya 6,10 meter, sedangkan untuk tunggal 5,18 meter. Net dipasang setinggi 1,55 meter di bagian tengah.',
            'Pertandingan memakai sistem rally point dengan target 21 poin. Pemain atau pasangan yang memenangkan dua game lebih dulu menjadi pemenang. Jika skor 20-20, permainan dilanjutkan hingga selisih dua poin, dengan batas 30 poin.',
            'Servis dilakukan secara diagonal ke area servis lawan. Saat memukul servis, shuttlecock harus berada di bawah pinggang. Pelanggaran umum meliputi shuttlecock keluar lapangan, menyentuh net, dan servis yang tidak melewati net.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Pegangan forehand', 'Pukulan dari sisi kanan', 'Raket dipegang seperti berjabat tangan'],
            ['Pegangan backhand', 'Pukulan dari sisi kiri', 'Ibu jari menempel di sisi raket'],
            ['Servis', 'Memulai rally', 'Shuttlecock di bawah pinggang, ayunan terkendali'],
            ['Smash', 'Menyerang', 'Lompat, raket di atas kepala, pukul menukik'],
            ['Dropshot', 'Mengubah tempo', 'Pukulan pelan, shuttlecock jatuh dekat net'],
        ],
        'visual': chart_block(
            'pjok-5-ukuran-lapangan',
            'Ukuran penting lapangan bulu tangkis (meter)',
            'bar',
            [('Panjang', 13.4), ('Lebar ganda', 6.1), ('Lebar tunggal', 5.18), ('Tinggi net', 1.55)],
        ),
        'activity': categorize_block(
            'pjok-5-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pelanggaran atau gerak sah.',
            [('b1', 'Pelanggaran'), ('b2', 'Gerak sah')],
            [
                ('i1', 'Shuttlecock jatuh di luar garis lapangan', 'b1'),
                ('i2', 'Raket menyentuh net saat memukul', 'b1'),
                ('i3', 'Servis diagonal ke area lawan', 'b2'),
                ('i4', 'Smash dari belakang lapangan', 'b2'),
                ('i5', 'Shuttlecock menyangkut di net', 'b1'),
                ('i6', 'Dropshot ke dekat net', 'b2'),
            ],
            'Tepat. Shuttlecock keluar, raket menyentuh net, dan shuttlecock menyangkut adalah pelanggaran.',
            'Periksa lagi: servis, smash, dan dropshot adalah gerakan sah.',
        ),
        'subtitle': 'Taktik sederhana',
        'list': [
            'Pukulan lob tinggi memberi waktu untuk kembali ke posisi tengah.',
            'Dropshot menarik lawan ke depan net, lalu smash diarahkan ke belakang.',
            'Permainan ganda memakai pola depan-belakang atau samping-samping.',
            'Komunikasi singkat seperti “saya”, “kamu”, atau “lepas” mencegah tabrakan antar pemain.',
        ],
        'checkpoint': (
            'Berapa target poin untuk memenangkan satu game?',
            [
                ('21 poin', True),
                ('15 poin', False),
                ('25 poin', False),
                ('11 poin', False),
            ],
            'Satu game dimenangkan dengan 21 poin, kecuali terjadi deuce.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bermain dengan sportif',
        'paragraphs': [
            'Permainan sesungguhnya menguji keputusan, bukan hanya teknik. Pemain harus membaca arah shuttlecock dan posisi lawan, lalu memilih antara smash, dropshot, atau lob. Keputusan yang tergesa-gesa sering menghasilkan kesalahan sendiri.',
            'Sportivitas tampak ketika pemain mengakui shuttlecock jatuh di dalam garis, membantu lawan yang terjatuh, dan menghormati keputusan wasit. Kerja sama dibangun melalui komunikasi dan pembagian area yang jelas.',
            'Gunakan latihan berpasangan untuk melatih servis, lob, dan dropshot. Hentikan latihan sesaat untuk membahas penempatan yang tepat.',
        ],
        'scenario': scenario(
            'pjok-5-skenario',
            'Keputusan di poin kritis',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Skor 20-20 dan lawan mengirim lob tinggi ke belakang. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Memukul smash ke area kosong', 'next': 'n2', 'score': 2, 'feedback': 'Smash ke area kosong menyulitkan pertahanan lawan.'},
                        {'text': 'Memukul pelan ke tengah lapangan', 'next': 'n3', 'score': 0, 'feedback': 'Pukulan lambat mudah diserang balik.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Lawan berhasil mengembalikan smash ke depan net. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Melakukan netting terkendali', 'next': 'n4', 'score': 2, 'feedback': 'Netting terkendali menjaga rally tetap dalam kendali.'},
                        {'text': 'Memukul sekuat tenaga dari posisi sulit', 'next': 'n3', 'score': 0, 'feedback': 'Pukulan keras dari posisi sulit mudah keluar.'},
                    ],
                },
                {'id': 'n3', 'text': 'Poin hilang karena keputusan diambil tergesa-gesa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kamu menutup rally dan bermain dengan tenang.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu dropshot?', 'back': 'Pukulan pelan yang menjatuhkan shuttlecock dekat net.'},
            {'front': 'Berapa tinggi net di tengah?', 'back': '1,55 meter.'},
            {'front': 'Berapa poin untuk memenangkan game?', 'back': '21 poin.'},
            {'front': 'Apa itu deuce?', 'back': 'Skor 20-20 yang membuat permainan dilanjutkan hingga selisih dua poin.'},
        ],
        'checkpoint': (
            'Saat lawan berada di belakang lapangan, pukulan paling tepat adalah…',
            [
                ('Dropshot ke dekat net', True),
                ('Lob tinggi ke belakang', False),
                ('Smash ke arah lawan', False),
                ('Servis ulang', False),
            ],
            'Dropshot memaksa lawan bergerak jauh ke depan net.',
        ),
        'challenge': challenge_block(
            'pjok-5-tantangan',
            'Tantangan istilah bulu tangkis',
            90,
            [
                ('Induk organisasi bulu tangkis Indonesia', 'PBSI'),
                ('Poin untuk memenangkan game', '21'),
                ('Tinggi net di tengah', '1,55 m'),
                ('Pukulan keras menukik', 'smash'),
                ('Pukulan pelan dekat net', 'dropshot'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa induk organisasi bulu tangkis Indonesia?', 'PBSI', ['PSSI', 'PERBASI', 'PBVSI'], 'PBSI adalah Persatuan Bulu Tangkis Seluruh Indonesia.', 'Bandingkan dengan PSSI untuk sepak bola.'),
        ('Berapa poin yang dibutuhkan untuk memenangkan satu game?', '21 poin', ['15 poin', '25 poin', '11 poin'], 'Satu game dimenangkan dengan 21 poin.', 'Jika 20-20, permainan dilanjutkan hingga selisih dua.'),
        ('Berapa tinggi net bulu tangkis di bagian tengah?', '1,55 meter', ['1,52 meter', '1,60 meter', '2,43 meter'], 'Net dipasang setinggi 1,55 meter di tengah.', 'Tinggi di pinggir sedikit berbeda.'),
        ('Berapa panjang lapangan bulu tangkis?', '13,40 meter', ['12,00 meter', '14,00 meter', '18,00 meter'], 'Lapangan bulu tangkis panjangnya 13,40 meter.', 'Lebar ganda 6,10 meter.'),
        ('Berapa lebar lapangan bulu tangkis untuk permainan tunggal?', '5,18 meter', ['6,10 meter', '4,50 meter', '5,50 meter'], 'Lapangan tunggal lebarnya 5,18 meter.', 'Ganda memakai lebar 6,10 meter.'),
        ('Apa nama bola bulu tangkis?', 'Shuttlecock', ['Raket', 'Net', 'Bola kasti'], 'Shuttlecock berbentuk kerucut dengan bulu di bagian atas.', 'Bentuknya membuat gerakannya melambat saat melayang.'),
        ('Apa nama pukulan pertama untuk memulai rally?', 'Servis', ['Smash', 'Dropshot', 'Lob'], 'Servis memulai rally dan dilakukan secara diagonal.', 'Shuttlecock harus berada di bawah pinggang saat dipukul.'),
        ('Apa nama pukulan keras dan menukik ke bawah?', 'Smash', ['Lob', 'Dropshot', 'Netting'], 'Smash adalah pukulan keras dan menukik untuk menyerang.', 'Smash biasanya dilakukan sambil melompat.'),
        ('Apa nama pukulan pelan yang jatuh dekat net?', 'Dropshot', ['Smash', 'Lob', 'Servis'], 'Dropshot menjatuhkan shuttlecock dekat net.', 'Pukulan ini mengubah tempo permainan.'),
        ('Berapa skor yang memicu deuce?', '20-20', ['19-19', '21-21', '18-18'], 'Deuce terjadi saat skor 20-20.', 'Setelah deuce, pemenang harus unggul dua poin.'),
        ('Apa batas maksimal poin dalam satu game saat deuce?', '30 poin', ['25 poin', '29 poin', '35 poin'], 'Permainan dihentikan pada 30 poin bila selisih dua belum tercapai.', 'Pemain yang mencapai 30 poin menang.'),
        ('Ke area mana servis harus diarahkan?', 'Area servis lawan secara diagonal', ['Area tengah lapangan', 'Area belakang sendiri', 'Bebas ke mana saja'], 'Servis harus melewati net dan masuk area servis lawan secara diagonal.', 'Perhatikan garis area servis.'),
        ('Apa nama pegangan raket yang searah telapak tangan?', 'Forehand', ['Backhand', 'Servis', 'Smash'], 'Pegangan forehand memakai sisi raket yang searah telapak tangan.', 'Pegangan ini dipakai untuk pukulan dari sisi kanan.'),
        ('Apa nama pukulan tinggi untuk memberi waktu kembali ke posisi?', 'Lob', ['Smash', 'Dropshot', 'Netting'], 'Lob adalah pukulan tinggi ke belakang lapangan lawan.', 'Pukulan ini memberi waktu untuk kembali ke tengah.'),
    ],
    'multi': [
        ('Manakah yang termasuk teknik dasar bulu tangkis?', ['Servis', 'Forehand', 'Backhand'], ['Dribbling', 'Heading'], 'Servis, forehand, dan backhand adalah teknik dasar bulu tangkis.', 'Dribbling dan heading bukan istilah bulu tangkis.'),
        ('Manakah yang termasuk pelanggaran dalam bulu tangkis?', ['Shuttlecock keluar lapangan', 'Raket menyentuh net'], ['Servis diagonal', 'Smash dari belakang'], 'Shuttlecock keluar dan raket menyentuh net adalah pelanggaran.', 'Servis diagonal dan smash adalah gerakan sah.'),
        ('Apa tujuan melakukan dropshot?', ['Menarik lawan ke depan net', 'Mengubah tempo permainan'], ['Mencetak poin langsung dari belakang', 'Menghentikan waktu'], 'Dropshot menarik lawan ke depan dan mengubah tempo.', 'Pukulan ini tidak selalu langsung mematikan.'),
        ('Manakah ciri servis yang benar?', ['Shuttlecock dipukul di bawah pinggang', 'Arah servis diagonal ke area lawan'], ['Shuttlecock dipukul di atas kepala', 'Servis diarahkan ke area sendiri'], 'Servis dilakukan di bawah pinggang dan diagonal ke area lawan.', 'Perhatikan garis servis.'),
        ('Manakah yang termasuk jenis pukulan bulu tangkis?', ['Lob', 'Smash', 'Dropshot'], ['Jump shot', 'Lay-up'], 'Lob, smash, dan dropshot adalah pukulan bulu tangkis.', 'Jump shot dan lay-up bukan istilah bulu tangkis.'),
        ('Manakah tugas pemain depan dalam ganda?', ['Menutup area net', 'Mencari bola pendek'], ['Menjaga gawang', 'Melakukan servis dari belakang terus-menerus'], 'Pemain depan menutup area net dan bola pendek.', 'Pemain belakang mengatur serangan.'),
        ('Manakah pola permainan ganda yang umum?', ['Depan-belakang', 'Samping-samping'], ['4-4-2', '5-1'], 'Depan-belakang dan samping-samping adalah pola ganda bulu tangkis.', '4-4-2 dan 5-1 bukan pola bulu tangkis.'),
        ('Manakah pernyataan yang benar tentang deuce?', ['Terjadi saat skor 20-20', 'Pemenang harus unggul dua poin'], ['Terjadi saat skor 15-15', 'Pemenang ditentukan satu poin'], 'Deuce terjadi pada 20-20 dan pemenang harus unggul dua poin.', 'Batas akhirnya 30 poin.'),
    ],
    'pairs': [
        ('Servis', 'pukulan pertama memulai rally'),
        ('Forehand', 'pukulan dengan sisi raket searah telapak tangan'),
        ('Backhand', 'pukulan dengan sisi raket membelakangi telapak tangan'),
        ('Smash', 'pukulan keras menukik ke bawah'),
        ('Dropshot', 'pukulan pelan dekat net'),
        ('Lob', 'pukulan tinggi ke belakang lapangan'),
        ('Deuce', 'skor 20-20'),
        ('Shuttlecock', 'bola bulu tangkis'),
    ],
    'steps': [
        ('Urutkan langkah melakukan servis forehand.', ['Berdiri di area servis', 'Pegang shuttlecock di depan badan', 'Ayunkan raket dari belakang', 'Pukul shuttlecock di bawah pinggang'], 'Servis forehand dimulai dari posisi berdiri lalu ayunan raket.', 'Arahkan shuttlecock diagonal melewati net.'),
        ('Urutkan langkah melakukan smash.', ['Ambil posisi di belakang shuttlecock', 'Lompat dan angkat raket', 'Pukul shuttlecock di titik tertinggi', 'Arahkan menukik ke area lawan'], 'Smash membutuhkan posisi, lompatan, dan pukulan menukik.', 'Perhatikan timing lompatan.'),
        ('Urutkan fase melakukan dropshot.', ['Ambil posisi seperti akan smash', 'Turunkan kecepatan ayunan', 'Pukul shuttlecock dengan lembut', 'Arahkan jatuh dekat net'], 'Dropshot meniru gerakan smash tetapi dengan tenaga kecil.', 'Gerakan awal yang sama mengecoh lawan.'),
        ('Urutkan langkah kembali ke posisi tengah setelah pukulan.', ['Selesaikan pukulan', 'Langkah kaki ke arah tengah', 'Siapkan raket di depan badan', 'Pantau arah shuttlecock lawan'], 'Setelah memukul, pemain harus segera kembali ke posisi siap.', 'Posisi tengah memudahkan menjangkau bola ke segala arah.'),
        ('Urutkan alur rally dari servis sampai poin.', ['Servis melewati net', 'Lawan mengembalikan', 'Cari bola tinggi', 'Lakukan smash', 'Shuttlecock jatuh di area lawan'], 'Rally bergerak dari servis menuju penyelesaian poin.', 'Setiap pukulan membuka peluang berikutnya.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
