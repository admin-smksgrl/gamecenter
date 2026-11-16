# Laporan Implementasi — Fase 3: Game Engine

**Tanggal:** 16 November 2026
**Rilis:** `0.7.0`
**Lokasi proyek:** `C:\laragon\www\gamecenter\gamecenter`
**Status:** ✅ Selesai — 56 test / 390 assertion lulus, typecheck bersih, build produksi sukses, dan alur bermain terverifikasi di browser.

---

## 1. Ringkasan

Fase 3 menghubungkan katalog materi dengan pengalaman bermain yang utuh:
siswa memilih bab dan tingkat kesulitan, melihat ringkasan sesi, menjawab soal
satu per satu, menerima umpan balik langsung, lalu mendapatkan skor, XP, koin,
level, lencana, dan tinjauan jawaban.

Mesin permainan berjalan di client agar respons instan dan tetap bisa dipakai
offline. Server tetap menjadi sumber kebenaran untuk soal objektif saat sesi
disinkronkan. Soal uraian disimpan untuk penilaian lanjutan, tetapi belum
dihitung ke skor sesi.

Fitur utama pada fase ini:

- Halaman `/main/{assessment}` dengan fase **intro → bermain → hasil**.
- Enam mekanik: pilihan ganda, pilihan ganda kompleks, urutan, menjodohkan,
  simulasi, dan uraian.
- Timer sesi, petunjuk, peta soal, umpan balik, dan tinjauan jawaban.
- Gamifikasi XP, koin, level, dan lencana sesi.
- Cache soal ke IndexedDB dan antrean hasil sesi otomatis.

## 2. Berkas yang ditambahkan/diubah

### Backend

| Berkas | Fungsi |
|--------|--------|
| `app/Http/Controllers/PlayController.php` | Memuat asesmen + soal + opsi, memvalidasi rantai kurikulum aktif, mengirim props Inertia |
| `routes/web.php` | Route `GET /main/{assessment}` → `play.show` |
| `database/seeders/DemoContentSeeder.php` | Menambah soal interaktif dan payload JSON untuk mode sedang/sulit |
| `tests/Feature/PlayPageTest.php` | Test halaman bermain tamu, data mekanik, dan asesmen nonaktif |
| `tests/Feature/SyncApiTest.php` | Test tambahan: uraian disimpan tetapi tidak masuk skor |
| `tests/Feature/GameCenterPageTest.php` | Jumlah soal katalog disesuaikan menjadi 22 |
| `tests/Feature/CurriculumSeedTest.php` | Jumlah soal idempoten disesuaikan menjadi 22 |

### Klien

| Berkas | Fungsi |
|--------|--------|
| `resources/js/lib/game/game-engine.ts` | Tipe soal, evaluasi jawaban, ringkasan sesi, payload sinkronisasi, helper urutan/pasangan |
| `resources/js/lib/game/gamification.ts` | Ambang level, progress level, konversi koin, lencana sesi |
| `resources/js/Components/Game/QuizGame.tsx` | Pilihan ganda, ganda kompleks, uraian + rubrik, pintasan angka |
| `resources/js/Components/Game/DragDropGame.tsx` | Urutan drag & drop + tombol naik/turun (dipakai juga untuk puzzle) |
| `resources/js/Components/Game/MatchGame.tsx` | Menjodohkan kiri–kanan, lepas pasangan, kunci jawaban saat ditinjau |
| `resources/js/Components/Game/SimulationGame.tsx` | Pilihan keputusan studi kasus |
| `resources/js/Pages/GameCenter/Play.tsx` | Orkestrasi sesi, timer, cache, penilaian, hasil, dan antrean sinkronisasi |
| `resources/js/Pages/GameCenter/Index.tsx` | Tombol **Main** pada kartu asesmen dan penjelasan alur bermain |

## 3. Alur permainan

```
Katalog / panel bab
  └─ tombol Main → GET /main/{assessment}
       ├─ Intro: ringkasan soal, waktu, poin, KKM, pemain, progres terbaik
       ├─ Bermain
       │    ├─ pilih jawaban / susun urutan / jodohkan / tulis uraian
       │    ├─ Periksa jawaban → nilai + penjelasan + jawaban benar
       │    ├─ peta soal untuk berpindah atau meninjau jawaban
       │    └─ timer habis → sesi otomatis selesai
       └─ Hasil
            ├─ skor, benar/salah/kosong, durasi, lulus KKM
            ├─ XP, koin, level, lencana
            ├─ tinjauan seluruh jawaban
            └─ antrean sinkronisasi (atau ajakan masuk untuk tamu)
```

