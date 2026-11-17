"""Fase 5.1 batch 6b — blok interaktif untuk INF 5, INF 6, INF 7, INF 8.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b6b.py`
lalu `php artisan gamecenter:materi-import`.
"""
import json
import io

BASE = 'database/seeders/data/sma-smk/fase-e/informatika/'


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


# ── INF 5 — Analisis Data ─────────────────────────────────────────────
path = 'inf-5-analisis-data.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "chart", "id": "ch-hobi", "kind": "bar",
     "title": "Survei hobi 40 siswa",
     "desc": "Grafik batang tiga kategori: membaca 15 siswa, olahraga 13 siswa, musik 12 siswa. Totalnya 40 siswa.",
     "data": [
         {"label": "Membaca", "value": 15},
         {"label": "Olahraga", "value": 13},
         {"label": "Musik", "value": 12},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Data", "definition": "Fakta mentah yang belum diolah, misalnya deretan angka hasil survei."},
        {"term": "Informasi", "definition": "Data yang sudah diolah sehingga bermakna dan dapat dipakai mengambil keputusan."},
        {"term": "Sel", "definition": "Kotak pada lembar kerja dengan alamat seperti B2 (kolom B, baris 2)."},
        {"term": "Rentang", "definition": "Sekumpulan sel berurutan yang ditulis dengan tanda titik dua, misalnya B2:B6."},
    ]},
    {"type": "checkpoint", "id": "cp-average",
     "question": "Fungsi =AVERAGE(B2:B6) menghasilkan…",
     "choices": [
         {"id": "a", "text": "Rata-rata nilai B2 sampai B6", "correct": True},
         {"id": "b", "text": "Jumlah nilai B2 sampai B6"},
         {"id": "c", "text": "Nilai terbesar B2 sampai B6"},
     ],
     "explanation": "AVERAGE menghitung rata-rata; SUM menjumlahkan, MAX mengambil nilai terbesar, dan COUNT menghitung banyak sel berisi angka."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-tahapan-analisis",
     "prompt": "Urutkan tahapan mengolah data menjadi kesimpulan.",
     "items": [
         {"id": "s1", "text": "Mengumpulkan data"},
         {"id": "s2", "text": "Membersihkan data"},
         {"id": "s3", "text": "Mengolah dan menganalisis"},
         {"id": "s4", "text": "Menyajikan dalam grafik"},
         {"id": "s5", "text": "Menarik kesimpulan"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar: kumpulkan, bersihkan, olah, sajikan, lalu simpulkan.",
         "wrong": "Data kotor harus dibersihkan sebelum diolah, kalau tidak kesimpulannya salah.",
     }},
    {"type": "checkpoint", "id": "cp-data-kotor",
     "question": "Sel berisi teks \"12\" (bukan angka) pada rentang yang dijumlahkan dengan =SUM akan…",
     "choices": [
         {"id": "a", "text": "Diabaikan oleh SUM sehingga jumlah menyimpang", "correct": True},
         {"id": "b", "text": "Tetap dihitung sebagai angka 12"},
         {"id": "c", "text": "Membuat lembar kerja error total"},
     ],
     "explanation": "SUM mengabaikan sel berisi teks, sehingga totalnya lebih kecil dari seharusnya. Inilah salah satu alasan pembersihan data wajib dilakukan."},
])

add_blocks(data, 2, [
    {"type": "categorize", "id": "cat-jenis-grafik",
     "prompt": "Kelompokkan jenis grafik sesuai kegunaan yang paling tepat.",
     "buckets": [
         {"id": "banding", "label": "Membandingkan kategori"},
         {"id": "tren", "label": "Menunjukkan tren waktu"},
         {"id": "proporsi", "label": "Proporsi terhadap keseluruhan"},
     ],
     "items": [
         {"id": "c1", "text": "Diagram batang", "bucket": "banding"},
         {"id": "c2", "text": "Diagram garis", "bucket": "tren"},
         {"id": "c3", "text": "Diagram lingkaran", "bucket": "proporsi"},
     ],
     "feedback": {
         "correct": "Benar — batang untuk kategori, garis untuk tren, lingkaran untuk proporsi.",
         "wrong": "Grafik yang salah membuat pembaca salah paham meskipun datanya benar.",
     }},
    {"type": "checkpoint", "id": "cp-rata-rata-latihan",
     "question": "Rata-rata data 4, 6, 8, 10, 12 adalah…",
     "choices": [
         {"id": "a", "text": "8", "correct": True},
         {"id": "b", "text": "10"},
         {"id": "c", "text": "40"},
     ],
     "explanation": "Jumlah data 40 dibagi banyak data 5 menghasilkan 8. Angka 40 adalah jumlahnya, bukan rata-ratanya."},
    {"type": "challenge", "id": "ch-analisis-data",
     "title": "Tantangan Kilat: Analisis Data",
     "time_limit": 80,
     "items": [
         {"question": "=MAX(B2:B6) mencari nilai …", "answer": "terbesar"},
         {"question": "=COUNT(B2:B6) menghitung sel berisi …", "answer": "angka"},
         {"question": "37,5% dari 40 siswa yang memilih membaca = … siswa", "answer": "15"},
         {"question": "Sel B2 berarti kolom B baris …", "answer": "2"},
         {"question": "Grafik untuk menunjukkan tren dari waktu ke waktu → diagram …", "answer": "garis"},
     ],
     "feedback": {
         "correct": "Tepat — fungsi dasar lembar kerja sudah kamu kuasai.",
         "wrong": "SUM menjumlah, AVERAGE merata-ratakan, MAX/MIN mengambil ekstrem, COUNT menghitung angka.",
     }},
])
save(path, data)

