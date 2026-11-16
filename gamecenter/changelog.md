# Changelog

Semua perubahan penting pada **Ruang Belajar — Game Center** dicatat di file
ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/)
dengan tambahan timestamp rilis. Aplikasi membaca heading rilis pertama yang
berisi versi semver dan menampilkannya di footer (`Ruang belajar v.<versi>`),
sehingga file ini adalah satu-satunya sumber kebenaran versi sistem.
Timestamp memakai waktu lokal server (WIB, UTC+7). Setiap heading rilis dan
bagian verifikasi mencantumkan tanggal + jam.

**Terakhir diperbarui:** 2026-11-16 20:40 WIB (rilis 0.18.0).

## [0.18.0] - 2026-11-16 20:40 WIB

**Navigasi jenjang: PAUD, TK, SD-MI, SMP-MTs, SMA-SMK.**

### Ditambah
- **Jenjang SD-MI** (`sd`) beserta enam rombel (Kelas 1–6, Fase A–C) dan
  delapan mata pelajaran wajib. Materi belum ditulis; kartu mapel berlabel
  "Segera" dan halaman menampilkan pemberitahuan bahwa materi sedang disiapkan.
- **`resources/js/lib/level-groups.ts`** — peta pengelompokan jenjang untuk
  navigasi atas.
- **Pemberitahuan jenjang kosong** pada katalog materi.

### Diubah
- **Topbar "Jenjang"** kini berisi lima pilihan: PAUD, TK, SD-MI, SMP-MTs,
  SMA-SMK. Sebelumnya lima baris terpisah termasuk SMA dan SMK sendiri-sendiri.
- **SMA dan SMK digabung** menjadi satu pilihan `SMA-SMK`. Daftar kelas berisi
  enam entri dengan keterangan asal jenjang (`Kelas 10 / SMA`,
  `Kelas 10 / SMK`, …).
- **Nama jenjang** di basis data: `SD-MI` dan `SMP-MTs` (sebelumnya `SMP`).
- **Ringkasan katalog** (mapel, bab, soal) mengikuti kelas yang dibuka,
  bukan total seluruh situs. Sebelumnya jenjang tanpa materi menampilkan
  "1.500 soal" milik jenjang lain.

### Catatan teknis
- Penggabungan hanya di lapisan tampilan; basis data tetap menyimpan jenjang
  `sma` dan `smk` terpisah agar rombel dan mapel kejuruan tidak tercampur.
- Urutan jenjang baru: PAUD 1, TK 2, SD 3, SMP 4, SMA 5, SMK 6.
- Total jenjang 6 baris, rombel 18, mata pelajaran 181.

### Verifikasi
- Menu topbar: `PAUD (1 kelas)`, `TK (2 kelas)`, `SD-MI (6 kelas)`,
  `SMP-MTs (3 kelas)`, `SMA-SMK (6 kelas · SMA & SMK)` — satu entri, bukan dua.
- Daftar kelas `SMA-SMK`: `Kelas 10 / SMA`, `Kelas 11 / SMA`, `Kelas 12 / SMA`,
  `Kelas 10 / SMK`, `Kelas 11 / SMK`, `Kelas 12 / SMK`.
- Halaman SD-MI: 8 mapel, 0 bab, 0 soal, pemberitahuan "sedang disiapkan".
- `php artisan test` → **96 passed** (872 assertions).

## [0.17.0] - 2026-11-16 20:05 WIB

**Satu tema untuk semua jenjang: merah `#e60012` di atas putih.**

### Diubah
- **Palet per jenjang dihapus.** Sebelumnya PAUD rose `#e11d48`, TK amber
  `#d97706`, SMP indigo `#4f46e5`, dan SMA/SMK biru `#2563eb`. Kini kelima
  jenjang memakai merah `#e60012` yang sama.
- **Satu heksa merah di seluruh sistem.** `[data-level-theme]` menimpa token
  dengan nilai identik dengan akar dokumen, sehingga halaman masuk, beranda,
  permainan, panduan, dan panel admin memakai merah yang sama.
- **Latar putih bersih.** `--color-canvas` dan `--color-surface` menjadi
  `#ffffff`, dengan garis pemisah `#e9d3d3` dan bayangan tipis agar kartu tetap
  terbaca.
- **Halaman bawaan Laravel (`welcome.blade.php`)** yang masih memakai merah
  `#f53003`, `#FF4433`, dan `#F3BEC7` diseragamkan menjadi `#e60012`,
  `#ff3945`, dan `#ffebec`.
- **Data jenjang** di `EducationLevelSeeder` diset `theme = 'default'` dan
  dijalankan ulang, sehingga tidak ada lagi jenjang yang memakai palet lain.
- **`level-theme.ts`** memakai aksen `#e60012` dan tint `#ffebec` untuk semua
  entri.

### Catatan teknis
- Blok CSS `[data-level-theme='playful'|'adventure'|'scifi'|'professional']`
  beserta varian gelapnya dihapus, diganti satu blok `[data-level-theme]`
  yang menimpa token merah dengan nilai akar.
- Aturan tipografi `.display` per jenjang ikut dihapus; tipografi display kini
  seragam.
- `--level-motion` tidak lagi dipakai sehingga animasi orb menjadi statis.

### Verifikasi
- Aksen kelima jenjang (PAUD, TK, SMP, SMA, SMK) diukur di peramban:
  **satu nilai unik**, `#e60012`; tint `#ffebec`; `shadow-fab`
  `0 8px 20px -8px #e600128c`; `theme-color` `#e60012`.
- Latar halaman `rgb(255, 255, 255)` pada semua jenjang.
- Pemindaian warna DOM di beranda, progres, panduan, keanggotaan, halaman
  masuk, dan halaman daftar: hanya **merah + putih + netral**.
- `php artisan test` → **96 passed** (865 assertions).

## [0.16.0] - 2026-11-16 19:05 WIB

**Tema jenjang diselaraskan: satu jenjang = satu warna. SMA dan SMK kini biru.**

### Diubah
- **SMA dan SMK memakai aksen biru** `#2563eb` (gelap `#60a5fa`), menggantikan
  teal. Kedua jenjang memakai identitas yang sama, sesuai keputusan produk.
- **Bayangan mengikuti jenjang.** `--shadow-lift` dan `--shadow-fab` sekarang
  diturunkan dari `--level-glow` / `--level-glow-strong`, bukan merah tetap
  `#b8000f` / `#e60012`. Sebelumnya bayangan tetap merah di semua jenjang.
- **Kartu mapel tidak lagi berwarna-warni.** `subjectTheme()` memakai tint
  jenjang, sehingga mapel tidak lagi memunculkan biru/teal/amber sendiri di
  dalam jenjang yang aksennya berbeda.
- **Status di dalam permainan memakai aksen jenjang**: benar, salah, uraian,
  lencana kelulusan, navigator soal, dan ringkasan hasil dibedakan lewat aksen
  solid, tint aksen, dan netral — bukan hijau/merah/amber.
- **Toast** memakai aksen jenjang untuk nada sukses dan netral untuk peringatan.
- **Bilah peramban (`theme-color`)** mengikuti aksen jenjang dan ikut berubah
  saat jenjang diganti.
- **Diagram Mermaid di `/panduan`** memakai aksen jenjang.
- **Halaman tanpa `levelTheme`** (mis. `/panduan`) mewarisi jenjang pengguna,
  bukan warna dasar merah.
- **Halaman jelajah materi** membuka jenjang milik pengguna lebih dulu, jadi
  siswa SMA langsung melihat biru, bukan tema PAUD.