Urutan soal mengikuti `order` dari server. Sesi dapat dimulai ulang dari layar
hasil tanpa memuat ulang halaman. Soal yang sudah diperiksa terkunci, sehingga
jawaban tidak dapat diubah setelah umpan balik tampil.

## 4. Model penilaian

| Tipe soal | Penilaian client | Perilaku server saat sync |
|-----------|------------------|---------------------------|
| `multiple_choice` | Opsi benar dari `is_correct` | Dihitung ulang dari opsi/kunci |
| `multiple_answer` | Himpunan opsi harus sama persis | Dihitung ulang dari opsi/kunci |
| `drag_drop`, `puzzle` | Urutan harus sama persis | Memakai poin client, dibatasi `points` |
| `matching` | Semua pasangan harus benar | Memakai poin client, dibatasi `points` |
| `simulation` | Opsi keputusan benar | Memakai poin client, dibatasi `points` |
| `essay` | `ungraded`, poin 0 | Disimpan, poin 0, menunggu guru/AI |

Ketentuan skor:

- Skor sesi = `round(poin diperoleh / poin maksimum soal inti × 100)`.
- Soal uraian tidak masuk pembilang maupun penyebut skor.
- `passed` jika skor ≥ `passing_score` asesmen.
- XP sesi = poin yang diperoleh; koin = `floor(XP / 5)`.
- Durasi dihitung dari `started_at` sampai `completed_at`.
- Waktu per soal dicatat untuk analitik jawaban.

Nilai objektif dikirim sebagai payload jawaban, tetapi server tidak
mempercayainya dan menghitung ulang. Nilai tipe interaktif memakai hasil client
yang dibatasi poin soal agar tidak bisa melampaui maksimum.

## 5. Mekanik antarmuka

- **Pilihan ganda / ganda kompleks:** kartu opsi dengan status terpilih,
  benar/salah, dan pintasan angka `1–9` selama fokus bukan input teks.
- **Uraian:** textarea, penghitung karakter, catatan penilaian lanjutan, dan
  daftar rubrik berbobot.
- **Urutan / puzzle:** daftar dapat diubah dengan drag & drop atau tombol panah;
  posisi benar ditandai hijau saat ditinjau.
- **Menjodohkan:** pilih kartu kiri lalu kartu kanan; pasangan dapat dilepas;
  kartu kanan yang sudah dipakai ditandai; jawaban benar ditampilkan saat
  ditinjau.
- **Simulasi:** pilihan keputusan A–F dengan penanda benar/salah.
- Semua mekanik memakai props yang sama (`question`, `response`, `onChange`,
  `disabled`, `revealed`) dan status aksesibilitas `aria-pressed` pada pilihan.

## 6. Gamifikasi

| Level | XP minimum | Gelar |
|-------|------------|-------|
| 1 | 0 | Pemula |
| 2 | 100 | Pemain |
| 3 | 250 | Ahli |
| 4 | 500 | Master |
| 5 | 1000 | Legenda |

Lencana sesi yang tersedia:

- **Langkah Pertama** — menyelesaikan minimal satu soal inti.
- **Sempurna!** — skor 100.
- **Pemanasan** — tiga jawaban benar berturut-turut.
- **Tak Terbendung** — sepuluh jawaban benar berturut-turut.
- **Jenius Matematika** — skor sempurna pada mode sulit Matematika.
- **Ahli Studi Kasus** — skor ≥ 80 pada sesi yang memuat simulasi.

## 7. Offline-first dan sinkronisasi

Saat halaman bermain dibuka:

1. Asesmen disimpan ke store `assessments`.
2. Setiap soal disimpan ke store `questions`, termasuk `payload`,
   `correct_answer`, poin, dan batas waktu.
3. Jika pengguna masuk dan sesi selesai, `syncService.enqueue('session', ...)`
   menambahkan payload ke `syncQueue`.
4. Sesi lokal juga ditulis ke store `sessions` dengan `synced=false`.
5. Footer menjalankan flush saat online, saat tab aktif kembali, atau lewat
   klik manual.

Tamu dapat bermain penuh, tetapi hasil tidak masuk antrean. Layar hasil
menampilkan ajakan masuk agar hasil berikutnya tersimpan ke profil.

