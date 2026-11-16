# Game Center Edukasi

Aplikasi game edukasi multi-jenjang (PAUD, TK, SMP, SMA, SMK) berbasis materi resmi
Kemdikdasmen. Offline-first, server ringan, dan siap untuk shared hosting.

**Stack:** Laravel 13 · Inertia.js · React 19 · TypeScript · Tailwind CSS 4 · Vite 7 ·
Filament 5 (admin) · MySQL 8 / MariaDB 10.6+ · Sanctum · Mermaid 12.

---

## Status: Fase 1–4 + keanggotaan + panduan + dashboard admin selesai

Fondasi aplikasi, skema database, model, data awal, sistem keanggotaan, pusat
bantuan, fondasi offline-first, game engine, tema per jenjang, dan halaman
progres sudah berjalan. Siswa dapat bermain dari katalog materi hingga menerima
skor, XP, koin, level, dan lencana, lalu meninjau perkembangan belajarnya.

| Komponen | Status |
|----------|--------|
| Laravel 13 + Inertia + React + TypeScript | ✅ |
| Filament 5 panel (`/admin`) | ✅ |
| Sanctum (SPA + token) | ✅ |
| Migrasi database (17 tabel domain) | ✅ |
| Model Eloquent + relasi + enum | ✅ |
| Seeder jenjang/kelas/mapel (5 jenjang, 12 kelas, 133 mapel) | ✅ |
| Seeder bank soal contoh (5 bab, 82 soal, 3 tingkat) | ✅ |
| Kurasi materi lintas jenjang (PAUD, TK, SMP, SMA, SMK) | ✅ |
| Tema visual per jenjang (ceria, petualangan, penjelajah, fokus) | ✅ |
| Halaman jelajah materi (jenjang → kelas → mapel → mode, pencarian, pagination) | ✅ |
| Menu bermain: sesi pribadi (nama pemain) dan kelompok (nama kelompok + pemain) | ✅ |
| Halaman bermain `/main/{assessment}`: materi, intro, timer, umpan balik, hasil | ✅ |
| Mesin permainan: pilihan ganda/ganda kompleks, urutan, menjodohkan, simulasi, uraian | ✅ |
| Gamifikasi sesi: skor, XP, koin, level, lencana | ✅ |
| Halaman progres `/progres`: statistik, aktivitas, riwayat sesi, lencana | ✅ |
| Halaman hasil `/hasil/{gameSession}`: ringkasan dan pembahasan jawaban | ✅ |
| Mode gelap/terang (toggle topbar, tersimpan otomatis) | ✅ |
| Autentikasi siswa/guru (`/masuk`, `/daftar`) | ✅ |
| Keanggotaan: katalog paket, pengajuan upgrade, riwayat | ✅ |
| Persetujuan pengajuan oleh admin di Filament | ✅ |
| Dashboard admin bertema: statistik, grafik, akses cepat, antrean pengajuan | ✅ |
| Pusat bantuan `/panduan` dengan sidebar, pencarian, TOC, dan diagram Mermaid | ✅ |
| Offline-first: cache IndexedDB, antrean `syncQueue`, PWA + service worker | ✅ |
| API sinkronisasi batch `POST /api/sync` (idempoten, skor server) | ✅ |
| Test otomatis (68 test, 611 assertion) | ✅ |

---

## Desain antarmuka

Halaman jelajah memakai **grid kartu materi** bernuansa **game edukasi modern**
dengan palet dasar **merah bendera Indonesia, putih, dan hitam**. Kanvas putih
hangat berpola titik, kartu putih ringkas, dan aksen merah untuk status aktif.
Ikon emoji tampil berwarna, dan setiap mapel membawa aksen warnanya sendiri
(border kartu + tile ikon) dari kolom `color` di database. Tingkat kesulitan
dibedakan lewat merah/hitam. Fraunces Variable (judul) dan Instrument Sans
Variable (label) di-host sendiri lewat Fontsource agar tetap tampil offline.

