"""Fase 5.1 batch 2b — blok interaktif untuk BIO 1, BIO 2, BIO 3.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b2b.py`
lalu `php artisan gamecenter:materi-import`.
"""
import json
import io

BASE = 'database/seeders/data/sma-smk/fase-e/'


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


# ── BIO 1 — Virus dan Peranannya ───────────────────────────────────────
path = 'biologi/bio-1-virus-peranannya.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-struktur-virus", "engine": "mermaid",
     "title": "Bagian-bagian virus",
     "code": "flowchart TD\n  V[Virus] --> G[Materi genetik: DNA atau RNA]\n  V --> K[Kapsid: selubung protein]\n  K --> S[Kadang selubung lipid tambahan]\n  V --> R[Membutuhkan reseptor sel hidup]"},
    {"type": "glossary", "terms": [
        {"term": "Kapsid", "definition": "Selubung protein yang membungkus materi genetik virus."},
        {"term": "Parasit obligat intraseluler", "definition": "Organisme yang hanya dapat bereproduksi di dalam sel hidup lain."},
        {"term": "Bakteriofag", "definition": "Virus yang menyerang bakteri."},
        {"term": "Viroida", "definition": "Partikel infeksius berupa RNA tanpa kapsid yang menyerang tanaman."},
    ]},
    {"type": "checkpoint", "id": "cp-virus-parasit",
     "question": "Mengapa virus disebut parasit obligat intraseluler?",
     "choices": [
         {"id": "a", "text": "Karena tidak punya ribosom dan metabolisme sendiri, sehingga harus memakai sel hidup", "correct": True},
         {"id": "b", "text": "Karena virus selalu menyerang manusia"},
         {"id": "c", "text": "Karena virus dapat membuat makanan sendiri"},
     ],
     "explanation": "Virus tidak memiliki sitoplasma, ribosom, maupun mitokondria. Tanpa sel inang ia tidak dapat menyintesis protein atau menggandakan diri."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-litik",
     "prompt": "Urutkan tahap siklus litik.",
     "items": [
         {"id": "s1", "text": "Adsorpsi — virus menempel pada reseptor sel inang"},
         {"id": "s2", "text": "Penetrasi — materi genetik virus masuk"},
         {"id": "s3", "text": "Sintesis — sel inang membuat bagian-bagian virus"},
         {"id": "s4", "text": "Perakitan — bagian-bagian disusun menjadi virion"},
         {"id": "s5", "text": "Lisis — sel inang pecah dan virus keluar"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Tepat: menempel, masuk, menyintesis, merakit, lalu memecahkan sel.",
         "wrong": "Mulai dari adsorpsi, dan ingat lisis selalu tahap terakhir karena sel inang pecah.",
     }},
    {"type": "checkpoint", "id": "cp-lisogenik",
     "question": "Ciri khas siklus lisogenik adalah…",
     "choices": [
         {"id": "a", "text": "Materi genetik virus menyisip ke DNA inang tanpa segera membunuhnya", "correct": True},
         {"id": "b", "text": "Sel inang langsung pecah pada tahap pertama"},
         {"id": "c", "text": "Virus tidak membutuhkan sel inang"},
     ],
     "explanation": "Pada lisogenik, DNA virus menyisip dan ikut diperbanyak bersama sel inang. Virus dapat aktif kembali dan berpindah ke siklus litik."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-virus-cepat",
     "title": "Tantangan Kilat: Istilah Virus",
     "time_limit": 80,
     "items": [
         {"question": "Virus yang menyerang bakteri disebut …", "answer": "bakteriofag"},
         {"question": "Selubung protein virus disebut …", "answer": "kapsid"},
         {"question": "Malaria disebabkan oleh …", "answer": "plasmodium"},
         {"question": "Materi genetik virus berupa DNA atau …", "answer": "rna"},
         {"question": "Viroida hanya berupa RNA tanpa …", "answer": "kapsid"},
     ],
     "feedback": {
         "correct": "Tepat — istilah kunci virus sudah dikuasai.",
         "wrong": "Ulangi bagian struktur virus: kapsid, materi genetik, bakteriofag, viroida.",
     }},
])
save(path, data)

