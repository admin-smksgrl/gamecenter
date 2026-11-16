# Laporan Implementasi — Fase 4: Konten & UI

**Tanggal:** 16 November 2026
**Rilis:** `0.8.0`
**Lokasi proyek:** `C:\laragon\www\gamecenter\gamecenter`
**Status:** ✅ Selesai — 65 test / 593 assertion lulus, typecheck bersih, build produksi sukses, dan seed MySQL berhasil.

---

## 1. Ringkasan

Fase 4 melengkapi pengalaman belajar dari sisi konten dan antarmuka:

- Seluruh jenjang memakai **satu tema visual** (merah `#e60012` di atas putih)
  tanpa menduplikasi komponen; jenjang dibedakan lewat isi dan label.
- **Materi pembelajaran** kini tampil di halaman bermain sebagai porsi 60%
  sebelum soal, lengkap dengan penanda "sudah dibaca".
- Dua halaman baru, **`/progres`** dan **`/hasil/{gameSession}`**, memberi
  siswa ringkasan perkembangan, riwayat sesi, koleksi lencana, dan pembahasan
  jawaban yang bisa dibuka kembali.
- Katalog materi mendapat **filter mapel** sehingga alurnya menjadi
  jenjang → kelas → mapel → mode, ditambah strip "Lanjutkan belajar".
- Konten dikurasi manual lintas jenjang: **4 bab baru** (PAUD, TK, SMP, SMK)
  dengan total **60 soal** dan materi pendukung.
- Lencana diberikan **di server** lewat `AchievementService`, sehingga aman
  dari klaim berulang di perangkat offline.

Total konten saat ini: **5 bab, 82 soal, 8 lencana**, dan **12 kelas**.

## 2. Berkas yang ditambahkan/diubah

### Backend

| Berkas | Fungsi |
|--------|--------|
| `database/migrations/2026_11_16_000000_add_materials_read_to_user_progress_table.php` | Menambah kolom `materials_read` pada `user_progress` |
| `app/Models/UserProgress.php` | Fillable + cast `materials_read` |
| `app/Services/AchievementService.php` | Menilai dan memberikan lencana setelah sesi/progres tersinkron |
| `app/Services/SyncService.php` | Menyimpan `materials_read`, memanggil layanan lencana |
| `app/Http/Controllers/PlayController.php` | Mengirim `materials` + `progress.materials_read` |
| `app/Http/Controllers/ProgressController.php` | Props halaman progres (statistik, aktivitas, riwayat, lencana) |
| `app/Http/Controllers/ResultController.php` | Props halaman hasil + pembahasan jawaban |
| `app/Http/Middleware/HandleInertiaRequests.php` | Props auth `education_level_slug` dan `level_theme` |
| `routes/web.php` | Route `progress.index` dan `result.show` (middleware `auth`) |
| `database/seeders/CuratedContentSeeder.php` | Kurasi 4 bab lintas jenjang |
| `database/seeders/AchievementSeeder.php` | Syarat `chapter-master` menjadi 3 tingkat kesulitan |
| `database/seeders/DatabaseSeeder.php` | Mendaftarkan `CuratedContentSeeder` |
| `tests/Feature/ProgressPageTest.php` | Test halaman progres |
| `tests/Feature/ResultPageTest.php` | Test halaman hasil + otorisasi |
| `tests/Feature/PlayPageTest.php` | Test materi dan `materials_read` |
| `tests/Feature/SyncApiTest.php` | Hadiah XP/koin disesuaikan dengan lencana server |
| `tests/Feature/GameCenterPageTest.php` | Statistik katalog 5 bab / 82 soal |
| `tests/Feature/CurriculumSeedTest.php` | Jumlah soal idempoten 82 |

### Klien

| Berkas | Fungsi |
|--------|--------|
| `resources/js/lib/level-theme.ts` | Metadata tema per jenjang |
| `resources/css/app.css` | Token tema, varian gelap, tipografi, animasi, `.material-prose` |
| `resources/js/Components/Game/MaterialViewer.tsx` | Akordeon materi, renderer markdown ringan, progress baca |
| `resources/js/Layouts/AppLayout.tsx` | Prop `levelTheme`, atribut `data-level-theme`, menu Progres |
| `resources/js/Pages/GameCenter/Index.tsx` | Filter mapel, strip lanjutkan belajar, tema jenjang |
| `resources/js/Pages/GameCenter/Play.tsx` | Materi di intro, enqueue `materials_read`, tautan hasil |
| `resources/js/Pages/GameCenter/Progress.tsx` | Halaman progres baru |
| `resources/js/Pages/GameCenter/Result.tsx` | Halaman hasil baru |
| `resources/js/types/index.d.ts` | Tipe auth `level_theme` dan `education_level_slug` |
| `public/sw.js` | `CACHE_VERSION` naik ke `0.8.0` |

## 2b. Navigasi jenjang di topbar

Topbar halaman katalog menampilkan lima pilihan jenjang, sesuai struktur
sekolah di Indonesia:

