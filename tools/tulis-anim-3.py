"""ANIM 3 — Peluang Usaha dan Profesi di Bidang Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 3',
    'slug': 'anim-3-peluang-usaha-profesi',
    'title': 'Peluang Usaha dan Profesi di Bidang Animasi',
    'description': (
        'Memahami beragam profesi di industri animasi beserta tugasnya, '
        'membaca peluang usaha (jasa dan IP), serta mengembangkan '
        'kewirausahaan melalui technopreneurship, business model canvas, '
        'dan pitch bible.'
    ),
    'objectives': [
        'Mengidentifikasi profesi pada praproduksi, produksi, dan pascaproduksi animasi.',
        'Membedakan bisnis animasi bidang jasa dan bidang kepemilikan intelektual (IP).',
        'Menjelaskan peran technopreneur dalam industri animasi.',
        'Menyusun business model canvas dan pitch bible sederhana.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 3 Peluang Usaha dan Profesi di Bidang Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Produser', 'definition': 'Perencana anggaran dan waktu produksi, pengelola tim, serta penjaga hubungan dengan klien dan investor.'},
        {'term': 'Scriptwriter', 'definition': 'Penulis naskah: mengembangkan konsep cerita, karakter, plot, dan dialog.'},
        {'term': 'Storyboard artist', 'definition': 'Menerjemahkan naskah menjadi rangkaian gambar visual.'},
        {'term': 'Layout artist', 'definition': 'Mendesain shot frame, angle, pergerakan kamera, dan pencahayaan adegan.'},
        {'term': 'Animator', 'definition': 'Pembuat gerakan karakter dan objek melalui keyframe atau motion capture.'},
        {'term': 'Composer', 'definition': 'Pembuat musik utama, musik latar, dan efek suara animasi.'},
        {'term': 'Compositor', 'definition': 'Menggabungkan elemen-elemen animasi menjadi satu tampilan utuh.'},
        {'term': 'Technopreneur', 'definition': 'Wirausaha yang memanfaatkan teknologi untuk menjalankan bisnis.'},
        {'term': 'Business Model Canvas', 'definition': 'Kerangka sembilan elemen untuk merancang model bisnis.'},
        {'term': 'Pitch bible', 'definition': 'Dokumen presentasi berisi konsep, desain karakter, dan alur untuk menarik investor atau studio.'},
    ],
    'intro': {
        'material_title': 'Profesi dalam industri animasi',
        'title': 'Lebih dari sekadar animator',
        'paragraphs': [
            'Di mata orang awam, semua pekerja animasi disebut animator. Padahal animator hanyalah satu dari banyak profesi dengan jenjang kariernya sendiri.',
            'Pada praproduksi bekerja scriptwriter, 2D artist (storyboard artist, character designer, background artist, colorist), dan 3D artist.',
            'Pada produksi bekerja animator, key drawing, inbetweener, dan layout artist. Pada pascaproduksi bekerja composer, editor, dan compositor.',
            'Produser memegang peran penting: merencanakan anggaran, mengatur waktu, mengelola kontrak, memilih tim, dan menjaga kualitas produksi.',
        ],
        'diagram': (
            'Peta profesi berdasar alur produksi',
            'flowchart LR\n'
            '  A[Praproduksi] --> B[Scriptwriter, 2D artist, 3D artist]\n'
            '  C[Produksi] --> D[Animator, key drawing, inbetweener]\n'
            '  D --> E[Layout artist]\n'
            '  F[Pascaproduksi] --> G[Composer, editor, compositor]\n'
            '  A & C & F --> H[Produser mengatur anggaran dan tim]',
        ),
        'callout': 'Pilih profesi sesuai minat: menulis cerita, menggambar, menggerakkan karakter, atau meracik musik dan efek suara.',
        'checkpoint': (
            'Profesi yang merencanakan anggaran proyek animasi adalah…',
            [
                ('produser', True),
                ('animator', False),
                ('composer', False),
                ('colorist', False),
            ],
            'Produser mengelola anggaran, waktu, dan kontrak.',
        ),
    },
    'concept': {
        'material_title': 'Peluang usaha animasi',
        'title': 'Bisnis jasa dan bisnis IP',
        'paragraphs': [
            'Bisnis animasi bidang jasa menawarkan layanan produksi animasi kepada klien, misalnya iklan komersial, serial, atau pengembangan karakter, dan dapat dijalankan sebagai perusahaan maupun freelancer.',
            'Bisnis animasi bidang IP berfokus pada pengembangan karakter dan cerita yang dilindungi hak cipta, lalu dipasarkan lewat film, merchandise, atau game. Pendapatannya dari royalti, lisensi, dan penjualan merchandise.',
            'Technopreneurship adalah wirausaha yang memanfaatkan teknologi. Seorang technopreneur cerdas, inovatif, menyukai teknologi, dan berani mengambil risiko.',
            'Animasi menciptakan lapangan kerja, meningkatkan pemanfaatan sumber daya lokal, dan membuka peluang bisnis baru di berbagai bidang.',
        ],
        'table': [
            ['Aspek', 'Bisnis jasa', 'Bisnis IP'],
            ['Fokus', 'Layanan untuk klien', 'Karakter dan cerita sendiri'],
            ['Lindung', 'Kontrak kerja', 'Hak cipta dan lisensi'],
            ['Pendapatan', 'Pembayaran proyek', 'Royalti, merchandise, lisensi'],
            ['Investasi awal', 'Lebih kecil', 'Besar untuk membangun karakter'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-3-bisnis',
            'engine': 'mermaid',
            'title': 'Dua jalur bisnis animasi',
            'code': 'flowchart TB\n'
                    '  A[Bisnis Animasi] --> B[Bidang Jasa: iklan, serial, produksi]\n'
                    '  A --> C[Bidang IP: karakter dan cerita]\n'
                    '  B --> D[Perusahaan atau freelancer]\n'
                    '  C --> E[Royalti dan lisensi merchandise]\n'
                    '  C --> F[Hak cipta melindungi karya]',
        },
        'activity': categorize_block(
            'anim-3-klasifikasi',
            'Kelompokkan pernyataan sesuai jenis bisnis animasi.',
            [('b1', 'Bisnis jasa'), ('b2', 'Bisnis IP')],
            [
                ('i1', 'Membuat iklan komersial untuk klien', 'b1'),
                ('i2', 'Menjual merchandise karakter sendiri', 'b2'),
                ('i3', 'Menerima royalti dari lisensi', 'b2'),
                ('i4', 'Bekerja sebagai freelancer', 'b1'),
                ('i5', 'Karakter dilindungi hak cipta', 'b2'),
                ('i6', 'Membuat serial sesuai pesanan studio', 'b1'),
            ],
            'Tepat. Jasa melayani klien; IP membangun dan menjual karakter sendiri.',
            'Ingat: jasa = layanan; IP = kepemilikan karakter dan cerita.',
        ),
        'subtitle': 'BMC dan pitch bible',
        'list': [
            'Business Model Canvas memetakan sembilan elemen: segmen pasar, proposisi nilai, saluran distribusi, hubungan pelanggan, sumber pendapatan, aktivitas kunci, sumber daya kunci, mitra kunci, dan struktur biaya.',
            'Pitch bible adalah dokumen presentasi yang memperkenalkan proyek animasi kepada investor atau studio: cover page, genre dan target usia, durasi dan episode, premis, serta storylines.',
            'Target usia di pitch bible dibagi prasekolah bawah (0–3), prasekolah atas (3–5), anak-anak (6–11), dan remaja (12–15).',
            'Langkah menyusun BMC: identifikasi elemen, isi tiap elemen, evaluasi dan perbaiki, lalu implementasikan dalam bisnis.',
        ],
        'checkpoint': (
            'Bisnis animasi yang pendapatannya dari royalti dan penjualan merchandise disebut…',
            [
                ('bisnis bidang IP', True),
                ('bisnis bidang jasa', False),
                ('bisnis perdagangan', False),
                ('bisnis jasa konstruksi', False),
            ],
            'Bisnis IP mengembangkan karakter berhak cipta.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merancang bisnis animasi',
        'paragraphs': [
            'Animator Indonesia seperti Andre Surya (lighting) dan Michael Reynold Tagore (texture) membuktikan profesi animasi membuka karier internasional.',
            'Animasi dimanfaatkan di pendidikan, kesehatan, industri, keamanan, teknik, dan hiburan, sehingga peluang pasar dan usahanya sangat luas.',
            'Dalam pitch bible, premis ditulis singkat 1–2 kalimat yang menjelaskan inti cerita, karakter utama, dan konflik utamanya.',
        ],
        'scenario': scenario(
            'anim-3-skenario',
            'Studiomu ingin menarik investor',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu dan teman-teman memiliki ide serial animasi dan ingin didanai investor. Langkah pertamamu?',
                    'choices': [
                        {'text': 'Menyusun pitch bible yang menarik dan komunikatif', 'next': 'n2', 'score': 2, 'feedback': 'Pitch bible membantu investor memahami visi proyek.'},
                        {'text': 'Langsung memproduksi tanpa dokumen apa pun', 'next': 'n3', 'score': 0, 'feedback': 'Investor perlu melihat konsep yang terencana.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Apa yang perlu dijelaskan agar investor yakin?',
                    'choices': [
                        {'text': 'Genre, target usia, premis, dan target pasar produk', 'next': 'n4', 'score': 2, 'feedback': 'BMC dan pitch bible menunjukkan peluang bisnis yang jelas.'},
                        {'text': 'Hanya nama karakter tanpa gambaran cerita', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa cerita dan pasar, proyek sulit dinilai layak.'},
                    ],
                },
                {'id': 'n3', 'text': 'Investor menolak karena proyek tidak terdokumentasi dengan baik.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Investor tertarik dan proyek mendapat pendanaan.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Siapa yang merencanakan anggaran proyek animasi?', 'back': 'Produser.'},
            {'front': 'Apa tugas storyboard artist?', 'back': 'Menerjemahkan naskah menjadi rangkaian gambar visual.'},
            {'front': 'Sebutkan sembilan elemen BMC.', 'back': 'Segmen pasar, proposisi nilai, saluran, hubungan pelanggan, pendapatan, aktivitas kunci, sumber daya kunci, mitra kunci, struktur biaya.'},
            {'front': 'Apa itu pitch bible?', 'back': 'Dokumen presentasi proyek animasi untuk investor atau studio.'},
        ],
        'checkpoint': (
            'Proses pascaproduksi yang menggabungkan elemen animasi menjadi satu tampilan utuh dilakukan oleh…',
            [
                ('compositor', True),
                ('scriptwriter', False),
                ('inbetweener', False),
                ('colorist', False),
            ],
            'Compositor menyatukan elemen hasil produksi.',
        ),
        'challenge': challenge_block(
            'anim-3-tantangan',
            'Tantangan profesi dan kewirausahaan',
            90,
            [
                ('Penulis naskah animasi', 'Scriptwriter'),
                ('Pembuat gerakan karakter', 'Animator'),
                ('Pembuat musik dan efek suara', 'Composer'),
                ('Wirausaha berbasis teknologi', 'Technopreneur'),
                ('Dokumen presentasi untuk investor', 'Pitch bible'),
            ],
            'Lima istilah profesi dan kewirausahaan terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Profesi yang mengelola anggaran dan waktu produksi adalah…', 'produser', ['composer', 'colorist', 'inbetweener'], 'Produser memastikan proyek selesai tepat waktu.', 'Ia juga mengurus kontrak dan klien.'),
        ('Tugas scriptwriter adalah…', 'menulis skenario dan dialog animasi', ['membuat musik', 'menggabungkan elemen', 'mengatur pencahayaan'], 'Naskah menjadi dasar animasi.', 'Menentukan karakter, plot, dan dialog.'),
        ('Storyboard artist bertugas…', 'menerjemahkan naskah menjadi gambar visual', ['merekam suara', 'membuat anggaran', 'mengompres film'], 'Storyboard memvisualkan cerita.', 'Menjadi panduan produksi.'),
        ('Profesi pembuat gerakan karakter adalah…', 'animator', ['editor', 'produser', 'scriptwriter'], 'Animator mengubah konsep menjadi gerakan.', 'Pakai keyframe atau motion capture.'),
        ('Inbetweener bertugas membuat…', 'gerakan di antara keypose', ['lagu tema', 'poster film', 'kontrak kerja'], 'Inbetween melengkapi keypose.', 'Bekerja dengan key drawing.'),
        ('Layout artist merancang…', 'shot frame, angle, dan pergerakan kamera', ['musik latar', 'iklan media', 'harga tiket'], 'Kamera virtual direplikasi layout artist.', 'Bekerja sama dengan sutradara.'),
        ('Composer dalam animasi bertugas…', 'membuat musik dan efek suara', ['mewarnai karakter', 'menyusun adegan', 'membagi anggaran'], 'Composer bekerja sama dengan sutradara.', 'Menciptakan leitmotif karakter.'),
        ('Compositor bertugas…', 'menggabungkan elemen animasi menjadi utuh', ['menulis premis', 'membuat storyboard', 'mengatur tim'], 'Elemen digabung menjadi satu tampilan.', 'Bagian dari pascaproduksi.'),
        ('Bisnis animasi bidang jasa adalah…', 'menawarkan layanan animasi kepada klien', ['menjual merchandise', 'mengembangkan IP', 'mengelola royalti'], 'Layanan produksi, iklan, dan serial.', 'Dapat dijalankan freelancer.'),
        ('Sumber pendapatan bisnis IP berupa…', 'royalti, lisensi, dan penjualan merchandise', ['gaji bulanan klien', 'ongkos kirim', 'biaya parkir'], 'Karakter berhak cipta dipasarkan luas.', 'Film, merchandise, dan game.'),
        ('Technopreneur adalah wirausaha yang…', 'memanfaatkan teknologi dalam bisnis', ['menolak teknologi', 'hanya jualan manual', 'menghindari risiko'], 'Bisnis melibatkan teknologi secara intens.', 'Karakter: cerdas, inovatif, berani risiko.'),
        ('Business Model Canvas memetakan…', 'sembilan elemen model bisnis', ['tiga tahap produksi', 'lima warna dasar', 'empat komponen K3'], 'Dari segmen pasar hingga struktur biaya.', 'Lalu dievaluasi dan diimplementasikan.'),
        ('Pitch bible digunakan untuk…', 'memperkenalkan proyek animasi kepada investor', ['mengganti kontrak', 'mengedit film', 'mencetak poster'], 'Berisi konsep, desain karakter, dan alur.', 'Menentukan kelayakan pendanaan.'),
        ('Animator Indonesia yang berperan dalam film internasional membuktikan…', 'profesi animasi membuka karier global', ['animasi tidak laku', 'artis tidak perlu belajar', 'studio asing menutup diri'], 'Andre Surya di lighting, Tagore di texture.', 'Karya Indonesia mendunia.'),
    ],
    'multi': [
        ('Manakah profesi pada praproduksi animasi?', ['Scriptwriter', 'Storyboard artist', '2D artist'], ['Compositor', 'Editor'], 'Praproduksi menyiapkan naskah dan gambar.', 'Compositor dan editor pascaproduksi.'),
        ('Manakah profesi pada produksi animasi?', ['Animator', 'Key drawing', 'Layout artist'], ['Scriptwriter', 'Colorist'], 'Produksi membuat gerakan dan layout.', 'Naskah adalah praproduksi.'),
        ('Manakah profesi pada pascaproduksi animasi?', ['Composer', 'Editor', 'Compositor'], ['Inbetweener', 'Character designer'], 'Pascaproduksi merapikan hasil akhir.', 'Pembuat gerakan dan desain adalah produksi.'),
        ('Manakah bentuk bisnis animasi bidang jasa?', ['Iklan komersial', 'Serial pesanan', 'Produksi untuk klien'], ['Merchandise karakter', 'Royalti lisensi'], 'Jasa melayani kebutuhan klien.', 'Merchandise dan royalti ciri bisnis IP.'),
        ('Manakah ciri seorang technopreneur?', ['Cerdas dan inovatif', 'Menyukai teknologi', 'Berani mengambil risiko'], ['Menolak perubahan', 'Menghindari teknologi'], 'Technopreneur memanfaatkan teknologi.', 'Tidak menghindari inovasi.'),
        ('Manakah bidang pemanfaatan animasi?', ['Pendidikan dan kesehatan', 'Industri dan keamanan', 'Hiburan dan teknik'], ['Pertanian tradisional', 'Perbankan konvensional'], 'Animasi membantu banyak bidang.', 'Cakupan terbatas.'),
        ('Manakah bagian dari pitch bible?', ['Cover page', 'Genre dan target usia', 'Premis dan storylines'], ['Laporan keuangan', 'Daftar gaji', 'Surat izin bangunan'], 'Pitch bible berisi konsep proyek.', 'Laporan keuangan bukan isi pitch bible.'),
        ('Manakah elemen Business Model Canvas?', ['Segmen pasar', 'Proposisi nilai', 'Mitra kunci'], ['Lokasi gedung', 'Harga kursi', 'Merk komputer'], 'BMC memuat sembilan elemen inti.', 'Detail teknis tidak termasuk.'),
    ],
    'pairs': [
        ('Produser', 'mengatur anggaran dan tim'),
        ('Scriptwriter', 'menulis skenario'),
        ('Animator', 'membuat gerakan karakter'),
        ('Composer', 'musik dan efek suara'),
        ('Compositor', 'menggabungkan elemen'),
        ('Technopreneur', 'wirausaha berbasis teknologi'),
        ('BMC', 'sembilan elemen model bisnis'),
        ('Pitch bible', 'dokumen untuk investor'),
    ],
    'steps': [
        ('Urutkan alur cerita sampai tayang.', ['Naskah scriptwriter', 'Storyboard artist', 'Desain karakter', 'Animasi gerak', 'Pascaproduksi'], 'Naskah menjadi awal.', 'Pascaproduksi menutup proses.'),
        ('Urutkan langkah menyusun BMC.', ['Identifikasi elemen BMC', 'Isi tiap elemen', 'Evaluasi dan perbaiki', 'Implementasikan'], 'Mulai dari memahami sembilan elemen.', 'Implementasi menutup proses.'),
        ('Urutkan bagian pitch bible.', ['Cover page', 'Genre dan target usia', 'Durasi dan episode', 'Premis', 'Storylines'], 'Pitch bible dimulai dari sampul.', 'Storylines merinci cerita.'),
        ('Urutkan pembagian target usia penonton animasi.', ['Prasekolah bawah 0–3 tahun', 'Prasekolah atas 3–5 tahun', 'Anak-anak 6–11 tahun', 'Remaja 12–15 tahun'], 'Target usia dari termuda.', 'Remaja menutup rentang.'),
        ('Urutkan langkah membangun bisnis animasi.', ['Membaca peluang pasar', 'Menentukan jenis bisnis jasa atau IP', 'Menyusun BMC', 'Membuat pitch bible', 'Memulai produksi'], 'Bisnis berawal dari peluang.', 'Produksi menutup rangkaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)