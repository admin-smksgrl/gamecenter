"""ANIM 6 — Quality Control Produksi Animasi (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 6',
    'slug': 'anim-6-quality-control',
    'title': 'Quality Control Produksi Animasi',
    'description': (
        'Memahami pengertian dan manfaat quality control, tiga tipe metode '
        'pengendalian mutu, serta penerapannya di produksi animasi melalui '
        'manajemen produksi, key visual, Gantt chart, form revisi, dan test '
        'screening.'
    ),
    'objectives': [
        'Menjelaskan pengertian dan manfaat quality control.',
        'Membandingkan metode X-bar R chart, Taguchi, dan 100% inspection.',
        'Menerapkan quality control melalui key visual, Gantt chart, dan form revisi.',
        'Menjelaskan fungsi test screening dalam menjaga kualitas animasi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 6 Quality Control Produksi Animasi; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Quality control', 'definition': 'Proses memastikan produk dibuat sesuai standar kualitas dan meminimalisasi kesalahan.'},
        {'term': 'X-bar R chart', 'definition': 'Chart control untuk data variabel guna memeriksa kestabilan proses produksi.'},
        {'term': 'Taguchi', 'definition': 'Metode QC yang menekankan riset, desain, dan pengembangan produk untuk mengurangi cacat.'},
        {'term': '100% inspection', 'definition': 'Metode menilai seluruh bagian produk untuk menghilangkan kekurangan.'},
        {'term': 'Key visual', 'definition': 'Tema grafis yang muncul di seluruh materi iklan: warna, huruf, layout, dan elemen grafik.'},
        {'term': 'Gantt chart', 'definition': 'Perangkat perencanaan dan monitoring proyek berisi tugas, pelaksana, waktu, dan target.'},
        {'term': 'Form revisi', 'definition': 'Dokumen cetak atau digital untuk mencatat bagian yang perlu direvisi beserta rekomendasinya.'},
        {'term': 'Major revision', 'definition': 'Perbaikan mendasar dan banyak sehingga memengaruhi jadwal produksi.'},
        {'term': 'Minor revision', 'definition': 'Perbaikan kecil dan teknis yang dapat dikerjakan cepat.'},
        {'term': 'Test screening', 'definition': 'Pemutaran pratinjau sebelum rilis untuk mengukur reaksi penonton.'},
    ],
    'intro': {
        'material_title': 'Quality control dan manfaatnya',
        'title': 'Menjaga mutu di setiap tahap',
        'paragraphs': [
            'Quality control adalah proses yang dilakukan perusahaan untuk memastikan produknya berkualitas, meminimalisasi kesalahan manajemen dan staf, serta mengontrol efektivitas waktu dan efisiensi biaya.',
            'QC dapat dikembangkan untuk tingkat perusahaan, divisi, maupun produk individu agar standar kualitas tetap terjaga.',
            'Manfaat QC: membangun reputasi, membangun kepercayaan stakeholder, meningkatkan hubungan dengan konsumen, dan menciptakan otomatisasi kerja.',
        ],
        'diagram': (
            'Empat manfaat quality control',
            'flowchart TB\n'
            '  A[Quality control] --> B[Membangun reputasi]\n'
            '  A --> C[Kepercayaan stakeholder]\n'
            '  A --> D[Hubungan baik dengan konsumen]\n'
            '  A --> E[Otomatisasi dan delegasi tugas]',
        ),
        'callout': 'QC ibarat saringan: kesalahan dibuang di tahap awal agar tidak menumpuk dan menghabiskan biaya di tahap akhir.',
        'checkpoint': (
            'Quality control bertujuan untuk…',
            [
                ('memastikan produk sesuai standar kualitas', True),
                ('mempercepat produksi tanpa standar', False),
                ('menaikkan harga produk', False),
                ('mengurangi jumlah karyawan', False),
            ],
            'QC menjaga mutu dan konsistensi produk.',
        ),
    },
    'concept': {
        'material_title': 'Metode quality control',
        'title': 'X-bar R chart, Taguchi, dan 100% inspection',
        'paragraphs': [
            'X-bar R chart adalah chart control untuk data variabel. Variabel X menunjukkan produk yang diuji, variabel Y menunjukkan sejauh mana varian produk dapat diterima sehingga kecacatan acak atau sistematis dapat diketahui.',
            'Metode Taguchi menekankan peran penelitian dan pengembangan, desain produk, serta pengembangan produk untuk mengurangi cacat dan kegagalan.',
            'Metode 100% inspection menilai seluruh bagian produk untuk menghilangkan kekurangan; pada praktiknya perusahaan besar mencapai sekitar 80% yang mendekati 100%.',
            'Pemilihan metode bergantung pada jenis produk dan industrinya; industri animasi memerlukan QC agar gambar dan kualitas animasi konsisten.',
        ],
        'table': [
            ['Metode', 'Penekanan', 'Ciri khas'],
            ['X-bar R chart', 'Stabilitas proses', 'Grafik variabel X dan Y'],
            ['Taguchi', 'Riset dan desain produk', 'Mengurangi cacat sejak desain'],
            ['100% inspection', 'Pemeriksaan menyeluruh', 'Menilai semua bagian produk'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-6-metode',
            'engine': 'mermaid',
            'title': 'Tiga tipe metode quality control',
            'code': 'flowchart TB\n'
                    '  A[Quality control] --> B[X-bar R chart: kestabilan proses]\n'
                    '  A --> C[Taguchi: riset dan desain produk]\n'
                    '  A --> D[100% inspection: periksa seluruh bagian]\n'
                    '  B --> E[Deteksi cacat acak atau sistematis]',
        },
        'activity': categorize_block(
            'anim-6-klasifikasi',
            'Kelompokkan pernyataan sesuai metode quality control.',
            [('b1', 'X-bar R chart'), ('b2', 'Taguchi'), ('b3', '100% inspection')],
            [
                ('i1', 'Memakai grafik variabel X dan Y', 'b1'),
                ('i2', 'Menekankan riset dan desain produk', 'b2'),
                ('i3', 'Memeriksa seluruh bagian produk', 'b3'),
                ('i4', 'Mengetahui cacat acak atau sistematis', 'b1'),
                ('i5', 'Mengurangi cacat sejak tahap desain', 'b2'),
                ('i6', 'Menghilangkan kekurangan pada produk', 'b3'),
            ],
            'Tepat. Setiap metode punya fokus pemeriksaan yang berbeda.',
            'Ingat: chart untuk proses, Taguchi untuk desain, 100% untuk keseluruhan.',
        ),
        'subtitle': 'Penerapan pada produksi animasi',
        'list': [
            'Manajemen produksi mengawasi seluruh jadwal, menyeimbangkan kebutuhan departemen, dan menunjuk project leader.',
            'Key visual adalah tema grafis yang muncul di seluruh materi iklan, mencakup warna, huruf, layout, dan elemen grafik.',
            'Gantt chart membantu tim memahami hubungan antartugas, status shot, priority shot, dan memprediksi keterlambatan.',
            'Form revisi menghasilkan major revision (mendasar, memengaruhi jadwal) dan minor revision (kecil dan teknis).',
            'Test screening adalah pemutaran pratinjau sebelum rilis untuk mengukur reaksi penonton.',
        ],
        'checkpoint': (
            'Perangkat perencanaan dan monitoring proyek animasi disebut…',
            [
                ('Gantt chart', True),
                ('key visual', False),
                ('form revisi', False),
                ('test screening', False),
            ],
            'Gantt chart memetakan tugas, pelaksana, dan target waktu.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Mengendalikan mutu produksi',
        'paragraphs': [
            'Setiap tahap menghasilkan output: praproduksi menghasilkan naskah dan desain, produksi menghasilkan karakter dan adegan, pascaproduksi menghasilkan film utuh.',
            'Major revision sangat dihindari; sebaiknya revisi mendasar terjadi di tahap praproduksi agar tidak menghabiskan waktu dan biaya.',
            'Tanggung jawab mengisi form revisi berada pada project leader, lead animator, koordinator, bahkan pelanggan sesuai kesepakatan dengan merujuk key visual.',
        ],
        'scenario': scenario(
            'anim-6-skenario',
            'Episode jadi tetapi tidak konsisten',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Animasi proyekmu hampir selesai, tetapi banyak adegan tidak sesuai standar visual. Apa langkahmu?',
                    'choices': [
                        {'text': 'Memeriksa adegan memakai form revisi dan key visual acuan', 'next': 'n2', 'score': 2, 'feedback': 'QC dengan acuan key visual menjaga konsistensi.'},
                        {'text': 'Mengirim hasil ke klien apa adanya', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa QC, produk gagal memenuhi standar dan merusak reputasi.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Revisi apa yang perlu diprioritaskan?',
                    'choices': [
                        {'text': 'Merapikan bagian kecil dan teknis lebih dulu (minor revision)', 'next': 'n4', 'score': 2, 'feedback': 'Minor revision cepat dan tidak mengganggu jadwal.'},
                        {'text': 'Mengulang seluruh isi film dari awal', 'next': 'n3', 'score': 0, 'feedback': 'Major revision menghabiskan waktu dan biaya.'},
                    ],
                },
                {'id': 'n3', 'text': 'Klien menolak hasil; proyek harus diulang dan jadwal molor.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kualitas animasi terjaga dan proyek diterima klien.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa empat manfaat quality control?', 'back': 'Reputasi, kepercayaan stakeholder, hubungan konsumen, otomatisasi.'},
            {'front': 'Apa itu Gantt chart?', 'back': 'Perangkat perencanaan dan monitoring proyek animasi.'},
            {'front': 'Apa beda major dan minor revision?', 'back': 'Major bersifat mendasar dan memengaruhi jadwal; minor kecil dan teknis.'},
            {'front': 'Apa itu test screening?', 'back': 'Pemutaran pratinjau sebelum rilis untuk mengukur reaksi penonton.'},
        ],
        'checkpoint': (
            'Tema grafis yang muncul di seluruh materi iklan disebut…',
            [
                ('key visual', True),
                ('Gantt chart', False),
                ('form revisi', False),
                ('storyboard', False),
            ],
            'Key visual mencakup warna, huruf, layout, dan elemen grafik.',
        ),
        'challenge': challenge_block(
            'anim-6-tantangan',
            'Tantangan istilah quality control',
            90,
            [
                ('Grafik pengendalian mutu proses produksi', 'X-bar R chart'),
                ('Metode QC berfokus pada riset dan desain', 'Taguchi'),
                ('Pemeriksaan seluruh bagian produk', '100% inspection'),
                ('Perangkat monitoring jadwal proyek', 'Gantt chart'),
                ('Pemutaran pratinjau sebelum rilis', 'Test screening'),
            ],
            'Lima istilah quality control terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Quality control merupakan proses untuk…', 'memastikan produk dibuat sesuai standar kualitas', ['menaikkan harga produk', 'mempercepat distribusi', 'menambah jumlah karyawan'], 'QC meminimalisasi kesalahan.', 'Mengontrol waktu dan biaya.'),
        ('Salah satu manfaat quality control adalah…', 'membangun reputasi perusahaan', ['menambah hutang', 'mengurangi konsumen', 'menghapus merek'], 'Produk konsisten membangun reputasi.', 'Juga membangun kepercayaan stakeholder.'),
        ('Metode yang memakai grafik variabel X dan Y adalah…', 'X-bar R chart', ['Taguchi', '100% inspection', 'test screening'], 'X produk diuji, Y penerimaan varian.', 'Mendeteksi cacat acak.'),
        ('Metode QC yang menekankan riset dan desain produk adalah…', 'Taguchi', ['X-bar R chart', '100% inspection', 'form revisi'], 'Fokus mengurangi cacat sejak desain.', 'Memastikan kesesuaian spesifikasi.'),
        ('Metode yang memeriksa seluruh bagian produk disebut…', '100% inspection', ['sampling acak', 'Taguchi', 'Gantt chart'], 'Semua bagian dinilai.', 'Angka 80% mendekati 100%.'),
        ('Gantt chart berfungsi untuk…', 'perencanaan dan monitoring proyek', ['mewarnai karakter', 'membuat musik', 'mencetak tiket'], 'Menunjukkan posisi pekerjaan dan target.', 'Membantu mengalokasikan sumber daya.'),
        ('Key visual mencakup komponen…', 'warna, huruf, layout, dan elemen grafik', ['anggaran dan jadwal', 'gaji dan kontrak', 'stok dan gudang'], 'Tema grafis di seluruh materi iklan.', 'Menjadi acuan produksi.'),
        ('Major revision adalah revisi yang…', 'bersifat mendasar dan memengaruhi jadwal produksi', ['kecil dan teknis', 'hanya kosmetik', 'tidak perlu dilakukan'], 'Sebaiknya terjadi di praproduksi.', 'Mahal bila terlambat.'),
        ('Minor revision bersifat…', 'perbaikan kecil dan teknis yang cepat', ['perbaikan menyeluruh', 'penulisan ulang naskah', 'penggantian seluruh tim'], 'Contohnya perbaikan aset animasi.', 'Tidak mengganggu jadwal.'),
        ('Test screening dilakukan untuk…', 'mengukur reaksi penonton sebelum rilis', ['menghitung pajak', 'menaikkan harga', 'merekrut staf'], 'Pemutaran pratinjau film.', 'Menjaga kualitas akhir.'),
        ('Manajemen produksi bertugas…', 'mengawasi jadwal dan kebutuhan seluruh departemen', ['menggambar semua karakter', 'membuat musik', 'menjual produk'], 'Menyeimbangkan dan memprioritaskan kebutuhan.', 'Menunjuk project leader.'),
        ('Hubungan antartugas dan status shot dapat dipahami melalui…', 'Gantt chart', ['key visual', 'flashcard', 'test screening'], 'Gantt chart juga menunjukkan priority shot.', 'Memantau ketepatan waktu.'),
        ('Dokumen untuk mencatat bagian yang perlu diperbaiki disebut…', 'form revisi', ['storyboard', 'Gantt chart', 'key visual'], 'Berisi keterangan dan rekomendasi revisi.', 'Diisi project leader atau klien.'),
        ('Quality control pada animasi bertujuan agar…', 'gambar dan kualitas animasi konsisten', ['warna sesuka hati', 'jumlah episode bertambah', 'biaya naik'], 'QC menjaga konsistensi visual.', 'Menghindari kesalahan berulang.'),
    ],
    'multi': [
        ('Manakah manfaat quality control?', ['Membangun reputasi', 'Kepercayaan stakeholder', 'Hubungan baik dengan konsumen'], ['Menambah kesalahan', 'Mengurangi mutu', 'Menghapus standar'], 'QC menjaga mutu dan kepercayaan.', 'Mutu terjaga menghasilkan manfaat.'),
        ('Manakah tipe metode quality control?', ['X-bar R chart', 'Taguchi', '100% inspection'], ['Storyboard', 'Keyframe', 'Dubbing'], 'Tiga metode pengendalian mutu.', 'Lainnya istilah produksi.'),
        ('Manakah ciri X-bar R chart?', ['Untuk data variabel', 'Menguji kestabilan proses', 'Menunjukkan varian yang diterima'], ['Memeriksa seluruh produk', 'Menekankan desain', 'Membuat jadwal'], 'Chart memantau kestabilan proses.', 'Variabel X dan Y terlihat.'),
        ('Manakah perangkat manajemen produksi animasi?', ['Manajemen produksi', 'Gantt chart', 'Form revisi'], ['Kamera video', 'Mic karaoke', 'Speaker aktif'], 'Perangkat disiapkan sebelum produksi.', 'Alat-alat lain bukan manajemen.'),
        ('Manakah komponen key visual?', ['Warna dan huruf', 'Layout', 'Elemen grafik'], ['Gaji pegawai', 'Harga sewa', 'Biaya listrik'], 'Key visual berupa tema grafis.', 'Bukan komponen biaya.'),
        ('Manakah ciri major revision?', ['Bersifat mendasar', 'Banyak perbaikan', 'Memengaruhi jadwal'], ['Perbaikan kecil', 'Bisa dikerjakan cepat', 'Tidak menambah waktu'], 'Major revision berisiko waktu dan biaya.', 'Dihindari jika mungkin.'),
        ('Manakah ciri minor revision?', ['Perbaikan teknis kecil', 'Cepat dikerjakan', 'Contohnya perbaikan aset'], ['Menulis ulang naskah', 'Mengulang produksi', 'Mengganti seluruh tim'], 'Minor revision ringan.', 'Tidak merombak jadwal.'),
        ('Manakah tujuan manajemen produksi?', ['Mengawasi jadwal produksi', 'Menyeimbangkan kebutuhan departemen', 'Memprioritaskan pekerjaan'], ['Menghapus standar mutu', 'Mengabaikan tenggat', 'Menutup studio'], 'Manajemen menjaga produksi tepat waktu.', 'Prioritas pekerjaan selalu diatur.'),
    ],
    'pairs': [
        ('Quality control', 'menjaga standar kualitas'),
        ('X-bar R chart', 'grafik kestabilan proses'),
        ('Taguchi', 'riset dan desain produk'),
        ('100% inspection', 'periksa seluruh bagian'),
        ('Key visual', 'tema grafis iklan'),
        ('Gantt chart', 'monitoring jadwal proyek'),
        ('Major revision', 'perbaikan mendasar'),
        ('Test screening', 'pratinjau sebelum rilis'),
    ],
    'steps': [
        ('Urutkan penerapan QC dalam produksi animasi.', ['Menyusun manajemen produksi', 'Menetapkan key visual', 'Membuat Gantt chart', 'Mengisi form revisi', 'Melakukan test screening'], 'Manajemen disiapkan pertama.', 'Test screening menutup QC.'),
        ('Urutkan penanganan temuan QC.', ['Mencatat temuan di form revisi', 'Menentukan major atau minor', 'Merevisi aset', 'Memeriksa ulang hasil', 'Menyetujui hasil akhir'], 'Temuan dicatat dulu.', 'Persetujuan menutup proses.'),
        ('Urutkan langkah membuat Gantt chart.', ['Mendaftar tugas produksi', 'Menentukan pelaksana', 'Menentukan waktu awal', 'Menetapkan target selesai', 'Memantau progres'], 'Tugas didata dulu.', 'Progres dipantau di akhir.'),
        ('Urutkan pengembangan key visual.', ['Diskusi ide dengan konsumen', 'Menciptakan solusi kreatif', 'Presentasi desain', 'Adaptasi dan penyempurnaan', 'Kesepakatan key visual'], 'Ide berawal dari konsumen.', 'Kesepakatan menutup proses.'),
        ('Urutkan pemanfaatan hasil test screening.', ['Pemutaran pratinjau', 'Mencatat reaksi penonton', 'Menganalisis masukan', 'Memperbaiki bagian lemah', 'Merilis versi final'], 'Pratinjau menghasilkan masukan.', 'Rilis menutup rangkaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)