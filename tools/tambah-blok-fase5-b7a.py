"""Fase 5.1 batch 7a — blok interaktif untuk PAI 1 sampai PAI 5.

Jalankan dari folder gamecenter:

    python ../tools/tambah-blok-fase5-b7a.py
    python ../tools/rapikan-blok-fase5.py --apply
    php artisan gamecenter:materi-import

Skrip ini hanya menambah blok aktivitas/visual. Blok teks (heading, paragraph,
list, table, callout) disisipkan otomatis oleh `rapikan-blok-fase5.py` supaya
seluruh isi markdown tetap tampil (plan §5.3: teks asli 100%).
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


# ── PAI 1 — Kompetisi dalam Kebaikan dan Etos Kerja ───────────────────
path = 'pai-1-kompetisi-dan-etos-kerja.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-fastabiqul-khairat", "engine": "mermaid",
     "title": "Ciri kompetisi yang benar menurut fastabiqul khairat",
     "code": "flowchart LR\n  A[Syariat setiap umat] --> B[Berlomba dalam kebaikan]\n  B --> C[Cara halal dan berakhlak]\n  B --> D[Tidak merugikan orang lain]\n  B --> E[Tujuan memperbaiki kualitas bersama]\n  C --> F[Fastabiqul khairat]\n  D --> F\n  E --> F"},
    {"type": "glossary", "terms": [
        {"term": "Fastabiqul khairat", "definition": "Berlomba dan bersegera mengerjakan kebaikan, bukan berlomba mengejar keunggulan dengan mengorbankan orang lain."},
        {"term": "Asbabun nuzul", "definition": "Sebab atau peristiwa yang melatarbelakangi turunnya suatu ayat."},
        {"term": "Syariat", "definition": "Aturan dan jalan yang Allah tetapkan untuk setiap umat."},
        {"term": "Istiqamah", "definition": "Konsisten dan teguh berada di jalan yang benar."},
    ]},
    {"type": "checkpoint", "id": "cp-pai1-asbab",
     "question": "Peristiwa yang menjadi latar turunnya Q.S. al-Maidah/5: 48 adalah…",
     "choices": [
         {"id": "a", "text": "Perubahan arah kiblat dan penegasan bahwa setiap umat punya syariat", "correct": True},
         {"id": "b", "text": "Perang Badar antara kaum muslim dan Quraisy"},
         {"id": "c", "text": "Pembebasan kota Mekah tanpa pertumpahan darah"},
     ],
     "explanation": "Ayat ini turun berkaitan dengan perubahan arah kiblat dan menegaskan bahwa setiap umat memiliki syariat sendiri, sehingga kita menghargai keberagaman tanpa meninggalkan istiqamah."},
    {"type": "categorize", "id": "cat-pai1-kompetisi",
     "prompt": "Kelompokkan sikap berikut ke dalam kompetisi yang benar atau yang salah.",
     "buckets": [
         {"id": "benar", "label": "Kompetisi yang benar"},
         {"id": "salah", "label": "Kompetisi yang salah"},
     ],
     "items": [
         {"id": "k1", "text": "Caranya halal dan berakhlak", "bucket": "benar"},
         {"id": "k2", "text": "Tidak merugikan orang lain", "bucket": "benar"},
         {"id": "k3", "text": "Tujuannya memperbaiki kualitas bersama", "bucket": "benar"},
         {"id": "k4", "text": "Memaksa umat lain mengikuti syariat kita", "bucket": "salah"},
         {"id": "k5", "text": "Bersikap sinis kepada pemeluk agama lain", "bucket": "salah"},
     ],
     "feedback": {
         "correct": "Benar — kompetisi dalam kebaikan menjaga cara, tidak merugikan, dan mengutamakan kualitas bersama.",
         "wrong": "Kompetisi yang benar tetap menghargai keberagaman dan tidak memaksa keyakinan orang lain.",
     }},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-pai1-syarat",
     "prompt": "Urutkan tiga syarat pekerjaan yang diterima menurut materi.",
     "items": [
         {"id": "s1", "text": "Halal caranya"},
         {"id": "s2", "text": "Bermanfaat hasilnya"},
         {"id": "s3", "text": "Sungguh-sungguh pelaksanaannya"},
     ],
     "answer": ["s1", "s2", "s3"],
     "feedback": {
         "correct": "Benar: halal caranya, bermanfaat hasilnya, lalu dikerjakan dengan sungguh-sungguh.",
         "wrong": "Urutan syaratnya: halal caranya, bermanfaat hasilnya, dan sungguh-sungguh pelaksanaannya.",
     }},
    {"type": "checkpoint", "id": "cp-pai1-etos",
     "question": "Ayat yang memerintahkan bekerja dan menegaskan bahwa pekerjaan dilihat Allah, Rasul-Nya, serta orang-orang mukmin adalah…",
     "choices": [
         {"id": "a", "text": "Q.S. at-Taubah/9: 105", "correct": True},
         {"id": "b", "text": "Q.S. al-Maidah/5: 48"},
         {"id": "c", "text": "Q.S. al-Isra'/17: 26"},
     ],
     "explanation": "Q.S. at-Taubah/9: 105 berisi perintah bekerja dan menegaskan bahwa hasil kerja akan dilihat Allah, Rasul-Nya, dan orang-orang mukmin."},
    {"type": "categorize", "id": "cat-pai1-seimbang",
     "prompt": "Kelompokkan kebiasaan bekerja berikut.",
     "buckets": [
         {"id": "seimbang", "label": "Etos kerja seimbang"},
         {"id": "berlebihan", "label": "Kerja berlebihan"},
     ],
     "items": [
         {"id": "b1", "text": "Bekerja keras dan bertanggung jawab", "bucket": "seimbang"},
         {"id": "b2", "text": "Tetap menunaikan ibadah", "bucket": "seimbang"},
         {"id": "b3", "text": "Mengabaikan istirahat", "bucket": "berlebihan"},
         {"id": "b4", "text": "Memaksakan diri sampai jasmani dan ruhani rusak", "bucket": "berlebihan"},
     ],
     "feedback": {
         "correct": "Tepat — etos kerja diimbangi ibadah dan istirahat, karena kerja berlebihan merusak jasmani dan ruhani.",
         "wrong": "Etos kerja yang sehat tetap menyisakan waktu untuk ibadah dan istirahat.",
     }},
])

add_blocks(data, 2, [
    {"type": "scenario", "id": "sc-pai1-prestasi",
     "title": "Melihat teman lebih berprestasi",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Pengumuman lomba: namamu tidak muncul, tetapi nama teman sebangkumu masuk tiga besar. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengucapkan selamat dan bertanya cara ia belajar", "next": "n2", "score": 2,
               "feedback": "Fastabiqul khairat mendorong kita termotivasi dan belajar dari keberhasilan orang lain."},
              {"text": "Diam saja lalu mencari alasan mengapa ia menang", "next": "n3", "score": 1,
               "feedback": "Diam bukan kesalahan, tetapi membuang kesempatan belajar dari keberhasilannya."},
              {"text": "Menyebarkan anggapan bahwa ia menang dengan cara curang", "next": "n4", "score": 0,
               "feedback": "Menuduh tanpa bukti merugikan orang lain dan bertentangan dengan kompetisi yang berakhlak."},
          ]},
         {"id": "n2", "text": "Temanmu menawarkan belajar bersama untuk lomba berikutnya. Bagaimana sikapmu?",
          "choices": [
              {"text": "Menerima dan menyusun jadwal belajar bersama", "next": "n5", "score": 2,
               "feedback": "Belajar bersama memperbaiki kualitas kalian berdua — inilah kompetisi dalam kebaikan."},
              {"text": "Menerima, tetapi menyembunyikan materi yang kamu punya", "next": "n6", "score": 1,
               "feedback": "Belajar bersama tetap berjalan, tetapi menyembunyikan materi membuatnya tidak maksimal."},
          ]},
         {"id": "n3", "text": "Guru menanyakan siapa yang ingin ikut lomba berikutnya. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mendaftar dan meminta masukan dari teman yang menang", "next": "n2", "score": 2,
               "feedback": "Bertanya kepada yang lebih berpengalaman adalah cara sehat mengejar ketertinggalan."},
              {"text": "Tidak mendaftar karena merasa tidak mungkin menang", "next": "n7", "score": 0,
               "feedback": "Menyerah sebelum berusaha menutup peluang memperbaiki diri."},
          ]},
         {"id": "n4", "text": "Kabar tuduhanmu sampai ke guru. Temanmu kecewa. Apa langkahmu?",
          "choices": [
              {"text": "Minta maaf dan mengakui bahwa itu hanya prasangka", "next": "n5", "score": 1,
               "feedback": "Mengakui kekeliruan memulihkan hubungan dan menjaga akhlak kompetisi."},
              {"text": "Membela diri karena merasa tersaingi", "next": "n7", "score": 0,
               "feedback": "Membela prasangka hanya memperbesar kerugian yang sudah terjadi."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kalian belajar bersama, saling mendorong, dan sama-sama meningkat. Prestasi teman menjadi motivasi, bukan ancaman."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Belajar bersama berjalan setengah hati. Persaingan tidak merusak, tetapi kerja samanya belum maksimal."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Kekecewaan dan prasangka membuat hubungan renggang. Kesempatan memperbaiki diri justru terlewat."},
     ]},
    {"type": "challenge", "id": "ch-pai1-kompetisi",
     "title": "Tantangan Kilat: Kompetisi dan Etos Kerja",
     "time_limit": 80,
     "items": [
         {"question": "Berlomba dan bersegera mengerjakan kebaikan disebut…", "answer": "fastabiqul khairat"},
         {"question": "Sebab turunnya suatu ayat disebut…", "answer": "asbabun nuzul"},
         {"question": "Konsisten di jalan yang benar disebut…", "answer": "istiqamah"},
         {"question": "Tanggung jawab atas tugas yang diberikan disebut…", "answer": "amanah"},
         {"question": "Sebaik-baik rezeki berasal dari usaha… sendiri", "answer": "tangan"},
     ],
     "feedback": {
         "correct": "Tepat — kompetisi dalam kebaikan berjalan bersama etos kerja yang halal dan bertanggung jawab.",
         "wrong": "Ingat: fastabiqul khairat, asbabun nuzul, istiqamah, amanah, dan rezeki dari usaha tangan sendiri.",
     }},
])
save(path, data)

# ── PAI 2 — Syu'abul Iman ─────────────────────────────────────────────
path = 'pai-2-syuabul-iman.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Syu'abul iman", "definition": "Cabang-cabang iman, yaitu amal yang tumbuh dari keyakinan tauhid."},
        {"term": "Iman", "definition": "Membenarkan dengan hati, mengucapkan dengan lisan, dan mengamalkan dengan perbuatan."},
        {"term": "Tauhid", "definition": "Keyakinan bahwa Allah itu satu; menjadi akar bagi seluruh cabang iman."},
        {"term": "Rukun iman", "definition": "Enam pilar keyakinan yang menjadi dasar keimanan seorang muslim."},
    ]},
    {"type": "checkpoint", "id": "cp-pai2-puncak",
     "question": "Cabang iman yang kedudukannya paling tinggi adalah…",
     "choices": [
         {"id": "a", "text": "Ucapan la ilaha illallah", "correct": True},
         {"id": "b", "text": "Menghilangkan gangguan di jalan"},
         {"id": "c", "text": "Rasa malu"},
     ],
     "explanation": "Kalimat tauhid adalah cabang tertinggi, menghilangkan gangguan di jalan adalah cabang terendah, sedangkan rasa malu disebut cabang yang istimewa."},
    {"type": "checkpoint", "id": "cp-pai2-istilah",
     "question": "Iman menurut istilah adalah membenarkan dengan hati, mengucapkan dengan…, dan mengamalkan dengan perbuatan.",
     "choices": [
         {"id": "a", "text": "Lisan", "correct": True},
         {"id": "b", "text": "Hati"},
         {"id": "c", "text": "Tulisan"},
     ],
     "explanation": "Iman mencakup tiga hal sekaligus: pembenaran hati, pengucapan lisan, dan pengamalan perbuatan. Jadi iman bukan hanya keyakinan."},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-pai2-wilayah", "engine": "mermaid",
     "title": "Tiga wilayah cabang iman yang tumbuh dari tauhid",
     "code": "flowchart TD\n  A[Akar: tauhid] --> B[Wilayah hati]\n  A --> C[Wilayah lisan]\n  A --> D[Wilayah perbuatan]\n  B --> B1[Malu, tawakal, sabar, menahan amarah]\n  C --> C1[Jujur, menjauhi ghibah, kalimat tauhid]\n  D --> D1[Salat, menolong teman, menjaga kebersihan]"},
    {"type": "categorize", "id": "cat-pai2-wilayah",
     "prompt": "Kelompokkan amal berikut menurut wilayah cabang imannya.",
     "buckets": [
         {"id": "hati", "label": "Hati"},
         {"id": "lisan", "label": "Lisan"},
         {"id": "perbuatan", "label": "Perbuatan"},
     ],
     "items": [
         {"id": "w1", "text": "Malu", "bucket": "hati"},
         {"id": "w2", "text": "Tawakal", "bucket": "hati"},
         {"id": "w3", "text": "Menahan amarah", "bucket": "hati"},
         {"id": "w4", "text": "Jujur", "bucket": "lisan"},
         {"id": "w5", "text": "Menjauhi ghibah", "bucket": "lisan"},
         {"id": "w6", "text": "Salat", "bucket": "perbuatan"},
         {"id": "w7", "text": "Menolong teman", "bucket": "perbuatan"},
         {"id": "w8", "text": "Menghilangkan gangguan di jalan", "bucket": "perbuatan"},
     ],
     "feedback": {
         "correct": "Benar — hati berisi sikap batin, lisan berisi ucapan, dan perbuatan berisi amal nyata.",
         "wrong": "Perhatikan letaknya: sikap batin di hati, ucapan di lisan, dan tindakan nyata di perbuatan.",
     }},
    {"type": "checkpoint", "id": "cp-pai2-ihsan",
     "question": "Kualitas dan kesadaran beribadah, sebagaimana dijelaskan dalam hadis Jibril, disebut…",
     "choices": [
         {"id": "a", "text": "Ihsan", "correct": True},
         {"id": "b", "text": "Islam"},
         {"id": "c", "text": "Iman"},
     ],
     "explanation": "Islam menekankan amal lahir, iman menekankan keyakinan, dan ihsan menekankan kualitas serta kesadaran beribadah."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-pai2-langkah",
     "prompt": "Urutkan langkah menumbuhkan cabang iman dalam kehidupan sehari-hari.",
     "items": [
         {"id": "s1", "text": "Memahami makna cabang iman"},
         {"id": "s2", "text": "Memilih satu amal kecil untuk dibiasakan"},
         {"id": "s3", "text": "Melaksanakan secara istiqamah"},
         {"id": "s4", "text": "Mengevaluasi dan menambah amal lain"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: pahami, pilih satu amal, biasakan, lalu evaluasi dan tambah amal lain.",
         "wrong": "Mulai dari pemahaman, lalu pilih satu amal kecil, biasakan, dan evaluasi sebelum menambah amal.",
     }},
    {"type": "scenario", "id": "sc-pai2-amarah",
     "title": "Menahan amarah saat diejek",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Di grup kelas, seseorang mengunggah foto lama milikmu dengan keterangan yang mengejek. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menahan amarah dan menanyakan baik-baik maksudnya", "next": "n2", "score": 2,
               "feedback": "Menahan amarah adalah cabang iman di wilayah hati; bertanya baik-baik membuka jalan penyelesaian."},
              {"text": "Membalas dengan ejekan yang lebih keras", "next": "n3", "score": 0,
               "feedback": "Membalas dengan keburukan menambah dosa dan memperpanjang masalah."},
              {"text": "Diam, tetapi menyimpan dendam", "next": "n4", "score": 1,
               "feedback": "Diam lebih baik daripada membalas, tetapi dendam masih mengganggu hati."},
          ]},
         {"id": "n2", "text": "Ia meminta maaf dan menghapus unggahan. Bagaimana sikapmu?",
          "choices": [
              {"text": "Memaafkan dan tetap berteman baik", "next": "n5", "score": 2,
               "feedback": "Memaafkan menutup masalah dan menjaga persaudaraan."},
              {"text": "Memaafkan, tetapi mengingatnya untuk dibalas nanti", "next": "n6", "score": 1,
               "feedback": "Maaf yang disimpan bersama rencana balas belum menjadi maaf yang tulus."},
          ]},
         {"id": "n3", "text": "Guru menegur kalian berdua karena keributan di grup. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui bagian kesalahanku dan berhenti membalas", "next": "n2", "score": 1,
               "feedback": "Mengakui kesalahan menghentikan rangkaian balas-membalas."},
              {"text": "Menyalahkan teman sepenuhnya", "next": "n7", "score": 0,
               "feedback": "Melepas tanggung jawab membuat masalah tidak selesai dan menyakiti hubungan."},
          ]},
         {"id": "n4", "text": "Beberapa hari kemudian kamu masih merasa kesal setiap mengingatnya. Apa langkahmu?",
          "choices": [
              {"text": "Memaafkan dan mendoakan kebaikannya", "next": "n5", "score": 2,
               "feedback": "Memaafkan disertai doa membersihkan hati dan menguatkan cabang iman."},
              {"text": "Menjauhinya tanpa penjelasan", "next": "n6", "score": 1,
               "feedback": "Menjauh bisa meredakan, tetapi tanpa penjelasan hubungan tetap retak."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Amarah diredam, masalah selesai dengan baik, dan hati tetap bersih. Cabang iman di wilayah hati tumbuh."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Masalah tidak meledak, tetapi sisa rasa kesal masih tersimpan. Hati belum sepenuhnya lapang."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Balas-membalas membuat suasana kelas memanas dan keduanya mendapat teguran."},
     ]},
    {"type": "challenge", "id": "ch-pai2-cabang",
     "title": "Tantangan Kilat: Cabang-Cabang Iman",
     "time_limit": 80,
     "items": [
         {"question": "Cabang-cabang iman disebut…", "answer": "syuabul iman"},
         {"question": "Cabang iman tertinggi adalah ucapan…", "answer": "la ilaha illallah"},
         {"question": "Cabang iman terendah adalah menghilangkan… di jalan", "answer": "gangguan"},
         {"question": "Cabang iman yang istimewa adalah rasa…", "answer": "malu"},
         {"question": "Kualitas dan kesadaran beribadah disebut…", "answer": "ihsan"},
     ],
     "feedback": {
         "correct": "Tepat — iman bercabang pada hati, lisan, dan perbuatan, lalu tumbuh melalui pembiasaan.",
         "wrong": "Cabang tertinggi: la ilaha illallah; terendah: menghilangkan gangguan; istimewa: rasa malu.",
     }},
])
save(path, data)

# ── PAI 3 — Berfoya-foya, Riya', Sum'ah, Takabur, Hasad ───────────────
path = 'pai-3-berfoya-foya-riya-takabur-hasad.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Berfoya-foya", "definition": "Membelanjakan harta untuk hal yang tidak bermanfaat dan berlebihan."},
        {"term": "Riya'", "definition": "Beramal agar dilihat orang sehingga mengharap pujian lewat penglihatan."},
        {"term": "Sum'ah", "definition": "Beramal agar didengar orang sehingga mengharap pujian lewat pendengaran."},
        {"term": "Ikhlas", "definition": "Beramal murni untuk Allah tanpa mengharap pujian manusia."},
    ]},
    {"type": "checkpoint", "id": "cp-pai3-pemboros",
     "question": "Q.S. al-Isra'/17: 26–27 menyebut pemboros sebagai…",
     "choices": [
         {"id": "a", "text": "Saudara setan", "correct": True},
         {"id": "b", "text": "Orang yang paling dermawan"},
         {"id": "c", "text": "Orang yang paling sabar"},
     ],
     "explanation": "Ayat tersebut melarang berlebih-lebihan dan menyebut pemboros sebagai saudara setan karena membelanjakan harta tanpa manfaat."},
    {"type": "categorize", "id": "cat-pai3-riya-sumah",
     "prompt": "Kelompokkan bentuk amal yang dirusak niat berikut.",
     "buckets": [
         {"id": "riya", "label": "Riya'"},
         {"id": "sumah", "label": "Sum'ah"},
     ],
     "items": [
         {"id": "r1", "text": "Beramal agar dilihat orang", "bucket": "riya"},
         {"id": "r2", "text": "Mengharap pujian lewat penglihatan", "bucket": "riya"},
         {"id": "r3", "text": "Beramal agar didengar orang", "bucket": "sumah"},
         {"id": "r4", "text": "Mengharap pujian lewat pendengaran", "bucket": "sumah"},
     ],
     "feedback": {
         "correct": "Benar — riya' lewat penglihatan, sum'ah lewat pendengaran. Keduanya merusak kemurnian niat.",
         "wrong": "Riya' = ingin dilihat; sum'ah = ingin didengar. Keduanya mengharap pujian manusia.",
     }},
])

add_blocks(data, 1, [
    {"type": "diagram", "id": "dg-pai3-takabur", "engine": "mermaid",
     "title": "Takabur dan tawadu: dua arah yang berlawanan",
     "code": "flowchart LR\n  A[Percaya diri] --> B[Tidak merendahkan orang]\n  C[Takabur] --> D[Merendahkan orang lain]\n  C --> E[Sulit menerima kebenaran dan nasihat]\n  F[Tawadu] --> G[Rendah hati]\n  G --> H[Mudah menerima nasihat]\n  G --> I[Mudah berkembang]"},
    {"type": "checkpoint", "id": "cp-pai3-hasad",
     "question": "Iri dan benci atas nikmat orang lain, bahkan berharap nikmat itu hilang, disebut…",
     "choices": [
         {"id": "a", "text": "Hasad", "correct": True},
         {"id": "b", "text": "Ghibtah"},
         {"id": "c", "text": "Tawadu"},
     ],
     "explanation": "Hasad berharap nikmat orang lain hilang dan merusak hubungan. Ghibtah justru ingin kebaikan serupa sementara nikmat orang tetap."},
    {"type": "categorize", "id": "cat-pai3-hasad-ghibtah",
     "prompt": "Kelompokkan sikap berikut ke dalam hasad atau ghibtah.",
     "buckets": [
         {"id": "hasad", "label": "Hasad"},
         {"id": "ghibtah", "label": "Ghibtah"},
     ],
     "items": [
         {"id": "h1", "text": "Berharap nikmat orang lain hilang", "bucket": "hasad"},
         {"id": "h2", "text": "Merusak hubungan", "bucket": "hasad"},
         {"id": "h3", "text": "Ingin kebaikan serupa, nikmat orang tetap", "bucket": "ghibtah"},
         {"id": "h4", "text": "Memotivasi diri untuk berusaha", "bucket": "ghibtah"},
     ],
     "feedback": {
         "correct": "Tepat — hasad merusak karena menginginkan nikmat orang hilang, ghibtah memotivasi tanpa merugikan siapa pun.",
         "wrong": "Hasad menginginkan nikmat orang hilang; ghibtah ingin kebaikan serupa dan membiarkan nikmat orang tetap.",
     }},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-pai3-ikhlas",
     "prompt": "Urutkan langkah membersihkan hati dari riya'.",
     "items": [
         {"id": "s1", "text": "Menyadari adanya dorongan riya'"},
         {"id": "s2", "text": "Memperbarui niat hanya untuk Allah"},
         {"id": "s3", "text": "Membiasakan amal yang tidak diketahui orang"},
         {"id": "s4", "text": "Memeriksa kembali tujuan beramal"},
         {"id": "s5", "text": "Berteman dengan orang saleh dan meminta nasihat"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — sadari dorongannya, perbarui niat, biasakan amal tersembunyi, periksa tujuan, lalu minta nasihat orang saleh.",
         "wrong": "Mulai dari menyadari dorongan riya', lalu perbarui niat dan biasakan amal yang tidak diketahui orang.",
     }},
    {"type": "categorize", "id": "cat-pai3-pengganti",
     "prompt": "Pisahkan perilaku tercela dari pengganti terpuji yang diajarkan materi.",
     "buckets": [
         {"id": "tercela", "label": "Perilaku tercela"},
         {"id": "terpuji", "label": "Pengganti terpuji"},
     ],
     "items": [
         {"id": "t1", "text": "Berfoya-foya", "bucket": "tercela"},
         {"id": "t2", "text": "Hidup sederhana dan menabung", "bucket": "terpuji"},
         {"id": "t3", "text": "Riya' dan sum'ah", "bucket": "tercela"},
         {"id": "t4", "text": "Ikhlas", "bucket": "terpuji"},
         {"id": "t5", "text": "Takabur", "bucket": "tercela"},
         {"id": "t6", "text": "Tawadu", "bucket": "terpuji"},
         {"id": "t7", "text": "Hasad", "bucket": "tercela"},
         {"id": "t8", "text": "Syukur dan ghibtah", "bucket": "terpuji"},
     ],
     "feedback": {
         "correct": "Benar — setiap perilaku tercela punya pengganti terpuji: sederhana, ikhlas, tawadu, dan syukur.",
         "wrong": "Pasangannya: berfoya-foya → sederhana, riya' → ikhlas, takabur → tawadu, hasad → syukur dan ghibtah.",
     }},
    {"type": "scenario", "id": "sc-pai3-riya",
     "title": "Amal yang mulai mengharap pujian",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kamu menjadi relawan bakti sosial. Seorang teman mengambil fotomu saat sedang bekerja dan ingin mengunggahnya. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Meminta unggahan tidak menonjolkan dirimu", "next": "n2", "score": 2,
               "feedback": "Menyembunyikan amal yang bisa disembunyikan menjaga niat tetap ikhlas."},
              {"text": "Membiarkannya karena itu bisa memotivasi orang lain", "next": "n3", "score": 1,
               "feedback": "Bisa bermanfaat, tetapi periksa lagi apakah ada dorongan ingin dipuji."},
              {"text": "Meminta unggahan dibuat semenarik mungkin agar banyak yang memuji", "next": "n4", "score": 0,
               "feedback": "Keinginan dipuji menggeser tujuan amal dari Allah kepada manusia."},
          ]},
         {"id": "n2", "text": "Temanmu tetap mengunggah foto itu tanpa menyebut namamu. Bagaimana perasaanmu?",
          "choices": [
              {"text": "Biasa saja karena amal tidak perlu diketahui orang", "next": "n5", "score": 2,
               "feedback": "Amal yang tidak diketahui orang justru lebih terjaga dari riya'."},
              {"text": "Kecewa karena namamu tidak disebut", "next": "n6", "score": 0,
               "feedback": "Kekecewaan itu tanda niat mulai bercampur harapan pujian."},
          ]},
         {"id": "n3", "text": "Unggahan itu mendapat banyak pujian. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengingatkan diri bahwa amal hanya untuk Allah", "next": "n5", "score": 2,
               "feedback": "Memperbarui niat setelah pujian datang menjaga amal tetap murni."},
              {"text": "Membalas komentar agar pujian bertambah", "next": "n4", "score": 0,
               "feedback": "Menambah pujian yang diharapkan memperkuat riya'."},
          ]},
         {"id": "n4", "text": "Kegiatan bakti sosial berikutnya tiba. Apa keputusanmu?",
          "choices": [
              {"text": "Ikut tanpa memberi tahu siapa pun", "next": "n5", "score": 2,
               "feedback": "Membiasakan amal yang tidak diketahui orang melatih ikhlas."},
              {"text": "Ikut hanya jika ada yang mendokumentasikan", "next": "n7", "score": 0,
               "feedback": "Syarat dokumentasi menunjukkan amal bergantung pada pengakuan orang."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Amal tetap berjalan dan niat terjaga. Kamu belajar menikmati kebaikan tanpa perlu pujian."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Kamu menyadari ada rasa kecewa. Itu tanda awal riya' yang bisa diperbaiki dengan memperbarui niat."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Amal menjadi bergantung pada pengakuan orang. Riya' tumbuh dan nilai amal berkurang."},
     ]},
    {"type": "challenge", "id": "ch-pai3-hati",
     "title": "Tantangan Kilat: Membersihkan Hati",
     "time_limit": 80,
     "items": [
         {"question": "Membelanjakan harta berlebihan untuk hal tak bermanfaat disebut…", "answer": "berfoya-foya"},
         {"question": "Beramal agar dilihat orang disebut…", "answer": "riya"},
         {"question": "Beramal agar didengar orang disebut…", "answer": "sumah"},
         {"question": "Membanggakan diri dan merasa lebih tinggi disebut…", "answer": "takabur"},
         {"question": "Lawan takabur yang berarti rendah hati disebut…", "answer": "tawadu"},
         {"question": "Iri pada nikmat orang sampai berharap nikmat itu hilang disebut…", "answer": "hasad"},
     ],
     "feedback": {
         "correct": "Tepat — kenali nama penyakit hati agar bisa diganti dengan ikhlas, tawadu, dan syukur.",
         "wrong": "Berfoya-foya, riya', sum'ah, takabur, hasad — semuanya disembuhkan dengan ikhlas dan muhasabah.",
     }},
])
save(path, data)

# ── PAI 4 — Asuransi, Bank, dan Koperasi Syariah ──────────────────────
path = 'pai-4-asuransi-bank-koperasi-syariah.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pai4-akad", "engine": "mermaid",
     "title": "Memilih akad sesuai kebutuhan transaksi",
     "code": "flowchart LR\n  A[Kebutuhan transaksi] --> B[Pilih akad]\n  B --> C[Mudarabah: kerja sama bagi hasil]\n  B --> D[Musyarakah: kerja sama modal]\n  B --> E[Wadiah: titipan dana]\n  B --> F[Tabarru': dana tolong-menolong]\n  C --> G[Catat kesepakatan tertulis]\n  D --> G\n  E --> G\n  F --> G"},
    {"type": "glossary", "terms": [
        {"term": "Akad", "definition": "Perjanjian antara pihak yang bertransaksi sebagai dasar ikatan hak dan kewajiban."},
        {"term": "Mudarabah", "definition": "Kerja sama usaha dengan bagi hasil sesuai nisbah yang disepakati."},
        {"term": "Musyarakah", "definition": "Kerja sama modal antara pihak-pihak yang bertransaksi."},
        {"term": "Wadiah", "definition": "Titipan dana yang dapat diambil kembali oleh pemiliknya."},
        {"term": "Tabarru'", "definition": "Dana tolong-menolong untuk menanggung risiko bersama."},
        {"term": "Riba", "definition": "Tambahan yang diambil tanpa imbalan yang sah, misalnya bunga pinjaman."},
        {"term": "Gharar", "definition": "Ketidakjelasan dalam transaksi yang dapat merugikan salah satu pihak."},
    ]},
    {"type": "checkpoint", "id": "cp-pai4-riba",
     "question": "Tambahan yang diambil tanpa imbalan yang sah, misalnya bunga pinjaman, disebut…",
     "choices": [
         {"id": "a", "text": "Riba", "correct": True},
         {"id": "b", "text": "Gharar"},
         {"id": "c", "text": "Wadiah"},
     ],
     "explanation": "Riba dilarang karena menimbulkan ketidakadilan, membebani pihak yang lemah, dan membuat risiko tidak ditanggung bersama. Gharar adalah ketidakjelasan akad."},
    {"type": "sort", "id": "srt-pai4-utang",
     "prompt": "Urutkan langkah berutang secara sehat.",
     "items": [
         {"id": "s1", "text": "Pastikan kebutuhan benar-benar penting"},
         {"id": "s2", "text": "Hitung kemampuan membayar"},
         {"id": "s3", "text": "Pilih lembaga dan akad yang jelas dan halal"},
         {"id": "s4", "text": "Catat kesepakatan secara tertulis"},
         {"id": "s5", "text": "Lunasi tepat waktu"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — pastikan kebutuhan, hitung kemampuan, pilih akad halal, catat, lalu lunasi tepat waktu.",
         "wrong": "Mulai dari memastikan kebutuhan penting dan kemampuan membayar sebelum memilih akad.",
     }},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-pai4-asuransi",
     "prompt": "Kelompokkan ciri berikut ke dalam asuransi konvensional atau syariah.",
     "buckets": [
         {"id": "konvensional", "label": "Konvensional"},
         {"id": "syariah", "label": "Syariah"},
     ],
     "items": [
         {"id": "a1", "text": "Premi menjadi milik perusahaan", "bucket": "konvensional"},
         {"id": "a2", "text": "Mengandung unsur bunga", "bucket": "konvensional"},
         {"id": "a3", "text": "Ada dana tabarru' bersama", "bucket": "syariah"},
         {"id": "a4", "text": "Berbasis akad dan bagi hasil", "bucket": "syariah"},
         {"id": "a5", "text": "Risiko ditanggung bersama", "bucket": "syariah"},
     ],
     "feedback": {
         "correct": "Benar — asuransi syariah berbasis ta'awun dan dana tabarru', bukan perpindahan risiko dengan bunga.",
         "wrong": "Ciri syariah: dana tabarru', akad dan bagi hasil, risiko ditanggung bersama. Konvensional: premi milik perusahaan dan mengandung bunga.",
     }},
    {"type": "checkpoint", "id": "cp-pai4-tabarru",
     "question": "Dana kebajikan yang dikumpulkan peserta asuransi syariah untuk saling menanggung risiko disebut dana…",
     "choices": [
         {"id": "a", "text": "Tabarru'", "correct": True},
         {"id": "b", "text": "Mudarabah"},
         {"id": "c", "text": "Wadiah"},
     ],
     "explanation": "Dana tabarru' adalah dana tolong-menolong. Prinsip dasarnya ta'awun: peserta saling menanggung musibah, bukan memindahkan risiko kepada perusahaan."},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-pai4-wadiah",
     "question": "Produk bank syariah berupa titipan dana yang dapat diambil kembali disebut…",
     "choices": [
         {"id": "a", "text": "Wadiah", "correct": True},
         {"id": "b", "text": "Mudarabah"},
         {"id": "c", "text": "Musyarakah"},
     ],
     "explanation": "Wadiah adalah titipan, mudarabah adalah pembiayaan bagi hasil, dan musyarakah adalah penyertaan modal."},
    {"type": "sort", "id": "srt-pai4-etika",
     "prompt": "Urutkan etika memilih lembaga keuangan.",
     "items": [
         {"id": "s1", "text": "Pahami kebutuhan keuangan"},
         {"id": "s2", "text": "Periksa akad dan produk"},
         {"id": "s3", "text": "Pastikan legalitas lewat izin resmi"},
         {"id": "s4", "text": "Baca dan pahami perjanjian"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — pahami kebutuhan, periksa akad, pastikan legalitas, lalu baca perjanjian.",
         "wrong": "Kebutuhan dulu, lalu akad, legalitas, dan terakhir membaca perjanjian sebelum menandatangani.",
     }},
    {"type": "scenario", "id": "sc-pai4-pinjol",
     "title": "Tawaran pinjaman online untuk membeli gawai",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Seorang teman mengirim tautan pinjaman online: dananya cair cepat tanpa jaminan. Kamu ingin membeli gawai baru. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Memeriksa legalitas dan membaca perjanjian lebih dulu", "next": "n2", "score": 2,
               "feedback": "Langkah pertama adalah memastikan legalitas lewat izin resmi dan memahami isi perjanjian."},
              {"text": "Mengajukan pinjaman karena prosesnya mudah", "next": "n3", "score": 0,
               "feedback": "Kemudahan bukan jaminan aman; pinjaman ilegal sering membawa bunga dan denda mencekik."},
              {"text": "Menunda dan menghitung apakah gawai itu benar-benar kebutuhan", "next": "n4", "score": 1,
               "feedback": "Menunda itu baik, tetapi kebutuhan dan kemampuan membayar perlu dihitung dengan jelas."},
          ]},
         {"id": "n2", "text": "Ternyata penyedia itu tidak memiliki izin resmi. Apa langkahmu?",
          "choices": [
              {"text": "Membatalkan dan mencari lembaga berizin", "next": "n5", "score": 2,
               "feedback": "Legalitas melindungi hak. Lembaga berizin terikat aturan dan akad yang jelas."},
              {"text": "Tetap meminjam dalam jumlah kecil karena dianggap aman", "next": "n6", "score": 0,
               "feedback": "Jumlah kecil tidak menghapus risiko penyalahgunaan data dan denda yang mencekik."},
          ]},
         {"id": "n3", "text": "Beberapa minggu kemudian tagihan membengkak karena denda. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Mengakui keadaan kepada orang tua dan mencari bantuan", "next": "n7", "score": 1,
               "feedback": "Terbuka kepada keluarga lebih baik daripada berutang lagi untuk menutup utang."},
              {"text": "Meminjam lagi dari aplikasi lain untuk menutup tagihan", "next": "n8", "score": 0,
               "feedback": "Berutang untuk membayar utang membuat beban berlipat dan sulit berhenti."},
          ]},
         {"id": "n4", "text": "Setelah dihitung, gawai baru belum mendesak. Apa keputusanmu?",
          "choices": [
              {"text": "Menabung bertahap dan membeli tanpa utang berbunga", "next": "n5", "score": 2,
               "feedback": "Menabung sesuai kemampuan menghindari jerat bunga dan menjaga keuangan sehat."},
              {"text": "Tetap meminjam agar bisa membeli sekarang", "next": "n6", "score": 0,
               "feedback": "Membeli sekarang dengan utang berbunga mengorbankan keamanan keuangan nanti."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kamu memilih lembaga berizin atau menabung sendiri. Keuangan aman dan data pribadi terlindungi."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Pinjaman berjalan, tetapi kamu masih menanggung bunga dan risiko di kemudian hari."},
         {"id": "n7", "end": True, "outcome": "neutral",
          "text": "Beban terasa, tetapi keterbukaan kepada keluarga membuka jalan penyelesaian yang lebih aman."},
         {"id": "n8", "end": True, "outcome": "bad",
          "text": "Utang baru menutup utang lama. Tagihan makin besar dan tekanan terus bertambah."},
     ]},
    {"type": "challenge", "id": "ch-pai4-syariah",
     "title": "Tantangan Kilat: Akad dan Lembaga Keuangan Syariah",
     "time_limit": 90,
     "items": [
         {"question": "Perjanjian dasar transaksi disebut…", "answer": "akad"},
         {"question": "Kerja sama usaha dengan bagi hasil disebut…", "answer": "mudarabah"},
         {"question": "Kerja sama modal disebut…", "answer": "musyarakah"},
         {"question": "Titipan dana yang dapat diambil kembali disebut…", "answer": "wadiah"},
         {"question": "Dana tolong-menolong untuk menanggung risiko disebut…", "answer": "tabarru"},
         {"question": "Tambahan tanpa imbalan sah disebut…", "answer": "riba"},
         {"question": "Ketidakjelasan dalam transaksi disebut…", "answer": "gharar"},
     ],
     "feedback": {
         "correct": "Tepat — akad yang jelas dan halal melindungi kedua pihak dari riba dan gharar.",
         "wrong": "Ingat istilahnya: akad, mudarabah, musyarakah, wadiah, tabarru', riba, dan gharar.",
     }},
])
save(path, data)

# ── PAI 5 — Meneladani Ulama Penyebar Islam ───────────────────────────
path = 'pai-5-meneladani-ulama-penyebar-islam.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pai5-jalur", "engine": "mermaid",
     "title": "Lima jalur masuknya Islam ke Nusantara",
     "code": "flowchart LR\n  A[Perdagangan] --> F[Islam diterima secara damai]\n  B[Perkawinan] --> F\n  C[Pendidikan] --> F\n  D[Tasawuf] --> F\n  E[Kesenian] --> F\n  F --> G[Bersifat akomodatif terhadap budaya]\n  G --> H[Tidak menghapus bahasa dan tradisi setempat]"},
    {"type": "checkpoint", "id": "cp-pai5-kerajaan",
     "question": "Kerajaan Islam pertama di Indonesia yang terletak di Aceh adalah…",
     "choices": [
         {"id": "a", "text": "Samudra Pasai", "correct": True},
         {"id": "b", "text": "Demak"},
         {"id": "c", "text": "Gowa-Tallo"},
     ],
     "explanation": "Samudra Pasai di Aceh adalah kerajaan Islam pertama. Demak adalah kerajaan Islam besar pertama di Jawa, sedangkan Gowa-Tallo berada di Sulawesi Selatan."},
    {"type": "categorize", "id": "cat-pai5-kerajaan",
     "prompt": "Kelompokkan kesultanan berikut menurut wilayahnya.",
     "buckets": [
         {"id": "aceh", "label": "Aceh"},
         {"id": "jawa", "label": "Jawa"},
         {"id": "sulawesi", "label": "Sulawesi"},
         {"id": "maluku", "label": "Maluku"},
     ],
     "items": [
         {"id": "c1", "text": "Samudra Pasai", "bucket": "aceh"},
         {"id": "c2", "text": "Aceh Darussalam", "bucket": "aceh"},
         {"id": "c3", "text": "Demak", "bucket": "jawa"},
         {"id": "c4", "text": "Mataram Islam", "bucket": "jawa"},
         {"id": "c5", "text": "Gowa-Tallo", "bucket": "sulawesi"},
         {"id": "c6", "text": "Ternate dan Tidore", "bucket": "maluku"},
     ],
     "feedback": {
         "correct": "Benar — Samudra Pasai dan Aceh Darussalam di Aceh, Demak dan Mataram Islam di Jawa, Gowa-Tallo di Sulawesi, Ternate–Tidore di Maluku.",
         "wrong": "Periksa peta: Aceh di ujung barat, Jawa di tengah, Sulawesi dan Maluku di timur.",
     }},
])

add_blocks(data, 1, [
    {"type": "glossary", "terms": [
        {"term": "Ulama", "definition": "Orang yang berilmu agama dan menjadi panutan serta pembimbing masyarakat."},
        {"term": "Pesantren", "definition": "Pusat pendidikan Islam yang mendidik santri serta melahirkan dai dan ulama."},
        {"term": "Mufasir", "definition": "Ulama yang menjelaskan dan menafsirkan isi Al-Qur'an."},
        {"term": "Sufi", "definition": "Ulama yang menekankan pendekatan spiritual dan penulisan tasawuf."},
    ]},
    {"type": "categorize", "id": "cat-pai5-tokoh",
     "prompt": "Kelompokkan ulama berikut menurut daerahnya.",
     "buckets": [
         {"id": "aceh", "label": "Aceh"},
         {"id": "gowa", "label": "Gowa"},
         {"id": "mataram", "label": "Mataram"},
         {"id": "sumbar", "label": "Sumatra Barat"},
     ],
     "items": [
         {"id": "t1", "text": "Hamzah Fansuri", "bucket": "aceh"},
         {"id": "t2", "text": "Abdurrauf as-Singkili", "bucket": "aceh"},
         {"id": "t3", "text": "Syekh Yusuf", "bucket": "gowa"},
         {"id": "t4", "text": "Sultan Agung", "bucket": "mataram"},
         {"id": "t5", "text": "Buya Hamka", "bucket": "sumbar"},
     ],
     "feedback": {
         "correct": "Benar — Hamzah Fansuri dan Abdurrauf as-Singkili dari Aceh, Syekh Yusuf dari Gowa, Sultan Agung dari Mataram, Buya Hamka dari Sumatra Barat.",
         "wrong": "Ingat pasangannya: Aceh, Gowa, Mataram, dan Sumatra Barat masing-masing punya tokoh yang disebut di materi.",
     }},
    {"type": "checkpoint", "id": "cp-pai5-hamzah",
     "question": "Ulama sufi dari Aceh yang dikenal sebagai penulis karya tasawuf adalah…",
     "choices": [
         {"id": "a", "text": "Hamzah Fansuri", "correct": True},
         {"id": "b", "text": "Buya Hamka"},
         {"id": "c", "text": "Sultan Agung"},
     ],
     "explanation": "Hamzah Fansuri adalah ulama sufi dari Aceh dan penulis tasawuf. Buya Hamka berasal dari Sumatra Barat, sedangkan Sultan Agung dari Mataram."},
    {"type": "checkpoint", "id": "cp-pai5-pesantren",
     "question": "Lembaga yang menjadi pusat pendidikan, mendidik santri, dan melahirkan dai serta ulama adalah…",
     "choices": [
         {"id": "a", "text": "Pesantren", "correct": True},
         {"id": "b", "text": "Pasar"},
         {"id": "c", "text": "Keraton"},
     ],
     "explanation": "Pesantren menjadi pusat pendidikan Islam: mendidik santri, melahirkan dai dan ulama, serta menjadi penggerak perubahan sosial."},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-pai5-budaya",
     "prompt": "Kelompokkan sikap terhadap budaya setempat sesuai prinsip dakwah ulama.",
     "buckets": [
         {"id": "diterima", "label": "Diakomodasi"},
         {"id": "ditolak", "label": "Tidak diakomodasi"},
     ],
     "items": [
         {"id": "b1", "text": "Wayang sebagai media dakwah", "bucket": "diterima"},
         {"id": "b2", "text": "Gamelan sebagai media dakwah", "bucket": "diterima"},
         {"id": "b3", "text": "Bahasa dan tradisi setempat yang tidak bertentangan dengan syariat", "bucket": "diterima"},
         {"id": "b4", "text": "Tradisi yang menabrak nilai agama", "bucket": "ditolak"},
     ],
     "feedback": {
         "correct": "Benar — ulama memilih budaya yang bermanfaat dan tidak menabrak nilai agama, bukan menerima atau menolak semuanya.",
         "wrong": "Prinsipnya selektif: budaya yang bermanfaat diakomodasi, yang bertentangan dengan syariat ditolak.",
     }},
    {"type": "scenario", "id": "sc-pai5-dakwah",
     "title": "Berdakwah di lingkungan sekolah yang beragam",
     "start": "n1",
     "nodes": [
         {"id": "n1", "text": "Kelasmu punya teman dari berbagai keyakinan. Kamu ingin berbagi kebaikan. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menjadi teladan akhlak dan menawarkan bantuan tanpa memaksa", "next": "n2", "score": 2,
               "feedback": "Dakwah damai menampilkan keteladanan, bukan paksaan — sesuai cara ulama menyebarkan Islam."},
              {"text": "Mendebat keyakinan teman agar ia berubah", "next": "n3", "score": 0,
               "feedback": "Debat yang menyerang membuat orang menjauh dan bertentangan dengan dakwah santun."},
              {"text": "Tidak berbuat apa-apa karena takut salah bicara", "next": "n4", "score": 1,
               "feedback": "Hati-hati itu baik, tetapi menahan kebaikan membuat teladan tidak terlihat."},
          ]},
         {"id": "n2", "text": "Sekolah mengadakan festival budaya. Ada usulan menampilkan kesenian daerah. Bagaimana sikapmu?",
          "choices": [
              {"text": "Mendukung selama tidak bertentangan dengan syariat", "next": "n5", "score": 2,
               "feedback": "Akomodasi budaya yang bermanfaat adalah cara ulama mendekatkan pesan tanpa menghapus tradisi."},
              {"text": "Menolak semua kesenian daerah", "next": "n6", "score": 0,
               "feedback": "Menolak semuanya bertentangan dengan sikap akomodatif ulama terhadap budaya yang tidak melanggar syariat."},
          ]},
         {"id": "n3", "text": "Temanmu tersinggung dan menjauh. Apa langkahmu?",
          "choices": [
              {"text": "Meminta maaf dan memperbaiki cara berbicara", "next": "n2", "score": 1,
               "feedback": "Meminta maaf memulihkan hubungan dan membuka jalan dakwah yang lebih santun."},
              {"text": "Merasa benar dan membiarkannya menjauh", "next": "n7", "score": 0,
               "feedback": "Membiarkan perpecahan menghilangkan kesempatan menampilkan akhlak baik."},
          ]},
         {"id": "n4", "text": "Seorang teman bertanya tentang ajaran Islam. Apa yang kamu lakukan?",
          "choices": [
              {"text": "Menjelaskan dengan santun sesuai pengetahuan dan mengajak bertanya kepada guru", "next": "n5", "score": 2,
               "feedback": "Menjelaskan dengan santun dan merujuk kepada guru menjaga kebenaran sekaligus kerukunan."},
              {"text": "Menjawab sebisanya tanpa peduli benar atau salah", "next": "n6", "score": 0,
               "feedback": "Menjawab tanpa dasar berisiko menyampaikan ajaran yang keliru."},
          ]},
         {"id": "n5", "end": True, "outcome": "good",
          "text": "Kebaikan tersampaikan lewat keteladanan. Teman-teman menghargai sikapmu dan persatuan kelas terjaga."},
         {"id": "n6", "end": True, "outcome": "neutral",
          "text": "Niatmu baik, tetapi caranya belum tepat. Perbaiki dengan belajar dan bertanya kepada guru."},
         {"id": "n7", "end": True, "outcome": "bad",
          "text": "Hubungan renggang dan pesan kebaikan tidak tersampaikan. Dakwah santun justru menjaga hubungan."},
     ]},
    {"type": "challenge", "id": "ch-pai5-ulama",
     "title": "Tantangan Kilat: Ulama Penyebar Islam",
     "time_limit": 90,
     "items": [
         {"question": "Kerajaan Islam pertama di Indonesia di Aceh adalah…", "answer": "samudra pasai"},
         {"question": "Kerajaan Islam besar pertama di Jawa adalah…", "answer": "demak"},
         {"question": "Ulama sufi penulis tasawuf dari Aceh adalah Hamzah…", "answer": "fansuri"},
         {"question": "Ulama dan pejuang dari Gowa adalah Syekh…", "answer": "yusuf"},
         {"question": "Sunan yang berdakwah melalui wayang dan gamelan adalah Sunan…", "answer": "kalijaga"},
         {"question": "Pusat pendidikan yang melahirkan dai dan ulama disebut…", "answer": "pesantren"},
     ],
     "feedback": {
         "correct": "Tepat — jalur damai, akomodasi budaya, dan keteladanan membuat Islam mudah diterima di Nusantara.",
         "wrong": "Ingat: Samudra Pasai, Demak, Hamzah Fansuri, Syekh Yusuf, Sunan Kalijaga, dan pesantren.",
     }},
])
save(path, data)

print('batch 7a: PAI 1 sampai PAI 5 selesai')