# ── BIO 2 — Keanekaragaman Hayati ──────────────────────────────────────
path = 'biologi/bio-2-keanekaragaman-hayati.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-tingkat-hayati", "engine": "mermaid",
     "title": "Tiga tingkat keanekaragaman hayati",
     "code": "flowchart TD\n  A[Keanekaragaman hayati] --> B[Tingkat gen]\n  A --> C[Tingkat jenis]\n  A --> D[Tingkat ekosistem]\n  B --> B1[Variasi dalam satu spesies]\n  C --> C1[Berbagai spesies dalam satu famili]\n  D --> D1[Mangrove, sawah, padang rumput]"},
    {"type": "glossary", "terms": [
        {"term": "Endemik", "definition": "Spesies yang hanya hidup secara alami di wilayah tertentu, misalnya komodo."},
        {"term": "Taksonomi", "definition": "Ilmu pengelompokan makhluk hidup berdasarkan persamaan ciri."},
        {"term": "Genus", "definition": "Takson di atas spesies yang mengelompokkan spesies berkerabat dekat."},
        {"term": "Jasa ekosistem", "definition": "Manfaat ekosistem bagi manusia, seperti penyerbukan dan pengaturan air."},
    ]},
    {"type": "checkpoint", "id": "cp-endemik",
     "question": "Komodo hanya hidup alami di Nusa Tenggara. Status ini disebut…",
     "choices": [
         {"id": "a", "text": "Endemik", "correct": True},
         {"id": "b", "text": "Kosmopolitan"},
         {"id": "c", "text": "Invasif"},
     ],
     "explanation": "Endemik berarti penyebaran alaminya terbatas pada satu wilayah. Karena itu kehilangan habitat di wilayah tersebut langsung mengancam jenisnya."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-taksonomi",
     "prompt": "Urutkan takson dari yang paling umum ke paling khusus.",
     "items": [
         {"id": "t1", "text": "Kingdom"},
         {"id": "t2", "text": "Filum"},
         {"id": "t3", "text": "Kelas"},
         {"id": "t4", "text": "Ordo"},
         {"id": "t5", "text": "Famili"},
         {"id": "t6", "text": "Genus"},
         {"id": "t7", "text": "Spesies"},
     ],
     "answer": ["t1", "t2", "t3", "t4", "t5", "t6", "t7"],
     "feedback": {
         "correct": "Benar: semakin ke bawah, anggota makin sedikit tetapi ciri persamaannya makin banyak.",
         "wrong": "Ingat urutan Kingdom → Filum → Kelas → Ordo → Famili → Genus → Spesies.",
     }},
    {"type": "checkpoint", "id": "cp-rantai-energi",
     "question": "Pada rantai makanan padi → tikus → ular → elang, panah menunjukkan…",
     "choices": [
         {"id": "a", "text": "Arah perpindahan energi dari yang dimakan ke pemakannya", "correct": True},
         {"id": "b", "text": "Arah perpindahan suhu lingkungan"},
         {"id": "c", "text": "Jumlah populasi setiap jenis"},
     ],
     "explanation": "Panah selalu menunjuk pemakan, yaitu arah energi berpindah. Rantai makanan selalu diawali produsen karena hanya produsen yang menangkap energi matahari."},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-in-situ",
     "prompt": "Kelompokkan upaya pelestarian berikut.",
     "buckets": [
         {"id": "insitu", "label": "In situ"},
         {"id": "exsitu", "label": "Ex situ"},
     ],
     "items": [
         {"id": "c1", "text": "Taman nasional", "bucket": "insitu"},
         {"id": "c2", "text": "Kebun binatang", "bucket": "exsitu"},
         {"id": "c3", "text": "Cagar alam", "bucket": "insitu"},
         {"id": "c4", "text": "Penangkaran hewan", "bucket": "exsitu"},
         {"id": "c5", "text": "Bank benih", "bucket": "exsitu"},
         {"id": "c6", "text": "Restorasi mangrove di habitat aslinya", "bucket": "insitu"},
     ],
     "feedback": {
         "correct": "Benar — in situ menjaga ekosistem asli, ex situ memindahkan individu ke luar habitat.",
         "wrong": "Tanyakan: apakah individu tetap di habitat aslinya? Jika ya, in situ.",
     }},
    {"type": "scenario", "id": "sc-ular-sawah",
     "title": "Ular hilang, tikus meledak",
     "start": "n1",
     "nodes": [
         {"id": "n1",
          "text": "Petani mengeluh populasi tikus meledak setelah banyak ular ditangkap untuk dijual. Apa tindakanmu sebagai anggota kelompok pelestarian?",
          "choices": [
              {"text": "Mengembalikan ular dan menjaga habitat sawah", "next": "n2", "score": 2,
               "feedback": "Predator alami menjaga populasi di bawahnya — ini pengendalian hayati, bukan sekadar menambah racun."},
              {"text": "Menyemprot pestisida dosis tinggi", "next": "n3", "score": 0,
               "feedback": "Pestisida membunuh tikus, tetapi juga serangga penyerbuk dan musuh alami lain."},
              {"text": "Menangkap lebih banyak ular untuk dijual", "next": "n4", "score": 0,
               "feedback": "Menjual predator justru memperparah ledakan hama di sawah."},
          ]},
         {"id": "n2",
          "text": "Ular kembali, tetapi sebagian petani takut dan ingin membunuhnya. Langkahmu?",
          "choices": [
              {"text": "Sosialisasi peran ular sebagai predator alami", "next": "n5", "score": 2,
               "feedback": "Penjelasan menurunkan ketakutan dan membuat warga ikut menjaga predator."},
              {"text": "Membiarkan tanpa penjelasan", "next": "n6", "score": 1,
               "feedback": "Populasi pulih, tetapi tanpa pemahaman warga, ular bisa kembali dibunuh."},
          ]},
         {"id": "n3",
          "text": "Tikus berkurang, tetapi serangga penyerbuk ikut mati dan biaya pestisida naik. Langkahmu?",
          "choices": [
              {"text": "Beralih ke pengendalian hayati bersama predator alami", "next": "n5", "score": 1,
               "feedback": "Koreksi tepat: kembalikan keseimbangan ekosistem, bukan menambah bahan kimia."},
              {"text": "Menambah dosis pestisida", "next": "n7", "score": 0,
               "feedback": "Dosis lebih tinggi memperbesar kerusakan ekosistem dan biaya petani."},
          ]},
         {"id": "n4",
          "text": "Penangkapan makin banyak, tikus makin banyak, dan petani mulai merugi. Langkahmu?",
          "choices": [
              {"text": "Menghentikan penangkapan dan memulihkan habitat", "next": "n5", "score": 1,
               "feedback": "Menghentikan pemicu masalah adalah langkah pertama yang benar."},
              {"text": "Melanjutkan penjualan karena untung", "next": "n7", "score": 0,
               "feedback": "Keuntungan jangka pendek dibayar dengan gagal panen berulang."},
          ]},
         {"id": "n5", "text": "Ular kembali, tikus terkendali, dan petani menghemat biaya pestisida. Rantai makanan pulih.", "end": True, "outcome": "good"},
         {"id": "n6", "text": "Populasi ular pulih, tetapi ketakutan warga masih ada sehingga sebagian ular kembali dibunuh.", "end": True, "outcome": "neutral"},
         {"id": "n7", "text": "Hama makin kebal, biaya naik, dan penyerbuk hilang sehingga hasil panen menurun.", "end": True, "outcome": "bad"},
     ]},
])
save(path, data)