# ── INF 6 — Algoritma dan Pemrograman ─────────────────────────────────
path = 'inf-6-algoritma-pemrograman.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-algoritma-luas", "engine": "mermaid",
     "title": "Algoritma menghitung luas persegi panjang",
     "code": "flowchart TD\n  A[Mulai] --> B[Baca panjang]\n  B --> C[Baca lebar]\n  C --> D[luas = panjang x lebar]\n  D --> E[Cetak luas]\n  E --> F[Selesai]"},
    {"type": "glossary", "terms": [
        {"term": "Algoritma", "definition": "Urutan langkah yang jelas, berhingga, dan logis untuk menyelesaikan masalah."},
        {"term": "Variabel", "definition": "Penampung nilai yang dapat berubah selama program berjalan."},
        {"term": "Konstanta", "definition": "Penampung nilai yang nilainya tetap selama program berjalan."},
        {"term": "Mod", "definition": "Operator sisa pembagian, misalnya 7 mod 2 = 1."},
    ]},
    {"type": "checkpoint", "id": "cp-mod",
     "question": "Hasil dari 7 mod 2 adalah…",
     "choices": [
         {"id": "a", "text": "1", "correct": True},
         {"id": "b", "text": "3"},
         {"id": "c", "text": "2"},
     ],
     "explanation": "7 = 3 × 2 + 1, sehingga sisanya 1. Bilangan genap selalu memiliki x mod 2 = 0."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-urutan-keluaran",
     "prompt": "Urutkan keluaran program: i = 0; selama i < 3: cetak i; i = i + 1.",
     "items": [
         {"id": "s1", "text": "0"},
         {"id": "s2", "text": "1"},
         {"id": "s3", "text": "2"},
     ],
     "answer": ["s1", "s2", "s3"],
     "feedback": {
         "correct": "Benar — perulangan berhenti saat i = 3 karena kondisi i < 3 tidak lagi benar.",
         "wrong": "Periksa kondisinya: selama i < 3, jadi 0, 1, 2 yang tercetak, bukan 3.",
     }},
    {"type": "checkpoint", "id": "cp-bersarang",
     "question": "Pada keputusan bersarang: jika nilai ≥ 75 cetak \"A\" selain itu jika nilai ≥ 60 cetak \"B\". Nilai 80 menghasilkan…",
     "choices": [
         {"id": "a", "text": "\"A\" tanpa memeriksa kondisi kedua", "correct": True},
         {"id": "b", "text": "\"B\""},
         {"id": "c", "text": "\"A\" dan \"B\""},
     ],
     "explanation": "Kondisi pertama sudah benar, sehingga percabangan berhenti di sana dan kondisi kedua tidak diperiksa."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-lacak-program",
     "title": "Tantangan Kilat: Melacak Program",
     "time_limit": 90,
     "items": [
         {"question": "jumlah = 0; untuk i 1..5: jumlah = jumlah + i. Hasil = …", "answer": "15"},
         {"question": "n = 1 diulang 5 kali n = n x 2. Nilai akhir = …", "answer": "32"},
         {"question": "7 mod 2 = …", "answer": "1"},
         {"question": "Bilangan genap: x mod 2 = …", "answer": "0"},
         {"question": "10 mod 3 = …", "answer": "1"},
     ],
     "feedback": {
         "correct": "Tepat — tabel pelacakan satu baris per iterasi membuat hasilnya pasti.",
         "wrong": "Jangan menebak: catat nilai variabel setelah setiap iterasi.",
     }},
])
save(path, data)