### Catatan teknis
- Token baru: `--level-accent-rgb`, `--level-glow`, `--level-glow-strong`, dan
  `--shadow-lift` / `--shadow-fab` per jenjang (termasuk varian gelap).
- `--shadow-lift` dan `--shadow-fab` di `@theme` ditulis ulang memakai
  `var(--level-glow*)`; Tailwind menginline nilai itu sehingga resolve-nya
  terjadi saat runtime di subtree `data-level-theme`.
- `subjectTheme(color)` tetap menerima argumen lama agar pemanggil tidak perlu
  diubah, tetapi warna mapel sengaja diabaikan.

### Verifikasi
- Pemindaian warna DOM di halaman beranda, progres, panduan, keanggotaan, dan
  permainan (siswa SMA): hanya **biru + netral**, tanpa merah/hijau/amber/teal.
- Tema tiap jenjang: PAUD `#e11d48`, TK `#d97706`, SMP `#4f46e5`, SMA/SMK
  `#2563eb`; bayangan dan `theme-color` ikut nilai yang sama.
- Mode gelap: aksen `#60a5fa`, bayangan `#60a5fa57`/`#60a5fa75`.
- `php artisan test` → **96 passed** (865 assertions).

## [0.15.0] - 2026-11-16 17:20 WIB

**Materi SMA/SMK — Tahap 1d: Pendidikan Pancasila X (4/4 bab) dan PAI Budi Pekerti X (10/10 bab).**

### Ditambahkan
- **Pendidikan Pancasila Kelas X — seluruh isi buku (4 bab)**:
  - PAN 1 Pancasila sebagai Pemersatu Bangsa (4 materi = 4 unit)
  - PAN 2 Membangun Budaya Taat Hukum (4 materi = 7 unit)
  - PAN 3 Mengelola Kebinekaan sebagai Modal Sosial Pembangunan Nasional
    (3 materi = 5 unit)
  - PAN 4 Menjadi Warga Negara yang Baik (3 materi = 3 unit)
- **PAI dan Budi Pekerti Kelas X — seluruh isi buku (10 bab)**:
  kompetisi dalam kebaikan dan etos kerja, syu'abul iman, berfoya-foya
  riya' sum'ah takabur hasad, asuransi/bank/koperasi syariah, meneladani
  ulama penyebar Islam, pergaulan bebas dan zina, mahabbah khauf raja'
  tawakal, akhlak madzmumah dan mahmudah, al-kulliyatu al-khamsah, dan
  Wali Songo.
- Folder materi baru: `fase-e/pancasila/` (4 berkas), `fase-e/pai/` (10 berkas).
- **`doc/peta-cakupan-materi.md`** — peta kerja semua 88 buku ajar: setiap
  buku, jumlah bab, status, dan urutan pengerjaan. Aturannya satu buku
  ditandai ✅ hanya bila **seluruh** babnya sudah masuk.

### Catatan teknis
- Grafik ligatur `fi`/`fl` hilang pada .docx modul ajar PAI dan Pancasila
  (`identiikasi`, `Deinisi`, `relektif`, `ilosois`). Pemulihan huruf
  dilakukan saat ekstraksi; kalimat tidak diubah.
- Tujuan pembelajaran PAI berbentuk kalimat "Melalui metode … mampu …"
  (tanpa kata "peserta didik"), sehingga pola ekstraksi diperluas.
- Pancasila: satu materi per unit modul ajar, sehingga jumlah materi per
  bab bervariasi (3–4), bukan selalu 3.
- Butir soal yang kuncinya tidak ada di daftar opsi (Pancasila PAN 1) dan
  soal yang kuncinya bertentangan dengan penjelasan (PAI 2, PAI 9) ditemukan
  oleh `assert` generator lalu diperbaiki sebelum rilis.

### Verifikasi
- Audit otomatis 52 berkas: **0 masalah** — 48 chapter, 146 materi,
  144 asesmen, **1.440 soal** (240 mudah / 480 sedang / 720 sulit),
  5 tipe soal terwakili, tanpa U+FFFD, tanpa LaTeX, tanpa `hint` di soal sulit.
- Import idempoten dua kali: `chapter 0 baru/48 diperbarui`.
- Basis data: `chapters=52 materials=154 questions=1500`.
- `php artisan test` → **96 passed** (865 assertions).

### Cakupan
- **8 mapel Kelas X selesai utuh**: Matematika 8/8, Informatika 8/8,
  Bahasa Indonesia 5/5, IPA 8/8, Pancasila 4/4, PAI 10/10.
- Total **48 chapter / 1.440 soal** terkurasi.

## [0.14.0] - 2026-11-16 15:52 WIB

**Materi SMA/SMK — Tahap 1c: IPA Kelas 10 (Fisika, Kimia, Biologi).**

### Ditambahkan
- **8 chapter baru** dari buku IPA Kelas 10 (Kurikulum Merdeka) sehingga total
  materi terkurasi menjadi **34 chapter / 1.020 soal**:
  - **Fisika 2 bab**: FIS 1 Sistem Pengukuran dalam Kerja Ilmiah (buku Bab I),
    FIS 2 Usaha, Energi, dan Energi Terbarukan (buku Bab VII).
  - **Kimia 3 bab**: KIM 1 Struktur Atom dan Nanoteknologi (Bab III),
    KIM 2 Hukum Dasar Kimia di Sekitar Kita (Bab IV),
    KIM 3 Kimia Hijau dalam Pembangunan Berkelanjutan 2030 (Bab V).
  - **Biologi 3 bab**: BIO 1 Virus dan Peranannya (Bab II),
    BIO 2 Keanekaragaman Makhluk Hidup, Interaksi, dan Peranannya di Alam
    (Bab VI), BIO 3 Perubahan Iklim (Bab VIII).
- Folder materi baru: `fase-e/fisika/`, `fase-e/kimia/`, `fase-e/biologi/`.
- Seluruh **8 bab buku IPA Kelas 10** kini terwakili (buku IPA terpadu
  dipetakan ke tiga mapel sesuai disiplin dominannya).

### Catatan teknis
- Tujuan pembelajaran diambil **verbatim** dari bagian `I. TUJUAN
  PEMBELAJARAN` setiap modul ajar. Modul `.doc` (format OLE2) diekstrak
  dengan dekode UTF-16LE karena `antiword`/`catdoc` tidak tersedia.
- Nomor modul ajar tidak sama dengan nomor bab buku (mis. modul Bab 5 =
  buku Bab III, modul Bab 6 = buku Bab VII); pemetaan dicatat pada
  `source_reference` tiap chapter.
- Generator soal memakai `assert` numerik (usaha, energi, angka penting,
  stoikiometri) sehingga kunci jawaban tidak dapat bergeser.

### Diperbaiki
- 4 soal pada batch ini dikoreksi sebelum dirilis: notasi ilmiah 3200 m,
  penjumlahan angka penting 4,56 + 1,2, massa jenis 2,50 ÷ 0,500, dan
  perhitungan energi kinetik 2 kg pada 9 m/s.

### Verifikasi
- Audit otomatis 34 berkas: **0 masalah** (tanpa U+FFFD, tanpa LaTeX, tanpa
  `hint` pada soal sulit, semua `explanation` terisi, 5/10/15 per chapter,
  5 tipe soal terwakili).
- Import idempoten: import kedua → `chapter 0 baru/34 diperbarui`, total
  tetap `chapters=38 materials=110 questions=1080`.
- `php artisan test` → **96 passed**.
- Browser (Playwright): `/admin/chapters` pager "dari 38 hasil", detail
  chapter KIM 1 menampilkan 5 tujuan pembelajaran, 3 materi, dan 30 soal
  tanpa teks terpotong. `/main/{31,34,36,38}` → HTTP 200.

