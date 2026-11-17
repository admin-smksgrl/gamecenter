# Rencana Materi Game — SMA & SMK

**Disusun:** 16 November 2026
**Status:** 🟡 Kelas X hampir tuntas: 54 chapter / 1.620 soal (Matematika 13, Informatika 8, Bahasa Indonesia 5, Bahasa Inggris 6, IPA 8, Pancasila 4, PAI 10). Berikutnya: IPS X (8 bab), lalu sisa Kelas X dan Fase F.
**Cakupan:** Fase E (Kelas 10) dan Fase F (Kelas 11–12), jenjang SMA & SMK
**Sumber data:** `data/kurmer/SMKSMA/` (BUKU AJAR, CP, ATP, KKTP, MAPEL, PROSEM, PROTA)

---

## 1. Ringkasan Eksekutif

Game Center saat ini punya 5 chapter dan 82 soal — cukup untuk membuktikan
mesin game bekerja, tetapi belum mencerminkan kurikulum SMA/SMK yang sebenarnya.
Folder `data/kurmer/SMKSMA/` berisi **451 berkas** kurikulum resmi (88 buku ajar
PDF, 196 modul ajar, 48 CP, 29 ATP, 30 KKTP, 30 PROSEM, 30 PROTA).

Rencana ini mengubah materi dari "contoh" menjadi **materi yang benar-benar
mengikuti capaian pembelajaran**, dengan batasan realistis: tidak semua mapel
dikerjakan sekaligus.

### Keputusan inti

| Keputusan | Alasan |
|---|---|
| **Mulai dari 6 mapel wajib**, bukan 30+ mapel | Sumber daya terbatas; mapel wajib dinikmati semua siswa |
| **Kelas 10 lebih dulu**, lalu 11, lalu 12 | Fase E adalah pintu masuk; kontennya paling lengkap di folder sumber |
| **Satu chapter = satu modul ajar** | Modul ajar sudah punya tujuan pembelajaran siap pakai |
| **3 tingkat kesulitan per chapter** (Mudah/Sedang/Sulit) | Sudah didukung `Difficulty` enum: 5/10/15 soal, 10/20/30 poin |
| **Setiap chapter wajib punya materi + 3 asesmen** | Agar tidak ada chapter "kosong soal" seperti kondisi sekarang |
| **Soal minimal 30% bertipe non-pilihan-ganda** | Memanfaatkan `drag_drop`, `matching`, `puzzle`, `simulation` yang sudah ada |

---

## 2. Analisis Sumber Data

### 2.1 Isi folder `data/kurmer/SMKSMA/`

| Folder | Jumlah berkas | Kegunaan untuk kita |
|---|---|---|
| `BUKU AJAR/` | 88 PDF (Kelas X, XI, XII) | Sumber teks & latihan; rujukan `source_reference` |
| `CP/` | 48 docx (Fase E & F) | **Capaian pembelajaran** → dasar tujuan chapter |
| `ATP/` | 29 docx | **Alur tujuan pembelajaran** → urutan chapter |
| `KKTP/` | 30 docx | Kriteria ketercapaian → ambang `passing_score` |
| `MAPEL/` | 196 docx/pdf (modul ajar) | **Sumber utama**: tujuan pembelajaran per bab |
| `PROSEM/` | 30 docx | Semester & alokasi waktu → `estimated_minutes` |
| `PROTA/` | 30 docx | Program tahunan → cakupan per tahun |

### 2.2 Struktur yang ditemukan

**Fase E (Kelas 10)** — 10 mapel, 92 modul ajar:

| Mapel | Modul | Mapel | Modul |
|---|---|---|---|
| Matematika | 20 | PAI & Budi Pekerti | 10 |
| Pendidikan Pancasila | 19 | Informatika | 9 |
| IPA (Fisika/Biologi/Kimia) | 8 | Bahasa Inggris | 6 |
| Bahasa Indonesia | 6 | IPS (Sejarah/Sosiologi/Ekonomi/Geografi) | 4 |
| Pemrograman Dasar | 0 (hanya PDF) | | |

**Fase F (Kelas 11–12)** — 16 mapel, 104 modul ajar, sudah dipisah per bidang:
Matematika, Biologi, Fisika, Kimia, Ekonomi, Geografi, Sejarah, Sosiologi,
Informatika, PAI, Pancasila, PJOK, Bahasa Indonesia, Bahasa Inggris (reguler &
tingkat lanjut), Bahasa Indonesia tingkat lanjut.

