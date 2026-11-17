"""Fase 5.1 batch 8 — blok interaktif untuk PAN 2, PAN 3, dan PAN 4.

Jalankan dari folder gamecenter:

    python ../tools/tambah-blok-fase5-b8.py
    python ../tools/rapikan-blok-fase5.py --apply
    php artisan gamecenter:materi-import
"""
import io
import json

BASE = 'database/seeders/data/sma-smk/fase-e/pancasila/'


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


# ── PAN 2 — Membangun Budaya Taat Hukum ───────────────────────────────
path = 'pan-2-budaya-taat-hukum.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "timeline", "id": "tl-pan2-konstitusi",
     "title": "Perjalanan konstitusi Indonesia",
     "items": [
         {"when": "18 Agustus 1945", "title": "UUD 1945 disahkan",
          "text": "PPKI mengesahkan UUD 1945 sebagai hukum dasar negara."},
         {"when": "1949", "title": "Konstitusi RIS",
          "text": "Indonesia berbentuk negara serikat dengan Konstitusi RIS."},
         {"when": "1950", "title": "UUDS 1950",
          "text": "Kembali ke bentuk negara kesatuan dengan UUDS 1950."},
         {"when": "5 Juli 1959", "title": "Dekrit Presiden",
          "text": "UUD 1945 kembali berlaku melalui Dekrit Presiden."},
         {"when": "1999–2002", "title": "Amandemen UUD 1945",
          "text": "UUD 1945 diperbarui melalui amandemen bertahap."},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Konstitusi", "definition": "Hukum dasar yang mengatur penyelenggaraan negara dan hubungan negara dengan warga negara."},
        {"term": "Konvensi", "definition": "Kebiasaan ketatanegaraan yang tidak tertulis tetapi dijalankan dalam praktik."},
        {"term": "Norma", "definition": "Aturan yang menjadi pedoman perilaku, dengan sumber dan sanksi masing-masing."},
    ]},
    {"type": "checkpoint", "id": "cp-pan2-konstitusi",
     "question": "Hukum dasar yang mengatur penyelenggaraan negara dan hubungan negara dengan warga negara disebut…",
     "choices": [
         {"id": "a", "text": "Konstitusi", "correct": True},
         {"id": "b", "text": "Konvensi"},
         {"id": "c", "text": "Peraturan daerah"},
     ],
     "explanation": "Konstitusi adalah hukum dasar. Tujuannya membatasi kekuasaan negara, menjamin hak warga, dan memberi kepastian hukum."},
    {"type": "categorize", "id": "cat-pan2-norma",
     "prompt": "Kelompokkan sumber dan contoh berikut menurut macam normanya.",
     "buckets": [
         {"id": "agama", "label": "Norma agama"},
         {"id": "kesusilaan", "label": "Norma kesusilaan"},
         {"id": "kesopanan", "label": "Norma kesopanan"},
         {"id": "hukum", "label": "Norma hukum"},
     ],
     "items": [
         {"id": "n1", "text": "Sumbernya Tuhan", "bucket": "agama"},
         {"id": "n2", "text": "Sumbernya hati nurani", "bucket": "kesusilaan"},
         {"id": "n3", "text": "Sumbernya kebiasaan masyarakat", "bucket": "kesopanan"},
         {"id": "n4", "text": "Sumbernya negara", "bucket": "hukum"},
         {"id": "n5", "text": "Mengucapkan permisi", "bucket": "kesopanan"},
         {"id": "n6", "text": "Melanggar lalu lintas", "bucket": "hukum"},
     ],
     "feedback": {
         "correct": "Benar — setiap norma punya sumber dan sanksi berbeda: agama, kesusilaan, kesopanan, dan hukum.",
         "wrong": "Agama bersumber dari Tuhan, kesusilaan dari hati nurani, kesopanan dari kebiasaan, hukum dari negara.",
     }},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-pan2-hierarki",
     "prompt": "Urutkan hierarki peraturan perundang-undangan dari tertinggi.",
     "items": [
         {"id": "s1", "text": "UUD NRI Tahun 1945"},
         {"id": "s2", "text": "TAP MPR"},
         {"id": "s3", "text": "Undang-Undang / Perppu"},
         {"id": "s4", "text": "Peraturan Pemerintah"},
         {"id": "s5", "text": "Peraturan Presiden"},
         {"id": "s6", "text": "Peraturan Daerah Provinsi"},
         {"id": "s7", "text": "Peraturan Daerah Kabupaten/Kota"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5", "s6", "s7"],
     "feedback": {
         "correct": "Benar — UUD 1945, TAP MPR, UU/Perppu, PP, Perpres, Perda Provinsi, lalu Perda Kabupaten/Kota.",
         "wrong": "Urutkan dari yang tertinggi: UUD 1945 → TAP MPR → UU/Perppu → PP → Perpres → Perda Provinsi → Perda Kabupaten/Kota.",
     }},
    {"type": "diagram", "id": "dg-pan2-hierarki", "engine": "mermaid",
     "title": "Pancasila sebagai sumber dari segala sumber hukum",
     "code": "flowchart TD\n  A[Pancasila: sumber segala sumber hukum] --> B[UUD NRI 1945]\n  B --> C[TAP MPR]\n  C --> D[UU dan Perppu]\n  D --> E[Peraturan Pemerintah]\n  E --> F[Peraturan Presiden]\n  F --> G[Perda Provinsi]\n  G --> H[Perda Kabupaten dan Kota]"},
    {"type": "checkpoint", "id": "cp-pan2-superior",
     "question": "Asas yang menyatakan peraturan lebih rendah tidak boleh bertentangan dengan peraturan lebih tinggi adalah…",
     "choices": [
         {"id": "a", "text": "Lex superior derogat legi inferiori", "correct": True},
         {"id": "b", "text": "Lex specialis derogat legi generali"},
         {"id": "c", "text": "Lex posterior derogat legi priori"},
     ],
     "explanation": "Lex superior mengatur hubungan antarjenjang. Lex specialis berarti aturan khusus mengesampingkan aturan umum, dan lex posterior berarti aturan baru mengesampingkan aturan lama."},
    {"type": "checkpoint", "id": "cp-pan2-perda",
     "question": "Jika peraturan daerah bertentangan dengan undang-undang, peraturan daerah itu…",
     "choices": [
         {"id": "a", "text": "Tidak sah dan harus dibatalkan", "correct": True},
         {"id": "b", "text": "Tetap berlaku karena dibuat lebih dulu"},
         {"id": "c", "text": "Otomatis mengubah undang-undang"},
     ],
     "explanation": "Karena kedudukannya lebih rendah, perda yang bertentangan dengan UU tidak sah dan harus dibatalkan agar tidak menimbulkan ketidakpastian hukum."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-pan2-kesepakatan",
     "prompt": "Urutkan langkah membuat kesepakatan bersama.",
     "items": [
         {"id": "s1", "text": "Membuka pertemuan dan menyepakati agenda"},
         {"id": "s2", "text": "Menampung semua pendapat tanpa memotong"},
         {"id": "s3", "text": "Membahas usulan dan mencari titik temu"},
         {"id": "s4", "text": "Menyetujui hasil musyawarah, sedapat mungkin mufakat"},
         {"id": "s5", "text": "Mencatat dan menandatangani kesepakatan"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — buka agenda, tampung pendapat, bahas, setujui, lalu catat dan tanda tangani.",
         "wrong": "Mulai dari membuka pertemuan dan agenda, lalu menampung pendapat sebelum membahas.",
     }},
    {"type": "checkpoint", "id": "cp-pan2-analisis",
     "question": "Saat menganalisis sebuah peraturan, pertanyaan yang tepat adalah…",
     "choices": [
         {"id": "a", "text": "Apakah peraturan melayani rakyat kebanyakan dan tidak melanggar hak?", "correct": True},
         {"id": "b", "text": "Apakah peraturan menguntungkan pejabat pembuatnya?"},
         {"id": "c", "text": "Apakah peraturan cukup panjang?"},
     ],
     "explanation": "Analisis peraturan menimbang tujuan negara, pelayanan kepada rakyat, perlindungan hak, dan kemungkinan pengawasan pelaksanaannya."},
    {"type": "challenge", "id": "ch-pan2-hukum",
     "title": "Tantangan Kilat: Konstitusi dan Norma",
     "time_limit": 90,
     "items": [
         {"question": "Hukum dasar negara disebut…", "answer": "konstitusi"},
         {"question": "UUD 1945 disahkan PPKI pada 18… 1945", "answer": "agustus"},
         {"question": "Norma yang bersumber dari hati nurani adalah norma…", "answer": "kesusilaan"},
         {"question": "Aturan khusus mengesampingkan aturan umum: lex… derogat legi generali", "answer": "specialis"},
         {"question": "Aturan baru mengesampingkan aturan lama: lex posterior derogat legi…", "answer": "priori"},
         {"question": "Taat hukum karena kesadaran, bukan karena…", "answer": "takut"},
     ],
     "feedback": {
         "correct": "Tepat — konstitusi, norma, dan asas peraturan menjaga kepastian hukum.",
         "wrong": "Ingat: konstitusi, norma kesusilaan, lex specialis, lex posterior, dan taat hukum karena kesadaran.",
     }},
])

