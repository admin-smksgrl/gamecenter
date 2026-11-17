"""Fase 5.1 batch 3b — blok interaktif untuk MA 2.1 (Barisan) dan MA 2.2 (Deret).

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b3b.py`
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


# ── MA 2.1 — Barisan ──────────────────────────────────────────────────
path = 'matematika/ma-2.1-barisan.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Barisan aritmetika", "definition": "Barisan yang setiap suku diperoleh dengan menambah bilangan tetap (beda)."},
        {"term": "Beda (b)", "definition": "Selisih tetap antara dua suku berurutan pada barisan aritmetika."},
        {"term": "Rasio (r)", "definition": "Hasil bagi tetap antara dua suku berurutan pada barisan geometri."},
        {"term": "Suku pertama (a)", "definition": "Nilai U₁ yang menjadi titik awal barisan."},
    ]},
    {"type": "chart", "id": "ch-banding-barisan", "kind": "line",
     "title": "Aritmetika (tambah 3) versus geometri (kali 3)",
     "desc": "Garis aritmetika 2, 5, 8, 11, 14 naik tetap; garis geometri 2, 6, 18, 54 naik makin cepat.",
     "data": [
         {"label": "1", "value": 2},
         {"label": "2", "value": 5},
         {"label": "3", "value": 8},
         {"label": "4", "value": 11},
         {"label": "5", "value": 14},
     ]},
    {"type": "checkpoint", "id": "cp-beda-barisan",
     "question": "Barisan 4, 8, 12, 16, … adalah barisan…",
     "choices": [
         {"id": "a", "text": "Aritmetika dengan b = 4", "correct": True},
         {"id": "b", "text": "Geometri dengan r = 4"},
         {"id": "c", "text": "Aritmetika dengan b = 2"},
     ],
     "explanation": "Selisih suku berurutan selalu 4 (8 − 4 = 4, 12 − 8 = 4), jadi barisan aritmetika dengan beda 4."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-cari-beda",
     "prompt": "Urutkan langkah menentukan beda bila U₃ = 11 dan U₇ = 27.",
     "items": [
         {"id": "s1", "text": "Hitung selisih indeks: 7 − 3 = 4 langkah"},
         {"id": "s2", "text": "Hitung selisih nilai: 27 − 11 = 16"},
         {"id": "s3", "text": "Bagi selisih nilai dengan selisih indeks: 16 ÷ 4"},
         {"id": "s4", "text": "Peroleh beda b = 4"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: beda = selisih nilai dibagi selisih indeks.",
         "wrong": "Hitung dulu jarak indeks antar dua suku, baru bagi selisih nilainya.",
     }},
    {"type": "checkpoint", "id": "cp-suku-ke-n",
     "question": "Barisan 5, 9, 13, 17, … memiliki U₁₀ = …",
     "choices": [
         {"id": "a", "text": "41", "correct": True},
         {"id": "b", "text": "45"},
         {"id": "c", "text": "40"},
     ],
     "explanation": "a = 5, b = 4, sehingga U₁₀ = 5 + (10 − 1) × 4 = 5 + 36 = 41."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-barisan-cepat",
     "title": "Tantangan Kilat: Barisan",
     "time_limit": 90,
     "items": [
         {"question": "5, 9, 13, … memiliki U₁₀ = …", "answer": "41"},
         {"question": "3, 6, 12, 24, … memiliki U₈ = …", "answer": "384"},
         {"question": "Baris pertama 12 kursi, tiap baris +4. Baris ke-8 = … kursi", "answer": "40"},
         {"question": "Barisan 3, 9, 27, 81 memiliki rasio …", "answer": "3"},
         {"question": "U₃ = 11 dan U₇ = 27 pada barisan aritmetika. Beda b = …", "answer": "4"},
     ],
     "feedback": {
         "correct": "Tepat — rumus Uₙ dan penentuan beda/rasio sudah dipakai benar.",
         "wrong": "Ingat Uₙ = a + (n − 1)b dan Uₙ = a × rⁿ⁻¹; pangkatnya (n − 1), bukan n.",
     }},
])
save(path, data)

# ── MA 2.2 — Deret ───────────────────────────────────────────────────
path = 'matematika/ma-2.2-deret.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Deret", "definition": "Jumlah suku-suku suatu barisan, ditulis dengan tanda tambah."},
        {"term": "Sₙ", "definition": "Jumlah n suku pertama barisan."},
        {"term": "Deret konvergen", "definition": "Deret geometri tak hingga dengan |r| < 1 yang jumlahnya menuju satu nilai tetap."},
        {"term": "Suku ke-n dari jumlah", "definition": "Uₙ = Sₙ − Sₙ₋₁, selisih dua jumlah berurutan."},
    ]},
    {"type": "chart", "id": "ch-jumlah-kumulatif", "kind": "bar",
     "title": "Jumlah kumulatif 2 + 5 + 8 + 11 + 14",
     "desc": "Grafik batang jumlah kumulatif: S1 = 2, S2 = 7, S3 = 15, S4 = 26, S5 = 40.",
     "data": [
         {"label": "S1", "value": 2},
         {"label": "S2", "value": 7},
         {"label": "S3", "value": 15},
         {"label": "S4", "value": 26},
         {"label": "S5", "value": 40},
     ]},
    {"type": "checkpoint", "id": "cp-sn-selisih",
     "question": "Jika S₅ = 40 dan S₄ = 26, maka U₅ = …",
     "choices": [
         {"id": "a", "text": "14", "correct": True},
         {"id": "b", "text": "40"},
         {"id": "c", "text": "66"},
     ],
     "explanation": "Uₙ = Sₙ − Sₙ₋₁, sehingga U₅ = 40 − 26 = 14 — sesuai suku kelima barisan 2, 5, 8, 11, 14."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-jumlah-aritmetika",
     "prompt": "Urutkan langkah menghitung S₁₀ dari 3 + 7 + 11 + …",
     "items": [
         {"id": "s1", "text": "Tentukan a = 3, b = 4, dan n = 10"},
         {"id": "s2", "text": "Pilih rumus Sₙ = (n/2)(2a + (n − 1)b)"},
         {"id": "s3", "text": "Substitusi: (10/2)(6 + 9 × 4)"},
         {"id": "s4", "text": "Hitung: 5 × 42 = 210"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: tentukan unsur, pilih rumus, substitusi, lalu hitung.",
         "wrong": "Mulai dengan mencatat a, b, dan n agar substitusi tidak tertukar.",
     }},
    {"type": "checkpoint", "id": "cp-tak-hingga",
     "question": "Jumlah tak hingga 8 + 4 + 2 + 1 + … adalah…",
     "choices": [
         {"id": "a", "text": "16", "correct": True},
         {"id": "b", "text": "15"},
         {"id": "c", "text": "Tidak punya jumlah karena deretnya membesar"},
     ],
     "explanation": "a = 8 dan r = ½ (|r| < 1), sehingga S∞ = a/(1 − r) = 8/0,5 = 16."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-deret-cepat",
     "title": "Tantangan Kilat: Deret",
     "time_limit": 100,
     "items": [
         {"question": "S₁₀ dari 3 + 7 + 11 + … = …", "answer": "210"},
         {"question": "S₅ dari 2 + 6 + 18 + … = …", "answer": "242"},
         {"question": "8 + 4 + 2 + … tak hingga = …", "answer": "16"},
         {"question": "½ + ¼ + ⅛ + … tak hingga = …", "answer": "1"},
         {"question": "Tabungan 100 ribu, naik 25 ribu/bulan. Total 12 bulan = … ribu rupiah", "answer": "2850"},
     ],
     "feedback": {
         "correct": "Semua tepat — rumus jumlah aritmetika dan geometri sudah dipakai benar.",
         "wrong": "Periksa n, a, dan b/r; untuk tak hingga pastikan |r| < 1 lebih dulu.",
     }},
])
save(path, data)

print('batch 3b: MA 2.1 dan MA 2.2 selesai')
