# Changelog

Semua perubahan penting pada **Ruang Belajar — Game Center** dicatat di file
ini. Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/)
dengan tambahan timestamp rilis. Aplikasi membaca heading rilis pertama yang
berisi versi semver dan menampilkannya di footer (`Ruang belajar v.<versi>`),
sehingga file ini adalah satu-satunya sumber kebenaran versi sistem.
Timestamp memakai waktu lokal server (WIB, UTC+7). Setiap heading rilis dan
bagian verifikasi mencantumkan tanggal + jam.

**Terakhir diperbarui:** 2026-11-20 16:23 WIB (rilis 0.40.0).

## [0.40.0] - 2026-11-20 16:23 WIB

**Batch 16 — buku Prakarya Budi Daya Kelas X tuntas 3/3 unit.**

### Ditambah
- **PRA 8 Budi Daya Tanaman Pangan dan Pemanfaatan Limbahnya** — glosarium
  tanaman pangan, diagram alur budi daya, tabel serealia–kacang–umbi, grafik
  umur panen, kelompokkan tanaman, pemanfaatan limbah menjadi kompos/biogas/
  silase, skenario “Lahan sekolah yang sempit”, kartu istilah, dan tantangan.
- **PRA 9 Budikdamber dan Pemanfaatan Limbahnya** — glosarium Budikdamber,
  diagram alur air kaya hara, tabel komponen ember, grafik umur panen sayuran,
  kelompokkan ikan/sayuran, pemeliharaan dan keselamatan, skenario “Budikdamber
  di halaman sekolah”, dan tantangan istilah.
- **PRA 10 Pemanfaatan Limbah Budi Daya Ternak** — glosarium limbah padat/cair,
  diagram alur pengolahan, tabel produk olahan, grafik unsur hara kompos,
  kelompokkan limbah padat/cair, lima teknik budi daya ternak dan analisis
  usaha, skenario “Kandang ayam dekat pemukiman”, dan tantangan istilah.
- Ketiga bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- **Buku Prakarya Budi Daya X tuntas 3/3 unit**, seluruhnya memenuhi minimum
  §5.3 (satu visual, empat aktivitas, dua skenario/tantangan, dua recall,
  tiga checkpoint per bab).

### Verifikasi
- `gamecenter:materi-import --dry-run` → 76 berkas, **0 gagal**.
- Impor sungguhan menambah **3 bab / 9 materi / 9 asesmen / 90 soal**.
- `gamecenter:materi-coverage` → **77 dari 80 chapter** memenuhi minimum §5.3,
  **2.695 blok**. PRA 8–10 masing-masing 26 blok, semuanya ✅.
- `php artisan test` → **149 lulus, 1 dilewati, 1.635 asertion**; tes impor
  mengharapkan 76 bab dan 2.280 soal, tes cakupan memeriksa kesepuluh bab
  Prakarya dan halaman bermain PRA 1, PRA 4, serta PRA 8.
- `npm run typecheck` dan `npm run build` → berhasil.
- `gamecenter:deploy-check` → 0 gagal.

## [0.39.0] - 2026-11-20 16:04 WIB

**Batch 15 — buku Prakarya Rekayasa Kelas X tuntas 4/4 unit.**

### Ditambah
- **PRA 4 Lampu Sensor Suara** — glosarium sensor dan komponen, diagram alur
  kerja lampu, tabel komponen rangkaian, grafik konsumsi daya lampu,
  kelompokkan sensor/pengendali, prinsip keselamatan listrik dan HPP,
  skenario “Lampu gudang yang gelap”, kartu istilah, dan tantangan istilah.
- **PRA 5 Alat Pendeteksi Hujan** — glosarium sensor hujan dan mitigasi,
  diagram alur peringatan dini, tabel komponen, grafik kategori curah hujan
  BMKG, kelompokkan masukan/keluaran, langkah mitigasi banjir, skenario
  “Peringatan dini di sekolah”, dan tantangan istilah.
- **PRA 6 Alat Penyiram Tanaman Otomatis** — glosarium hidrofit–higrofit–
  xerofit, diagram alur penyiraman, tabel kelompok tanaman dan teknik,
  grafik frekuensi penyiraman, kelompokkan tanaman berdasarkan kebutuhan
  air, prinsip perawatan alat, skenario “Taman sekolah saat libur”, dan
  tantangan istilah.
- **PRA 7 Alat Pakan Otomatis** — glosarium pakan dan komponen, diagram
  alur pengeluaran pakan, tabel komponen alat, grafik jadwal pakan,
  kelompokkan penyimpan/pengendali, prinsip kebersihan dan keselamatan,
  skenario “Pakan ayam saat pemilik pergi”, dan tantangan istilah.
- Keempat bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- **Buku Prakarya Rekayasa X tuntas 4/4 unit**, seluruhnya memenuhi minimum
  §5.3 (satu visual, empat aktivitas, dua skenario/tantangan, dua recall,
  tiga checkpoint per bab).

### Verifikasi
- `gamecenter:materi-import --dry-run` → 73 berkas, **0 gagal**.
- Impor sungguhan menambah **4 bab / 12 materi / 12 asesmen / 120 soal**.
- `gamecenter:materi-coverage` → **74 dari 77 chapter** memenuhi minimum §5.3,
  **2.617 blok**. PRA 4–7 masing-masing 26 blok, semuanya ✅.
- `php artisan test` → **148 lulus, 1 dilewati, 1.582 asertion**; tes impor
  mengharapkan 73 bab dan 2.190 soal, tes cakupan memeriksa ketujuh bab
  Prakarya dan halaman bermain PRA 1 serta PRA 4.
- `npm run typecheck` dan `npm run build` → berhasil.
- `gamecenter:deploy-check` → 0 gagal.

## [0.38.0] - 2026-11-20 15:40 WIB

**Batch 14 — buku Prakarya Kerajinan Kelas X tuntas 3/3 unit.**

### Ditambah
- **PRA 1 Ragam Hias Nusantara pada Produk Fesyen** — glosarium motif dan
  teknik, diagram alur proyek fesyen, tabel sulam–aplikasi–lukis tekstil,
  grafik waktu pengerjaan, kelompokkan motif/teknik, prinsip ergonomi dan
  nilai ekonomis, skenario “Pesanan aksesori sekolah”, kartu istilah, dan
  tantangan istilah.
- **PRA 2 Produk Aksesoris Interior Nusantara** — glosarium interior,
  diagram alur proyek, tabel makrame–pilin–lempeng–anyaman, grafik waktu
  pengeringan bahan, kelompokkan bahan alami/olahan, prinsip keselamatan
  kerja, skenario “Menghias sudut baca”, dan tantangan istilah.
- **PRA 3 Produk Aksesoris Eksterior dengan Memanfaatkan Bahan Lokal** —
  glosarium bahan lokal dan pengawetan, diagram alur proyek kelompok, tabel
  kelebihan/perawatan bahan, grafik daya tahan, kelompokkan bahan tahan
  cuaca/mudah rusak, skenario “Lampu taman untuk sekolah”, dan tantangan
  istilah.
- Ketiga bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- **Buku Prakarya Kerajinan X tuntas 3/3 unit**, seluruhnya memenuhi minimum
  §5.3 (satu visual, empat aktivitas, dua skenario/tantangan, dua recall,
  tiga checkpoint per bab).

### Verifikasi
- `gamecenter:materi-import --dry-run` → 69 berkas, **0 gagal**.
- Impor sungguhan menambah **3 bab / 9 materi / 9 asesmen / 90 soal**.
- `gamecenter:materi-coverage` → **70 dari 73 chapter** memenuhi minimum §5.3,
  **2.513 blok**. PRA 1–3 masing-masing 26 blok, semuanya ✅.
- `php artisan test` → **147 lulus, 1 dilewati, 1.516 asertion**; tes impor
  mengharapkan 69 bab dan 2.070 soal, tes cakupan memeriksa ketiga bab
  Prakarya dan halaman bermain PRA 1.
- `gamecenter:deploy-check` → 0 gagal.

## [0.37.0] - 2026-11-20 15:14 WIB

**Batch 13 tuntas — buku PJOK Kelas X 8/8 bab.**

### Ditambah
- **PJOK 1 Permainan Bola Basket** — glosarium istilah basket, diagram alur
  permainan, tabel teknik (passing, dribbling, shooting, pivot, rebound),
  grafik nilai poin, kelompokkan pelanggaran/gerak sah, taktik fast break dan
  man-to-man, skenario “Keputusan di menit terakhir”, kartu istilah, dan
  tantangan istilah.
