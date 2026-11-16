# Laporan Implementasi — Fase 2: Offline-First Core

**Tanggal:** 16 November 2026
**Rilis:** `0.5.0`
**Lokasi proyek:** `C:\laragon\www\gamecenter\gamecenter`
**Status:** ✅ Selesai — 50 test / 328 assertion lulus, typecheck bersih, build produksi sukses.

---

## 1. Ringkasan

Fase 2 memasang fondasi **offline-first**: data katalog dan hasil bermain
disimpan di IndexedDB, hasil yang belum terkirim masuk antrean lokal, lalu
dikirim ke server dalam batch saat koneksi tersedia. Server tetap menjadi
sumber kebenaran skor: jawaban objektif dihitung ulang di backend, sehingga
klien tidak bisa memalsukan nilai, XP, atau koin.

Aplikasi juga sudah menjadi **PWA**: service worker menyimpan app shell dan
halaman terakhir, tersedia halaman `offline.html`, serta Background Sync
memicu pengiriman antrean saat koneksi kembali.

Game engine dan UI bermain belum dibangun pada fase ini; antrean dan endpoint
sudah siap dipakai olehnya pada Fase 3.

## 2. Berkas yang ditambahkan/diubah

### Backend

| Berkas | Fungsi |
|--------|--------|
| `app/Http/Controllers/Api/SyncController.php` | Endpoint invokable `POST /api/sync` |
| `app/Http/Requests/Sync/StoreSyncBatchRequest.php` | Validasi batch (1–50 item, UUID unik, tipe terbatas) |
| `app/Services/SyncService.php` | Inti sinkronisasi: idempotensi, transaksi, penilaian server, XP/koin/level/streak, progres |
| `routes/api.php` | `/health` publik; `/user` dan `/sync` di grup `auth:sanctum` |
| `.env.example`, `.env` | `SANCTUM_STATEFUL_DOMAINS` untuk domain lokal |
| `tests/Feature/SyncApiTest.php` | 7 test API sinkronisasi |

### Klien

| Berkas | Fungsi |
|--------|--------|
| `resources/js/lib/offline/db-schema.ts` | Nama/versi database, daftar store, tipe record |
| `resources/js/lib/offline/offline-db.ts` | Wrapper IndexedDB: CRUD, katalog, antrean, pembersihan |
| `resources/js/lib/offline/sync-service.ts` | Antrean batch, retry, event online/offline, snapshot untuk React |
| `resources/js/Hooks/useOfflineSync.ts` | Hook `useSyncExternalStore` + `syncNow()` |
| `resources/js/Pages/GameCenter/Index.tsx` | Menyimpan katalog terakhir ke IndexedDB |
| `resources/js/Layouts/AppLayout.tsx` | Indikator status sinkron di footer; bersihkan data lokal saat logout |

### PWA

| Berkas | Fungsi |
|--------|--------|
| `public/sw.js` | Service worker: app shell, navigasi, aset, Background Sync |
| `public/manifest.webmanifest` | Manifest PWA (`standalone`, ikon, tema) |
| `public/icon.svg`, `public/icon-maskable.svg` | Ikon aplikasi |
| `public/offline.html` | Halaman cadangan saat offline (terang/gelap) |
| `resources/views/app.blade.php` | Tautan manifest, ikon, meta PWA |
| `resources/js/app.tsx` | Registrasi service worker hanya pada build produksi |

## 3. Alur data

```
┌──────────── browser ────────────┐            ┌──────────── server ────────────┐
│ Main / progres                  │            │ auth:sanctum + throttle 60/men │
│   ↓ tulis lokal                 │            │   ↓                            │
│ IndexedDB: sessions/progress    │            │ SyncService::sync(items)       │
│   ↓ queueSync(uuid, payload)    │  POST      │   ↓ per item (transaksi)       │
│ syncQueue (pending)  ───────────┼───────────▶│ SyncQueue firstOrCreate(uuid)  │
│   ↑ markSynced / markSyncFailed │  /api/sync │   ↓ session/progress/answer    │
│   │ retry maks 5×               │◀───────────┤ hitung ulang skor objektif     │
│ Online / Background Sync        │  results   │ XP, koin, level, streak,       │
│ event → flush batch 25          │            │ user_progress                  │
└─────────────────────────────────┘            └────────────────────────────────┘
```

- UUID dibuat di klien (`crypto.randomUUID`, dengan fallback) dan menjadi kunci
  idempotensi di dua lapis: `sync_queue.client_uuid` dan
  `game_sessions.client_uuid`.
- Item yang sudah `completed` dikembalikan `completed` tanpa diproses ulang.
- UUID milik pengguna lain ditolak sebagai item gagal.
- Satu item gagal tidak menghentikan item lain dalam batch.

## 4. Skema IndexedDB

Database `gamecenter-offline` versi 1, dibuat saat pertama kali dibuka.

