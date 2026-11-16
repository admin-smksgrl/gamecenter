# Game Center Edukasi

Platform belajar berbasis permainan untuk PAUD sampai SMA-SMK. Siswa memilih
jenjang, kelas, dan mata pelajaran, membaca materi, lalu mengerjakan soal dalam
tiga tingkat kesulitan. Guru dan admin mengelola kurikulum, materi, dan soal
lewat panel Filament.

Dibangun dengan **Laravel 12**, **Inertia + React 19**, **TypeScript**, dan
**Tailwind CSS v4**.

## Isi repo

```
gamecenter/        aplikasi Laravel (kode utama)
doc/               dokumen rencana, laporan per fase, peta cakupan materi
artisan            pintasan agar `php artisan ...` bisa jalan dari folder ini
serve.bat          pintasan menjalankan server lokal (Windows)
```

> Folder `data/` (sumber kurikulum mentah, ±1,5 GB) **tidak** disertakan.
> Materi yang sudah dikurasi tersimpan sebagai JSON di
> `gamecenter/database/seeders/data/sma-smk/`.

## Kebutuhan

- PHP 8.3+ dengan ekstensi `pdo_mysql`, `mbstring`, `gd`
- Composer 2
- Node.js 20+ dan npm
- MySQL 8 (atau MariaDB 10.6+) — SQLite juga bisa untuk pengembangan

## Pasang di komputer baru

```bash
cd gamecenter

composer install
npm install

cp .env.example .env          # Windows: copy .env.example .env
php artisan key:generate

# Isi DB_DATABASE / DB_USERNAME / DB_PASSWORD di .env, lalu:
php artisan migrate --seed
npm run build

php artisan serve             # http://127.0.0.1:8000
```

Akun demo setelah `--seed` (kata sandi semuanya `password`):

| Username | Peran | Jenjang |
|----------|-------|---------|
| `admin` | admin | — |
| `guru` | guru | — |
| `siswa` | siswa | SMA, Kelas 10 |
| `siswa-smk` | siswa | SMK, Kelas 10 |

Masuk lewat satu halaman **`/masuk`**; tujuan setelah masuk ditentukan peran
(siswa → beranda materi, guru/admin → `/admin`).

## Perintah yang sering dipakai

```bash
# Materi & soal
php artisan gamecenter:materi-import                    # impor semua JSON
php artisan gamecenter:materi-import --dry-run          # uji tanpa menulis
php artisan gamecenter:materi-import path/ke/berkas.json

# Kesiapan rilis
php artisan gamecenter:deploy-check                     # laporan
php artisan gamecenter:deploy-check --strict            # gagal bila ada peringatan (CI)

# Pengembangan
php artisan test                                        # seluruh tes
npm run dev                                             # vite dev server
npm run build                                           # aset produksi
```

Selalu jalankan `php artisan optimize:clear` sebelum `php artisan test` bila
konfigurasi pernah di-cache.

## Alur materi

1. Satu modul ajar = satu bab = satu berkas JSON di
   `gamecenter/database/seeders/data/sma-smk/fase-e/<mapel>/`.
2. Setiap bab berisi **3 materi** dan **3 asesmen** (mudah 5 soal, sedang 10,
   sulit 15). Setiap soal wajib punya `explanation`; `hint` dilarang pada soal
   sulit. Simbol matematika memakai Unicode (`²`, `×`, `÷`, `√`), bukan LaTeX.
3. Berkas JSON adalah **sumber kebenaran**. Koreksi dilakukan di JSON lalu
   diimpor ulang — bukan lewat panel.
4. Importer bersifat idempoten dan transaksional: satu masalah validasi berarti
   tidak ada yang ditulis.

## Dokumentasi

- [`doc/plan-materi-SMASMK.md`](doc/plan-materi-SMASMK.md) — rencana materi SMA/SMK
- [`doc/peta-cakupan-materi.md`](doc/peta-cakupan-materi.md) — peta cakupan 88 buku
- [`doc/fase-4-implementasi.md`](doc/fase-4-implementasi.md) — tema & desain
- [`doc/fase-5-implementasi.md`](doc/fase-5-implementasi.md) — kesiapan deploy
- [`gamecenter/changelog.md`](gamecenter/changelog.md) — riwayat rilis
- [`gamecenter/README.md`](gamecenter/README.md) — catatan teknis aplikasi

## Lisensi

Kode aplikasi: MIT. Materi pembelajaran dikurasi dari buku ajar Kurikulum
Merdeka dan tetap mengikuti ketentuan pemilik hak cipta masing-masing.
