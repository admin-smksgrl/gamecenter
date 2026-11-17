"""Fase 5.1 batch 7b — blok interaktif untuk PAI 6 sampai PAI 10.

Jalankan dari folder gamecenter:

    python ../tools/tambah-blok-fase5-b7b.py
    python ../tools/rapikan-blok-fase5.py --apply
    php artisan gamecenter:materi-import
"""
import io
import json

BASE = 'database/seeders/data/sma-smk/fase-e/pai/'


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


# ── PAI 6 — Pergaulan Bebas dan Zina ──────────────────────────────────
path = 'pai-6-pergaulan-bebas-dan-zina.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pai6-bertahap", "engine": "mermaid",
     "title": "Larangan zina ditegakkan bertahap",
     "code": "flowchart LR\n  A[Mencegah dorongan] --> B[Menjaga pandangan]\n  A --> C[Menjaga pergaulan]\n  A --> D[Menghindari konten pornografi]\n  B --> E[Tidak mendekati zina]\n  C --> E\n  D --> E\n  E --> F[Hukum bagi pelanggaran]"},
    {"type": "glossary", "terms": [
        {"term": "Zina", "definition": "Perbuatan keji dan jalan yang buruk; Islam melarang mendekatinya, bukan hanya melakukannya."},
        {"term": "Muhsan", "definition": "Sebutan bagi orang yang sudah pernah menikah."},
        {"term": "Ghayr muhsan", "definition": "Sebutan bagi orang yang belum pernah menikah."},
        {"term": "Pornografi", "definition": "Konten berisi kecabulan yang wajib dihindari karena termasuk hal yang mendekati zina."},
    ]},
    {"type": "checkpoint", "id": "cp-pai6-mendekati",
     "question": "Q.S. al-Isra'/17: 32 melarang…",
     "choices": [
         {"id": "a", "text": "Mendekati zina, bukan hanya perbuatannya", "correct": True},
         {"id": "b", "text": "Menikah sebelum mampu"},
         {"id": "c", "text": "Menuntut ilmu agama"},
     ],
     "explanation": "Ayat melarang mendekati zina. Karena itu menjaga pandangan, menjaga pergaulan, dan menghindari konten pornografi termasuk perintah yang harus dijalankan."},
    {"type": "checkpoint", "id": "cp-pai6-muhsan",
     "question": "Istilah untuk orang yang sudah pernah menikah adalah…",
     "choices": [
         {"id": "a", "text": "Muhsan", "correct": True},
         {"id": "b", "text": "Ghayr muhsan"},
         {"id": "c", "text": "Mukallaf"},
     ],
     "explanation": "Muhsan berarti sudah pernah menikah, sedangkan ghayr muhsan berarti belum pernah menikah."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-pai6-pergaulan",
     "prompt": "Kelompokkan bentuk pergaulan berikut.",
     "buckets": [
         {"id": "bebas", "label": "Pergaulan bebas"},
         {"id": "sehat", "label": "Pergaulan sehat"},
     ],
     "items": [
         {"id": "p1", "text": "Berduaan di tempat sepi", "bucket": "bebas"},
         {"id": "p2", "text": "Bercanda yang melampaui batas", "bucket": "bebas"},
         {"id": "p3", "text": "Menyebarkan foto atau data pribadi tanpa izin", "bucket": "bebas"},
         {"id": "p4", "text": "Menikmati konten pornografi", "bucket": "bebas"},
         {"id": "p5", "text": "Bekerja sama tugas dengan menjaga etika", "bucket": "sehat"},
         {"id": "p6", "text": "Saling menghormati batas dan membawa manfaat", "bucket": "sehat"},
     ],
     "feedback": {
         "correct": "Benar — pergaulan sehat saling menghormati batas dan membawa manfaat, bukan melanggar norma.",
         "wrong": "Pergaulan bebas melanggar norma agama dan sosial; pergaulan sehat menjaga batas serta memberi manfaat.",
     }},
    {"type": "checkpoint", "id": "cp-pai6-bahaya",
     "question": "Dampak pergaulan bebas pada bidang belajar adalah…",
     "choices": [
         {"id": "a", "text": "Waktu dan fokus berkurang sehingga prestasi menurun", "correct": True},
         {"id": "b", "text": "Prestasi meningkat karena lebih banyak teman"},
         {"id": "c", "text": "Tidak ada dampak sama sekali"},
     ],
     "explanation": "Pergaulan bebas menyita waktu dan fokus belajar. Dampak lainnya menyentuh kesehatan, sosial, masa depan, dan akhlak."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-pai6-tekanan",
     "prompt": "Urutkan langkah menghadapi tekanan teman agar tidak terjerumus.",
     "items": [
         {"id": "s1", "text": "Menyadari ajakan itu melanggar nilai"},
         {"id": "s2", "text": "Mengingat tujuan dan masa depan diri"},
         {"id": "s3", "text": "Menolak dengan tegas dan santun"},
         {"id": "s4", "text": "Mencari teman dan kegiatan positif"},
         {"id": "s5", "text": "Meminta dukungan orang tua atau guru"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — sadari, ingat tujuan, tolak dengan santun, cari lingkungan positif, lalu minta dukungan.",
         "wrong": "Mulai dari menyadari bahwa ajakan itu melanggar nilai, lalu menolaknya dengan tegas dan santun.",
     }},
    {"type": "scenario", "id": "sc-pai6-tekanan",
     "title": "Tekanan teman untuk melanggar batas",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Sepulang sekolah, teman-teman mengajak berduaan di tempat sepi. Mereka bilang semua orang juga begitu. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak dengan tegas dan santun, lalu pulang bersama teman lain", "next": "n2", "score": 2,
               "feedback": "Menolak dengan tegas dan santun menjaga batas tanpa harus memutus pertemanan."},
              {"text": "Ikut sebentar agar tidak dianggap sombong", "next": "n3", "score": 0,
               "feedback": "Ikut karena takut dianggap sombong berarti menyerahkan prinsip kepada tekanan teman."},
              {"text": "Diam saja dan mencari alasan untuk pergi", "next": "n4", "score": 1,
               "feedback": "Pergi itu aman, tetapi alasan yang tidak jelas membuat ajakan bisa terulang."},
          ]},
         {"id": "n2", "text": "Mereka mengejekmu penakut. Bagaimana sikapmu?",
          "choices": [
              {"text": "Tetap tenang dan mengingat tujuan serta masa depanmu", "next": "n5", "score": 2,
               "feedback": "Ejekan tidak mengubah nilai. Mengingat tujuan membuat pendirian lebih kuat."},
              {"text": "Membalas ejekan dengan kata-kata kasar", "next": "n6", "score": 0,
               "feedback": "Membalas dengan kasar memperpanjang masalah dan merusak akhlak."},
          ]},
         {"id": "n3", "text": "Kamu merasa tidak nyaman dan ingin berhenti. Apa langkahmu?",
          "choices": [
              {"text": "Berhenti, minta maaf, dan menjauh dari kebiasaan itu", "next": "n2", "score": 1,
               "feedback": "Berhenti dan memperbaiki diri adalah langkah taubat yang benar."},
              {"text": "Melanjutkan karena sudah terlanjur ikut", "next": "n7", "score": 0,
               "feedback": "Sudah terlanjur bukan alasan untuk melanjutkan pelanggaran."},
          ]},
         {"id": "n4", "text": "Keesokan harinya mereka mengajak lagi. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak jelas dan mengajak mereka ke kegiatan yang bermanfaat", "next": "n5", "score": 2,
               "feedback": "Penolakan jelas disertai ajakan positif memutus kebiasaan tanpa memutus pertemanan."},
              {"text": "Menghindar tanpa penjelasan dan menjauhi semua teman", "next": "n6", "score": 1,
               "feedback": "Menjauh aman, tetapi tanpa penjelasan kamu kehilangan dukungan teman yang baik."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kamu menjaga batas, tetap punya teman, dan mengisi waktu dengan kegiatan positif. Prinsipmu menguat."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Kamu terhindar dari ajakan itu, tetapi caranya belum ideal. Perbaiki dengan komunikasi yang santun."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Pelanggaran berlanjut dan kamu kehilangan kendali atas pilihan sendiri. Segera minta bantuan guru atau keluarga."},
     ]},
    {"type": "challenge", "id": "ch-pai6-pergaulan",
     "title": "Tantangan Kilat: Menjaga Kehormatan Diri",
     "time_limit": 80,
     "items": [
         {"question": "Surah yang melarang mendekati zina adalah al-Isra' ayat…", "answer": "32"},
         {"question": "Orang yang sudah pernah menikah disebut…", "answer": "muhsan"},
         {"question": "Orang yang belum pernah menikah disebut ghayr…", "answer": "muhsan"},
         {"question": "Menyesali, berhenti, dan memperbaiki diri disebut…", "answer": "taubat"},
         {"question": "Pergaulan sehat ditandai saling menghormati…", "answer": "batas"},
     ],
     "feedback": {
         "correct": "Tepat — menjaga batas dan memilih lingkungan positif melindungi masa depan.",
         "wrong": "Ingat: larangan mendekati zina, istilah muhsan, taubat, dan pergaulan yang menghormati batas.",
     }},
])
save(path, data)

