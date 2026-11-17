"""Fase 5.1 batch 5a — blok interaktif untuk MA 6.2 dan MA 6.3.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b5a.py`
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


# ── MA 6.2 — Membentuk dan Mengubah Bentuk Fungsi Kuadrat ─────────────
path = 'matematika/ma-6.2-membentuk-mengubah-bentuk.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-tiga-bentuk", "engine": "mermaid",
     "title": "Tiga bentuk fungsi kuadrat dan informasi yang terlihat",
     "code": "flowchart TD\n  A[Fungsi kuadrat yang sama] --> B[Bentuk umum: ax2 + bx + c]\n  A --> C[Bentuk puncak: a(x - p)2 + q]\n  A --> D[Bentuk faktor: a(x - x1)(x - x2)]\n  B --> B1[Titik potong sumbu-y]\n  C --> C1[Titik puncak]\n  D --> D1[Titik potong sumbu-x]"},
    {"type": "glossary", "terms": [
        {"term": "Bentuk umum", "definition": "f(x) = ax² + bx + c; titik potong sumbu-y langsung terbaca di (0, c)."},
        {"term": "Bentuk puncak", "definition": "f(x) = a(x − p)² + q; titik puncak langsung terbaca (p, q)."},
        {"term": "Bentuk faktor", "definition": "f(x) = a(x − x₁)(x − x₂); titik potong sumbu-x adalah x₁ dan x₂."},
        {"term": "Melengkapi kuadrat", "definition": "Teknik mengubah bentuk umum menjadi bentuk puncak dengan menambah dan mengurangi kuadrat setengah koefisien x."},
    ]},
    {"type": "checkpoint", "id": "cp-bentuk-puncak",
     "question": "Bentuk yang paling cepat menunjukkan titik puncak parabola adalah…",
     "choices": [
         {"id": "a", "text": "f(x) = 2(x − 3)² − 5", "correct": True},
         {"id": "b", "text": "f(x) = 2x² − 12x + 13"},
         {"id": "c", "text": "f(x) = 2(x − 1)(x − 5)"},
     ],
     "explanation": "Bentuk puncak a(x − p)² + q memperlihatkan puncak (3, −5) secara langsung, tanpa menghitung lagi."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-lengkapi-kuadrat",
     "prompt": "Urutkan langkah melengkapi kuadrat sempurna.",
     "items": [
         {"id": "s1", "text": "Faktorkan a dari dua suku pertama"},
         {"id": "s2", "text": "Ambil setengah koefisien x lalu kuadratkan"},
         {"id": "s3", "text": "Tambahkan dan kurangkan bilangan itu di dalam kurung"},
         {"id": "s4", "text": "Sederhanakan menjadi bentuk puncak"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: faktorkan a, ambil setengah koefisien, tambah-kurang, lalu sederhanakan.",
         "wrong": "Setengah koefisien x adalah kunci; jangan lupa menambah dan mengurangi bilangan yang sama.",
     }},
    {"type": "checkpoint", "id": "cp-puncak-lengkap",
     "question": "Bentuk puncak dari f(x) = x² − 10x + 18 adalah…",
     "choices": [
         {"id": "a", "text": "(x − 5)² − 7", "correct": True},
         {"id": "b", "text": "(x − 5)² + 18"},
         {"id": "c", "text": "(x + 5)² − 7"},
     ],
     "explanation": "Setengah dari −10 adalah −5 dan kuadratnya 25, sehingga x² − 10x = (x − 5)² − 25. Maka f(x) = (x − 5)² − 25 + 18 = (x − 5)² − 7."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-bentuk-kuadrat-cepat",
     "title": "Tantangan Kilat: Bentuk Fungsi Kuadrat",
     "time_limit": 90,
     "items": [
         {"question": "Akar 2 dan 5 dengan a = 1. Suku tetapnya = …", "answer": "10"},
         {"question": "Puncak (1, 2) melalui (0, 5). Nilai a = …", "answer": "3"},
         {"question": "Memotong sumbu-x di −3 dan 1 serta melalui (0, −3). Nilai a = …", "answer": "1"},
         {"question": "f(x) = x² − 4x + 3. Puncak p = …", "answer": "2"},
         {"question": "f(x) = 2x² + 8x + 11. Bentuk puncak 2(x + 2)² + q, q = …", "answer": "3"},
     ],
     "feedback": {
         "correct": "Tepat — memilih bentuk yang sesuai data adalah kuncinya.",
         "wrong": "Diketahui akar → bentuk faktor; diketahui puncak → bentuk puncak; tiga titik → bentuk umum.",
     }},
])
save(path, data)

# ── MA 6.3 — Menyelesaikan Masalah dengan Fungsi Kuadrat ──────────────
path = 'matematika/ma-6.3-menyelesaikan-masalah.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "chart", "id": "ch-tinggi-bola", "kind": "line",
     "title": "Tinggi bola h(t) = −5t² + 20t",
     "desc": "Grafik garis: t = 0 tinggi 0 m, t = 1 tinggi 15 m, t = 2 tinggi 20 m (puncak), t = 3 tinggi 15 m, t = 4 tinggi 0 m (menyentuh tanah).",
     "data": [
         {"label": "0", "value": 0},
         {"label": "1", "value": 15},
         {"label": "2", "value": 20},
         {"label": "3", "value": 15},
         {"label": "4", "value": 0},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Nilai maksimum", "definition": "Nilai terbesar fungsi, terjadi di titik puncak saat parabola terbuka ke bawah (a < 0)."},
        {"term": "Nilai minimum", "definition": "Nilai terkecil fungsi, terjadi di titik puncak saat parabola terbuka ke atas (a > 0)."},
        {"term": "Fungsi tujuan", "definition": "Fungsi yang hendak dimaksimumkan atau diminimumkan, misalnya luas atau laba."},
        {"term": "Akar fungsi", "definition": "Nilai variabel yang membuat fungsi bernilai nol, misalnya waktu saat bola menyentuh tanah."},
    ]},
    {"type": "checkpoint", "id": "cp-maks-min",
     "question": "Fungsi laba L(x) = −2x² + 40x − 100 memiliki a negatif. Titik puncaknya merupakan…",
     "choices": [
         {"id": "a", "text": "Nilai maksimum laba", "correct": True},
         {"id": "b", "text": "Nilai minimum laba"},
         {"id": "c", "text": "Titik potong sumbu-x"},
     ],
     "explanation": "a < 0 membuat parabola terbuka ke bawah, sehingga titik puncak adalah nilai maksimum — sesuai pertanyaan laba terbesar."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-soal-terapan",
     "prompt": "Urutkan langkah menyelesaikan soal terapan fungsi kuadrat.",
     "items": [
         {"id": "s1", "text": "Beri nama variabel yang berubah"},
         {"id": "s2", "text": "Susun fungsi tujuan dari syarat soal"},
         {"id": "s3", "text": "Cari puncak x = −b/(2a) lalu hitung nilainya"},
         {"id": "s4", "text": "Tafsirkan hasil beserta satuannya"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: beri nama, susun fungsi, cari puncak, lalu tafsirkan.",
         "wrong": "Sebelum mencari puncak, pastikan fungsinya sudah dalam satu variabel.",
     }},
    {"type": "checkpoint", "id": "cp-pagar-taman",
     "question": "Pagar 60 m dipakai untuk tiga sisi taman (sisi keempat dinding). Luas terbesar yang dapat dibuat adalah…",
     "choices": [
         {"id": "a", "text": "450 m²", "correct": True},
         {"id": "b", "text": "900 m²"},
         {"id": "c", "text": "300 m²"},
     ],
     "explanation": "L(x) = x(60 − 2x) = −2x² + 60x. Puncak di x = 15, sehingga L = 15 × 30 = 450 m²."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-kuadrat-terapan",
     "title": "Tantangan Kilat: Soal Terapan",
     "time_limit": 100,
     "items": [
         {"question": "Dua bilangan berjumlah 20. Hasil kali maksimumnya …", "answer": "100"},
         {"question": "L(x) = −2x² + 40x − 100. Puncak di x = …", "answer": "10"},
         {"question": "Laba maksimum L(10) = … ribu rupiah", "answer": "100"},
         {"question": "h(t) = −5t² + 20t. Tinggi maksimum … m", "answer": "20"},
         {"question": "h(t) = −5t² + 20t. Bola menyentuh tanah pada t = … detik", "answer": "4"},
     ],
     "feedback": {
         "correct": "Tepat — puncak untuk \"berapa\", akar untuk \"kapan\".",
         "wrong": "Pertanyaan tinggi memakai puncak; pertanyaan waktu mendarat memakai akar h(t) = 0.",
     }},
])
save(path, data)

print('batch 5a: MA 6.2 dan MA 6.3 selesai')
