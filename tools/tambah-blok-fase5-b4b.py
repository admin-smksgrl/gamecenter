"""Fase 5.1 batch 4b — blok interaktif untuk MA 5.1 (SPL) dan MA 5.2 (Pertidaksamaan).

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b4b.py`
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


# ── MA 5.1 — Sistem Persamaan Linear ──────────────────────────────────
path = 'matematika/ma-5.1-spl.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-spl-kasus", "engine": "mermaid",
     "title": "Tiga kemungkinan penyelesaian SPLDV",
     "code": "flowchart TD\n  A[SPLDV dua variabel] --> B[Dua garis berpotongan]\n  A --> C[Dua garis sejajar]\n  A --> D[Dua garis berimpit]\n  B --> B1[Satu penyelesaian]\n  C --> C1[Tidak ada penyelesaian]\n  D --> D1[Tak hingga penyelesaian]"},
    {"type": "glossary", "terms": [
        {"term": "Variabel", "definition": "Nilai yang dicari, biasanya x dan y."},
        {"term": "Koefisien", "definition": "Bilangan yang mengalikan variabel pada persamaan."},
        {"term": "SPLDV", "definition": "Sistem persamaan linear dua variabel: dua persamaan dipakai bersama."},
        {"term": "Penyelesaian tunggal", "definition": "Satu pasangan (x, y) yang memenuhi kedua persamaan."},
    ]},
    {"type": "checkpoint", "id": "cp-spl-tunggal",
     "question": "Penyelesaian sistem x + y = 7 dan x − y = 1 adalah…",
     "choices": [
         {"id": "a", "text": "x = 4, y = 3", "correct": True},
         {"id": "b", "text": "x = 3, y = 4"},
         {"id": "c", "text": "x = 5, y = 2"},
     ],
     "explanation": "Jumlahkan kedua persamaan: 2x = 8 → x = 4. Substitusi ke x + y = 7 memberi y = 3, dan 4 − 3 = 1 benar."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-substitusi",
     "prompt": "Urutkan langkah metode substitusi untuk 2x + y = 8 dan x − y = 1.",
     "items": [
         {"id": "s1", "text": "Nyatakan y dari persamaan pertama: y = 8 − 2x"},
         {"id": "s2", "text": "Substitusikan ke persamaan kedua: x − (8 − 2x) = 1"},
         {"id": "s3", "text": "Selesaikan: 3x = 9 sehingga x = 3"},
         {"id": "s4", "text": "Cari y: y = 8 − 6 = 2"},
         {"id": "s5", "text": "Periksa ke kedua persamaan asal"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar: nyatakan satu variabel, substitusi, selesaikan, lalu periksa.",
         "wrong": "Substitusi selalu memerlukan satu variabel dinyatakan lebih dulu, misalnya y = 8 − 2x.",
     }},
    {"type": "checkpoint", "id": "cp-spl-substitusi",
     "question": "Dari 2x + y = 8 dan x − y = 1, nilai y adalah…",
     "choices": [
         {"id": "a", "text": "2", "correct": True},
         {"id": "b", "text": "3"},
         {"id": "c", "text": "8"},
     ],
     "explanation": "Substitusi memberi x = 3, lalu y = 8 − 2(3) = 2. Periksa: 3 − 2 = 1 memenuhi persamaan kedua."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-spl-cepat",
     "title": "Tantangan Kilat: SPLDV",
     "time_limit": 90,
     "items": [
         {"question": "x + y = 7 dan x − y = 1. Nilai x = …", "answer": "4"},
         {"question": "x + y = 7 dan x − y = 1. Nilai y = …", "answer": "3"},
         {"question": "2b + 3p = 13.000 dan b + p = 6.000. Harga pulpen = … ribu", "answer": "1"},
         {"question": "… maka harga buku = … ribu", "answer": "5"},
         {"question": "3x + 2y = 16 dan 2x + 3y = 19. Nilai x = …", "answer": "2"},
     ],
     "feedback": {
         "correct": "Tepat — eliminasi dan substitusi sudah dipakai benar.",
         "wrong": "Jumlahkan atau kurangkan persamaan untuk menghilangkan satu variabel, lalu periksa hasilnya.",
     }},
])
save(path, data)

# ── MA 5.2 — Pertidaksamaan Linear ────────────────────────────────────
path = 'matematika/ma-5.2-pertidaksamaan-linear.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-garis-batas", "engine": "mermaid",
     "title": "Memilih garis penuh atau putus-putus",
     "code": "flowchart TD\n  A[Pertidaksamaan linear] --> B[Tanda kurang dari atau lebih dari]\n  A --> C[Tanda kurang dari sama dengan atau lebih dari sama dengan]\n  B --> B1[Garis putus-putus, titik tidak termasuk]\n  C --> C1[Garis penuh, titik termasuk]"},
    {"type": "glossary", "terms": [
        {"term": "Garis batas", "definition": "Garis yang diperoleh dengan mengubah tanda pertidaksamaan menjadi tanda sama dengan."},
        {"term": "Daerah penyelesaian", "definition": "Wilayah bidang yang memenuhi semua pertidaksamaan pada sistem."},
        {"term": "Titik pojok", "definition": "Titik pertemuan garis-garis batas; tempat nilai optimum berada."},
        {"term": "Uji titik", "definition": "Memasukkan satu titik ke pertidaksamaan untuk menentukan sisi daerah yang benar."},
    ]},
    {"type": "checkpoint", "id": "cp-uji-titik",
     "question": "Apakah titik (0, 0) memenuhi x + y ≤ 5?",
     "choices": [
         {"id": "a", "text": "Ya, karena 0 + 0 = 0 ≤ 5", "correct": True},
         {"id": "b", "text": "Tidak, karena 0 lebih kecil dari 5"},
         {"id": "c", "text": "Tidak bisa ditentukan tanpa gambar"},
     ],
     "explanation": "Substitusi (0, 0) memberi 0 ≤ 5 yang bernilai benar, sehingga daerah penyelesaian memuat titik asal."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-nilai-optimum",
     "prompt": "Urutkan langkah mencari nilai optimum pada daerah penyelesaian.",
     "items": [
         {"id": "s1", "text": "Gambar garis batas dan arsir daerahnya"},
         {"id": "s2", "text": "Tentukan semua titik pojok"},
         {"id": "s3", "text": "Substitusikan setiap titik pojok ke fungsi tujuan"},
         {"id": "s4", "text": "Pilih nilai terbesar atau terkecil sesuai pertanyaan"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: gambar daerah, ambil titik pojok, hitung, lalu pilih nilai ekstremnya.",
         "wrong": "Nilai optimum selalu diperiksa di titik pojok, bukan di tengah daerah.",
     }},
    {"type": "checkpoint", "id": "cp-nilai-optimum",
     "question": "Fungsi tujuan 2x + 3y pada titik pojok (0,0), (5,0), (0,4), dan (2,3). Nilai maksimumnya adalah…",
     "choices": [
         {"id": "a", "text": "13 di titik (2, 3)", "correct": True},
         {"id": "b", "text": "12 di titik (0, 4)"},
         {"id": "c", "text": "10 di titik (5, 0)"},
     ],
     "explanation": "Nilai di tiap titik: 0, 10, 12, dan 13. Nilai terbesar 13 muncul di titik pojok (2, 3)."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-pertidaksamaan-cepat",
     "title": "Tantangan Kilat: Pertidaksamaan",
     "time_limit": 80,
     "items": [
         {"question": "Luas daerah x ≥ 0, y ≥ 0, 2x + y ≤ 8 adalah … satuan luas", "answer": "16"},
         {"question": "Apakah (1, 2) memenuhi 3x + 2y ≥ 7? Jawab ya atau tidak", "answer": "ya"},
         {"question": "Nilai 2x + 3y di titik (0, 4) adalah …", "answer": "12"},
         {"question": "Tanda ≤ memakai garis … (penuh/putus-putus)", "answer": "penuh"},
         {"question": "Setelah dikali bilangan negatif, arah tanda harus … (balik/tetap)", "answer": "balik"},
     ],
     "feedback": {
         "correct": "Tepat — garis batas, uji titik, dan nilai optimum sudah dipahami.",
         "wrong": "Ingat: ≤/≥ memakai garis penuh, dan tanda dibalik setelah dikali bilangan negatif.",
     }},
])
save(path, data)

print('batch 4b: MA 5.1 dan MA 5.2 selesai')