# ── PAI 7 — Mahabbah, Khauf, Raja', dan Tawakal ───────────────────────
path = 'pai-7-mahabbah-khauf-raja-tawakal.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Mahabbah", "definition": "Rasa cinta kepada Allah yang diwujudkan dengan menjalankan perintah dan menjauhi larangan-Nya."},
        {"term": "Zikir", "definition": "Mengingat Allah dengan menyebut nama-Nya, termasuk memperbanyak doa."},
        {"term": "Sunah", "definition": "Cara dan ajaran Rasulullah Saw. yang diikuti sebagai tanda cinta kepada Allah."},
    ]},
    {"type": "checkpoint", "id": "cp-pai7-tanda",
     "question": "Menurut hadis, tanda cinta kepada Allah adalah…",
     "choices": [
         {"id": "a", "text": "Mengikuti Rasulullah Saw.", "correct": True},
         {"id": "b", "text": "Memperbanyak bicara tentang cinta"},
         {"id": "c", "text": "Menjauhi pergaulan sehari-hari"},
     ],
     "explanation": "Cinta sejati melahirkan ketaatan. Hadis menegaskan bahwa tanda cinta kepada Allah adalah mengikuti Rasulullah dan menjalankan sunahnya."},
    {"type": "sort", "id": "srt-pai7-cinta",
     "prompt": "Urutkan cara menumbuhkan cinta kepada Allah.",
     "items": [
         {"id": "s1", "text": "Mengenali nikmat Allah"},
         {"id": "s2", "text": "Memperbanyak ibadah"},
         {"id": "s3", "text": "Merenungkan nama dan sifat Allah"},
         {"id": "s4", "text": "Memperbanyak zikir dan doa"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — kenali nikmat-Nya, perbanyak ibadah, renungkan nama dan sifat-Nya, lalu perbanyak zikir dan doa.",
         "wrong": "Mulai dari mengenali nikmat Allah, lalu ibadah, perenungan, dan zikir.",
     }},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-pai7-khauf-raja", "engine": "mermaid",
     "title": "Khauf dan raja' harus berjalan seimbang",
     "code": "flowchart TD\n  A[Khauf: takut kepada Allah] --> B[Menjauhi larangan]\n  C[Raja': berharap rahmat Allah] --> D[Berhusnuzan dan beramal]\n  A --> E[Seimbang]\n  C --> E\n  E --> F[Tidak putus asa]\n  E --> G[Tidak meremehkan dosa]"},
    {"type": "checkpoint", "id": "cp-pai7-putus-asa",
     "question": "Khauf yang berlebihan tanpa raja' dapat menyebabkan…",
     "choices": [
         {"id": "a", "text": "Putus asa dari rahmat Allah", "correct": True},
         {"id": "b", "text": "Meremehkan dosa"},
         {"id": "c", "text": "Merasa aman dari azab"},
     ],
     "explanation": "Khauf tanpa raja' membuat seseorang putus asa, sedangkan raja' tanpa khauf membuatnya meremehkan dosa dan merasa aman."},
    {"type": "categorize", "id": "cat-pai7-khauf-raja",
     "prompt": "Kelompokkan pernyataan berikut ke dalam khauf atau raja'.",
     "buckets": [
         {"id": "khauf", "label": "Khauf"},
         {"id": "raja", "label": "Raja'"},
     ],
     "items": [
         {"id": "k1", "text": "Takut kepada Allah atas perbuatan salah", "bucket": "khauf"},
         {"id": "k2", "text": "Mendorong menjauhi larangan", "bucket": "khauf"},
         {"id": "k3", "text": "Berharap penuh pada rahmat dan ampunan Allah", "bucket": "raja"},
         {"id": "k4", "text": "Berhusnuzan atas setiap ketetapan Allah", "bucket": "raja"},
     ],
     "feedback": {
         "correct": "Benar — khauf mendorong menjauhi larangan, raja' menumbuhkan harapan dan husnuzan.",
         "wrong": "Khauf itu rasa takut yang mendorong taat; raja' itu harapan pada rahmat dan ampunan.",
     }},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-pai7-tawakal",
     "prompt": "Kelompokkan sikap berikut ke dalam tawakal atau malas.",
     "buckets": [
         {"id": "tawakal", "label": "Tawakal"},
         {"id": "malas", "label": "Malas"},
     ],
     "items": [
         {"id": "t1", "text": "Berusaha maksimal lalu menyerahkan hasil kepada Allah", "bucket": "tawakal"},
         {"id": "t2", "text": "Diiringi doa", "bucket": "tawakal"},
         {"id": "t3", "text": "Menerima hasil dengan sabar", "bucket": "tawakal"},
         {"id": "t4", "text": "Tanpa usaha", "bucket": "malas"},
         {"id": "t5", "text": "Meninggalkan kewajiban", "bucket": "malas"},
     ],
     "feedback": {
         "correct": "Tepat — tawakal dilakukan setelah usaha maksimal dan diiringi doa, bukan pengganti usaha.",
         "wrong": "Tawakal bukan malas: usaha tetap maksimal, doa menyertai, lalu hasil diterima dengan sabar.",
     }},
    {"type": "sort", "id": "srt-pai7-ujian",
     "prompt": "Urutkan langkah tawakal dalam menghadapi ujian.",
     "items": [
         {"id": "s1", "text": "Belajar dengan sungguh-sungguh"},
         {"id": "s2", "text": "Berdoa memohon kemudahan"},
         {"id": "s3", "text": "Mengerjakan ujian dengan jujur"},
         {"id": "s4", "text": "Menerima hasil dengan sabar"},
         {"id": "s5", "text": "Mengevaluasi dan memperbaiki diri"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — belajar, berdoa, jujur saat ujian, sabar menerima hasil, lalu evaluasi.",
         "wrong": "Usaha belajar tetap lebih dulu, doa menyertai, lalu hasilnya diterima dengan sabar.",
     }},
    {"type": "scenario", "id": "sc-pai7-ujian",
     "title": "Hasil ujian tidak sesuai harapan",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu sudah belajar, tetapi nilai ujian masih rendah. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menerima hasil dengan sabar lalu mengevaluasi cara belajar", "next": "n2", "score": 2,
               "feedback": "Tawakal berarti menerima hasil dengan sabar dan tetap berusaha memperbaiki diri."},
              {"text": "Menyalahkan guru dan soal yang dianggap tidak adil", "next": "n3", "score": 0,
               "feedback": "Menyalahkan pihak lain menutup peluang memperbaiki cara belajar sendiri."},
              {"text": "Merasa sedih dan berhenti berusaha", "next": "n4", "score": 1,
               "feedback": "Sedih itu wajar, tetapi berhenti berusaha membuat hasil berikutnya tidak berubah."},
          ]},
         {"id": "n2", "text": "Teman menawarkan bocoran soal ujian berikutnya. Apa sikapmu?",
          "choices": [
              {"text": "Menolak karena kejujuran bagian dari tawakal", "next": "n5", "score": 2,
               "feedback": "Jujur saat ujian adalah wujud tawakal setelah berusaha; bocoran bukan usaha."},
              {"text": "Menerima agar nilainya naik", "next": "n6", "score": 0,
               "feedback": "Nilai naik dengan cara curang menghilangkan keberkahan dan kejujuran."},
          ]},
         {"id": "n3", "text": "Guru menjelaskan bahwa soal sesuai materi. Apa langkahmu?",
          "choices": [
              {"text": "Memeriksa catatan dan meminta bantuan belajar", "next": "n2", "score": 1,
               "feedback": "Memeriksa diri sendiri lebih berguna daripada menyalahkan pihak lain."},
              {"text": "Tetap yakin gurunya salah", "next": "n7", "score": 0,
               "feedback": "Menolak penjelasan membuat masalah yang sama terulang."},
          ]},
         {"id": "n4", "text": "Beberapa hari kemudian kamu masih kecewa. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Berdoa, bangkit, dan menyusun jadwal belajar baru", "next": "n5", "score": 2,
               "feedback": "Doa dan usaha baru memulihkan semangat tanpa melupakan tawakal."},
              {"text": "Membiarkan nilai itu dan tidak belajar lagi", "next": "n7", "score": 0,
               "feedback": "Berhenti belajar membuat kekecewaan berulang di ujian berikutnya."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kamu menerima hasil dengan sabar, tetap jujur, dan memperbaiki cara belajar. Tawakal berjalan bersama usaha."},
         {"id": "n6", "end": True, "outcome": "bad",
          "text": "Nilai mungkin naik, tetapi kejujuran hilang. Tawakal tidak pernah berarti mencari jalan curang."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Kekecewaan berubah menjadi keputusasaan. Tanpa usaha baru, hasil berikutnya sulit berubah."},
     ]},
    {"type": "challenge", "id": "ch-pai7-hati",
     "title": "Tantangan Kilat: Mahabbah, Khauf, Raja', Tawakal",
     "time_limit": 80,
     "items": [
         {"question": "Rasa cinta kepada Allah disebut…", "answer": "mahabbah"},
         {"question": "Rasa takut kepada Allah atas perbuatan salah disebut…", "answer": "khauf"},
         {"question": "Berharap penuh pada rahmat dan ampunan Allah disebut…", "answer": "raja"},
         {"question": "Menyerahkan hasil kepada Allah setelah usaha maksimal disebut…", "answer": "tawakal"},
         {"question": "Tanda cinta kepada Allah adalah mengikuti…", "answer": "rasulullah"},
     ],
     "feedback": {
         "correct": "Tepat — cinta melahirkan ketaatan, takut dan harap berjalan seimbang, tawakal menyertai usaha.",
         "wrong": "Ingat: mahabbah, khauf, raja', tawakal, dan mengikuti Rasulullah sebagai tanda cinta.",
     }},
])
save(path, data)