add_blocks(data, 3, [
    {"type": "categorize", "id": "cat-pan2-sanksi",
     "prompt": "Kelompokkan pelanggaran berikut menurut norma dan sanksinya.",
     "buckets": [
         {"id": "hukum", "label": "Norma hukum — pidana"},
         {"id": "kesusilaan", "label": "Norma kesusilaan — rasa bersalah"},
         {"id": "kesopanan", "label": "Norma kesopanan — teguran"},
         {"id": "agama", "label": "Norma agama — dosa"},
     ],
     "items": [
         {"id": "s1", "text": "Mencuri", "bucket": "hukum"},
         {"id": "s2", "text": "Berbohong kepada orang tua", "bucket": "kesusilaan"},
         {"id": "s3", "text": "Tidak menghormati guru", "bucket": "kesopanan"},
         {"id": "s4", "text": "Meninggalkan ibadah", "bucket": "agama"},
     ],
     "feedback": {
         "correct": "Benar — sanksi mengikuti norma yang dilanggar, dari pidana sampai dosa.",
         "wrong": "Mencuri → hukum, berbohong kepada orang tua → kesusilaan, tidak menghormati guru → kesopanan, meninggalkan ibadah → agama.",
     }},
    {"type": "scenario", "id": "sc-pan2-lampu-merah",
     "title": "Lampu merah di jalan yang sepi",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Malam hari, jalan sangat sepi. Lampu merah menyala dan tidak ada kendaraan lain. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Tetap berhenti karena taat hukum adalah kesadaran", "next": "n2", "score": 2,
               "feedback": "Budaya taat hukum bukan karena takut petugas, melainkan karena kesadaran."},
              {"text": "Menerobos karena jalan sepi dan tidak ada petugas", "next": "n3", "score": 0,
               "feedback": "Menerobos saat tidak diawasi menunjukkan ketaatan hanya karena takut sanksi."},
              {"text": "Berhenti, tetapi hanya karena takut kamera tilang", "next": "n4", "score": 1,
               "feedback": "Berhenti itu benar, tetapi alasannya belum menunjukkan kesadaran hukum."},
          ]},
         {"id": "n2", "text": "Temanmu bertanya mengapa kamu tetap berhenti padahal sepi. Apa jawabmu?",
          "choices": [
              {"text": "Karena aturan berlaku tanpa menunggu ada petugas", "next": "n5", "score": 2,
               "feedback": "Aturan berlaku terus; kesadaran membuat kita taat tanpa pengawasan."},
              {"text": "Karena takut ditilang kalau ada kamera", "next": "n6", "score": 1,
               "feedback": "Takut sanksi masih lebih baik daripada melanggar, tetapi belum menjadi kesadaran."},
          ]},
         {"id": "n3", "text": "Di persimpangan berikutnya ada razia. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui pernah menerobos dan berjanji tidak mengulangi", "next": "n7", "score": 1,
               "feedback": "Mengakui dan memperbaiki diri adalah langkah menuju ketaatan yang sadar."},
              {"text": "Berhenti hanya saat ada razia dan menerobos lagi setelahnya", "next": "n8", "score": 0,
               "feedback": "Taat hanya saat diawasi bukan budaya taat hukum."},
          ]},
         {"id": "n4", "text": "Kamera ternyata tidak berfungsi. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Tetap berhenti karena aturan tetap berlaku", "next": "n5", "score": 2,
               "feedback": "Ketaatan tidak bergantung pada ada atau tidaknya pengawasan."},
              {"text": "Menerobos karena tidak akan tertangkap", "next": "n8", "score": 0,
               "feedback": "Melanggar saat tidak diawasi menunjukkan hukum hanya dipatuhi karena takut."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kamu taat karena kesadaran. Budaya taat hukum terbentuk dari kebiasaan kecil seperti ini."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Kamu berhenti, tetapi masih bergantung pada rasa takut. Kesadaran hukum perlu dilatih."},
         {"id": "n7", "end": True, "outcome": "neutral",
          "text": "Kamu mengakui kesalahan dan mulai memperbaiki diri. Itu langkah yang lebih baik."},
         {"id": "n8", "end": True, "outcome": "bad",
          "text": "Ketaatan hanya muncul saat diawasi. Pelanggaran akan terulang setiap kali tidak ada petugas."},
     ]},
])
save(path, data)

