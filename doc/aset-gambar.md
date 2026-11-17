# Aset Gambar Materi (pipeline `tools/pdf-extract-images.py`)

Blok visual `hotspots` dan `label` memakai gambar yang diambil dari buku ajar
PDF yang sudah tersedia di `data/kurmer/`. Setiap gambar wajib bisa
dilacak kembali ke halaman asalnya supaya kualitas dan hak pakainya jelas
(plan-materi-interaktif §6.0).

## Alur singkat

```bash
# 1. gambar raster yang tertanam di PDF (foto, tangkapan layar)
python tools/pdf-extract-images.py \
  "data/kurmer/SMKSMA/BUKU AJAR/KELAS X/Matematika-BG-KLS-X.pdf" \
  --out gamecenter/public/media/matematika/ma-6-1 \
  --manifest tools/out/ma-6-1.json \
  --pages 196 --min-size 200

# 2. figur vektor (grafik, diagram garis): render halaman lalu potong
python tools/pdf-extract-images.py \
  "data/kurmer/SMKSMA/BUKU AJAR/KELAS X/Matematika-BG-KLS-X.pdf" \
  --out gamecenter/public/media/matematika/ma-6-1 \
  --manifest tools/out/ma-6-1-grafik.json \
  --pages 196 --render-pages 196 --render-name grafik-b \
  --render-clip 0.15,0.47,0.50,0.82 --render-dpi 220
```

Keluaran:

```
gamecenter/public/media/<mapel>/<bab>/<nama>.png
tools/out/<nama>.json      ← manifest (jangan dihapus)
```

## Isi manifest

| Kunci | Arti |
|---|---|
| `book` | nama berkas PDF asal |
| `page` | halaman 1-based di PDF (bukan nomor halaman cetak) |
| `xref` | nomor objek gambar di PDF (`null` untuk hasil render) |
| `w`, `h` | ukuran piksel |
| `file` | nama berkas di `public/media/...` |
| `checksum` | 16 karakter pertama SHA-256, untuk mendeteksi duplikat |
| `kind`, `clip`, `dpi` | hanya untuk hasil render halaman |
| `skipped` | jumlah gambar yang dibuang karena terlalu kecil/duplikat |

## Aturan pemakaian di materi

1. `image_url` memakai path absolut dari `public`, misal
   `/media/matematika/ma-6-1/grafik-b-hal196.png`.
2. Selalu isi `image_source`:

   ```json
   "image_source": { "book": "Matematika-BG-KLS-X.pdf", "page": 196, "figure": "Grafik y = -x² + 4x + 4" }
   ```

   `BlockSchema` menolak blok `hotspots`/`label` tanpa `book` + `page`.
3. Selalu isi `caption` pada `hotspots` — dipakai sebagai teks alternatif
   gambar (plan §4.1 & §7.2).
4. Koordinat titik memakai fraksi `0..1` terhadap ukuran gambar, bukan piksel,
   supaya tetap akurat di layar kecil. Perkirakan dari hasil render, lalu
   periksa ulang dengan tangkapan layar.
5. Jangan memakai halaman yang memuat teks jawaban kunci atau data pribadi;
   pilih halaman dengan figur mandiri.
6. Gambar hasil ekstraksi otomatis masuk cache service worker
   (`isStaticAsset` mencakup `/media/`), jadi tetap tersedia offline.

## Berkas yang sudah dipakai

| Berkas | Sumber | Dipakai di |
|---|---|---|
| `media/matematika/ma-6-1/grafik-b-hal196.png` | Matematika-BG-KLS-X.pdf hlm. 196 | MA 6.1 “Bentuk dan Arah Parabola” (blok `hotspots`) |

Manifest terkait: `tools/out/ma-6-1-grafik-b.json`.

## Catatan renderer diagram

Blok `diagram` memakai `engine: "mermaid"` dengan **subset** sintaks:

```
graph TD            (atau LR)
  A[Kotak] --> B(Kotak bulat)
  B -->|label| C{Keputusan}
```

Subset ini dirender oleh `resources/js/lib/material/diagram.ts` (parser + tata
letak SVG sendiri). Alasan: Mermaid 11/12 di lingkungan aplikasi ini salah
mengukur lebar label (~10× terlalu besar) sehingga diagram menyebar dengan
kotak kecil — bug yang juga terlihat pada diagram halaman Panduan. Keuntungan
lain: halaman materi tidak lagi mengunduh chunk Mermaid ~660 kB dan diagram
tetap tampil saat offline. Kode di luar subset (subgraph, classDef, klik)
diabaikan; bila tidak ada node yang dikenali, kode aslinya ditampilkan.

Untuk figur khusus, `engine: "svg"` menerima SVG manual; sebelum disisipkan,
skrip/`foreignObject`/atribut `on*` dibuang.

## Batasan yang ditemui

- Sebagian besar figur pada buku kelas X adalah **gambar vektor**, sehingga
  tidak muncul lewat ekstraksi raster; pakai mode `--render-pages`.
- Buku `IPA_BG_KLS_X_Rev.pdf` tidak memuat ilustrasi alat ukur (jangka sorong,
  mikrometer), jadi materi FIS 1 memakai `diagram`, `chart`, dan `timeline`
  lebih dulu. Blok gambar untuk Fisika menyusul saat ada sumber figur yang
  sesuai.
- Ekstraksi tanpa `--pages` akan menyapu seluruh PDF; selalu batasi halaman.