# ── PAI 8 — Akhlak Madzmumah dan Mahmudah ─────────────────────────────
path = 'pai-8-akhlak-madzmumah-mahmudah.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Akhlak madzmumah", "definition": "Akhlak tercela yang merusak hubungan dengan Allah dan manusia."},
        {"term": "Akhlak mahmudah", "definition": "Akhlak terpuji yang mendatangkan kebaikan bagi diri dan lingkungan."},
        {"term": "Ghadhab", "definition": "Sikap temperamental atau mudah marah karena emosi dan ego tidak terkendali."},
    ]},
    {"type": "checkpoint", "id": "cp-pai8-ghadhab",
     "question": "Sikap temperamental atau mudah marah disebut…",
     "choices": [
         {"id": "a", "text": "Ghadhab", "correct": True},
         {"id": "b", "text": "Husnuzan"},
         {"id": "c", "text": "Syaja'ah"},
     ],
     "explanation": "Ghadhab adalah akhlak madzmumah berupa mudah marah. Dampaknya merusak hubungan sosial dan membuat keputusan diambil berdasarkan emosi."},
    {"type": "sort", "id": "srt-pai8-marah",
     "prompt": "Urutkan cara mengendalikan marah.",
     "items": [
         {"id": "s1", "text": "Menyadari emosi muncul"},
         {"id": "s2", "text": "Menahan diri dan diam"},
         {"id": "s3", "text": "Mengambil wudu atau memindahkan posisi"},
         {"id": "s4", "text": "Berpikir dan memilih respons terbaik"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — sadari, tahan diri, ambil wudu atau pindah posisi, lalu pilih respons terbaik.",
         "wrong": "Mulai dari menyadari emosi, menahan diri, meredakan dengan wudu, baru memilih respons.",
     }},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-pai8-kontrol", "engine": "mermaid",
     "title": "Kontrol diri dan manfaatnya",
     "code": "flowchart LR\n  A[Kontrol diri] --> B[Mengendalikan emosi dan dorongan]\n  B --> C[Hubungan sosial lebih baik]\n  B --> D[Keputusan lebih matang]\n  B --> E[Emosi lebih stabil]\n  F[Pembiasaan yang diulang] --> A"},
    {"type": "checkpoint", "id": "cp-pai8-husnuzan",
     "question": "Berprasangka baik, misalnya tidak menuduh teman yang terlambat tanpa bukti, disebut…",
     "choices": [
         {"id": "a", "text": "Husnuzan", "correct": True},
         {"id": "b", "text": "Ghadhab"},
         {"id": "c", "text": "Syaja'ah"},
     ],
     "explanation": "Husnuzan adalah berprasangka baik. Sikap ini mencegah tuduhan tanpa bukti yang merusak hubungan."},
    {"type": "categorize", "id": "cat-pai8-akhlak",
     "prompt": "Kelompokkan sikap berikut ke dalam akhlak mahmudah atau madzmumah.",
     "buckets": [
         {"id": "mahmudah", "label": "Akhlak mahmudah"},
         {"id": "madzmumah", "label": "Akhlak madzmumah"},
     ],
     "items": [
         {"id": "a1", "text": "Sabar", "bucket": "mahmudah"},
         {"id": "a2", "text": "Husnuzan", "bucket": "mahmudah"},
         {"id": "a3", "text": "Jujur", "bucket": "mahmudah"},
         {"id": "a4", "text": "Tolong-menolong", "bucket": "mahmudah"},
         {"id": "a5", "text": "Tawadu", "bucket": "mahmudah"},
         {"id": "a6", "text": "Ghadhab", "bucket": "madzmumah"},
         {"id": "a7", "text": "Mudah marah karena ego tinggi", "bucket": "madzmumah"},
         {"id": "a8", "text": "Menuduh teman tanpa bukti", "bucket": "madzmumah"},
     ],
     "feedback": {
         "correct": "Benar — sabar, husnuzan, jujur, tolong-menolong, dan tawadu adalah akhlak mahmudah.",
         "wrong": "Ghadhab, mudah marah, dan menuduh tanpa bukti termasuk akhlak madzmumah.",
     }},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-pai8-syajaah",
     "question": "Keberanian yang didasari kebenaran, pertimbangan risiko, dan ilmu disebut…",
     "choices": [
         {"id": "a", "text": "Syaja'ah", "correct": True},
         {"id": "b", "text": "Nekat"},
         {"id": "c", "text": "Ghadhab"},
     ],
     "explanation": "Syaja'ah adalah berani membela kebenaran dengan pertimbangan dan ilmu. Tanpa ilmu, keberanian berubah menjadi kenekatan."},
    {"type": "sort", "id": "srt-pai8-syajaah",
     "prompt": "Urutkan langkah menumbuhkan syaja'ah.",
     "items": [
         {"id": "s1", "text": "Memahami nilai akhlak yang ingin dibiasakan"},
         {"id": "s2", "text": "Menetapkan target perilaku harian"},
         {"id": "s3", "text": "Melaksanakan secara konsisten"},
         {"id": "s4", "text": "Meminta umpan balik dari guru atau teman"},
         {"id": "s5", "text": "Mengevaluasi dan memperbaiki"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — pahami nilainya, tetapkan target, lakukan konsisten, minta umpan balik, lalu evaluasi.",
         "wrong": "Mulai dari memahami nilai akhlak, lalu target harian, konsistensi, umpan balik, dan evaluasi.",
     }},
    {"type": "scenario", "id": "sc-pai8-curang",
     "title": "Ajakan curang saat ujian",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Saat ujian, teman sebangku meminta jawabanmu. Ia sudah sering membantumu belajar. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak dengan santun dan fokus pada ujian sendiri", "next": "n2", "score": 2,
               "feedback": "Syaja'ah berarti berani menolak ajakan curang meski kepada teman yang baik."},
              {"text": "Memberi jawaban karena tidak enak hati", "next": "n3", "score": 0,
               "feedback": "Tidak enak hati bukan alasan membenarkan kecurangan; keduanya ikut salah."},
              {"text": "Pura-pura tidak mendengar", "next": "n4", "score": 1,
               "feedback": "Menghindar mencegah kecurangan, tetapi teman tetap belum tahu batasnya."},
          ]},
         {"id": "n2", "text": "Setelah ujian, temanmu kecewa dan menjauh. Apa langkahmu?",
          "choices": [
              {"text": "Menjelaskan alasannya dengan santun dan menawarkan belajar bersama", "next": "n5", "score": 2,
               "feedback": "Menjelaskan dengan santun menjaga hubungan sekaligus menegakkan kebenaran."},
              {"text": "Membiarkannya menjauh karena merasa benar", "next": "n6", "score": 1,
               "feedback": "Pendirianmu benar, tetapi membiarkan hubungan rusak tanpa penjelasan belum ideal."},
          ]},
         {"id": "n3", "text": "Guru menyadari ada jawaban yang sama. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui kesalahan dan menerima konsekuensinya", "next": "n5", "score": 2,
               "feedback": "Berani mengakui kesalahan adalah bagian dari syaja'ah dan langkah memperbaiki diri."},
              {"text": "Menyalahkan teman yang meminta jawaban", "next": "n7", "score": 0,
               "feedback": "Melepas tanggung jawab tidak menyelesaikan masalah dan menambah keburukan."},
          ]},
         {"id": "n4", "text": "Temanmu tetap memaksa dengan menyodorkan kertas. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak tegas dan melapor kepada pengawas bila perlu", "next": "n5", "score": 2,
               "feedback": "Menolak tegas dan meminta bantuan pengawas melindungi integritas ujian."},
              {"text": "Memberi sedikit jawaban agar ia berhenti memaksa", "next": "n7", "score": 0,
               "feedback": "Memberi sedikit tetap merupakan kecurangan dan tidak menyelesaikan masalah."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kebenaran dijaga dengan cara santun. Kamu berani menolak curang tanpa kehilangan pertemanan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Kamu tidak ikut curang, tetapi hubungan perlu diperbaiki dengan penjelasan yang santun."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Kecurangan terjadi dan tanggung jawab dilempar. Kepercayaan guru dan teman berkurang."},
     ]},
    {"type": "challenge", "id": "ch-pai8-akhlak",
     "title": "Tantangan Kilat: Akhlak dan Keberanian",
     "time_limit": 80,
     "items": [
         {"question": "Akhlak tercela disebut…", "answer": "madzmumah"},
         {"question": "Akhlak terpuji disebut…", "answer": "mahmudah"},
         {"question": "Mudah marah disebut…", "answer": "ghadhab"},
         {"question": "Berprasangka baik disebut…", "answer": "husnuzan"},
         {"question": "Berani membela kebenaran disebut…", "answer": "syajaah"},
         {"question": "Keberanian tanpa pertimbangan dan ilmu disebut…", "answer": "nekat"},
     ],
     "feedback": {
         "correct": "Tepat — akhlak terpuji dibiasakan, sedangkan marah dan kenekatan dikendalikan dengan ilmu.",
         "wrong": "Ingat: madzmumah, mahmudah, ghadhab, husnuzan, syaja'ah, dan nekat.",
     }},
])
save(path, data)

