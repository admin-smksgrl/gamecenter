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


# ── PAN 1: lini masa, glosarium, 2 checkpoint ───────────────────────────
path = 'pancasila/pan-1-pancasila-pemersatu-bangsa.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "heading", "text": "Jejak perumusan Pancasila", "level": 3},
    {"type": "timeline", "id": "tl-perumusan-pancasila",
     "title": "Empat momen perumusan Pancasila",
     "items": [
         {"when": "29 Mei 1945", "title": "Usulan Mr. Soepomo",
          "text": "Dalam sidang BPUPKI, Soepomo mengusulkan dasar negara yang bersifat integralistik."},
         {"when": "1 Juni 1945", "title": "Pidato Ir. Soekarno",
          "text": "Soekarno memperkenalkan lima sila yang kemudian dikenal sebagai Pancasila."},
         {"when": "22 Juni 1945", "title": "Piagam Jakarta",
          "text": "Panitia Sembilan menyusun rumusan dasar negara yang memuat tujuh kata pada sila pertama."},
         {"when": "18 Agustus 1945", "title": "Pengesahan UUD 1945",
          "text": "Tujuh kata dihapus demi persatuan, lalu Pancasila disahkan bersama UUD 1945 oleh PPKI."},
     ]},
    {"type": "glossary", "terms": [
        {"term": "BPUPKI", "definition": "Badan Penyelidik Usaha-Usaha Persiapan Kemerdekaan Indonesia yang menyidangkan dasar negara."},
        {"term": "Piagam Jakarta", "definition": "Rumusan dasar negara hasil Panitia Sembilan, 22 Juni 1945."},
        {"term": "Musyawarah", "definition": "Cara mengambil keputusan bersama dengan saling mendengar hingga mencapai kesepakatan."},
        {"term": "Integralistik", "definition": "Pandangan bahwa negara dan rakyat merupakan satu kesatuan yang tidak terpisah."},
    ]},
    {"type": "checkpoint", "id": "cp-pan1-pendiri",
     "question": "Mengapa tujuh kata pada sila pertama Piagam Jakarta diubah sebelum Pancasila disahkan?",
     "choices": [
         {"id": "a", "text": "Agar menjaga persatuan seluruh wilayah Indonesia yang majemuk", "correct": True},
         {"id": "b", "text": "Karena rumusan sebelumnya tidak dibahas dalam sidang"},
         {"id": "c", "text": "Supaya teks Pancasila menjadi lebih pendek"},
     ],
     "explanation": "Perubahan itu hasil musyawarah para pendiri untuk merangkul seluruh golongan. Persatuan diutamakan di atas kepentingan satu kelompok, sesuai sila ketiga."},
])

add_blocks(data, 2, [
    {"type": "heading", "text": "Cek pemahaman", "level": 3},
    {"type": "checkpoint", "id": "cp-pan1-tantangan",
     "question": "Berita bohong yang menyudutkan satu kelompok paling tepat dihadapi dengan cara…",
     "choices": [
         {"id": "a", "text": "Membalas dengan berita bohong lain yang lebih keras"},
         {"id": "b", "text": "Memverifikasi sumber lalu mengajak diskusi dengan santun", "correct": True},
         {"id": "c", "text": "Menyebarkan ke semua grup agar cepat ramai"},
     ],
     "explanation": "Sila kedua dan ketiga menuntut sikap adil dan menjaga persatuan. Verifikasi sumber mencegah perpecahan, sedangkan membalas hoaks justru memperluas konflik."},
])
save(path, data)

# ── MA 1.1: grafik, glosarium, checkpoint, urutkan ─────────────────────
path = 'matematika/ma-1.1-eksponen.json'
data = load(path)