### Cakupan saat ini
- **5 dari 15+ mapel** Kelas 10: Matematika 8/8 bab, Informatika 8/8,
  Bahasa Indonesia 5/5, IPA 8/8 (Fisika 2, Kimia 3, Biologi 3).
- Belum: Bahasa Inggris, Ekonomi, Sejarah, Geografi, Sosiologi, Antropologi,
  PAI, Pancasila, PJOK, Prakarya, Seni Budaya, mapel kejuruan SMK.

## [0.13.0] - 2026-11-16 14:35 WIB

**Materi SMA/SMK — Tahap 1b: Matematika, Informatika, dan Bahasa Indonesia Kelas 10 lengkap.**

### Ditambahkan
- **15 chapter baru** sehingga total materi terkurasi menjadi **26 chapter /
  780 soal** (di luar 4 chapter demo PAUD/TK/SMP).
  - Matematika Kelas 10 **lengkap 8 bab**: MA 3.1 Vektor, MA 4.1 Trigonometri,
    MA 5.2 Sistem Pertidaksamaan Linear Dua Variabel, MA 7.1 Statistika,
    MA 8.1 Peluang (melengkapi MA 1.1, 1.2, 2.1, 2.2, 5.1, 6.1–6.3).
  - Informatika Kelas 10 **lengkap 8 bab**: INF 4 Jaringan Komputer dan
    Internet, INF 5 Analisis Data, INF 6 Algoritma dan Pemrograman,
    INF 7 Dampak Sosial Informatika, INF 8 Praktika Lintas Bidang.
  - Bahasa Indonesia Kelas 10 **5 bab**: BI 1 Laporan Hasil Observasi,
    BI 2 Kritik Sosial lewat Anekdot, BI 3 Nilai dalam Cerita Lintas Zaman,
    BI 4 Negosiator Ulung, BI 5 Biografi Tokoh.
- Folder materi baru `database/seeders/data/sma-smk/fase-e/bahasa-indonesia/`.
- `doc/inventaris-bab-buku.md` — inventaris 88 buku ajar (PDF) dengan hasil
  pembacaan daftar isi per mapel/kelas/semester.

### Diperbaikan
- **9 kunci jawaban melenceng** pada batch pertama ditemukan oleh penguji
  konsistensi otomatis (MA 2.1 ×2, MA 2.2 ×3, MA 5.1 ×3, MA 6.3 ×1) — sudah
  dikoreksi. Seluruh batch baru memakai **generator ber-assert**
  (`fractions`/`math`) sehingga nilai kunci tidak dapat bergeser.
- 4 soal rusak pada batch Matematika/Informatika/Bahasa Indonesia diperbaiki:
  - MA 5.2 `2x + y < 6` tidak punya opsi benar → diubah ke `≤ 6`
  - MA 5.2 nilai maksimum: opsi benar bertentangan dengan pembahasan
  - MA 7.1 modus: pembahasan bertentangan dengan kunci
  - MA 8.1 peluang mata dadu prima: kunci 1/3 padahal pembahasan 1/2
- Typo `palingbermanfaat` pada materi INF 8.
- `database/seeders/data/sma-smk/_inventory.json` dipindahkan ke
  `database/seeders/data/inventaris-buku-ajar.json` karena sebelumnya ikut
  terbaca importer dan menggagalkan validasi.

### Verifikasi
- `gamecenter:materi-import` idempoten: import kedua menulis 0 chapter baru
  dengan total identik (`chapters=30 materials=86 questions=840`).
- Audit otomatis 26 berkas materi: **0 masalah** (tidak ada U+FFFD, tidak ada
  LaTeX, tidak ada `hint` pada soal sulit, semua `explanation` terisi,
  5/10/15 soal per chapter, 5 tipe soal terwakili).
- `php artisan test` → **96 passed (773 assertions)**.
- Browser (Playwright): `/admin/chapters` menampilkan 10 baris dengan pager
  "dari 30 hasil", halaman 2 menampilkan 10 baris, detail chapter BI 1
  menampilkan tujuan pembelajaran, 3 materi, dan 30 soal tanpa teks terpotong.
- `/main/{16,20,23,26,30}` mengembalikan HTTP 200.

### Catatan
- Cakupan saat ini: **3 dari 15+ mapel** pada Kelas 10 (Matematika 8/8 bab,
  Informatika 8/8 bab, Bahasa Indonesia 5/6 bab — Bab 6 belum ada modul
  ajarnya di folder sumber).
- Sisanya (Fisika, Kimia, Biologi, Ekonomi, Sejarah, PAI, Pancasila, PJOK,
  Prakarya, Seni Budaya, Sosiologi, Antropologi, Geografi, Bahasa Inggris,
  serta mapel kejuruan SMK) masih menunggu pengerjaan per mapel.

## [0.12.0] - 2026-11-16 13:17 WIB

**Materi SMA/SMK — Tahap 1 (Matematika & Informatika Kelas 10).**

### Ditambahkan
- **10 chapter baru** untuk kelas 10 fase E, sehingga total menjadi **11
  chapter / 330 soal** bersama pilot MA 1.1 Eksponen.

  **Matematika** (7 chapter):
  - MA 1.2 Logaritma
  - MA 2.1 Barisan
  - MA 2.2 Deret
  - MA 5.1 Sistem Persamaan Linear
  - MA 6.1 Karakteristik Fungsi Kuadrat
  - MA 6.2 Membentuk dan Mengubah Bentuk Fungsi Kuadrat
  - MA 6.3 Menyelesaikan Masalah dengan Fungsi Kuadrat

  **Informatika** (3 chapter):
  - INF 1 Berpikir Komputasional
  - INF 2 Teknologi Informasi dan Komunikasi
  - INF 3 Sistem Komputer

- **Struktur folder materi per mapel**: berkas kini disimpan sebagai
  `fase-e/matematika/ma-<kode>-<slug>.json` dan
  `fase-e/informatika/inf-<n>-<slug>.json`, satu berkas untuk satu chapter.
- **Dua tes regresi materi bawaan** di `MateriImportCommandTest`:
  - kelengkapan 11 chapter (3 materi + 5/10/15 soal per chapter, semua soal
    berpenjelasan, tidak ada hint pada soal sulit);
  - cakupan seluruh tipe soal objektif (pilihan ganda, jawaban ganda,
    menjodohkan, seret-lepas, susun urutan) dan total 330 soal.

### Diubah
- Berkas pilot `sma-kelas-10-matematika.json` dipindahkan menjadi
  `fase-e/matematika/ma-1.1-eksponen.json`; rujukan path di tes dan seeder
  ikut diperbarui.

### Catatan kualitas
- Setiap soal punya `explanation`. Soal sulit tidak memakai `hint`.
- Penulisan simbol matematika memakai Unicode (², ×, ÷, √), bukan LaTeX.
- Jawaban soal hitungan diperiksa ulang dengan skrip pembanding, bukan hanya
  dibaca manual: ditemukan dan diperbaiki **9 kunci jawaban keliru** —
  MA 2.1 ×2 (satu di antaranya soalnya tidak konsisten sehingga ditulis
  ulang), MA 2.2 ×3, MA 5.1 ×3, dan MA 6.3 ×1. Skrip pembanding kini menjadi
  bagian dari alur penulisan chapter.
- Hasil impor idempoten: impor kedua melaporkan `0 baru / 11 diperbarui`
  dengan jumlah baris basis data tidak berubah.

