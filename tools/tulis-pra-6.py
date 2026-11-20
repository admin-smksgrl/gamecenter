"""PRA 6 — Alat Penyiram Tanaman Otomatis (Kelas X, Fase E)."""
from prakarya_common import (
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    write_chapter,
)

CH = {
    'code': 'PRA 6',
    'slug': 'prakarya-6-penyiram-otomatis',
    'title': 'Alat Penyiram Tanaman Otomatis',
    'description': (
        'Merancang alat penyiram tanaman otomatis: mengenal kelompok tanaman, '
        'teknik penyiraman, sumber air, timer, sensor soil moisture, dan Arduino Uno.'
    ),
    'objectives': [
        'Mengamati kondisi budi daya tanaman dan jenis tanamannya.',
        'Mengeksplorasi teknik penyiraman dan sumber air di lingkungan sekitar.',
        'Merancang rangkaian alat penyiram tanaman otomatis.',
        'Membuat dan menguji alat penyiram tanaman otomatis.',
        'Mengevaluasi produk serta menghitung harga pokok produksi.',
    ],
    'minutes': 135,
    'source': 'Prakarya-Rekayasa-BG-KLS-X.pdf Unit 3 Alat Penyiram Tanaman Otomatis',
    'glossary': [
        {'term': 'Hidrofit', 'definition': 'Tanaman yang hidup di air, seperti eceng gondok dan teratai.'},
        {'term': 'Higrofit', 'definition': 'Tanaman yang hidup di tempat lembap, seperti lumut dan tanaman paku.'},
        {'term': 'Xerofit', 'definition': 'Tanaman yang hidup di daerah kering, seperti kaktus dan lidah buaya.'},
        {'term': 'Soil moisture', 'definition': 'Sensor yang mengukur kadar air atau kelembapan tanah.'},
        {'term': 'Timer', 'definition': 'Pengatur waktu yang menyalakan atau mematikan alat secara terjadwal.'},
        {'term': 'Irigasi tetes', 'definition': 'Teknik penyiraman dengan meneteskan air langsung ke akar tanaman.'},
        {'term': 'Smart farm', 'definition': 'Sistem pertanian yang memakai alat otomatis dan sensor.'},
        {'term': 'Arduino Uno', 'definition': 'Papan mikrokontroler yang dapat diprogram untuk mengendalikan alat.'},
    ],
    'intro': {
        'material_title': 'Mengapa penyiraman perlu otomatis?',
        'title': 'Menjaga tanaman tetap terawat',
        'paragraphs': [
            'Penyiraman adalah kegiatan pemeliharaan tanaman yang penting. Air dibutuhkan untuk fotosintesis, menjaga kelembapan tanah, mengatur suhu tanaman, dan mendukung kesuburan. Tanpa air yang cukup, tanaman dapat layu bahkan mati.',
            'Penyiraman manual sering terlupa atau tidak tepat waktu. Untuk area yang luas, pekerjaan ini juga memakan waktu lama. Alat penyiram tanaman otomatis membantu mengubah pekerjaan manual menjadi otomatis sehingga lebih teratur, efektif, dan efisien.',
            'Alat sederhana dapat memakai timer keran air, sedangkan alat modern memakai sensor soil moisture dan Arduino Uno. Keduanya bertujuan mengatur jadwal penyiraman sesuai kebutuhan tanaman.',
        ],
        'diagram': (
            'Alur kerja penyiram tanaman otomatis',
            'flowchart LR\n'
            '  A[Waktu penyiraman tiba] --> B[Timer atau sensor aktif]\n'
            '  B --> C[Sistem memeriksa kelembapan]\n'
            '  C --> D[Pompa atau keran menyala]\n'
            '  D --> E[Air mengalir ke tanaman]\n'
            '  E --> F[Penyiraman berhenti sesuai jadwal]',
        ),
        'callout': 'Gunakan pompa dan sumber listrik yang sesuai. Jauhkan sambungan listrik dari air dan periksa selang sebelum alat dinyalakan.',
        'checkpoint': (
            'Apa tujuan utama penyiraman tanaman?',
            [
                ('Menjaga asupan air dan kelembapan tanah', True),
                ('Membuat daun menjadi kering', False),
                ('Menambah jumlah hama', False),
                ('Menghentikan fotosintesis', False),
            ],
            'Penyiraman menjaga asupan air, kelembapan tanah, suhu, dan kesuburan tanaman.',
        ),
    },
    'concept': {
        'material_title': 'Kelompok tanaman dan teknik penyiraman',
        'title': 'Menyiram sesuai jenis tanaman',
        'paragraphs': [
            'Berdasarkan kebutuhan airnya, tanaman dikelompokkan menjadi hidrofit, higrofit, dan xerofit. Hidrofit hidup di air, higrofit di tempat lembap, sedangkan xerofit tahan hidup di daerah kering. Kelompok tanaman menentukan banyaknya air yang diberikan.',
            'Penyiraman terbaik dilakukan pagi hari sebelum matahari terik agar air tidak cepat menguap. Jika menyiram sore hari, jaga daun tetap kering karena kelembapan tinggi pada malam hari dapat memicu jamur.',
            'Sumber air dapat berasal dari mata air, air hujan, air sungai, dan waduk. Teknik penyiraman meliputi penyiraman di permukaan, di dalam tanah, penyemprotan, dan sistem tetes. Pilih teknik yang sesuai dengan jenis tanaman dan kondisi tempat budi daya.',
        ],
        'table': [
            ['Kelompok', 'Ciri', 'Contoh'],
            ['Hidrofit', 'Hidup di air', 'Eceng gondok, teratai, kangkung'],
            ['Higrofit', 'Hidup di tempat lembap', 'Lumut, tanaman paku'],
            ['Xerofit', 'Tahan di daerah kering', 'Kaktus, kurma, lidah buaya'],
            ['Teknik tetes', 'Air menetes ke akar', 'Cocok untuk lahan kering'],
        ],
        'visual': chart_block(
            'pra-6-frekuensi-siram',
            'Perkiraan frekuensi penyiraman per minggu',
            'bar',
            [('Kaktus', 1), ('Lidah buaya', 2), ('Tanaman hias', 4), ('Sayuran', 7)],
        ),
        'activity': categorize_block(
            'pra-6-klasifikasi',
            'Kelompokkan tanaman berikut berdasarkan kebutuhan airnya.',
            [('b1', 'Hidrofit'), ('b2', 'Higrofit'), ('b3', 'Xerofit')],
            [
                ('i1', 'Eceng gondok', 'b1'),
                ('i2', 'Teratai', 'b1'),
                ('i3', 'Lumut', 'b2'),
                ('i4', 'Tanaman paku', 'b2'),
                ('i5', 'Kaktus', 'b3'),
                ('i6', 'Lidah buaya', 'b3'),
            ],
            'Tepat. Eceng gondok dan teratai hidrofit; lumut dan paku higrofit; kaktus dan lidah buaya xerofit.',
            'Periksa lagi: cocokkan tanaman dengan tempat hidup aslinya.',
        ),
        'subtitle': 'Komponen otomatis dan perawatan',
        'list': [
            'Timer mengatur jadwal penyalaan pompa atau keran secara berkala.',
            'Sensor soil moisture memberi masukan kadar air tanah kepada sistem.',
            'Arduino Uno memproses masukan sensor dan mengendalikan pompa.',
            'Periksa selang, sambungan, dan sumber air agar tidak bocor atau tersumbat.',
        ],
        'checkpoint': (
            'Alat penyiram tanaman otomatis modern memakai sensor…',
            [
                ('Soil moisture', True),
                ('Sensor suara', False),
                ('Sensor hujan', False),
                ('Sensor gerak', False),
            ],
            'Sensor soil moisture mengukur kelembapan tanah untuk menentukan penyiraman.',
        ),
    },
    'practice': {
        'material_title': 'Contoh dan latihan',
        'title': 'Merancang penyiram untuk taman sekolah',
        'paragraphs': [
            'Amati taman sekolah dan catat jenis tanamannya. Bedakan tanaman yang membutuhkan banyak air dari tanaman yang tahan kering. Ukur luas area dan tentukan letak sumber air agar selang tidak terlalu panjang.',
            'Rancang jadwal penyiraman. Jika memakai timer, atur waktu pagi hari. Jika memakai sensor soil moisture, tentukan ambang kelembapan sehingga pompa menyala hanya saat tanah kering.',
            'Rakit alat, uji aliran air, dan periksa apakah semua tanaman terjangkau. Hitung biaya bahan dan tenaga kerja, lalu presentasikan hasilnya beserta rencana perawatan.',
        ],
        'scenario': scenario(
            'pra-6-skenario',
            'Taman sekolah saat libur',
            'n1',
            [
                {
                    'id': 'n1',
                    'text': 'Tanaman taman sekolah sering layu saat libur karena tidak ada yang menyiram. Apa solusinya?',
                    'choices': [
                        {'text': 'Membuat penyiram otomatis dengan timer', 'next': 'n2', 'score': 2, 'feedback': 'Timer menjaga penyiraman tetap terjadwal saat libur.'},
                        {'text': 'Membiarkan tanaman sampai kering', 'next': 'n3', 'score': 0, 'feedback': 'Tanaman dapat mati jika tidak disiram.'},
                    ],
                },
                {
                    'id': 'n2',
                    'text': 'Tanah taman masih basah ketika jadwal penyiraman tiba. Apa yang sebaiknya dilakukan sistem?',
                    'choices': [
                        {'text': 'Menunda penyalaan pompa karena sensor mendeteksi lembap', 'next': 'n4', 'score': 2, 'feedback': 'Sensor mencegah penyiraman berlebihan.'},
                        {'text': 'Tetap menyiram sebanyak mungkin', 'next': 'n3', 'score': 0, 'feedback': 'Air berlebih dapat merusak akar.'},
                    ],
                },
                {'id': 'n3', 'text': 'Tanaman rusak karena penyiraman tidak tepat.', 'end': True, 'outcome': 'bad'},
                {'id': 'n4', 'text': 'Tanaman tetap sehat meski sekolah libur.', 'end': True, 'outcome': 'good'},
            ],
        ),
        'flashcards': [
            {'front': 'Sebutkan tiga kelompok tanaman berdasarkan kebutuhan air.', 'back': 'Hidrofit, higrofit, dan xerofit.'},
            {'front': 'Kapan waktu penyiraman terbaik?', 'back': 'Pagi hari sebelum matahari terik.'},
            {'front': 'Apa fungsi sensor soil moisture?', 'back': 'Mengukur kadar air atau kelembapan tanah.'},
            {'front': 'Apa itu irigasi tetes?', 'back': 'Penyiraman dengan meneteskan air langsung ke akar.'},
        ],
        'checkpoint': (
            'Mengapa penyiraman sebaiknya dilakukan pagi hari?',
            [
                ('Agar air tidak cepat menguap', True),
                ('Agar daun cepat kering', False),
                ('Agar tanah menjadi panas', False),
                ('Agar tanaman berhenti tumbuh', False),
            ],
            'Penyiraman pagi mengurangi penguapan dan membantu tanaman menyerap air.',
        ),
        'challenge': challenge_block(
            'pra-6-tantangan',
            'Tantangan istilah penyiram otomatis',
            90,
            [
                ('Tanaman hidup di air', 'hidrofit'),
                ('Tanaman hidup di tempat lembap', 'higrofit'),
                ('Tanaman tahan daerah kering', 'xerofit'),
                ('Sensor kelembapan tanah', 'soil moisture'),
                ('Penyiraman menetes ke akar', 'irigasi tetes'),
            ],
            'Lima istilah terjawab tepat.',
            'Ulangi istilah yang belum tepat, lalu coba lagi.',
        ),
    },
    'facts': [
        ('Apa tujuan utama penyiraman tanaman?', 'Menjaga asupan air dan kelembapan tanah', ['Mengeringkan daun', 'Menambah hama', 'Menghentikan fotosintesis'], 'Penyiraman menjaga air, kelembapan, suhu, dan kesuburan tanaman.', 'Air penting untuk fotosintesis.'),
        ('Tanaman yang hidup di air disebut…', 'Hidrofit', ['Higrofit', 'Xerofit', 'Tropofit'], 'Hidrofit adalah tanaman yang hidup di air.', 'Contohnya eceng gondok.'),
        ('Tanaman yang hidup di tempat lembap disebut…', 'Higrofit', ['Hidrofit', 'Xerofit', 'Tropofit'], 'Higrofit hidup di tempat lembap.', 'Contohnya lumut dan tanaman paku.'),
        ('Tanaman yang tahan hidup di daerah kering disebut…', 'Xerofit', ['Hidrofit', 'Higrofit', 'Tropofit'], 'Xerofit dapat hidup di daerah kering dan curah hujan rendah.', 'Contohnya kaktus.'),
        ('Manakah contoh hidrofit?', 'Eceng gondok', ['Kaktus', 'Lumut', 'Lidah buaya'], 'Eceng gondok hidup di air sehingga termasuk hidrofit.', 'Teratai juga hidrofit.'),
        ('Manakah contoh xerofit?', 'Kaktus', ['Teratai', 'Lumut', 'Eceng gondok'], 'Kaktus tahan hidup di daerah kering.', 'Lidah buaya juga xerofit.'),
        ('Waktu penyiraman terbaik adalah…', 'Pagi sebelum matahari terik', ['Tengah hari saat panas', 'Malam hari tanpa cahaya', 'Saat hujan deras'], 'Penyiraman pagi mencegah penguapan berlebihan.', 'Air lebih mudah diserap tanaman.'),
        ('Mengapa daun harus tetap kering saat menyiram sore hari?', 'Mencegah penyakit jamur', ['Agar warna daun berubah', 'Agar tanaman cepat layu', 'Agar air cepat menguap'], 'Kelembapan tinggi pada malam hari membuat daun basah mudah berjamur.', 'Jamur tumbuh pada kondisi lembap.'),
        ('Alat penyiram otomatis sederhana memakai…', 'Timer', ['Sensor suara', 'Sensor gerak', 'Sensor asap'], 'Timer mengatur jadwal penyalaan air.', 'Timer keran air mudah dipasang.'),
        ('Alat penyiram otomatis modern memakai sensor…', 'Soil moisture', ['Suara', 'Cahaya', 'Gas'], 'Sensor soil moisture mengukur kelembapan tanah.', 'Sensor ini mencegah penyiraman berlebihan.'),
        ('Mikrokontroler yang disebut dalam buku adalah…', 'Arduino Uno', ['Raspberry Pi', 'ESP32', 'Micro:bit'], 'Buku menyebut Arduino Uno sebagai pengendali sistem penyiraman.', 'Arduino Uno dapat diprogram.'),
        ('Teknik penyiraman dengan meneteskan air ke akar disebut…', 'Irigasi tetes', ['Penyemprotan', 'Penggenangan', 'Penyiraman permukaan'], 'Irigasi tetes meneteskan air langsung ke akar.', 'Teknik ini hemat air.'),
        ('Apa itu smart farm?', 'Sistem pertanian otomatis berbasis sensor', ['Kebun tanpa tanaman', 'Alat memasak', 'Pupuk cair'], 'Smart farm memakai alat otomatis dan sensor untuk merawat tanaman.', 'Tujuannya efisien dan teratur.'),
        ('Mengapa penyiraman manual sering bermasalah?', 'Terlupa dan tidak tepat waktu', ['Selalu berlebihan', 'Tidak membutuhkan air', 'Tidak memerlukan alat'], 'Penyiraman manual dapat terlupa dan memakan waktu lama.', 'Otomatisasi membantu mengatasinya.'),
    ],
    'multi': [
        ('Manakah kelompok tanaman berdasarkan kebutuhan air?', ['Hidrofit', 'Higrofit', 'Xerofit'], ['Tropofit', 'Akuafit'], 'Buku membagi tanaman menjadi hidrofit, higrofit, dan xerofit.', 'Istilah lain tidak dipakai dalam buku.'),
        ('Manakah contoh xerofit?', ['Kaktus', 'Kurma', 'Lidah buaya'], ['Eceng gondok', 'Teratai'], 'Kaktus, kurma, dan lidah buaya tahan di daerah kering.', 'Eceng gondok dan teratai hidup di air.'),
        ('Manakah sumber air penyiraman?', ['Mata air', 'Air hujan', 'Air sungai'], ['Air laut', 'Limbah pabrik'], 'Mata air, air hujan, dan air sungai dapat dipakai menyiram.', 'Air laut dan limbah pabrik tidak cocok.'),
        ('Manakah teknik penyiraman?', ['Penyiraman permukaan', 'Penyiraman dalam tanah', 'Irigasi tetes'], ['Pembakaran', 'Penimbunan'], 'Teknik penyiraman meliputi permukaan, dalam tanah, penyemprotan, dan tetes.', 'Pembakaran dan penimbunan bukan teknik penyiraman.'),
        ('Apa manfaat penyiraman otomatis?', ['Terjadwal', 'Efisien'], ['Selalu terlupa', 'Membuat tanaman kering'], 'Otomatisasi membuat penyiraman terjadwal dan efisien.', 'Pekerjaan manual berkurang.'),
        ('Manakah komponen sistem otomatis?', ['Timer', 'Sensor soil moisture', 'Pompa'], ['Gunting', 'Kuas'], 'Timer, sensor, dan pompa adalah komponen sistem penyiraman.', 'Gunting dan kuas bukan komponennya.'),
        ('Apa tujuan penyiraman tanaman?', ['Membantu fotosintesis', 'Menjaga kelembapan tanah'], ['Menambah hama', 'Mengeringkan daun'], 'Air membantu fotosintesis dan menjaga kelembapan tanah.', 'Penyiraman yang benar menjauhkan penyakit.'),
        ('Manakah tahap proyek penyiram otomatis?', ['Observasi', 'Desain', 'Produksi', 'Evaluasi'], ['Menghindari uji coba', 'Membuang bahan sembarangan'], 'Proyek melalui observasi, desain, produksi, dan evaluasi.', 'Uji coba memastikan alat bekerja.'),
    ],
    'pairs': [
        ('Hidrofit', 'tanaman yang hidup di air'),
        ('Higrofit', 'tanaman yang hidup di tempat lembap'),
        ('Xerofit', 'tanaman yang hidup di daerah kering'),
        ('Soil moisture', 'sensor kelembapan tanah'),
        ('Timer', 'pengatur jadwal penyalaan'),
        ('Irigasi tetes', 'air menetes langsung ke akar'),
        ('Smart farm', 'pertanian berbasis alat otomatis'),
        ('Arduino Uno', 'papan mikrokontroler yang diprogram'),
    ],
    'steps': [
        ('Urutkan alur proyek penyiram otomatis.', ['Observasi tanaman dan sumber air', 'Perancangan rangkaian', 'Persiapan alat dan bahan', 'Perakitan dan uji coba', 'Evaluasi produk'], 'Proyek bergerak dari observasi menuju evaluasi.', 'Rancangan dibuat sebelum perakitan.'),
        ('Urutkan langkah memasang penyiram dengan timer.', ['Siapkan keran dan selang', 'Pasang timer pada keran', 'Atur jadwal penyiraman', 'Uji aliran air'], 'Pemasangan dimulai dari penyiapan keran lalu pengaturan timer.', 'Uji aliran memastikan semua tanaman terjangkau.'),
        ('Urutkan langkah merakit sistem berbasis sensor.', ['Pasang sensor soil moisture', 'Hubungkan sensor ke Arduino', 'Hubungkan pompa ke rangkaian', 'Unggah program', 'Uji respons pompa'], 'Perakitan dimulai dari sensor lalu diuji melalui program.', 'Program mengatur kapan pompa menyala.'),
        ('Urutkan langkah merawat tanaman.', ['Periksa kelembapan tanah', 'Siram pada pagi hari', 'Jaga daun tetap kering', 'Amati pertumbuhan tanaman'], 'Perawatan dimulai dari pemeriksaan lalu penyiraman dan pengamatan.', 'Pengamatan mendeteksi masalah lebih awal.'),
        ('Urutkan langkah evaluasi produk.', ['Uji jadwal penyiraman', 'Periksa kebocoran selang', 'Nilai efisiensi air', 'Catat perbaikan yang diperlukan'], 'Evaluasi menguji jadwal, kebocoran, dan efisiensi.', 'Hasil evaluasi menjadi dasar perbaikan.'),
    ],
}

if __name__ == '__main__':
    write_chapter(CH)