add_blocks(data, 1, [
    {"type": "chart", "id": "ch-2pangkat-x", "kind": "line",
     "title": "Pertumbuhan 2^x",
     "desc": "Grafik garis yang naik makin cepat: 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16.",
     "data": [
         {"label": "0", "value": 1},
         {"label": "1", "value": 2},
         {"label": "2", "value": 4},
         {"label": "3", "value": 8},
         {"label": "4", "value": 16},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Basis", "definition": "Bilangan yang dipangkatkan, misalnya 2 pada 2³."},
        {"term": "Eksponen", "definition": "Pangkat yang menunjukkan berapa kali basis dikalikan dirinya sendiri."},
        {"term": "Pangkat nol", "definition": "Setiap bilangan bukan nol berpangkat nol hasilnya 1 (a⁰ = 1)."},
        {"term": "Pangkat negatif", "definition": "a⁻ⁿ = 1/aⁿ, sehingga pangkat negatif berarti kebalikan."},
    ]},
    {"type": "checkpoint", "id": "cp-eksponen-sifat",
     "question": "Bentuk sederhana dari a⁵ × a² adalah…",
     "choices": [
         {"id": "a", "text": "a⁷", "correct": True},
         {"id": "b", "text": "a¹⁰"},
         {"id": "c", "text": "2a⁷"},
     ],
     "explanation": "Pada perkalian dengan basis sama, pangkat dijumlahkan: a⁵ × a² = a⁵⁺² = a⁷. Basis tidak ikut dikalikan."},
    {"type": "sort", "id": "srt-eksponen-langkah",
     "prompt": "Urutkan langkah menyederhanakan (2³ × 2²) ÷ 2⁴.",
     "items": [
         {"id": "s1", "text": "Tulis ulang: (2³ × 2²) ÷ 2⁴"},
         {"id": "s2", "text": "Jumlahkan pangkat pembilang: 2⁵ ÷ 2⁴"},
         {"id": "s3", "text": "Kurangkan pangkat: 2⁵⁻⁴"},
         {"id": "s4", "text": "Hasil akhir: 2¹ = 2"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Urutan benar: kalikan dulu (pangkat dijumlahkan), lalu bagi (pangkat dikurangkan).",
         "wrong": "Kerjakan bertahap: sederhanakan pembilang dulu, baru bagi dengan penyebut.",
     }},
])
save(path, data)

# ── MA 6.1: glosarium, 2 checkpoint, tantangan ─────────────────────────
path = 'matematika/ma-6.1-karakteristik-fungsi-kuadrat.json'
data = load(path)

add_blocks(data, 1, [
    {"type": "glossary", "terms": [
        {"term": "Titik puncak", "definition": "Titik tertinggi atau terendah parabola, terletak pada sumbu simetri."},
        {"term": "Sumbu simetri", "definition": "Garis vertikal x = −b/2a yang membagi parabola menjadi dua bagian sama."},
        {"term": "Diskriminan", "definition": "Nilai D = b² − 4ac yang menentukan jumlah titik potong dengan sumbu-x."},
        {"term": "Akar-akar", "definition": "Nilai x saat y = 0, yaitu titik tempat parabola memotong sumbu-x."},
    ]},
    {"type": "checkpoint", "id": "cp-kuadrat-puncak",
     "question": "Parabola y = x² − 4x + 3 punya sumbu simetri di…",
     "choices": [
         {"id": "a", "text": "x = 2", "correct": True},
         {"id": "b", "text": "x = −2"},
         {"id": "c", "text": "x = 4"},
     ],
     "explanation": "Sumbu simetri x = −b/2a = −(−4)/(2·1) = 2. Substitusi x = 2 memberi titik puncak (2, −1)."},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-kuadrat-diskriminan",
     "question": "Jika diskriminan sebuah fungsi kuadrat bernilai negatif, grafiknya…",
     "choices": [
         {"id": "a", "text": "Tidak memotong sumbu-x", "correct": True},
         {"id": "b", "text": "Memotong sumbu-x di dua titik"},
         {"id": "c", "text": "Menyinggung sumbu-x di satu titik"},
     ],
     "explanation": "D < 0 berarti persamaan kuadrat tidak punya akar real, sehingga parabola tidak menyentuh sumbu-x sama sekali."},
    {"type": "challenge", "id": "ch-kuadrat-cepat",
     "title": "Tantangan Kilat: Karakteristik Parabola",
     "time_limit": 90,
     "items": [
         {"question": "y = x² − 6x + 5. Sumbu simetri x = …", "answer": "3"},
         {"question": "y = x² − 6x + 5. Nilai diskriminan D = …", "answer": "16"},
         {"question": "y = x² − 4x + 3 memotong sumbu-x di x = 1 dan x = …", "answer": "3"},
         {"question": "Parabola y = −x² + 2x terbuka ke arah …", "answer": "bawah"},
         {"question": "y = x² − 4x + 3. Nilai minimum y = …", "answer": "-1"},
     ],
     "feedback": {
         "correct": "Semua tepat — ciri parabola sudah terbaca cepat.",
         "wrong": "Ingat: x puncak = −b/2a, D = b² − 4ac, dan tanda a menentukan arah bukaan.",
     }},
])
save(path, data)