# ── PAN 3 — Mengelola Kebinekaan ──────────────────────────────────────
path = 'pan-3-mengelola-kebinekaan.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pan3-identitas", "engine": "mermaid",
     "title": "Dua jenis identitas dan pembentuknya",
     "code": "flowchart TD\n  A[Identitas] --> B[Given: diperoleh sejak lahir]\n  A --> C[Pilihan: dibentuk melalui usaha]\n  B --> B1[Suku bangsa, daerah asal, warna kulit, jenis kelamin]\n  C --> C1[Profesi, prestasi, keahlian]\n  D[Keluarga] --> A\n  E[Lingkungan sosial] --> A\n  F[Pengalaman hidup] --> A\n  G[Pendidikan] --> A"},
    {"type": "glossary", "terms": [
        {"term": "Identitas", "definition": "Ciri yang melekat pada diri seseorang atau kelompok yang membedakannya dari yang lain."},
        {"term": "Identitas given", "definition": "Identitas yang diperoleh sejak lahir dan tidak dipilih, seperti suku bangsa dan daerah asal."},
        {"term": "Identitas pilihan", "definition": "Identitas yang dibentuk melalui usaha, seperti profesi, prestasi, dan keahlian."},
        {"term": "Bhinneka Tunggal Ika", "definition": "Berbeda-beda tetapi tetap satu jua; persatuan tidak berarti penyeragaman."},
    ]},
    {"type": "categorize", "id": "cat-pan3-identitas",
     "prompt": "Kelompokkan contoh identitas berikut.",
     "buckets": [
         {"id": "given", "label": "Identitas given"},
         {"id": "pilihan", "label": "Identitas pilihan"},
     ],
     "items": [
         {"id": "i1", "text": "Suku bangsa", "bucket": "given"},
         {"id": "i2", "text": "Daerah asal", "bucket": "given"},
         {"id": "i3", "text": "Warna kulit", "bucket": "given"},
         {"id": "i4", "text": "Jenis kelamin", "bucket": "given"},
         {"id": "i5", "text": "Profesi", "bucket": "pilihan"},
         {"id": "i6", "text": "Prestasi", "bucket": "pilihan"},
         {"id": "i7", "text": "Keahlian", "bucket": "pilihan"},
     ],
     "feedback": {
         "correct": "Benar — identitas given diperoleh sejak lahir, identitas pilihan dibentuk melalui usaha.",
         "wrong": "Suku, daerah asal, warna kulit, dan jenis kelamin adalah given; profesi, prestasi, dan keahlian adalah pilihan.",
     }},
    {"type": "checkpoint", "id": "cp-pan3-bhinneka",
     "question": "Semboyan Bhinneka Tunggal Ika menegaskan bahwa persatuan…",
     "choices": [
         {"id": "a", "text": "Tidak berarti penyeragaman", "correct": True},
         {"id": "b", "text": "Mengharuskan semua budaya disamakan"},
         {"id": "c", "text": "Hanya berlaku bagi satu suku"},
     ],
     "explanation": "Bhinneka Tunggal Ika berarti berbeda-beda tetapi tetap satu. Persatuan tidak menghapus keragaman, melainkan menghargainya."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-pan3-kolaborasi",
     "prompt": "Urutkan tahap kolaborasi antarbudaya.",
     "items": [
         {"id": "s1", "text": "Mengenali identitas diri dan kelompok sendiri"},
         {"id": "s2", "text": "Mengenali dan menghargai identitas kelompok lain"},
         {"id": "s3", "text": "Menemukan tujuan bersama"},
         {"id": "s4", "text": "Bekerja sama dengan pembagian peran yang adil"},
         {"id": "s5", "text": "Merefleksikan hasil kerja sama"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — kenali diri, hargai yang lain, temukan tujuan, bekerja sama, lalu refleksi.",
         "wrong": "Mulai dari mengenali identitas sendiri, lalu menghargai identitas kelompok lain.",
     }},
    {"type": "checkpoint", "id": "cp-pan3-global",
     "question": "Sikap yang diperlukan dalam pertukaran budaya di pentas global adalah…",
     "choices": [
         {"id": "a", "text": "Bangga pada budaya sendiri sekaligus terbuka mempelajari budaya lain", "correct": True},
         {"id": "b", "text": "Menutup diri dari semua budaya asing"},
         {"id": "c", "text": "Menerima semua budaya asing tanpa menyaring"},
     ],
     "explanation": "Sikap terbuka dan kritis membuat budaya saling memperkaya. Penyaringan dilakukan dengan nilai Pancasila dan budaya sendiri."},
    {"type": "categorize", "id": "cat-pan3-sikap",
     "prompt": "Kelompokkan sikap berikut menurut akibatnya.",
     "buckets": [
         {"id": "terbuka", "label": "Terbuka dan kritis"},
         {"id": "menutup", "label": "Menutup diri total"},
         {"id": "tanpa-saring", "label": "Menerima tanpa menyaring"},
     ],
     "items": [
         {"id": "s1", "text": "Budaya saling memperkaya", "bucket": "terbuka"},
         {"id": "s2", "text": "Kehilangan peluang belajar", "bucket": "menutup"},
         {"id": "s3", "text": "Kehilangan jati diri", "bucket": "tanpa-saring"},
         {"id": "s4", "text": "Menyaring dengan nilai Pancasila dan budaya sendiri", "bucket": "terbuka"},
     ],
     "feedback": {
         "correct": "Benar — terbuka dan kritis memperkaya, menutup diri kehilangan peluang, menerima tanpa saring kehilangan jati diri.",
         "wrong": "Sikap terbaik adalah terbuka sekaligus kritis dengan penyaringan nilai Pancasila.",
     }},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-pan3-kearifan",
     "prompt": "Kelompokkan kearifan lokal berikut menurut daerahnya.",
     "buckets": [
         {"id": "bali", "label": "Bali"},
         {"id": "maluku", "label": "Maluku dan Papua"},
         {"id": "jawa", "label": "Jawa"},
         {"id": "sumatra", "label": "Sumatra"},
     ],
     "items": [
         {"id": "k1", "text": "Subak — irigasi sawah berbasis gotong royong", "bucket": "bali"},
         {"id": "k2", "text": "Sasi — larangan memanen agar sumber daya pulih", "bucket": "maluku"},
         {"id": "k3", "text": "Pranata mangsa — kalender tanam berdasarkan tanda alam", "bucket": "jawa"},
         {"id": "k4", "text": "Lubuk larangan — larangan menangkap ikan di bagian sungai tertentu", "bucket": "sumatra"},
     ],
     "feedback": {
         "correct": "Benar — Subak di Bali, Sasi di Maluku dan Papua, Pranata mangsa di Jawa, Lubuk larangan di Sumatra.",
         "wrong": "Cocokkan daerahnya: Bali, Maluku/Papua, Jawa, dan Sumatra.",
     }},
    {"type": "checkpoint", "id": "cp-pan3-modal",
     "question": "Kebinekaan disebut modal sosial pembangunan karena…",
     "choices": [
         {"id": "a", "text": "Menyediakan jaringan kerja sama dan pengetahuan yang luas", "correct": True},
         {"id": "b", "text": "Mengharuskan semua orang memiliki budaya yang sama"},
         {"id": "c", "text": "Membatasi kerja sama hanya pada satu daerah"},
     ],
     "explanation": "Perbedaan adalah kekayaan. Kebinekaan menyediakan jaringan kerja sama dan pengetahuan luas yang menjadi modal sosial pembangunan."},
    {"type": "scenario", "id": "sc-pan3-festival",
     "title": "Festival budaya kelas",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kelasmu mengadakan festival budaya. Beberapa teman ingin menampilkan budaya daerahnya, tetapi ada yang malu karena minoritas. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengajak semua tampil dan memberi panggung yang setara", "next": "n2", "score": 2,
               "feedback": "Kolaborasi antarbudaya menghargai setiap identitas dan membagi peran secara adil."},
              {"text": "Memilih budaya yang paling populer agar acara ramai", "next": "n3", "score": 0,
               "feedback": "Mengutamakan yang populer membuat kelompok lain merasa tidak dihargai."},
              {"text": "Membiarkan yang malu tidak tampil", "next": "n4", "score": 1,
               "feedback": "Tidak memaksa itu baik, tetapi belum mengajak dan memberi ruang yang setara."},
          ]},
         {"id": "n2", "text": "Saat latihan, ada kelompok yang mengejek tarian daerah lain. Apa sikapmu?",
          "choices": [
              {"text": "Mengingatkan bahwa perbedaan adalah kekayaan", "next": "n5", "score": 2,
               "feedback": "Menghargai keragaman mencegah prasangka dan konflik."},
              {"text": "Ikut tertawa agar suasana tidak tegang", "next": "n6", "score": 0,
               "feedback": "Ikut menertawakan budaya lain memperkuat prasangka."},
          ]},
         {"id": "n3", "text": "Kelompok yang budayanya tidak dipilih kecewa. Apa langkahmu?",
          "choices": [
              {"text": "Meminta maaf dan membuka kesempatan tampil di sesi lain", "next": "n2", "score": 1,
               "feedback": "Membuka kesempatan kembali memulihkan rasa dihargai."},
              {"text": "Mengatakan bahwa pilihan sudah final", "next": "n7", "score": 0,
               "feedback": "Menutup ruang membuat kekecewaan menjadi konflik."},
          ]},
         {"id": "n4", "text": "Teman yang malu akhirnya bertanya apakah boleh ikut. Apa jawabmu?",
          "choices": [
              {"text": "Menyambut dan membantunya berlatih", "next": "n5", "score": 2,
               "feedback": "Menyambut dan mendampingi mewujudkan kolaborasi yang setara."},
              {"text": "Menyuruhnya tampil sendiri tanpa bantuan", "next": "n6", "score": 0,
               "feedback": "Membiarkan sendiri membuatnya semakin ragu dan tidak terlibat."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Semua kelompok tampil dan saling menghargai. Kebinekaan menjadi kekuatan kelas, bukan sumber perpecahan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Acara berjalan, tetapi sebagian teman belum merasa dihargai. Perbaiki dengan sikap yang lebih terbuka."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Kekecewaan berubah menjadi perpecahan. Keputusan tanpa musyawarah melemahkan kerja sama."},
     ]},
    {"type": "challenge", "id": "ch-pan3-kebinekaan",
     "title": "Tantangan Kilat: Kebinekaan",
     "time_limit": 90,
     "items": [
         {"question": "Identitas yang diperoleh sejak lahir disebut identitas…", "answer": "given"},
         {"question": "Identitas yang dibentuk melalui usaha disebut identitas…", "answer": "pilihan"},
         {"question": "Semboyan bangsa Indonesia adalah Bhinneka Tunggal…", "answer": "ika"},
         {"question": "Irigasi sawah berbasis gotong royong di Bali disebut…", "answer": "subak"},
         {"question": "Larangan memanen agar sumber daya pulih di Maluku dan Papua disebut…", "answer": "sasi"},
         {"question": "Kebinekaan menjadi modal… pembangunan", "answer": "sosial"},
     ],
     "feedback": {
         "correct": "Tepat — identitas, kearifan lokal, dan sikap terbuka menjadikan kebinekaan kekuatan.",
         "wrong": "Ingat: identitas given/pilihan, Bhinneka Tunggal Ika, Subak, Sasi, dan modal sosial.",
     }},
])
save(path, data)

