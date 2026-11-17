"""Fase 5.1 batch 9 — blok interaktif untuk BI 1 sampai BI 5.

Jalankan dari folder gamecenter:

    python ../tools/tambah-blok-fase5-b9.py
    python ../tools/rapikan-blok-fase5.py --apply
    php artisan gamecenter:materi-import
"""
import io
import json

BASE = 'database/seeders/data/sma-smk/fase-e/bahasa-indonesia/'


def load(path):
    return json.load(io.open(BASE + path, encoding='utf-8'))


def save(path, data):
    io.open(BASE + path, 'w', encoding='utf-8').write(
        json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    )


def add_blocks(data, index, blocks):
    material = data['chapters'][0]['materials'][index]
    material['blocks'] = (material.get('blocks') or []) + blocks
    return material


# ── BI 1 — Laporan Hasil Observasi ────────────────────────────────────
path = 'bi-1-laporan-hasil-observasi.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-bi1-struktur", "engine": "mermaid",
     "title": "Struktur laporan hasil observasi",
     "code": "flowchart TD\n  A[Pernyataan umum: pengenalan objek] --> B[Deskripsi bagian: rincian per bagian]\n  B --> C[Simpulan: ringkasan pokok pengamatan]"},
    {"type": "glossary", "terms": [
        {"term": "Laporan hasil observasi", "definition": "Teks yang menyajikan hasil pengamatan terhadap suatu objek secara sistematis, objektif, dan faktual."},
        {"term": "Objektif", "definition": "Menggambarkan kenyataan apa adanya tanpa memasukkan pendapat pribadi."},
        {"term": "Faktual", "definition": "Berdasarkan fakta yang dapat diverifikasi."},
        {"term": "Opini", "definition": "Pernyataan berupa penilaian yang tidak dapat diverifikasi seperti fakta."},
    ]},
    {"type": "checkpoint", "id": "cp-bi1-ciri",
     "question": "Ciri bahasa laporan hasil observasi adalah…",
     "choices": [
         {"id": "a", "text": "Objektif, faktual, dan memakai istilah teknis", "correct": True},
         {"id": "b", "text": "Penuh pendapat pribadi dan kata “sebaiknya”"},
         {"id": "c", "text": "Menggunakan cerita khayalan"},
     ],
     "explanation": "Laporan hasil observasi bersifat objektif dan faktual serta memakai istilah teknis agar makna tepat. Kata seperti “sebaiknya” menandai opini yang perlu dipindahkan ke teks lain."},
    {"type": "categorize", "id": "cat-bi1-fakta-opini",
     "prompt": "Kelompokkan pernyataan berikut ke dalam fakta atau opini.",
     "buckets": [
         {"id": "fakta", "label": "Fakta"},
         {"id": "opini", "label": "Opini"},
     ],
     "items": [
         {"id": "f1", "text": "Bus berangkat pukul 06.00", "bucket": "fakta"},
         {"id": "f2", "text": "Mangrove tumbuh di daerah pasang surut pantai", "bucket": "fakta"},
         {"id": "f3", "text": "Bus itu paling nyaman", "bucket": "opini"},
         {"id": "f4", "text": "Pemerintah seharusnya lebih peduli pada komodo", "bucket": "opini"},
     ],
     "feedback": {
         "correct": "Benar — fakta dapat diverifikasi, opini berupa penilaian.",
         "wrong": "Fakta dapat diverifikasi; opini berisi penilaian atau saran.",
     }},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-bi1-akurasi",
     "prompt": "Urutkan tiga hal yang diperiksa untuk menilai akurasi laporan.",
     "items": [
         {"id": "s1", "text": "Sumber data — disebut atau tidak"},
         {"id": "s2", "text": "Kelengkapan angka — jumlahnya jelas atau tidak"},
         {"id": "s3", "text": "Konsistensi — simpulan sejalan dengan isi sebelumnya"},
     ],
     "answer": ["s1", "s2", "s3"],
     "feedback": {
         "correct": "Benar — periksa sumber data, kelengkapan angka, lalu konsistensi simpulan.",
         "wrong": "Urutannya: sumber data, kelengkapan angka, dan konsistensi simpulan.",
     }},
    {"type": "checkpoint", "id": "cp-bi1-bias",
     "question": "Kalimat “Kantin sekolah selalu lebih baik dari semua kantin mana pun” termasuk…",
     "choices": [
         {"id": "a", "text": "Bias berupa generalisasi tanpa dasar data", "correct": True},
         {"id": "b", "text": "Fakta yang dapat diverifikasi"},
         {"id": "c", "text": "Simpulan berdasarkan angka lengkap"},
     ],
     "explanation": "Kalimat itu generalisasi tanpa dasar data. Bias muncul ketika penulis hanya memilih data yang mendukung pandangannya."},
    {"type": "checkpoint", "id": "cp-bi1-eksplanasi",
     "question": "Teks yang menjelaskan proses sebab-akibat suatu fenomena adalah…",
     "choices": [
         {"id": "a", "text": "Teks eksplanasi", "correct": True},
         {"id": "b", "text": "Teks negosiasi"},
         {"id": "c", "text": "Teks anekdot"},
     ],
     "explanation": "Teks eksplanasi menjawab “mengapa terjadi”, sedangkan laporan hasil observasi memaparkan objek dan menjawab “apa dan bagaimana”."},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-bi1-visual",
     "question": "Data “60% sampah sekolah adalah plastik” paling jelas disajikan dengan…",
     "choices": [
         {"id": "a", "text": "Diagram lingkaran disertai keterangan jumlah sampel", "correct": True},
         {"id": "b", "text": "Cerita khayalan"},
         {"id": "c", "text": "Daftar tanpa angka"},
     ],
     "explanation": "Data proporsi paling tepat disajikan sebagai diagram lingkaran, disertai keterangan jumlah sampel agar dapat diverifikasi."},
    {"type": "scenario", "id": "sc-bi1-presentasi",
     "title": "Presentasi laporan hasil observasi",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu mempresentasikan laporan observasi kantin. Seorang teman bertanya tentang jumlah sampel yang kamu pakai. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menjawab berdasarkan data yang tercatat", "next": "n2", "score": 2,
               "feedback": "Presentasi yang baik menjawab pertanyaan berdasarkan data, bukan dugaan."},
              {"text": "Mengarang angka agar terlihat meyakinkan", "next": "n3", "score": 0,
               "feedback": "Mengarang data memanipulasi informasi dan merusak kepercayaan."},
              {"text": "Mengalihkan pembicaraan ke hal lain", "next": "n4", "score": 1,
               "feedback": "Mengalihkan pertanyaan menghindari masalah, tetapi tidak menjelaskan data."},
          ]},
         {"id": "n2", "text": "Guru menilai laporanmu masih memuat kalimat opini. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Memindahkan kalimat opini ke teks opini dan mempertahankan fakta", "next": "n5", "score": 2,
               "feedback": "Laporan hasil observasi harus objektif; opini dipindahkan, fakta tetap dijaga."},
              {"text": "Menghapus semua kalimat agar aman", "next": "n6", "score": 0,
               "feedback": "Menghapus semua kalimat menghilangkan data dan merusak laporan."},
          ]},
         {"id": "n3", "text": "Temanmu menanyakan sumber angka. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui angka belum tercatat dan memperbaikinya", "next": "n5", "score": 1,
               "feedback": "Mengakui dan memperbaiki data lebih baik daripada mempertahankan angka karangan."},
              {"text": "Tetap memakai angka itu karena presentasi sudah berjalan", "next": "n7", "score": 0,
               "feedback": "Mempertahankan data tanpa sumber membuat laporan tidak dapat dipercaya."},
          ]},
         {"id": "n4", "text": "Selesai presentasi, guru meminta perbaikan. Apa langkahmu?",
          "choices": [
              {"text": "Melengkapi sumber, angka, dan konsistensi simpulan", "next": "n5", "score": 2,
               "feedback": "Memperbaiki sumber, kelengkapan angka, dan konsistensi adalah cara menilai akurasi."},
              {"text": "Mengubah topik laporan agar tidak diperiksa", "next": "n7", "score": 0,
               "feedback": "Mengganti topik menghindari perbaikan yang seharusnya dilakukan."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Laporan menjadi akurat dan objektif. Presentasimu dijawab berdasarkan data, bukan dugaan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Laporan bersih dari opini, tetapi data penting ikut hilang. Perbaiki dengan memindahkan, bukan menghapus."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Laporan kehilangan kepercayaan karena data tidak dapat diverifikasi."},
     ]},
    {"type": "challenge", "id": "ch-bi1-laporan",
     "title": "Tantangan Kilat: Laporan Hasil Observasi",
     "time_limit": 90,
     "items": [
         {"question": "Teks hasil pengamatan sistematis dan faktual disebut laporan hasil…", "answer": "observasi"},
         {"question": "Bagian yang mengenalkan objek secara umum disebut pernyataan…", "answer": "umum"},
         {"question": "Bagian berisi rincian objek per bagian disebut deskripsi…", "answer": "bagian"},
         {"question": "Pernyataan berupa penilaian disebut…", "answer": "opini"},
         {"question": "Data proporsi paling jelas disajikan dengan diagram…", "answer": "lingkaran"},
         {"question": "Teks yang menjelaskan sebab-akibat disebut teks…", "answer": "eksplanasi"},
     ],
     "feedback": {
         "correct": "Tepat — laporan yang baik objektif, faktual, dan sumbernya jelas.",
         "wrong": "Ingat struktur laporan, ciri fakta/opini, dan jenis grafik untuk data proporsi.",
     }},
])
save(path, data)

