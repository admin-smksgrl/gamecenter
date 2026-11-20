"""ANIM 10 — Cerita secara Visual (Fase E, SMK)."""
from animasi_common import (
    categorize_block,
    challenge_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'ANIM 10',
    'slug': 'anim-10-cerita-visual',
    'title': 'Cerita secara Visual',
    'description': (
        'Membangun unsur cerita film animasi, menyusun shot, scene, dan '
        'sequence, menulis sinopsis serta skenario, membuat storyboard, dan '
        'menyiapkan pre-visualisasi (animatic).'
    ),
    'objectives': [
        'Menentukan premise, logline, dan unsur cerita film animasi.',
        'Membedakan shot, scene, dan sequence beserta angle kamera.',
        'Menulis sinopsis tiga babak dan skenario animasi.',
        'Membuat storyboard dan animatic sebagai produk akhir praproduksi.',
    ],
    'minutes': 180,
    'source': (
        'Dasar-Animasi-BS-KLS-X.pdf Bab 10 Cerita secara Visual; '
        'CP Fase E Mata Pelajaran Dasar-Dasar Animasi'
    ),
    'glossary': [
        {'term': 'Premise', 'definition': 'Ide atau gagasan utama yang melatarbelakangi penulisan cerita.'},
        {'term': 'Logline', 'definition': 'Satu kalimat yang menjelaskan peristiwa utama dalam cerita.'},
        {'term': 'Shot', 'definition': 'Bagian terkecil adegan berupa satu pengambilan gambar.'},
        {'term': 'Scene', 'definition': 'Satu atau gabungan beberapa shot.'},
        {'term': 'Sequence', 'definition': 'Gabungan beberapa scene membentuk rangkaian cerita.'},
        {'term': 'Close up', 'definition': 'Angle kamera untuk menunjukkan ekspresi karakter dalam dialog.'},
        {'term': 'Sinopsis', 'definition': 'Uraian isi cerita berisi penokohan dan latar dengan alur dramatis, tiga paragraf.'},
        {'term': 'Skenario', 'definition': 'Naskah cerita berurutan per adegan memuat keterangan, setting, waktu, dan dialog.'},
        {'term': 'Storyboard', 'definition': 'Gambar dalam panel hasil visualisasi skenario menjadi urutan adegan.'},
        {'term': 'Animatic', 'definition': 'Prototipe hasil akhir praproduksi untuk mengukur durasi secara realtime.'},
    ],
    'intro': {
        'material_title': 'Unsur-unsur cerita',
        'title': 'Dari premise menjadi logline',
        'paragraphs': [
            'Cerita adalah rangkaian kejadian yang dibuat scriptwriter untuk menciptakan konflik antartokoh atau dalam diri tokoh.',
            'Premise adalah ide utama cerita; setelah itu disusun dramatic premise atau logline, yaitu satu kalimat yang menjelaskan peristiwa dalam cerita.',
            'Sumber ide cerita sangat beragam: buku, alam, kehidupan sehari-hari, kejadian alam, cerita sejarah, sains, musik, hubungan keluarga, permainan anak, kearifan lokal, dan cerita rakyat.',
            'Unsur cerita animasi meliputi premise, alur atau plot, tokoh/karakter, latar/setting, gaya/style, dan pesan yang ingin disampaikan.',
        ],
        'diagram': (
            'Sumber ide cerita animasi',
            'flowchart TB\n'
            '  A[Sumber ide] --> B[Buku dan cerita rakyat]\n'
            '  A --> C[Alam dan kejadian alam]\n'
            '  A --> D[Kehidupan sehari-hari dan keluarga]\n'
            '  A --> E[Sejarah, sains, musik, permainan]\n'
            '  A --> F[Kearifan budaya lokal]',
        ),
        'callout': 'Premise Timun Mas: Timun Mas ingin hidup bahagia bersama Mbok Sirni, tetapi saat berusia tujuh tahun ia harus diserahkan kepada raksasa.',
        'checkpoint': (
            'Ide atau gagasan utama yang melatarbelakangi cerita disebut…',
            [
                ('premise', True),
                ('storyboard', False),
                ('animatic', False),
                ('sinopsis', False),
            ],
            'Premise lalu diturunkan menjadi logline.',
        ),
    },
    'concept': {
        'material_title': 'Shot, scene, dan sequence',
        'title': 'Urutan pengambilan adegan',
        'paragraphs': [
            'Shot adalah bagian terkecil adegan, scene terdiri atas satu atau gabungan beberapa shot, dan sequence adalah gabungan beberapa scene.',
            'Angle kamera memperkuat dramatik: close up untuk dialog, extreme close up untuk emosi ekstrem, medium shot dari pinggang ke atas.',
            'Full shot menampilkan karakter utuh dari kaki sampai kepala untuk memperlihatkan gestur, sedangkan long shot menyorot objek dari jauh untuk menampilkan environment.',
            'Panning menggerakkan kamera searah gerak objek, dapat juga memperlihatkan suasana ruangan.',
        ],
        'table': [
            ['Angle/teknik', 'Penggunaan'],
            ['Close up', 'Adegan dialog, fokus ekspresi'],
            ['Extreme close up', 'Emosi ekstrem: kemarahan, kelicikan'],
            ['Medium shot', 'Percakapan antarkarakter'],
            ['Full shot', 'Karakter utuh dan gestur'],
            ['Long shot', 'Environment dan suasana pembuka scene'],
            ['Panning', 'Kamera mengikuti gerak objek'],
        ],
        'visual': {
            'type': 'diagram',
            'id': 'anim-10-urutan',
            'engine': 'mermaid',
            'title': 'Hubungan shot, scene, dan sequence',
            'code': 'flowchart LR\n'
                    '  A[Shot: bagian terkecil] --> B[Scene: gabungan shot]\n'
                    '  B --> C[Sequence: gabungan scene]\n'
                    '  C --> D[Film utuh]\n'
                    '  A --> E[Angle kamera menentukan kesan dramatik]',
        },
        'activity': categorize_block(
            'anim-10-klasifikasi',
            'Kelompokkan kegiatan sesuai urutan produksi cerita.',
            [('b1', 'Praproduksi naskah'), ('b2', 'Visualisasi'), ('b3', 'Pengukuran waktu')],
            [
                ('i1', 'Menulis premise dan logline', 'b1'),
                ('i2', 'Menyusun sinopsis tiga babak', 'b1'),
                ('i3', 'Membuat storyboard', 'b2'),
                ('i4', 'Menentukan angle kamera per shot', 'b2'),
                ('i5', 'Membuat animatic', 'b3'),
                ('i6', 'Mengukur durasi film sebelum diproduksi', 'b3'),
            ],
            'Tepat. Naskah dulu, lalu divisualkan, akhirnya diukur waktunya.',
            'Ingat: premise dan sinopsis naskah; storyboard visual; animatic waktu.',
        ),
        'subtitle': 'Storyboard dan animatic',
        'list': [
            'Sinopsis dibuat tiga paragraf mengikuti struktur tiga babak, sedangkan skenario diuraikan per adegan secara berurutan.',
            'Fungsi skenario adalah petunjuk kerja storyboard artist untuk memvisualkan cerita menjadi gambar storyboard.',
            'Storyboard dikembangkan Walt Disney tahun 1930 dan menjadi standar studio animasi pada 1937–1938.',
            'Storyboard memuat karakteristik tokoh, gerakan, durasi adegan, setting, dan perlakuan kamera beserta keterangan suara.',
            'Animatic adalah produk terakhir praproduksi untuk mengukur waktu dan gerakan kamera secara realtime.',
        ],
        'checkpoint': (
            'Produk terakhir praproduksi animasi untuk mengukur durasi disebut…',
            [
                ('animatic', True),
                ('storyboard', False),
                ('sinopsis', False),
                ('skenario', False),
            ],
            'Animatic berupa prototipe berdurasi nyata.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Menyusun cerita sampai animatic',
        'paragraphs': [
            'Sinopsis Timun Mas ditulis berdasarkan scene dan sequence: dari Mbok Sirni yang mendambakan anak hingga Timun Mas yang harus menghadapi raksasa.',
            'Template storyboard memuat shot description, audio, effect/graphics, dialogue/narration, scene, shot, dan transition.',
            'Animatic dibuat setelah storyboard, dubbing, sound effect, dan musik latar, sehingga durasi film sudah diketahui sebelum produksi penuh.',
        ],
        'scenario': scenario(
            'anim-10-skenario',
            'Cerita film pendek belum jelas',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Tim produksimu ingin membuat film pendek, tetapi ide masih kabur. Langkah pertama?',
                    'choices': [
                        {'text': 'Menentukan premise dan menuliskan logline satu kalimat', 'next': 'n2', 'score': 2, 'feedback': 'Premise dan logline memperjelas inti cerita.'},
                        {'text': 'Langsung menggambar semua adegan tanpa naskah', 'next': 'n3', 'score': 0, 'feedback': 'Tanpa naskah, cerita cenderung kacau dan melebar.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Agar tim memahami cerita, dokumen apa yang dibuat berikutnya?',
                    'choices': [
                        {'text': 'Sinopsis tiga babak, skenario, lalu storyboard dan animatic', 'next': 'n4', 'score': 2, 'feedback': 'Urutan dokumen ini menjadi pedoman produksi.'},
                        {'text': 'Hanya daftar nama karakter tanpa alur', 'next': 'n3', 'score': 0, 'feedback': 'Alur dan konflik harus terlihat agar cerita hidup.'},
                    ],
                },
                {'id': 'n3', 'text': 'Film selesai tetapi ceritanya membingungkan penonton.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Cerita jelas dan durasi terkontrol sehingga produksi lancar.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu logline?', 'back': 'Satu kalimat yang menjelaskan peristiwa dalam cerita.'},
            {'front': 'Urutan shot, scene, sequence?', 'back': 'Shot terkecil, scene gabungan shot, sequence gabungan scene.'},
            {'front': 'Berapa paragraf sinopsis?', 'back': 'Tiga paragraf sesuai struktur tiga babak.'},
            {'front': 'Apa isi template storyboard?', 'back': 'Shot description, audio, efek, dialog, scene, shot, transition.'},
        ],
        'checkpoint': (
            'Dokumen yang menjadi petunjuk kerja storyboard artist adalah…',
            [
                ('skenario', True),
                ('animatic', False),
                ('premise', False),
                ('sinopsis', False),
            ],
            'Skenario menjadi dasar visualisasi storyboard.',
        ),
        'challenge': challenge_block(
            'anim-10-tantangan',
            'Tantangan istilah cerita visual',
            90,
            [
                ('Ide utama cerita', 'Premise'),
                ('Bagian terkecil adegan', 'Shot'),
                ('Gabungan beberapa scene', 'Sequence'),
                ('Gambar panel visualisasi skenario', 'Storyboard'),
                ('Prototipe praproduksi untuk mengukur durasi', 'Animatic'),
            ],
            'Lima istilah cerita visual terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Ide utama yang melatarbelakangi cerita disebut…', 'premise', ['storyboard', 'logline', 'animatic'], 'Premise lalu dijabarkan jadi logline.', 'Menjadi fondasi cerita.'),
        ('Satu kalimat yang menjelaskan peristiwa cerita disebut…', 'logline', ['premise', 'sinopsis', 'sequence'], 'Disebut juga dramatic premise.', 'Memuat konflik utama.'),
        ('Film yang ide ceritanya berasal dari buku adalah…', 'How to Train Your Dragon: The Hidden World', ['A Bugs Life', 'Ice Age: The Meltdown', 'Ron’s Gone Wrong'], 'Diadaptasi dari buku fiksi.', 'Ide dari buku sangat umum.'),
        ('Film animasi yang ide ceritanya bersumber dari alam adalah…', 'A Bugs Life', ['Coco in Concert', 'Battle of Surabaya', 'Si Juki Anak Kosan'], 'Menampilkan kehidupan serangga.', 'Alam kaya inspirasi.'),
        ('Bagian terkecil dari adegan film disebut…', 'shot', ['scene', 'sequence', 'sinopsis'], 'Durasi beberapa detik hingga menit.', 'Ditentukan dengan angle kamera.'),
        ('Gabungan beberapa scene membentuk…', 'sequence', ['shot', 'logline', 'premise'], 'Sequence lebih besar dari scene.', 'Scene gabungan shot.'),
        ('Angle kamera untuk menampilkan ekspresi emosi ekstrem adalah…', 'extreme close up', ['medium shot', 'full shot', 'long shot'], 'Menyorot mata dan wajah.', 'Mengekspresikan kemarahan.'),
        ('Medium shot dibatasi dari…', 'pinggang ke atas', ['kaki ke kepala', 'kepala saja', 'mata saja'], 'Cocok untuk percakapan.', 'Menampilkan gestur tangan.'),
        ('Full shot memperlihatkan karakter…', 'utuh dari ujung kaki sampai ujung kepala', ['hanya wajah', 'hanya mata', 'hanya latar'], 'Memperlihatkan gestur.', 'Menunjukkan relasi antarkarakter.'),
        ('Teknik menggerakkan kamera searah gerak objek disebut…', 'panning', ['zoom', 'tilting', 'cut'], 'Dapat juga untuk memperlihatkan ruangan.', 'Menampilkan environment.'),
        ('Sinopsis cerita dibuat dalam…', 'tiga paragraf sesuai struktur tiga babak', ['satu paragraf panjang', 'lima paragraf', 'sepuluh paragraf'], 'Memuat penokohan dan latar.', 'Alur dramatis.'),
        ('Fungsi skenario adalah…', 'petunjuk kerja storyboard artist', ['menghitung anggaran', 'menjual produk', 'mengatur gaji'], 'Memuat keterangan, setting, waktu, dialog.', 'Disusun sesuai struktur dramatik.'),
        ('Storyboard pertama kali dikembangkan oleh…', 'studio Walt Disney tahun 1930', ['Pixar tahun 1995', 'Toon Boom tahun 2000', 'DreamWorks tahun 1994'], 'Berkembang dari sketsa cerita komik.', 'Menjadi standar pada 1937–1938.'),
        ('Animatic dibuat setelah…', 'storyboard, dubbing, sound effect, dan musik latar', ['film dirilis', 'pameran selesai', 'poster dicetak'], 'Durasi diketahui dari suara.', 'Menjadi prototipe praproduksi.'),
    ],
    'multi': [
        ('Manakah unsur cerita animasi?', ['Premise', 'Alur atau plot', 'Latar atau setting'], ['Rendering', 'Compositing', 'Dubbing'], 'Unsur cerita membangun narasi.', 'Sisanya tahap teknis.'),
        ('Manakah sumber ide cerita animasi?', ['Buku dan cerita rakyat', 'Alam dan kejadian alam', 'Kehidupan sehari-hari'], ['Jadwal produksi', 'Anggaran', 'Kontrak kerja'], 'Ide datang dari banyak sumber.', 'Sisanya administrasi.'),
        ('Manakah angle kamera yang dibahas?', ['Close up', 'Extreme close up', 'Medium shot'], ['Render engine', 'Keyframe', 'Viewport'], 'Angle menentukan kesan dramatik.', 'Sisanya istilah teknis 3D.'),
        ('Manakah urutan pengambilan adegan?', ['Shot', 'Scene', 'Sequence'], ['Premise', 'Logline', 'Sinopsis'], 'Urutan dari bagian terkecil ke besar.', 'Sisanya istilah naskah.'),
        ('Manakah isi storyboard?', ['Shot description', 'Dialogue atau narration', 'Transition'], ['Harga sewa', 'Gaji kru', 'Stok kertas'], 'Storyboard memuat keterangan adegan.', 'Sisanya bukan isi storyboard.'),
        ('Manakah ciri animatic?', ['Prototipe praproduksi', 'Mengukur durasi realtime', 'Memuat suara dan gerakan kamera'], ['Film final siap rilis', 'Poster promosi', 'Naskah tertulis'], 'Animatic mengukur waktu.', 'Bukan produk final.'),
        ('Manakah contoh film animasi Indonesia bertema kearifan lokal?', ['Binekon', 'Battle of Surabaya', 'Si Juki Anak Kosan'], ['Toy Story', 'Frozen', 'Moana'], 'Karya anak bangsa mengangkat lokalitas.', 'Sisanya film studio asing.'),
        ('Manakah fungsi angle kamera?', ['Memperkuat dramatik', 'Memudahkan penonton mengikuti alur', 'Menentukan keypose adegan'], ['Menghitung anggaran', 'Menyusun jadwal', 'Menyeleksi kru'], 'Angle mendukung cerita.', 'Sisanya pekerjaan manajemen.'),
    ],
    'pairs': [
        ('Premise', 'ide utama cerita'),
        ('Logline', 'ringkasan satu kalimat'),
        ('Shot', 'bagian terkecil adegan'),
        ('Sequence', 'gabungan beberapa scene'),
        ('Sinopsis', 'uraian cerita tiga paragraf'),
        ('Skenario', 'naskah per adegan'),
        ('Storyboard', 'gambar panel adegan'),
        ('Animatic', 'prototipe pengukur durasi'),
    ],
    'steps': [
        ('Urutkan penulisan naskah animasi.', ['Menentukan premise', 'Menulis logline', 'Menyusun sinopsis tiga babak', 'Menulis skenario', 'Membuat storyboard dan animatic'], 'Premise menjadi awal.', 'Animatic menutup praproduksi.'),
        ('Urutkan skala adegan dari kecil ke besar.', ['Shot', 'Scene', 'Sequence', 'Film utuh'], 'Shot paling kecil.', 'Film utuh paling besar.'),
        ('Urutkan pembuatan animatic.', ['Menyelesaikan storyboard', 'Merekam dubbing', 'Menambahkan sound effect dan musik', 'Menyusun gambar sesuai durasi suara', 'Evaluasi dan revisi'], 'Storyboard mendahului suara.', 'Evaluasi menutup proses.'),
        ('Urutkan pembuatan storyboard.', ['Membaca skenario', 'Memilih scene dan shot', 'Menentukan angle kamera', 'Menggambar panel dan keterangan', 'Menambahkan dialog dan efek'], 'Skenario dibaca dulu.', 'Dialog melengkapi panel.'),
        ('Urutkan perjalanan ide menjadi film.', ['Sumber ide', 'Premise dan logline', 'Sinopsis dan skenario', 'Storyboard dan animatic', 'Produksi dan pascaproduksi'], 'Ide menjadi awal.', 'Produksi menutup rangkaian.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)