# ── PAN 4 — Warga Negara yang Baik ────────────────────────────────────
path = 'pan-4-warga-negara-yang-baik.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Paham kebangsaan", "definition": "Kesadaran bahwa rakyat Indonesia bersatu sebagai satu bangsa yang melampaui perbedaan."},
        {"term": "Nasionalisme", "definition": "Kesetiaan pada bangsa yang diwujudkan melalui pengorbanan, menjaga keutuhan, dan berprestasi."},
        {"term": "Chauvinisme", "definition": "Sikap mengagung-agungkan bangsa sendiri dan merendahkan bangsa lain."},
        {"term": "Patriotisme", "definition": "Cinta dan kesiapan membela tanah air, termasuk menghormati simbol negara dan menaati hukum."},
    ]},
    {"type": "categorize", "id": "cat-pan4-nasionalisme",
     "prompt": "Kelompokkan sikap berikut ke dalam nasionalisme atau chauvinisme.",
     "buckets": [
         {"id": "nasionalisme", "label": "Nasionalisme"},
         {"id": "chauvinisme", "label": "Chauvinisme"},
     ],
     "items": [
         {"id": "n1", "text": "Bangga dan setia pada bangsa sendiri", "bucket": "nasionalisme"},
         {"id": "n2", "text": "Menghargai bangsa lain", "bucket": "nasionalisme"},
         {"id": "n3", "text": "Kerja sama antarbangsa terjaga", "bucket": "nasionalisme"},
         {"id": "n4", "text": "Mengagung-agungkan bangsa sendiri", "bucket": "chauvinisme"},
         {"id": "n5", "text": "Merendahkan bangsa lain", "bucket": "chauvinisme"},
         {"id": "n6", "text": "Hubungan antarbangsa rusak", "bucket": "chauvinisme"},
     ],
     "feedback": {
         "correct": "Benar — nasionalisme bangga tanpa merendahkan; chauvinisme mengagungkan diri dan merendahkan bangsa lain.",
         "wrong": "Nasionalisme menghargai bangsa lain; chauvinisme merendahkannya sehingga hubungan rusak.",
     }},
    {"type": "checkpoint", "id": "cp-pan4-patriotisme",
     "question": "Wujud patriotisme yang sederhana bagi pelajar adalah…",
     "choices": [
         {"id": "a", "text": "Menghormati simbol negara, menaati hukum, dan menjaga kerukunan", "correct": True},
         {"id": "b", "text": "Merendahkan budaya bangsa lain"},
         {"id": "c", "text": "Menolak semua kerja sama internasional"},
     ],
     "explanation": "Patriotisme tidak harus berupa tindakan besar. Menghormati simbol negara, menaati hukum, menjaga kerukunan, dan mengikuti kegiatan kebangsaan adalah wujudnya."},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-pan4-montevideo", "engine": "mermaid",
     "title": "Empat unsur pembentuk negara",
     "code": "flowchart LR\n  A[Unsur pembentuk negara] --> B[Wilayah]\n  A --> C[Rakyat]\n  A --> D[Pemerintahan]\n  A --> E[Pengakuan negara lain]\n  B --> F[NKRI berdasarkan Pasal 25A UUD 1945]\n  C --> F\n  D --> F\n  E --> F"},
    {"type": "sort", "id": "srt-pan4-unsur",
     "prompt": "Urutkan unsur pembentuk negara menurut Konvensi Montevideo 1933.",
     "items": [
         {"id": "s1", "text": "Wilayah"},
         {"id": "s2", "text": "Rakyat"},
         {"id": "s3", "text": "Pemerintahan"},
         {"id": "s4", "text": "Pengakuan negara lain"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — wilayah, rakyat, pemerintahan, lalu pengakuan negara lain.",
         "wrong": "Urutannya: wilayah, rakyat, pemerintahan, dan pengakuan negara lain.",
     }},
    {"type": "checkpoint", "id": "cp-pan4-pasal",
     "question": "Pasal yang menegaskan negara kesatuan berbentuk republik dengan wilayah yang ditetapkan undang-undang adalah…",
     "choices": [
         {"id": "a", "text": "Pasal 25A UUD NRI Tahun 1945", "correct": True},
         {"id": "b", "text": "Pasal 1 UUD NRI Tahun 1945"},
         {"id": "c", "text": "Pasal 31 UUD NRI Tahun 1945"},
     ],
     "explanation": "Pasal 25A menegaskan negara kesatuan berbentuk republik dengan wilayah yang ditetapkan undang-undang."},
    {"type": "categorize", "id": "cat-pan4-ancaman",
     "prompt": "Kelompokkan ancaman berikut.",
     "buckets": [
         {"id": "militer", "label": "Ancaman militer"},
         {"id": "nonmiliter", "label": "Ancaman nonmiliter"},
     ],
     "items": [
         {"id": "a1", "text": "Invasi", "bucket": "militer"},
         {"id": "a2", "text": "Blokade", "bucket": "militer"},
         {"id": "a3", "text": "Berita bohong yang memecah belah", "bucket": "nonmiliter"},
         {"id": "a4", "text": "Ancaman ideologi", "bucket": "nonmiliter"},
     ],
     "feedback": {
         "correct": "Benar — invasi dan blokade bersifat militer; hoaks dan ancaman ideologi bersifat nonmiliter.",
         "wrong": "Ancaman militer memakai kekuatan bersenjata; nonmiliter menyerang ideologi, informasi, dan persatuan.",
     }},
])

