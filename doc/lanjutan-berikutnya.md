# Catatan Lanjutan Pengerjaan

Dokumen ini adalah titik lanjut (handoff) antar sesi. Perbarui setiap kali satu
buku/rilis selesai, lalu commit bersama rilisnya.

**Terakhir diperbarui:** 20 November 2026 · rilis **0.46.0** (commit `4353a22`,
sudah di-push ke `origin/main`).

---

## 1. Keadaan sekarang

| Item | Nilai |
|---|---|
| Versi aplikasi | 0.46.0 (dibaca dari heading pertama `gamecenter/changelog.md`) |
| Basis data | 118 bab · 341 materi · 3.480 soal · 354 asesmen · 190 mapel |
| Berkas materi | 114 JSON di `gamecenter/database/seeders/data/sma-smk/fase-e/` |
| Cakupan §5.3 | 115 dari 118 chapter (3.703 blok interaktif) |
| Tes | 160 lulus · 1 dilewati · 2.210 asersi |
| `deploy-check` | 13 lulus · 5 peringatan lokal · 0 gagal |
| Git | `main` bersih, sejajar `origin/main` |

Tiga chapter yang **sengaja** belum lengkap (contoh lama, di luar lingkup buku):
PAUD 1.1, TK 1.1, MTK 7.1.

### Buku Kelas X yang sudah tuntas

Matematika 8/8 · Informatika 8/9 · Bahasa Indonesia 5/6 · IPA 8/8 ·
Pancasila 4/4 · PAI 10/10 · Bahasa Inggris 6/6 · IPS 4/4 · PJOK 8/8 ·
Prakarya 14/14 · Sejarah 4/4 · Kepercayaan 8/8 · Projek IPAS 6/6 ·
**TJKT 6/6 (0.45.0)** · **Animasi 10/10 (0.46.0)**.

---

## 2. Langkah berikutnya: DKV (Desain Komunikasi Visual)

Berkas sumber:

- `data/kurmer/SMKSMA/BUKU AJAR/KELAS X/DKV-Sem-1.pdf`
- `data/kurmer/SMKSMA/BUKU AJAR/KELAS X/Dasar-Dasar-DKV-Semester-2.pdf`

Rencana: peta cakupan mencatat **7 bab** untuk mapel ini. Mulai dengan membaca
daftar isi kedua PDF, lalu petakan bab ke satu seri `DKV 1 … DKV n`
(gunakan penomoran berurutan lintas semester bila babnya bersambung).

Judul mapel untuk `SubjectSeeder`: **Dasar-Dasar Desain Komunikasi Visual**,
slug `dkv`, grup `Kejuruan`, jenjang `smk`, `grades => [10]`, ikon 🎨, warna
`rose`/`amber` (pilih yang belum dipakai).

### Setelah DKV

SMK Kelas X yang belum: Otomotif (BG + Sem 2 + Sem 1), Teknik Mesin,
Elektronika Sem 1, Konstruksi, Agriteknologi Sem 1, Pemrograman Dasar
(daftar isi belum dipetakan). Lalu Kelas XI (17 buku) dan XII (18 buku),
kemudian materi SD–MI.

---

## 3. Resep per bab (jalur yang sudah terbukti 4 buku terakhir)

Semua perintah dijalankan dari `C:\laragon\www\gamecenter` (root repo).

```bash
# PHP tidak ada di PATH — tambahkan dulu
export PATH="/c/laragon/bin/php/php-8.5.10-Win32-vs16-x64:$PATH"
export PYTHONIOENCODING=utf-8      # wajib: Python 3.14 + cp1252 gagal pada "→"

# 1. ekstrak teks PDF per bab (pymupdf)
python - <<'EOF'
import pymupdf, os, re
d = pymupdf.open('../data/kurmer/SMKSMA/BUKU AJAR/KELAS X/<BUKU>.pdf')
os.makedirs('out/<mapel>', exist_ok=True)
open('out/<mapel>/b1.txt','w',encoding='utf-8').write('\n'.join(d[i].get_text() for i in range(<awal>,<akhir>)))
EOF

# 2. tulis bab (satu skrip per bab) lalu impor
cd gamecenter
python ../tools/tulis-<mapel>-1.py
php artisan gamecenter:materi-import
php artisan gamecenter:materi-coverage | grep -E "<KODE>|dari"

# 3. verifikasi penuh
php artisan test
php artisan gamecenter:deploy-check
```