### Verifikasi
- `php artisan gamecenter:materi-import --dry-run` → **11 berkas, 0 gagal**.
- Impor nyata: chapters 15, materials 41, assessments 45, questions 390,
  options 1360 (tidak berubah pada impor ulang).
- `php artisan test` → **96 passed (743 assertions)**.
- Peramban: daftar chapter admin menampilkan 15 baris (10 + 5 pada halaman 2),
  semua chapter baru menunjukkan 3 materi / 30 soal / 90 menit; halaman tinjau
  MA 6.1 menampilkan tujuan pembelajaran, materi, dan kuis.
- `/main/<id>` untuk chapter 6, 9, 11, 13, 15 semuanya **HTTP 200**.


## [0.11.0] - 2026-11-16 12:43 WIB

**Materi SMA/SMK — Tahap 0 (fondasi impor materi).**

### Ditambahkan
- **Perintah `php artisan gamecenter:materi-import`** untuk mengimpor berkas
  JSON materi SMA/SMK ke database. Opsi `--dry-run` hanya memeriksa skema
  tanpa menulis. Impor bersifat **idempoten**: berkas yang sama boleh
  dijalankan berulang tanpa menambah baris.
- **`app/Services/Materi/`** — `MateriImporter` (logika impor, transaksional),
  `MateriSchema` (validator), `MateriImportResult` (ringkasan), dan
  `MateriValidationException` (galat berisi daftar masalah per lokasi).
- **`database/seeders/SmaSmkMaterialSeeder`** — mengimpor seluruh
  `database/seeders/data/sma-smk/**/*.json` saat `db:seed`.
- **Chapter percontoh MA 1.1 "Eksponen"** (SMA kelas 10 Matematika):
  3 materi bacaan + 3 asesmen dengan 30 soal (5 mudah, 10 sedang, 15 sulit),
  mencakup pilihan ganda, pilihan ganda kompleks, menjodohkan, puzzle, dan
  tarik-letak. Ditulis ulang dari modul ajar `MA 1.1 Eksponen.docx`.
- **Halaman panel "Materi → Chapter materi"** (hanya-baca) untuk meninjau
  chapter, materi, dan seluruh soal beserta kuncinya.
- **12 tes** di `tests/Feature/MateriImportCommandTest.php` dan
  `tests/Concerns/SeedsDemoContent.php`.

### Diubah
- **`DemoContentSeeder` tidak lagi dipanggil `DatabaseSeeder`.** Chapter demo
  "Eksponen" menempati mapel dan slug yang sama dengan materi sesungguhnya;
  menyemai keduanya membuat baris materi berlipat setiap `db:seed` diulang.
  Seeder demo tetap tersedia sebagai fixture tes.

### Diverifikasi
- **94 test otomatis / 712 assertion** lulus via `php artisan test`
  (2026-11-16 12:43 WIB).
- `migrate:fresh` + `db:seed` dua kali berturut-turut: jumlah chapter, materi,
  asesmen, soal, dan opsi **tidak berubah** pada penyemaian kedua.
- Impor membuang `hint` pada soal sulit dan mengisi `points`/`time_limit`
  otomatis dari enum `Difficulty` (10/20/30 poin; 90/75/60 detik).
- Halaman tinjau diperiksa di Chromium: 5 chapter terdaftar, tabel materi dan
  ketiga tabel asesmen selebar 968 px dengan kolom rata, tanpa luapan
  horizontal pada lebar 390 px.
- Ketiga asesmen Eksponen dapat dimainkan (`/main/{id}` → HTTP 200); muatan
  `puzzle` dan `drag_drop` sampai ke klien.

### Catatan
- Validator menolak seluruh berkas bila ada satu masalah, sehingga tidak
  pernah ada impor setengah jadi. Contoh aturan: soal tanpa `explanation`
  ditolak (standar mutu §9), begitu juga `hint` pada soal sulit.



## [0.10.0] - 2026-11-16 11:48 WIB

**Fase 5 — Kesiapan deploy.**

### Ditambahkan
- **Perintah `php artisan gamecenter:deploy-check`** (`--strict` untuk CI)
  dengan 18 pemeriksaan: versi & ekstensi PHP, `APP_ENV`, `APP_DEBUG`,
  `APP_KEY`, `APP_URL`, cookie sesi aman, izin 6 folder tulis, `storage:link`,
  manifest build, tema panel Filament, aset PWA, koneksi database, migrasi
  tertunda, data awal, dan route inti. Exit code `1` bila ada kegagalan atau
  (dengan `--strict`) peringatan tersisa.
- **`.env.production.example`** — template environment produksi tanpa
  kredensial nyata, memakai placeholder `>>> GANTI <<<`, `LOG_CHANNEL=daily`,
  `SESSION_ENCRYPT=true`, dan `SESSION_SECURE_COOKIE=true`.
- **5 test baru** di `tests/Feature/DeployCheckCommandTest.php`.

### Diubah
- Toast kini muncul dari **atas layar ke bawah**, di tengah, untuk panel admin
  (Filament, via `Notifications::alignment(...)` di `AppServiceProvider`) dan
  aplikasi siswa (`ToastHub`). Animasi baru `drop` di `resources/css/app.css`.
- Tipografi halaman **Ringkasan** disamakan dengan sidebar sebagai jangkar
  14px: token `--gc-text-*` dan skala peran di
  `resources/css/filament/admin/theme.css`. Judul halaman/hero turun dari
  34–42px menjadi 20px, dan tinggi hero menyusut 251px → 191px sehingga kartu
  statistik terlihat tanpa scroll.
- **Kartu pengguna + tombol Keluar** di footer sidebar panel
  (`resources/views/filament/sidebar-user-card.blade.php`), dengan dialog
  konfirmasi. Setelah keluar, pengguna kembali ke beranda melalui
  `App\Filament\Auth\Responses\LogoutResponse`.
- Halaman login panel (`/admin/login`) dihapus; semua peran masuk lewat
  `/masuk` dan diarahkan berdasarkan role (`RedirectsAfterAuth` memakai
  `Inertia::location` agar tidak memicu dialog error Inertia).
- `CACHE_VERSION` service worker dinaikkan ke `0.10.0`.

### Diperbaiki
- Login admin/guru menampilkan toast "Ada yang belum berjalan" karena
  redirect 302 ke halaman non-Inertia. Diganti `Inertia::location()`.
- Tombol "Ya, keluar" pada dialog konfirmasi tidak berfungsi: atribut
  `data-confirm` tanpa nilai menghasilkan `dataset.confirm === ""` (falsy)
  sehingga submit selalu ditahan.
- Hook `AUTH_LOGIN_FORM_AFTER` merujuk view yang sudah dihapus.

### Diverifikasi
- **81 test otomatis / 665 assertion** lulus via `php artisan test`
  (2026-11-16 11:48 WIB).
- `migrate` + `db:seed` dari nol di SQLite bersih: 21 migrasi, 5 jenjang,
  12 kelas, 133 mapel, 82 soal, 8 lencana, 4 akun demo.
- `php artisan optimize` sukses (config, event, route, view, blade-icons,
  filament).
- `gamecenter:deploy-check`: dev = 13 lulus/5 peringatan/0 gagal; simulasi
  env produksi = 17 lulus/1 peringatan/0 gagal.
- Toast diverifikasi di Chromium: panel `top: 20px` tengah, hilang otomatis
  ~6 s; aplikasi siswa `top: 12px` tengah, hilang otomatis 4,8 s.
- Tipografi diukur langsung: sidebar 14px, judul halaman 20px, hero 20px,
  label stat 11px, nilai stat 24px.

