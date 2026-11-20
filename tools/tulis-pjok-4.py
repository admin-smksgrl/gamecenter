"""PJOK 4 — Permainan Bola Voli (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 4',
    'slug': 'pjok-4-bola-voli',
    'title': 'Permainan Bola Voli',
    'description': (
        'Mempelajari sejarah dan peraturan bola voli, teknik servis, passing, '
        'smash, dan block, serta kerja sama tim dalam menyusun serangan.'
    ),
    'objectives': [
        'Menjelaskan sejarah dan peraturan dasar permainan bola voli.',
        'Mempraktikkan teknik servis, passing bawah, passing atas, smash, dan block.',
        'Menerapkan pola serangan dan pertahanan sederhana dalam bola voli.',
        'Menunjukkan sportivitas, disiplin, dan kerja sama selama bermain.',
        'Menjaga keselamatan diri dan teman melalui pemanasan serta pendinginan.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 4 Permainan Bola Voli; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Bola voli', 'definition': 'Olahraga dua tim berisi enam pemain yang berusaha menjatuhkan bola di daerah lawan.'},
        {'term': 'Servis', 'definition': 'Pukulan pertama untuk memulai rally dari belakang garis lapangan.'},
        {'term': 'Passing bawah', 'definition': 'Menerima bola dengan kedua lengan bawah yang dirapatkan.'},
        {'term': 'Passing atas', 'definition': 'Menerima bola dengan ujung jari di atas dahi untuk menyiapkan serangan.'},
        {'term': 'Smash', 'definition': 'Memukul bola keras ke bawah di daerah lawan.'},
        {'term': 'Block', 'definition': 'Menahan bola di dekat net dengan kedua tangan terangkat.'},
        {'term': 'Libero', 'definition': 'Pemain bertahan khusus yang memakai seragam berbeda dan tidak boleh melakukan smash.'},
        {'term': 'Rally point', 'definition': 'Sistem penilaian ketika setiap rally menghasilkan satu poin.'},
    ],
    'intro': {
        'material_title': 'Mengapa bola voli menarik?',
        'title': 'Permainan tim yang menuntut koordinasi',
        'paragraphs': [
            'Bola voli adalah permainan bola besar yang dimainkan dua tim. Setiap tim berusaha menjatuhkan bola di daerah lawan melewati net. Bola boleh dimainkan paling banyak tiga sentuhan sebelum dikembalikan.',
            'William G. Morgan menciptakan bola voli pada 1895 di Amerika Serikat. Ia mencari permainan yang lebih ringan daripada bola basket. Di Indonesia, Persatuan Bola Voli Seluruh Indonesia (PBVSI) berdiri pada 22 Januari 1955.',
            'Bola voli melatih koordinasi, reaksi cepat, dan komunikasi. Setiap pemain memiliki peran khusus, mulai dari pengumpan hingga penyerang.',
        ],
        'diagram': (
            'Alur dasar permainan bola voli',
            'flowchart LR\n'
            '  A[Servis] --> B[Terima bola]\n'
            '  B --> C[Passing ke pengumpan]\n'
            '  C --> D[Umpan ke penyerang]\n'
            '  D --> E[Smash]\n'
            '  E --> F[Bertahan dan ulangi]',
        ),
        'callout': 'Potong kuku, lepas aksesori, dan periksa net serta tiang sebelum bermain agar cedera dapat dicegah.',
        'checkpoint': (
            'Siapa pencipta permainan bola voli?',
            [
                ('William G. Morgan', True),
                ('James Naismith', False),
                ('Pierre de Coubertin', False),
                ('Friedrich Ludwig Jahn', False),
            ],
            'William G. Morgan menciptakan bola voli pada 1895; James Naismith menciptakan bola basket.',
        ),
    },
    'concept': {
        'material_title': 'Peraturan dan teknik dasar',
        'title': 'Peraturan, teknik, dan taktik',
        'paragraphs': [
            'Lapangan bola voli berukuran panjang 18 meter dan lebar 9 meter. Net dipasang di tengah lapangan dengan tinggi 2,43 meter untuk putra dan 2,24 meter untuk putri. Setiap tim menurunkan enam pemain inti di lapangan.',
            'Pertandingan memakai sistem rally point. Tim yang memenangkan rally mendapat satu poin dan berhak melakukan servis berikutnya. Setiap set dimenangkan oleh tim yang lebih dulu mencapai 25 poin dengan selisih minimal dua poin.',
            'Pemain melakukan rotasi searah jarum jam setiap kali timnya memperoleh hak servis. Pelanggaran umum meliputi bola keluar, menyentuh net, memukul bola dua kali berturut-turut, dan servis yang tidak melewati net.',
        ],
        'table': [
            ['Teknik', 'Tujuan', 'Kunci gerak'],
            ['Servis', 'Memulai rally', 'Lambungkan bola, pukul dengan telapak tangan'],
            ['Passing bawah', 'Menerima servis atau smash', 'Lengan rapat, lutut lentur, bola di depan badan'],
            ['Passing atas', 'Menyiapkan serangan', 'Jari terbuka, bola di atas dahi'],
            ['Smash', 'Mencetak poin', 'Awalan, lompat, pukul bola di titik tertinggi'],
            ['Block', 'Menahan serangan lawan', 'Tangan terangkat, jari rapat, dekat net'],
        ],
        'visual': chart_block(
            'pjok-4-tinggi-net',
            'Tinggi net bola voli (meter)',
            'bar',
            [('Putra', 2.43), ('Putri', 2.24)],
        ),
        'activity': categorize_block(
            'pjok-4-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam pelanggaran atau gerak sah.',
            [('b1', 'Pelanggaran'), ('b2', 'Gerak sah')],
            [
                ('i1', 'Bola menyentuh net saat servis', 'b1'),
                ('i2', 'Pemain menyentuh net', 'b1'),
                ('i3', 'Menerima bola dengan passing bawah', 'b2'),
                ('i4', 'Melakukan smash dari area serang', 'b2'),
                ('i5', 'Memukul bola dua kali berturut-turut', 'b1'),
                ('i6', 'Melakukan block dengan kedua tangan', 'b2'),
            ],
            'Tepat. Bola menyentuh net, pemain menyentuh net, dan double touch adalah pelanggaran.',
            'Periksa lagi: passing, smash, dan block adalah gerakan sah.',
        ),
        'subtitle': 'Taktik sederhana',
        'list': [
            'Pola 4-2 memakai dua pengumpan dan empat penyerang.',
            'Pola 5-1 memakai satu pengumpan utama yang mengatur seluruh serangan.',
            'Servis diarahkan ke area kosong atau ke penerima yang lemah.',
            'Komunikasi singkat seperti “saya”, “lepas”, atau “block” mencegah tabrakan antar pemain.',
        ],
        'checkpoint': (
            'Berapa poin yang dibutuhkan untuk memenangkan satu set?',
            [
                ('25 poin dengan selisih minimal dua', True),
                ('21 poin dengan selisih minimal dua', False),
                ('15 poin tanpa selisih', False),
                ('30 poin tanpa selisih', False),
            ],
            'Satu set dimenangkan dengan 25 poin dan selisih minimal dua poin.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bermain dengan sportif',
        'paragraphs': [
            'Permainan sesungguhnya menguji keputusan, bukan hanya teknik. Pemain harus membaca posisi rekan dan lawan, lalu memilih antara mengoper, menyerang, atau bertahan. Keputusan yang tergesa-gesa sering menghasilkan kesalahan sendiri.',
            'Sportivitas tampak ketika pemain mengakui bola menyentuh lantai, membantu lawan yang jatuh, dan menghormati keputusan wasit. Kerja sama dibangun melalui komunikasi dan pembagian peran yang jelas.',
            'Gunakan permainan kecil tiga lawan tiga untuk melatih passing, pergerakan tanpa bola, dan pertahanan. Hentikan permainan sesaat untuk membahas keputusan yang tepat.',
        ],
        'scenario': scenario(
            'pjok-4-skenario',
            'Keputusan di set penentuan',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Timmu tertinggal satu poin di set penentuan. Servis lawan datang ke arahmu. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Menerima dengan passing bawah lalu mengarahkan ke pengumpan', 'next': 'n2', 'score': 2, 'feedback': 'Penerimaan terkendali membuka peluang serangan.'},
                        {'text': 'Memukul bola langsung ke daerah lawan', 'next': 'n3', 'score': 0, 'feedback': 'Bola servis sulit diserang langsung dengan aman.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Pengumpan memberi umpan tinggi ke arahmu. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Melakukan smash ke area kosong', 'next': 'n4', 'score': 2, 'feedback': 'Smash ke area kosong menyulitkan pertahanan lawan.'},
                        {'text': 'Mengembalikan bola pelan ke tengah lawan', 'next': 'n3', 'score': 0, 'feedback': 'Bola lambat mudah dibaca dan dipertahankan.'},
                    ],
                },
                {'id': 'n3', 'text': 'Peluang habis karena keputusan diambil tergesa-gesa.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tim mencetak poin dan bermain sebagai satu kesatuan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu libero?', 'back': 'Pemain bertahan khusus dengan seragam berbeda yang tidak boleh melakukan smash.'},
            {'front': 'Berapa tinggi net putra?', 'back': '2,43 meter.'},
            {'front': 'Berapa jumlah pemain inti?', 'back': '6 pemain.'},
            {'front': 'Apa itu rally point?', 'back': 'Sistem ketika setiap rally menghasilkan satu poin.'},
        ],
        'checkpoint': (
            'Saat bola servis datang rendah, teknik yang paling tepat adalah…',
            [
                ('Passing bawah dengan lengan rapat', True),
                ('Smash langsung dari belakang', False),
                ('Block di dekat net', False),
                ('Servis ulang', False),
            ],
            'Passing bawah adalah cara paling aman menerima bola rendah.',
        ),
        'challenge': challenge_block(
            'pjok-4-tantangan',
            'Tantangan istilah bola voli',
            90,
            [
                ('Pencipta bola voli', 'William G. Morgan'),
                ('Jumlah pemain inti', '6'),
                ('Tinggi net putra', '2,43 m'),
                ('Poin untuk memenangkan set', '25'),
                ('Pemain bertahan khusus', 'libero'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Siapa pencipta permainan bola voli?', 'William G. Morgan', ['James Naismith', 'Michael Jordan', 'Pierre de Coubertin'], 'William G. Morgan menciptakan bola voli pada 1895.', 'James Naismith menciptakan bola basket.'),
        ('Berapa jumlah pemain inti setiap tim bola voli?', '6 pemain', ['5 pemain', '7 pemain', '11 pemain'], 'Setiap tim menurunkan enam pemain inti.', 'Bandingkan dengan bola basket yang lima pemain.'),
        ('Apa induk organisasi bola voli Indonesia?', 'PBVSI', ['PSSI', 'PERBASI', 'PBSI'], 'PBVSI adalah Persatuan Bola Voli Seluruh Indonesia.', 'Bandingkan dengan PSSI untuk sepak bola.'),
        ('Berapa tinggi net bola voli putra?', '2,43 meter', ['2,24 meter', '2,50 meter', '2,30 meter'], 'Net putra dipasang setinggi 2,43 meter.', 'Net putri lebih rendah, yaitu 2,24 meter.'),
        ('Berapa tinggi net bola voli putri?', '2,24 meter', ['2,43 meter', '2,10 meter', '2,30 meter'], 'Net putri dipasang setinggi 2,24 meter.', 'Selisihnya sekitar 19 cm dari net putra.'),
        ('Apa nama pukulan pertama untuk memulai rally?', 'Servis', ['Smash', 'Block', 'Passing'], 'Servis memulai rally dari belakang garis lapangan.', 'Servis dilakukan oleh pemain belakang kanan.'),
        ('Apa nama teknik menerima bola dengan lengan bawah?', 'Passing bawah', ['Passing atas', 'Smash', 'Block'], 'Passing bawah memakai kedua lengan bawah yang dirapatkan.', 'Teknik ini sering dipakai menerima servis.'),
        ('Berapa ukuran lapangan bola voli?', '18 m × 9 m', ['28 m × 15 m', '40 m × 20 m', '20 m × 10 m'], 'Lapangan bola voli berukuran 18 meter × 9 meter.', 'Net berada di tengah lapangan.'),
        ('Berapa sentuhan maksimal sebelum bola dikembalikan?', '3 sentuhan', ['2 sentuhan', '4 sentuhan', '5 sentuhan'], 'Setiap tim boleh menyentuh bola paling banyak tiga kali.', 'Block tidak dihitung sebagai sentuhan pertama dalam beberapa aturan.'),
        ('Apa nama pemain bertahan khusus dalam bola voli?', 'Libero', ['Setter', 'Spiker', 'Blocker'], 'Libero adalah pemain bertahan khusus dengan seragam berbeda.', 'Libero tidak boleh melakukan smash.'),
        ('Ke arah mana pemain melakukan rotasi?', 'Searah jarum jam', ['Berlawanan jarum jam', 'Acak', 'Tidak ada rotasi'], 'Rotasi dilakukan searah jarum jam saat tim memperoleh hak servis.', 'Pemain berpindah satu posisi.'),
        ('Apa nama teknik menahan bola di dekat net?', 'Block', ['Smash', 'Servis', 'Passing'], 'Block dilakukan dengan kedua tangan terangkat di dekat net.', 'Block bertujuan menahan serangan lawan.'),
        ('Berapa jumlah poin untuk memenangkan satu set?', '25 poin', ['21 poin', '15 poin', '30 poin'], 'Satu set dimenangkan dengan 25 poin dan selisih minimal dua.', 'Jika imbang 24-24, set dilanjutkan sampai selisih dua.'),
        ('Apa istilah memukul bola keras ke bawah di daerah lawan?', 'Smash', ['Servis', 'Block', 'Passing'], 'Smash adalah pukulan keras ke bawah untuk mencetak poin.', 'Smash biasanya dilakukan setelah umpan pengumpan.'),
    ],
    'multi': [
        ('Manakah yang termasuk teknik dasar bola voli?', ['Servis', 'Passing', 'Smash'], ['Dribbling', 'Heading'], 'Servis, passing, dan smash adalah teknik dasar bola voli.', 'Dribbling dan heading bukan istilah bola voli.'),
        ('Manakah yang termasuk pelanggaran dalam bola voli?', ['Menyentuh net', 'Memukul bola dua kali berturut-turut'], ['Passing bawah', 'Block dengan dua tangan'], 'Menyentuh net dan double touch adalah pelanggaran.', 'Passing dan block adalah gerakan sah.'),
        ('Apa tujuan melakukan servis?', ['Memulai rally', 'Menyulitkan penerimaan lawan'], ['Mencetak gol langsung', 'Menghentikan waktu'], 'Servis memulai rally dan dapat menyulitkan lawan.', 'Poin tetap dihitung per rally.'),
        ('Manakah ciri passing bawah yang benar?', ['Lengan rapat dan lurus', 'Lutut lentur'], ['Bola dipukul dengan telapak tangan', 'Badan berdiri kaku'], 'Passing bawah memakai lengan rapat dengan lutut lentur.', 'Bola diarahkan ke pengumpan.'),
        ('Manakah yang termasuk peran pemain dalam bola voli?', ['Pengumpan', 'Penyerang', 'Libero'], ['Penjaga gawang', 'Striker'], 'Pengumpan, penyerang, dan libero adalah peran dalam bola voli.', 'Penjaga gawang dan striker bukan istilah bola voli.'),
        ('Manakah tugas pengumpan?', ['Mengatur tempo serangan', 'Memberi umpan kepada penyerang'], ['Mencetak gol ke gawang', 'Menjaga gawang'], 'Pengumpan mengatur tempo dan memberi umpan kepada penyerang.', 'Pengumpan berada di dekat net.'),
        ('Manakah pola permainan bola voli yang umum?', ['4-2', '5-1'], ['4-4-2', '3-5-2'], '4-2 dan 5-1 adalah pola bola voli.', '4-4-2 dan 3-5-2 adalah formasi sepak bola.'),
        ('Manakah pernyataan yang benar tentang libero?', ['Memakai seragam berbeda', 'Tidak boleh melakukan smash'], ['Boleh melakukan servis di semua posisi', 'Harus selalu berada di depan net'], 'Libero memakai seragam berbeda dan tidak boleh melakukan smash.', 'Libero berperan utama dalam pertahanan.'),
    ],
    'pairs': [
        ('Servis', 'pukulan pertama memulai rally'),
        ('Passing bawah', 'menerima bola dengan lengan bawah'),
        ('Passing atas', 'menerima bola dengan ujung jari'),
        ('Smash', 'memukul bola keras ke daerah lawan'),
        ('Block', 'menahan bola di dekat net'),
        ('Libero', 'pemain bertahan khusus'),
        ('Rally point', 'setiap rally menghasilkan satu poin'),
        ('Rotasi', 'pergeseran posisi searah jarum jam'),
    ],
    'steps': [
        ('Urutkan langkah melakukan servis bawah.', ['Berdiri di belakang garis', 'Pegang bola di depan badan', 'Ayunkan tangan ke belakang', 'Pukul bola dengan telapak tangan'], 'Servis bawah dimulai dari posisi berdiri lalu ayunan tangan.', 'Arahkan bola melewati net ke daerah lawan.'),
        ('Urutkan langkah melakukan passing bawah.', ['Rapatkan kedua lengan', 'Tekuk lutut', 'Arahkan bola ke lengan bawah', 'Dorong bola ke pengumpan'], 'Passing bawah memakai lengan rapat dan dorongan dari lutut.', 'Jangan mengayun lengan terlalu jauh.'),
        ('Urutkan fase melakukan smash.', ['Ambil awalan beberapa langkah', 'Tolak dengan kedua kaki', 'Angkat tangan memukul', 'Pukul bola di titik tertinggi'], 'Smash membutuhkan awalan, tolakan, dan pukulan di titik tertinggi.', 'Perhatikan timing dengan umpan pengumpan.'),
        ('Urutkan langkah melakukan block.', ['Berdiri dekat net', 'Tekuk lutut', 'Lompat dengan kedua tangan terangkat', 'Rapatkan jari menahan bola'], 'Block dilakukan dengan lompatan dan tangan terangkat di dekat net.', 'Jangan menyentuh net saat melakukan block.'),
        ('Urutkan alur serangan dalam bola voli.', ['Terima servis', 'Passing ke pengumpan', 'Umpan ke penyerang', 'Smash ke daerah lawan'], 'Serangan bergerak dari penerimaan menuju smash.', 'Tiga sentuhan dipakai untuk menyiapkan serangan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