# ── BI 2 — Kritik Sosial lewat Anekdot ────────────────────────────────
path = 'bi-2-kritik-sosial-anekdot.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Anekdot", "definition": "Cerita singkat lucu yang menyindir dan menyampaikan kritik sosial."},
        {"term": "Eksposisi", "definition": "Teks yang menyampaikan gagasan disertai alasan dan bukti."},
        {"term": "Stand up comedy", "definition": "Lawakan tunggal yang berisi kritik sosial."},
        {"term": "Koda", "definition": "Penutup anekdot yang berisi pesan atau simpulan."},
    ]},
    {"type": "sort", "id": "srt-bi2-struktur",
     "prompt": "Urutkan struktur anekdot.",
     "items": [
         {"id": "s1", "text": "Orientasi — pengenalan tokoh dan situasi"},
         {"id": "s2", "text": "Komplikasi — masalah atau kejadian tak terduga"},
         {"id": "s3", "text": "Koda — penutup berisi pesan atau simpulan"},
     ],
     "answer": ["s1", "s2", "s3"],
     "feedback": {
         "correct": "Benar — orientasi, komplikasi, lalu koda.",
         "wrong": "Urutannya: orientasi, komplikasi, dan koda.",
     }},
    {"type": "checkpoint", "id": "cp-bi2-humor",
     "question": "Mengapa anekdot memakai humor?",
     "choices": [
         {"id": "a", "text": "Agar pesan kritik lebih mudah diterima tanpa konfrontasi langsung", "correct": True},
         {"id": "b", "text": "Agar kritik tidak perlu memiliki pesan"},
         {"id": "c", "text": "Agar pembaca tidak memahami isinya"},
     ],
     "explanation": "Humor menarik perhatian lebih dulu sehingga pesan kritik lebih mudah diterima. Anekdot yang baik membuat pembaca langsung menangkap pesan kritiknya."},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-bi2-kritik", "engine": "mermaid",
     "title": "Kritik, celaan, dan ancaman",
     "code": "flowchart LR\n  A[Kritik] --> A1[Disertai alasan]\n  A1 --> A2[Bertujuan memperbaiki]\n  B[Celaan] --> B1[Hanya menyerang]\n  C[Ancaman] --> C1[Menekan pihak lain]"},
    {"type": "categorize", "id": "cat-bi2-fakta-opini",
     "prompt": "Kelompokkan pernyataan berikut ke dalam fakta atau opini.",
     "buckets": [
         {"id": "fakta", "label": "Fakta"},
         {"id": "opini", "label": "Opini"},
     ],
     "items": [
         {"id": "f1", "text": "Antrean rata-rata 45 menit", "bucket": "fakta"},
         {"id": "f2", "text": "Jumlah keluhan naik 30 persen", "bucket": "fakta"},
         {"id": "f3", "text": "Pelayanan di kantor itu sangat buruk", "bucket": "opini"},
         {"id": "f4", "text": "Petugas seharusnya lebih ramah", "bucket": "opini"},
     ],
     "feedback": {
         "correct": "Benar — angka dan kejadian terukur adalah fakta; penilaian dan saran adalah opini.",
         "wrong": "Penanda opini antara lain sebaiknya, seharusnya, sangat, buruk, dan terbaik.",
     }},
    {"type": "checkpoint", "id": "cp-bi2-kritik",
     "question": "Pernyataan “Petugasnya semuanya tidak becus” termasuk…",
     "choices": [
         {"id": "a", "text": "Celaan karena hanya menyerang", "correct": True},
         {"id": "b", "text": "Kritik karena disertai alasan"},
         {"id": "c", "text": "Fakta karena menyebut petugas"},
     ],
     "explanation": "Kritik disertai alasan dan bertujuan memperbaiki; celaan hanya menyerang. Kalimat itu menyerang tanpa alasan."},
    {"type": "checkpoint", "id": "cp-bi2-aural",
     "question": "Menyimak melalui pendengaran, misalnya saat menyimak lawakan tunggal, disebut menyimak…",
     "choices": [
         {"id": "a", "text": "Aural", "correct": True},
         {"id": "b", "text": "Visual"},
         {"id": "c", "text": "Skimming"},
     ],
     "explanation": "Menyimak aural berarti melalui pendengaran. Pada teks visual, pesan dibangun oleh perpaduan gambar dan kata."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-bi2-menyusun",
     "prompt": "Urutkan langkah menyusun anekdot.",
     "items": [
         {"id": "s1", "text": "Pilih masalah sosial nyata"},
         {"id": "s2", "text": "Susun cerita singkat dengan tokoh dan latar"},
         {"id": "s3", "text": "Tambahkan kelucuan pada bagian komplikasi"},
         {"id": "s4", "text": "Tutup dengan koda berisi pesan kritik"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — pilih masalah, susun cerita, tambahkan kelucuan, lalu tutup dengan koda.",
         "wrong": "Mulai dari memilih masalah sosial nyata, lalu menyusun cerita dan komplikasi.",
     }},
    {"type": "scenario", "id": "sc-bi2-kritik",
     "title": "Menyampaikan kritik tentang antrean kantin",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu kesal karena antrean kantin sangat panjang. Kamu ingin menyampaikan kritik di media sosial sekolah. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menulis kritik santun disertai data dan usulan perbaikan", "next": "n2", "score": 2,
               "feedback": "Kritik yang baik disertai alasan, data, dan tujuan memperbaiki."},
              {"text": "Menulis celaan terhadap petugas kantin", "next": "n3", "score": 0,
               "feedback": "Celaan hanya menyerang dan tidak membantu perbaikan."},
              {"text": "Menyebarkan keluhan tanpa data agar cepat viral", "next": "n4", "score": 1,
               "feedback": "Keluhan tanpa data mudah dibantah dan tidak memberi solusi."},
          ]},
         {"id": "n2", "text": "Ada teman yang membalas dengan kata kasar. Apa sikapmu?",
          "choices": [
              {"text": "Membalas dengan santun dan mengajak fokus pada solusi", "next": "n5", "score": 2,
               "feedback": "Kritik sosial dijaga dengan bahasa santun dan fokus pada perbaikan."},
              {"text": "Membalas dengan kata kasar yang lebih keras", "next": "n6", "score": 0,
               "feedback": "Membalas kasar mengubah kritik menjadi konflik."},
          ]},
         {"id": "n3", "text": "Petugas kantin membaca unggahanmu dan merasa tersinggung. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Meminta maaf dan menyampaikan kritik dengan alasan", "next": "n2", "score": 1,
               "feedback": "Meminta maaf lalu menyampaikan alasan memulihkan hubungan."},
              {"text": "Membiarkan karena merasa berhak mengkritik", "next": "n7", "score": 0,
               "feedback": "Kritik tetap harus santun dan tidak menyerang pribadi."},
          ]},
         {"id": "n4", "text": "Guru menyarankan membuat anekdot agar pesannya lebih diterima. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menyusun anekdot dengan koda berisi kritik yang jelas", "next": "n5", "score": 2,
               "feedback": "Anekdot membuat kritik lebih mudah diterima tanpa konfrontasi langsung."},
              {"text": "Menambahkan tuduhan tanpa sumber agar lebih lucu", "next": "n7", "score": 0,
               "feedback": "Tuduhan tanpa sumber merusak kredibilitas dan dapat merugikan orang lain."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kritikmu disampaikan dengan santun dan data. Petugas menanggapi dan antrean mulai diperbaiki."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Pesan kritikmu sampai, tetapi caranya membuat suasana memanas. Perbaiki dengan bahasa santun."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Kritik berubah menjadi konflik. Orang menolak pesan karena caranya menyerang."},
     ]},
    {"type": "challenge", "id": "ch-bi2-anekdot",
     "title": "Tantangan Kilat: Anekdot dan Kritik Sosial",
     "time_limit": 90,
     "items": [
         {"question": "Cerita singkat lucu yang menyindir disebut…", "answer": "anekdot"},
         {"question": "Bagian pengenalan tokoh dan situasi disebut…", "answer": "orientasi"},
         {"question": "Bagian masalah atau kejadian tak terduga disebut…", "answer": "komplikasi"},
         {"question": "Penutup berisi pesan kritik disebut…", "answer": "koda"},
         {"question": "Kritik yang hanya menyerang disebut…", "answer": "celaan"},
         {"question": "Menyimak melalui pendengaran disebut menyimak…", "answer": "aural"},
     ],
     "feedback": {
         "correct": "Tepat — anekdot mengkritik lewat humor, bukan celaan.",
         "wrong": "Ingat struktur anekdot dan bedakan kritik, celaan, serta ancaman.",
     }},
])
save(path, data)