- Seluruh halaman muat dalam **satu viewport** (`h-dvh`, tanpa scroll halaman).
  Daftar kartu diatur agar tidak menampilkan scrollbar; pagination menjaga
  jumlah kartu per halaman sesuai tinggi layar.
- **Navigasi ada di topbar:** jenjang, kelas, dan mode permainan berupa menu
  dropdown di bilah atas ( nilai aktif selalu terlihat ), sedangkan pencarian
  berupa tombol ikon yang membuka palet pencarian. Dengan begitu area konten
  sepenuhnya dipakai kartu materi.
- **Kartu mapel adalah fokus utama:** grid **4 kolom** di desktop (3 di tablet,
  2 di ponsel), kartu putih kompak (~125 px) dengan border berwarna sesuai
  mapel, tile ikon senada, nama, kelompok, jumlah bab, dan jumlah soal untuk
  mode aktif. Kartu aktif terangkat saat hover; kartu tanpa konten tetap
  terbaca dengan label "Segera".
- **Pagination di footer:** ringkasan "Menampilkan a–b dari n mapel" dan tombol
  nomor halaman (plus prev/next) menyatu dalam **satu baris footer**, rata
  tengah viewport. Di ponsel ringkasan disingkat `a–b / n` dan pager menjadi
  `‹ halaman / total ›` agar tetap rapi. Halaman otomatis kembali ke 1 saat
  jenjang/kelas/rumpun/pencarian berubah.
- **Footer tipis** di semua halaman: kiri `Ruang belajar v.<versi>` yang dibaca
  otomatis dari heading rilis teratas [`changelog.md`](changelog.md) (single
  source of truth), tengah ringkasan + pagination, kanan kredit
  `created & developed by haraki`.
- **Tanpa kartu statistik:** ringkasan (mapel, bab, soal) tampil sebagai teks
  inline di bawah judul, dan rumpun mapel berupa chip gulir di kanvas.
- Header ringkas memuat identitas aplikasi, tombol **Bermain**, tombol tema,
  tombol cari, chip koin/XP, dan menu akun. Tamu melihat tombol **Masuk**
  (plus **Daftar** di layar lebar); pengguna masuk melihat avatar dengan menu
  Keanggotaan, panel admin/guru sesuai peran, dan Keluar.
- Panel bab tampil sebagai drawer di kanan (lebar penuh di ponsel). Tombol cari
  atau `/` membuka palet pencarian, `Esc` menutup palet/panel.
- **Menu Bermain** (tombol merah di topbar) menawarkan **Main pribadi** — cukup
  tulis nama pemain — dan **Bermain kelompok** — nama kelompok plus 2–8 nama
  pemain dengan tambah/hapus baris. Sesi aktif tampil di tombol topbar (nama
  atau nama kelompok + jumlah pemain) dan bertahan setelah muat ulang karena
  disimpan di `localStorage` (`gamecenter.play-session`). Menu yang sama
  menampilkan ringkasan sesi dan opsi **Akhiri sesi**.
- Palet dasar: `canvas #f5f2f2`, `surface #ffffff`, `ink #171114`,
  `red #e60012`, `red-deep #b8000f`, `red-tint #ffebec`, `rule #e6dfdf` (lihat
  `resources/css/app.css`).
- **Mode gelap/terang:** tombol ikon matahari/bulan di topbar mengganti seluruh
  palet. Preferensi awal mengikuti setelan perangkat (`prefers-color-scheme`),
  lalu pilihan pengguna disimpan di `localStorage` (`gamecenter.theme`) dan
  diterapkan sebelum halaman digambar (tanpa kedip). Palet gelap:
  `canvas #0e0c0d`, `surface #171214`, `ink #f7f1f2`, `rule #2d2629`,
  `red #ff3945`, `red-tint #3b1014`.

---

## Bermain & mesin permainan

Halaman bermain tersedia di **`/main/{assessment}`** dan dibuka lewat tombol
**Main** pada kartu asesmen di panel bab. Alurnya: intro (jumlah soal, waktu,
poin, KKM, progres terbaik) → soal satu per satu → hasil dan tinjauan.