| Store | Key | Isi |
|-------|-----|-----|
| `catalog` | `id` | Katalog terakhir: jenjang, statistik, versi aplikasi |
| `materials` | `id` | Materi bab |
| `questions` | `id` | Soal dan opsinya |
| `assessments` | `id` | Asesmen per bab/tingkat |
| `progress` | `id` | Progres bab lokal |
| `sessions` | `uuid` | Sesi permainan lokal |
| `syncQueue` | `uuid` | Item pending: `type`, `payload`, `status`, `attempts`, `lastError` |
| `userSettings` | `key` | Preferensi lokal pengguna |

API utama `OfflineDB`: `saveCatalog`, `loadCatalog`, `setSetting`,
`getSetting`, `queueSync`, `listSyncQueue`, `pendingSync`, `queueCount`,
`markSynced`, `markSyncFailed`, dan `clearUserData`.

`clearUserData` mengosongkan `progress`, `sessions`, `syncQueue`, dan
`userSettings`, tetapi **mempertahankan katalog** agar jelajah materi tetap
tersedia setelah logout.

## 5. Kontrak API `POST /api/sync`

**Autentikasi:** sesi Sanctum (cookie SPA). Tamu menerima `401`.
**Throttle:** 60 permintaan/menit. **Ukuran batch:** 1–50 item.

```json
{
  "items": [
    {
      "uuid": "3f1c2a9e-7b4d-4c2a-9e11-5a6b7c8d9e0f",
      "type": "session",
      "recorded_at": "2026-11-16T06:40:00+07:00",
      "payload": {
        "assessment_id": 1,
        "mode": "easy",
        "answers": [
          { "question_id": 1, "user_answer": { "option_id": 2 } }
        ]
      }
    }
  ]
}
```

```json
{
  "results": [
    {
      "uuid": "3f1c2a9e-...",
      "status": "completed",
      "message": "Sesi tersimpan."
    }
  ],
  "summary": { "completed": 1, "failed": 0 }
}
```

Validasi: `uuid` wajib UUID dan unik dalam batch, `type` ∈
`session|progress|answer`, `recorded_at` opsional, `payload` wajib array.

### Perilaku per tipe

| Tipe | Perilaku server |
|------|-----------------|
| `session` | Memuat asesmen + soal + opsi, menilai jawaban, membuat `game_sessions`, `session_answers`, `session_results`, memperbarui XP/koin/level/streak dan `user_progress` |
| `progress` | Upsert progres bab dengan nilai terbaik; status tertinggi menang (`Completed` tidak bisa turun); mengisi `completed_at` |
| `answer` | Memperbarui `session_answers` pada sesi milik pengguna; benar/salah dihitung ulang |

### Penilaian

- **Pilihan ganda:** cocokkan `user_answer.option_id` dengan opsi benar
  (fallback ke teks `correct_answer`).
- **Pilihan ganda kompleks:** himpunan opsi harus sama persis dengan kunci.
- **Uraian dan tipe lanjutan:** memakai poin dari klien, tetapi **dibatasi**
  maksimal poin soal (`min(points, max)`).
- Skor = `round(earned / maxScore × 100)`; lulus mengikuti `passing_score`.
- **XP = poin yang diperoleh**, **koin = XP ÷ 5** (integer). Level memakai
  `User::levelForXp()`.
- **Streak:** hari yang sama mempertahankan streak, hari sebelumnya menambah
  1, selain itu kembali ke 1.

## 6. Antrean & retry di klien

`SyncService` memakai `useSyncExternalStore` sehingga footer dapat berlangganan
snapshot `{ online, syncing, pending, lastSyncedAt, lastError }`.

- Batch maksimal **25 item**, maksimal 4 batch per flush.
- Hanya item `pending`/`failed` dengan `attempts < 5` yang dikirim otomatis;
  sinkronisasi manual tetap mengikutkan item yang sudah habis percobaan.
- `401`/`419` menghasilkan pesan "Masuk untuk menyinkronkan data." dan antrean
  dipertahankan.
- CSRF diambil dari cookie `XSRF-TOKEN` dan dikirim sebagai header
  `X-XSRF-TOKEN`; request memakai `credentials: 'same-origin'`.
- Flush dipicu saat: aplikasi mulai, event `online`, tab kembali terlihat,
  pesan Background Sync dari service worker, dan klik status di footer.

## 7. PWA & strategi cache

| Jenis request | Strategi |
|---------------|----------|
| Navigasi halaman | Network-first → cache halaman terakhir → `offline.html` |
| Aset `/build`, font, ikon | Cache-first |
| Request Inertia (`X-Inertia`) | Network-only + JSON `503` saat offline (tidak di-cache) |
| `/api/*`, `/sanctum`, `/admin`, `/up` | Lewat langsung (tidak di-cache) |
| `POST /keluar` | Menghapus cache halaman, lalu diteruskan |
| Lainnya (GET) | Stale-while-revalidate |