# ── BI 3 — Hikayat dan Cerpen ─────────────────────────────────────────
path = 'bi-3-hikayat-cerpen.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-bi3-banding", "engine": "mermaid",
     "title": "Hikayat dan cerpen: dua zaman, dua ciri",
     "code": "flowchart LR\n  A[Hikayat] --> A1[Sastra lama Melayu]\n  A --> A2[Kata arkais]\n  A --> A3[Kesaktian dan keajaiban]\n  B[Cerpen] --> B1[Cerita pendek modern]\n  B --> B2[Bahasa masa kini]\n  B --> B3[Konflik batin dan realisme]"},
    {"type": "glossary", "terms": [
        {"term": "Hikayat", "definition": "Karya sastra lama Melayu yang menceritakan kesaktian dan keajaiban."},
        {"term": "Kata arkais", "definition": "Kata lama yang sudah jarang dipakai, seperti alkisah, syahdan, dan hatta."},
        {"term": "Cerpen", "definition": "Cerita pendek modern yang memusatkan cerita pada satu peristiwa utama dengan tokoh terbatas."},
        {"term": "Amanat", "definition": "Pesan moral yang ingin disampaikan cerita kepada pembaca."},
    ]},
    {"type": "checkpoint", "id": "cp-bi3-arkais",
     "question": "Kata “alkisah”, “syahdan”, dan “hatta” merupakan contoh…",
     "choices": [
         {"id": "a", "text": "Kata arkais dalam hikayat", "correct": True},
         {"id": "b", "text": "Kata serapan modern dalam cerpen"},
         {"id": "c", "text": "Istilah teknis laporan"},
     ],
     "explanation": "Hikayat banyak memakai kata arkais, yaitu kata lama yang sudah jarang dipakai. Cerpen modern memakai bahasa masa kini."},
    {"type": "categorize", "id": "cat-bi3-ciri",
     "prompt": "Kelompokkan ciri berikut ke dalam hikayat atau cerpen.",
     "buckets": [
         {"id": "hikayat", "label": "Hikayat"},
         {"id": "cerpen", "label": "Cerpen"},
     ],
     "items": [
         {"id": "h1", "text": "Sastra lama Melayu", "bucket": "hikayat"},
         {"id": "h2", "text": "Kesaktian dan keajaiban", "bucket": "hikayat"},
         {"id": "h3", "text": "Kata arkais", "bucket": "hikayat"},
         {"id": "c1", "text": "Cerita pendek modern", "bucket": "cerpen"},
         {"id": "c2", "text": "Konflik batin dan realisme", "bucket": "cerpen"},
         {"id": "c3", "text": "Fokus pada satu peristiwa", "bucket": "cerpen"},
     ],
     "feedback": {
         "correct": "Benar — hikayat berciri sastra lama dan kesaktian, cerpen berciri modern dan realisme.",
         "wrong": "Hikayat: sastra lama, kata arkais, kesaktian. Cerpen: modern, konflik batin, satu peristiwa.",
     }},
])