- **Enam mekanik:** pilihan ganda, pilihan ganda kompleks, urutan
  (`drag_drop`/`puzzle`), menjodohkan, simulasi keputusan, dan uraian + rubrik.
- **Umpan balik langsung:** setelah **Periksa jawaban**, pilihan benar/salah
  ditandai, jawaban benar dan penjelasan ditampilkan, lalu soal terkunci.
- **Navigasi:** peta soal untuk berpindah atau meninjau jawaban; timer sesi
  berjalan sejak tombol mulai dan otomatis menutup sesi saat habis.
- **Penilaian:** client menilai untuk umpan balik instan; server tetap
  menghitung ulang soal objektif saat sinkronisasi. Tipe interaktif memakai
  poin client yang dibatasi poin soal. Uraian disimpan tetapi tidak masuk skor
  sampai dinilai guru/AI.
- **Gamifikasi:** skor 0–100, lulus KKM, XP = poin diperoleh, koin = XP ÷ 5,
  level 1–5 (Pemula s.d. Legenda), dan lencana sesi.
- **Offline:** asesmen + soal lengkap disimpan ke IndexedDB; hasil sesi masuk
  `syncQueue` bila pengguna masuk. Tamu tetap bisa bermain dan diarahkan masuk
  agar hasil tersimpan.

Bank soal demo Eksponen berisi **22 soal**: 5 mudah, 8 sedang (termasuk ganda
kompleks + drag & drop), dan 9 sulit (termasuk menjodohkan, puzzle, dan
simulasi). Rincian implementasi ada di
[`../doc/fase-3-implementasi.md`](../doc/fase-3-implementasi.md).

---

## Menjalankan di lokal (Laragon)

1. Jalankan **Laragon** → Start All (Apache + MySQL/MariaDB). PHP 8.3+.
2. Buat database `gamecenter` (utf8mb4) bila belum ada.
3. Salin `.env.example` → `.env`, lalu:
   ```bash
   php artisan key:generate
   php artisan migrate --seed
   npm install
   npm run build
   ```
4. Buka **http://gamecenter.test** (virtual host Laragon).
5. Panel admin: **http://gamecenter.test/admin**.

> **Sanctum & domain lokal:** `.env.example` sudah memuat
> `SANCTUM_STATEFUL_DOMAINS` untuk `gamecenter.test`, `localhost`, dan
> `127.0.0.1` (termasuk port 8000). Bila memakai domain/port lain, tambahkan
> di sana agar `POST /api/sync` memakai sesi cookie SPA, lalu jalankan
> `php artisan config:clear`. Service worker dan PWA hanya aktif dari hasil
> `npm run build` (bukan `npm run dev`).

> **Catatan virtual host:** `gamecenter.test` harus menunjuk ke folder
> `gamecenter/public` (bukan root proyek). Konfigurasi ada di
> `C:\laragon\etc\apache2\sites-enabled\auto.gamecenter.test.conf`:
> ```
> define ROOT "C:/laragon/www/gamecenter/gamecenter/public"
> ```
> Jika Laragon membuat ulang vhost otomatis dan menampilkan daftar folder,
> ubah `ROOT` ke path `public` di atas lalu klik **Reload** pada Laragon.

Alternatif tanpa Laragon: `php artisan serve` → `http://localhost:8000`
(pastikan `APP_URL` disesuaikan).

> **Penting soal folder kerja:** proyek Laravel ada di subfolder `gamecenter`.
> Kalau terminal berada di `C:\laragon\www\gamecenter`, jalankan `serve.bat`
> atau `php artisan serve`. File `artisan` di folder induk otomatis meneruskan
> perintah ke proyek, jadi tidak perlu `cd gamecenter` lebih dulu.
> Panel admin menerima **email atau username** (contoh: `admin` / `password`).
> Semua pemberitahuan di aplikasi tampil sebagai toast berbahasa Indonesia,
> termasuk saat login gagal atau koneksi terputus.