### Catatan
- Jalankan `php artisan optimize:clear` sebelum `php artisan test`. Cache
  config hasil `optimize` menyimpan `SESSION_ENCRYPT`/`APP_ENV` sehingga sesi
  test tidak cocok dengan token CSRF (7 tes gagal dengan HTTP 419).



## [0.9.0] - 2026-11-16 09:47 WIB

### Ditambahkan
- **Sistem toast global** `ToastHub` + `resources/js/lib/toast.ts` untuk semua
  pemberitahuan sukses, info, peringatan, dan error. Toast tampil di kanan
  bawah (atau tengah bawah di ponsel), bisa ditutup, dan menutup sendiri.
- **Pemeta error ramah pengguna** `resources/js/lib/friendly-error.ts`.
  Dialog teknis bawaan Inertia untuk `httpException`/`networkError` diganti
  toast berbahasa Indonesia yang menjelaskan penyebab dan langkah berikutnya.
- **Login panel admin menerima email atau username** lewat
  `App\Filament\Auth\Login`, sama seperti login utama. Pesan gagal masuk dan
  batas percobaan memakai bahasa awam.
- **Halaman error ramah** untuk `401`, `403`, `404`, `419`, `429`, `500`, dan
  `503` dengan tombol kembali ke beranda/halaman sebelumnya.
- **Terjemahan validasi Indonesia** di `lang/id` (`validation`, `auth`,
  `passwords`) dan nama field yang mudah dipahami.
- **Pintasan menjalankan aplikasi**: file `artisan` di folder induk meneruskan
  perintah ke proyek, plus `serve.bat` untuk menjalankan server lokal.

### Diubah
- Flash keanggotaan tidak lagi berupa kotak inline; semuanya tampil sebagai
  toast melalui layout.
- Pesan sinkronisasi offline dibuat lebih ramah, tanpa kode status teknis.
- **Card login panel admin dipersempit** ke `Width::Small` (maks. 24rem) dengan
  padding lebih ringkas, dan ditambahkan tombol **Kembali ke Game Center** di
  bawah form untuk kembali ke beranda aplikasi.
- `CACHE_VERSION` service worker dinaikkan ke `0.9.0`.