add_blocks(data, 1, [
    {"type": "checkpoint", "id": "cp-bi3-karakterisasi",
     "question": "“Dengan tangan gemetar ia menyerahkan seluruh bekalnya kepada pengemis itu.” Watak tokoh disampaikan secara…",
     "choices": [
         {"id": "a", "text": "Tidak langsung, melalui tindakan", "correct": True},
         {"id": "b", "text": "Langsung, melalui penjelasan penulis"},
         {"id": "c", "text": "Melalui daftar kata sifat"},
     ],
     "explanation": "Karakterisasi tidak langsung membuat pembaca menyimpulkan watak dari tindakan, dialog, atau penilaian tokoh lain."},
    {"type": "sort", "id": "srt-bi3-plot",
     "prompt": "Urutkan bagian plot cerita.",
     "items": [
         {"id": "s1", "text": "Orientasi — pengenalan"},
         {"id": "s2", "text": "Komplikasi — munculnya konflik"},
         {"id": "s3", "text": "Klimaks — puncak ketegangan"},
         {"id": "s4", "text": "Resolusi — penyelesaian"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — orientasi, komplikasi, klimaks, lalu resolusi.",
         "wrong": "Plot bergerak dari orientasi ke komplikasi, klimaks, dan resolusi.",
     }},
    {"type": "checkpoint", "id": "cp-bi3-antagonis",
     "question": "Tokoh yang menentang jalannya cerita dan menciptakan konflik disebut…",
     "choices": [
         {"id": "a", "text": "Antagonis", "correct": True},
         {"id": "b", "text": "Protagonis"},
         {"id": "c", "text": "Narator"},
     ],
     "explanation": "Protagonis mendukung jalannya cerita, sedangkan antagonis menentangnya dan menciptakan konflik."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-bi3-menulis",
     "prompt": "Urutkan langkah menulis fiksi dari nilai hikayat.",
     "items": [
         {"id": "s1", "text": "Pilih nilai kehidupan dari hikayat"},
         {"id": "s2", "text": "Tentukan tokoh dan latar masa kini"},
         {"id": "s3", "text": "Susun alur konflik yang mencerminkan nilai itu"},
         {"id": "s4", "text": "Tutup dengan penyelesaian yang bermakna"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — pilih nilai, tentukan tokoh dan latar, susun konflik, lalu beri penyelesaian.",
         "wrong": "Mulai dari memilih nilai kehidupan, lalu tokoh dan latar masa kini.",
     }},
    {"type": "scenario", "id": "sc-bi3-publikasi",
     "title": "Mempublikasikan cerpen di media digital",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu menulis cerpen berdasarkan nilai hikayat. Teman menawarkan mengunggahnya di akun komunitas tanpa mencantumkan namamu. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Memastikan nama penulis tetap dicantumkan", "next": "n2", "score": 2,
               "feedback": "Publikasi digital harus menghormati karya sendiri; nama penulis tetap dicantumkan."},
              {"text": "Membiarkan tanpa nama agar cepat dipublikasikan", "next": "n3", "score": 0,
               "feedback": "Membiarkan karya tanpa nama membuka peluang klaim oleh orang lain."},
              {"text": "Menolak semua publikasi digital", "next": "n4", "score": 1,
               "feedback": "Menolak semua membuat karya tidak dikenal, padahal publikasi digital boleh dilakukan dengan aman."},
          ]},
         {"id": "n2", "text": "Seseorang menyalin cerpenmu dan mengaku sebagai penulisnya. Apa langkahmu?",
          "choices": [
              {"text": "Menunjukkan bukti karyamu dan melaporkan pelanggaran hak cipta", "next": "n5", "score": 2,
               "feedback": "Karya sendiri dilindungi; bukti dan pelaporan yang benar menjaga hak cipta."},
              {"text": "Membalas dengan menyalin karya orang lain juga", "next": "n6", "score": 0,
               "feedback": "Membalas dengan pelanggaran baru tidak menyelesaikan masalah."},
          ]},
         {"id": "n3", "text": "Cerpenmu viral, tetapi namamu tidak disebut. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menghubungi pengunggah dan meminta nama penulis dicantumkan", "next": "n5", "score": 1,
               "feedback": "Meminta pencantuman nama adalah langkah tepat sebelum menempuh jalur lain."},
              {"text": "Diam saja karena yang penting karya dibaca", "next": "n7", "score": 0,
               "feedback": "Diam membiarkan hak penulis diabaikan dan berpotensi diulang."},
          ]},
         {"id": "n4", "text": "Guru menawarkan membantu publikasi yang aman. Apa jawabmu?",
          "choices": [
              {"text": "Menerima dan mempelajari cara menjaga hak cipta", "next": "n5", "score": 2,
               "feedback": "Publikasi aman tetap menjaga karya sendiri dan tidak melanggar hak cipta."},
              {"text": "Menolak karena takut karyanya dinilai", "next": "n6", "score": 1,
               "feedback": "Takut dinilai membuat karya tidak berkembang; publikasi bisa dimulai dengan aman."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Cerpenmu terbit dengan nama penulis yang jelas. Alih wahana mengubah bentuk penyajian, bukan isi cerita."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Karya belum terbit atau masalah belum tuntas, tetapi kamu masih punya kesempatan memperbaikinya."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Nama penulis hilang dan karyamu berisiko diklaim orang lain. Hak cipta perlu dijaga sejak awal."},
     ]},
    {"type": "challenge", "id": "ch-bi3-sastra",
     "title": "Tantangan Kilat: Hikayat dan Cerpen",
     "time_limit": 90,
     "items": [
         {"question": "Karya sastra lama Melayu yang menceritakan kesaktian disebut…", "answer": "hikayat"},
         {"question": "Kata lama seperti alkisah dan hatta disebut kata…", "answer": "arkais"},
         {"question": "Pesan moral dalam cerita disebut…", "answer": "amanat"},
         {"question": "Bagian plot berisi puncak ketegangan disebut…", "answer": "klimaks"},
         {"question": "Tokoh yang menentang jalannya cerita disebut…", "answer": "antagonis"},
         {"question": "Latar yang menggambarkan keadaan perasaan disebut latar…", "answer": "suasana"},
     ],
     "feedback": {
         "correct": "Tepat — hikayat dan cerpen sama-sama menyimpan nilai yang bisa relevan hari ini.",
         "wrong": "Ingat: hikayat, kata arkais, amanat, klimaks, antagonis, dan latar suasana.",
     }},
])
save(path, data)