# ── BIO 3 — Perubahan Iklim ────────────────────────────────────────────
path = 'biologi/bio-3-perubahan-iklim.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-efek-rumah-kaca", "engine": "mermaid",
     "title": "Alur efek rumah kaca",
     "code": "flowchart LR\n  A[Cahaya matahari] --> B[Permukaan bumi]\n  B --> C[Panas inframerah dipancarkan]\n  C --> D[Gas rumah kaca menahan panas]\n  D --> B"},
    {"type": "glossary", "terms": [
        {"term": "Pemanasan global", "definition": "Kenaikan suhu rata-rata atmosfer dan permukaan bumi."},
        {"term": "Gas rumah kaca", "definition": "Gas yang meneruskan cahaya matahari tetapi menahan panas inframerah, misalnya CO₂ dan CH₄."},
        {"term": "Rosot karbon", "definition": "Penyerap karbon alami seperti hutan yang menyerap CO₂ melalui fotosintesis."},
        {"term": "Mitigasi", "definition": "Tindakan mengurangi penyebab perubahan iklim, misalnya memakai energi terbarukan."},
    ]},
    {"type": "checkpoint", "id": "cp-grk-bukan",
     "question": "Gas berikut yang BUKAN gas rumah kaca adalah…",
     "choices": [
         {"id": "a", "text": "Oksigen (O₂)", "correct": True},
         {"id": "b", "text": "Karbon dioksida (CO₂)"},
         {"id": "c", "text": "Metana (CH₄)"},
     ],
     "explanation": "Oksigen dan nitrogen tidak menyerap panas inframerah secara berarti. Gas rumah kaca utama adalah CO₂, CH₄, dan N₂O."},
])