- **PJOK 2 Permainan Sepak Bola** — peraturan PSSI dan lapangan FIFA, tabel
  teknik passing–heading, grafik ukuran lapangan, kelompokkan pelanggaran,
  taktik formasi 4-4-2 dan 4-3-3, skenario serangan menit akhir, serta
  tantangan istilah.
- **PJOK 3 Permainan Bola Tangan** — peraturan ABTI, lapangan 40 × 20 m,
  tabel catching–pivot, grafik ukuran gawang, kelompokkan pelanggaran tiga
  langkah/tiga detik, pola pertahanan 6-0 dan 5-1, skenario serangan cepat,
  dan tantangan istilah.
- **PJOK 4 Permainan Bola Voli** — sejarah William G. Morgan, aturan rally
  point dan rotasi, tabel servis–block, grafik tinggi net putra/putri,
  kelompokkan pelanggaran net/double touch, pola 4-2 dan 5-1, skenario set
  penentuan, dan tantangan istilah.
- **PJOK 5 Permainan Bulu Tangkis** — peraturan PBSI, lapangan dan net,
  tabel pegangan raket serta pukulan, grafik ukuran lapangan, kelompokkan
  pelanggaran, taktik lob–dropshot, skenario poin kritis 20-20, dan tantangan
  istilah.
- **PJOK 6 Atletik** — nomor jalan, lari, lompat, dan lempar; tabel start–
  tolak peluru, grafik berat peluru, kelompokkan nomor lari/lempar, prinsip
  keselamatan, skenario latihan lompat jauh, dan tantangan istilah.
- **PJOK 7 Senam** — senam lantai dan ketangkasan, tabel guling–handstand,
  grafik tingkat kesulitan, kelompokkan gerak berguling/keseimbangan,
  prinsip spotting, skenario latihan handstand, dan tantangan istilah.
- **PJOK 8 Gerak Berirama** — unsur senam irama, langkah dasar dan ayunan
  lengan, tabel unsur/gerak, grafik ketukan birama, kelompokkan langkah
  kaki/ayunan lengan, alat simpai–pita, skenario latihan kelompok, dan
  tantangan istilah.
- Kedelapan bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- **Buku PJOK X kini lengkap 8/8 bab**, seluruhnya memenuhi minimum §5.3
  (satu visual, empat aktivitas, dua skenario/tantangan, dua recall, tiga
  checkpoint per bab).

### Verifikasi
- `gamecenter:materi-import --dry-run` → 66 berkas, **0 gagal**.
- Impor sungguhan menambah **8 bab / 24 materi / 24 asesmen / 240 soal**
  (996 opsi jawaban pada delapan berkas PJOK).
- `gamecenter:materi-coverage` → **67 dari 70 chapter** memenuhi minimum §5.3,
  **2.435 blok**. PJOK 1–8 masing-masing 26 blok, semuanya ✅.
- `php artisan test` → **145 lulus, 1 dilewati, 1.464 asertion**; tes impor
  mengharapkan 66 bab dan 1.980 soal, tes cakupan memeriksa kedelapan bab
  PJOK dan halaman bermain PJOK 1.
- `npm run typecheck` dan `npm run build` → lulus.
- `gamecenter:deploy-check` → 0 gagal.

## [0.36.0] - 2026-11-18 06:05 WIB

**Batch 12 tuntas — buku IPS Kelas X 4/4 bab.**

### Ditambah
- **IPS 3 Manusia dan Upaya Pemenuhan Kebutuhan** (kajian ilmu ekonomi) —
  glosarium istilah ekonomi, diagram tiga pertanyaan pokok ekonomi, tabel
  kebutuhan vs keinginan, kelompokkan kebutuhan/keinginan, diagram alur
  produksi–distribusi–konsumsi, tabel pelaku ekonomi, urutkan perjalanan beras,
  diagram dan tabel permintaan–penawaran, grafik permintaan, kelompokkan bank
  vs lembaga keuangan nonbank, skenario “Uang saku bulan ini”, dan tantangan
  istilah.
- **IPS 4 Manusia, Ruang, dan Lingkungan** (kajian geografi) — glosarium
  objek dan aspek geografi, diagram tiga sudut pandang geografi, tabel konsep
  geografi, kelompokkan aspek fisik/sosial, tabel komponen peta, alur kerja
  SIG, grafik suhu menurut ketinggian, urutan langkah SIG, glosarium geosfer,
  diagram hubungan antarsfera, tabel jenis bencana dan mitigasi, garis waktu
  evakuasi gempa, kelompokkan mitigasi/adaptasi, skenario “Banjir di
  kampungmu”, kartu lapisan geosfer, dan tantangan istilah.
- Kedua bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- **Buku IPS X kini lengkap 4/4 bab** (Sejarah, Sosiologi, Ekonomi, Geografi),
  seluruhnya memenuhi minimum §5.3.

### Verifikasi
- `gamecenter:materi-import` → 58 berkas, **0 gagal**; impor sungguhan
  menambah **4 bab / 12 materi / 12 asesmen / 120 soal** (opsi jawaban 6.224).
- `gamecenter:materi-coverage` → **59 dari 62 chapter** memenuhi minimum §5.3,
  **2.227 blok**. IPS 1–4: 36, 34, 32, dan 30 blok, semuanya ✅.
- `php artisan test` → **143 lulus, 1 dilewati, 1.347 asertion**; tes impor
  mengharapkan 58 bab dan 1.740 soal, tes cakupan memeriksa keempat bab IPS.
- `gamecenter:deploy-check` → 0 gagal.

## [0.35.0] - 2026-11-18 05:00 WIB

**Batch 12 — IPS X dimulai: 2 dari 4 bab (Sejarah dan Sosiologi).**

### Ditambah
- **IPS 1 Manusia, Ruang, dan Waktu** (kajian ilmu sejarah) — glosarium istilah
  sejarah, diagram cara kerja ilmu sejarah, tabel kronologi/periodisasi/
  anakronisme, diagram tiga dimensi sejarah, garis waktu Nusantara,
  kelompokkan pertanyaan diakronik/sinkronik, glosarium sumber sejarah, tabel
  jenis sumber, urutan lima langkah penelitian, skenario “Meneliti sejarah
  sekolah”, dan tantangan istilah.
- **IPS 2 Individu dan Masyarakat** (kajian sosiologi) — diagram dari individu
  sampai masyarakat, tabel tokoh (Comte, Durkheim, Weber), tabel empat tipe
  tindakan sosial, tabel bentuk interaksi asosiatif/disosiatif, kelompokkan
  contoh interaksi, glosarium nilai–norma–lembaga, urutan penelitian sosial,
  skenario “Konflik di kelas”, dan tantangan istilah sosiologi.
- Kedua bab memakai **30 soal** (5 mudah / 10 sedang / 15 sulit) dengan
  campuran pilihan ganda, jawaban ganda, menjodohkan, seret-lepas, dan susun
  urutan; setiap soal ber-`explanation` dan soal sulit tanpa hint.
- Mapel **IPS Kelas X** kini benar-benar terisi (2 bab, 6 materi, 60 soal).

### Verifikasi
- `gamecenter:materi-import` → 56 berkas, **0 gagal**; impor sungguhan
  menambah **2 bab / 6 materi / 6 asesmen / 60 soal** (opsi jawaban 6.012).
- `gamecenter:materi-coverage` → **57 dari 60 chapter** memenuhi minimum §5.3,
  **2.165 blok**. IPS 1 (36 blok) dan IPS 2 (34 blok) lengkap.
- `php artisan test` → **143 lulus, 1 dilewati, 1.315 asertion**; tes baru
  menjaga kedua bab IPS memenuhi §5.3 dan halaman `/main/{asesmen}` IPS 1
  menyajikan 3 materi serta 5 soal.
- `gamecenter:deploy-check` → 0 gagal.

## [0.34.0] - 2026-11-18 04:15 WIB

**Batch 11 — Bahasa Inggris X tuntas 6/6 bab (ENG 1–ENG 6, 180 soal).**

### Ditambah
- **ENG 1 Great Athletes** — glosarium teks deskriptif, diagram struktur
  identification–description, tabel ciri bahasa, membaca teks Cristiano
  Ronaldo, kelompokkan fakta/opini, checkpoint, skenario “Menulis deskripsi
  atlet”, dan tantangan kilat.
- **ENG 2 Sports Events** — teks recount pribadi, diagram alur peristiwa,
  tabel kata kerja lampau dan kata penghubung waktu, membaca pengalaman
  menonton pertandingan, urutan kejadian, checkpoint, skenario dan tantangan.
- **ENG 3 Sports and Health** — teks prosedur, tabel struktur goal–steps,
  membaca tips kesehatan, kelompokkan kebiasaan sehat/tidak sehat, checkpoint,
  skenario kampanye kesehatan, dan tantangan kilat.