# ── BI 4 — Teks Negosiasi ─────────────────────────────────────────────
path = 'bi-4-teks-negosiasi.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Negosiasi", "definition": "Proses tawar-menawar untuk mencapai kesepakatan yang menguntungkan kedua pihak."},
        {"term": "Debat", "definition": "Pertukaran argumen untuk mencari kemenangan, bukan kesepakatan."},
        {"term": "Kompromi", "definition": "Kesediaan kedua pihak saling mengurangi tuntutan agar kepentingan bertemu."},
    ]},
    {"type": "sort", "id": "srt-bi4-struktur",
     "prompt": "Urutkan struktur teks negosiasi.",
     "items": [
         {"id": "s1", "text": "Orientasi — pembuka dan penyampaian maksud"},
         {"id": "s2", "text": "Pengajuan — penawaran awal"},
         {"id": "s3", "text": "Penawaran — tanggapan berisi tawaran balik"},
         {"id": "s4", "text": "Persetujuan — kesepakatan yang dicapai"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — orientasi, pengajuan, penawaran, lalu persetujuan.",
         "wrong": "Urutannya: orientasi, pengajuan, penawaran, dan persetujuan.",
     }},
    {"type": "checkpoint", "id": "cp-bi4-debat",
     "question": "Perbedaan utama negosiasi dan debat adalah…",
     "choices": [
         {"id": "a", "text": "Negosiasi mencari kesepakatan, debat mencari kemenangan argumen", "correct": True},
         {"id": "b", "text": "Negosiasi selalu memakai kata kasar"},
         {"id": "c", "text": "Debat tidak memerlukan argumen"},
     ],
     "explanation": "Negosiasi mencari kesepakatan yang menguntungkan kedua pihak, sedangkan debat mencari kemenangan argumen."},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-bi4-santun", "engine": "mermaid",
     "title": "Bahasa santun membuka jalan kesepakatan",
     "code": "flowchart LR\n  A[Santun] --> A1[Membuka ruang]\n  A1 --> A2[Kesepakatan tercapai]\n  B[Menekan] --> B1[Menutup ruang]\n  B1 --> B2[Negosiasi gagal]"},
    {"type": "categorize", "id": "cat-bi4-santun",
     "prompt": "Kelompokkan kalimat berikut ke dalam santun atau menekan.",
     "buckets": [
         {"id": "santun", "label": "Santun — membuka ruang"},
         {"id": "menekan", "label": "Menekan — menutup ruang"},
     ],
     "items": [
         {"id": "s1", "text": "Apakah Bapak berkenan memberikan harga khusus untuk pembelian 10 unit?", "bucket": "santun"},
         {"id": "s2", "text": "Mohon maaf, penawaran itu di luar anggaran kami. Apakah ada alternatif lain?", "bucket": "santun"},
         {"id": "s3", "text": "Pokoknya harus turun sekarang!", "bucket": "menekan"},
         {"id": "s4", "text": "Kalau tidak sesuai harga saya, saya akan membeli di tempat lain.", "bucket": "menekan"},
     ],
     "feedback": {
         "correct": "Benar — kalimat santun membuka ruang dan disertai alasan atau alternatif.",
         "wrong": "Kalimat yang menekan menutup ruang; kalimat santun mengajak dan menawarkan pilihan.",
     }},
    {"type": "checkpoint", "id": "cp-bi4-menolak",
     "question": "Menolak penawaran dengan santun sebaiknya…",
     "choices": [
         {"id": "a", "text": "Disertai alasan dan alternatif", "correct": True},
         {"id": "b", "text": "Disertai ancaman"},
         {"id": "c", "text": "Tanpa penjelasan apa pun"},
     ],
     "explanation": "Menolak dengan santun berarti menyampaikan alasan dan menawarkan alternatif agar negosiasi tetap berjalan."},
    {"type": "checkpoint", "id": "cp-bi4-kesepakatan",
     "question": "Kesepakatan negosiasi sebaiknya memuat…",
     "choices": [
         {"id": "a", "text": "Harga, jumlah, waktu, dan cara pembayaran", "correct": True},
         {"id": "b", "text": "Hanya harga tanpa jumlah"},
         {"id": "c", "text": "Janji lisan tanpa catatan"},
     ],
     "explanation": "Catatan tertulis yang memuat harga, jumlah, waktu, dan cara pembayaran mencegah perbedaan penafsiran di kemudian hari."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-bi4-langkah",
     "prompt": "Urutkan langkah menyiapkan negosiasi.",
     "items": [
         {"id": "s1", "text": "Tentukan kebutuhan dan anggaran"},
         {"id": "s2", "text": "Cari data harga pembanding"},
         {"id": "s3", "text": "Siapkan argumen dan alternatif"},
         {"id": "s4", "text": "Lakukan dialog tawar-menawar hingga sepakat"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — tentukan kebutuhan dan anggaran, cari pembanding, siapkan argumen, lalu bernegosiasi.",
         "wrong": "Mulai dari kebutuhan dan anggaran, lalu data pembanding dan argumen.",
     }},
    {"type": "scenario", "id": "sc-bi4-tawar",
     "title": "Menawar harga perlengkapan kelas",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu ditugaskan membeli 10 perlengkapan kelas. Penjual menawarkan Rp150.000 per unit, sedangkan anggaranmu Rp135.000. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menyampaikan anggaran dan menanyakan kemungkinan harga khusus", "next": "n2", "score": 2,
               "feedback": "Negosiasi dibuka dengan maksud jelas dan bahasa santun."},
              {"text": "Menuntut turun sekarang tanpa alasan", "next": "n3", "score": 0,
               "feedback": "Menekan menutup ruang negosiasi dan membuat pihak lain bertahan."},
              {"text": "Langsung membeli meski melebihi anggaran", "next": "n4", "score": 1,
               "feedback": "Membeli tanpa menawar melewati kesempatan mencapai kesepakatan yang lebih baik."},
          ]},
         {"id": "n2", "text": "Penjual menawarkan Rp140.000. Apa langkahmu?",
          "choices": [
              {"text": "Mengajukan Rp135.000 dengan data pembanding dan jumlah pembelian", "next": "n5", "score": 2,
               "feedback": "Data pembanding dan jumlah pembelian memperkuat dasar penawaran."},
              {"text": "Menerima langsung tanpa mempertimbangkan anggaran", "next": "n4", "score": 1,
               "feedback": "Menerima terlalu cepat membuat anggaran tetap terlampaui."},
          ]},
         {"id": "n3", "text": "Penjual tetap pada harga awal. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak dengan santun dan menanyakan alternatif", "next": "n2", "score": 1,
               "feedback": "Menolak dengan alasan dan alternatif menjaga hubungan tetap baik."},
              {"text": "Mengancam akan membeli di tempat lain dengan kata kasar", "next": "n6", "score": 0,
               "feedback": "Ancaman merusak negosiasi dan menutup peluang kesepakatan."},
          ]},
         {"id": "n4", "text": "Kesepakatan belum tercapai dan waktu terbatas. Apa keputusanmu?",
          "choices": [
              {"text": "Menyepakati harga yang masih dalam anggaran atau mencari penjual lain dengan data", "next": "n5", "score": 2,
               "feedback": "Kesepakatan harus tetap menjaga anggaran dan didasari data."},
              {"text": "Menyetujui semua syarat penjual agar cepat selesai", "next": "n6", "score": 0,
               "feedback": "Menyetujui semua syarat mengorbankan kepentingan yang seharusnya dijaga."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kesepakatan tercapai: harga sesuai anggaran, jumlah jelas, dan kedua pihak sepakat."},
         {"id": "n6", "end": True, "outcome": "bad",
          "text": "Negosiasi gagal atau anggaran terlampaui. Ancaman dan keputusan terburu-buru merugikan."},
     ]},
    {"type": "challenge", "id": "ch-bi4-negosiasi",
     "title": "Tantangan Kilat: Negosiasi",
     "time_limit": 90,
     "items": [
         {"question": "Proses tawar-menawar untuk mencapai kesepakatan disebut…", "answer": "negosiasi"},
         {"question": "Bagian pembuka dan penyampaian maksud disebut…", "answer": "orientasi"},
         {"question": "Bagian berisi tawaran balik disebut…", "answer": "penawaran"},
         {"question": "Bagian berisi kesepakatan disebut…", "answer": "persetujuan"},
         {"question": "Kesediaan saling mengurangi tuntutan disebut…", "answer": "kompromi"},
         {"question": "Data dari sumber lain untuk menguji kewajaran harga disebut data…", "answer": "pembanding"},
     ],
     "feedback": {
         "correct": "Tepat — negosiasi yang baik santun, berbasis data, dan menjaga kepentingan kedua pihak.",
         "wrong": "Ingat struktur negosiasi dan bedakan santun, menekan, serta ancaman.",
     }},
])
save(path, data)

