"""Fase 5.1 batch 3a — blok interaktif untuk FIS 2 dan MA 1.2.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b3a.py`
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


# ── FIS 2 — Usaha, Energi, dan Energi Terbarukan ──────────────────────
path = 'fisika/fis-2-usaha-energi-terbarukan.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Usaha", "definition": "Hasil kali gaya dengan perpindahan searah gaya, W = F × s × cos θ."},
        {"term": "Daya", "definition": "Usaha yang dilakukan per satuan waktu, P = W ÷ t, satuannya watt."},
        {"term": "Energi kinetik", "definition": "Energi yang dimiliki benda karena bergerak, Ek = ½mv²."},
        {"term": "Energi potensial", "definition": "Energi yang dimiliki benda karena posisinya, Ep = mgh."},
    ]},
    {"type": "chart", "id": "ch-usaha-sudut", "kind": "bar",
     "title": "Faktor cos θ pada usaha",
     "desc": "Grafik batang: cos 0 derajat = 1, cos 60 derajat = 0,5, cos 90 derajat = 0, sehingga usaha menjadi nol saat gaya tegak lurus perpindahan.",
     "data": [
         {"label": "0°", "value": 1},
         {"label": "30°", "value": 0.87},
         {"label": "60°", "value": 0.5},
         {"label": "90°", "value": 0},
     ]},
    {"type": "checkpoint", "id": "cp-usaha-tegak-lurus",
     "question": "Seseorang membawa tas dengan tangan lurus ke bawah sambil berjalan mendatar. Usaha oleh gaya angkat tangan terhadap tas adalah…",
     "choices": [
         {"id": "a", "text": "Nol, karena gaya tegak lurus perpindahan", "correct": True},
         {"id": "b", "text": "Positif sebesar m × g × s"},
         {"id": "c", "text": "Negatif karena tas berayun"},
     ],
     "explanation": "Usaha W = F × s × cos θ. Gaya angkat ke atas tegak lurus perpindahan mendatar, sehingga cos 90° = 0 dan usahanya nol."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-kekekalan-energi",
     "prompt": "Urutkan langkah menyelesaikan soal kekekalan energi mekanik.",
     "items": [
         {"id": "s1", "text": "Tentukan titik awal dan titik akhir lintasan"},
         {"id": "s2", "text": "Tulis Ep + Ek di kedua titik"},
         {"id": "s3", "text": "Samakan jumlah energi di kedua titik (tanpa gesekan)"},
         {"id": "s4", "text": "Selesaikan persamaan untuk besaran yang ditanya"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Urutan benar: pilih titik, tulis energi, samakan, lalu hitung.",
         "wrong": "Mulai dengan menentukan dua titik, baru menuliskan Ep dan Ek pada masing-masing.",
     }},
    {"type": "checkpoint", "id": "cp-jatuh-bebas",
     "question": "Bola dilepas dari ketinggian 5 m tanpa gesekan (g = 10 m/s²). Kecepatannya saat menyentuh tanah adalah…",
     "choices": [
         {"id": "a", "text": "10 m/s", "correct": True},
         {"id": "b", "text": "5 m/s"},
         {"id": "c", "text": "50 m/s"},
     ],
     "explanation": "mgh = ½mv² sehingga v = √(2gh) = √(2 × 10 × 5) = √100 = 10 m/s. Massa tidak memengaruhi hasil."},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-energi-sumber",
     "prompt": "Kelompokkan sumber energi berikut.",
     "buckets": [
         {"id": "terbarukan", "label": "Terbarukan"},
         {"id": "fosil", "label": "Tidak terbarukan"},
     ],
     "items": [
         {"id": "c1", "text": "Panas bumi", "bucket": "terbarukan"},
         {"id": "c2", "text": "Batu bara", "bucket": "fosil"},
         {"id": "c3", "text": "Angin", "bucket": "terbarukan"},
         {"id": "c4", "text": "Minyak bumi", "bucket": "fosil"},
         {"id": "c5", "text": "Biomassa", "bucket": "terbarukan"},
         {"id": "c6", "text": "Gas alam", "bucket": "fosil"},
     ],
     "feedback": {
         "correct": "Benar — sumber terbarukan dapat pulih, fosil terbatas dan beremisi.",
         "wrong": "Sumber terbarukan terus tersedia (matahari, angin, air, panas bumi, biomassa).",
     }},
    {"type": "challenge", "id": "ch-energi-cepat",
     "title": "Tantangan Kilat: Usaha & Energi",
     "time_limit": 90,
     "items": [
         {"question": "Gaya 20 N menggeser benda 3 m searah. Usaha = … J", "answer": "60"},
         {"question": "Usaha 60 J dalam 5 sekon menghasilkan daya … W", "answer": "12"},
         {"question": "Pembangkit listrik tenaga air disingkat …", "answer": "plta"},
         {"question": "Energi kinetik berbanding … dengan kecepatan (tulis 'kuadrat' atau 'lurus')", "answer": "kuadrat"},
         {"question": "Gaya tegak lurus perpindahan menghasilkan usaha … J", "answer": "0"},
     ],
     "feedback": {
         "correct": "Tepat — rumus usaha, daya, dan konversi energi sudah dipakai benar.",
         "wrong": "Ingat W = F·s·cos θ, P = W/t, dan Ek = ½mv² (kuadrat terhadap v).",
     }},
])
save(path, data)

# ── MA 1.2 — Logaritma ────────────────────────────────────────────────
path = 'matematika/ma-1.2-logaritma.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Logaritma", "definition": "Pangkat yang harus diberikan pada basis agar hasilnya sama dengan numerus: ᵃlog b = c berarti aᶜ = b."},
        {"term": "Basis", "definition": "Bilangan pokok logaritma, harus positif dan tidak sama dengan 1."},
        {"term": "Numerus", "definition": "Bilangan yang dicari logaritmanya, harus lebih besar dari nol."},
        {"term": "Logaritma natural", "definition": "Logaritma dengan basis e ≈ 2,718, ditulis ln."},
    ]},
    {"type": "chart", "id": "ch-log2", "kind": "bar",
     "title": "Nilai ²log x untuk x = 1, 2, 4, 8, 16",
     "desc": "Setiap kali numerus berlipat dua, nilai logaritma bertambah satu: ²log 1 = 0, ²log 2 = 1, ²log 4 = 2, ²log 8 = 3, ²log 16 = 4.",
     "data": [
         {"label": "1", "value": 0},
         {"label": "2", "value": 1},
         {"label": "4", "value": 2},
         {"label": "8", "value": 3},
         {"label": "16", "value": 4},
     ]},
    {"type": "checkpoint", "id": "cp-log-definisi",
     "question": "Nilai ⁵log 1 adalah…",
     "choices": [
         {"id": "a", "text": "0", "correct": True},
         {"id": "b", "text": "1"},
         {"id": "c", "text": "5"},
     ],
     "explanation": "Karena 5⁰ = 1, maka ⁵log 1 = 0. Logaritma dari 1 selalu bernilai nol untuk basis apa pun yang sah."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-gabung-log",
     "prompt": "Urutkan langkah menghitung ²log 6 + ²log 8 − ²log 3.",
     "items": [
         {"id": "s1", "text": "Periksa bahwa semua basis sama, yaitu 2"},
         {"id": "s2", "text": "Gabungkan menjadi ²log (6 × 8 ÷ 3)"},
         {"id": "s3", "text": "Sederhanakan numerus menjadi 16"},
         {"id": "s4", "text": "Hitung ²log 16 = 4"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: samakan basis, gabungkan numerus, sederhanakan, lalu hitung.",
         "wrong": "Jangan menjumlah nilai lognya langsung; gabungkan dulu bilangan di dalam log.",
     }},
    {"type": "checkpoint", "id": "cp-log-pangkat",
     "question": "Nilai ²log 8² adalah…",
     "choices": [
         {"id": "a", "text": "6", "correct": True},
         {"id": "b", "text": "3"},
         {"id": "c", "text": "9"},
     ],
     "explanation": "Gunakan ᵃlog bⁿ = n × ᵃlog b: ²log 8² = 2 × ²log 8 = 2 × 3 = 6."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-logaritma-cepat",
     "title": "Tantangan Kilat: Logaritma",
     "time_limit": 80,
     "items": [
         {"question": "²log 16 = …", "answer": "4"},
         {"question": "²log 8 = …", "answer": "3"},
         {"question": "⁹log 1 = …", "answer": "0"},
         {"question": "Larutan dengan [H⁺] = 10⁻⁴ memiliki pH = …", "answer": "4"},
         {"question": "Bunyi 60 dB … kali lebih kuat daripada 50 dB", "answer": "10"},
     ],
     "feedback": {
         "correct": "Tepat — definisi dan sifat logaritma sudah melekat.",
         "wrong": "Ingat ᵃlog b = c berarti aᶜ = b, serta ᵃlog bⁿ = n × ᵃlog b.",
     }},
])
save(path, data)

print('batch 3a: FIS 2 dan MA 1.2 selesai')
