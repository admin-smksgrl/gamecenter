# Laporan Implementasi — Fase 5: Deploy & Launch

**Tanggal:** 16 November 2026
**Rilis:** `0.9.0`
**Lokasi proyek:** `C:\laragon\www\gamecenter\gamecenter`
**Status:** ⏳ Sebagian selesai — bagian yang dapat diverifikasi lokal sudah jalan; sisanya menunggu server produksi & UAT manusia.

---

## 1. Ringkasan

Fase 5 pada `plan-1.md` berisi tujuh butir: setup produksi, konfigurasi `.env`,
migrasi + seed, build aset, deploy panel Filament, UAT, dan launch.

Empat di antaranya **tidak dapat diselesaikan dari mesin lokal** karena
membutuhkan cPanel/SSH, domain, sertifikat TLS, dan manusia (guru/siswa) untuk
UAT. Karena itu fase ini dikerjakan dalam dua bagian:

1. **Yang bisa disiapkan & diverifikasi sekarang** — semua prasyarat teknis
   dibuat, dijalankan, dan diuji.
2. **Yang harus dilakukan di server** — dicatat sebagai prosedur runbook pada
   `doc/deploy-runbook.md` (menyusul) dan butir checklist di bawah.

Pekerjaan utama fase ini adalah **`gamecenter:deploy-check`**, satu perintah
Artisan yang memeriksa 18 hal dan menjadi gerbang sebelum rilis.

---

## 2. Butir Roadmap vs Status

| Butir `plan-1.md` | Status | Keterangan |
|---|---|---|
| Setup produksi (shared hosting / cPanel) | ⏳ Menunggu server | Perlu akses hosting. |
| Konfigurasi `.env` produksi | ✅ Siap | `.env.production.example` dibuat & diuji. Penerapan di server menunggu hosting. |
| Migrasi + seed database produksi | ✅ Terverifikasi | Migrasi + seed dari nol diuji penuh di SQLite bersih. |
| Build aset (`npm run build`) + upload | ✅ Build terverifikasi | `npm run build` sukses; manifest & tema panel diperiksa otomatis. Upload menunggu hosting. |
| Deploy Filament admin panel | ✅ Terverifikasi lokal | Route, tema, logout, dan akses panel tercakup tes. |
| UAT dengan guru/siswa | ⏳ Butuh manusia | Butuh pengguna nyata; tidak bisa diotomasi. |
| Launch | ⏳ Menunggu | Bergantung butir di atas. |

---

## 3. Berkas yang ditambahkan/diubah

| Berkas | Fungsi |
|--------|--------|
| `app/Console/Commands/DeployCheckCommand.php` | Perintah `gamecenter:deploy-check` — 18 pemeriksaan kesiapan deploy, mode `--strict` untuk CI |
| `.env.production.example` | Template environment produksi tanpa kredensial nyata |
| `tests/Feature/DeployCheckCommandTest.php` | 5 tes untuk perintah deploy-check dan template env |
| `doc/fase-5-implementasi.md` | Laporan ini |

---

## 4. Perintah `gamecenter:deploy-check`

### 4.1 Pemeriksaan

| Kelompok | Yang diperiksa | Gagal bila |
|---|---|---|
| PHP | Versi PHP | < 8.3 |
| Ekstensi PHP | 13 ekstensi wajib | ada yang hilang |
| `APP_ENV` | nilai env | — (peringatan bila bukan `production`) |
| `APP_DEBUG` | nilai debug | — (peringatan bila `true`) |
| `APP_KEY` | kunci aplikasi | kosong |
| `APP_URL` | skema & domain | — (peringatan bila bukan https/domain asli) |
| `SESSION_SECURE_COOKIE` | cookie aman | — (peringatan bila nonaktif) |
| Folder tulis | 6 folder storage & bootstrap | tidak dapat ditulis |
| `storage:link` | symlink publik | — (peringatan bila belum ada) |
| Aset build | `public/build/manifest.json` | tidak ada |
| Tema panel | entri tema Filament di manifest | — (peringatan) |
| PWA | `sw.js`, `manifest.webmanifest`, `offline.html` | — (peringatan) |
| Database | koneksi PDO | tidak tersambung |
| Migrasi | migrasi tertunda | — (peringatan) |
| Data awal | jumlah users & questions | — (peringatan bila 0) |
| Route inti | `login`, `home`, `filament.admin.auth.logout` | ada yang hilang |

### 4.2 Perilaku keluar

| Kondisi | Exit code |
|---|---|
| Ada item gagal (×) | `1` |
| Ada peringatan (!) + `--strict` | `1` |
| Hanya peringatan, tanpa `--strict` | `0` |
| Semua lulus | `0` |

### 4.3 Contoh keluaran (mesin dev lokal)