# ── PAI 9 — Al-Kulliyatu al-Khamsah ───────────────────────────────────
path = 'pai-9-al-kulliyatu-al-khamsah.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pai9-lima", "engine": "mermaid",
     "title": "Lima prinsip dasar yang wajib dilindungi",
     "code": "flowchart TD\n  A[Al-kulliyatu al-khamsah] --> B[hifzhu al-din: menjaga agama]\n  A --> C[hifzhu al-nafs: menjaga jiwa]\n  A --> D[hifzhu al-aql: menjaga akal]\n  A --> E[hifzhu al-nasl: menjaga keturunan]\n  A --> F[hifzhu al-mal: menjaga harta]\n  B --> G[Inti maqashid syariah]"},
    {"type": "glossary", "terms": [
        {"term": "Al-kulliyatu al-khamsah", "definition": "Lima prinsip dasar yang wajib dilindungi dalam hukum Islam."},
        {"term": "Kulliyah", "definition": "Menyeluruh: prinsip mendasar yang berlaku umum, bukan untuk kasus tertentu."},
        {"term": "Maqashid syariah", "definition": "Tujuan-tujuan yang hendak diwujudkan oleh syariat; intinya lima prinsip dasar."},
        {"term": "Hifzhu al-din", "definition": "Menjaga agama; prinsip pertama karena agama menjadi pedoman utama."},
    ]},
    {"type": "sort", "id": "srt-pai9-urutan",
     "prompt": "Urutkan lima prinsip al-kulliyatu al-khamsah.",
     "items": [
         {"id": "s1", "text": "Hifzhu al-din — menjaga agama"},
         {"id": "s2", "text": "Hifzhu al-nafs — menjaga jiwa"},
         {"id": "s3", "text": "Hifzhu al-aql — menjaga akal"},
         {"id": "s4", "text": "Hifzhu al-nasl — menjaga keturunan"},
         {"id": "s5", "text": "Hifzhu al-mal — menjaga harta"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — agama, jiwa, akal, keturunan, lalu harta.",
         "wrong": "Urutannya: agama, jiwa, akal, keturunan, dan harta.",
     }},
    {"type": "checkpoint", "id": "cp-pai9-agama",
     "question": "Mengapa menjaga agama ditempatkan pada urutan pertama?",
     "choices": [
         {"id": "a", "text": "Karena agama menjadi pedoman utama yang menata aspek kehidupan lainnya", "correct": True},
         {"id": "b", "text": "Karena agama lebih mudah dijalankan daripada yang lain"},
         {"id": "c", "text": "Karena prinsip lain tidak penting"},
     ],
     "explanation": "Agama menjadi pedoman utama yang menata aspek kehidupan lainnya, sehingga dijaga pertama. Prinsip lain tetap wajib dilindungi."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-pai9-penerapan",
     "prompt": "Kelompokkan contoh penerapan berikut menurut prinsip yang dijaga.",
     "buckets": [
         {"id": "agama", "label": "Agama"},
         {"id": "jiwa", "label": "Jiwa"},
         {"id": "akal", "label": "Akal"},
         {"id": "keturunan", "label": "Keturunan"},
         {"id": "harta", "label": "Harta"},
     ],
     "items": [
         {"id": "c1", "text": "Menjaga ibadah dan mempelajari ajarannya", "bucket": "agama"},
         {"id": "c2", "text": "Menjaga kesehatan dan tidak menyakiti diri", "bucket": "jiwa"},
         {"id": "c3", "text": "Menjauhi minuman keras dan belajar tekun", "bucket": "akal"},
         {"id": "c4", "text": "Menjaga pergaulan dan kehormatan diri", "bucket": "keturunan"},
         {"id": "c5", "text": "Menghindari pemborosan dan mengatur uang saku", "bucket": "harta"},
     ],
     "feedback": {
         "correct": "Benar — setiap contoh menjaga satu prinsip: agama, jiwa, akal, keturunan, atau harta.",
         "wrong": "Cocokkan: ibadah → agama, kesehatan → jiwa, minuman keras → akal, pergaulan → keturunan, uang → harta.",
     }},
    {"type": "checkpoint", "id": "cp-pai9-terkait",
     "question": "Mengapa kerusakan akal berisiko merusak jiwa?",
     "choices": [
         {"id": "a", "text": "Karena akal yang rusak dapat mendorong perilaku yang membahayakan diri", "correct": True},
         {"id": "b", "text": "Karena akal dan jiwa tidak berhubungan"},
         {"id": "c", "text": "Karena jiwa hanya dijaga oleh harta"},
     ],
     "explanation": "Prinsip saling terkait: akal yang rusak dapat mendorong perilaku berbahaya sehingga jiwa ikut terancam. Karena itu perlindungan harus menyeluruh."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-pai9-masalah",
     "prompt": "Urutkan langkah menyelesaikan masalah dengan lima prinsip.",
     "items": [
         {"id": "s1", "text": "Mengidentifikasi masalah yang dihadapi"},
         {"id": "s2", "text": "Menentukan prinsip yang berkaitan"},
         {"id": "s3", "text": "Menimbang dampak setiap pilihan"},
         {"id": "s4", "text": "Memilih jalan yang paling menjaga kelima prinsip"},
         {"id": "s5", "text": "Mengevaluasi hasil dan memperbaiki bila perlu"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — identifikasi masalah, tentukan prinsip, timbang dampak, pilih, lalu evaluasi.",
         "wrong": "Mulai dari mengidentifikasi masalah, lalu tentukan prinsip yang berkaitan dan timbang dampaknya.",
     }},
    {"type": "scenario", "id": "sc-pai9-zat",
     "title": "Tekanan teman untuk mencoba zat berbahaya",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Di sebuah acara, teman menawarkan minuman yang katanya membuat lebih percaya diri. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menolak karena menjaga akal dan jiwa", "next": "n2", "score": 2,
               "feedback": "Ajakan itu menyangkut hifzhu al-aql dan hifzhu al-nafs; menolak menjaga keduanya."},
              {"text": "Mencoba sedikit karena penasaran", "next": "n3", "score": 0,
               "feedback": "Rasa penasaran tidak sebanding dengan risiko kerusakan akal dan jiwa."},
              {"text": "Menolak, tetapi tetap bergaul dengan lingkaran itu", "next": "n4", "score": 1,
               "feedback": "Menolak itu benar, tetapi lingkungan yang sama akan terus menekan."},
          ]},
         {"id": "n2", "text": "Temanmu mendesak dengan alasan solidaritas. Apa langkahmu?",
          "choices": [
              {"text": "Menegaskan penolakan dengan santun dan meninggalkan acara", "next": "n5", "score": 2,
               "feedback": "Penolakan santun disertai menjauh dari tekanan menjaga akal dan jiwa sekaligus hubungan baik."},
              {"text": "Menghina teman agar berhenti mendesak", "next": "n6", "score": 0,
               "feedback": "Menolak dengan menghina merusak hubungan dan bukan cara yang benar."},
          ]},
         {"id": "n3", "text": "Kamu merasa tidak nyaman setelah mencoba. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Berhenti, minta bantuan orang tua atau guru, dan memperbaiki diri", "next": "n5", "score": 1,
               "feedback": "Berhenti dan meminta bantuan adalah langkah perbaikan yang tepat."},
              {"text": "Mencoba lagi karena sudah pernah", "next": "n7", "score": 0,
               "feedback": "Sudah pernah mencoba bukan alasan melanjutkan; risiko justru bertambah."},
          ]},
         {"id": "n4", "text": "Beberapa hari kemudian ajakan itu muncul lagi. Apa keputusanmu?",
          "choices": [
              {"text": "Menjauh dari lingkaran itu dan mencari kegiatan positif", "next": "n5", "score": 2,
               "feedback": "Mengganti lingkungan adalah cara menjaga diri secara menyeluruh."},
              {"text": "Ikut sekali lagi agar tidak dikucilkan", "next": "n7", "score": 0,
               "feedback": "Takut dikucilkan membuat tekanan mengendalikan pilihan."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Akal dan jiwa terjaga. Kamu juga belajar menolak dengan cara yang santun dan mencari lingkungan yang sehat."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Ajakan ditolak, tetapi caranya melukai hubungan. Perbaiki dengan penolakan yang santun."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Tekanan teman menguasai keputusan. Risiko terhadap akal dan jiwa makin besar."},
     ]},
    {"type": "challenge", "id": "ch-pai9-khamsah",
     "title": "Tantangan Kilat: Lima Prinsip Dasar",
     "time_limit": 90,
     "items": [
         {"question": "Lima prinsip dasar dalam hukum Islam disebut al-kulliyatu…", "answer": "al-khamsah"},
         {"question": "Menjaga agama disebut hifzhu…", "answer": "al-din"},
         {"question": "Menjaga jiwa disebut hifzhu…", "answer": "al-nafs"},
         {"question": "Menjaga akal disebut hifzhu…", "answer": "al-aql"},
         {"question": "Menjaga keturunan disebut hifzhu…", "answer": "al-nasl"},
         {"question": "Menjaga harta disebut hifzhu…", "answer": "al-mal"},
     ],
     "feedback": {
         "correct": "Tepat — agama, jiwa, akal, keturunan, dan harta dilindungi bersama-sama.",
         "wrong": "Ingat pasangannya: din = agama, nafs = jiwa, aql = akal, nasl = keturunan, mal = harta.",
     }},
])
save(path, data)

