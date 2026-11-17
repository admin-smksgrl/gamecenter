"""Fase 5.1 batch 5b — blok interaktif untuk MA 7.1 (Statistika) dan MA 8.1 (Peluang).

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b5b.py`
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


# ── MA 7.1 — Statistika ───────────────────────────────────────────────
path = 'matematika/ma-7.1-statistika.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "chart", "id": "ch-data-tunggal", "kind": "bar",
     "title": "Data 7, 8, 8, 9, 10",
     "desc": "Grafik batang lima data: 7 muncul sekali, 8 muncul dua kali, 9 sekali, dan 10 sekali. Mean 8,4; median 8; modus 8.",
     "data": [
         {"label": "7", "value": 1},
         {"label": "8", "value": 2},
         {"label": "9", "value": 1},
         {"label": "10", "value": 1},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Mean", "definition": "Jumlah seluruh data dibagi banyak data (rata-rata)."},
        {"term": "Median", "definition": "Nilai tengah setelah data diurutkan; untuk data genap diambil rata-rata dua nilai tengah."},
        {"term": "Modus", "definition": "Nilai yang paling sering muncul dalam data."},
        {"term": "Jangkauan", "definition": "Selisih data terbesar dan data terkecil, menggambarkan sebaran data."},
    ]},
    {"type": "checkpoint", "id": "cp-median-genap",
     "question": "Median dari data 1, 2, 3, 4, 5, 6 adalah…",
     "choices": [
         {"id": "a", "text": "3,5", "correct": True},
         {"id": "b", "text": "3"},
         {"id": "c", "text": "4"},
     ],
     "explanation": "Banyak data genap, jadi median = rata-rata dua nilai tengah = (3 + 4) ÷ 2 = 3,5. Data harus diurutkan lebih dulu."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-ukuran-ekstrem",
     "prompt": "Kelompokkan ukuran statistika berdasarkan pengaruh nilai ekstrem.",
     "buckets": [
         {"id": "terpengaruh", "label": "Terpengaruh nilai ekstrem"},
         {"id": "aman", "label": "Tidak terpengaruh"},
     ],
     "items": [
         {"id": "c1", "text": "Mean", "bucket": "terpengaruh"},
         {"id": "c2", "text": "Median", "bucket": "aman"},
         {"id": "c3", "text": "Modus", "bucket": "aman"},
         {"id": "c4", "text": "Jangkauan", "bucket": "terpengaruh"},
     ],
     "feedback": {
         "correct": "Benar — mean dan jangkauan memakai nilai ekstrem, median dan modus tidak.",
         "wrong": "Mean memakai seluruh nilai dan jangkauan memakai nilai terbesar/terkecil, jadi keduanya ikut berubah.",
     }},
    {"type": "checkpoint", "id": "cp-gaji-median",
     "question": "Empat pegawai bergaji 5 juta dan satu direktur bergaji 100 juta. Ukuran yang paling menggambarkan keadaan sebenarnya adalah…",
     "choices": [
         {"id": "a", "text": "Median, yaitu 5 juta", "correct": True},
         {"id": "b", "text": "Mean, yaitu 24 juta"},
         {"id": "c", "text": "Jangkauan, yaitu 95 juta"},
     ],
     "explanation": "Mean tertarik oleh gaji direktur sehingga terlihat jauh lebih tinggi daripada kenyataan. Median tetap 5 juta karena hanya melihat posisi tengah."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-statistika-cepat",
     "title": "Tantangan Kilat: Statistika",
     "time_limit": 80,
     "items": [
         {"question": "Mean 5 data adalah 8. Jumlah seluruh data = …", "answer": "40"},
         {"question": "Empat data 6, 7, 9, 10 dengan mean 8. Data kelima = …", "answer": "8"},
         {"question": "Jangkauan data 7, 8, 8, 9, 10 = …", "answer": "3"},
         {"question": "Modus data 7, 8, 8, 9, 10 = …", "answer": "8"},
         {"question": "Mean 4 data 10 lalu ditambah data 15. Mean baru = …", "answer": "11"},
     ],
     "feedback": {
         "correct": "Tepat — selalu mulai dari jumlah total = mean × banyak data.",
         "wrong": "Kembalikan mean ke jumlah total lebih dulu, lalu tambahkan atau kurangkan data baru.",
     }},
])
save(path, data)

# ── MA 8.1 — Peluang ─────────────────────────────────────────────────
path = 'matematika/ma-8.1-peluang.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "chart", "id": "ch-peluang-dadu", "kind": "bar",
     "title": "Banyak pasangan dua dadu untuk jumlah 2 sampai 7",
     "desc": "Grafik batang dari 36 pasangan: jumlah 2 ada 1, jumlah 3 ada 2, jumlah 4 ada 3, jumlah 5 ada 4, jumlah 6 ada 5, jumlah 7 ada 6 pasangan.",
     "data": [
         {"label": "2", "value": 1},
         {"label": "3", "value": 2},
         {"label": "4", "value": 3},
         {"label": "5", "value": 4},
         {"label": "6", "value": 5},
         {"label": "7", "value": 6},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Ruang sampel", "definition": "Himpunan semua hasil yang mungkin dari suatu percobaan."},
        {"term": "Kejadian", "definition": "Himpunan hasil yang kita inginkan, bagian dari ruang sampel."},
        {"term": "Komplemen", "definition": "Kejadian \"bukan A\" dengan peluang P(Aᶜ) = 1 − P(A)."},
        {"term": "Kejadian saling bebas", "definition": "Dua kejadian yang peluangnya tidak saling memengaruhi: P(A dan B) = P(A) × P(B)."},
    ]},
    {"type": "checkpoint", "id": "cp-ruang-sampel-dadu",
     "question": "Banyak anggota ruang sampel pelemparan dua dadu adalah…",
     "choices": [
         {"id": "a", "text": "36", "correct": True},
         {"id": "b", "text": "12"},
         {"id": "c", "text": "18"},
     ],
     "explanation": "Aturan perkalian: dadu pertama 6 kemungkinan dan dadu kedua 6 kemungkinan, sehingga 6 × 6 = 36 pasangan berurutan."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-hitung-peluang",
     "prompt": "Urutkan langkah menghitung peluang suatu kejadian.",
     "items": [
         {"id": "s1", "text": "Tentukan ruang sampel dan banyak anggotanya n(S)"},
         {"id": "s2", "text": "Tentukan kejadian yang diinginkan dan n(A)"},
         {"id": "s3", "text": "Bagi: P(A) = n(A) ÷ n(S)"},
         {"id": "s4", "text": "Periksa hasilnya berada antara 0 dan 1"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: ruang sampel, kejadian, bagi, lalu periksa kisarannya.",
         "wrong": "Pembilang adalah hasil yang diinginkan, penyebut adalah seluruh ruang sampel.",
     }},
    {"type": "checkpoint", "id": "cp-komplemen",
     "question": "Peluang muncul bukan mata 6 pada satu dadu adalah…",
     "choices": [
         {"id": "a", "text": "5/6", "correct": True},
         {"id": "b", "text": "1/6"},
         {"id": "c", "text": "1/5"},
     ],
     "explanation": "Gunakan komplemen: P(bukan 6) = 1 − P(6) = 1 − 1/6 = 5/6."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-peluang-cepat",
     "title": "Tantangan Kilat: Peluang",
     "time_limit": 80,
     "items": [
         {"question": "Dua koin dilempar. n(S) = …", "answer": "4"},
         {"question": "Tiga koin dilempar. n(S) = …", "answer": "8"},
         {"question": "Dua dadu dilempar. n(S) = …", "answer": "36"},
         {"question": "Peluang jumlah 7 pada dua dadu = 1/…", "answer": "6"},
         {"question": "Peluang bukan mata 6 pada satu dadu = 5/…", "answer": "6"},
     ],
     "feedback": {
         "correct": "Tepat — aturan perkalian dan komplemen sudah dipakai benar.",
         "wrong": "Hitung n(S) dengan aturan perkalian, lalu bandingkan dengan n(A).",
     }},
])
save(path, data)

print('batch 5b: MA 7.1 dan MA 8.1 selesai')
