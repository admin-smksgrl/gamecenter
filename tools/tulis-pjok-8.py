"""PJOK 8 — Gerak Berirama (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 8',
    'slug': 'pjok-8-gerak-berirama',
    'title': 'Gerak Berirama',
    'description': (
        'Mempelajari senam irama, unsur gerak, langkah dasar, ayunan lengan, '
        'penggunaan alat, dan penyusunan rangkaian gerak dengan iringan musik.'
    ),
    'objectives': [
        'Menjelaskan pengertian dan unsur gerak berirama.',
        'Mempraktikkan langkah dasar dan ayunan lengan sesuai ketukan.',
        'Menyusun rangkaian gerak berirama secara berkelompok.',
        'Menunjukkan kekompakan, disiplin, dan sportivitas dalam berlatih.',
        'Menjaga keselamatan diri dan teman selama latihan gerak berirama.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 8 Gerak Berirama; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Gerak berirama', 'definition': 'Gerak senam yang dilakukan mengikuti irama musik atau ketukan.'},
        {'term': 'Senam irama', 'definition': 'Senam yang memadukan gerak dengan musik, hitungan, atau nyanyian.'},
        {'term': 'Langkah biasa', 'definition': 'Langkah ke depan dengan kaki bergantian mengikuti irama.'},
        {'term': 'Langkah rapat', 'definition': 'Langkah yang diakhiri dengan merapatkan kaki di sisi kaki tumpu.'},
        {'term': 'Langkah keseimbangan', 'definition': 'Langkah dengan satu kaki ditahan sebentar untuk menjaga keseimbangan.'},
        {'term': 'Ayunan lengan', 'definition': 'Gerak mengayunkan lengan ke depan, samping, atau atas sesuai irama.'},
        {'term': 'Simpai', 'definition': 'Alat berbentuk lingkaran yang digunakan dalam senam irama.'},
        {'term': 'Keluwesan', 'definition': 'Kemampuan melakukan gerak secara lentur dan tidak kaku.'},
    ],
    'intro': {
        'material_title': 'Mengapa gerak berirama menyenangkan?',
        'title': 'Bergerak selaras dengan musik',
        'paragraphs': [
            'Gerak berirama adalah aktivitas jasmani yang dilakukan mengikuti irama musik, ketukan, atau nyanyian. Gerakannya menggabungkan kelenturan, keseimbangan, dan koordinasi tubuh.',
            'Senam irama dapat dilakukan tanpa alat atau dengan alat seperti simpai, tali, bola, gada, dan pita. Gerakan diiringi musik agar tubuh bergerak selaras dan kompak.',
            'Gerak berirama melatih kebugaran, kepekaan terhadap irama, dan kerja sama. Dalam kelompok, setiap anggota harus bergerak pada waktu yang sama agar tampak rapi.',
        ],
        'diagram': (
            'Alur belajar gerak berirama',
            'flowchart LR\n'
            '  A[Mendengar irama] --> B[Menghitung ketukan]\n'
            '  B --> C[Melakukan langkah dasar]\n'
            '  C --> D[Menambahkan ayunan lengan]\n'
            '  D --> E[Merangkai gerak]\n'
            '  E --> F[Tampil berkelompok]',
        ),
        'callout': 'Gunakan pakaian yang nyaman, alas kaki yang tidak licin, dan lakukan pemanasan sebelum berlatih agar gerakan aman.',
        'checkpoint': (
            'Apa yang menjadi pengiring utama gerak berirama?',
            [
                ('Musik atau ketukan', True),
                ('Sorakan penonton', False),
                ('Bunyi peluit wasit', False),
                ('Suara kendaraan', False),
            ],
            'Gerak berirama dilakukan mengikuti musik, ketukan, atau nyanyian.',
        ),
    },
    'concept': {
        'material_title': 'Unsur dan langkah dasar',
        'title': 'Unsur gerak, langkah, dan ayunan',
        'paragraphs': [
            'Gerak berirama memiliki beberapa unsur utama: kelenturan, keseimbangan, keluwesan, ketepatan irama, dan koordinasi. Unsur-unsur ini membuat gerakan tampak indah dan selaras.',
            'Langkah dasar dalam senam irama meliputi langkah biasa, langkah rapat, langkah keseimbangan, dan langkah samping. Ayunan lengan dilakukan ke depan, samping, atau atas sesuai ketukan.',
            'Gerakan dapat dihitung dalam birama 2/4, 3/4, atau 4/4. Hitungan membantu kelompok bergerak serempak. Alat seperti simpai dan tali menambah variasi gerakan.',
        ],
        'table': [
            ['Unsur/Gerak', 'Tujuan', 'Kunci gerak'],
            ['Kelenturan', 'Gerakan tidak kaku', 'Lenturkan sendi dan otot'],
            ['Keseimbangan', 'Tubuh stabil', 'Tumpuan kaki kuat, badan tegak'],
            ['Langkah biasa', 'Bergerak maju', 'Kaki bergantian mengikuti irama'],
            ['Langkah rapat', 'Merapatkan kaki', 'Kaki dirapatkan di sisi kaki tumpu'],
            ['Ayunan lengan', 'Memperindah gerak', 'Lengan rileks, arah sesuai hitungan'],
        ],
        'visual': chart_block(
            'pjok-8-hitungan-birama',
            'Jumlah ketukan dalam satu birama',
            'bar',
            [('Birama 2/4', 2), ('Birama 3/4', 3), ('Birama 4/4', 4)],
        ),
        'activity': categorize_block(
            'pjok-8-klasifikasi',
            'Kelompokkan pernyataan berikut ke dalam langkah kaki atau ayunan lengan.',
            [('b1', 'Langkah kaki'), ('b2', 'Ayunan lengan')],
            [
                ('i1', 'Langkah biasa', 'b1'),
                ('i2', 'Langkah rapat', 'b1'),
                ('i3', 'Ayunan ke depan', 'b2'),
                ('i4', 'Ayunan ke samping', 'b2'),
                ('i5', 'Langkah keseimbangan', 'b1'),
                ('i6', 'Ayunan ke atas', 'b2'),
            ],
            'Tepat. Langkah biasa, rapat, dan keseimbangan termasuk gerak kaki; ayunan termasuk gerak lengan.',
            'Periksa lagi: langkah memakai kaki, ayunan memakai lengan.',
        ),
        'subtitle': 'Alat dan iringan',
        'list': [
            'Simpai diputar atau diayunkan mengikuti irama.',
            'Tali diayunkan melewati tubuh sesuai hitungan.',
            'Bola diayunkan atau dilempar ringan dengan kendali.',
            'Pita digerakkan membentuk pola lengkung agar tampak indah.',
        ],
        'checkpoint': (
            'Berapa ketukan dalam satu birama 4/4?',
            [
                ('4 ketukan', True),
                ('2 ketukan', False),
                ('3 ketukan', False),
                ('6 ketukan', False),
            ],
            'Birama 4/4 memiliki empat ketukan dalam satu birama.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Bergerak kompak dan sportif',
        'paragraphs': [
            'Gerak berirama menuntut kekompakan. Setiap anggota kelompok harus menghitung ketukan dan bergerak pada waktu yang sama. Latihan berulang membantu tubuh mengingat urutan gerak.',
            'Sportivitas tampak ketika peserta memberi semangat, menerima masukan, dan tidak menyalahkan teman saat gerakan belum rapi. Kerja sama dibangun melalui latihan bersama.',
            'Susun rangkaian gerak sederhana: langkah biasa, ayunan lengan, langkah rapat, lalu gerak keseimbangan. Ulangi rangkaian sampai kompak sebelum tampil.',
        ],
        'scenario': scenario(
            'pjok-8-skenario',
            'Keputusan saat latihan kelompok',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Saat latihan, satu anggota kelompok sering terlambat mengikuti hitungan. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Mengulang latihan bersama dengan hitungan yang jelas', 'next': 'n2', 'score': 2, 'feedback': 'Latihan bersama membantu kekompakan.'},
                        {'text': 'Membiarkannya dan berharap tampil baik', 'next': 'n3', 'score': 0, 'feedback': 'Ketidakkompakan akan terlihat saat tampil.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Musik yang dipakai terlalu cepat untuk rangkaian gerak kalian. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Memilih tempo yang sesuai kemampuan kelompok', 'next': 'n4', 'score': 2, 'feedback': 'Tempo yang sesuai membuat gerakan lebih rapi.'},
                        {'text': 'Tetap memakai tempo cepat agar terlihat sulit', 'next': 'n3', 'score': 0, 'feedback': 'Tempo terlalu cepat membuat gerakan tidak kompak.'},
                    ],
                },
                {'id': 'n3', 'text': 'Penampilan kurang rapi karena latihan tidak disesuaikan.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kelompok tampil kompak dan selaras dengan irama.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu gerak berirama?', 'back': 'Gerak senam yang dilakukan mengikuti irama musik atau ketukan.'},
            {'front': 'Sebutkan unsur gerak berirama.', 'back': 'Kelenturan, keseimbangan, keluwesan, ketepatan irama, dan koordinasi.'},
            {'front': 'Apa itu langkah rapat?', 'back': 'Langkah yang diakhiri dengan merapatkan kaki di sisi kaki tumpu.'},
            {'front': 'Sebutkan alat senam irama.', 'back': 'Simpai, tali, bola, gada, dan pita.'},
        ],
        'checkpoint': (
            'Agar kelompok tampil kompak, hal paling penting adalah…',
            [
                ('Berlatih bersama dengan hitungan yang jelas', True),
                ('Memakai musik paling cepat', False),
                ('Bergerak sesuai keinginan masing-masing', False),
                ('Menghafal gerakan tanpa berlatih', False),
            ],
            'Latihan bersama dengan hitungan jelas membuat gerakan serempak.',
        ),
        'challenge': challenge_block(
            'pjok-8-tantangan',
            'Tantangan istilah gerak berirama',
            90,
            [
                ('Pengiring gerak berirama', 'musik'),
                ('Alat berbentuk lingkaran', 'simpai'),
                ('Langkah yang merapatkan kaki', 'langkah rapat'),
                ('Jumlah ketukan birama 3/4', '3'),
                ('Kemampuan bergerak lentur', 'keluwesan'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa yang mengiringi gerak berirama?', 'Musik atau ketukan', ['Peluit wasit', 'Sorakan penonton', 'Bunyi kendaraan'], 'Gerak berirama dilakukan mengikuti musik, ketukan, atau nyanyian.', 'Irama membantu tubuh bergerak selaras.'),
        ('Apa nama lain dari gerak berirama?', 'Senam irama', ['Senam lantai', 'Senam ketangkasan', 'Senam aerobik'], 'Gerak berirama juga disebut senam irama.', 'Gerakan ini menekankan keselarasan dengan irama.'),
        ('Apa induk organisasi senam Indonesia?', 'PERSANI', ['PASI', 'PBSI', 'PERBASI'], 'PERSANI adalah Persatuan Senam Indonesia.', 'Organisasi ini juga menaungi senam irama.'),
        ('Apa nama langkah yang diakhiri merapatkan kaki?', 'Langkah rapat', ['Langkah biasa', 'Langkah keseimbangan', 'Langkah samping'], 'Langkah rapat diakhiri dengan merapatkan kaki di sisi kaki tumpu.', 'Gerakan ini membuat posisi kaki kembali rapat.'),
        ('Apa nama langkah dengan satu kaki ditahan sebentar?', 'Langkah keseimbangan', ['Langkah biasa', 'Langkah rapat', 'Langkah samping'], 'Langkah keseimbangan menahan satu kaki sebentar untuk menjaga keseimbangan.', 'Gerakan ini melatih kestabilan tubuh.'),
        ('Berapa ketukan dalam birama 3/4?', '3 ketukan', ['2 ketukan', '4 ketukan', '6 ketukan'], 'Birama 3/4 memiliki tiga ketukan.', 'Hitung satu, dua, tiga secara berulang.'),
        ('Berapa ketukan dalam birama 4/4?', '4 ketukan', ['2 ketukan', '3 ketukan', '6 ketukan'], 'Birama 4/4 memiliki empat ketukan.', 'Birama ini sering dipakai dalam musik populer.'),
        ('Apa nama alat senam irama berbentuk lingkaran?', 'Simpai', ['Tali', 'Gada', 'Pita'], 'Simpai adalah alat berbentuk lingkaran.', 'Alat ini dapat diputar atau diayunkan.'),
        ('Apa nama alat senam irama yang panjang dan lentur?', 'Pita', ['Simpai', 'Bola', 'Gada'], 'Pita adalah alat panjang dan lentur yang digerakkan membentuk pola.', 'Gerakan pita membentuk lengkungan indah.'),
        ('Apa unsur gerak berirama yang membuat gerakan tidak kaku?', 'Kelenturan', ['Kekuatan', 'Kecepatan', 'Ketepatan'], 'Kelenturan membuat gerakan tampak lentur dan tidak kaku.', 'Kelenturan dilatih melalui peregangan.'),
        ('Apa unsur yang membuat tubuh tetap stabil saat bergerak?', 'Keseimbangan', ['Kelenturan', 'Kecepatan', 'Daya tahan'], 'Keseimbangan menjaga tubuh tetap stabil.', 'Tumpuan kaki yang kuat membantu keseimbangan.'),
        ('Apa tujuan ayunan lengan dalam gerak berirama?', 'Memperindah gerakan', ['Menambah berat badan', 'Menghentikan musik', 'Mengganti langkah kaki'], 'Ayunan lengan membuat gerakan lebih indah dan selaras.', 'Lengan bergerak rileks sesuai irama.'),
        ('Apa yang harus dilakukan sebelum latihan gerak berirama?', 'Pemanasan', ['Langsung tampil', 'Makan berat', 'Berlari jauh'], 'Pemanasan menyiapkan otot dan sendi sebelum bergerak.', 'Pemanasan mengurangi risiko cedera.'),
        ('Apa yang membuat kelompok tampak rapi saat tampil?', 'Gerakan serempak sesuai hitungan', ['Gerakan berbeda setiap orang', 'Musik paling cepat', 'Tidak berlatih bersama'], 'Kekompakan muncul dari latihan bersama dan hitungan yang jelas.', 'Setiap anggota harus bergerak pada waktu yang sama.'),
    ],
    'multi': [
        ('Manakah yang termasuk unsur gerak berirama?', ['Kelenturan', 'Keseimbangan', 'Ketepatan irama'], ['Kecepatan berkendara', 'Kekuatan menggigit'], 'Kelenturan, keseimbangan, dan ketepatan irama adalah unsur gerak berirama.', 'Unsur lain di luar gerak berirama.'),
        ('Manakah yang termasuk langkah dasar senam irama?', ['Langkah biasa', 'Langkah rapat'], ['Langkah smash', 'Langkah servis'], 'Langkah biasa dan langkah rapat adalah langkah dasar senam irama.', 'Smash dan servis bukan istilah senam irama.'),
        ('Apa manfaat gerak berirama?', ['Melatih kebugaran', 'Melatih kepekaan irama'], ['Menghilangkan kebutuhan pemanasan', 'Menggantikan tidur'], 'Gerak berirama melatih kebugaran dan kepekaan irama.', 'Pemanasan tetap diperlukan.'),
        ('Manakah ciri gerakan yang selaras dengan irama?', ['Gerak mengikuti ketukan', 'Gerak dilakukan serempak'], ['Gerak acak tanpa hitungan', 'Setiap orang bergerak berbeda'], 'Gerak selaras mengikuti ketukan dan dilakukan serempak.', 'Hitungan membantu kekompakan.'),
        ('Manakah yang termasuk alat senam irama?', ['Simpai', 'Tali', 'Pita'], ['Raket', 'Tongkat estafet'], 'Simpai, tali, dan pita adalah alat senam irama.', 'Raket dan tongkat estafet bukan alat senam irama.'),
        ('Manakah unsur yang membuat gerakan tampak indah?', ['Keluwesan', 'Koordinasi'], ['Kekakuan', 'Ketegangan berlebih'], 'Keluwesan dan koordinasi membuat gerakan indah.', 'Gerakan kaku mengurangi keindahan.'),
        ('Manakah pernyataan yang benar tentang birama?', ['Birama 2/4 memiliki 2 ketukan', 'Birama 4/4 memiliki 4 ketukan'], ['Birama 3/4 memiliki 4 ketukan', 'Birama 4/4 memiliki 2 ketukan'], 'Jumlah ketukan sesuai angka pembilang birama.', 'Hitung ketukan secara berulang.'),
        ('Manakah pernyataan yang benar tentang latihan kelompok?', ['Latihan dilakukan bersama', 'Hitungan dibuat jelas'], ['Setiap anggota berlatih sendiri tanpa koordinasi', 'Tempo musik tidak perlu diperhatikan'], 'Latihan bersama dan hitungan jelas membuat kelompok kompak.', 'Kekompakan adalah tujuan utama.'),
    ],
    'pairs': [
        ('Gerak berirama', 'gerak mengikuti irama musik'),
        ('Langkah biasa', 'langkah ke depan dengan kaki bergantian'),
        ('Langkah rapat', 'langkah yang merapatkan kaki'),
        ('Langkah keseimbangan', 'langkah dengan satu kaki ditahan'),
        ('Ayunan lengan', 'gerak lengan sesuai irama'),
        ('Simpai', 'alat senam berbentuk lingkaran'),
        ('Pita', 'alat senam panjang dan lentur'),
        ('Keluwesan', 'kemampuan bergerak lentur'),
    ],
    'steps': [
        ('Urutkan langkah melakukan gerak langkah biasa.', ['Berdiri tegak', 'Langkahkan kaki kanan ke depan', 'Langkahkan kaki kiri menyusul', 'Ulangi sesuai hitungan'], 'Langkah biasa dilakukan dengan kaki bergantian mengikuti irama.', 'Jaga badan tetap tegak.'),
        ('Urutkan langkah melakukan langkah rapat.', ['Langkahkan satu kaki ke samping', 'Rapatkan kaki lainnya', 'Kembalikan ke posisi semula', 'Ulangi sesuai hitungan'], 'Langkah rapat diakhiri dengan merapatkan kaki.', 'Gerakan dilakukan bergantian ke dua arah.'),
        ('Urutkan langkah melakukan ayunan lengan ke depan.', ['Berdiri tegak', 'Rentangkan lengan ke bawah', 'Ayunkan lengan ke depan', 'Kembalikan sesuai hitungan'], 'Ayunan lengan dilakukan rileks mengikuti ketukan.', 'Jangan mengangkat bahu berlebihan.'),
        ('Urutkan langkah menyusun rangkaian gerak berirama.', ['Pilih musik dan hitungan', 'Tentukan langkah dasar', 'Tambahkan ayunan lengan', 'Latih rangkaian bersama kelompok'], 'Rangkaian disusun dari musik, langkah, ayunan, lalu latihan bersama.', 'Ulangi sampai gerakan kompak.'),
        ('Urutkan alur latihan gerak berirama yang aman.', ['Pemanasan', 'Latihan langkah dasar', 'Latihan rangkaian dengan musik', 'Pendinginan'], 'Latihan dimulai dari pemanasan dan diakhiri pendinginan.', 'Jangan langsung menampilkan rangkaian sulit.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