### 2.3 Contoh isi modul ajar (nyata, dari `MA 1.1 Eksponen.docx`)

Modul ajar memuat blok yang bisa langsung dipetakan ke skema kita:

| Blok modul ajar | Kolom tujuan |
|---|---|
| Judul bab ("EKSPONEN DAN LOGARITMA") | `chapters.title` |
| Kode ("MA 1.1") | `chapters.code` |
| Fase / Kelas | `chapters` + `subjects.class_room_id` |
| Prediksi Alokasi Waktu ("2 JP") | `chapters.estimated_minutes` |
| **A. Tujuan Pembelajaran** (4 butir) | `chapters.learning_objectives` (JSON) |
| Kompetensi Awal | `learning_materials.content` (pemantik) |
| Pertanyaan Pemantik | `learning_materials.content` |
| Kegiatan Pembelajaran | `learning_materials` per pertemuan |

Ini bukti bahwa **satu modul ajar = satu chapter** adalah pemetaan yang wajar,
bukan pemaksaan.

### 2.4 Daftar judul modul yang terbaca (sampel terverifikasi)

**Matematika Fase E** (20 modul): Eksponen; Logaritma; Barisan; Deret; Notasi &
Jenis Vektor; Vektor dan Sistem Koordinat; Operasi Vektor; Pemanfaatan
Perbandingan Trigonometri; Sistem Persamaan Linear; Sistem Pertidaksamaan
Linear; Karakteristik Fungsi Kuadrat; Mengkonstruksi Fungsi Kuadrat;
Menyelesaikan Masalah dengan Fungsi Kuadrat; Histogram; Frekuensi Relatif;
Ukuran Pemusatan; Ukuran Penempatan; Ukuran Penyebaran; Distribusi Peluang;
Aturan Penjumlahan.

**Fisika Fase F** (12 modul): Alat Optik; Dinamika Rotasi; Elastisitas; Fluida
Dinamis; Fluida Statis; Gelombang Berjalan dan Stasioner; Gelombang Bunyi dan
Cahaya; Karakteristik Gelombang; Pemanasan Global; Suhu dan Kalor; Teori Kinetik
Gas; Termodinamika.

**Biologi Fase F** (15 modul): Struktur dan Fungsi Sel; Membran Sel; Jaringan
Meristem; Jaringan Hewan; Sistem Ekskresi; Sistem Pencernaan; Sistem Pernapasan;
Sistem Sirkulasi; Sistem Pertahanan Tubuh; Sistem Gerak; Sistem Saraf; Sistem
Reproduksi; Prinsip Reproduksi Manusia; Psikotropika.

---

## 3. Kondisi Saat Ini vs Target

### 3.1 Kondisi sekarang

```
Chapter: 5
  1. Matematika (judul kosong)         — soal uji mesin
  2. Mengenal Bentuk & Warna           — PAUD/TK
  3. Numerasi Awal                     — PAUD/TK
  4. Matematika                        — tanpa judul
  5. Pemrograman Dasar                 — SMP/SMK
Soal: 82
Mapel SMA/SMK terdaftar: 30 (Fase E & F) — sebagian besar kosong
```

Masalah: 30 mapel SMA/SMK sudah ada di database tetapi **hampir semuanya tanpa
chapter dan tanpa soal**. Siswa SMA/SMK yang masuk akan menemukan mapel kosong.

### 3.2 Target akhir rencana ini

```
Chapter SMA/SMK: 79
  Kelas 10 (Fase E): 43 chapter / 13 mapel
  Kelas 11 (Fase F): 24 chapter / 6 mapel
  Kelas 12 (Fase F): 12 chapter / 6 mapel
Soal: 2.370 (79 chapter × 30 soal)
Asesmen: 237 (79 chapter × 3 tingkat)
Materi bacaan: 237 (79 chapter × 3 bagian)
```

Catatan: folder sumber Fase E hanya berisi 9 mapel, tetapi IPA dan IPS dipecah
menjadi mapel terpisah (Fisika/Kimia/Biologi dan
Sejarah/Sosiologi/Ekonomi/Geografi), sehingga jumlah mapel nyata menjadi 13.

**Aritmetika target soal:** tiap chapter punya 3 asesmen (Mudah 5, Sedang 10,
Sulit 15 soal) = 30 soal/chapter. 79 × 30 = **2.370 soal**.