# ── INF 1: diagram pilar + tantangan ───────────────────────────────────
path = 'informatika/inf-1-berpikir-komputasional.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-pilar-berpikir", "engine": "mermaid",
     "title": "Alur berpikir komputasional",
     "code": "flowchart TD\n  A[Masalah] --> B[Dekomposisi]\n  B --> C[Pengenalan pola]\n  C --> D[Abstraksi]\n  D --> E[Algoritma]\n  E --> F[Solusi]"},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-inf-istilah",
     "title": "Tantangan Kilat: Istilah Berpikir Komputasional",
     "time_limit": 75,
     "items": [
         {"question": "Memecah masalah besar menjadi bagian kecil disebut …", "answer": "dekomposisi"},
         {"question": "Mengambil ciri penting dan mengabaikan detail disebut …", "answer": "abstraksi"},
         {"question": "Langkah berurutan yang pasti selesai disebut …", "answer": "algoritma"},
         {"question": "Struktur data yang memakai aturan terakhir masuk pertama keluar adalah …", "answer": "stack"},
         {"question": "Struktur data yang memakai aturan pertama masuk pertama keluar adalah …", "answer": "queue"},
     ],
     "feedback": {
         "correct": "Semua tepat — istilah dasar sudah melekat.",
         "wrong": "Ulangi bagian Empat Pilar: dekomposisi, pola, abstraksi, algoritma.",
     }},
])
save(path, data)

# ── FIS 1: glosarium, 2 checkpoint, tantangan ──────────────────────────
path = 'fisika/fis-1-pengukuran-kerja-ilmiah.json'
data = load(path)

add_blocks(data, 1, [
    {"type": "glossary", "terms": [
        {"term": "Besaran pokok", "definition": "Besaran yang tidak diturunkan dari besaran lain, misalnya panjang, massa, dan waktu."},
        {"term": "Besaran turunan", "definition": "Besaran yang disusun dari besaran pokok, misalnya kecepatan dan gaya."},
        {"term": "Notasi ilmiah", "definition": "Penulisan angka sebagai a × 10ⁿ dengan 1 ≤ a < 10."},
        {"term": "Ketidakpastian mutlak", "definition": "Setengah dari nilai skala terkecil alat ukur, ditulis ±."},
    ]},
    {"type": "checkpoint", "id": "cp-besaran-turunan",
     "question": "Manakah yang termasuk besaran turunan?",
     "choices": [
         {"id": "a", "text": "Kecepatan", "correct": True},
         {"id": "b", "text": "Massa"},
         {"id": "c", "text": "Waktu"},
     ],
     "explanation": "Kecepatan disusun dari panjang dan waktu (m/s), jadi termasuk turunan. Massa dan waktu adalah besaran pokok."},
])

add_blocks(data, 2, [
    {"type": "checkpoint", "id": "cp-ketidakpastian",
     "question": "Hasil pengukuran 12,50 cm dengan ketidakpastian ±0,05 cm paling tepat dilaporkan sebagai…",
     "choices": [
         {"id": "a", "text": "(12,50 ± 0,05) cm", "correct": True},
         {"id": "b", "text": "12,5 cm saja"},
         {"id": "c", "text": "(12,50 ± 0,5) cm"},
     ],
     "explanation": "Ketidakpastian ditulis dengan jumlah desimal yang sama dengan hasil ukur. Menuliskannya menjaga kejujuran tingkat ketelitian alat."},
    {"type": "challenge", "id": "ch-fis-satuan",
     "title": "Tantangan Kilat: Satuan & Alat Ukur",
     "time_limit": 75,
     "items": [
         {"question": "Satuan SI untuk panjang adalah …", "answer": "meter"},
         {"question": "Satuan SI untuk massa adalah …", "answer": "kilogram"},
         {"question": "Alat ukur diameter dalam silinder adalah …", "answer": "jangka sorong"},
         {"question": "Ketelitian mikrometer sekrup adalah … mm", "answer": "0,01"},
         {"question": "Angka 0,00250 memiliki … angka penting", "answer": "3"},
     ],
     "feedback": {
         "correct": "Semua tepat — satuan dan alat ukur sudah dikenali.",
         "wrong": "Periksa tabel besaran pokok dan skala terkecil tiap alat ukur.",
     }},
])
save(path, data)

print('konten Fase 5.1 (batch 1) ditambahkan')
