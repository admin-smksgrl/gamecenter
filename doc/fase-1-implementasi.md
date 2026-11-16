# Laporan Implementasi — Fase 1: Setup & Database

**Tanggal:** 15 November 2026
**Lokasi proyek:** `C:\laragon\www\gamecenter\gamecenter`
**Status:** ✅ Selesai — aplikasi berjalan di `http://gamecenter.test`, database terisi, 19 test otomatis lulus.

---

## 1. Ringkasan

Fase 1 membangun fondasi teknis Game Center Edukasi: kerangka Laravel 13 dengan
Inertia + React, panel admin Filament 5, autentikasi Sanctum, skema database
kurikulum lengkap, model Eloquent, serta data awal untuk seluruh jenjang dan
mata pelajaran SMA/SMK. Sebagai bukti pipeline konten, satu bab nyata
(**Matematika Kelas 10 — Eksponen**) sudah diisi materi, tiga tingkat assessment,
dan 17 soal.

## 2. Versi yang terpasang

| Paket | Versi |
|-------|-------|
| PHP | 8.3.13 |
| Laravel Framework | 13.42.0 |
| Inertia Laravel | 3.7.0 |
| Laravel Sanctum | 4.4.0 |
| Filament | 5.11.3 |
| Livewire | 4.4.8 |
| React / React DOM | 19.3.1 |
| TypeScript | 7.0.2 |
| Vite | 7.3.8 |
| Tailwind CSS | 4.x |
| Database | MariaDB 11.8.5 (`gamecenter`, utf8mb4) |

## 3. Struktur proyek

```
gamecenter/                     (root aplikasi)
├── app/
│   ├── Enums/                  UserRole, Difficulty, QuestionType,
│   │                           MaterialType, ProgressStatus, SyncStatus
│   ├── Filament/               (siap diisi resource pada fase berikutnya)
│   ├── Http/
│   │   ├── Controllers/        GameCenterController
│   │   └── Middleware/         HandleInertiaRequests, EnsureUserHasRole
│   ├── Models/                 15 model Eloquent
│   └── Providers/Filament/     AdminPanelProvider
├── database/
│   ├── migrations/             15 migrasi domain + 1 migrasi Sanctum
│   ├── seeders/                EducationLevel, Class, Subject, Achievement,
│   │                           DemoContent, User, Database
│   └── factories/              UserFactory (admin/teacher state)
├── resources/js/
│   ├── Layouts/AppLayout.tsx
│   ├── Pages/GameCenter/Index.tsx
│   ├── lib/utils.ts
│   └── types/index.d.ts
├── routes/
│   ├── web.php                 GET /  → GameCenterController@index
│   └── api.php                 GET /api/health, GET /api/user
└── tests/Feature/              GameCenterPageTest, CurriculumSeedTest
```

## 4. Skema database

15 tabel domain, seluruh relasi memakai foreign key dengan `cascadeOnDelete`
(kecuali `users.class_id` yang `nullOnDelete`).