Itu angka besar. Karena itu rencana dibagi menjadi 5 tahap yang masing-masing
sudah bernilai dan bisa berhenti kapan saja tanpa merusak yang lain (§6).

---

## 4. Pemetaan ke Skema Database

Tidak ada migrasi baru yang dibutuhkan — semua kolom sudah tersedia.

| Kebutuhan rencana | Tabel.kolom | Catatan |
|---|---|---|
| Judul bab | `chapters.title` | dari judul modul ajar |
| Kode bab | `chapters.code` | `"MA 1.1"`, `"FIS 3.2"` |
| Tujuan pembelajaran | `chapters.learning_objectives` (JSON) | array string, disalin dari modul |
| Estimasi waktu | `chapters.estimated_minutes` | JP × 45 menit |
| Rujukan buku | `learning_materials.source_reference` | `"BS Matematika KLS X hal. 12"` |
| Materi bacaan | `learning_materials.content` | Markdown |
| Blok game | `learning_materials.blocks` (JSON) | untuk tipe `game` |
| Tingkat kesulitan | `assessments.difficulty` | `easy` / `medium` / `hard` |
| Ambang lulus | `assessments.passing_score` | dari KKTP, default 70 |
| Soal | `questions.question` | teks |
| Opsi | `questions.options` (JSON) / `question_options` | lihat §4.1 |
| Kunci | `questions.correct_answer` (JSON) | bentuk per tipe |

### 4.1 Bentuk `correct_answer` per tipe soal

Wajib konsisten, karena mesin penilaian membaca JSON ini:

| `type` | `options` | `correct_answer` |
|---|---|---|
| `multiple_choice` | — (pakai `question_options`) | `{"text": "8"}` |
| `multiple_answer` | — | `{"texts": ["A", "C"]}` |
| `drag_drop` | `{"items":[{id,text}], "targets":[{id,label}]}` | `{"map": {"itemId": "targetId"}}` |
| `matching` | `{"pairs":[{id,left,right}]}` | `{"map": {"leftId": "rightId"}}` |
| `puzzle` | `{"pieces":[{id,text}]}` | `{"order": ["a","b","c"]}` |
| `simulation` | `{"params":{...}, "goal":{...}}` | `{"expected": {...}}` |
| `essay` | — | `null` + `rubric` |

### 4.2 Konvensi penulisan soal (wajib)

1. **Bahasa Indonesia baku**, kalimat maksimal 25 kata.
2. **Satu soal = satu konsep.** Jangan gabung dua pertanyaan.
3. `explanation` **wajib** — menjelaskan *mengapa*, bukan mengulang jawaban.
4. `hint` diisi untuk `easy` & `medium`; `hard` tanpa hint (sesuai
   `Difficulty::hintAvailable()`).
5. **Poin mengikuti enum**: easy 10, medium 20, hard 30.
6. **Waktu mengikuti enum**: easy 90 s, medium 75 s, hard 60 s per soal.
7. Simbol matematika memakai Unicode (`²`, `×`, `÷`, `√`, `≤`), bukan LaTeX —
   renderer saat ini belum memproses LaTeX.
8. Tidak ada soal yang jawabannya bisa ditebak dari panjang opsi.

---

## 5. Struktur Materi per Chapter

Setiap chapter punya **pola baku** yang sama, supaya siswa mengenali ritmenya
dan guru mudah memeriksa:

```
Chapter
├─ 1. Materi: "Mengapa ini penting"     (type: text, 3–5 menit baca)
├─ 2. Materi: "Konsep inti"             (type: text, 5–8 menit)
├─ 3. Materi: "Contoh & latihan"        (type: interactive, 3–5 menit)
├─ 4. Asesmen Mudah    (5 soal,  10 poin/soal, 90 s/soal, lulus 60)
├─ 5. Asesmen Sedang   (10 soal, 20 poin/soal, 75 s/soal, lulus 70)
└─ 6. Asesmen Sulit    (15 soal, 30 poin/soal, 60 s/soal, lulus 80)
```

**Alasan urutan ini:** siswa membaca dulu (menurunkan frustrasi), lalu
mengerjakan yang mudah (membangun keyakinan), baru naik. Ambang lulus naik
seiring kesulitan agar "sulit" benar-benar berarti.

---

## 6. Tahapan Implementasi