- **ENG 4 Healthy Foods** — prosedur dan tips pola makan sehat, tabel
  perbandingan pilihan makanan, kelompokkan makanan bergizi/kurang bergizi,
  checkpoint, skenario “Tantangan makan sehat”, dan tantangan kilat.
- **ENG 5 Graffiti** — dua teks ekspositori berseberangan, diagram struktur
  analytical exposition, tabel argumen–bukti, kelompokkan pernyataan
  Text 1/Text 2/both/neither, checkpoint, skenario survei publik, dan
  tantangan kilat.
- **ENG 6 Fractured Stories** — glosarium unsur naratif, diagram
  orientation–complication–resolution, tabel struktur dan unsur intrinsik,
  kartu hafalan, membaca Little Red Riding Hood versi tradisional dan versi
  serigala, kelompokkan detail kedua versi, urutan langkah menulis cerita
  pecahan, skenario “Menceritakan ulang Cinderella”, dan tantangan unsur cerita.
- **Mapel IPS (Kelas X)** pada `SubjectSeeder`, sehingga IPS terpadu siap
  menerima chapter Sejarah/Sosiologi/Ekonomi/Geografi pada batch berikutnya.
- Batasan jenjang mapel kini memakai kunci `grades` yang umum: **IPS** hanya
  Kelas X dan **Pemrograman Dasar** hanya SMK Kelas X.

### Verifikasi
- `gamecenter:materi-import --dry-run` → **54 berkas, 0 gagal**;
  impor sungguhan menambah **1 chapter / 3 materi / 3 asesmen / 30 soal**.
- `gamecenter:materi-coverage` → **55 dari 58 chapter memenuhi minimum §5.3**,
  **2.095 blok**. Bahasa Inggris **6/6 lengkap**; sisa tiga chapter di luar
  cakupan SMA/SMK (PAUD 1.1, TK 1.1, MTK 7.1).
- `php artisan test` → **141 lulus, 1 dilewati, 1.270 asertion**; dua tes
  regresi baru menjaga enam bab Bahasa Inggris tetap memenuhi §5.3 dan
  halaman `/main/{asesmen}` ENG 6 menyajikan blok materi beserta 5 soal.

## [0.33.0] - 2026-11-18 03:00 WIB

**Batch 10 — PEMDAS 1.1 menjadi interaktif; konversi materi SMA/SMK selesai.**

### Ditambah
- **PEMDAS 1.1 Algoritma dan Logika (materi Algoritma)** — glosarium (algoritma,
  pseudocode, input, output), diagram alur menghitung luas persegi panjang,
  urutan langkah menghitung luas, checkpoint pseudocode, dan checkpoint luas.
- **PEMDAS 1.1 materi Flowchart dan Logika** — glosarium (flowchart, proses,
  keputusan, logika boolean), tabel simbol flowchart, daftar aturan logika,
  diagram keputusan kelulusan, kelompokkan simbol flowchart, checkpoint
  `true AND false`, checkpoint `if (nilai >= 70)`, skenario “Membaca flowchart
  kelulusan dengan jujur”, dan tantangan kilat 5 butir.
- Kedua materi tetap menyimpan teks aslinya sebagai blok teks, sehingga
  `MaterialViewer` menampilkan teori sekaligus aktivitas.

### Verifikasi
- `gamecenter:materi-coverage` → **49 dari 52 chapter lengkap**, **1.850 blok**
  (1.469 blok teks + 381 aktivitas/visual). Hanya **PAUD 1.1**, **TK 1.1**, dan
  **MTK 7.1** yang tidak dikonversi karena di luar cakupan SMA/SMK.
- `php artisan test` → **138 lulus, 1 dilewati, 1.147 asertion**.
- Audit fidelitas: **0 materi** menyembunyikan isi.
- Tes regresi baru `test_pemdas_chapter_from_curated_seeder_stays_interactive`
  menjaga PEMDAS 1.1 tetap punya blok teks dan memenuhi minimum §5.3.

## [0.32.0] - 2026-11-18 02:30 WIB

**Batch 9 — Bahasa Indonesia tuntas 5/5 bab.**

### Ditambah
- **BI 1 Laporan Hasil Observasi** — diagram struktur laporan, glosarium
  (laporan hasil observasi, objektif, faktual, opini), checkpoint ciri bahasa,
  kelompokkan fakta/opini, urutan tiga hal yang diperiksa untuk akurasi,
  checkpoint bias, checkpoint teks eksplanasi, checkpoint diagram lingkaran,
  skenario “Presentasi laporan hasil observasi”, dan tantangan kilat 6 butir.
- **BI 2 Kritik Sosial lewat Anekdot** — glosarium (anekdot, eksposisi, stand
  up comedy, koda), urutan struktur anekdot, checkpoint alasan memakai humor,
  diagram kritik/celaan/ancaman, kelompokkan fakta/opini, checkpoint celaan,
  checkpoint menyimak aural, urutan menyusun anekdot, skenario “Menyampaikan
  kritik tentang antrean kantin”, dan tantangan kilat 6 butir.
- **BI 3 Hikayat dan Cerpen** — diagram perbandingan hikayat/cerpen, glosarium
  (hikayat, kata arkais, cerpen, amanat), checkpoint kata arkais, kelompokkan
  ciri hikayat/cerpen, checkpoint karakterisasi tidak langsung, urutan bagian
  plot, checkpoint antagonis, urutan menulis fiksi dari nilai hikayat, skenario
  “Mempublikasikan cerpen di media digital”, dan tantangan kilat 6 butir.
- **BI 4 Teks Negosiasi** — glosarium (negosiasi, debat, kompromi), urutan
  struktur negosiasi, checkpoint beda negosiasi/debat, diagram bahasa santun,
  kelompokkan kalimat santun/menekan, checkpoint menolak dengan santun,
  checkpoint isi kesepakatan, urutan menyiapkan negosiasi, skenario “Menawar
  harga perlengkapan kelas”, dan tantangan kilat 6 butir.
- **BI 5 Teks Biografi** — diagram struktur biografi, glosarium (biografi,
  autobiografi, ide pokok, tersirat), checkpoint reorientasi, urutan menemukan
  ide pokok, checkpoint makna tersirat, kelompokkan kata baku/tidak baku,
  checkpoint kutipan, checkpoint tanda titik, urutan menulis biografi, skenario
  “Menilai biografi tanpa sumber”, dan tantangan kilat 6 butir.

### Verifikasi
- `gamecenter:materi-coverage` → **Bahasa Indonesia 5/5 chapter lengkap**;
  total aplikasi **48 dari 52 chapter**, **1.828 blok** (1.459 blok teks + 369
  aktivitas/visual).
- Tes fidelitas dan coverage lulus; satu tes dilewati karena seluruh chapter
  pada seeder utama sudah memenuhi minimum.
- Audit fidelitas: **0 materi** menyembunyikan isi.

## [0.31.0] - 2026-11-18 02:00 WIB

**Batch 8 — Pancasila tuntas 4/4 bab.**

### Ditambah
- **PAN 2 Membangun Budaya Taat Hukum** — lini masa perjalanan konstitusi
  Indonesia, glosarium (konstitusi, konvensi, norma), checkpoint konstitusi,
  kelompokkan sumber dan contoh empat norma, urutan hierarki peraturan,
  diagram Pancasila sebagai sumber segala sumber hukum, checkpoint asas lex
  superior, checkpoint perda yang bertentangan dengan UU, urutan membuat
  kesepakatan, checkpoint analisis peraturan, tantangan kilat 6 butir,
  kelompokkan pelanggaran menurut sanksi, dan skenario “Lampu merah di jalan
  yang sepi”.
- **PAN 3 Mengelola Kebinekaan** — diagram identitas given/pilihan beserta
  pembentuknya, glosarium, kelompokkan contoh identitas, checkpoint Bhinneka
  Tunggal Ika, urutan tahap kolaborasi, checkpoint sikap dalam pertukaran
  budaya global, kelompokkan sikap terbuka/menutup/menerima tanpa saring,
  kelompokkan empat kearifan lokal menurut daerah, checkpoint kebinekaan
  sebagai modal sosial, skenario “Festival budaya kelas”, dan tantangan kilat
  6 butir.
- **PAN 4 Menjadi Warga Negara yang Baik** — glosarium (paham kebangsaan,
  nasionalisme, chauvinisme, patriotisme), kelompokkan nasionalisme/chauvinisme,
  checkpoint wujud patriotisme, diagram empat unsur negara, urutan unsur
  Montevideo, checkpoint Pasal 25A, kelompokkan ancaman militer/nonmiliter,
  diagram jalur penyelesaian sengketa batas, checkpoint Sipadan-Ligitan,
  checkpoint Ambalat, skenario “Berita bohong tentang wilayah Indonesia”, dan
  tantangan kilat 6 butir.