# ── PAI 10 — Wali Songo ───────────────────────────────────────────────
path = 'pai-10-wali-songo.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pai10-kunci", "engine": "mermaid",
     "title": "Empat kunci keberhasilan dakwah Wali Songo",
     "code": "flowchart TD\n  A[Wali Songo] --> B[Pendekatan budaya yang akrab]\n  A --> C[Dakwah bertahap dan sabar]\n  A --> D[Keteladanan perilaku sederhana]\n  A --> E[Pendidikan lewat pesantren]\n  E --> F[Melahirkan dai lintas generasi]"},
    {"type": "glossary", "terms": [
        {"term": "Wali Songo", "definition": "Sembilan wali penyebar Islam di Jawa yang berdakwah dengan pendekatan budaya."},
        {"term": "Dakwah", "definition": "Upaya menyampaikan dan mengajak kepada ajaran Islam dengan cara yang bijak."},
        {"term": "Pesantren", "definition": "Lembaga pendidikan Islam yang melahirkan dai sehingga dakwah berlanjut lintas generasi."},
        {"term": "Dai", "definition": "Penyampai ajaran Islam yang dibina melalui pendidikan."},
    ]},
    {"type": "categorize", "id": "cat-pai10-wali",
     "prompt": "Kelompokkan Wali Songo menurut pendekatan dakwah yang menonjol.",
     "buckets": [
         {"id": "pendidikan", "label": "Pendidikan"},
         {"id": "budaya", "label": "Seni dan budaya"},
         {"id": "sosial", "label": "Kepedulian sosial"},
         {"id": "wilayah", "label": "Wilayah dakwah"},
     ],
     "items": [
         {"id": "w1", "text": "Sunan Gresik — membuka jalan melalui pendidikan", "bucket": "pendidikan"},
         {"id": "w2", "text": "Sunan Giri — pesantren dan permainan anak", "bucket": "pendidikan"},
         {"id": "w3", "text": "Sunan Bonang — gamelan dan tembang", "bucket": "budaya"},
         {"id": "w4", "text": "Sunan Kalijaga — wayang dan gamelan", "bucket": "budaya"},
         {"id": "w5", "text": "Sunan Kudus — menghormati tradisi masyarakat", "bucket": "budaya"},
         {"id": "w6", "text": "Sunan Drajat — peduli fakir miskin dan anak yatim", "bucket": "sosial"},
         {"id": "w7", "text": "Sunan Muria — masyarakat pedesaan dan pegunungan", "bucket": "sosial"},
         {"id": "w8", "text": "Sunan Ampel — berdakwah di Ampel Denta, Surabaya", "bucket": "wilayah"},
         {"id": "w9", "text": "Sunan Gunung Jati — Cirebon dan Banten", "bucket": "wilayah"},
     ],
     "feedback": {
         "correct": "Benar — setiap wali menonjol pada satu pendekatan, tetapi semuanya memakai cara damai.",
         "wrong": "Perhatikan kata kuncinya: pendidikan, gamelan/wayang/tradisi, kepedulian sosial, atau nama wilayah.",
     }},
    {"type": "checkpoint", "id": "cp-pai10-sembilan",
     "question": "Wali Songo berarti…",
     "choices": [
         {"id": "a", "text": "Sembilan wali penyebar Islam di Jawa", "correct": True},
         {"id": "b", "text": "Sembilan kerajaan Islam di Jawa"},
         {"id": "c", "text": "Sembilan kitab tasawuf"},
     ],
     "explanation": "Wali Songo adalah sembilan wali penyebar Islam di Jawa. Mereka berdakwah melalui budaya, pendidikan, dan keteladanan tanpa memaksa."},
])

