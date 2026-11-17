"""Fase 5.1 batch 6a — blok interaktif untuk INF 2, INF 3, INF 4.

Jalankan dari folder gamecenter: `python ../tools/tambah-blok-fase5-b6a.py`
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


# ── INF 2 — Teknologi Informasi dan Komunikasi ────────────────────────
path = 'inf-2-tik.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-alur-integrasi", "engine": "mermaid",
     "title": "Alur integrasi data antar aplikasi perkantoran",
     "code": "flowchart LR\n  A[Hitung di pengolah angka] --> B[Pindahkan tabel]\n  B --> C[Tautkan: rujukan ke berkas sumber]\n  B --> D[Tanamkan: objek ikut tersimpan]\n  C --> E[Laporan di pengolah kata]\n  D --> E\n  E --> F[Grafik di presentasi]"},
    {"type": "glossary", "terms": [
        {"term": "Pengolah kata", "definition": "Aplikasi untuk menyusun dokumen teks seperti surat, laporan, dan makalah."},
        {"term": "Pengolah angka", "definition": "Aplikasi untuk menghitung dan menganalisis data berbentuk tabel, misalnya nilai dan anggaran."},
        {"term": "Tautkan (link)", "definition": "Objek hanya menyimpan rujukan ke berkas sumber, sehingga ikut berubah saat sumber diperbarui."},
        {"term": "Tanamkan (embed)", "definition": "Objek disimpan di dalam dokumen tujuan sehingga tetap utuh meski berkas sumber dihapus."},
    ]},
    {"type": "checkpoint", "id": "cp-link",
     "question": "Objek yang menyimpan rujukan ke berkas sumber sehingga ikut berubah saat sumber diperbarui disebut…",
     "choices": [
         {"id": "a", "text": "Tautan (link)", "correct": True},
         {"id": "b", "text": "Tanaman (embed)"},
         {"id": "c", "text": "Salin–tempel biasa"},
     ],
     "explanation": "Link menyimpan rujukan, embed menyimpan salinan objek di dalam dokumen, sedangkan salin–tempel biasa menghasilkan data mati yang tidak ikut berubah."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-mail-merge",
     "prompt": "Urutkan langkah membuat surat massal dengan mail merge.",
     "items": [
         {"id": "s1", "text": "Siapkan dokumen induk"},
         {"id": "s2", "text": "Siapkan sumber data penerima"},
         {"id": "s3", "text": "Sisipkan medan (field) ke dokumen"},
         {"id": "s4", "text": "Jalankan penggabungan lalu simpan hasil"},
     ],
     "answer": ["s1", "s2", "s3", "s4"],
     "feedback": {
         "correct": "Benar: induk, sumber data, medan, lalu gabungkan.",
         "wrong": "Medan hanya bisa disisipkan setelah dokumen induk dan sumber data siap.",
     }},
    {"type": "checkpoint", "id": "cp-pivot",
     "question": "Fitur pengolah angka yang merangkum data berukuran besar menjadi ringkasan adalah…",
     "choices": [
         {"id": "a", "text": "Pivot table", "correct": True},
         {"id": "b", "text": "Freeze panes"},
         {"id": "c", "text": "Data validation"},
     ],
     "explanation": "Freeze panes menjaga baris judul tetap terlihat dan data validation membatasi nilai yang boleh dimasukkan, bukan merangkum data."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-link-embed",
     "title": "Tantangan Kilat: Link atau Embed?",
     "time_limit": 70,
     "items": [
         {"question": "Ikut berubah saat berkas sumber diperbarui → …", "answer": "link"},
         {"question": "Dokumen tetap utuh walau sumber dihapus → …", "answer": "embed"},
         {"question": "Ukuran dokumen tujuan lebih kecil → …", "answer": "link"},
         {"question": "Bergantung pada keberadaan berkas sumber → …", "answer": "link"},
         {"question": "Objek disimpan di dalam dokumen tujuan → …", "answer": "embed"},
     ],
     "feedback": {
         "correct": "Tepat — link untuk data yang terus berubah, embed untuk dokumen yang harus utuh.",
         "wrong": "Link = rujukan (kecil, ikut berubah, bergantung sumber); embed = salinan tersimpan (lebih besar, mandiri).",
     }},
])
save(path, data)

# ── INF 3 — Sistem Komputer ───────────────────────────────────────────
path = 'inf-3-sistem-komputer.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-sistem-komputer", "engine": "mermaid",
     "title": "Empat kelompok komponen sistem komputer",
     "code": "flowchart LR\n  A[Masukan: keyboard, mouse, scanner] --> B[CPU: ALU, control unit, register]\n  B --> C[Keluaran: monitor, printer, speaker]\n  B <--> D[Penyimpanan: RAM, hard disk, SSD]"},
    {"type": "glossary", "terms": [
        {"term": "ALU", "definition": "Bagian CPU yang melakukan operasi aritmetika dan logika."},
        {"term": "Control unit", "definition": "Bagian CPU yang mengatur urutan pengambilan dan pelaksanaan instruksi."},
        {"term": "Register", "definition": "Penyimpan kecil berkecepatan sangat tinggi di dalam CPU."},
        {"term": "RAM", "definition": "Memori sementara yang isinya hilang saat daya putus."},
        {"term": "Cache", "definition": "Penyimpan data yang sering dipakai agar tidak perlu diambil jauh dari RAM."},
    ]},
    {"type": "checkpoint", "id": "cp-ram-volatile",
     "question": "Pekerjaan yang belum disimpan hilang saat listrik padam karena datanya masih berada di…",
     "choices": [
         {"id": "a", "text": "RAM", "correct": True},
         {"id": "b", "text": "Hard disk"},
         {"id": "c", "text": "SSD"},
     ],
     "explanation": "RAM bersifat volatile: isinya hilang saat daya putus. Hard disk dan SSD bersifat permanen sehingga data tersimpan meski daya mati."},
])

add_blocks(data, 1, [
    {"type": "sort", "id": "srt-boot",
     "prompt": "Urutkan proses menyalakan komputer sampai siap dipakai.",
     "items": [
         {"id": "s1", "text": "POST memeriksa perangkat keras"},
         {"id": "s2", "text": "Bootloader mencari dan memuat sistem operasi"},
         {"id": "s3", "text": "Sistem operasi berjalan dan siap dipakai"},
     ],
     "answer": ["s1", "s2", "s3"],
     "feedback": {
         "correct": "Benar: POST, bootloader, lalu sistem operasi.",
         "wrong": "Firmware berjalan lebih dulu karena sistem operasi belum dimuat.",
     }},
    {"type": "checkpoint", "id": "cp-siklus-cpu",
     "question": "Urutan siklus kerja CPU adalah…",
     "choices": [
         {"id": "a", "text": "fetch → decode → execute", "correct": True},
         {"id": "b", "text": "decode → fetch → execute"},
         {"id": "c", "text": "execute → decode → fetch"},
     ],
     "explanation": "CPU mengambil instruksi (fetch), menerjemahkannya (decode), lalu melaksanakannya (execute) — berulang miliaran kali per detik."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-sistem-komputer",
     "title": "Tantangan Kilat: Sistem Komputer",
     "time_limit": 70,
     "items": [
         {"question": "Mengambil instruksi dari memori → tahap …", "answer": "fetch"},
         {"question": "Menerjemahkan instruksi → tahap …", "answer": "decode"},
         {"question": "Melaksanakan instruksi → tahap …", "answer": "execute"},
         {"question": "Memeriksa perangkat keras saat komputer menyala → …", "answer": "POST"},
         {"question": "Menjadwalkan pemakaian CPU antarprogram → manajemen …", "answer": "proses"},
     ],
     "feedback": {
         "correct": "Tepat — fetch, decode, execute berulang sangat cepat.",
         "wrong": "Ingat urutannya: ambil dulu, terjemahkan, baru laksanakan.",
     }},
])
save(path, data)

# ── INF 4 — Jaringan Komputer dan Internet ────────────────────────────
path = 'inf-4-jaringan-komputer-internet.json'
data = load(path)

add_blocks(data, 0, [
    {"type": "diagram", "id": "dg-jaringan", "engine": "mermaid",
     "title": "Perangkat penghubung dari LAN ke internet",
     "code": "flowchart LR\n  A[Komputer di LAN] --> B[Switch]\n  C[Laptop nirkabel] --> D[Access point]\n  D --> B\n  B --> E[Router]\n  E --> F[Modem]\n  F --> G[Internet]"},
    {"type": "glossary", "terms": [
        {"term": "LAN", "definition": "Jaringan yang menghubungkan perangkat dalam wilayah terbatas seperti satu gedung atau sekolah."},
        {"term": "Switch", "definition": "Menghubungkan perangkat dalam satu jaringan lokal."},
        {"term": "Router", "definition": "Meneruskan paket antar jaringan berbeda, termasuk ke internet."},
        {"term": "Access point", "definition": "Memancarkan sinyal nirkabel agar perangkat dapat terhubung tanpa kabel."},
        {"term": "Alamat IP", "definition": "Identitas numerik setiap perangkat di jaringan, misalnya 192.168.1.1 pada IPv4."},
    ]},
    {"type": "checkpoint", "id": "cp-router",
     "question": "Perangkat yang meneruskan paket antar jaringan berbeda, termasuk ke internet, adalah…",
     "choices": [
         {"id": "a", "text": "Router", "correct": True},
         {"id": "b", "text": "Switch"},
         {"id": "c", "text": "Access point"},
     ],
     "explanation": "Switch hanya menghubungkan perangkat dalam satu jaringan lokal, sedangkan router menghubungkan jaringan lokal dengan jaringan lain."},
])

add_blocks(data, 1, [
    {"type": "categorize", "id": "cat-kabel-nirkabel",
     "prompt": "Kelompokkan media transmisi berikut.",
     "buckets": [
         {"id": "kabel", "label": "Berbasis kabel"},
         {"id": "nirkabel", "label": "Nirkabel"},
     ],
     "items": [
         {"id": "c1", "text": "Kabel UTP (IEEE 802.3)", "bucket": "kabel"},
         {"id": "c2", "text": "Serat optik", "bucket": "kabel"},
         {"id": "c3", "text": "Wi-Fi (IEEE 802.11)", "bucket": "nirkabel"},
         {"id": "c4", "text": "Bluetooth", "bucket": "nirkabel"},
     ],
     "feedback": {
         "correct": "Benar — UTP dan serat optik memakai media fisik, Wi-Fi dan Bluetooth memakai gelombang elektromagnetik.",
         "wrong": "Media fisik (kabel) memakai tembaga atau cahaya; nirkabel memancarkan gelombang elektromagnetik.",
     }},
    {"type": "checkpoint", "id": "cp-bandwidth",
     "question": "Bandwidth menyatakan…",
     "choices": [
         {"id": "a", "text": "Banyaknya data yang dapat dikirim per satuan waktu", "correct": True},
         {"id": "b", "text": "Jarak jangkauan sinyal nirkabel"},
         {"id": "c", "text": "Banyak perangkat yang dapat terhubung"},
     ],
     "explanation": "Bandwidth diukur dalam bit per detik: semakin besar, semakin banyak data yang dapat lewat pada waktu yang sama."},
])

add_blocks(data, 2, [
    {"type": "challenge", "id": "ch-keamanan-data",
     "title": "Tantangan Kilat: Proteksi Data",
     "time_limit": 80,
     "items": [
         {"question": "Enkripsi dengan satu kunci untuk mengunci dan membuka → …", "answer": "simetris"},
         {"question": "Enkripsi dengan pasangan kunci publik dan privat → …", "answer": "asimetris"},
         {"question": "Protokol situs yang lalu lintasnya terenkripsi → …", "answer": "HTTPS"},
         {"question": "Jaringan virtual untuk mengamankan Wi-Fi publik → …", "answer": "VPN"},
         {"question": "Langkah keamanan selain kata sandi saat masuk akun → verifikasi … langkah", "answer": "dua"},
     ],
     "feedback": {
         "correct": "Tepat — kata sandi kuat, verifikasi dua langkah, dan enkripsi saling melengkapi.",
         "wrong": "Enkripsi hanya sekuat pengelolaan kuncinya, jadi kirim kunci lewat saluran berbeda.",
     }},
])
save(path, data)

print('batch 6a: INF 2, INF 3, INF 4 selesai')