### Verifikasi
- `gamecenter:materi-coverage` → **Pancasila 4/4 chapter lengkap**; total
  aplikasi **43 dari 52 chapter**, **1.597 blok** (1.279 blok teks + 318
  aktivitas/visual).
- Tes fidelitas dan coverage lulus (5 tes / 80 asertion).
- Audit fidelitas: **0 materi** menyembunyikan isi.

## [0.30.0] - 2026-11-18 01:30 WIB

**Batch 7b — PAI 6 sampai PAI 10, PAI tuntas 10/10 bab.**

### Ditambah
- **PAI 6 Pergaulan Bebas dan Zina** — diagram larangan bertahap, glosarium
  (zina, muhsan, ghayr muhsan, pornografi), checkpoint larangan mendekati zina,
  checkpoint istilah muhsan, kelompokkan pergaulan bebas/sehat, checkpoint
  dampak pada belajar, urutan menghadapi tekanan teman, skenario “Tekanan teman
  untuk melanggar batas”, dan tantangan kilat 5 butir.
- **PAI 7 Mahabbah, Khauf, Raja', Tawakal** — glosarium, checkpoint tanda cinta
  kepada Allah, urutan cara menumbuhkan cinta, diagram keseimbangan khauf dan
  raja', checkpoint akibat khauf tanpa raja', kelompokkan khauf/raja',
  kelompokkan tawakal/malas, urutan tawakal menghadapi ujian, skenario “Hasil
  ujian tidak sesuai harapan”, dan tantangan kilat 5 butir.
- **PAI 8 Akhlak Madzmumah dan Mahmudah** — glosarium, checkpoint ghadhab,
  urutan mengendalikan marah, diagram kontrol diri dan manfaatnya, checkpoint
  husnuzan, kelompokkan akhlak mahmudah/madzmumah, checkpoint syaja'ah, urutan
  menumbuhkan syaja'ah, skenario “Ajakan curang saat ujian”, dan tantangan
  kilat 6 butir.
- **PAI 9 Al-Kulliyatu al-Khamsah** — diagram lima prinsip, glosarium
  (al-kulliyatu al-khamsah, kulliyah, maqashid syariah, hifzhu al-din), urutan
  lima prinsip, checkpoint alasan agama pertama, kelompokkan contoh penerapan
  per prinsip, checkpoint keterkaitan akal dan jiwa, urutan menyelesaikan
  masalah, skenario “Tekanan teman untuk mencoba zat berbahaya”, dan tantangan
  kilat 6 butir.
- **PAI 10 Wali Songo** — diagram empat kunci keberhasilan dakwah, glosarium
  (Wali Songo, dakwah, pesantren, dai), kelompokkan sembilan wali menurut
  pendekatan, checkpoint arti Wali Songo, glosarium dakwah moderat, checkpoint
  bi al-hikmah, urutan strategi dakwah damai, kelompokkan sikap dakwah
  moderat, checkpoint dampak terhadap budaya, skenario “Menghargai teman yang
  berbeda keyakinan”, dan tantangan kilat 6 butir.

### Verifikasi
- `gamecenter:materi-coverage` → **PAI 10/10 chapter lengkap**; total aplikasi
  **40 dari 52 chapter**, **1.463 blok** (1.181 blok teks + 282
  aktivitas/visual).
- Tes fidelitas dan coverage lulus (5 tes / 80 asertion).
- Audit fidelitas: **0 materi** menyembunyikan isi.

## [0.29.0] - 2026-11-18 01:00 WIB

**Batch 7a — PAI 1 sampai PAI 5 menjadi materi interaktif.**

### Ditambah
- **PAI 1 Kompetisi dalam Kebaikan dan Etos Kerja** — diagram ciri fastabiqul
  khairat, glosarium (fastabiqul khairat, asbabun nuzul, syariat, istiqamah),
  checkpoint asbabun nuzul, kelompokkan sikap kompetisi benar/salah, urutan
  tiga syarat pekerjaan, checkpoint Q.S. at-Taubah/9: 105, kelompokkan etos
  kerja seimbang/berlebihan, skenario “Melihat teman lebih berprestasi”, dan
  tantangan kilat 5 butir.
- **PAI 2 Syu'abul Iman** — glosarium (syu'abul iman, iman, tauhid, rukun
  iman), checkpoint cabang iman tertinggi, checkpoint tiga unsur iman, diagram
  tiga wilayah cabang iman, kelompokkan amal hati/lisan/perbuatan, checkpoint
  ihsan, urutan langkah menumbuhkan cabang iman, skenario “Menahan amarah saat
  diejek”, dan tantangan kilat 5 butir.
- **PAI 3 Berfoya-foya, Riya', Sum'ah, Takabur, Hasad** — glosarium, checkpoint
  pemboros sebagai saudara setan, kelompokkan riya'/sum'ah, diagram takabur vs
  tawadu, checkpoint hasad, kelompokkan hasad/ghibtah, urutan langkah
  membersihkan hati dari riya', kelompokkan perilaku tercela dan penggantinya,
  skenario “Amal yang mulai mengharap pujian”, dan tantangan kilat 6 butir.
- **PAI 4 Asuransi, Bank, dan Koperasi Syariah** — diagram memilih akad,
  glosarium tujuh istilah (akad, mudarabah, musyarakah, wadiah, tabarru', riba,
  gharar), checkpoint riba, urutan utang sehat, kelompokkan ciri asuransi
  konvensional/syariah, checkpoint dana tabarru', checkpoint wadiah, urutan
  etika memilih lembaga keuangan, skenario “Tawaran pinjaman online untuk
  membeli gawai”, dan tantangan kilat 7 butir.
- **PAI 5 Meneladani Ulama Penyebar Islam** — diagram lima jalur masuknya
  Islam, checkpoint kerajaan Islam pertama, kelompokkan kesultanan menurut
  wilayah, glosarium (ulama, pesantren, mufasir, sufi), kelompokkan tokoh
  menurut daerah, checkpoint Hamzah Fansuri, checkpoint pesantren, kelompokkan
  sikap terhadap budaya, skenario “Berdakwah di lingkungan sekolah yang
  beragam”, dan tantangan kilat 6 butir.

### Verifikasi
- `gamecenter:materi-coverage` → **PAI 1–5 lengkap 5/5**; total aplikasi
  **35 dari 52 chapter**, **1.268 blok** (1.035 blok teks + 233 aktivitas/visual).
- `php artisan test` → 23 tes terkait materi lulus (356 asertion), termasuk
  `MateriContentFidelityTest` dan `MateriCoverageCommandTest`.
- Audit fidelitas: **0 materi** menyembunyikan isi.

## [0.28.0] - 2026-11-18 00:30 WIB

**Batch 6 (Informatika tuntas 8/8 bab) + pemulihan teks materi yang hilang.**

### Ditambah
- **INF 2 Teknologi Informasi dan Komunikasi** — diagram alur integrasi data,
  glosarium (pengolah kata, pengolah angka, tautkan, tanamkan), checkpoint
  link/embed, urutan langkah mail merge, checkpoint pivot table, dan tantangan
  kilat 5 butir.
- **INF 3 Sistem Komputer** — diagram empat kelompok komponen, glosarium (ALU,
  control unit, register, RAM, cache), checkpoint RAM volatile, urutan proses
  boot, checkpoint siklus fetch-decode-execute, dan tantangan kilat 5 butir.
- **INF 4 Jaringan Komputer dan Internet** — diagram LAN → internet,
  glosarium (LAN, switch, router, access point, alamat IP), checkpoint router,
  kelompokkan media kabel/nirkabel, checkpoint bandwidth, dan tantangan kilat
  proteksi data.
- **INF 5 Analisis Data** — grafik batang survei hobi 40 siswa, glosarium
  (data, informasi, sel, rentang), checkpoint AVERAGE, urutan tahapan analisis,
  checkpoint data kotor, kelompokkan jenis grafik, checkpoint rata-rata,
  dan tantangan kilat.
- **INF 6 Algoritma dan Pemrograman** — diagram algoritma luas, glosarium
  (algoritma, variabel, konstanta, mod), checkpoint 7 mod 2, urutan keluaran
  perulangan, checkpoint keputusan bersarang, dan tantangan kilat pelacakan.
- **INF 7 Dampak Sosial Informatika** — lini masa sejarah komputasi,
  glosarium (mesin Turing, ENIAC, Revolusi Industri 4.0, UU ITE), checkpoint
  WWW, kelompokkan dampak ekonomi, checkpoint etika data, urutan merancang
  gagasan, dan tantangan kilat.