| Pilihan topbar | Jenjang di basis data | Kelas |
|----------------|-----------------------|-------|
| PAUD | `paud` | Kelompok Bermain |
| TK | `tk` | TK A, TK B |
| SD-MI | `sd` | Kelas 1–6 (Fase A–C) |
| SMP-MTs | `smp` | Kelas 7–9 (Fase D) |
| SMA-SMK | `sma` + `smk` | Kelas 10–12 (Fase E–F), keduanya |

**SMA dan SMK digabung** dalam satu pilihan karena yang membedakan keduanya
hanya sebagian mata pelajaran kejuruan. Penggabungan terjadi di lapisan
navigasi (`resources/js/lib/level-groups.ts`), bukan di basis data: jenjang
tetap dua baris terpisah sehingga rombel, mapel, dan materi kejuruan tidak
tercampur.

Saat `SMA-SMK` dipilih, daftar **Kelas** berisi enam entri dan setiap entri
diberi keterangan asal jenjangnya (`Kelas 10 / SMA`, `Kelas 10 / SMK`, dan
seterusnya). Memilih salah satu kelas langsung mempersempit mapel ke jenjang
kelas itu.

Jenjang `sd` sudah dibuat lengkap dengan enam rombel dan delapan mata pelajaran
wajib, tetapi **belum punya bab**. Halaman menampilkan pemberitahuan
"Materi SD-MI sedang disiapkan" dan kartu mapel berlabel "Segera" agar tidak
menyesatkan. Angka pada ringkasan katalog (mapel, bab, soal) dihitung dari
kelas yang sedang dibuka, bukan total seluruh situs.

## 3. Tema: satu warna untuk semua jenjang (merah + putih)

Awalnya setiap jenjang punya palet sendiri (PAUD rose, TK amber, SMP indigo,
SMA/SMK teal lalu biru). Palet per jenjang itu **dihapus** karena memunculkan
tumpang tindih warna: bayangan masih merah sementara aksen biru, atau kartu
mapel memunculkan warna lain di dalam jenjang yang berbeda.

Sekarang **satu identitas untuk semua jenjang**: merah `#e60012` di atas
permukaan putih.

| Token | Terang | Gelap |
|-------|--------|-------|
| `--color-red` (aksi/aksen) | `#e60012` | `#ff3945` |
| `--color-red-deep` (hover) | `#b8000f` | `#d2101c` |
| `--color-red-tint` (latar aksen) | `#ffebec` | `#3b1014` |
| `--color-canvas` | `#ffffff` | `#0e0c0d` |
| `--color-surface` | `#ffffff` | `#171214` |
| `--color-rule` | `#e9d3d3` | `#2d2629` |

Aturan penerapan:

1. **Satu heksa merah.** `[data-level-theme]` menimpa token dengan nilai yang
   **identik** dengan akar dokumen, jadi halaman login, beranda, permainan,
   panduan, dan panel admin memakai merah yang sama.
2. **Bayangan ikut merah.** `--shadow-lift` dan `--shadow-fab` memakai
   `rgb(184 0 15 / 0.4)` dan `rgb(230 0 18 / 0.55)`, bukan warna jenjang lain.
3. **Kartu mapel netral.** `subjectTheme()` memakai tint merah, bukan palet
   per mapel.
4. **Status permainan memakai merah/netral** (bukan hijau/amber): benar =
   merah solid, salah = netral, uraian = netral.
5. **Permukaan putih bersih.** `canvas` dan `surface` sama-sama `#ffffff`,
   dipisahkan garis `#e9d3d3` dan bayangan tipis.
6. **`theme-color` peramban** selalu `#e60012`.

Jenjang tetap dibedakan lewat **isi dan label** (PAUD, TK, SMP, SMA, SMK),
bukan lewat warna.

## 4. Kurasi konten lintas jenjang

Konten dikurasi manual dari tema Kurikulum Merdeka, bukan hasil scraping SIBI.
Setiap bab memiliki 2 materi dan 3 asesmen (mudah/sedang/sulit) berisi 5 soal.

| Jenjang | Bab | Kode | Soal |
|---------|-----|------|------|
| PAUD | Mengenal Bentuk Dasar | `PAUD 1.1` | 15 |
| TK | Berhitung 1–10 | `TK 1.1` | 15 |
| SMP | Bilangan Bulat | `MTK 7.1` | 15 |
| SMK | Algoritma & Logika | `PEMDAS 1.1` | 15 |

Bab Eksponen (SMA) tetap menjadi konten demo interaktif dengan 22 soal. Seeder
bersifat idempoten (`updateOrCreate`) sehingga aman dijalankan berulang.

## 5. Halaman dan alur

### Katalog `/`

- Filter berlapis: **jenjang → kelas → mapel → mode**.
- Menu mapel di topbar menyaring daftar kartu dan berpadu dengan chip kelompok
  serta pencarian; memilih salah satu mereset filter lain agar hasil konsisten.
- Strip **"Lanjutkan belajar"** menampilkan bab yang terakhir dibuka beserta
  skor terbaik dan tautan langsung ke sesi.
- Tema jenjang aktif langsung mengubah aksen seluruh layout.

### Bermain `/main/{assessment}`

