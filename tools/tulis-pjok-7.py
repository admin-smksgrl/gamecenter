"""PJOK 7 — Senam (Kelas X, Fase E)."""
from pjok_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PJOK 7',
    'slug': 'pjok-7-senam',
    'title': 'Senam',
    'description': (
        'Mempelajari senam lantai dan ketangkasan, mulai dari guling depan, '
        'guling belakang, sikap lilin, kayang, meroda, hingga handstand, '
        'dengan menekankan keselamatan.'
    ),
    'objectives': [
        'Menjelaskan jenis dan manfaat senam lantai.',
        'Mempraktikkan guling depan, guling belakang, sikap lilin, dan kayang.',
        'Mempraktikkan gerak meroda, handstand, dan headstand dengan bantuan.',
        'Menerapkan prinsip keselamatan dan spotting dalam senam.',
        'Menunjukkan disiplin, keberanian, dan tanggung jawab selama berlatih.',
    ],
    'minutes': 90,
    'source': (
        'PJOK-BG-KLS-X.pdf Bab 7 Senam; '
        'CP Fase E PJOK; ATP Fase E Kelas 10 PJOK'
    ),
    'glossary': [
        {'term': 'Senam lantai', 'definition': 'Senam yang dilakukan di atas matras tanpa alat bantu utama.'},
        {'term': 'Guling depan', 'definition': 'Berguling ke depan dengan tubuh membulat dan tengkuk menyentuh matras.'},
        {'term': 'Guling belakang', 'definition': 'Berguling ke belakang dengan tubuh membulat dan tangan menopang.'},
        {'term': 'Sikap lilin', 'definition': 'Berdiri di atas bahu dan tengkuk dengan kedua kaki lurus ke atas.'},
        {'term': 'Kayang', 'definition': 'Melengkungkan badan ke belakang dengan tangan dan kaki menopang tubuh.'},
        {'term': 'Meroda', 'definition': 'Berputar ke samping dengan tangan dan kaki bergantian menyentuh matras.'},
        {'term': 'Handstand', 'definition': 'Berdiri dengan kedua tangan sebagai penopang tubuh.'},
        {'term': 'Spotting', 'definition': 'Bantuan pengaman dari teman atau guru saat melakukan gerakan sulit.'},
    ],
    'intro': {
        'material_title': 'Mengapa senam penting?',
        'title': 'Melatih kelenturan dan kendali tubuh',
        'paragraphs': [
            'Senam adalah aktivitas jasmani yang menekankan kelenturan, keseimbangan, kekuatan, dan koordinasi. Senam lantai dilakukan di atas matras dengan gerakan berguling, berputar, dan bertumpu.',
            'Senam lantai termasuk senam ketangkasan. Gerakannya dapat dilakukan tanpa alat bantu utama, tetapi membutuhkan matras dan pengaman. Di Indonesia, Persatuan Senam Indonesia (PERSANI) menjadi induk organisasinya.',
            'Senam melatih keberanian dan tanggung jawab. Gerakan sulit harus dipelajari bertahap dengan bantuan guru atau teman agar aman.',
        ],
        'diagram': (
            'Alur belajar senam lantai',
            'flowchart LR\n'
            '  A[Pemanasan] --> B[Gerak dasar]\n'
            '  B --> C[Gerak dengan bantuan]\n'
            '  C --> D[Gerak mandiri]\n'
            '  D --> E[Pendinginan]\n'
            '  E --> F[Evaluasi gerak]',
        ),
        'callout': 'Gunakan matras yang tidak licin, lepas aksesori, dan minta bantuan spotting saat mencoba gerakan baru.',
        'checkpoint': (
            'Apa induk organisasi senam Indonesia?',
            [
                ('PERSANI', True),
                ('PASI', False),
                ('PBSI', False),
                ('PERBASI', False),
            ],
            'PERSANI adalah Persatuan Senam Indonesia.',
        ),
    },
    'concept': {
        'material_title': 'Gerak dasar senam lantai',
        'title': 'Guling, keseimbangan, dan putaran',
        'paragraphs': [
            'Senam lantai dilakukan di area matras berukuran sekitar 12 meter × 12 meter. Gerakan dasar meliputi guling depan, guling belakang, sikap lilin, kayang, meroda, handstand, dan headstand.',
            'Guling depan dilakukan dengan tubuh membulat, dagu menempel dada, dan tengkuk menyentuh matras. Guling belakang dilakukan dengan tangan menopang di samping kepala agar leher tidak terbebani.',
            'Gerakan keseimbangan seperti sikap lilin, handstand, dan headstand membutuhkan kekuatan lengan serta kendali tubuh. Gerakan putaran seperti meroda membutuhkan koordinasi tangan dan kaki.',
        ],
        'table': [
            ['Gerakan', 'Tujuan', 'Kunci gerak'],
            ['Guling depan', 'Melatih kelenturan dan kendali', 'Dagu ke dada, tengkuk di matras, tubuh membulat'],
            ['Guling belakang', 'Melatih koordinasi', 'Tangan menopang, kaki mendorong, tubuh membulat'],
            ['Sikap lilin', 'Melatih keseimbangan', 'Siku menopang pinggang, kaki lurus ke atas'],
            ['Kayang', 'Melatih kelenturan punggung', 'Tangan dan kaki menopang, badan melengkung'],
            ['Meroda', 'Melatih koordinasi samping', 'Tangan dan kaki bergantian menyentuh matras'],
            ['Handstand', 'Melatih kekuatan lengan', 'Tangan menopang, badan lurus, kaki rapat'],
        ],
        'visual': chart_block(
            'pjok-7-urutan-gerak',
            'Tingkat kesulitan relatif gerak senam',
            'bar',
            [('Guling depan', 1), ('Sikap lilin', 2), ('Meroda', 3), ('Handstand', 4)],
        ),
        'activity': categorize_block(
            'pjok-7-klasifikasi',
            'Kelompokkan gerakan berikut ke dalam gerak berguling atau gerak keseimbangan.',
            [('b1', 'Gerak berguling'), ('b2', 'Gerak keseimbangan')],
            [
                ('i1', 'Guling depan', 'b1'),
                ('i2', 'Guling belakang', 'b1'),
                ('i3', 'Sikap lilin', 'b2'),
                ('i4', 'Handstand', 'b2'),
                ('i5', 'Kayang', 'b2'),
                ('i6', 'Meroda', 'b1'),
            ],
            'Tepat. Guling dan meroda melibatkan putaran; sikap lilin, handstand, dan kayang menekankan keseimbangan.',
            'Periksa lagi: gerak berguling memutar tubuh, gerak keseimbangan menahan posisi.',
        ),
        'subtitle': 'Prinsip keselamatan',
        'list': [
            'Periksa matras agar tidak licin dan tidak ada benda keras di sekitarnya.',
            'Lakukan pemanasan pada leher, bahu, pinggang, dan pergelangan tangan.',
            'Minta bantuan spotting saat mencoba handstand atau headstand.',
            'Hentikan gerakan jika merasa nyeri pada leher atau punggung.',
        ],
        'checkpoint': (
            'Bagian tubuh yang pertama menyentuh matras saat guling depan adalah…',
            [
                ('Tengkuk', True),
                ('Dahi', False),
                ('Punggung', False),
                ('Pinggang', False),
            ],
            'Guling depan mendaratkan tengkuk lebih dulu, bukan dahi, agar leher aman.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Berlatih bertahap dan aman',
        'paragraphs': [
            'Senam menuntut latihan bertahap. Mulailah dari gerakan mudah seperti guling depan, lalu tingkatkan ke gerakan yang lebih sulit. Jangan memaksakan gerakan yang belum dikuasai.',
            'Sportivitas tampak ketika peserta membantu teman dengan spotting, memberi semangat, dan menghormati batas kemampuan. Kerja sama membuat latihan lebih aman.',
            'Gunakan matras dan dampingan guru. Hentikan latihan sesaat untuk membahas posisi tubuh yang benar.',
        ],
        'scenario': scenario(
            'pjok-7-skenario',
            'Keputusan saat latihan senam',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Kamu ingin mencoba handstand, tetapi belum pernah melakukannya. Apa yang kamu lakukan?',
                    'choices': [
                        {'text': 'Meminta bantuan guru atau teman untuk spotting', 'next': 'n2', 'score': 2, 'feedback': 'Spotting membuat latihan lebih aman.'},
                        {'text': 'Mencoba sendiri tanpa pengaman', 'next': 'n3', 'score': 0, 'feedback': 'Gerakan baru tanpa pengaman berisiko cedera.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Saat mencoba, tanganmu terasa lemas. Apa pilihanmu?',
                    'choices': [
                        {'text': 'Berhenti dan berlatih kekuatan lengan lebih dulu', 'next': 'n4', 'score': 2, 'feedback': 'Kekuatan dasar penting sebelum gerakan sulit.'},
                        {'text': 'Tetap memaksa sampai berhasil', 'next': 'n3', 'score': 0, 'feedback': 'Memaksa tubuh yang lemas dapat menyebabkan cedera.'},
                    ],
                },
                {'id': 'n3', 'text': 'Latihan terhenti karena risiko cedera.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Kamu berlatih bertahap dan berhasil dengan aman.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Apa itu spotting?', 'back': 'Bantuan pengaman dari teman atau guru saat melakukan gerakan sulit.'},
            {'front': 'Apa kunci guling depan?', 'back': 'Dagu menempel dada dan tengkuk menyentuh matras.'},
            {'front': 'Apa itu sikap lilin?', 'back': 'Berdiri di atas bahu dengan kedua kaki lurus ke atas.'},
            {'front': 'Apa itu meroda?', 'back': 'Berputar ke samping dengan tangan dan kaki bergantian menyentuh matras.'},
        ],
        'checkpoint': (
            'Saat berlatih handstand, bantuan pengaman sebaiknya diberikan oleh…',
            [
                ('Guru atau teman yang memahami teknik', True),
                ('Siapa saja yang kebetulan lewat', False),
                ('Diri sendiri tanpa pengawasan', False),
                ('Teman yang belum pernah berlatih', False),
            ],
            'Spotting harus dilakukan oleh orang yang memahami teknik dan keselamatan.',
        ),
        'challenge': challenge_block(
            'pjok-7-tantangan',
            'Tantangan istilah senam',
            90,
            [
                ('Induk organisasi senam Indonesia', 'PERSANI'),
                ('Alas untuk senam lantai', 'matras'),
                ('Gerakan berdiri dengan tangan', 'handstand'),
                ('Bantuan pengaman saat senam', 'spotting'),
                ('Gerakan berputar ke samping', 'meroda'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa induk organisasi senam Indonesia?', 'PERSANI', ['PASI', 'PBSI', 'PERBASI'], 'PERSANI adalah Persatuan Senam Indonesia.', 'Bandingkan dengan PASI untuk atletik.'),
        ('Apa alas yang digunakan untuk senam lantai?', 'Matras', ['Papan', 'Rumput', 'Lantai keramik'], 'Senam lantai dilakukan di atas matras agar aman.', 'Matras mengurangi benturan.'),
        ('Apa nama gerakan berguling ke depan?', 'Guling depan', ['Guling belakang', 'Meroda', 'Kayang'], 'Guling depan dilakukan dengan tubuh membulat ke depan.', 'Dagu menempel dada saat berguling.'),
        ('Apa nama gerakan berguling ke belakang?', 'Guling belakang', ['Guling depan', 'Sikap lilin', 'Handstand'], 'Guling belakang dilakukan dengan tubuh membulat ke belakang.', 'Tangan menopang di samping kepala.'),
        ('Apa nama gerakan berdiri di atas bahu dengan kaki ke atas?', 'Sikap lilin', ['Kayang', 'Meroda', 'Handstand'], 'Sikap lilin bertumpu pada bahu dan tengkuk.', 'Kedua kaki lurus ke atas.'),
        ('Apa nama gerakan melengkungkan badan ke belakang?', 'Kayang', ['Sikap lilin', 'Guling depan', 'Meroda'], 'Kayang melengkungkan badan dengan tangan dan kaki menopang.', 'Gerakan ini melatih kelenturan punggung.'),
        ('Apa nama gerakan berputar ke samping?', 'Meroda', ['Guling depan', 'Kayang', 'Headstand'], 'Meroda berputar ke samping dengan tangan dan kaki bergantian.', 'Gerakan ini menyerupai roda berputar.'),
        ('Apa nama gerakan berdiri dengan kedua tangan?', 'Handstand', ['Headstand', 'Sikap lilin', 'Kayang'], 'Handstand bertumpu pada kedua tangan.', 'Tubuh lurus dan kaki rapat ke atas.'),
        ('Apa nama gerakan berdiri dengan kepala?', 'Headstand', ['Handstand', 'Sikap lilin', 'Meroda'], 'Headstand bertumpu pada kepala dan kedua tangan.', 'Gerakan ini membutuhkan pengaman.'),
        ('Bagian tubuh yang menyentuh matras pertama saat guling depan?', 'Tengkuk', ['Dahi', 'Punggung', 'Pinggang'], 'Tengkuk menyentuh matras lebih dulu agar leher aman.', 'Dagu menempel dada untuk membulatkan tubuh.'),
        ('Apa fungsi spotting?', 'Membantu keamanan saat melakukan gerakan sulit', ['Menambah nilai', 'Mempercepat gerakan', 'Menggantikan pemanasan'], 'Spotting membantu menjaga keselamatan saat berlatih.', 'Bantuan diberikan oleh guru atau teman yang paham teknik.'),
        ('Apa yang harus dilakukan sebelum senam?', 'Pemanasan', ['Langsung berguling', 'Makan berat', 'Berlari jauh'], 'Pemanasan menyiapkan otot dan sendi sebelum senam.', 'Pemanasan juga mengurangi risiko cedera.'),
        ('Berapa ukuran area matras senam lantai?', 'Sekitar 12 m × 12 m', ['8 m × 8 m', '18 m × 9 m', '28 m × 15 m'], 'Area senam lantai berukuran sekitar 12 meter × 12 meter.', 'Ukuran ini memberi ruang untuk gerakan.'),
        ('Apa yang harus dilakukan jika merasa nyeri saat senam?', 'Berhenti dan melapor kepada guru', ['Memaksa melanjutkan', 'Mengabaikan rasa nyeri', 'Mengulang gerakan lebih keras'], 'Nyeri adalah tanda tubuh perlu istirahat.', 'Keselamatan lebih penting daripada menyelesaikan gerakan.'),
    ],
    'multi': [
        ('Manakah yang termasuk gerak senam lantai?', ['Guling depan', 'Sikap lilin', 'Meroda'], ['Smash', 'Servis'], 'Guling depan, sikap lilin, dan meroda adalah gerak senam lantai.', 'Smash dan servis bukan istilah senam.'),
        ('Manakah yang termasuk gerak keseimbangan?', ['Sikap lilin', 'Handstand'], ['Guling depan', 'Guling belakang'], 'Sikap lilin dan handstand menekankan keseimbangan.', 'Guling termasuk gerak berguling.'),
        ('Apa manfaat senam lantai?', ['Melatih kelenturan', 'Melatih keseimbangan'], ['Meningkatkan tinggi badan secara instan', 'Menghilangkan kebutuhan pemanasan'], 'Senam melatih kelenturan dan keseimbangan.', 'Pemanasan tetap diperlukan.'),
        ('Manakah ciri guling depan yang benar?', ['Dagu menempel dada', 'Tengkuk menyentuh matras'], ['Dahi menyentuh matras lebih dulu', 'Leher ditegangkan'], 'Guling depan membulatkan tubuh dengan tengkuk di matras.', 'Dahi tidak boleh menjadi tumpuan.'),
        ('Manakah yang termasuk perlengkapan keselamatan senam?', ['Matras', 'Spotting'], ['Lantai keramik', 'Sepatu roda'], 'Matras dan spotting membantu keselamatan senam.', 'Lantai keramik dan sepatu roda berbahaya.'),
        ('Manakah prinsip latihan senam yang benar?', ['Bertahap dari mudah ke sulit', 'Minta bantuan saat gerakan sulit'], ['Langsung melakukan gerakan tersulit', 'Mengabaikan rasa nyeri'], 'Latihan senam harus bertahap dan meminta bantuan.', 'Keselamatan harus diutamakan.'),
        ('Manakah pernyataan yang benar tentang handstand?', ['Bertumpu pada kedua tangan', 'Tubuh lurus dan kaki rapat'], ['Bertumpu pada kepala', 'Tubuh membungkuk ke depan'], 'Handstand bertumpu pada tangan dengan tubuh lurus.', 'Headstand bertumpu pada kepala.'),
        ('Manakah pernyataan yang benar tentang meroda?', ['Berputar ke samping', 'Tangan dan kaki bergantian menyentuh matras'], ['Berputar ke belakang', 'Hanya memakai satu tangan'], 'Meroda berputar ke samping dengan tumpuan bergantian.', 'Gerakan ini membutuhkan koordinasi.'),
    ],
    'pairs': [
        ('Guling depan', 'berguling ke depan dengan tubuh membulat'),
        ('Guling belakang', 'berguling ke belakang dengan tangan menopang'),
        ('Sikap lilin', 'berdiri di atas bahu dengan kaki ke atas'),
        ('Kayang', 'melengkungkan badan ke belakang'),
        ('Meroda', 'berputar ke samping'),
        ('Handstand', 'berdiri dengan kedua tangan'),
        ('Headstand', 'berdiri dengan kepala dan tangan'),
        ('Spotting', 'bantuan pengaman saat senam'),
    ],
    'steps': [
        ('Urutkan langkah melakukan guling depan.', ['Ambil posisi jongkok', 'Letakkan tangan di matras', 'Masukkan kepala dengan dagu ke dada', 'Berguling dan kembali berdiri'], 'Guling depan dimulai dari jongkok lalu berguling dengan tubuh membulat.', 'Tengkuk menyentuh matras lebih dulu.'),
        ('Urutkan langkah melakukan guling belakang.', ['Ambil posisi jongkok membelakangi matras', 'Letakkan tangan di samping kepala', 'Dorong tubuh ke belakang', 'Berguling dan kembali berdiri'], 'Guling belakang memakai tangan untuk menopang saat berguling.', 'Jaga leher agar tidak terbebani.'),
        ('Urutkan langkah melakukan sikap lilin.', ['Berbaring telentang', 'Angkat kedua kaki ke atas', 'Topang pinggang dengan siku', 'Luruskan kaki dan tahan posisi'], 'Sikap lilin bertumpu pada bahu dengan pinggang ditopang siku.', 'Pandangan ke arah kaki.'),
        ('Urutkan langkah melakukan handstand dengan bantuan.', ['Berdiri menghadap matras', 'Letakkan kedua tangan di matras', 'Tolak kaki ke atas dengan bantuan spotting', 'Rapatkan kaki dan tahan posisi'], 'Handstand membutuhkan tumpuan tangan dan bantuan pengaman.', 'Jaga siku tetap lurus.'),
        ('Urutkan alur latihan senam yang aman.', ['Pemanasan', 'Latihan gerak dasar', 'Latihan dengan spotting', 'Pendinginan'], 'Latihan senam dimulai dari pemanasan dan diakhiri pendinginan.', 'Jangan langsung mencoba gerakan sulit.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