| Tabel | Fungsi | Kolom kunci |
|-------|--------|-------------|
| `education_levels` | Jenjang PAUD/TK/SMP/SMA/SMK | `slug`, `theme`, `order`, `is_active` |
| `classes` | Kelas per jenjang + fase | `education_level_id`, `grade_level`, `phase` |
| `subjects` | Mata pelajaran per kelas | `class_id`, `slug`, `group`, `icon`, `color` |
| `chapters` | Bab materi | `subject_id`, `code`, `learning_objectives` (json) |
| `learning_materials` | Materi (60%) | `type`, `content`, `blocks` (json), `source_reference` |
| `assessments` | Tes (40%) per tingkat | `difficulty` (unique per bab), `duration`, `passing_score` |
| `questions` | Bank soal 7 tipe | `type`, `options`, `correct_answer`, `rubric`, `ai_assisted` |
| `question_options` | Opsi pilihan ganda | `label`, `text`, `is_correct` |
| `users` | Siswa/guru/admin + gamifikasi | `username`, `role`, `class_id`, `xp`, `level`, `coins`, `streak_days` |
| `game_sessions` | Sesi bermain (idempoten) | `client_uuid` (unique), `mode`, `score`, `synced` |
| `session_answers` | Jawaban per soal | unique `(game_session_id, question_id)`, `ai_feedback` |
| `session_results` | Ringkasan hasil sesi | 1:1 dengan sesi, `xp_earned`, `is_passed` |
| `user_progress` | Progres per bab | unique `(user_id, chapter_id)`, `best_score` |
| `achievements` | Katalog lencana | `slug`, `requirement_type`, `xp_reward` |
| `user_achievements` | Lencana yang dibuka | unique `(user_id, achievement_id)` |
| `sync_queue` | Antrian sinkronisasi offline | `client_uuid` (unique), `payload`, `status`, `attempts` |

### Penyimpangan kecil dari rencana awal

| Rencana | Implementasi | Alasan |
|---------|--------------|--------|
| `achievements` = pencapaian user | `achievements` (katalog) + `user_achievements` (pivot) | Lencana bisa dikelola admin, tidak duplikatif |
| `classes` tanpa fase | kolom `phase` (A–F) | Kurikulum Merdeka memetakan kelas → fase |
| `users.email` wajib | `email` nullable, `username` unik | Siswa PAUD/SMP sering tanpa email (UU PDP) |
| 14 tabel | 15 tabel | Tambahan `user_achievements` |

## 5. Model & enum

**Model:** `EducationLevel`, `ClassRoom` (tabel `classes`), `Subject`, `Chapter`,
`LearningMaterial`, `Assessment`, `Question`, `QuestionOption`, `User`,
`GameSession`, `SessionAnswer`, `SessionResult`, `UserProgress`, `Achievement`,
`SyncQueue`.

**Enum (PHP 8.1 backed enums):** `UserRole`, `Difficulty` (dengan aturan jumlah
soal/poin/waktu), `QuestionType`, `MaterialType`, `ProgressStatus`, `SyncStatus`.

**Gamifikasi:** ambang level `1:0 · 2:100 · 3:250 · 4:500 · 5:1000` XP dengan
helper `User::levelForXp()` dan `User::xpToNextLevel()`.

**Akses admin:** `User` mengimplementasikan `FilamentUser`; hanya
`admin`/`teacher` aktif yang boleh masuk `/admin`.

## 6. Data awal (seeder)

| Data | Jumlah |
|------|--------|
| Jenjang | 5 (PAUD, TK, SMP, SMA, SMK) |
| Kelas | 12 (PAUD 1, TK 2, SMP 3, SMA 3, SMK 3) |
| Mata pelajaran | 133 |
| Bab | 1 (Eksponen) |
| Materi | 3 |
| Assessment | 3 (easy, medium, hard) |
| Soal | 17 (15 pilihan ganda + 2 essay) |
| Opsi jawaban | 60 |
| Achievement | 8 |
| Akun demo | 4 |

Seeder bersifat **idempoten** (`updateOrCreate`) sehingga aman dijalankan
berulang — sudah diverifikasi oleh test `test_seeders_are_idempotent`.

### Cakupan mata pelajaran

- **PAUD/TK** — tema perkembangan (bentuk & warna, numerasi awal, literasi awal, seni, motorik).
- **SMP** — 11 mapel wajib (Matematika, IPA, IPS, Bahasa, Informatika, PJOK, Prakarya, Seni, PAI, Pancasila).
- **SMA** — 17 mapel (termasuk Fisika, Kimia, Biologi, Ekonomi, Geografi, Sosiologi, Antropologi).
- **SMK** — 11 mapel (termasuk Projek IPAS dan Pemrograman Dasar khusus kelas 10).

## 7. Endpoint & halaman