- **INF 8 Praktika Lintas Bidang** — diagram abstraksi sistem perpustakaan,
  glosarium (abstraksi, kolaborasi digital, prototipe, kasus uji), checkpoint
  abstraksi, urutan membangun artefak, checkpoint hasil uji, dan tantangan
  kilat.

### Diperbaiki
- **Teks materi tidak lagi hilang dari layar.** `MaterialViewer` merender
  `blocks` **atau** markdown, bukan keduanya. Batch 2–6 hanya menambahkan blok
  interaktif, sehingga **79 materi** (7.745 kata penjelasan) tidak pernah
  tampil — siswa hanya melihat grafik, glosarium, dan soal tanpa uraiannya.
  Kini seluruh isi markdown dikonversi menjadi blok teks (`heading`,
  `paragraph`, `list`, `table`, `callout`, `code`), dan blok interaktif
  disisipkan pada bagian yang paling relevan: glosarium di awal
  (*pre-training*), checkpoint setelah konsep dijelaskan, visual setelah tabel
  atau bagian yang cocok, tantangan/skenario di akhir. **85 materi** diperbaiki.
- **`gamecenter:materi-coverage`** menambah kolom **Blok** dan **Teori** serta
  peringatan **"teks tidak tampil"** bila ada materi berblok tanpa blok teks.
- **`tests/Feature/MateriContentFidelityTest.php`** (baru) — mengunci dua
  aturan: materi berblok wajib punya blok teks (≥70 % kata konten) dan setiap
  judul `##`/`###` wajib muncul sebagai blok judul.

### Diubah
- **`public/sw.js`** — `CACHE_VERSION` 0.28.0.
- **`tools/rapikan-blok-fase5.py`** (baru) — konverter markdown → blok teks
  dengan penempatan blok interaktif berbasis kecocokan kata kunci; idempoten
  (melewati materi yang teksnya sudah lengkap).

### Verifikasi
- `gamecenter:materi-coverage` → **Informatika 8/8 chapter lengkap**;
  total aplikasi **30 dari 52 chapter**, **1.062 blok** (185 aktivitas/visual +
  877 blok teks).
- `php artisan test` **140 tes / 1.148 asertion** lulus.
- Audit fidelitas: **0 materi** menyembunyikan isi (sebelumnya 79).

## [0.27.0] - 2026-11-17 23:55 WIB

**Skala konten §5.3 batch 5 — Matematika tuntas 13/13 bab.**

### Ditambah
- **MA 6.2 Membentuk & Mengubah Bentuk Fungsi Kuadrat** — diagram tiga bentuk
  (umum, puncak, faktor), glosarium, checkpoint bentuk puncak, urutan langkah
  melengkapi kuadrat, checkpoint (x − 5)² − 7, dan tantangan kilat 5 butir.
- **MA 6.3 Masalah dengan Fungsi Kuadrat** — grafik garis h(t) = −5t² + 20t,
  glosarium (maksimum, minimum, tujuan, akar), checkpoint a < 0, urutan empat
  langkah baku, checkpoint pagar taman 450 m², dan tantangan kilat (hasil kali
  100, laba 100 ribu, tinggi 20 m, mendarat 4 detik).
- **MA 7.1 Statistika** — grafik batang data 7, 8, 8, 9, 10, glosarium (mean,
  median, modus, jangkauan), checkpoint median data genap, kelompokkan ukuran
  yang terpengaruh nilai ekstrem, checkpoint kasus gaji direktur, dan tantangan
  kilat (total 40, data kelima 8, jangkauan 3, modus 8, mean baru 11).
- **MA 8.1 Peluang** — grafik batang banyak pasangan dua dadu (jumlah 2–7),
  glosarium (ruang sampel, kejadian, komplemen, saling bebas), checkpoint
  n(S) = 36, urutan langkah menghitung peluang, checkpoint komplemen 5/6, dan
  tantangan kilat (4, 8, 36, 1/6, 5/6).

### Diubah
- **`public/sw.js`** — `CACHE_VERSION` 0.27.0.

### Verifikasi
- `gamecenter:materi-coverage` → **Matematika 13/13 chapter lengkap §5.3**;
  total aplikasi **23 dari 52 chapter, 159 blok interaktif** (sebelumnya 19
  chapter / 135 blok).
- `php artisan test` **137 tes / 1.132 asertion** lulus setelah impor ulang.
- Uji browser (CDP + vision): `/main/43` (MA 6.3) grafik h(t) dengan puncak
  (2, 20) dan titik mendarat (4, 0) tampil benar; `/main/55` (MA 7.1) grafik
  data + glosarium + soal median; materi 2 menampilkan "Kelompokkan ukuran
  statistika"; `/main/58` (MA 8.1) dirender tanpa galat. Tidak ada galat konsol.

## [0.26.0] - 2026-11-17 23:05 WIB

**Skala konten §5.3 batch 4: Matematika lanjutan + perbaikan diagram.**

### Ditambah
- **MA 3.1 Vektor** — diagram komponen v = (3, 4), glosarium (skalar, vektor,
  komponen, vektor satuan), checkpoint panjang vektor, urutan langkah vektor
  satuan, checkpoint AB = (3, 4), dan tantangan kilat 5 butir.
- **MA 4.1 Trigonometri** — glosarium (sin, cos, tan, identitas), checkpoint
  definisi tan, grafik batang nilai sin pada sudut istimewa, checkpoint
  tan 90° tak terdefinisi, dan tantangan kilat (90°, tan 45°, identitas,
  sin 30° = cos 60°, tinggi tiang 10 m).
- **MA 5.1 Sistem Persamaan Linear** — diagram tiga kemungkinan penyelesaian,
  glosarium, checkpoint penyelesaian tunggal, urutan langkah substitusi,
  checkpoint nilai y, dan tantangan kilat (x, y, harga pulpen/buku, x = 2).
- **MA 5.2 Pertidaksamaan Linear** — diagram pemilihan garis penuh/putus-putus,
  glosarium, checkpoint uji titik asal, urutan langkah nilai optimum,
  checkpoint maksimum 13 di (2, 3), dan tantangan kilat (luas 16, uji titik,
  nilai 12, "penuh", "balik").

### Diperbaiki
- **`resources/js/lib/material/diagram.ts`** — label node kini **dibungkus ke
  beberapa baris** (`wrapLabel`) dan tinggi kotak menyesuaikan jumlah baris,
  dengan pemotongan aman untuk kata yang lebih panjang dari kotak. Sebelumnya
  label panjang seperti "Tanda kurang dari sama dengan atau lebih dari sama
  dengan" terpotong di tepi kotak; kini semua diagram aman.
- **`public/sw.js`** — `CACHE_VERSION` 0.26.0.

### Verifikasi
- `gamecenter:materi-coverage` → **19 dari 52 chapter** memenuhi §5.3, total
  **135 blok interaktif** (sebelumnya 15 chapter / 112 blok).
- `php artisan test` **137 tes / 1.132 asertion** lulus setelah impor ulang.
- `./node_modules/.bin/tsc --noEmit` bersih; `npm run build` sukses.
- Uji browser (CDP + vision): `/main/46` (MA 3.1) diagram vektor + glosarium +
  Cek pemahaman tampil rapi; `/main/52` (MA 5.2) dua label cabang panjang kini
  terbungkus dua baris **tanpa terpotong**; `/main/91` (BIO 1) diagram virus
  seluruh label berada di dalam kotak. Tidak ada galat konsol.

## [0.25.0] - 2026-11-17 22:15 WIB

**Skala konten §5.3 batch 3: Fisika 2 dan Matematika (eksponen lanjut).**

### Ditambah
- **FIS 2 Usaha, Energi, dan Energi Terbarukan** — glosarium (usaha, daya, Ek,
  Ep), grafik batang faktor cos θ (0°, 30°, 60°, 90°), checkpoint "usaha nol
  saat gaya tegak lurus", urutan langkah kekekalan energi mekanik, checkpoint
  jatuh bebas (10 m/s), kelompokkan sumber terbarukan/fosil, dan tantangan
  kilat 5 butir (60 J, 12 W, PLTA, kuadrat, 0 J).
- **MA 1.2 Logaritma** — glosarium (logaritma, basis, numerus, ln), grafik
  batang ²log x (1–16), checkpoint ⁵log 1 = 0, urutan langkah menggabungkan
  log, checkpoint ²log 8² = 6, dan tantangan kilat (²log 16, ²log 8, ⁹log 1,
  pH, desibel).
