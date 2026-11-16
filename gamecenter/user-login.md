# Daftar Login Demo

Semua akun demo menggunakan password: `password`

| Peran | Nama | Username | Email | Password | Akses Dashboard |
| --- | --- | --- | --- | --- | --- |
| Admin | Administrator | `admin` | `admin@gamecenter.test` | `password` | Ya (penuh) |
| Guru | Bu Sari | `guru` | `guru@gamecenter.test` | `password` | Ya (tanpa keanggotaan) |
| Siswa SMA | Budi Santoso | `siswa` | `siswa@gamecenter.test` | `password` | Tidak |
| Siswa SMK | Rina Wulandari | `siswa-smk` | `smk@gamecenter.test` | `password` | Tidak |

## URL Akses

- Login (semua peran, satu halaman): `http://127.0.0.1:8000/masuk`
- Dashboard admin/guru: `http://127.0.0.1:8000/admin` (otomatis diarahkan ke `/masuk` bila belum login)
- Halaman login Filament `/admin/login` sudah tidak dipakai (404).
- Aplikasi siswa: `http://127.0.0.1:8000` atau `http://gamecenter.test`
- Login (Laragon): `http://gamecenter.test/masuk`

## Catatan

- Login memakai email **atau** username, plus password, di satu halaman `/masuk`.
- Setelah login: admin & guru diarahkan ke `/admin`, siswa ke beranda.
- Hanya akun aktif dengan peran admin atau guru yang dapat masuk ke `/admin`.
- Akun siswa hanya dapat mengakses aplikasi sisi siswa.
- Akun ini berasal dari `database/seeders/UserSeeder.php` dan hanya untuk pengujian lokal. Ganti password sebelum digunakan di produksi.