### Berkas pendukung yang harus dibuat per mapel baru

1. `tools/<mapel>_common.py` — pembungkus tipis, contohnya:

   ```python
   from pjok_common import *  # noqa: F401,F403
   from pjok_common import write_chapter as _write_chapter

   def write_chapter(chapter):
       _write_chapter(chapter, subject='<slug>', folder='<slug>', level='smk')
   ```

2. `tools/tulis-<mapel>-N.py` — satu bab per skrip, memakai dict `CH` dengan
   kunci: `code`, `slug`, `title`, `description`, `objectives`, `minutes`,
   `source`, `glossary`, `intro`, `concept`, `practice`, `facts` (14), `multi`
   (8), `pairs` (8), `steps` (5). Rujuk `tools/tulis-anim-7.py` sebagai contoh
   terlengkap.

3. Daftarkan mapel di `gamecenter/database/seeders/SubjectSeeder.php`, lalu:

   ```bash
   php artisan db:seed --class=SubjectSeeder --force
   ```

### Aturan isi yang tidak boleh dilanggar

- Satu buku = seluruh bab; tiap bab = **3 materi + 30 soal**
  (5 mudah / 10 sedang / 15 sulit), lima tipe soal interaktif.
- Minimum §5.3: ≥1 blok visual, ≥2 blok aktivitas, ≥1 skenario/tantangan,
  ≥1 glossary/flashcards, checkpoint sesuai kebutuhan; tidak ada isi tersembunyi.
- Tiap soal punya `explanation`; soal sulit tanpa `hint`.
- `concept['visual']` harus blok bertipe visual (diagram/chart/timeline/hotspots);
  blok `categorize` masuk ke `concept['activity']`.

### Jebakan yang pernah menggigit

- **Jumlah soal di tes harus dibaca dari DB setelah impor**, jangan ditebak.
  Pola: `Question::count()` di DB = angka tes + 60 (3 bab contoh lama).
  Angka terakhir: 114 bab / 3.420 soal di tes vs 118 bab / 3.480 soal di DB.
- Heredoc yang menulis file sambil `cd gamecenter` membuat path relatif
  (`../README.md`) salah — jalankan dari folder yang benar.
- Setelah menulis skrip Python, cek sintaks dengan menjalankannya; typo seperti
  tanda kutip tak tertutup atau baris tanpa koma sering lolos dari mata.

### Berkas yang diperbarui setiap rilis

1. `gamecenter/changelog.md` — heading `## [x.y.z] - YYYY-MM-DD HH:MM WIB`
   (sumber kebenaran versi) + baris "Terakhir diperbarui".
2. `README.md` — versi, jumlah berkas JSON, jumlah tes/asersi, daftar buku
   tuntas, bagian "Berikutnya".
3. `doc/peta-cakupan-materi.md` — baris mapel → ✅ SELESAI, persentase.
4. `gamecenter/tests/Feature/MateriImportCommandTest.php` — jumlah chapter,
   daftar kode bab, jumlah soal.
5. `gamecenter/tests/Feature/MateriCoverageCommandTest.php` — tes
   `test_<mapel>_chapters_meet_the_plan_minimums` dan
   `test_<mapel>_play_page_serves_three_materials_and_five_easy_questions`.
6. Dokumen ini.
7. `git add -A && git commit && git push origin main`.

Tidak perlu `npm run typecheck` / `npm run build` bila yang berubah hanya JSON
materi, seeder, dan tes PHP.