> **Jika Apache gagal start karena port 443 terpakai** (`AH00072: make_sock`),
> layanan lain di mesin ini (mis. Dapodik) sedang memakai HTTPS. Jalankan Apache
> dengan salinan konfigurasi tanpa include SSL:
> ```powershell
> $src = "C:\laragon\bin\apache\httpd-2.4.54-win64-VS16\conf\httpd.conf"
> $dst = "$env:TEMP\httpd-gamecenter.conf"
> (Get-Content $src) -replace '^Include "C:/laragon/etc/apache2/httpd-ssl.conf"',
>   '# disabled: port 443 in use' | Set-Content $dst -Encoding ascii
> & "C:\laragon\bin\apache\httpd-2.4.54-win64-VS16\bin\httpd.exe" `
>   -d "C:/laragon/bin/apache/httpd-2.4.54-win64-VS16" -f $dst
> ```
> Situs tetap dapat diakses lewat `http://gamecenter.test`.

### Akun demo

| Peran | Username / Email | Password |
|-------|------------------|----------|
| Admin | `admin` / `admin@gamecenter.test` | `password` |
| Guru | `guru` / `guru@gamecenter.test` | `password` |
| Siswa SMA | `siswa` / `siswa@gamecenter.test` | `password` |
| Siswa SMK | `siswa-smk` / `smk@gamecenter.test` | `password` |

### Panel admin

Panel Filament di **`/admin`** memakai tema kustom yang sama dengan aplikasi
siswa: kanvas hangat berpola titik, kartu putih, aksen merah `#e60012`,
Fraunces Variable untuk judul, Instrument Sans Variable untuk UI, dan mode
gelap/terang.

- **Ringkasan** menampilkan sapaan kontekstual, kartu statistik dengan
  sparkline 7 hari, grafik aktivitas sesi, panel akses cepat, dan tabel
  pengajuan upgrade terbaru.
- **Admin** melihat antrean pengajuan, paket keanggotaan, dan tombol tinjau;
  **guru** hanya melihat statistik materi/soal serta tautan pengajaran, tanpa
  akses ke pengelolaan keanggotaan.
- Tema dimuat lewat `resources/css/filament/admin/theme.css` dan terdaftar di
  `vite.config.ts`; jalankan `npm run build` setelah mengubah token atau gaya
  panel.
- Login panel memakai brand yang sama (logo topi wisuda + wordmark), card
  ringkas selebar 24rem, dan komponen formulir bertema hangat. Tombol
  **Kembali ke Game Center** di bawah form membawa pengunjung ke beranda.

### Keanggotaan

| Paket | Bulanan | Tahunan | Sasaran |
|-------|---------|---------|---------|
| Gratis | Rp0 | Rp0 | Semua pengunjung (aktif otomatis) |
| Standard | Rp29.000 | Rp290.000 | Pelajar perorangan |
| Professional | Rp99.000 | Rp990.000 | Guru / kelas (rekomendasi) |
| Enterprise | Rp499.000 | Rp4.990.000 | Sekolah / lembaga |

- Katalog publik ada di **`/keanggotaan`**; tamu tetap bebas bermain dan
  diarahkan ke `/masuk` saat mencoba mengajukan paket.
- Anggota **Gratis** dapat langsung menekan **Upgrade sekarang** di halaman
  keanggotaan (membuka dialog paket rekomendasi) atau memilih **Upgrade
  keanggotaan** dari menu akun di topbar.
- Paket **Gratis** aktif otomatis untuk semua akun. Pengajuan hanya menerima
  paket berbayar yang **lebih tinggi** dari paket aktif, dan hanya satu
  pengajuan pending per pengguna.
- Alur upgrade: pilih paket dan siklus → kirim pengajuan (kode referensi
  `GC-XXXXXX` dibuat otomatis) → transfer manual ke rekening yayasan sesuai
  nominal → admin menyetujui di **`/admin/memberships`** → paket aktif dan paket
  sebelumnya otomatis kedaluwarsa.
- Data rekening diatur lewat `.env`:
  `MEMBERSHIP_BANK_NAME`, `MEMBERSHIP_BANK_NUMBER`, `MEMBERSHIP_BANK_HOLDER`.
- Kolom `limits` (JSON) pada paket sudah disiapkan untuk penegakan kuota fitur
  pada fase berikutnya; fase ini belum melakukan gating.