Setiap tahap **berdiri sendiri** — bisa dirilis dan dinikmati siswa walau tahap
berikutnya belum dikerjakan.

### Tahap 0 — Fondasi & alat bantu ✅ SELESAI (16 Nov 2026)

- [x] `php artisan gamecenter:materi-import` — importer JSON → DB
      (idempoten, `updateOrCreate`, dibungkus transaksi).
- [x] Skema JSON materi + validasi berlapis (`MateriSchema`).
- [x] Seeder `SmaSmkMaterialSeeder` yang membaca folder JSON tersebut.
- [x] Tes: importer idempoten (jalankan 2×, jumlah baris tidak bertambah).
- [x] Halaman admin Filament **Materi → Chapter materi** untuk meninjau
      chapter, materi, dan seluruh soal beserta kuncinya.

**Keluaran:** jalur produksi materi ✓ + satu chapter percontoh (MA 1.1 Eksponen,
30 soal) sebagai patokan mutu.

#### Rincian implementasi

| Berkas | Fungsi |
|---|---|
| `app/Services/Materi/MateriImporter.php` | Logika impor idempoten (dipakai command & seeder) |
| `app/Services/Materi/MateriSchema.php` | Pemeriksa skema; menolak berkas cacat sebelum menulis |
| `app/Services/Materi/MateriValidationException.php` | Galat berisi daftar masalah per lokasi |
| `app/Services/Materi/MateriImportResult.php` | Ringkasan hasil impor (created/updated) |
| `app/Console/Commands/MateriImportCommand.php` | `gamecenter:materi-import [path] [--dry-run]` |
| `database/seeders/SmaSmkMaterialSeeder.php` | Impor seluruh JSON saat `db:seed` |
| `app/Filament/Resources/Chapters/ChapterResource.php` | Halaman tinjau hanya-baca |
| `tests/Feature/MateriImportCommandTest.php` | 12 tes |

#### Aturan yang ditegakkan validator

Validator **menolak** berkas bila:
- `title`, `learning_objectives`, atau `content` kosong;
- soal tanpa `explanation` (plan §9 butir 4);
- soal `hard` diberi `hint` (plan §4.2 butir 4);
- pilihan ganda tidak punya tepat satu kunci;
- pilihan ganda kompleks punya kurang dari dua kunci;
- tipe `drag_drop`/`matching`/`puzzle`/`simulation` tanpa `payload`/`correct`;
- ada dua chapter atau dua tingkat kesulitan dengan slug/nama sama.

Bila satu berkas bermasalah, **tidak ada satu baris pun** yang ditulis.

#### Catatan penting: konflik dengan data demo

`DemoContentSeeder` membuat chapter **Eksponen** pada mapel yang sama
(SMA kelas 10 Matematika). Karena materi sesungguhnya menempati chapter itu,
keduanya tidak boleh disemai bersama — setiap `db:seed` berulang akan
melipatgandakan baris materi (ditemukan oleh tes idempotensi).

Keputusan: `DemoContentSeeder` **dikeluarkan dari `DatabaseSeeder`** dan tetap
tersedia sebagai fixture tes lewat `Tests\Concerns\SeedsDemoContent`.

#### Perintah

```bash
php artisan gamecenter:materi-import --dry-run   # periksa skema saja
php artisan gamecenter:materi-import             # impor semua berkas
php artisan gamecenter:materi-import fase-e/sma-kelas-10-matematika.json
```

Semua perintah aman diulang.

### Tahap 1 — Kelas 10, Matematika + Informatika + Bahasa Indonesia ✅ SELESAI (16 Nov 2026)

Paling berdampak: dua mapel dengan mesin game paling cocok (angka & logika).

| Chapter | Kode | Jml | Soal |
|---|---|---|---|
| Eksponen | MA 1.1 | 1 | 30 |
| Logaritma | MA 1.2 | 1 | 30 |
| Barisan | MA 2.1 | 1 | 30 |
| Deret | MA 2.2 | 1 | 30 |
| Sistem Persamaan Linear | MA 5.1 | 1 | 30 |
| Karakteristik Fungsi Kuadrat | MA 6.1 | 1 | 30 |
| Mengkonstruksi Fungsi Kuadrat | MA 6.2 | 1 | 30 |
| Menyelesaikan Masalah Fungsi Kuadrat | MA 6.3 | 1 | 30 |
| Berpikir Komputasional | INF 1 | 1 | 30 |
| Teknologi Informasi dan Komunikasi | INF 2 | 1 | 30 |
| Sistem Komputer | INF 3 | 1 | 30 |
| **Total** | | **11** | **330** |