add_blocks(data, 1, [
    {"type": "checkpoint", "id": "cp-karang",
     "question": "Pemutihan terumbu karang (coral bleaching) terjadi karena…",
     "choices": [
         {"id": "a", "text": "Suhu air laut naik sehingga karang melepas alga simbiotiknya", "correct": True},
         {"id": "b", "text": "Karang kekurangan cahaya matahari"},
         {"id": "c", "text": "Karang berpindah ke perairan yang lebih dingin"},
     ],
     "explanation": "Karang bergantung pada alga simbiotik untuk makanan dan warna. Saat suhu naik, alga dilepas sehingga karang memutih dan rentan mati."},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-mitigasi-adaptasi",
     "prompt": "Kelompokkan tindakan berikut sebagai mitigasi atau adaptasi.",
     "buckets": [
         {"id": "mitigasi", "label": "Mitigasi"},
         {"id": "adaptasi", "label": "Adaptasi"},
     ],
     "items": [
         {"id": "c1", "text": "Memakai energi terbarukan", "bucket": "mitigasi"},
         {"id": "c2", "text": "Menanam varietas tahan kekeringan", "bucket": "adaptasi"},
         {"id": "c3", "text": "Memakai transportasi publik", "bucket": "mitigasi"},
         {"id": "c4", "text": "Mengatur jadwal tanam berdasarkan prakiraan cuaca", "bucket": "adaptasi"},
         {"id": "c5", "text": "Menanam dan merestorasi mangrove", "bucket": "mitigasi"},
         {"id": "c6", "text": "Membangun perlindungan pesisir", "bucket": "adaptasi"},
     ],
     "feedback": {
         "correct": "Benar — mitigasi menyerang penyebab, adaptasi menyesuaikan diri dengan dampak.",
         "wrong": "Tanyakan: tindakan ini menurunkan emisi (mitigasi) atau mengurangi kerugian akibat dampak (adaptasi)?",
     }},
    {"type": "scenario", "id": "sc-aksi-iklim-sekolah",
     "title": "Dana kecil untuk program iklim sekolah",
     "start": "n1",
     "nodes": [
         {"id": "n1",
          "text": "Sekolah memberi dana kecil untuk program peduli iklim. Kamu ketua tim. Langkah pertama?",
          "choices": [
              {"text": "Audit pemakaian listrik lalu ganti lampu hemat energi", "next": "n2", "score": 2,
               "feedback": "Mitigasi paling terukur: listrik sekolah sebagian besar berasal dari bahan bakar fosil."},
              {"text": "Membeli banyak bibit pohon tanpa rencana perawatan", "next": "n3", "score": 1,
               "feedback": "Menanam pohon itu baik, tetapi tanpa perawatan bibit mati dan karbon tidak terserap."},
              {"text": "Membuat poster ajakan saja", "next": "n4", "score": 0,
               "feedback": "Kampanye tanpa tindakan dan pengukuran tidak menurunkan emisi."},
          ]},
         {"id": "n2",
          "text": "Listrik turun 12% dan sisa dana masih ada. Apa langkah berikutnya?",
          "choices": [
              {"text": "Menanam pohon disertai jadwal perawatan dan pencatatan", "next": "n5", "score": 2,
               "feedback": "Gabungan efisiensi energi dan penyerapan karbon memberi hasil yang bisa diukur."},
              {"text": "Menyimpan sisa dana tanpa evaluasi", "next": "n6", "score": 1,
               "feedback": "Hasil awal baik, tetapi tanpa evaluasi program berhenti di satu titik."},
          ]},
         {"id": "n3",
          "text": "Sebagian bibit mati karena tidak dirawat. Apa tindakanmu?",
          "choices": [
              {"text": "Membuat jadwal perawatan dan menghitung pohon yang hidup", "next": "n5", "score": 1,
               "feedback": "Memperbaiki dengan data membuat program berikutnya lebih berhasil."},
              {"text": "Membiarkan karena bibit sudah dibeli", "next": "n7", "score": 0,
               "feedback": "Tanpa perawatan, dana terbuang dan penyerapan karbon tetap nol."},
          ]},
         {"id": "n4",
          "text": "Poster terpasang, tetapi tidak ada perubahan yang bisa diukur. Apa langkahmu?",
          "choices": [
              {"text": "Memulai audit listrik dan mencatat hasilnya", "next": "n5", "score": 1,
               "feedback": "Tindakan terukur lebih berdampak daripada ajakan tanpa bukti."},
              {"text": "Tetap fokus pada poster", "next": "n7", "score": 0,
               "feedback": "Tanpa pengukuran, sekolah tidak tahu apakah programnya bekerja."},
          ]},
         {"id": "n5", "text": "Listrik turun, pohon terawat, dan hasilnya dicatat. Sekolah punya bukti untuk melanjutkan program.", "end": True, "outcome": "good"},
         {"id": "n6", "text": "Lampu hemat energi bertahan, tetapi tidak ada program lanjutan karena hasil tidak dievaluasi.", "end": True, "outcome": "neutral"},
         {"id": "n7", "text": "Dana habis tanpa hasil terukur, dan sekolah kehilangan kepercayaan pada program iklim.", "end": True, "outcome": "bad"},
     ]},
])
save(path, data)

print('batch 2b: BIO 1, BIO 2, BIO 3 selesai')