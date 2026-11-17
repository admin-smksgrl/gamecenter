"""Fase 5.1 batch 2a — blok interaktif untuk KIM 1, KIM 2, KIM 3.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b2a.py`
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


# ── KIM 1 — Struktur Atom dan Nanoteknologi ────────────────────────────
path = 'kimia/kim-1-struktur-atom-nanoteknologi.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-atom", "engine": "mermaid",
     "title": "Susunan partikel penyusun atom",
     "code": "flowchart TD\n  A[Atom netral] --> B[Inti atom]\n  A --> C[Kulit elektron]\n  B --> D[Proton: positif]\n  B --> E[Neutron: netral]\n  C --> F[Elektron: negatif]"},
    {"type": "glossary", "terms": [
        {"term": "Nomor atom (Z)", "definition": "Jumlah proton dalam inti atom; menentukan jenis unsur."},
        {"term": "Nomor massa (A)", "definition": "Jumlah proton ditambah neutron, ditulis sebagai bilangan bulat."},
        {"term": "Isotop", "definition": "Atom dengan nomor atom sama tetapi nomor massa berbeda, misalnya ¹²C dan ¹⁴C."},
        {"term": "Elektron valensi", "definition": "Elektron pada kulit terluar yang menentukan sifat kimia atom."},
    ]},
    {"type": "checkpoint", "id": "cp-atom-neutron",
     "question": "Atom dengan nomor atom Z = 12 dan nomor massa A = 24 memiliki … neutron.",
     "choices": [
         {"id": "a", "text": "12", "correct": True},
         {"id": "b", "text": "24"},
         {"id": "c", "text": "36"},
     ],
     "explanation": "Neutron = A − Z = 24 − 12 = 12. Jumlah proton dan elektron tetap 12 karena atom netral."},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-nano-skala",
     "question": "Ukuran 50 nm sama dengan …",
     "choices": [
         {"id": "a", "text": "5 × 10⁻⁸ m", "correct": True},
         {"id": "b", "text": "5 × 10⁻⁷ m"},
         {"id": "c", "text": "5 × 10⁻⁹ m"},
     ],
     "explanation": "1 nm = 10⁻⁹ m, jadi 50 nm = 50 × 10⁻⁹ m = 5 × 10⁻⁸ m."},
    {"type": "challenge", "id": "ch-atom-cepat",
     "title": "Tantangan Kilat: Atom & Nano",
     "time_limit": 80,
     "items": [
         {"question": "Partikel bermuatan positif di dalam inti atom adalah …", "answer": "proton"},
         {"question": "Atom dengan nomor atom sama tetapi nomor massa berbeda disebut …", "answer": "isotop"},
         {"question": "Jumlah neutron atom dengan Z = 12 dan A = 24 adalah …", "answer": "12"},
         {"question": "Kulit M maksimum berisi … elektron", "answer": "18"},
         {"question": "50 nm sama dengan … × 10⁻⁹ m", "answer": "50"},
     ],
     "feedback": {
         "correct": "Tepat — hubungan Z, A, neutron, dan skala nano sudah kuat.",
         "wrong": "Ingat: neutron = A − Z, kapasitas kulit 2-8-18-32, dan 1 nm = 10⁻⁹ m.",
     }},
])
save(path, data)

# ── KIM 2 — Hukum Dasar Kimia ─────────────────────────────────────────
path = 'kimia/kim-2-hukum-dasar-kimia.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Reaktan", "definition": "Zat yang bereaksi, ditulis di ruas kiri persamaan reaksi."},
        {"term": "Produk", "definition": "Zat hasil reaksi, ditulis di ruas kanan persamaan reaksi."},
        {"term": "Koefisien", "definition": "Angka di depan rumus zat yang boleh diubah saat menyetarakan reaksi."},
        {"term": "Katalis", "definition": "Zat yang mempercepat reaksi dengan menurunkan energi aktivasi tanpa ikut terpakai."},
    ]},
    {"type": "sort", "id": "srt-setara-reaksi",
     "prompt": "Urutkan langkah menyetarakan persamaan reaksi.",
     "items": [
         {"id": "s1", "text": "Tulis rumus reaktan dan produk"},
         {"id": "s2", "text": "Hitung jumlah atom setiap unsur"},
         {"id": "s3", "text": "Tambahkan koefisien agar jumlah atom sama"},
         {"id": "s4", "text": "Periksa ulang semua unsur"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Urutan benar: tulis, hitung, setarakan, lalu periksa ulang.",
         "wrong": "Mulai dari menulis persamaan, baru menghitung atom sebelum menambah koefisien.",
     }},
    {"type": "checkpoint", "id": "cp-setara-air",
     "question": "Pada persamaan 2H₂ + O₂ → 2H₂O, jumlah atom H di ruas kiri adalah …",
     "choices": [
         {"id": "a", "text": "4", "correct": True},
         {"id": "b", "text": "2"},
         {"id": "c", "text": "1"},
     ],
     "explanation": "Koefisien 2 dikalikan indeks 2 pada H₂ menghasilkan 4 atom H, sama dengan 2 × 2 pada 2H₂O."},
])

add_blocks(data, 1, [
    {"type": "timeline", "id": "tl-hukum-kimia",
     "title": "Empat hukum dasar kimia dan penemunya",
     "items": [
         {"when": "1789", "title": "Lavoisier — kekekalan massa",
          "text": "Massa zat sebelum dan sesudah reaksi selalu sama."},
         {"when": "1799", "title": "Proust — perbandingan tetap",
          "text": "Perbandingan massa unsur dalam satu senyawa selalu tetap."},
         {"when": "1803", "title": "Dalton — perbandingan berganda",
          "text": "Bila dua unsur membentuk beberapa senyawa, perbandingan massanya bilangan bulat sederhana."},
         {"when": "1808", "title": "Gay Lussac — perbandingan volume",
          "text": "Pada suhu dan tekanan sama, volume gas sebanding dengan koefisiennya."},
     ]},
    {"type": "categorize", "id": "cat-hukum-kimia",
     "prompt": "Kelompokkan pernyataan ke hukum yang sesuai.",
     "buckets": [
         {"id": "lavoisier", "label": "Lavoisier"},
         {"id": "proust", "label": "Proust"},
         {"id": "gaylussac", "label": "Gay Lussac"},
     ],
     "items": [
         {"id": "c1", "text": "Massa 56 g besi + 32 g belerang menghasilkan 88 g besi sulfida", "bucket": "lavoisier"},
         {"id": "c2", "text": "Massa C : O pada CO₂ selalu 3 : 8", "bucket": "proust"},
         {"id": "c3", "text": "10 L N₂ menghasilkan 20 L NH₃ pada suhu dan tekanan sama", "bucket": "gaylussac"},
         {"id": "c4", "text": "Tidak ada massa yang hilang saat kayu terbakar dalam wadah tertutup", "bucket": "lavoisier"},
     ],
     "feedback": {
         "correct": "Benar — setiap pernyataan cocok dengan bunyi hukumnya.",
         "wrong": "Bedakan: massa tetap (Lavoisier), perbandingan massa tetap (Proust), volume sebanding koefisien (Gay Lussac).",
     }},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-stoikiometri-cepat",
     "title": "Tantangan Kilat: Hitungan Hukum Dasar",
     "time_limit": 100,
     "items": [
         {"question": "56 g besi + 32 g belerang → … g besi sulfida", "answer": "88"},
         {"question": "Pada CO₂, 12 g C memerlukan … g oksigen (C : O = 3 : 8)", "answer": "32"},
         {"question": "Pada MgO, 9 g Mg memerlukan … g oksigen (Mg : O = 3 : 2)", "answer": "6"},
         {"question": "N₂ + 3H₂ → 2NH₃. Volume 10 L N₂ menghasilkan … L NH₃", "answer": "20"},
         {"question": "24 g karbon membentuk 88 g CO₂. Massa oksigen yang bereaksi = … g", "answer": "64"},
     ],
     "feedback": {
         "correct": "Semua tepat — perbandingan koefisien sudah dipakai dengan benar.",
         "wrong": "Gunakan perbandingan koefisien atau perbandingan massa unsur, lalu periksa satuannya.",
     }},
])
save(path, data)

# ── KIM 3 — Kimia Hijau ───────────────────────────────────────────────
path = 'kimia/kim-3-kimia-hijau.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "glossary", "terms": [
        {"term": "Kimia hijau", "definition": "Pendekatan kimia untuk mengurangi atau menghilangkan zat berbahaya bagi manusia dan lingkungan."},
        {"term": "Efisiensi atom", "definition": "Bagian atom reaktan yang berubah menjadi produk; makin tinggi, makin sedikit limbah."},
        {"term": "Pencegahan limbah", "definition": "Prinsip utama kimia hijau: mencegah limbah lebih baik daripada mengolahnya setelah terbentuk."},
        {"term": "Degradasi", "definition": "Terurainya produk secara alami setelah dipakai sehingga tidak menumpuk di lingkungan."},
    ]},
    {"type": "diagram", "id": "dg-siklus-hijau", "engine": "mermaid",
     "title": "Siklus kegiatan kimia hijau",
     "code": "flowchart LR\n  A[Amati masalah] --> B[Pilih prinsip kimia hijau]\n  B --> C[Rancang kegiatan]\n  C --> D[Laksanakan dan catat]\n  D --> E[Evaluasi dan perbaiki]\n  E --> B"},
    {"type": "checkpoint", "id": "cp-hijau-prinsip",
     "question": "Menurut kimia hijau, tindakan yang paling utama adalah…",
     "choices": [
         {"id": "a", "text": "Mencegah limbah terbentuk sejak awal", "correct": True},
         {"id": "b", "text": "Mengolah limbah yang sudah terbentuk"},
         {"id": "c", "text": "Membuang limbah ke saluran air agar tidak menumpuk"},
     ],
     "explanation": "Prinsip pertama kimia hijau adalah pencegahan. Mengolah limbah tetap memerlukan energi dan biaya serta menyisakan risiko."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-hijau-penerapan",
     "prompt": "Kelompokkan tindakan berikut sebagai penerapan atau pelanggaran kimia hijau.",
     "buckets": [
         {"id": "terap", "label": "Penerapan"},
         {"id": "langgar", "label": "Pelanggaran"},
     ],
     "items": [
         {"id": "c1", "text": "Memakai wadah pakai ulang di kantin", "bucket": "terap"},
         {"id": "c2", "text": "Membakar sampah plastik di halaman sekolah", "bucket": "langgar"},
         {"id": "c3", "text": "Mengganti pelarut klorin dengan hidrogen peroksida", "bucket": "terap"},
         {"id": "c4", "text": "Membuang limbah praktikum ke saluran air tanpa pengolahan", "bucket": "langgar"},
         {"id": "c5", "text": "Memilah limbah praktikum sebelum dibuang", "bucket": "terap"},
         {"id": "c6", "text": "Memakai pelarut beracun karena lebih murah", "bucket": "langgar"},
     ],
     "feedback": {
         "correct": "Benar — penerapan mengurangi bahaya sejak awal, pelanggaran memindahkan bahaya ke lingkungan.",
         "wrong": "Tanyakan: apakah tindakan ini mengurangi zat berbahaya, atau justru menambah pencemaran?",
     }},
])

add_blocks(data, 2, [
    {"type": "scenario", "id": "sc-hijau-kantin",
     "title": "Sampah plastik kantin menumpuk",
     "start": "n1",
     "nodes": [
         {"id": "n1",
          "text": "Setiap hari kantin sekolah menghasilkan tumpukan sampah plastik. Kamu diminta mengusulkan solusi yang sesuai prinsip kimia hijau. Apa usulmu?",
          "choices": [
              {"text": "Mengganti kemasan sekali pakai dengan wadah pakai ulang", "next": "n2", "score": 2,
               "feedback": "Tepat: mencegah limbah sejak awal adalah prinsip pertama kimia hijau."},
              {"text": "Membakar sampah plastik di belakang kantin", "next": "n3", "score": 0,
               "feedback": "Pembakaran plastik menghasilkan asap beracun — memindahkan masalah ke udara, bukan menyelesaikannya."},
              {"text": "Menimbun sampah plastik di lubang tanah", "next": "n4", "score": 0,
               "feedback": "Penimbunan tidak menghilangkan limbah dan berisiko mencemari tanah serta air."},
          ]},
         {"id": "n2",
          "text": "Wadah pakai ulang diterima, tetapi sampah organik dari kantin masih menumpuk. Langkah berikutnya?",
          "choices": [
              {"text": "Ajukan pemilahan sampah organik untuk dikompos", "next": "n5", "score": 2,
               "feedback": "Lengkap: pengurangan sumber plus pengolahan organik menutup dua alur limbah sekaligus."},
              {"text": "Cukup sampai wadah pakai ulang saja", "next": "n6", "score": 0,
               "feedback": "Bagus untuk plastik, tetapi sampah organik tetap menjadi masalah yang tidak terselesaikan."},
          ]},
         {"id": "n3",
          "text": "Warga sekolah mengeluh sesak napas karena asap pembakaran. Apa tindakanmu?",
          "choices": [
              {"text": "Menghentikan pembakaran dan mengusulkan pemilahan sampah", "next": "n5", "score": 1,
               "feedback": "Koreksi yang baik. Memperbaiki kesalahan lebih bernilai daripada mempertahankannya."},
              {"text": "Melanjutkan pembakaran karena lebih murah dan cepat", "next": "n7", "score": 0,
               "feedback": "Biaya murah hari ini menjadi biaya kesehatan yang jauh lebih besar kemudian."},
          ]},
         {"id": "n4",
          "text": "Timbunan mulai berbau dan air tanah di dekatnya berbau tidak sedap. Langkahmu?",
          "choices": [
              {"text": "Menghentikan penimbunan dan mengusulkan pemilahan", "next": "n5", "score": 1,
               "feedback": "Tepat: hentikan sumber pencemaran, lalu kelola limbah dengan cara yang benar."},
              {"text": "Menimbun lebih dalam agar baunya tidak tercium", "next": "n7", "score": 0,
               "feedback": "Menutup bau tidak menghilangkan pencemaran; air tanah tetap terancam."},
          ]},
         {"id": "n5", "text": "Kantin kini memakai wadah pakai ulang, memilah sampah, dan mengompos sisa organik. Limbah plastik turun dan biaya kebersihan berkurang.", "end": True, "outcome": "good"},
         {"id": "n6", "text": "Sampah plastik berkurang, tetapi sampah organik masih membusuk di tempat terbuka dan mengundang lalat.", "end": True, "outcome": "neutral"},
         {"id": "n7", "text": "Masalah bergeser: asap atau air tanah tercemar, sementara warga sekitar menanggung dampaknya.", "end": True, "outcome": "bad"},
     ]},
])
save(path, data)

print('batch 2a: KIM 1, KIM 2, KIM 3 selesai')