**Keluaran:** 11 chapter / 330 soal. Kelas 10 Matematika & Informatika terisi penuh.

### Tahap 1c — IPA Kelas 10 (Fisika, Kimia, Biologi) ✅ SELESAI (16 Nov 2026)

Buku IPA Kelas 10 adalah buku **terpadu** berisi 8 bab yang mencakup tiga
disiplin. Setiap bab dipetakan ke mapel sesuai disiplin dominannya.

| Kode | Chapter | Buku | Modul ajar | Mapel | Soal |
|---|---|---|---|---|---|
| FIS 1 | Sistem Pengukuran dalam Kerja Ilmiah | Bab I | Bab 1 | Fisika | 30 |
| BIO 1 | Virus dan Peranannya | Bab II | Bab 2 | Biologi | 30 |
| KIM 1 | Struktur Atom dan Nanoteknologi | Bab III | Bab 5 | Kimia | 30 |
| KIM 2 | Hukum Dasar Kimia di Sekitar Kita | Bab IV | Bab 4 | Kimia | 30 |
| KIM 3 | Kimia Hijau dalam Pembangunan Berkelanjutan 2030 | Bab V | Bab 3 | Kimia | 30 |
| BIO 2 | Keanekaragaman Makhluk Hidup, Interaksi, dan Peranannya di Alam | Bab VI | Bab 7 | Biologi | 30 |
| FIS 2 | Usaha, Energi, dan Energi Terbarukan | Bab VII | Bab 6 | Fisika | 30 |
| BIO 3 | Perubahan Iklim | Bab VIII | Bab 8 | Biologi | 30 |
| **Total** | | | | | **240** |

> **Penting:** nomor modul ajar **tidak** sama dengan nomor bab buku
> (modul Bab 5 → buku Bab III; modul Bab 6 → buku Bab VII). Pemetaan
> disimpan pada `source_reference` setiap chapter agar dapat dilacak.

**Catatan ekstraksi:** modul ajar IPA tersedia dalam format `.doc` (OLE2),
bukan `.docx`. Ekstraksi dilakukan dengan dekode UTF-16LE pada aliran teks
biner; sebagian berkas mengandung *run* teks campuran sehingga tujuan
pembelajaran dipulihkan dengan regex pada kata kerja operasional
(Mengidentifikasi, Menganalisis, Mendeskripsikan, dan seterusnya).

Seluruh **8 dari 8 bab** buku IPA Kelas 10 kini terwakili.

**Realisasi (16 Nov 2026).** Semua chapter di atas sudah diimpor dan tayang.

| Berkas | Chapter | Materi | Soal |
|---|---|---|---|
| `fase-e/matematika/ma-1.1-eksponen.json` | MA 1.1 Eksponen | 3 | 30 |
| `fase-e/matematika/ma-1.2-logaritma.json` | MA 1.2 Logaritma | 3 | 30 |
| `fase-e/matematika/ma-2.1-barisan.json` | MA 2.1 Barisan | 3 | 30 |
| `fase-e/matematika/ma-2.2-deret.json` | MA 2.2 Deret | 3 | 30 |
| `fase-e/matematika/ma-5.1-spl.json` | MA 5.1 Sistem Persamaan Linear | 3 | 30 |
| `fase-e/matematika/ma-6.1-karakteristik-fungsi-kuadrat.json` | MA 6.1 | 3 | 30 |
| `fase-e/matematika/ma-6.2-membentuk-mengubah-bentuk.json` | MA 6.2 | 3 | 30 |
| `fase-e/matematika/ma-6.3-menyelesaikan-masalah.json` | MA 6.3 | 3 | 30 |
| `fase-e/informatika/inf-1-berpikir-komputasional.json` | INF 1 | 3 | 30 |
| `fase-e/informatika/inf-2-tik.json` | INF 2 | 3 | 30 |
| `fase-e/informatika/inf-3-sistem-komputer.json` | INF 3 | 3 | 30 |
| **Total** | **11 chapter** | **33** | **330** |