# ── INF 7 — Dampak Sosial Informatika ────────────────────────────────
path = 'inf-7-dampak-sosial-informatika.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "timeline", "id": "tl-sejarah-komputasi",
     "title": "Tonggak sejarah komputasi",
     "items": [
         {"when": "1642", "title": "Pascaline", "text": "Blaise Pascal membuat kalkulator mekanis."},
         {"when": "1837", "title": "Mesin analitik", "text": "Charles Babbage merancang cikal bakal komputer."},
         {"when": "1843", "title": "Algoritma pertama", "text": "Ada Lovelace menulis algoritma untuk mesin analitik."},
         {"when": "1936", "title": "Mesin Turing", "text": "Alan Turing merumuskan dasar teori komputasi."},
         {"when": "1940-an", "title": "ENIAC", "text": "Salah satu komputer elektronik pertama berskala besar."},
         {"when": "1989", "title": "World Wide Web", "text": "Tim Berners-Lee mengembangkan WWW."},
     ]},
    {"type": "glossary", "terms": [
        {"term": "Mesin Turing", "definition": "Model teoretis komputasi yang dirumuskan Alan Turing, menjadi dasar ilmu komputer."},
        {"term": "ENIAC", "definition": "Salah satu komputer elektronik pertama berskala besar pada 1940-an."},
        {"term": "Revolusi Industri 4.0", "definition": "Era integrasi otomasi, pertukaran data, dan kecerdasan artifisial dalam produksi dan layanan."},
        {"term": "UU ITE", "definition": "Undang-undang yang mengatur informasi dan transaksi elektronik di Indonesia."},
    ]},
    {"type": "checkpoint", "id": "cp-tokoh",
     "question": "Tokoh yang mengembangkan World Wide Web adalah…",
     "choices": [
         {"id": "a", "text": "Tim Berners-Lee", "correct": True},
         {"id": "b", "text": "Alan Turing"},
         {"id": "c", "text": "Charles Babbage"},
     ],
     "explanation": "Tim Berners-Lee mengembangkan WWW; Turing merumuskan mesin Turing dan Babbage merancang mesin analitik."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-dampak-ekonomi",
     "prompt": "Kelompokkan dampak informatika pada ekonomi.",
     "buckets": [
         {"id": "positif", "label": "Dampak positif"},
         {"id": "negatif", "label": "Dampak negatif"},
     ],
     "items": [
         {"id": "c1", "text": "Lapangan kerja analis data", "bucket": "positif"},
         {"id": "c2", "text": "UMKM dapat memakai katalog daring", "bucket": "positif"},
         {"id": "c3", "text": "Penipuan daring", "bucket": "negatif"},
         {"id": "c4", "text": "Kesenjangan digital antar wilayah", "bucket": "negatif"},
     ],
     "feedback": {
         "correct": "Benar — informatika membuka pekerjaan baru tetapi juga membawa risiko dan kesenjangan.",
         "wrong": "Otomasi mengurangi pekerjaan rutin, tetapi keterampilan baru tetap dibutuhkan.",
     }},
    {"type": "checkpoint", "id": "cp-etika-data",
     "question": "Kamu menemukan data pribadi orang lain yang bocor. Langkah yang benar adalah…",
     "choices": [
         {"id": "a", "text": "Melaporkan dan tidak menyebarkannya", "correct": True},
         {"id": "b", "text": "Menyebarkan agar orang lain berhati-hati"},
         {"id": "c", "text": "Menyimpannya untuk dipakai sendiri"},
     ],
     "explanation": "Menyebarkan data pribadi tanpa izin melanggar perlindungan data pribadi dan berakibat hukum; langkah yang benar adalah melaporkan."},
])