```
Intro (materi 60% + ringkasan sesi)
  └─ MaterialViewer: akordeon, tandai dibaca, progress bar
       └─ enqueue progress { materials_read }
  └─ Mulai → soal → hasil
       └─ tombol "Lihat progres" dan "Jelajah materi"
```

Status baca disimpan di `localStorage` (`gamecenter.materials.{chapterId}`)
agar tetap tersedia offline, lalu disinkronkan sebagai item `progress`.

### Progres `/progres`

- Header identitas, level, XP, koin, streak, dan progress menuju level
  berikutnya.
- Enam kartu statistik: sesi, bab tuntas, materi dibaca, waktu belajar,
  rata-rata/terbaik, dan lencana.
- Grafik batang aktivitas 7 hari terakhir.
- Daftar progres per bab dengan skor terbaik, jumlah percobaan, dan tombol
  lanjut/ulangi.
- Riwayat 12 sesi terakhir dengan tautan ke halaman hasil.
- Grid 8 lencana dengan status terbuka/terkunci dan tanggal perolehan.

### Hasil `/hasil/{gameSession}`

- Ringkasan skor, status lulus, benar/salah/kosong, XP, koin, dan durasi.
- Pembahasan tiap jawaban: jawaban siswa, kunci, penjelasan, dan waktu.
- Jawaban uraian ditandai "Menunggu penilaian".
- Hanya pemilik sesi, guru, atau admin yang boleh membuka (403 untuk siswa lain).

## 6. Progres dan lencana

`AchievementService` memeriksa data server setelah sesi atau progres
tersinkron. Hadiah XP/koin hanya diberikan sekali per lencana.

| Lencana | Syarat |
|---------|--------|
| `first-step` | 1 sesi selesai |
| `perfect-score` | Skor 100 |
| `streak-3` | 3 jawaban benar berurutan |
| `streak-10` | 10 jawaban benar berurutan |
| `chapter-master` | 3 tingkat kesulitan tuntas dalam satu bab |
| `math-genius` | Skor 100 mode sulit Matematika |
| `case-master` | Skor ≥ 80 pada sesi bersimulasi |
| `bookworm` | Membaca 10 materi |

Kolom `materials_read` dijumlahkan lintas bab untuk lencana `bookworm`.

## 7. Sinkronisasi materi

`SyncService::processProgress` menerima field opsional `materials_read`.
Nilai disimpan dengan `max(nilai lama, nilai baru)` agar pembacaan tidak
mundur ketika perangkat lain mengirim angka lebih kecil. Perubahan progres juga
memicu pemeriksaan lencana tanpa menunggu sesi selesai.

## 8. Responsif

- Semua halaman baru memakai `scroll-quiet` dan lebar maksimum yang nyaman
  (`1080px` untuk progres, `860px` untuk hasil).
- Grid statistik: 2 kolom di ponsel, 3 di tablet, 6 di desktop.
- Header memakai `flex-wrap`; kartu progres dan riwayat menyesuaikan lebar.
- Target sentuh tombol minimal 32 px; teks memakai `tabular-nums` agar angka
  tidak bergeser.
- Breakpoint diverifikasi lewat audit kelas Tailwind dan build produksi.
  Uji perangkat fisik IFP/PID tetap disarankan pada UAT Fase 5.

## 9. Verifikasi

### Otomatis

- `php artisan test` → **65 passed, 593 assertions**
  (2026-11-16 08:59 WIB).
- `npm run typecheck` → bersih.
- `npm run build` → sukses; hanya peringatan ukuran chunk Mermaid yang sudah
  ada sebelumnya.
- Migrasi `add_materials_read_to_user_progress_table` dan `php artisan db:seed`
  berhasil pada MySQL `gamecenter`.

Test baru mencakup:

- Tamu diarahkan ke `/masuk` dari `/progres` dan `/hasil/{id}`.
- Halaman progres menampilkan statistik, aktivitas 7 hari, progres bab,
  riwayat sesi, dan 8 lencana; state kosong juga diuji.
- Pemilik, guru, dan admin dapat membuka hasil; siswa lain mendapat 403.
- Pembahasan jawaban memuat kunci dan penjelasan.
- Halaman bermain mengekspos materi dan `progress.materials_read`.
- Sinkronisasi progres menyimpan `materials_read` dan hadiah lencana.

### Regresi

Seluruh test Fase 1–3 tetap lulus. Nilai XP/koin pada `SyncApiTest`
disesuaikan karena lencana kini menambah hadiah di server (misalnya sesi mudah
sempurna menghasilkan 135 XP dan 50 koin).

## 10. Batasan dan lanjutan

- Kurasi konten masih manual dan baru mencakup satu bab per jenjang baru;
  penambahan bab berikutnya cukup melalui `CuratedContentSeeder` atau panel
  admin.
- Renderer materi mendukung subset markdown (judul, daftar, kode, tabel,
  tebal, inline code); belum ada lampiran video/audio kaya.
- Penilaian uraian masih menunggu alur guru/AI.
- Uji perangkat IFP/PID dan orientasi landscape secara fisik masuk agenda UAT
  Fase 5 (deploy & launch).