- **MA 2.1 Barisan** — glosarium (barisan, beda, rasio, suku pertama), grafik
  garis aritmetika vs geometri, checkpoint beda b = 4, urutan langkah mencari
  beda dari U₃ dan U₇, checkpoint U₁₀ = 41, dan tantangan kilat (U₁₀ = 41,
  U₈ = 384, 40 kursi, r = 3, b = 4).
- **MA 2.2 Deret** — glosarium (deret, Sₙ, konvergen, Uₙ = Sₙ − Sₙ₋₁), grafik
  batang jumlah kumulatif S₁–S₅, checkpoint U₅ = 14, urutan langkah menghitung
  S₁₀, checkpoint deret tak hingga = 16, dan tantangan kilat (210, 242, 16, 1,
  Rp2.850.000).

### Diubah
- **`public/sw.js`** — `CACHE_VERSION` 0.25.0.

### Verifikasi
- `gamecenter:materi-coverage` → **15 dari 52 chapter** memenuhi §5.3, total
  **112 blok interaktif** (sebelumnya 11 chapter / 87 blok).
- `php artisan test` **137 tes / 1.132 asertion** lulus setelah impor ulang
  (48 chapter, 146 materi, 1.440 soal, 5.148 opsi).
- Uji browser (CDP + vision): `/main/103` (FIS 2) menampilkan glosarium,
  grafik batang "Faktor cos θ pada usaha", dan "Cek pemahaman" tanpa tumpang
  tindih; `/main/25` (MA 1.2) menampilkan glosarium, grafik "Nilai ²log x",
  dan soal pilihan; kelompokkan sumber energi tampil pada materi 3. Tidak ada
  galat konsol.

## [0.24.0] - 2026-11-17 21:30 WIB

**Skala konten §5.3 batch 2: Kimia & Biologi.**

### Ditambah
- **KIM 1 Struktur Atom dan Nanoteknologi** — diagram susunan atom, glosarium
  (nomor atom, nomor massa, isotop, elektron valensi), 2 checkpoint, dan
  tantangan kilat 5 butir (proton, isotop, neutron, kulit M, skala nano).
- **KIM 2 Hukum Dasar Kimia** — glosarium, urutan langkah menyetarakan reaksi,
  lini masa Lavoisier–Proust–Dalton–Gay Lussac, aktivitas kelompokkan hukum,
  checkpoint penyetaraan, dan tantangan hitungan (88 g, 32 g, 6 g, 20 L, 64 g).
- **KIM 3 Kimia Hijau** — glosarium, diagram siklus kerja kimia hijau,
  checkpoint prinsip pencegahan, kelompokkan penerapan/pelanggaran, dan
  skenario 7 node "sampah plastik kantin" (3 akhir: baik/netral/buruk).
- **BIO 1 Virus dan Peranannya** — diagram struktur virus, glosarium, 2
  checkpoint (parasit obligat, siklus lisogenik), urutan 5 tahap siklus litik,
  dan tantangan istilah (bakteriofag, kapsid, Plasmodium, RNA, viroida).
- **BIO 2 Keanekaragaman Hayati** — diagram tiga tingkat, glosarium, 2
  checkpoint (endemik, aliran energi), urutan 7 takson, kelompokkan in situ/ex
  situ, dan skenario 7 node "ular hilang, tikus meledak".
- **BIO 3 Perubahan Iklim** — diagram efek rumah kaca, glosarium, checkpoint
  gas non-GRK & pemutihan karang, kelompokkan mitigasi/adaptasi, dan skenario
  7 node "dana kecil untuk program iklim sekolah".

### Diubah
- **`tests/Feature/MateriCoverageCommandTest.php`** — tes chapter "belum
  lengkap" kini memilih chapter pertama dari `--only-incomplete`, sehingga
  tidak usang setiap batch konversi selesai.
- **`public/sw.js`** — `CACHE_VERSION` 0.24.0.

### Verifikasi
- `gamecenter:materi-coverage` → **11 dari 52 chapter** memenuhi §5.3,
  total **87 blok interaktif** (sebelumnya 5 chapter / 52 blok).
- `php artisan test` **137 tes / 1.132 asertion** lulus setelah impor ulang
  (48 chapter, 146 materi, 1.440 soal, 5.148 opsi).
- Uji browser (CDP): `/main/106` (KIM 1) menampilkan diagram atom, glosarium,
  dan "Cek pemahaman"; `/main/94` (BIO 2) skenario "ular" berjalan dua langkah
  dan berakhir "Skenario selesai · Keputusan yang baik · Skor keputusan 4 dari
  4 (100%)"; kelompokkan in situ/ex situ tampil "0/6 sudah dipilih". Tidak ada
  galat konsol.

## [0.23.1] - 2026-11-17 20:35 WIB

**Toast "Tidak tersambung ke server" kini bisa ditindaklanjuti.**

### Diubah
- **`inertia:networkError`** (`resources/js/app.tsx`) — toast kegagalan jaringan
  tidak lagi menutup sendiri dan menyediakan tombol **Coba lagi**; sebelumnya
  siswa hanya melihat pesan dan tidak tahu harus berbuat apa.
- **Pesan lebih jujur** (`resources/js/lib/friendly-error.ts`) — deskripsi
  menyebut dua kemungkinan nyata: internet terputus **atau** server tidak
  merespons, bukan hanya menyalahkan koneksi pengguna.
- **`resources/js/lib/connection.ts`** (baru) — `retryConnection()` mengecek
  `/up` lebih dulu: bila server siap halaman dimuat ulang, bila belum muncul
  toast "Server belum siap"/"Masih tidak tersambung" sehingga tidak ada
  reload sia-sia ke halaman galat peramban.
- **`resources/js/lib/toast.ts` + `ToastHub`** — toast mendukung `action`
  (label + callback) dengan durasi lebih panjang.
- **`public/sw.js`** — `CACHE_VERSION` 0.23.1.

### Penyebab insiden
Server pengembangan `php artisan serve` di port 8000 berhenti (proses dimatikan
saat bersih-bersih pengujian), sehingga setiap navigasi Inertia gagal
`fetch`. Server sudah dijalankan kembali; aplikasi normal.

### Verifikasi
- `./node_modules/.bin/tsc --noEmit` bersih; `npm run build` sukses.
- Uji browser (CDP): server dimatikan → klik menu memunculkan toast
  "Tidak tersambung ke server … Coba lagi"; tekan **Coba lagi** saat server
  masih mati → muncul "Masih tidak tersambung" **tanpa** reload; server
  dinyalakan lalu **Coba lagi** → halaman `/panduan` termuat normal, tanpa
  pesan galat.
- `php artisan test tests/Feature/ProgressPageTest.php tests/Feature/ChapterRecapPanelTest.php`
  lulus (8 tes / 85 asertion).

## [0.23.0] - 2026-11-17 19:40 WIB

**Rekap formatif & skala konten (Fase 5 `plan-materi-interaktif.md`).**

### Ditambah
- **`BlockPracticeReport`** (`app/Services/Materi/BlockPracticeReport.php`) —
  satu sumber data untuk laporan siswa, rekap guru, CSV, dan audit blok:
  `forStudent()`, `forChapter()`, `chapterCsv()`, `blockAudit()`, plus label
  tipe blok berbahasa Indonesia.
- **Kartu "Latihan interaktif" di `/progres`** (Fase 5.5) — ringkasan blok
  dikerjakan/tuntas/rata-rata skor, lalu daftar per materi berisi chip tipe
  blok + skor dan tautan "Buka". Diberi keterangan tegas **formatif, bukan
  nilai rapor**; kosong jika siswa belum mengerjakan blok.
- **Rekap guru di panel Filament** (Fase 5.3) — bagian "Latihan interaktif
  (formatif)" pada halaman chapter: total blok/siswa/tuntas/rata-rata, tabel
  **per blok** (materi, id blok, tipe, tuntas, percobaan, rata-rata) dan tabel
  **per siswa** (nama, kelas, blok, percobaan, rata-rata, terakhir).
- **Ekspor CSV** (Fase 5.4) — aksi header "Ekspor CSV skor blok" pada halaman
  chapter (muncul bila ada skor). Berisi satu baris per siswa × blok dengan
  BOM UTF-8 supaya rapi dibuka di Excel, dan nama bernilai koma tetap dikutip.
- **Pratinjau & validasi blok** (Fase 5.2) — bagian baru di halaman chapter:
  daftar blok tiap materi beserta tipe, id, ringkasan, dan status validasi
  dari `BlockSchema`; blok bermasalah ditandai merah beserta pesan galatnya.