# ── BI 5 — Teks Biografi ──────────────────────────────────────────────
path = 'bi-5-teks-biografi.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-bi5-struktur", "engine": "mermaid",
     "title": "Struktur teks biografi",
     "code": "flowchart TD\n  A[Orientasi: pengenalan tokoh dan latar belakang] --> B[Peristiwa: rangkaian kejadian penting]\n  B --> C[Reorientasi: pandangan atau kesan penulis]"},
    {"type": "glossary", "terms": [
        {"term": "Biografi", "definition": "Riwayat hidup tokoh yang ditulis oleh orang lain berdasarkan fakta."},
        {"term": "Autobiografi", "definition": "Riwayat hidup yang ditulis oleh tokohnya sendiri."},
        {"term": "Ide pokok", "definition": "Gagasan utama sebuah paragraf."},
        {"term": "Tersirat", "definition": "Makna yang perlu disimpulkan, tidak dinyatakan langsung."},
    ]},
    {"type": "checkpoint", "id": "cp-bi5-struktur",
     "question": "Bagian biografi yang berisi pandangan atau kesan penulis terhadap tokoh adalah…",
     "choices": [
         {"id": "a", "text": "Reorientasi", "correct": True},
         {"id": "b", "text": "Orientasi"},
         {"id": "c", "text": "Peristiwa"},
     ],
     "explanation": "Orientasi mengenalkan tokoh, peristiwa memuat kejadian penting, dan reorientasi berisi pandangan atau kesan penulis."},
    {"type": "sort", "id": "srt-bi5-ide",
     "prompt": "Urutkan cara menemukan ide pokok paragraf.",
     "items": [
         {"id": "s1", "text": "Baca seluruh paragraf"},
         {"id": "s2", "text": "Tandai kalimat yang paling umum"},
         {"id": "s3", "text": "Periksa kalimat penjelas"},
         {"id": "s4", "text": "Rumuskan ide pokok dengan kalimat sendiri"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — baca, tandai kalimat umum, periksa penjelas, lalu rumuskan dengan kalimat sendiri.",
         "wrong": "Mulai dari membaca seluruh paragraf, lalu tandai kalimat yang paling umum.",
     }},
    {"type": "checkpoint", "id": "cp-bi5-tersirat",
     "question": "“Tokoh itu selalu datang paling awal, sehingga ia dikenal disiplin.” Watak disiplin dalam kalimat itu bersifat…",
     "choices": [
         {"id": "a", "text": "Tersirat, disimpulkan dari kebiasaan", "correct": True},
         {"id": "b", "text": "Tersurat, dinyatakan langsung"},
         {"id": "c", "text": "Opini tanpa dasar"},
     ],
     "explanation": "Tersirat berarti perlu disimpulkan. Kedisiplinan tidak dinyatakan langsung, melainkan disimpulkan dari kebiasaan datang paling awal."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-bi5-baku",
     "prompt": "Kelompokkan kata berikut ke dalam baku atau tidak baku.",
     "buckets": [
         {"id": "baku", "label": "Baku"},
         {"id": "tidak", "label": "Tidak baku"},
     ],
     "items": [
         {"id": "b1", "text": "Analisis", "bucket": "baku"},
         {"id": "b2", "text": "Efektivitas", "bucket": "baku"},
         {"id": "b3", "text": "Aktivitas", "bucket": "baku"},
         {"id": "b4", "text": "Analisa", "bucket": "tidak"},
         {"id": "b5", "text": "Efektifitas", "bucket": "tidak"},
         {"id": "b6", "text": "Aktifitas", "bucket": "tidak"},
     ],
     "feedback": {
         "correct": "Benar — bentuk baku: analisis, efektivitas, dan aktivitas.",
         "wrong": "Bentuk baku memakai -isis, -ivitas, dan -ivitas: analisis, efektivitas, aktivitas.",
     }},
    {"type": "checkpoint", "id": "cp-bi5-kutipan",
     "question": "Kutipan dalam biografi harus…",
     "choices": [
         {"id": "a", "text": "Sesuai dengan yang benar-benar diucapkan dan diapit tanda petik", "correct": True},
         {"id": "b", "text": "Dibuat-buat agar lebih menarik"},
         {"id": "c", "text": "Tanpa tanda petik agar terlihat luwes"},
     ],
     "explanation": "Kutipan yang dibuat-buat merusak kepercayaan pembaca. Kutipan harus sesuai ucapan sebenarnya dan diapit tanda petik."},
    {"type": "checkpoint", "id": "cp-bi5-titik",
     "question": "Kesalahan tanda baca yang paling umum dalam kalimat berita adalah…",
     "choices": [
         {"id": "a", "text": "Menghilangkan titik di akhir kalimat", "correct": True},
         {"id": "b", "text": "Menulis nama kota dengan huruf kapital"},
         {"id": "c", "text": "Memberi tanda petik pada kutipan langsung"},
     ],
     "explanation": "Kalimat berita diakhiri titik. Nama kota ditulis dengan huruf kapital dan kutipan langsung memakai tanda petik."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-bi5-menulis",
     "prompt": "Urutkan langkah menulis biografi.",
     "items": [
         {"id": "s1", "text": "Kumpulkan data dari sumber terpercaya"},
         {"id": "s2", "text": "Susun garis waktu peristiwa penting"},
         {"id": "s3", "text": "Tulis orientasi, peristiwa, dan reorientasi"},
         {"id": "s4", "text": "Sunting ejaan, tanda baca, dan kata serapan"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — kumpulkan data, susun garis waktu, tulis, lalu sunting.",
         "wrong": "Mulai dari mengumpulkan data terpercaya, lalu menyusun garis waktu.",
     }},
    {"type": "scenario", "id": "sc-bi5-sumber",
     "title": "Menilai biografi tanpa sumber",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu membaca biografi tokoh di internet. Isinya menarik, tetapi tidak mencantumkan satu pun sumber. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Memeriksa sumber lain sebelum memercayainya", "next": "n2", "score": 2,
               "feedback": "Biografi wajib berdasarkan fakta; memeriksa sumber mencegah penyebaran informasi keliru."},
              {"text": "Langsung membagikannya karena tulisannya bagus", "next": "n3", "score": 0,
               "feedback": "Membagikan tanpa verifikasi menyebarkan informasi yang belum tentu benar."},
              {"text": "Mengabaikan seluruh isi karena tidak ada sumber", "next": "n4", "score": 1,
               "feedback": "Berhati-hati itu baik, tetapi menolak seluruh isi tanpa memeriksa juga tidak membantu."},
          ]},
         {"id": "n2", "text": "Ternyata ada perbedaan tahun lahir antara artikel itu dan sumber resmi. Apa sikapmu?",
          "choices": [
              {"text": "Memakai sumber resmi dan mencatat perbedaannya", "next": "n5", "score": 2,
               "feedback": "Tahun penting harus akurat; sumber resmi dan catatan perbedaan menjaga ketepatan."},
              {"text": "Memilih tahun yang lebih menarik", "next": "n6", "score": 0,
               "feedback": "Memilih data karena menarik mengorbankan akurasi fakta."},
          ]},
         {"id": "n3", "text": "Guru meminta kamu menulis biografi tokoh. Apa langkah pertamamu?",
          "choices": [
              {"text": "Mengumpulkan data dari wawancara, dokumen resmi, dan buku", "next": "n5", "score": 2,
               "feedback": "Sumber terpercaya menjadi dasar biografi yang faktual."},
              {"text": "Menulis berdasarkan tebakan agar cepat selesai", "next": "n7", "score": 0,
               "feedback": "Tebakan tanpa verifikasi tidak boleh dipakai dalam biografi."},
          ]},
         {"id": "n4", "text": "Kamu menemukan kutipan tokoh yang bagus, tetapi tidak yakin kebenarannya. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mencari sumber kutipan atau tidak memakainya", "next": "n5", "score": 2,
               "feedback": "Kutipan harus sesuai ucapan sebenarnya; jika tidak dapat dipastikan, jangan dipakai."},
              {"text": "Memakainya dan mengubah sedikit agar lebih menarik", "next": "n7", "score": 0,
               "feedback": "Mengubah kutipan membuatnya tidak lagi sesuai ucapan asli."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Biografimu akurat dan sumbernya jelas. Keteladanan tokoh disampaikan dengan data, bukan tebakan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Tulisan tetap ada, tetapi akurasinya belum terjaga. Perbaiki dengan sumber resmi."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Biografi memuat data atau kutipan yang tidak benar. Kepercayaan pembaca hilang."},
     ]},
    {"type": "challenge", "id": "ch-bi5-biografi",
     "title": "Tantangan Kilat: Biografi",
     "time_limit": 90,
     "items": [
         {"question": "Riwayat hidup tokoh yang ditulis orang lain disebut…", "answer": "biografi"},
         {"question": "Riwayat hidup yang ditulis tokohnya sendiri disebut…", "answer": "autobiografi"},
         {"question": "Gagasan utama paragraf disebut ide…", "answer": "pokok"},
         {"question": "Bagian biografi berisi kesan penulis disebut…", "answer": "reorientasi"},
         {"question": "Bentuk baku dari “analisa” adalah…", "answer": "analisis"},
         {"question": "Makna yang perlu disimpulkan disebut…", "answer": "tersirat"},
     ],
     "feedback": {
         "correct": "Tepat — biografi yang baik faktual, bersumber jelas, dan mengikuti kaidah bahasa.",
         "wrong": "Ingat: biografi, autobiografi, ide pokok, reorientasi, analisis, dan tersirat.",
     }},
])
save(path, data)

print('batch 9: BI 1 sampai BI 5 selesai')