**Catatan penyesuaian nama.** Chapter INF 2 memakai judul asli modul sumber,
yaitu **Teknologi Informasi dan Komunikasi** (bukan "Algoritma &
Pemrograman"). Alasannya: modul Bab 3 pada `data/kurmer/SMKSMA` memang berisi
integrasi aplikasi perkantoran, sedangkan Algoritma & Pemrograman berada di
Bab 7 (Tahap berikutnya).

**Tujuan pembelajaran** diambil langsung dari `I.TUJUAN PEMBELAJARAN` tiap
modul ajar, bukan ditulis ulang, sehingga chapter dapat dipertanggungjawabkan
ke sumber Kurikulum Merdeka.

**Sebaran tipe soal:** pilihan ganda 265, jawaban ganda 23, menjodohkan 13,
seret-lepas 19, susun urutan 10. Komposisi per chapter tetap 5 mudah /
10 sedang / 15 sulit.

**Pemeriksaan kualitas yang dijalankan:**
1. Skrip pembanding menghitung ulang jawaban soal hitungan; **9 kunci jawaban
   keliru** ditemukan dan diperbaiki — MA 2.1 ×2 (satu soal datanya tidak
   konsisten sehingga ditulis ulang), MA 2.2 ×3, MA 5.1 ×3, MA 6.3 ×1.
2. Audit struktur: 0 soal tanpa penjelasan, 0 hint pada soal sulit, 0 karakter
   U+FFFD, 0 perintah LaTeX, 0 spasi ganda.
3. Impor dua kali → `0 baru / 11 diperbarui`, jumlah baris tidak berubah.
4. Dua tes regresi baru mengunci kelengkapan 11 chapter dan cakupan tipe soal.

**Sisa pekerjaan opsional pada tahap ini:** menambahkan 1–2 soal bertipe
`simulation` per chapter (rencana §8) — saat ini belum ada.

### Tahap 2 — Kelas 10, IPA + Bahasa (2 minggu)

| Mapel | Chapter | Soal |
|---|---|---|
| Fisika | Pengukuran; Gerak Lurus; Hukum Newton | 90 |
| Kimia | Struktur Atom; Ikatan Kimia; Hukum Dasar Kimia | 90 |
| Biologi | Keanekaragaman Hayati; Virus; Klasifikasi | 90 |
| Bahasa Indonesia | Teks Argumentasi; Teks Eksposisi; Teks Naratif | 90 |
| Bahasa Inggris | Descriptive Text; Narrative Text; Procedure Text | 90 |

**Keluaran:** +15 chapter / 450 soal. Total 26 chapter / 780 soal.

### Tahap 3 — Kelas 10, IPS + Pancasila + PAI (1½ minggu)

| Mapel | Chapter | Soal |
|---|---|---|
| Sejarah | Konsep Sejarah; Manusia & Ruang; Peradaban Awal | 90 |
| Sosiologi | Individu & Masyarakat; Interaksi Sosial; Nilai & Norma | 90 |
| Ekonomi | Kelangkaan; Permintaan & Penawaran; Pasar | 90 |
| Geografi | Peta & Penginderaan; Bumi & Antroposfer | 60 |
| Pendidikan Pancasila | Pancasila; UUD 1945; Bhinneka Tunggal Ika | 90 |
| PAI & Budi Pekerti | Al-Qur'an; Akidah; Akhlak | 90 |

**Keluaran:** +17 chapter / 510 soal. **Kelas 10 lengkap (43 chapter / 1.290 soal).**

### Tahap 4 — Kelas 11 (Fase F) (2 minggu)

Enam mapel, 4 chapter masing-masing, 24 chapter / 720 soal:

| Mapel | Chapter |
|---|---|
| Matematika | Barisan & Deret Lanjut; Fungsi Komposisi & Invers; Limit; Turunan |
| Fisika | Fluida Statis; Suhu & Kalor; Gelombang; Termodinamika |
| Biologi | Struktur & Fungsi Sel; Sistem Sirkulasi; Sistem Pencernaan; Sistem Saraf |
| Ekonomi | Pendapatan Nasional; Inflasi; APBN; Perpajakan |
| Sejarah | Kolonialisme; Pergerakan Nasional; Proklamasi; Mempertahankan Kemerdekaan |
| Informatika | Analisis Data; Algoritma Lanjut; Dampak Sosial Informatika; Jaringan |

### Tahap 5 — Kelas 12 (Fase F) (1½ minggu)

6 mapel × 2 chapter = 12 chapter / 360 soal, fokus **persiapan ujian**:

| Mapel | Chapter |
|---|---|
| Matematika | Dimensi Tiga; Peluang Lanjut |
| Fisika | Listrik Statis; Induksi Elektromagnetik |
| Biologi | Genetika; Bioteknologi |
| Bahasa Indonesia | Teks Editorial; Karya Ilmiah |
| Bahasa Inggris | Analytical Exposition; Report Text |
| Informatika | Kecerdasan Artifisial; Proyek Akhir |

---

## 7. Total Akumulasi

| Tahap | Chapter | Soal | Kumulatif chapter | Kumulatif soal |
|---|---|---|---|---|
| 0 | — | — | 0 | 0 |
| 1 | 11 | 330 | 11 | 330 |
| 2 | 15 | 450 | 26 | 780 |
| 3 | 17 | 510 | **43** | **1.290** |
| 4 | 24 | 720 | 67 | 2.010 |
| 5 | 12 | 360 | **79** | **2.370** |

---

## 8. Sebaran Tipe Soal

Agar game tidak monoton, tiap 30 soal per chapter wajib memenuhi:

| Tipe | Persentase | Jumlah/chapter | Contoh pemakaian |
|---|---|---|---|
| `multiple_choice` | 40% | 12 | hasil hitung, definisi |
| `multiple_answer` | 20% | 6 | ciri-ciri, faktor |
| `matching` | 15% | 4–5 | istilah ↔ pengertian |
| `drag_drop` | 12% | 3–4 | urutan langkah, klasifikasi |
| `puzzle` | 8% | 2–3 | susun kalimat/rumus |
| `simulation` | 5% | 1–2 | geser variabel, lihat hasil |

`essay` **tidak dipakai** di tahap ini karena menuntut penilaian AI dan rubrik
manual — masuk rencana terpisah agar tidak memblokir rilis.

---

## 9. Standar Mutu Isi

Sebelum chapter dianggap selesai, semua syarat ini harus terpenuhi:

1. **Rujukan nyata** — `source_reference` menunjuk buku/halaman yang benar-benar
   ada di `BUKU AJAR/`.
2. **Tujuan dari CP** — `learning_objectives` disalin dari modul ajar, bukan
   dikarang.
3. **Tidak ada soal duplikat** — diperiksa dengan pembanding teks ternormalisasi.
4. **Semua soal punya `explanation`.**
5. **Kunci jawaban diverifikasi** oleh minimal 1 guru mapel.
6. **Kesulitan bertingkat nyata** — soal `hard` tidak boleh sekadar soal `easy`
   dengan angka berbeda; harus menuntut langkah majemuk.
7. **Tidak ada salah ketik** — melewati pemeriksa ejaan + baca ulang.

---

## 10. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| 2.370 soal terlalu banyak untuk ditulis manual | Proyek berhenti di tengah | Tahap 1–3 sudah lengkap untuk Kelas 10; sisanya opsional |
| Soal dibuat AI tanpa verifikasi | Siswa belajar hal salah | Wajib review guru per chapter (§9 butir 5) |
| Modul ajar berisi "..." (tidak lengkap) | Tujuan pembelajaran kosong | Fallback ke CP/ATP untuk mapel tersebut |
| Materi terlalu padat untuk format game | Siswa bosan | Batas 3–5 menit baca per bagian (§5) |
| Chapter mapel SMK kejuruan tidak ada di sumber | Cakupan SMK pincang | Rencana ini fokus mapel **umum**; mapel kejuruan jadi rencana terpisah |
| Simbol matematika rusak saat render | Soal tidak terbaca | Wajib Unicode, dilarang LaTeX (§4.2 butir 7) |

---

## 11. Kriteria Selesai (Definition of Done)

Sebuah chapter dinyatakan selesai bila **semua** terpenuhi:

- [ ] 3 materi bacaan tersimpan dan tampil di aplikasi.
- [ ] 3 asesmen (Mudah/Sedang/Sulit) dengan 5/10/15 soal.
- [ ] Setiap soal punya `explanation`; `easy`/`medium` punya `hint`.
- [ ] Sebaran tipe soal memenuhi §8.
- [ ] Lolos uji main: satu sesi penuh tiap tingkat tanpa error.
- [ ] Lolos review guru (§9 butir 5).
- [ ] Muncul di `/progres` siswa setelah dikerjakan.

---

## 12. Struktur Berkas yang Akan Dibuat

```
database/seeders/data/sma-smk/
├─ fase-e/
│  ├─ matematika.json
│  ├─ informatika.json
│  ├─ fisika.json
│  ├─ kimia.json
│  ├─ biologi.json
│  ├─ bahasa-indonesia.json
│  ├─ bahasa-inggris.json
│  ├─ sejarah.json
│  ├─ sosiologi.json
│  ├─ ekonomi.json
│  ├─ geografi.json
│  ├─ pendidikan-pancasila.json
│  └─ pai-budi-pekerti.json
└─ fase-f/
   ├─ kelas-11/*.json
   └─ kelas-12/*.json
```

Bentuk satu berkas JSON (satu mapel):

```json
{
  "subject": "Matematika",
  "class_room": "Kelas 10",
  "phase": "E",
  "chapters": [
    {
      "code": "MA 1.1",
      "title": "Eksponen",
      "learning_objectives": [
        "Mengidentifikasi sifat-sifat eksponen.",
        "Mengidentifikasi bentuk akar.",
        "Menyelesaikan masalah sehari-hari dengan fungsi eksponen."
      ],
      "estimated_minutes": 90,
      "source_reference": "BS Matematika KLS X hal. 12",
      "materials": [
        { "title": "Mengapa ini penting", "type": "text", "content": "..." },
        { "title": "Konsep inti", "type": "text", "content": "..." },
        { "title": "Contoh & latihan", "type": "interactive", "content": "..." }
      ],
      "assessments": [
        {
          "difficulty": "easy",
          "passing_score": 60,
          "questions": [
            {
              "type": "multiple_choice",
              "question": "Berapakah hasil dari 2³ × 2²?",
              "options": [
                { "label": "A", "text": "2⁵", "is_correct": true },
                { "label": "B", "text": "2⁶", "is_correct": false },
                { "label": "C", "text": "4⁵", "is_correct": false },
                { "label": "D", "text": "4⁶", "is_correct": false }
              ],
              "explanation": "Pangkat dijumlahkan saat basis sama: 2³⁺² = 2⁵.",
              "hint": "Basisnya sama, jadi jumlahkan pangkatnya.",
              "points": 10,
              "time_limit": 90
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 13. Langkah Berikutnya

1. ~~**Setujui cakupan mapel**~~ — Tahap 1 tetap Matematika + Informatika
   (11 chapter / 330 soal) sampai diputuskan lain.
2. ~~**Kerjakan Tahap 0**~~ ✅ selesai. Importer, validator, seeder, tes, dan
   halaman tinjau sudah ada, sehingga Tahap 1–5 kini hanya pekerjaan mengisi
   JSON.
3. ~~**Tulis 1 chapter percontoh**~~ ✅ MA 1.1 Eksponen (3 materi, 30 soal:
   5 mudah / 10 sedang / 15 sulit) sudah masuk.
4. ~~**Kerjakan Tahap 1**~~ ✅ selesai (16 Nov 2026). 10 chapter baru
   (7 Matematika + 3 Informatika) sudah diimpor; total 11 chapter / 330 soal.
5. **(Sekarang) Review guru** atas 11 chapter Kelas 10 — terutama kunci
   jawaban, ketepatan tingkat kesulitan, dan kesesuaian bahasa dengan siswa.
   Catatan perbaikan dikirim ke berkas JSON lalu diimpor ulang; halaman admin
   hanya untuk meninjau.
6. ~~**Bahasa Inggris X**~~ ✅ selesai (18 Nov 2026): 6 chapter / 180 soal,
   termasuk ENG 6 Fractured Stories (3 materi, 30 soal, 8 checkpoint,
   skenario dan tantangan).
7. **Opsional:** tambahkan 1–2 soal `simulation` per chapter agar sesuai
   rencana §8.
8. **(Berikutnya) IPS X** — 8 bab dari `IPS_BG_KLS_X_Rev.pdf`, dipetakan ke
   empat mapel (Sejarah, Sosiologi, Ekonomi, Geografi). Mapel `ips` sudah
   didaftarkan pada `SubjectSeeder` untuk Kelas X dan siap menerima chapter.
9. **Lalu sisa Kelas X:** PJOK, Prakarya, Kepercayaan, Projek IPAS, mapel
   kejuruan SMK; setelah itu Kelas XI dan XII.