Alur ini sudah diuji langsung di browser: setelah service worker aktif,
halaman `/main/2` dimuat ulang dalam keadaan offline, soal dijawab, sesi
diselesaikan, dan antrean berisi 1 item. Saat koneksi dikembalikan, antrean
kosong dan server menerima sesi tersebut.

## 8. Konten demo

Bank soal Eksponen kini berisi **22 soal**:

| Mode | Jumlah | Komposisi |
|------|--------|-----------|
| Mudah | 5 | Pilihan ganda |
| Sedang | 8 | 5 pilihan ganda, 1 uraian, 1 ganda kompleks, 1 drag & drop |
| Sulit | 9 | 5 pilihan ganda, 1 uraian, 1 menjodohkan, 1 puzzle, 1 simulasi |

Seeder tetap idempoten: soal dan opsi lama diperbarui/dibersihkan sebelum
dibuat ulang.

## 9. Verifikasi

### Otomatis

- `php artisan test` → **56 passed, 390 assertions**
  (2026-11-16 08:05 WIB).
- `npm run typecheck` → bersih.
- `npm run build` → sukses; hanya ada peringatan ukuran chunk Mermaid yang
  sudah muncul sebelum fase ini.

Test baru mencakup:

- Tamu dapat membuka mode sedang, menerima 8 soal, opsi ganda kompleks, dan
  payload drag & drop.
- Mode sulit mengekspos data matching, puzzle, dan simulasi.
- Asesmen nonaktif menghasilkan 404.
- Jawaban uraian tersimpan lengkap, tetapi tidak menambah skor, XP, atau
  jumlah soal inti pada sesi server.

### Browser nyata (Playwright/Chromium)

- Login `siswa`, membuka mode sedang dari panel bab, menjawab 7 soal inti
  dengan benar, dan melewati uraian.
- Hasil: skor **100**, 7 benar, 0 salah, 0 kosong, **+145 XP**,
  **+29 koin**, level **3**, lencana tampil, dan status
  **“Hasil masuk antrean sinkronisasi.”**
- Mode sulit: matching, puzzle, dan simulasi masing-masing memberi umpan balik
  **“Tepat!”**.
- Tampilan ponsel 390×844: intro dan halaman soal tidak mengalami overflow
  horizontal.
- Tidak ada error halaman, error konsol, atau respons HTTP ≥ 400.

### Sinkronisasi server

Diperiksa lewat Tinker setelah antrean terkirim:

- Sesi terakhir: skor 100, 7 benar, `max_score=145`, `xp_earned=145`,
  `total_questions=7`, 7 jawaban, `synced=true`.
- Pengguna `siswa`: **265 XP**, **74 koin**, level **3**.
- Progres bab 1: `best_score=100`, `attempts=1`, status `completed`.

### Offline → online (browser nyata)

- Service worker aktif dan mengontrol halaman sebelum jaringan diputus.
- `/main/2` berhasil dimuat ulang saat offline dari cache halaman + aset.
- Satu soal dijawab, soal terakhir diperiksa, lalu sesi diselesaikan tanpa
  jaringan; layar hasil menampilkan “Hasil masuk antrean sinkronisasi.”
- `syncQueue` berisi **1 item** saat offline.
- Setelah online, antrean otomatis kosong; server menerima sesi
  (`score=14`, `max_score=145`, `xp_earned=20`, 2 jawaban, `synced=true`),
  pengguna `siswa-smk` naik ke **80 XP / 18 koin**, dan progres bab mencatat
  `attempts=2` (2026-11-16 08:09 WIB).
- Tidak ada error halaman atau konsol selama skenario offline.

## 10. Batasan dan lanjutan

- Timer yang berjalan adalah timer sesi; `time_limit` per soal baru disimpan
  dan belum dipakai untuk menghentikan soal secara individual.
- Penilaian uraian masih menunggu alur guru/AI; saat ini tersimpan dengan poin
  nol dan status belum dinilai.
- Tipe `CachedQuestion` di `db-schema.ts` belum memuat `payload` dan
  `correct_answer` secara eksplisit, meskipun penulisan cache sudah membawa
  kedua field tersebut.
- Fase berikutnya (Fase 4) berfokus pada tema visual per jenjang, kurasi materi
  SIBI, halaman progres, dan penguatan responsif perangkat IFP/PID.