```
  Game Center — Pemeriksaan Kesiapan Deploy

  ✓ PHP — 8.3.13
  ✓ Ekstensi PHP — 13 ekstensi wajib tersedia
  ! APP_ENV — local (produksi seharusnya "production")
  ! APP_DEBUG — true — jangan dipakai di produksi
  ✓ APP_KEY — terisi
  ! APP_URL — http://gamecenter.test (produksi seharusnya https dan domain asli)
  ! SESSION_SECURE_COOKIE — nonaktif — cookie sesi bisa terkirim lewat http
  ✓ Folder tulis — 6 folder dapat ditulis
  ! storage:link — belum dibuat — jalankan "php artisan storage:link" bila ada unggahan
  ✓ Aset build — manifest.json tersedia
  ✓ Tema panel — assets/theme-7vwtHVCB.css
  ✓ PWA sw.js — tersedia
  ✓ PWA manifest.webmanifest — tersedia
  ✓ PWA offline.html — tersedia
  ✓ Koneksi database — mysql
  ✓ Migrasi — semua migrasi sudah dijalankan
  ✓ Data awal — users=4, questions=82
  ✓ Route inti — login, home, logout panel tersedia

  Hasil: 13 lulus, 5 peringatan, 0 gagal
  Siap deploy. Tinjau peringatan di atas bila ada.
```

Dengan env produksi disimulasikan (`APP_ENV=production APP_DEBUG=false
APP_URL=https://… SESSION_SECURE_COOKIE=true`): **17 lulus, 1 peringatan,
0 gagal**.

---

## 5. Verifikasi yang dijalankan

| Uji | Hasil |
|---|---|
| `migrate` dari nol di SQLite bersih | 21 migrasi sukses |
| `db:seed` dari nol | 5 jenjang, 12 kelas, 133 mapel, 82 soal, 8 lencana, 4 akun, 4 paket |
| `php artisan optimize` | config, event, route, view, blade-icons, filament — semua ter-cache |
| `gamecenter:deploy-check` (dev) | 13 lulus / 5 peringatan / 0 gagal |
| `gamecenter:deploy-check` (env produksi simulasi) | 17 lulus / 1 peringatan / 0 gagal |
| `tests/Feature/DeployCheckCommandTest.php` | 5 passed (26 assertions) |
| Seluruh suite | lihat §6 |

### 5.1 Temuan penting: cache config memblokir test

Menjalankan `php artisan optimize` lalu langsung menjalankan test **membuat
7 tes gagal dengan HTTP 419**. Penyebabnya: `bootstrap/cache/config.php`
menyimpan `SESSION_ENCRYPT`/`APP_ENV` produksi, sehingga sesi test tidak cocok
dengan token CSRF.

**Aturan:** selalu `php artisan optimize:clear` sebelum menjalankan test, dan
jangan pernah menjalankan `optimize` di mesin dev yang dipakai untuk test.
Ini sudah dicatat di sini agar tidak terulang saat deploy.

---

## 6. Hasil test suite

```
Tests:  81 passed (665 assertions)
```

Sebelum fase ini: 76 tes. Fase 5 menambah 5 tes.

---

## 7. Yang belum dikerjakan (butuh server / manusia)

| Butir | Alasan | Tindakan berikutnya |
|---|---|---|
| Setup cPanel & upload | Butuh akses hosting | Ikuti `plan-1.md` §8.3 |
| `.env` produksi di server | Butuh kredensial asli | Salin `.env.production.example`, isi nilai `>>> GANTI <<<` |
| Migrasi di server | Butuh DB produksi | `php artisan migrate --force` |
| `storage:link` | Butuh server | `php artisan storage:link` |
| UAT guru/siswa | Butuh manusia | Skenario UAT pada §8 |
| Launch | Bergantung semua di atas | — |

---

## 8. Skenario UAT yang disarankan

Dijalankan di staging/produksi setelah deploy, oleh 1 guru dan 2 siswa.

**A. Siswa — alur utama**
1. Buka beranda → pilih jenjang → kelas → mapel → mode.
2. Baca materi, lalu selesaikan kuis sampai hasil muncul.
3. Cek `/progres`: XP, riwayat, lencana bertambah.
4. Buka `/hasil/{id}`: pembahasan jawaban tampil.

**B. Siswa — offline**
5. Muat satu materi (agar ter-cache), lalu matikan jaringan.
6. Selesaikan satu sesi saat offline → hasil tetap muncul.
7. Nyalakan jaringan → tunggu sinkronisasi → cek `/progres` di perangkat lain.

**C. Siswa — keanggotaan**
8. Ajukan upgrade di `/keanggotaan` dengan bukti transfer.

**D. Guru/Admin — panel**
9. Masuk lewat `/masuk` → otomatis ke `/admin`.
10. Setujui pengajuan → toast muncul dari atas layar, hilang sendiri.
11. Klik **Keluar** → konfirmasi **Ya, keluar** → kembali ke beranda.

**E. Kriteria lulus**
- Tidak ada halaman error 500.
- Data offline benar-benar terkirim (tidak ada antrean tersisa).
- Guru dapat menyelesaikan tugas panel tanpa bantuan teknis.

---

## 9. Catatan rilis

- Naikkan `CACHE_VERSION` di `public/sw.js` pada setiap rilis agar cache PWA
  lama dibuang. Versi saat ini: `0.9.0`.
- Setelah deploy, jalankan `php artisan gamecenter:deploy-check --strict`
  sebagai gerbang terakhir sebelum mengumumkan peluncuran.