| Rute | Keterangan |
|------|------------|
| `GET /` | Halaman jelajah materi (Inertia `GameCenter/Index`) |
| `GET /admin` | Panel Filament (login admin/guru) |
| `GET /api/health` | Health check JSON |
| `GET /api/user` | Profil user via token Sanctum |

### Halaman jelajah materi

Filter bertingkat **jenjang → kelas (dengan fase) → rumpun mapel → pencarian →
mode (mudah/sedang/sulit)**. Setiap entri mapel menampilkan jumlah bab; mapel
dengan bab aktif dapat dibuka untuk melihat daftar bab, jumlah materi, durasi,
dan jumlah soal per mode. Mapel tanpa konten ditandai "Segera".

Data dikirim sekali sebagai props Inertia — pada fase offline-first payload ini
yang akan disimpan ke IndexedDB.

### Arah desain antarmuka

Halaman jelajah memakai **dashboard kartu** bertema **merah maroon, putih, dan
hitam**. Semua blok tampil sebagai kartu putih bersudut bulat di atas latar
putih kemerahan; maroon dipakai untuk aksi dan status aktif. Tanpa gradien,
glassmorphism, atau ornamen dekoratif.

- **Satu layar penuh.** Shell memakai `h-dvh overflow-hidden`; header, kartu
  katalog, dan baris kontrol tetap di tempat, sementara daftar kartu mapel
  menggulir di dalam areanya sendiri. Halaman tidak pernah ikut menggulir.
- **Kartu katalog gabungan.** Satu kartu memuat judul, pencarian, dan strip
  ringkasan: rasio belajar 60:40, alur Baca–Main–XP, serta statistik koleksi
  5 jenjang / 12 kelas / 133 mapel. Cara belajar, alur, dan pemilih jenjang
  tidak lagi berdiri sebagai kartu terpisah.
- **Satu baris kontrol.** Jenjang dan kelas berupa dropdown asli (native select,
  aksesibel), sedangkan mode permainan berupa progress bar tiga segmen yang juga
  dapat diklik. Ketiganya diberi nomor 01–03 dan diletakkan dalam satu baris.
- **Kartu mapel sebagai fokus.** Jumlah kartu menentukan kolom: ≤6 → 3 kolom,
  ≤12 → 4 kolom, >12 → 5 kolom. Tiap kartu minimalis: chip nomor, nama mapel,
  status bab, rumpun, dan jumlah soal dengan panah. Kartu yang belum berisi
  memakai nada redup dan label "Segera"; kartu yang siap dimainkan memakai chip
  maroon dan tautan soal berwarna maroon.
- **Tipografi.** Fraunces Variable untuk judul dan nama mapel; Instrument Sans
  Variable untuk label, angka, dan teks kecil. Keduanya di-host sendiri lewat
  Fontsource sehingga tetap tersedia offline.
- **Panel bab** tampil sebagai drawer di kanan (lebar penuh di ponsel) berisi
  kartu bab, tab mode, dan alur; dapat ditutup dengan `Esc` atau klik latar.
- **Pintasan.** `/` memfokuskan kolom pencarian, `Esc` menutup panel.

Warna dan token didefinisikan di `resources/css/app.css`:

| Token | Nilai | Fungsi |
|-------|-------|--------|
| `--color-paper` | `#f6f1ef` | Latar halaman putih kemerahan |
| `--color-sheet` | `#ffffff` | Permukaan kartu |
| `--color-ink` | `#171114` | Teks utama (hitam) |
| `--color-maroon` | `#74182b` | Aksen, tombol aktif, panel |
| `--color-maroon-deep` | `#4c0d1b` | Hover aksen |
| `--color-maroon-soft` | `#a85163` | Penanda mode sedang |
| `--color-maroon-tint` | `#f6e7ea` | Chip dan latar lembut |
| `--color-rule` | `#e7dcd9` | Garis kartu |