### Diverifikasi
- **68 test otomatis / 613 assertion** lulus via `php artisan test`
  (2026-11-16 09:47 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses (2026-11-16 09:47 WIB).
- Login panel admin diuji dengan username dan email, termasuk tampilan card
  sempit dan tombol kembali ke beranda.
- `php artisan serve` dari folder induk berhasil setelah pintasan ditambahkan.

## [0.8.0] - 2026-11-16 08:59 WIB

### Ditambahkan
- **Tema visual per jenjang** (Fase 4): `data-level-theme` menimpa token
  `--color-red*`, tipografi display, orb dekoratif, dan animasi halus untuk
  **PAUD (ceria)**, **TK (petualangan)**, **SMP (penjelajah)**,
  **SMA/SMK (fokus)** beserta varian mode gelap.
- **Materi pembelajaran 60%** di halaman bermain: `MaterialViewer` dengan
  akordeon, renderer markdown ringan (judul, daftar, kode, tabel), penanda
  "sudah dibaca", progress bar, dan penyimpanan status baca di perangkat.
- **Halaman progres `/progres`**: ringkasan level/XP/koin/streak, enam kartu
  statistik, grafik aktivitas 7 hari, progres per bab, riwayat 12 sesi terakhir,
  dan koleksi lencana (terbuka/terkunci).
- **Halaman hasil `/hasil/{gameSession}`**: skor, lulus KKM, benar/salah/kosong,
  XP/koin, serta pembahasan tiap jawaban lengkap dengan kunci dan penjelasan.
- **Filter mapel** pada topbar katalog (jenjang → kelas → mapel → mode) yang
  saling menyaring dengan chip kelompok dan pencarian.
- **Strip "Lanjutkan belajar"** di katalog berisi bab terakhir yang dibuka.
- **Kurasi konten lintas jenjang** `CuratedContentSeeder`: 4 bab baru
  (PAUD bentuk & warna, TK angka & berhitung, SMP bilangan bulat, SMK
  algoritma) dengan total **15 soal per bab** dan materi pendukung.
- **`AchievementService`**: lencana diberikan di server setelah sesi/progres
  disinkronkan (`first-step`, `perfect-score`, `streak-3`, `streak-10`,
  `chapter-master`, `math-genius`, `case-master`, `bookworm`).
- Kolom **`materials_read`** pada `user_progress` dan sinkronisasi
  `progress` yang membawa jumlah materi dibaca.

### Diubah
- Menu pengguna menambahkan tautan **Progres & lencana**; halaman hasil
  menyediakan tombol menuju progres dan katalog.
- Syarat lencana `chapter-master` diselaraskan dengan deskripsinya, yaitu
  menuntaskan **3 tingkat kesulitan** dalam satu bab.
- Katalog menampilkan jumlah bab/soal terbaru (5 bab, 82 soal) dan tema
  jenjang aktif ikut mengubah aksen merah di seluruh layout.
- `CACHE_VERSION` service worker dinaikkan ke `0.8.0`.
- README, roadmap, dan laporan Fase 4 diperbarui.

### Diverifikasi
- **65 test otomatis / 593 assertion** lulus via `php artisan test`
  (2026-11-16 08:59 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses (hanya peringatan
  ukuran chunk Mermaid yang sudah ada).
- Migrasi `add_materials_read_to_user_progress_table` dan `db:seed` berhasil
  pada database MySQL `gamecenter`.

## [0.7.0] - 2026-11-16 08:05 WIB

### Ditambahkan
- **Halaman bermain `/main/{assessment}`** dengan alur lengkap: intro,
  timer sesi, soal satu per satu, umpan balik langsung setelah diperiksa,
  peta soal, petunjuk, hasil, tinjauan jawaban, dan tombol main lagi.
- **Mesin permainan client-side** `game-engine.ts`: tipe pilihan ganda,
  pilihan ganda kompleks, urutan (`drag_drop`/`puzzle`), menjodohkan,
  simulasi, dan uraian; penilaian, ringkasan skor, serta payload sesi.
- **Enam mekanik bermain**: `QuizGame` (termasuk pintasan angka 1–9),
  `DragDropGame` (tarik-lepas + tombol panah), `MatchGame` (pilih kiri lalu
  kanan, lepas pasangan), puzzle urutan, `SimulationGame` untuk studi kasus,
  dan editor uraian dengan rubrik.
- **Gamifikasi** `gamification.ts`: level 1–5 (Pemula s.d. Legenda), XP,
  koin, progress level, dan lencana sesi (Langkah Pertama, Sempurna, streak,
  Jenius Matematika, Ahli Studi Kasus).
- **Konten demo interaktif**: soal pilihan ganda kompleks dan drag & drop pada
  mode sedang, serta matching, puzzle, dan simulasi pada mode sulit. Total bank
  soal Eksponen menjadi **22 soal** (5 mudah, 8 sedang, 9 sulit).
- Cache asesmen + soal lengkap ke IndexedDB dan antrean sesi otomatis setelah
  selesai bermain; tamu tetap bisa bermain, lalu diarahkan masuk untuk
  menyimpan hasil.
- Test baru untuk halaman bermain dan penilaian uraian (lihat verifikasi).

### Diubah
- Kartu asesmen di panel bab kini memiliki tombol **Main** menuju halaman
  permainan; footer katalog menjelaskan alur mulai bermain dan penyimpanan
  otomatis.
- Soal uraian disimpan beserta jawaban siswa tetapi **tidak masuk skor sesi**
  sampai dinilai guru/AI; server tetap menilai ulang soal objektif saat sync.
- Jumlah soal pada test katalog dan idempotensi seeder disesuaikan menjadi 22.
- `CACHE_VERSION` service worker dinaikkan ke `0.7.0` agar aset lama dibuang.
- README, roadmap, dan laporan Fase 3 diperbarui.

### Diverifikasi
- **56 test otomatis / 390 assertion** lulus via `php artisan test`
  (2026-11-16 08:05 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses (hanya peringatan
  ukuran chunk Mermaid yang sudah ada).
- Uji browser nyata (Playwright/Chromium, 1440 px dan 390 px): login `siswa`,
  membuka mode sedang dari panel bab, menjawab 7 soal inti dengan benar,
  melewati uraian, lalu memperoleh skor **100**, 7 benar, 0 salah, 0 kosong,
  **+145 XP**, **+29 koin**, naik ke **level 3**, dan lencana sesi. Semua
  mekanik di mode sulit (matching, puzzle, simulasi) memberi umpan balik
  "Tepat!"; halaman ponsel tidak mengalami overflow; tidak ada error konsol
  atau respons HTTP ≥ 400 (2026-11-16 08:05 WIB).
- Sinkronisasi server terverifikasi: sesi skor 100, `max_score` 145,
  `xp_earned` 145, 7 jawaban, `synced=true`; pengguna `siswa` memiliki 265 XP,
  74 koin, level 3; progres bab 1 `best_score=100`, `attempts=1`, `completed`
  (2026-11-16 08:05 WIB).
- **Uji offline nyata**: service worker mengontrol halaman, `/main/2` dimuat
  ulang tanpa jaringan, satu soal dijawab dan sesi diselesaikan, antrean berisi
  1 item, lalu otomatis kosong setelah koneksi kembali. Server menerima sesi
  (`score=14`, `max_score=145`, `xp_earned=20`, 2 jawaban, `synced=true`),
  pengguna naik ke 80 XP / 18 koin, dan progres bab mencatat `attempts=2`
  (2026-11-16 08:09 WIB).

## [0.6.0] - 2026-11-16 07:35 WIB

### Ditambahkan
- **Tema Filament kustom** yang memakai identitas Ruang Belajar: palet kanvas
  hangat, permukaan putih, tinta gelap, merah `#e60012`, Fraunces Variable +
  Instrument Sans Variable (Fontsource), latar dot-grid, kartu bershadow,
  sidebar/topbar hangat, serta varian gelap dengan palet yang sama.
- **Dashboard admin baru** `/admin`: hero sapaan kontekstual (jam, tanggal,
  ringkasan sesi/siswa/pengajuan), empat kartu statistik dengan sparkline 7
  hari, grafik aktivitas sesi, panel akses cepat, dan tabel pengajuan upgrade
  terbaru dengan tautan langsung ke antrean.
- Dashboard sadar peran: **admin** melihat statistik dan antrean keanggotaan;
  **guru** melihat statistik materi/soal dan jalur akses pengajaran tanpa
  pengelolaan keanggotaan.
- Brand mark khusus (ikon topi wisuda + wordmark "Game Center / Ruang belajar")
  untuk sidebar, topbar login, dan favicon panel.
- 2 test dashboard baru: konten admin bertema + penyembunyian widget
  keanggotaan untuk guru.

### Diubah
- `AdminPanelProvider` memakai `viteTheme`, primary merah `#e60012`, gray
  Stone, font panel Fraunces/Instrument Sans, sidebar yang bisa diciutkan, dan
  logo/favicon kustom; widget bawaan `AccountWidget`/`FilamentInfoWidget`
  diganti widget dashboard aplikasi.
- `vite.config.ts` menambahkan entry `resources/css/filament/admin/theme.css`.
- Tombol aksi primary memakai merah merek penuh (bukan tint Filament yang
  pucat), termasuk tombol masuk di halaman login.
- Tabel pengajuan di dashboard menyembunyikan kolom nominal/status/waktu pada
  layar sempit agar tetap terbaca tanpa scroll horizontal.
- README menambahkan bagian panel admin dan memperbarui jumlah test.

### Diverifikasi
- 52 test otomatis / 341 assertion lulus via `php artisan test`
  (2026-11-16 07:35 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses, termasuk bundle tema
  Filament (2026-11-16 07:35 WIB).
- Uji browser nyata (Playwright/Chromium, 1440 px): login admin, dashboard
  light + dark, dashboard guru, dan tampilan ponsel 390 px tanpa error
  konsol; statistik, grafik, antrean, dan tautan aksi tampil sesuai peran
  (2026-11-16 07:35 WIB).

## [0.5.0] - 2026-11-16 06:55 WIB

### Ditambahkan
- Fondasi **offline-first** di client: IndexedDB `gamecenter-offline` (versi 1)
  dengan store `catalog`, `materials`, `questions`, `assessments`, `progress`,
  `sessions`, `syncQueue`, dan `userSettings`. Katalog jenjang/kelas/mapel
  disimpan otomatis setiap halaman jelajah berhasil dimuat.
- **Antrean sinkronisasi** client: item ber-`uuid`, pengiriman batch 25 item,
  retry otomatis (maksimal 5 percobaan), flush saat kembali online, saat tab
  aktif kembali, setelah item masuk antrean, dan tombol manual.
- **`POST /api/sync`** (`auth:sanctum`, throttle 60/menit, maksimal 50 item per
  batch) dengan idempotensi per `client_uuid`. Server menilai ulang jawaban
  pilihan ganda/ganda-kompleks, menyimpan sesi + jawaban + hasil, menghitung
  XP/koin/level/streak, dan memperbarui progres bab. Item gagal tidak
  memblokir item lain dan bisa dikirim ulang dengan UUID yang sama.
- **PWA**: `public/sw.js` (app shell network-first + fallback `offline.html`,
  cache-first untuk aset `/build`, font, dan ikon), `manifest.webmanifest`,
  ikon SVG + maskable, serta registrasi service worker pada build produksi.
- Background Sync tag `gamecenter-sync` memicu flush dari tab aktif; request
  Inertia dan `/api/*` tidak di-cache demi privasi.
- Indikator status di footer: **Offline**, **Menyinkronkan…**, **n tersimpan**
  (dapat diklik untuk sinkron manual), dan **Sinkron tertunda**.
- Pembersihan data lokal: cache halaman dihapus saat `POST /keluar`, antrean +
  progres IndexedDB dihapus saat pengguna keluar.
- 7 test baru `SyncApiTest`: akses tamu, penilaian server, idempotensi, progres,
  jawaban, dan kegagalan parsial.

### Diubah
- `SANCTUM_STATEFUL_DOMAINS` ditambahkan ke `.env.example` dan `.env`
  (`gamecenter.test`, `localhost`, `127.0.0.1`) agar `/api/*` menerima cookie
  sesi SPA.
- README mendokumentasikan offline-first, kontrak sinkronisasi, batasan fase,
  dan cara memperbarui cache service worker.
- Roadmap `doc/plan-1.md` menandai Phase 2 selesai; laporan lengkap ada di
  `doc/fase-2-implementasi.md`.

### Diverifikasi
- 50 test otomatis / 328 assertion lulus via `php artisan test`
  (2026-11-16 06:55 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses — app 364.58 kB
  (115.08 kB gzip) (2026-11-16 06:55 WIB).
- Uji HTTP nyata melalui `php artisan serve`: login sesi + CSRF lalu
  `POST /api/sync` mengembalikan `completed`; `/manifest.webmanifest`,
  `/sw.js`, `/offline.html`, dan `/icon.svg` merespons 200; sync tamu 401
  (2026-11-16 06:55 WIB).
- Catatan: uji manual offline di browser (DevTools offline + Background Sync)
  belum dijalankan pada mesin ini dan disarankan menyatu dengan modul permainan
  Fase 3.

## [0.4.3] - 2026-11-16 00:28 WIB

### Diubah
- Bagian **Peta peran dan akses** di `/panduan` tidak lagi memakai diagram
  Mermaid; akses per peran kini disajikan sebagai tabel teks (`DataTable`)
  dengan caption "Hubungan peran pengguna dengan fitur utama.".
- Diagram Mermaid tetap dipakai untuk alur bermain dan alur upgrade.

### Dihapus
- Definisi chart `roleChart` dan pemakaian `MermaidDiagram` pada halaman
  pengenalan, sehingga tidak ada lagi SVG yang bisa keluar dari kartu di
  bagian tersebut.

### Diverifikasi
- Bagian peta peran tidak memuat SVG diagram; tabel peran tampil penuh di
  320–1920 px tanpa overflow halaman (2026-11-16 00:28 WIB).
- `npm run typecheck` dan `npm run build` sukses (2026-11-16 00:28 WIB).

## [0.4.2] - 2026-11-16 00:22 WIB

### Diubah
- Label diagram **Peta peran dan akses** dipersingkat menjadi "Jelajah materi",
  "Keanggotaan", "Panel admin", dan "Verifikasi" agar diagram lebih ringkas dan
  tidak melebar sampai tepi kartu.
- Inset kartu diagram dinaikkan menjadi 16 px di ponsel dan 20 px di layar
  lebar; `useMaxWidth` diaktifkan eksplisit dan SVG dipusatkan dengan batas
  `max-width: 100%` di dalam kontainer `mx-auto max-w-full`.

### Diverifikasi
- Uji browser 320/360/390/768/1024/1366/1920 px: diagram tampil penuh, tepat di
  tengah kartu (selisih 0 px), berjarak dari tepi kartu, dan tanpa overflow
  halaman (2026-11-16 00:22 WIB).
- `npm run typecheck` dan `npm run build` sukses (2026-11-16 00:22 WIB).

## [0.4.1] - 2026-11-16 00:13 WIB

### Diperbaiki
- Diagram **Peta peran dan akses** pada `/panduan` kini tampil penuh, tepat di
  tengah kartu, dan tidak keluar dari layout kartu di semua lebar layar. Aturan
  CSS lama `min-width: 620px` pada ponsel memaksa SVG melebihi lebar kartu
  sehingga terpotong; aturan tersebut dihapus.
- SVG diagram dibatasi `max-width: 100%`, `height: auto`, dan dipusatkan dengan
  `margin-inline: auto`; kontainer kartu memakai `overflow-hidden` agar tidak
  ada luapan. Petunjuk "geser diagram" yang tidak relevan lagi dihapus.

### Diverifikasi
- Uji browser 1366/1024/390/360 px terang dan 390 px gelap: SVG terlihat,
  selisih tengah 0 px, seluruh diagram berada di dalam kartu, tanpa overflow
  horizontal halaman (2026-11-16 00:13 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses
  (2026-11-16 00:13 WIB).

## [0.4.0] - 2026-11-16 00:05 WIB

### Ditambahkan
- Pusat bantuan publik **`/panduan`** bergaya dokumentasi produk di dalam
  aplikasi (bukan Docusaurus): 11 topik dalam 4 kelompok, sidebar topik,
  pencarian, breadcrumb, daftar isi per halaman, navigasi sebelumnya/berikutnya,
  dan state topik tidak ditemukan.
- Tautan **Panduan** di topbar: chip pada baris menu beranda ponsel, ikon di
  halaman lain, tautan teks di desktop, serta item Panduan di menu akun.
- Diagram **Mermaid** untuk peta peran, alur bermain, dan alur upgrade. Mermaid
  dimuat dinamis, memakai `securityLevel: 'strict'`, mengikuti tema terang/gelap,
  dan bisa digeser horizontal di ponsel.
- `GuideController` + route publik `/panduan/{page?}` serta 3 test pusat bantuan.
- Dependency `mermaid` (chunk terpisah; tidak dimuat di halaman lain).

### Diubah
- Label menu Kelas di topbar beranda dipotong responsif (76 px di ponsel,
  124 px sejak `sm`) agar chip Panduan muat tanpa overflow pada 360 px.
- Drawer daftar topik ponsel dirender lewat portal agar menutup topbar, dengan
  animasi geser, tombol tutup, overlay, dan pintasan `Esc`.
- Halaman panduan memakai scroll internal satu viewport; pencarian topik
  direset saat berpindah halaman.
- README mendokumentasikan pusat bantuan, struktur topik, dan Mermaid.

### Diverifikasi
- 43 test otomatis / 269 assertion lulus via `php artisan test`
  (2026-11-16 00:05 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses
  (2026-11-16 00:05 WIB).
- Uji browser 360/390/1366 px, terang & gelap: navigasi topbar ke `/panduan`,
  diagram Mermaid tampil dan dirender ulang saat tema berganti, pencarian
  menyaring topik, deep link `/panduan/upgrade`, drawer terbuka/tutup
  (overlay dan `Esc`), diagram dapat digeser di ponsel, serta tidak ada overflow
  horizontal halaman (2026-11-16 00:05 WIB).

## [0.3.1] - 2026-11-15 23:39 WIB

### Ditambahkan
- Tombol **Upgrade sekarang** di hero halaman keanggotaan untuk anggota paket
  Gratis; sekali klik langsung membuka dialog pengajuan paket rekomendasi
  (Professional).
- Menu akun menandai anggota Gratis dengan tautan **Upgrade keanggotaan**
  (ikon merah + titik penanda), sedangkan anggota berbayar tetap melihat
  **Keanggotaan**.

### Diubah
- CTA kartu paket berbayar menjadi **Upgrade paket** agar maksud peningkatan
  paket lebih jelas bagi free member.
- README menjelaskan titik masuk upgrade untuk anggota Gratis.

### Diverifikasi
- `npm run typecheck` bersih dan `npm run build` sukses
  (2026-11-15 23:39 WIB).
- Uji browser 390 px: login anggota Gratis (`siswa-smk`) → menu akun
  "Upgrade keanggotaan" → tombol "Upgrade sekarang" membuka dialog paket
  Professional → Batal menutup dialog; CTA "Upgrade paket" tampil di kartu
  berbayar dan tidak ada overflow horizontal (2026-11-15 23:39 WIB).
- 40 test otomatis / 239 assertion lulus via `php artisan test`
  (2026-11-15 23:39 WIB).

## [0.3.0] - 2026-11-15 23:24 WIB

### Ditambahkan
- Autentikasi siswa/guru: halaman `/masuk` dan `/daftar`, login memakai email
  **atau** username, pembatasan 5 percobaan masuk per menit, penolakan akun
  nonaktif, dan redirect balik yang hanya menerima path internal.
- Skema keanggotaan: tabel `membership_plans` dan `memberships`, enum status
  (`pending`, `active`, `expired`, `rejected`) dan siklus tagihan
  (`monthly`, `yearly`), kode referensi unik `GC-XXXXXX`, serta snapshot harga
  saat pengajuan.
- Katalog publik `/keanggotaan` dengan empat paket — Gratis, Standard
  Rp29.000/bulan, Professional Rp99.000/bulan (rekomendasi), Enterprise
  Rp499.000/bulan — toggle bulanan/tahunan (tahunan = 10× bulanan), penanda
  paket aktif, dan rincian fitur tiap paket.
- Alur upgrade manual: pengguna mengajukan paket lebih tinggi, mentransfer ke
  rekening yayasan, lalu admin menyetujui atau menolak. Pengajuan ganda, paket
  gratis, dan paket setara/lebih rendah ditolak di server.
- Halaman admin Filament "Keanggotaan": kelola paket (harga, fitur, urutan,
  status unggulan) dan antrean pengajuan dengan filter status, badge jumlah
  pending di navigasi, serta aksi **Setujui**/**Tolak** beserta catatan admin.
  Resource keanggotaan hanya tampil untuk admin; guru tetap bisa masuk panel.
- Persetujuan membership berjalan dalam transaksi: paket baru aktif dengan
  `starts_at`/`ends_at` sesuai siklus, paket aktif sebelumnya otomatis
  kedaluwarsa, dan `approved_by`/`approved_at` tercatat.
- Menu akun di topbar: nama, username, badge paket beserta masa berlaku,
  tautan Keanggotaan, panel admin/guru sesuai peran, dan tombol Keluar (POST).
- Seeder paket + data demo (siswa Standard aktif, guru Professional pending),
  konfigurasi rekening `config/membership.php` dari
  `MEMBERSHIP_BANK_NAME/NUMBER/HOLDER`, tipe React `MembershipPlan`,
  `MembershipRecord`, `MembershipInfo`, serta helper `formatRupiah` dan
  `formatDateId`.

### Diubah
- Topbar tamu menampilkan tombol **Masuk** (dan **Daftar** di layar lebar)
  menggantikan chip "Mode tamu" dan tautan statis "Panel guru".
- Ringkasan keanggotaan dibagikan otomatis lewat props Inertia
  `auth.user.membership` untuk semua halaman.
- README mendokumentasikan akun demo, paket, alur transfer, dan variabel
  rekening.

### Diverifikasi
- 40 test otomatis / 239 assertion lulus via `php artisan test`
  (2026-11-15 23:24 WIB).
- `npm run typecheck` bersih dan `npm run build` sukses
  (2026-11-15 23:24 WIB).
- Uji browser 1366/390/360 px, terang & gelap: daftar → login → ajukan
  Standard tahunan → banner pending + kode referensi; admin menyetujui dari
  Filament dan siswa langsung melihat paket aktif; tanpa overflow horizontal
  dan input 16 px di ponsel (2026-11-15 23:24 WIB).

## [0.2.0] - 2026-11-15 22:57 WIB

### Ditambahkan
- Mode gelap/terang dengan tombol toggle (ikon matahari/bulan) di topbar.
  Preferensi awal mengikuti `prefers-color-scheme` perangkat; pilihan pengguna
  disimpan di localStorage (`gamecenter.theme`) sehingga bertahan setelah muat
  ulang.
- Skrip inline di `app.blade.php` yang menerapkan tema sebelum halaman digambar
  (tanpa kedip), sekaligus menyelaraskan `color-scheme` dan meta `theme-color`.
- Token palet gelap di `app.css`: kanvas `#0e0c0d`, surface `#171214`, ink
  `#f7f1f2`, rule `#2d2629`, merah `#ff3945`, lengkap dengan bayangan kartu,
  sheet, dan FAB, serta pola titik latar yang adaptif.
- Varian `dark:` untuk border dan tile ikon tiap warna mapel agar tetap lembut
  di latar gelap.

### Diubah
- Lapisan peredup dialog/drawer memakai `bg-black/45` agar tetap gelap pada
  kedua tema.
- Chip XP disembunyikan di bawah breakpoint `sm` supaya topbar tetap muat di
  ponsel setelah tombol tema ditambahkan.
- Badge level memakai `text-surface`/`ring-surface` agar teks dan cincin tetap
  kontras di kedua tema.
- README mendokumentasikan mode gelap/terang dan cara kerjanya.

### Diverifikasi
- `npm run typecheck` bersih dan `npm run build` sukses (22:57).
- 19 test otomatis / 140 assertion lulus via `php artisan test` (22:57).
- Uji browser pada lebar 360, 390, dan 1366 px: toggle berfungsi, preferensi
  bertahan setelah reload, footer tetap satu baris, dan tidak ada overflow
  (22:57).

## [0.1.0] - 2026-11-15 22:14 WIB

### Ditambahkan
- Fondasi Laravel 13, Inertia.js, React 19, TypeScript, Tailwind CSS 4, Vite 7,
  Filament 5 (`/admin`), dan Sanctum (SPA + token).
- 15 tabel domain, model Eloquent + relasi + enum, seeder jenjang/kelas/mapel
  (5 jenjang, 12 kelas, 133 mapel), seeder bank soal Eksponen (17 soal, 3
  tingkat), serta 19 test otomatis (140 assertion).
- Halaman jelajah materi `/` dengan data jenjang → kelas → mapel → bab →
  assessment dan ringkasan jumlah mapel/bab/soal.
- Navigasi topbar berupa menu dropdown Jenjang, Kelas, dan Mode permainan;
  pencarian berbentuk ikon dengan palet pencarian (pintasan `/`, tutup `Esc`).
- Grid kartu materi 4 kolom di desktop, 3 di tablet, 2 di ponsel; kartu kompak
  dengan border dan tile ikon berwarna per mapel, label "Segera" untuk mapel
  tanpa konten, serta drawer bab per mapel.
- Pagination 12 kartu (layar lebar) / 8 kartu (layar kecil) dengan ringkasan
  "Menampilkan a–b dari n mapel".
- Menu Bermain pribadi (nama pemain) dan kelompok (nama kelompok + 2–8 nama
  pemain, tambah/hapus baris), sesi tersimpan di localStorage
  (`gamecenter.play-session`), ringkasan sesi aktif, dan opsi akhiri sesi.
- Footer satu baris di semua halaman: versi sistem otomatis dari changelog ini
  di kiri, ringkasan + pagination rata tengah, dan kredit
  "created & developed by haraki" di kanan.

### Diubah
- Palet warna sistem menjadi merah bendera Indonesia `#e60012`, putih, dan
  hitam; font Fraunces Variable (judul) dan Instrument Sans Variable (label)
  di-host sendiri lewat Fontsource agar tetap offline.
- Header ringkas: identitas aplikasi, tombol Bermain, tombol cari, chip
  koin/XP, dan level pengguna; chip "Mode tamu" disembunyikan di layar sangat
  kecil agar topbar tetap satu baris.
- Antarmuka memakai satu viewport penuh (`h-dvh`) tanpa scroll halaman;
  daftar kartu memakai scrollbar tersembunyi.
- Pagination dipindahkan dari area konten ke footer; di ponsel ringkasan
  disingkat `a–b / n` dan pager menjadi `‹ halaman / total ›`.

### Diperbaiki
- Overflow horizontal topbar dan dropdown menu pada lebar 360–1440 px.
- Dropdown Bermain selalu berada di dalam layar, termasuk di ponsel.
- Dialog bermain dan palet pencarian kembali ringkas (tidak memenuhi tinggi
  layar) dan dapat ditutup dengan `Esc`.

### Dibatalkan
- Eksperimen bingkai 90% layar dibatalkan; antarmuka kembali memakai lebar
  penuh viewport.

## [0.0.0] - 2026-11-15 17:25 WIB

### Ditambahkan
- Inisialisasi proyek: kerangka Laravel + Inertia + React, konfigurasi
  database, dan struktur direktori aplikasi.