add_blocks(data, 2, [
    {"type": "diagram", "id": "dg-pan4-sengketa", "engine": "mermaid",
     "title": "Jalur penyelesaian sengketa batas wilayah",
     "code": "flowchart LR\n  A[Sengketa batas wilayah] --> B[Perundingan dan diplomasi]\n  A --> C[Mekanisme hukum internasional]\n  A --> D[Penguatan dokumen historis dan peta resmi]\n  A --> E[Menjaga wilayah secara nyata di lapangan]\n  B --> F[Penyelesaian damai]\n  C --> F\n  D --> F\n  E --> F"},
    {"type": "checkpoint", "id": "cp-pan4-sipadan",
     "question": "Pertimbangan utama Mahkamah Internasional dalam putusan Sipadan dan Ligitan tahun 2002 adalah…",
     "choices": [
         {"id": "a", "text": "Bukti pengelolaan nyata oleh Malaysia", "correct": True},
         {"id": "b", "text": "Jumlah penduduk kedua pulau"},
         {"id": "c", "text": "Luas wilayah masing-masing negara"},
     ],
     "explanation": "Mahkamah Internasional memutuskan kedua pulau menjadi milik Malaysia dengan pertimbangan bukti pengelolaan nyata (effective occupation)."},
    {"type": "checkpoint", "id": "cp-pan4-ambalat",
     "question": "Sengketa Ambalat menyangkut…",
     "choices": [
         {"id": "a", "text": "Batas landas kontinen dan hak eksplorasi di Laut Sulawesi", "correct": True},
         {"id": "b", "text": "Kepemilikan pulau di Selat Makassar"},
         {"id": "c", "text": "Batas darat antara Kalimantan dan Sabah"},
     ],
     "explanation": "Ambalat terletak di Laut Sulawesi dan menyangkut batas landas kontinen serta hak eksplorasi, bukan kepemilikan pulau. Penyelesaiannya ditempuh melalui diplomasi."},
    {"type": "scenario", "id": "sc-pan4-disinformasi",
     "title": "Berita bohong tentang wilayah Indonesia",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Di grup kelas beredar unggahan yang menyebut sebagian wilayah Indonesia sudah dijual ke negara lain. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Memeriksa sumber resmi sebelum menyebarkan", "next": "n2", "score": 2,
               "feedback": "Menolak disinformasi tentang wilayah adalah bentuk menjaga kedaulatan."},
              {"text": "Langsung meneruskan karena khawatir ketinggalan informasi", "next": "n3", "score": 0,
               "feedback": "Meneruskan tanpa memeriksa memperluas berita bohong yang memecah belah."},
              {"text": "Mengabaikan dan keluar dari grup", "next": "n4", "score": 1,
               "feedback": "Tidak menyebarkan itu baik, tetapi belum membantu meluruskan informasi."},
          ]},
         {"id": "n2", "text": "Ternyata unggahan itu tidak memiliki sumber resmi. Apa langkahmu?",
          "choices": [
              {"text": "Mengingatkan grup dan membagikan sumber resmi", "next": "n5", "score": 2,
               "feedback": "Meluruskan dengan sumber resmi mencegah hoaks menyebar lebih jauh."},
              {"text": "Diam saja karena sudah tahu itu bohong", "next": "n6", "score": 1,
               "feedback": "Tidak menyebarkan itu baik, tetapi diam membiarkan orang lain percaya hoaks."},
          ]},
         {"id": "n3", "text": "Beberapa teman mulai marah dan menyalahkan pemerintah. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui belum memeriksa dan mengajak mencari sumber resmi", "next": "n2", "score": 1,
               "feedback": "Mengakui kekeliruan dan mengajak memeriksa sumber memulihkan suasana."},
              {"text": "Terus membela unggahan itu", "next": "n7", "score": 0,
               "feedback": "Membela informasi tanpa bukti memperbesar perpecahan."},
          ]},
         {"id": "n4", "text": "Guru membahas pentingnya literasi informasi. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mulai memeriksa sumber setiap informasi tentang wilayah negara", "next": "n5", "score": 2,
               "feedback": "Literasi informasi membuat kita ikut menjaga kedaulatan secara sadar."},
              {"text": "Tetap mengabaikan semua berita tentang wilayah", "next": "n6", "score": 1,
               "feedback": "Mengabaikan semua berita membuat kita tidak peka terhadap isu kedaulatan."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Hoaks tidak menyebar dan grup kembali tenang. Kamu ikut menjaga persatuan dan kedaulatan."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Kamu tidak ikut menyebarkan hoaks, tetapi belum membantu orang lain memahami kebenarannya."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Perpecahan meluas dan hoaks makin dipercaya. Membela informasi tanpa bukti merugikan persatuan."},
     ]},
    {"type": "challenge", "id": "ch-pan4-warga",
     "title": "Tantangan Kilat: Warga Negara yang Baik",
     "time_limit": 90,
     "items": [
         {"question": "Kesetiaan pada bangsa disebut…", "answer": "nasionalisme"},
         {"question": "Mengagung-agungkan bangsa sendiri dan merendahkan bangsa lain disebut…", "answer": "chauvinisme"},
         {"question": "Cinta dan kesiapan membela tanah air disebut…", "answer": "patriotisme"},
         {"question": "Konvensi tentang unsur negara disepakati di Montevideo tahun…", "answer": "1933"},
         {"question": "Pasal yang menegaskan NKRI adalah Pasal…", "answer": "25a"},
         {"question": "Putusan Sipadan dan Ligitan keluar tahun…", "answer": "2002"},
     ],
     "feedback": {
         "correct": "Tepat — kebangsaan yang sehat bangga tanpa merendahkan bangsa lain.",
         "wrong": "Ingat: nasionalisme, chauvinisme, patriotisme, Montevideo 1933, Pasal 25A, dan putusan 2002.",
     }},
])

save(path, data)

print('batch 8: PAN 2, PAN 3, PAN 4 selesai')