add_blocks(data, 2, [
    {"type": "sort", "id": "srt-rancang-gagasan",
     "prompt": "Urutkan langkah merancang gagasan berbasis informatika.",
     "items": [
         {"id": "s1", "text": "Mengidentifikasi masalah nyata"},
         {"id": "s2", "text": "Menentukan solusi berbasis komputasi"},
         {"id": "s3", "text": "Merancang rencana pembuatan dan pengujian"},
         {"id": "s4", "text": "Menyajikan gagasan kepada pihak terkait"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar — gagasan yang baik selalu dimulai dari masalah nyata.",
         "wrong": "Tanpa masalah yang jelas, solusi komputasi mudah menjadi sekadar alat tanpa manfaat.",
     }},
    {"type": "challenge", "id": "ch-dampak-sosial",
     "title": "Tantangan Kilat: Dampak Sosial",
     "time_limit": 80,
     "items": [
         {"question": "Penemu kalkulator mekanis Pascaline → …", "answer": "Pascal"},
         {"question": "Perancang mesin analitik → …", "answer": "Babbage"},
         {"question": "Penulis algoritma pertama untuk mesin analitik → …", "answer": "Lovelace"},
         {"question": "Pengembang World Wide Web → …", "answer": "Berners-Lee"},
         {"question": "Undang-undang transaksi elektronik di Indonesia → UU …", "answer": "ITE"},
     ],
     "feedback": {
         "correct": "Tepat — sejarah dan aturan hukum sama pentingnya dengan keterampilan teknis.",
         "wrong": "Pascal (kalkulator), Babbage (mesin analitik), Lovelace (algoritma), Turing (teori), Berners-Lee (WWW).",
     }},
])
save(path, data)

# ── INF 8 — Praktika Lintas Bidang ───────────────────────────────────
path = 'inf-8-praktika-lintas-bidang.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-abstraksi", "engine": "mermaid",
     "title": "Abstraksi sistem peminjaman perpustakaan",
     "code": "flowchart LR\n  A[Sistem perpustakaan] --> B[Buku]\n  A --> C[Anggota]\n  A --> D[Transaksi peminjaman]\n  B --> E[Model yang dianalisis]\n  C --> E\n  D --> E"},
    {"type": "glossary", "terms": [
        {"term": "Abstraksi", "definition": "Menyederhanakan masalah dengan mengambil hanya bagian pentingnya."},
        {"term": "Kolaborasi digital", "definition": "Kerja tim memakai dokumen dan alat daring dengan riwayat perubahan terlacak."},
        {"term": "Prototipe", "definition": "Versi awal yang murah dan cepat untuk menguji gagasan sebelum dikembangkan penuh."},
        {"term": "Kasus uji", "definition": "Skenario pengujian beserta hasil yang diharapkan."},
    ]},
    {"type": "checkpoint", "id": "cp-abstraksi",
     "question": "Pada abstraksi sistem peminjaman perpustakaan, hal berikut TIDAK termasuk bagian abstraksi…",
     "choices": [
         {"id": "a", "text": "Warna rak buku", "correct": True},
         {"id": "b", "text": "Buku"},
         {"id": "c", "text": "Transaksi peminjaman"},
     ],
     "explanation": "Abstraksi hanya mengambil bagian penting: buku, anggota, dan transaksi. Warna rak atau merek komputer petugas tidak mempengaruhi model."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-artefak",
     "prompt": "Urutkan tahapan membangun artefak komputasi.",
     "items": [
         {"id": "s1", "text": "Mengenali dan mendefinisikan persoalan"},
         {"id": "s2", "text": "Mengembangkan model atau abstraksi"},
         {"id": "s3", "text": "Membuat artefak komputasi"},
         {"id": "s4", "text": "Menguji dan mendokumentasikan"},
         {"id": "s5", "text": "Mempresentasikan"},
     ],
     "answer": ["s1", "s2", "s3", "s4", "s5"],
     "feedback": {
         "correct": "Benar — langkah pertama selalu memahami persoalan, bukan langsung menulis kode.",
         "wrong": "Menulis kode sebelum persoalan dipahami membuat solusi melenceng dari kebutuhan pengguna.",
     }},
    {"type": "checkpoint", "id": "cp-hasil-uji",
     "question": "Hasil pengujian ternyata tidak sesuai harapan. Tindakan yang benar adalah…",
     "choices": [
         {"id": "a", "text": "Menelusuri penyebab, memperbaiki, lalu menguji ulang", "correct": True},
         {"id": "b", "text": "Mengubah harapan agar cocok dengan hasil"},
         {"id": "c", "text": "Menghapus kasus uji yang gagal"},
     ],
     "explanation": "Harapan dan kasus uji adalah acuan kebenaran. Mengubahnya hanya menyembunyikan kesalahan."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-praktika",
     "title": "Tantangan Kilat: Praktika Lintas Bidang",
     "time_limit": 80,
     "items": [
         {"question": "Kasus uji fitur login minimal: kata sandi benar, salah, dan kolom …", "answer": "kosong"},
         {"question": "Versi awal murah untuk menguji gagasan → …", "answer": "prototipe"},
         {"question": "Sebelum memakai gambar orang lain, periksa …", "answer": "lisensi"},
         {"question": "Hak cipta karya siswa dalam proyek sekolah dimiliki oleh …", "answer": "siswa"},
         {"question": "Memilih hanya data yang menguntungkan saat visualisasi akan merusak …", "answer": "kepercayaan"},
     ],
     "feedback": {
         "correct": "Tepat — uji, dokumentasikan, dan komunikasikan hasilnya dengan jujur.",
         "wrong": "Keterbatasan yang disebut jujur justru menunjukkan pemahaman mendalam.",
     }},
])
save(path, data)

print('batch 6b: INF 5, INF 6, INF 7, INF 8 selesai')