- **`php artisan gamecenter:materi-coverage`** (Fase 5.1) — laporan kesiapan
  konten per chapter terhadap minimum §5.3 (visual, ≥2 aktivitas,
  skenario/tantangan, glossary/flashcards, checkpoint per ±500 kata) dengan
  opsi `--chapter=`, `--json`, `--only-incomplete`.
- **Konten batch 1** — PAN 1, MA 1.1, MA 6.1, INF 1, dan FIS 1 kini memenuhi
  minimum §5.3: lini masa perumusan Pancasila, grafik 2^x, glosarium,
  checkpoint beralasan, tantangan kilat, dan urutan langkah eksponen.

### Diubah
- **`LearningMaterial`** — relasi `blockResponses()` untuk rekap/CSV.
- **`ProgressController`** — mengirim prop `block_practice` (terpisah dari
  statistik sesi).
- **`public/sw.js`** — `CACHE_VERSION` 0.23.0.

### Verifikasi
- `php artisan test` **137 tes / 1.133 asertion** lulus (bertambah 13 tes:
  laporan 5, panel 4, cakupan 3).
- `./node_modules/.bin/tsc --noEmit` bersih; `npm run build` sukses.
- `gamecenter:materi-coverage` → 5/52 chapter "lengkap" (batch 1), 52 blok
  interaktif; sisanya tercatat sebagai backlog 5.1.
- Uji browser: kartu "Latihan interaktif" tampil di `/progres` dengan chip
  skenario/tantangan; panel chapter menampilkan rekap per siswa + per blok,
  pratinjau validasi "semua blok valid", dan aksi ekspor CSV.

## [0.22.1] - 2026-11-17 18:20 WIB

**Perbaikan pesan galat saat server tidak terjangkau.**

### Diperbaiki
- **Toast "Layanan sedang sibuk" yang menyesatkan.** Service worker dulu
  mengubah kegagalan jaringan pada kunjungan Inertia (`X-Inertia`) menjadi
  respons buatan berstatus **503**, sehingga aplikasi menampilkan "Layanan
  sedang sibuk — kami sedang menyiapkan layanan kembali" padahal masalahnya
  server/HP sedang offline. Sekarang request Inertia diteruskan langsung ke
  jaringan tanpa intercept, jadi Inertia memicu `inertia:networkError` dan
  pengguna melihat pesan yang benar: **"Tidak tersambung ke server"** beserta
  saran memeriksa koneksi. Fungsi `networkOnlyJson` dihapus.
- **`public/sw.js`** — `CACHE_VERSION` 0.22.1 agar service worker lama
  diganti saat halaman berikutnya dibuka.

### Verifikasi
- Reproduksi: server dimatikan → klik tautan Inertia → sebelumnya toast
  "Layanan sedang sibuk" (status 503 buatan SW). Sesudah perbaikan → toast
  "Tidak tersambung ke server", tanpa status 503.
- Server hidup kembali → navigasi Inertia normal, cache shell tetap 0.22.1.

## [0.22.0] - 2026-11-17 17:35 WIB

**Skenario bercabang dan tantangan kilat (Fase 4 `plan-materi-interaktif.md`).**

### Ditambah
- **`ScenarioBlock.tsx`** — pemutar skenario bercabang: situasi → pilihan →
  umpan balik → lanjut, ringkasan seluruh keputusan di akhir, skor keputusan
  (bukan nilai akademik) yang disimpan lewat `useBlockAnswer`, tombol
  "Ulangi skenario", dan seluruh pilihan berupa `<button>` agar bisa dipakai
  keyboard (plan §7.2). Satu skenario menghasilkan satu baris
  `material_block_responses` dengan `details.path` + `details.choices` untuk
  pembahasan guru.
- **`ChallengeBlock.tsx`** — tantangan kilat berwaktu: 5–8 butir jawaban
  singkat, hitung mundur 60–120 detik yang **boleh dimatikan** sebelum mulai,
  pencocokan jawaban toleran huruf besar/kecil, spasi, dan tanda baca, lalu
  daftar butir yang salah beserta jawaban benarnya. Rekor pribadi memakai
  mekanisme skor blok yang sama (best score, jumlah percobaan).
- **`ScenarioValidator`** (`app/Services/Materi/ScenarioValidator.php`) —
  pemeriksa graf skenario: id node unik, `next` harus menunjuk node yang ada,
  setiap node bercabang minimal satu pilihan, semua node dapat dicapai dari
  `start`, setiap node punya jalan menuju node akhir (menangkap siklus tak
  berujung), minimal satu node `end`, dan maksimal 15 node. Dipakai
  `BlockSchema` sehingga validator materi dan perintah impor ikut memeriksanya.
- **`tests/Unit/ScenarioValidatorTest.php`** (10 tes) + satu tes impor baru
  yang memastikan skenario Pancasila valid dan tantangan matematika berisi
  5–8 butir.

### Diubah
- **`BlockRenderer.tsx`** — `scenario` dan `challenge` kini dirender; daftar
  `PENDING_LABEL` kosong karena 18 tipe blok sudah punya tampilan. Tipe blok
  di luar skema tetap jatuh ke catatan "belum tersedia".
- **Konten PAN 1** — submateri "Menerapkan Pancasila dalam Kehidupan
  Berbangsa" bertipe `scenario` dengan skenario rapat kelas 7 node (tiga
  akhir: baik/netral/kurang) dan satu callout.
- **Konten MA 1.1** — submateri "Sifat-Sifat Eksponen" ditutup tantangan
  kilat 6 butir / 90 detik tentang sifat pangkat.
- **`public/sw.js`** — `CACHE_VERSION` 0.22.0.

### Verifikasi
- `./node_modules/.bin/tsc --noEmit` bersih; `npm run build` sukses.
- `php artisan test` **124 tes / 997 asertion** lulus (bertambah 11 tes).
- `php artisan gamecenter:materi-import` tanpa galat validasi (0 chapter
  baru, 146 materi diperbarui).
- Uji browser (Chrome CDP): skenario PAN 1 menampilkan 3 pilihan, umpan balik
  muncul setelah memilih, ringkasan akhir berisi 2 keputusan + skor, dan skor
  tersimpan di localStorage (`gamecenter.blocks.112` → `sc-rapat-kelas`);
  tantangan MA 1.1 menghitung mundur, menerima jawaban "8" sebagai benar,
  menampilkan "Jawabanmu: 9 · seharusnya 8" untuk butir yang salah, dan
  mencatat rekor 100%. Tidak ada error konsol, dan kedua baris blok masuk
  `material_block_responses` (skor 100, completed) lewat antrean sync.

## [0.21.0] - 2026-11-17 16:20 WIB

**Visual learning: diagram, grafik, gambar berlabel, lini masa, dan aktivitas
beri label (Fase 0 + Fase 3 `plan-materi-interaktif.md`).**

### Ditambah
- **`tools/pdf-extract-images.py`** — pipeline aset buku ajar: mengekstrak
  gambar raster (dimensi & ukuran minimum, konversi CMYK→RGB, dedupe via
  checksum) **dan** merender potongan halaman (`--render-pages`,
  `--render-clip`, `--render-dpi`) untuk figur vektor. Setiap berkas tercatat
  di manifest `tools/out/*.json`: book, page, xref, w, h, checksum.
- **`doc/aset-gambar.md`** — cara pakai pipeline, arti manifest, aturan
  `image_source` + caption, dan batasan yang ditemui.
- **Blok `chart`** (`VisualBlocks.tsx`) — grafik batang, garis, dan lingkaran
  sebagai SVG sendiri (tanpa pustaka grafik), label sumbu dirapikan dan
  diunikkan, ringkasan data dipakai sebagai teks alternatif.
- **Blok `diagram`** — renderer `resources/js/lib/material/diagram.ts` untuk
  subset Mermaid (`graph TD|LR`, `A[kotak]`, `A(bulat)`, `A{keputusan}`,
  `A -->|label| B`), termasuk tata letak per rank dan panah. Kode tak dikenal
  ditampilkan apa adanya, bukan kotak kosong.
- **Blok `hotspots`** — gambar buku ajar dengan titik ternormalisasi (0..1),
  panel bacaan per titik, hitungan “terbuka n dari m”, dan daftar teks untuk
  pembaca layar.
- **Blok `timeline`** — lini masa vertikal dengan titik, tahun, judul, dan
  keterangan.
- **Blok `label`** (dinilai) — pilih label lalu ketuk titik pada gambar;
  skor = proporsi titik benar, bisa diulang, jawaban benar ditampilkan.
- **Aset**: `public/media/matematika/ma-6-1/grafik-b-hal196.png`
  (Matematika-BG-KLS-X.pdf hlm. 196) beserta manifest
  `tools/out/ma-6-1-grafik-b.json`.