---

## Offline-first & sinkronisasi

Fondasi offline-first sudah terpasang: data yang dibutuhkan untuk bermain
disimpan lokal, hasil permainan masuk antrean, lalu dikirim ke server saat
koneksi tersedia. Penilaian akhir tetap dihitung server. Alur **offline →
online** sudah diuji di Chromium: halaman bermain dimuat dari cache tanpa
jaringan, sesi diselesaikan, lalu antrean terkirim otomatis saat koneksi
kembali.

### Penyimpanan lokal (IndexedDB)

Database `gamecenter-offline` versi 1 dibuat otomatis di browser dengan store:

| Store | Isi |
|-------|-----|
| `catalog` | Katalog terakhir dari halaman jelajah (jenjang, statistik, versi) |
| `materials`, `questions`, `assessments` | Cache konten materi, soal, dan asesmen |
| `progress`, `sessions` | Progres bab dan sesi permainan lokal |
| `syncQueue` | Antrean item `session` / `progress` / `answer` yang belum terkirim |
| `userSettings` | Preferensi lokal pengguna |

Modul klien ada di [`resources/js/lib/offline/`](resources/js/lib/offline/):
`db-schema.ts` (nama/versi store + tipe), `offline-db.ts` (wrapper IndexedDB,
`queueSync`, `markSynced`, `markSyncFailed`, `clearUserData`), dan
`sync-service.ts` (antrean batch, event online/offline, `useSyncExternalStore`).
Hook [`useOfflineSync`](resources/js/Hooks/useOfflineSync.ts) dipakai footer
untuk menampilkan status dan memicu sinkronisasi manual.

### Kontrak `POST /api/sync`

- Middleware `auth:sanctum`, throttle **60 permintaan/menit**, maksimal **50
  item** per batch. Klien mengirim maksimal 25 item per batch.
- Setiap item punya `uuid` unik (idempotensi), `type`
  (`session` / `progress` / `answer`), `recorded_at` opsional, dan `payload`.
- Respons: `results[]` berisi `uuid`, `status` (`completed` / `failed`), dan
  `message`; `summary` berisi jumlah `completed` dan `failed`.
- Item gagal tidak memblokir item lain. Item tetap di antrean lokal dan dicoba
  ulang hingga **5 kali** (`attempts`, `lastError` tersimpan).
- UUID yang sudah selesai dikembalikan `completed` tanpa diproses ulang; UUID
  milik pengguna lain ditolak.

```json
{
  "items": [
    {
      "uuid": "3f1c2a9e-7b4d-4c2a-9e11-5a6b7c8d9e0f",
      "type": "session",
      "recorded_at": "2026-11-16T06:40:00+07:00",
      "payload": { "assessment_id": 1, "mode": "easy", "answers": [] }
    }
  ]
}
```

Saat memproses `session`, server memuat asesmen, **menghitung ulang** jawaban
objektif (pilihan ganda, pilihan ganda kompleks), memakai klien hanya untuk
jawaban non-objektif (uraian dan tipe lanjutan), lalu menyimpan sesi, jawaban,
hasil, XP (**XP = poin yang diperoleh**), koin (**koin = XP ÷ 5**), level,
streak harian, dan progres bab. `progress` menyimpan nilai terbaik dan status
tertinggi; `answer` memperbarui jawaban sesi yang sudah ada.

### PWA & service worker

- `public/manifest.webmanifest`, `public/icon.svg`, `public/icon-maskable.svg`,
  dan halaman cadangan `public/offline.html`.
- `public/sw.js` menyimpan app shell, navigasi terakhir (network-first dengan
  fallback cache dan `offline.html`), serta aset `/build`, font, dan ikon
  (cache-first). Respons **Inertia JSON, `/api/*`, `/sanctum`, dan `/admin`
  tidak di-cache** demi privasi.
- Service worker **hanya didaftarkan pada build produksi**
  (`import.meta.env.PROD`) di [`resources/js/app.tsx`](resources/js/app.tsx);
  jalankan `npm run build` untuk mencobanya.