- Cache halaman dibatasi 30 entri terbaru.
- Background Sync memakai tag `gamecenter-sync`; service worker mengirim pesan
  ke tab yang terbuka untuk memicu flush. Jika tidak ada tab, antrean tetap
  aman di IndexedDB dan dikirim saat aplikasi dibuka lagi.
- `CACHE_VERSION` di `public/sw.js` menentukan pembuangan cache lama saat
  aktivasi; naikkan pada setiap rilis.
- Service worker **hanya didaftarkan pada build produksi** agar tidak
  mengganggu HMR saat `npm run dev`.

## 8. Status di footer

Footer menampilkan status sinkronisasi di samping versi aplikasi:

| Kondisi | Tampilan |
|---------|----------|
| Tidak ada koneksi | **Offline** |
| Sedang mengirim | **Menyinkronkan…** |
| Ada antrean | **n tersimpan** |
| Ada item gagal | **Sinkron tertunda** |
| Bersih | Tidak ada indikator tambahan |

Status memakai `role="status"` dan `aria-live="polite"`. Klik status memicu
sinkronisasi manual. Indikator hanya aktif untuk pengguna yang sudah masuk;
data tamu tetap tersimpan lokal sampai login.

## 9. Keamanan & privasi

- Endpoint sinkronisasi wajib login dan dibatasi throttle.
- Skor objektif dihitung ulang di server; klien tidak dipercaya untuk nilai
  akhir, XP, koin, atau status lulus.
- Jawaban uraian dibatasi maksimal poin soal.
- Respons Inertia JSON dan API tidak disimpan service worker.
- Cache halaman dibersihkan saat logout; data pengguna di IndexedDB juga
  dibersihkan, sementara katalog publik dipertahankan.
- `SANCTUM_STATEFUL_DOMAINS` diisi domain lokal agar cookie sesi dipakai untuk
  `/api/sync` (bukan dianggap token API).

## 10. Verifikasi

```
Tests:    50 passed (328 assertions)
Typecheck: 0 error
Build:    sukses — app JS 364.58 kB (115.08 kB gzip), CSS 109.71 kB
```

`SyncApiTest` mencakup:

1. Tamu ditolak `401`.
2. Sesi semua benar → skor 100, XP 50, koin 10, streak 1, progres `completed`.
3. Jawaban objektif dihitung ulang (klien "berbohong" → skor 20, XP 10).
4. UUID sama tidak menggandakan sesi/XP.
5. Item gagal tidak memblokir item lain; retry UUID sama berhasil.
6. Progres mempertahankan nilai terbaik dan status tertinggi.
7. Item `answer` memperbarui jawaban sesi yang sudah ada.

**Uji HTTP nyata** (tanpa browser) memakai `php artisan serve` + `curl`:
login sesi + CSRF → `POST /api/sync` → `completed` (HTTP 200), aset PWA
(`/manifest.webmanifest`, `/sw.js`, `/offline.html`, `/icon.svg`) semuanya 200,
dan tamu tanpa sesi menerima 401. Data uji di database lokal dibersihkan
setelah verifikasi.

## 11. Keterbatasan

1. **Uji manual offline → online di browser belum dijalankan.** Perilaku
   service worker dan IndexedDB baru diuji lewat build, test API, dan HTTP;
   perlu dicoba dengan DevTools → Network → Offline saat game engine tersedia.
2. **Background Sync bergantung pada tab terbuka** untuk memicu flush; belum
   ada push worker yang mengirim data tanpa aplikasi berjalan.
3. **Gameplay offline penuh belum ada** — Fase 3 akan memakai `offlineDb` dan
   `syncService.enqueue()` dari komponen permainan.
4. **Jawaban uraian masih dipercaya klien** (dibatasi poin soal); penilaian AI
   menyusul pada fase gamifikasi/konten.
5. **Achievement belum dibuka otomatis** saat sinkronisasi; baru katalog dan
   pivot yang tersedia.
6. Service worker tidak aktif pada `npm run dev`; gunakan `npm run build`.

## 12. Catatan untuk fase berikutnya

1. **Game engine** (`game-engine.ts`) dan komponen `QuizGame`, `DragDropGame`,
   `MatchGame`, `PuzzleGame`, `SimulationGame` memakai kontrak `session` di
   atas; selesaikan sesi dengan `syncService.enqueue('session', payload)`.
2. **Uji offline nyata**: build produksi → buka beranda sekali → DevTools
   Offline → mainkan sesi → online → pastikan indikator berubah dari
   "n tersimpan" ke bersih dan XP muncul.
3. **Gamifikasi**: buka achievement saat sinkronisasi (XP, streak, skor).
4. **Timer** tetap di klien, tetapi batas waktu dapat divalidasi server dari
   `recorded_at` dan durasi asesmen bila diperlukan.
5. Naikkan `CACHE_VERSION` di `public/sw.js` setiap rilis agar cache lama
   terbuang.