- **Service worker**: `/media/` masuk daftar aset statis sehingga gambar buku
  tetap tampil offline; `CACHE_VERSION` naik ke `0.21.0`.

### Diubah
- **INF/MA/FIS memakai visual**: MA 6.1 “Bentuk dan Arah Parabola” (grafik
  garis, tabel, gambar parabola berlabel), FIS 1 “Besaran, Satuan, dan Alat
  Ukur” (diagram, lini masa), FIS 1 “Ketidakpastian Pengukuran” (grafik
  batang selisih pengukuran). Teks markdown lama tetap tersimpan sebagai
  fallback.
- **`BlockRenderer`** — blok `scenario` dan `challenge` saja yang masih
  ditandai “belum tersedia”.
- **`MaterialBlockType`** dokumentasi `diagram.engine`: `mermaid` = subset
  yang dirender sendiri, `svg` = SVG manual yang disanitasi.

### Catatan teknis
- Mermaid **tidak** dipakai di halaman materi: pada lingkungan aplikasi ini
  Mermaid 11 dan 12 salah mengukur lebar label (~10× terlalu besar) sehingga
  diagram menyebar dengan kotak kecil — bug yang juga terlihat pada diagram
  halaman Panduan. Renderer sendiri menghilangkan chunk ~660 kB dari halaman
  materi dan membuat diagram tetap tampil offline. Pustaka Mermaid tetap
  terpasang untuk halaman Panduan.
- Posisi titik `hotspots` ditentukan dari hasil render halaman lalu diperiksa
  ulang lewat tangkapan layar peramban.

### Verifikasi
- `./node_modules/.bin/tsc --noEmit` lulus; `npm run build` lulus.
- `php artisan test` lulus: **113 tes / 958 asersi** (tes baru memastikan blok
  visual MA/FIS terimpor, `image_source` book+page terisi, berkas gambar ada di
  `public/`, dan koordinat titik dalam 0..1).
- `gamecenter:materi-import`: 48 bab + 146 materi diperbarui, tanpa galat
  validasi untuk blok visual baru.
- Uji peramban (akun siswa): grafik garis MA 6.1 tampil, tiga titik gambar
  parabola tepat di puncak, potong sumbu-y, dan potong sumbu-x; diagram FIS 1
  padat dan terbaca; lini masa rapi; grafik batang “Selisih …” dengan sumbu
  0–0,2 tanpa label dobel.

## [0.20.0] - 2026-11-17 15:40 WIB

**Blok interaktif dasar dan penyimpanan skor formatif (Fase 2 `plan-materi-interaktif.md`).**

### Ditambah
- **Blok hafalan** `glossary` (istilah yang bisa dibuka) dan `flashcards`
  (kartu bolak-balik + “Sudah ingat” / “Ulangi semua”) di
  `.../Material/Blocks/RecallBlocks.tsx`. Tidak dinilai.
- **Blok `checkpoint`** — kuis satu pilihan dengan penjelasan mengapa jawaban
  benar/salah, bisa diulang, umpan balik diumumkan `aria-live`.
- **Blok `sort`** — urutan bisa diubah dengan drag **atau** tombol ↑ ↓
  (wajib untuk keyboard, plan §7.2), butir yang salah ditandai merah dan boleh
  diulang.
- **Blok `categorize`** — tiap butir diberi tombol keranjang (`aria-pressed`),
  skor dihitung dari jumlah penempatan benar.
- **`resources/js/lib/material/store.ts`** — penyimpanan jawaban blok di
  `localStorage` per materi: skor terbaik, jumlah percobaan, dan jawaban
  terakhir; tetap bekerja untuk tamu dan saat offline.
- **`useBlockAnswer`** — hook yang menyatukan penyimpanan lokal dengan
  pelaporan ke antrean sync.
- **Tabel `material_block_responses`** + model `MaterialBlockResponse`
  (unik per `user_id` + `material_id` + `block_id`, indeks per tipe blok).
- **`App\Services\Materi\BlockSchema`** — validasi seluruh 18 tipe blok:
  id unik, blok aktivitas wajib `id` + `feedback`, `checkpoint` wajib tepat
  satu jawaban benar + penjelasan, `sort.answer` harus cocok dengan `items`,
  `categorize`/`label` merujuk keranjang/pilihan yang ada, blok gambar wajib
  `image_source` (book + page), `scenario` wajib `start` dan `next` valid.
- **Item sync `material_block`** — divalidasi di `SyncService` (blok harus ada
  di materi, bertipe aktivitas, tipenya cocok) lalu disimpan idempoten dengan
  skor terbaik dan `attempts` tertinggi.
- **Isi contoh**: materi “Empat Pilar Berpikir Komputasional” (INF 1) kini
  memuat glosarium, satu `sort` urutan berpikir komputasional, dan dua
  `checkpoint`.

### Diubah
- **`MaterialViewer` / `IntroPanel`** meneruskan `onBlockRecord` sehingga skor
  blok diantrekan lewat `syncService` saat siswa masuk; tamu tetap mendapat
  progres lokal.
- **`SyncItemType`** menambah `material_block`, dan `StoreSyncBatchRequest`
  menerima tipe item tersebut.

### Verifikasi
- `./node_modules/.bin/tsc --noEmit` lulus; `npm run build` lulus.
- `php artisan test` lulus: **112 tes / 921 asersi** (sebelumnya 98/885),
  termasuk 11 tes `BlockSchema` dan 3 tes sync blok (tersimpan, idempoten,
  menolak blok asing/tipe salah).
- `php artisan migrate` + `gamecenter:materi-import` dijalankan; berkas INF 1
  lolos validasi blok baru.
- Uji peramban dengan akun siswa: glosarium terbuka, `sort` bisa disusun
  dengan tombol sampai skor 100, `checkpoint` benar/salah memberi umpan balik,
  dan baris `material_block_responses` tersimpan di server
  (`srt-urutan` 100/4×, `cp-pilar-1` 100/1×, `cp-pilar-2` 100/2×).
  Setelah muat ulang, skor “Terbaik” tetap tampil dari penyimpanan lokal.

### Catatan
- Skor blok **tidak** masuk `game_sessions` maupun nilai rapor; rekap untuk
  guru dan kartu di `/progres` menyusul di Fase 5 (plan §5.5).

## [0.19.0] - 2026-11-17 15:05 WIB

**Fondasi materi interaktif (Fase 1 `plan-materi-interaktif.md`).**

### Ditambah
- **Model data blok materi** `resources/js/lib/material/blocks.ts`: union
  `MaterialBlock` untuk 18 tipe blok (teks, visual, hafalan, aktivitas) plus
  `normalizeBlocks()` / `legacyValueBlocks()` yang menyaring data agar satu blok
  rusak tidak menjatuhkan seluruh materi.
- **`BlockRenderer`** (`resources/js/Components/Material/BlockRenderer.tsx`)
  yang merangkai blok sesuai urutan. Tipe yang renderer-nya baru datang pada
  Fase 2–4 ditampilkan sebagai catatan kecil, bukan halaman kosong.
- **Blok teks** `heading`, `paragraph`, `list` (termasuk daftar bernomor),
  `table`, `callout`, dan `code` di `.../Material/Blocks/TextBlocks.tsx`.
- **Gaya `.material-prose h4` dan `ol`** agar daftar bernomor dan subjudul
  level 4 punya tampilan setara heading lama.
- **Contoh isi**: materi pertama bab `INF 1 — Berpikir Komputasional` kini
  memakai `blocks` (heading, paragraf, tabel empat pilar, daftar bernomor,
  callout) sebagai bukti jalur render baru. Teks aslinya tetap disimpan.

### Diubah
- **`MaterialViewer`** memilih sumber render (plan §3.3): materi ber-`blocks`
  dirender lewat `BlockRenderer`; materi lama tetap memakai markdown, dan blok
  gaya lama `{ type, value }` (materi PAUD/TK) tetap tampil sebagai daftar.
- **`Inline`** dipindah ke `TextBlocks.tsx` agar jalur markdown dan blok baru
  memakai penanda tebal/kode yang sama.
- **`MaterialType`** menambah `visual` dan `scenario` beserta label dan ikonnya.

### Verifikasi
- `./node_modules/.bin/tsc --noEmit` lulus; `npm run build` lulus.
- `php artisan test` lulus (98 tes, 885 asersi), termasuk dua tes baru:
  blok INF 1 terimpor utuh dengan materi lain tetap markdown, dan tipe materi
  `visual`/`scenario` dikenali.
- Pratinjau peramban: materi INF 1 tampil dengan daftar bernomor dan kotak info;
  materi PAUD "Cari Pasangan Bentuk" tetap menampilkan blok `{type, value}`.

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