- **Background Sync** memakai tag `gamecenter-sync`. Browser mengirim pesan ke
  tab yang terbuka untuk memicu flush; antrean tetap tersimpan bila aplikasi
  ditutup.
- Logout mengosongkan cache halaman dan data pengguna di IndexedDB (katalog
  dipertahankan).
- Naikkan `CACHE_VERSION` di `public/sw.js` pada setiap rilis agar cache lama
  dibuang saat aktivasi.

### Status di footer

Footer menampilkan salah satu status: **Offline**, **Menyinkronkan…**,
**n tersimpan**, atau **Sinkron tertunda**. Klik status untuk sinkronisasi
manual. Sinkronisasi memerlukan login; data tamu tetap tersimpan lokal sampai
pengguna masuk.

---

## Panduan & bantuan

Pusat bantuan publik ada di **`/panduan`** dan dapat dibuka tanpa login. Isinya
disusun seperti dokumentasi produk—sidebar topik, pencarian, daftar isi per
halaman, dan navigasi sebelumnya/berikutnya—tetapi tetap berjalan di dalam
aplikasi Laravel + Inertia + React. **Tidak memakai Docusaurus** atau generator
dokumentasi terpisah.

- **11 topik dalam 4 kelompok:** Mulai, Akun & keanggotaan, Guru & admin, dan
  Bantuan (FAQ serta masalah umum).
- **Diagram Mermaid** untuk alur bermain dan alur upgrade; **peta peran dan
  akses** disajikan sebagai tabel teks agar tetap terbaca di semua layar.
  Mermaid dimuat dinamis (hanya saat diagram tampil), memakai
  `securityLevel: 'strict'`, mengikuti tema terang/gelap, dan selalu muat di
  dalam kartu tanpa overflow horizontal.
- Topik tak dikenal menampilkan state “tidak ditemukan” di dalam shell panduan,
  lengkap dengan tautan kembali.
- Entri panduan tersedia dari topbar: chip **Panduan** di baris menu pada beranda
  ponsel, ikon **Panduan** di halaman lain, tautan teks di desktop, serta item
  **Panduan** di menu akun.
- Isi topik berada di [`resources/js/Guide/pages.tsx`](resources/js/Guide/pages.tsx);
  tambah atau ubah topik di `GUIDE_PAGES` tanpa membuat route baru.

---

## Perintah berguna

```bash
php artisan migrate:fresh --seed   # reset + isi data awal
php artisan test                   # jalankan seluruh test
npm run typecheck                  # cek TypeScript
npm run build                      # build aset produksi
php artisan optimize               # cache config/route/view (produksi)
php artisan optimize:clear         # bersihkan cache (development)
```

> **Versi sistem:** ubah heading rilis teratas di [`changelog.md`](changelog.md)
> (contoh `## [0.5.0] - 2026-11-16 06:55 WIB`). Footer dan props Inertia
> `version` mengikuti otomatis tanpa mengubah kode. Semua timestamp memakai
> waktu lokal server (WIB, UTC+7).

---

## Struktur data materi

```
Jenjang (education_levels)
└── Kelas (classes, fase A–F)
    └── Mata Pelajaran (subjects)
        └── Bab (chapters)
            ├── Materi (learning_materials)   → 60% pengalaman belajar
            └── Assessment (assessments: easy/medium/hard)
                └── Soal (questions + question_options)
```

Bank soal mendukung tipe: `multiple_choice`, `multiple_answer`, `drag_drop`,
`matching`, `puzzle`, `simulation`, dan `essay` (dengan rubrik + flag `ai_assisted`).

---

## Dokumentasi perencanaan

Rencana lengkap (ERD, wireframe, roadmap fase 1–7) ada di
[`../doc/plan-1.md`](../doc/plan-1.md). Laporan implementasi per fase:
[`../doc/fase-1-implementasi.md`](../doc/fase-1-implementasi.md),
[`../doc/fase-2-implementasi.md`](../doc/fase-2-implementasi.md), dan
[`../doc/fase-3-implementasi.md`](../doc/fase-3-implementasi.md).