## 8. Verifikasi

```
Tests:    19 passed (140 assertions)
Duration: 6.75s
```

- `GameCenterPageTest` — halaman render, props jenjang/kelas/mapel benar, bab
  Eksponen dan tiga tingkat kesulitan terekspos, API health OK.
- `FilamentAccessTest` — halaman login panel tersedia, admin & guru bisa masuk
  dashboard, siswa dan akun nonaktif ditolak (403).
- `CurriculumSeedTest` — kelengkapan jenjang, mapel inti tiap kelas SMA, struktur
  soal (tepat satu opsi benar), essay ber-flag AI + rubrik, aturan Pemrograman
  Dasar, peran user demo, perhitungan level XP, idempotensi seeder.
- `npm run typecheck` — 0 error.
- `npm run build` — sukses (CSS 56 kB, JS app 364 kB / 115 kB gzip).

## 9. Cara menjalankan

```bash
cd C:\laragon\www\gamecenter\gamecenter
php artisan migrate:fresh --seed
npm install
npm run build
```

Lalu buka **http://gamecenter.test** (Laragon) · panel admin
**http://gamecenter.test/admin** (`admin` / `password`).

Virtual host Laragon diatur di
`C:\laragon\etc\apache2\sites-enabled\auto.gamecenter.test.conf` dengan
`ROOT = C:/laragon/www/gamecenter/gamecenter/public`.

**Catatan lingkungan:** Apache Laragon pada mesin ini memakai PHP 8.5.1
(sedangkan CLI memakai 8.3.13). Seluruh test sudah dijalankan di kedua versi dan
lulus. Antara 15–16 November 2026, MySQL sempat berhenti karena dua instance
`mysqld` saling rebutan `ibdata1`; cukup jalankan MySQL dari panel Laragon
(Start All) satu kali saja dan jangan menjalankan instance kedua.

**Port 443 dipakai layanan lain.** Di mesin pengembangan ini service Dapodik
menempati port 443, sehingga Apache Laragon gagal start dengan
`AH00072: make_sock: could not bind to address [::]:443`. Solusi sementara:
jalankan Apache dengan salinan konfigurasi yang mematikan include SSL.

```powershell
$src = "C:\laragon\bin\apache\httpd-2.4.54-win64-VS16\conf\httpd.conf"
$dst = "$env:TEMP\httpd-gamecenter.conf"
(Get-Content $src) -replace '^Include "C:/laragon/etc/apache2/httpd-ssl.conf"',
  '# disabled: port 443 in use' | Set-Content $dst -Encoding ascii

& "C:\laragon\bin\apache\httpd-2.4.54-win64-VS16\bin\httpd.exe" `
  -d "C:/laragon/bin/apache/httpd-2.4.54-win64-VS16" -f $dst
```

Situs lalu dilayani lewat HTTP di `http://gamecenter.test` (tanpa HTTPS).
Pada mesin lain tanpa konflik port, cukup Start All dari Laragon.

## 10. Catatan untuk fase berikutnya

1. **Fase 2 (Content Ingestion)** — parser DOCX/PDF di `tools/parser`, skema JSON
   mengikuti bentuk `DemoContentSeeder`, lalu impor seluruh mapel SMA/SMK.
2. **Fase 3 (Offline-first)** — payload props Inertia saat ini bisa langsung
   dijadikan sumber cache IndexedDB; `sync_queue` dan `client_uuid` sudah siap
   untuk idempotensi.
3. **Filament resources** — model sudah lengkap, tinggal
   `php artisan make:filament-resource --generate`.
4. **Locale Indonesia** — `APP_LOCALE=id` sudah aktif, tetapi pesan validasi
   bawaan masih Inggris; tambahkan `lang/id/validation.php` bila diperlukan.
5. **Autentikasi siswa** — Sanctum dan middleware `role` siap; halaman
   login/registrasi siswa menyusul bersama UI fase 5.