add_blocks(data, 1, [
    {"type": "glossary", "terms": [
        {"term": "Bi al-hikmah", "definition": "Cara dakwah yang bijak dan tepat sasaran."},
        {"term": "Al-mau'idlatil hasanah", "definition": "Nasihat yang baik dan menyentuh hati."},
        {"term": "Mujadalah ahsan", "definition": "Berdiskusi dengan cara terbaik tanpa menyerang."},
    ]},
    {"type": "checkpoint", "id": "cp-pai10-hikmah",
     "question": "Dakwah dengan cara bijak dan tepat sasaran disebut…",
     "choices": [
         {"id": "a", "text": "Bi al-hikmah", "correct": True},
         {"id": "b", "text": "Mujadalah ahsan"},
         {"id": "c", "text": "Al-mau'idlatil hasanah"},
     ],
     "explanation": "Bi al-hikmah berarti cara bijak dan tepat sasaran; al-mau'idlatil hasanah adalah nasihat yang baik; mujadalah ahsan adalah diskusi dengan cara terbaik."},
    {"type": "sort", "id": "srt-pai10-strategi",
     "prompt": "Urutkan strategi dakwah damai.",
     "items": [
         {"id": "s1", "text": "Mengenali bahasa dan budaya masyarakat"},
         {"id": "s2", "text": "Memilih media yang akrab"},
         {"id": "s3", "text": "Menyampaikan ajaran bertahap dengan hikmah"},
         {"id": "s4", "text": "Menjadi teladan dalam perilaku"},
         {"id": "s5", "text": "Membina masyarakat melalui pendidikan dan kegiatan sosial"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — kenali masyarakat, pilih media akrab, sampaikan bertahap, beri teladan, lalu bina.",
         "wrong": "Mulai dari mengenali bahasa dan budaya, lalu media akrab dan penyampaian bertahap.",
     }},
    {"type": "categorize", "id": "cat-pai10-moderat",
     "prompt": "Kelompokkan sikap berikut sesuai atau tidak sesuai dengan dakwah moderat.",
     "buckets": [
         {"id": "sesuai", "label": "Sesuai dakwah moderat"},
         {"id": "tidak", "label": "Tidak sesuai"},
     ],
     "items": [
         {"id": "m1", "text": "Dakwah tanpa paksaan", "bucket": "sesuai"},
         {"id": "m2", "text": "Menjaga adat yang tidak bertentangan dengan syariat", "bucket": "sesuai"},
         {"id": "m3", "text": "Memberi nasihat yang baik dan menyentuh hati", "bucket": "sesuai"},
         {"id": "m4", "text": "Memaksa orang beribadah", "bucket": "tidak"},
         {"id": "m5", "text": "Menempatkan adat di atas agama", "bucket": "tidak"},
         {"id": "m6", "text": "Menghapus seluruh adat masyarakat", "bucket": "tidak"},
     ],
     "feedback": {
         "correct": "Benar — dakwah moderat mengajak dengan kesadaran dan menghormati adat yang tidak melanggar syariat.",
         "wrong": "Tanpa paksaan, nasihat baik, dan adat yang tidak bertentangan dengan syariat adalah ciri dakwah moderat.",
     }},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-pai10-dampak",
     "question": "Dampak dakwah Wali Songo terhadap budaya masyarakat adalah…",
     "choices": [
         {"id": "a", "text": "Budaya yang tidak bertentangan dengan Islam tetap dilestarikan", "correct": True},
         {"id": "b", "text": "Seluruh budaya lama dihapus"},
         {"id": "c", "text": "Budaya dijadikan pengganti ajaran Islam"},
     ],
     "explanation": "Wali Songo melestarikan budaya yang tidak bertentangan dengan Islam, sehingga dakwah diterima luas tanpa mencabut akar budaya masyarakat."},
    {"type": "scenario", "id": "sc-pai10-berbeda",
     "title": "Menghargai teman yang berbeda keyakinan",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kelasmu punya teman yang berbeda keyakinan. Ia sedang merayakan hari besarnya. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menghormati dan tetap berteman baik", "next": "n2", "score": 2,
               "feedback": "Menghargai perbedaan keyakinan adalah keteladanan Wali Songo dalam bermasyarakat."},
              {"text": "Menjauhinya karena berbeda keyakinan", "next": "n3", "score": 0,
               "feedback": "Menjauh karena berbeda keyakinan bertentangan dengan sikap menghargai perbedaan."},
              {"text": "Diam saja agar tidak salah bicara", "next": "n4", "score": 1,
               "feedback": "Diam tidak merusak, tetapi belum menunjukkan sikap menghargai secara nyata."},
          ]},
         {"id": "n2", "text": "Seorang teman mengajakmu menghina keyakinan orang lain di grup kelas. Bagaimana sikapmu?",
          "choices": [
              {"text": "Menolak dan mengingatkan agar tidak menghina", "next": "n5", "score": 2,
               "feedback": "Menolak ujaran kebencian adalah wujud dakwah santun dan menjaga persatuan."},
              {"text": "Ikut tertawa agar tidak dianggap sok suci", "next": "n6", "score": 0,
               "feedback": "Ikut menghina keyakinan orang lain merusak persatuan dan melanggar akhlak."},
          ]},
         {"id": "n3", "text": "Temanmu menyadari sikapmu dan bertanya mengapa kamu menjauh. Apa jawabmu?",
          "choices": [
              {"text": "Meminta maaf dan menjelaskan bahwa perbedaan bukan alasan menjauh", "next": "n2", "score": 1,
               "feedback": "Mengakui kekeliruan memulihkan hubungan dan menunjukkan keteladanan."},
              {"text": "Mengatakan bahwa keyakinannya yang membuatmu menjauh", "next": "n7", "score": 0,
               "feedback": "Menjadikan keyakinan orang lain sebagai alasan menjauh melukai dan tidak adil."},
          ]},
         {"id": "n4", "text": "Guru membahas pentingnya menghargai perbedaan. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mulai berteman dan bekerja sama tanpa membedakan keyakinan", "next": "n5", "score": 2,
               "feedback": "Bekerja sama tanpa membedakan keyakinan mewujudkan sikap menghargai perbedaan."},
              {"text": "Tetap menjaga jarak agar aman", "next": "n6", "score": 1,
               "feedback": "Aman untuk diri sendiri, tetapi belum melatih sikap menghargai perbedaan."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kamu menghargai perbedaan dan menjaga persatuan. Kebaikan tersampaikan lewat keteladanan, bukan paksaan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Tidak terjadi konflik, tetapi sikapmu belum sepenuhnya mencerminkan keteladanan ulama."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Temanmu terluka dan hubungan memanas. Perbedaan keyakinan tidak boleh menjadi alasan merendahkan."},
     ]},
    {"type": "challenge", "id": "ch-pai10-walisongo",
     "title": "Tantangan Kilat: Wali Songo",
     "time_limit": 90,
     "items": [
         {"question": "Wali Songo berarti sembilan…", "answer": "wali"},
         {"question": "Sunan yang berdakwah melalui wayang dan gamelan adalah Sunan…", "answer": "kalijaga"},
         {"question": "Sunan yang berdakwah melalui gamelan dan tembang adalah Sunan…", "answer": "bonang"},
         {"question": "Sunan yang membuka jalan dakwah melalui pendidikan adalah Sunan…", "answer": "gresik"},
         {"question": "Dakwah dengan cara bijak dan tepat sasaran disebut bi al-…", "answer": "hikmah"},
         {"question": "Nasihat yang baik dan menyentuh hati disebut al-mau'idlatil…", "answer": "hasanah"},
     ],
     "feedback": {
         "correct": "Tepat — dakwah Wali Songo damai, bertahap, dan menghargai budaya yang tidak melanggar syariat.",
         "wrong": "Ingat: Kalijaga, Bonang, Gresik, bi al-hikmah, dan al-mau'idlatil hasanah.",
     }},
])
save(path, data)

print('batch 7b: PAI 6 sampai PAI 10 selesai')
