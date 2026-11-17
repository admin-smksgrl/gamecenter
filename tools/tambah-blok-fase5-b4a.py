"""Fase 5.1 batch 4a — blok interaktif untuk MA 3.1 (Vektor) dan MA 4.1 (Trigonometri).

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b4a.py`
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


# ── MA 3.1 — Vektor dan Operasinya ────────────────────────────────────
path = 'matematika/ma-3.1-vektor.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-vektor-komponen", "engine": "mermaid",
     "title": "Vektor v = (3, 4) dan komponennya",
     "code": "flowchart LR\n  V[Vektor v] --> X[Komponen x = 3]\n  V --> Y[Komponen y = 4]\n  X --> P[Panjang v = akar 3 kuadrat + 4 kuadrat]\n  Y --> P\n  P --> H[Hasil panjang = 5]"},
    {"type": "glossary", "terms": [
        {"term": "Skalar", "definition": "Besaran yang hanya punya besar, misalnya massa, suhu, dan waktu."},
        {"term": "Vektor", "definition": "Besaran yang punya besar sekaligus arah, misalnya perpindahan dan gaya."},
        {"term": "Komponen vektor", "definition": "Bagian mendatar (x) dan tegak (y) yang menyusun sebuah vektor."},
        {"term": "Vektor satuan", "definition": "Vektor berpanjang 1 yang menunjukkan arah vektor asal, v̂ = v ÷ |v|."},
    ]},
    {"type": "checkpoint", "id": "cp-panjang-vektor",
     "question": "Panjang vektor v = (3, 4) adalah…",
     "choices": [
         {"id": "a", "text": "5", "correct": True},
         {"id": "b", "text": "7"},
         {"id": "c", "text": "12"},
     ],
     "explanation": "|v| = √(3² + 4²) = √(9 + 16) = √25 = 5. Panjang dihitung dengan Pythagoras, bukan dengan menjumlahkan komponen."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-vektor-satuan",
     "prompt": "Urutkan langkah menentukan vektor satuan dari v = (3, 4).",
     "items": [
         {"id": "s1", "text": "Hitung panjang vektor: |v| = 5"},
         {"id": "s2", "text": "Bagi setiap komponen dengan |v|"},
         {"id": "s3", "text": "Tulis hasilnya: v̂ = (3/5, 4/5)"},
         {"id": "s4", "text": "Periksa panjang v̂ = 1"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: panjang dulu, bagi komponen, lalu periksa hasilnya berpanjang 1.",
         "wrong": "Vektor satuan selalu dibagi dengan panjang vektor, bukan dengan komponen terbesar.",
     }},
    {"type": "checkpoint", "id": "cp-vektor-ab",
     "question": "Vektor AB dari A(1, 2) ke B(4, 6) adalah…",
     "choices": [
         {"id": "a", "text": "(3, 4)", "correct": True},
         {"id": "b", "text": "(−3, −4)"},
         {"id": "c", "text": "(5, 8)"},
     ],
     "explanation": "AB = B − A = (4 − 1, 6 − 2) = (3, 4). Arahnya dari A ke B, jadi titik akhir dikurangi titik awal."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-vektor-cepat",
     "title": "Tantangan Kilat: Vektor",
     "time_limit": 80,
     "items": [
         {"question": "Panjang vektor (3, 4) = …", "answer": "5"},
         {"question": "Panjang vektor (6, 8) = …", "answer": "10"},
         {"question": "Panjang vektor nol (0, 0) = …", "answer": "0"},
         {"question": "Dua vektor tegak lurus berpanjang 6 dan 8. Panjang resultannya …", "answer": "10"},
         {"question": "Perpindahan 4 km timur lalu 3 km utara memiliki panjang … km", "answer": "5"},
     ],
     "feedback": {
         "correct": "Tepat — panjang resultan dihitung dengan Pythagoras, bukan dijumlah langsung.",
         "wrong": "Untuk vektor tegak lurus gunakan akar dari jumlah kuadrat komponen.",
     }},
])
save(path, data)

# ── MA 4.1 — Trigonometri ─────────────────────────────────────────────
path = 'matematika/ma-4.1-trigonometri.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Sinus (sin)", "definition": "Perbandingan sisi depan sudut dengan sisi miring."},
        {"term": "Kosinus (cos)", "definition": "Perbandingan sisi samping sudut dengan sisi miring."},
        {"term": "Tangen (tan)", "definition": "Perbandingan sisi depan dengan sisi samping, tan θ = sin θ ÷ cos θ."},
        {"term": "Identitas Pythagoras", "definition": "sin² θ + cos² θ = 1, berlaku untuk setiap sudut."},
    ]},
    {"type": "checkpoint", "id": "cp-tan-definisi",
     "question": "Pada segitiga siku-siku, tan θ sama dengan…",
     "choices": [
         {"id": "a", "text": "sisi depan ÷ sisi samping", "correct": True},
         {"id": "b", "text": "sisi samping ÷ sisi miring"},
         {"id": "c", "text": "sisi miring ÷ sisi depan"},
     ],
     "explanation": "tan θ = depan ÷ samping, atau setara dengan sin θ ÷ cos θ. Sisi miring dipakai oleh sinus dan kosinus."},
])

add_blocks(data, 1, [
    {"type": "chart", "id": "ch-sin-istimewa", "kind": "bar",
     "title": "Nilai sin pada sudut istimewa",
     "desc": "Grafik batang nilai sinus: 0 derajat = 0; 30 derajat = 0,5; 45 derajat = 0,707; 60 derajat = 0,866; 90 derajat = 1.",
     "data": [
         {"label": "0°", "value": 0},
         {"label": "30°", "value": 0.5},
         {"label": "45°", "value": 0.71},
         {"label": "60°", "value": 0.87},
         {"label": "90°", "value": 1},
     ]},
    {"type": "checkpoint", "id": "cp-tan-90",
     "question": "Mengapa tan 90° tidak terdefinisi?",
     "choices": [
         {"id": "a", "text": "Karena cos 90° = 0 sehingga terjadi pembagian dengan nol", "correct": True},
         {"id": "b", "text": "Karena sin 90° = 0"},
         {"id": "c", "text": "Karena segitiga tidak punya sudut 90°"},
     ],
     "explanation": "tan θ = sin θ ÷ cos θ. Pada 90°, cos 90° = 0, dan pembagian dengan nol tidak terdefinisi."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-trigonometri-cepat",
     "title": "Tantangan Kilat: Trigonometri",
     "time_limit": 80,
     "items": [
         {"question": "Sudut yang nilai kosinusnya 0 adalah … derajat", "answer": "90"},
         {"question": "tan 45° = …", "answer": "1"},
         {"question": "sin² θ + cos² θ = …", "answer": "1"},
         {"question": "sin 30° = cos … derajat", "answer": "60"},
         {"question": "Sudut elevasi 45° dari jarak 10 m memberi tinggi tiang … m", "answer": "10"},
     ],
     "feedback": {
         "correct": "Tepat — perbandingan dan sudut istimewa sudah dikenali.",
         "wrong": "Ingat tan = depan/samping dan nilai istimewa sin 30° = ½, sin 45° = ½√2.",
     }},
])
save(path, data)

print('batch 4a: MA 3.1 dan MA 4.1 selesai')
