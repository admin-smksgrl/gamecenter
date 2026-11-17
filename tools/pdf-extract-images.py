#!/usr/bin/env python3
"""Ekstrak ilustrasi dari PDF buku ajar untuk blok visual materi.

Dipakai oleh pipeline aset `plan-materi-interaktif.md` §6.0. Hanya aset yang
masuk manifest boleh dipakai di blok `hotspots` / `label` / `puzzle`, dan
setiap blok wajib mencantumkan `image_source` (book + page) agar dapat
diaudit serta ditarik kembali bila diperlukan.

Contoh:

    python tools/pdf-extract-images.py \
        "data/kurmer/SMKSMA/BUKU AJAR/KELAS X/Matematika-BG-KLS-X.pdf" \
        --out gamecenter/public/media/matematika/ma-6.1 \
        --pages 120-140 --min-size 200 \
        --manifest tools/out/ma-6.1.json

Aturan penyaring:
- dimensi minimum `--min-size` x `--min-size` piksel (default 200);
- berkas gambar minimum `--min-bytes` (default 2048) supaya ikon garis tidak ikut;
- CMYK / grayscale dikonversi ke RGB agar tampil konsisten di peramban;
- gambar duplikat (xref atau checksum sama) hanya ditulis sekali.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover - jalur bantuan
    try:
        import fitz as pymupdf  # type: ignore[no-redef]
    except ImportError:
        sys.exit(
            "PyMuPDF belum terpasang. Jalankan: pip install pymupdf\n"
            "(di mesin pengembang: Python 3.14 + pymupdf 2.1)"
        )


def parse_pages(value: str | None, total: int) -> list[int]:
    """`"30-45"`, `"3,8,12"`, atau `"30-45,80"` -> daftar halaman 1-based."""
    if not value:
        return list(range(1, total + 1))

    pages: list[int] = []

    for chunk in value.split(","):
        chunk = chunk.strip()

        if not chunk:
            continue

        if "-" in chunk:
            start, end = chunk.split("-", 1)
            pages.extend(range(int(start), int(end) + 1))
        else:
            pages.append(int(chunk))

    return sorted({page for page in pages if 1 <= page <= total})


def slug_book(name: str) -> str:
    return Path(name).stem


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", help="berkas PDF buku ajar")
    parser.add_argument("--out", required=True, help="folder tujuan gambar")
    parser.add_argument("--manifest", required=True, help="berkas manifest JSON")
    parser.add_argument("--pages", default=None, help="halaman, mis. 30-45 atau 3,8,12")
    parser.add_argument("--min-size", type=int, default=200, help="sisi minimum (px)")
    parser.add_argument("--min-bytes", type=int, default=2048, help="berkas minimum (byte)")
    parser.add_argument("--prefix", default=None, help="awalan nama berkas (default: nomor halaman)")
    parser.add_argument(
        "--render-pages",
        default=None,
        help="render halaman utuh (untuk figur vektor), mis. 176 atau 176,179",
    )
    parser.add_argument("--render-dpi", type=int, default=150, help="DPI render halaman")
    parser.add_argument(
        "--render-name",
        default=None,
        help="nama berkas hasil render (default: render-halNNN)",
    )
    parser.add_argument(
        "--render-clip",
        default="0,0,1,1",
        help="potong area halaman sebagai pecahan x0,y0,x1,y1 (0..1)",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf)

    if not pdf_path.exists():
        sys.exit(f"PDF tidak ditemukan: {pdf_path}")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = Path(args.manifest)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    book = slug_book(pdf_path.name)
    total_pages = doc.page_count

    assets: list[dict] = []
    seen_xref: set[int] = set()
    seen_checksum: set[str] = set()
    skipped = {"small": 0, "tiny": 0, "duplicate": 0, "empty": 0}

    try:
        for page_number in parse_pages(args.pages, doc.page_count):
            page = doc.load_page(page_number - 1)

            for image in page.get_images(full=True):
                xref = int(image[0])

                if xref in seen_xref:
                    skipped["duplicate"] += 1
                    continue

                seen_xref.add(xref)

                try:
                    pix = pymupdf.Pixmap(doc, xref)
                except Exception:
                    skipped["empty"] += 1
                    continue

                if pix.width < args.min_size or pix.height < args.min_size:
                    skipped["small"] += 1
                    continue

                # CMYK atau ada alpha ekstra -> render ulang sebagai RGB.
                if pix.colorspace is None or pix.n - pix.alpha >= 4:
                    pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

                data = pix.tobytes("png")

                if len(data) < args.min_bytes:
                    skipped["tiny"] += 1
                    continue

                checksum = hashlib.sha256(data).hexdigest()

                if checksum in seen_checksum:
                    skipped["duplicate"] += 1
                    continue

                seen_checksum.add(checksum)

                prefix = args.prefix or "hal"
                name = f"{prefix}{page_number:03d}-x{xref}.png"

                (out_dir / name).write_bytes(data)

                assets.append(
                    {
                        "book": pdf_path.name,
                        "page": page_number,
                        "xref": xref,
                        "w": pix.width,
                        "h": pix.height,
                        "bytes": len(data),
                        "file": name,
                        "checksum": checksum[:16],
                        "url": "/" + out_dir.as_posix().split("public/", 1)[-1] + "/" + name
                        if "public/" in out_dir.as_posix()
                        else f"/{out_dir.as_posix()}/{name}",
                    }
                )

                pix = None
    finally:
        doc.close()

    manifest = {
        "source": str(pdf_path.as_posix()),
        "book": pdf_path.name,
        "generated_with": "tools/pdf-extract-images.py",
        "pymupdf": getattr(pymupdf, "__version__", "unknown"),
        "min_size": args.min_size,
        "min_bytes": args.min_bytes,
        "pages": args.pages,
        "count": len(assets),
        "skipped": skipped,
        "assets": assets,
    }

    # Figur vektor (grafik, diagram) tidak tersimpan sebagai gambar di PDF,
    # jadi halaman dirender ulang lalu dipotong pada area figur.
    if args.render_pages:
        clip = [float(part) for part in args.render_clip.split(",")]

        if len(clip) != 4:
            sys.exit("--render-clip harus empat angka: x0,y0,x1,y1")

        doc = pymupdf.open(pdf_path)
        rendered: list[dict] = []

        try:
            for page_number in parse_pages(args.render_pages, doc.page_count):
                page = doc.load_page(page_number - 1)
                box = page.rect
                rect = pymupdf.Rect(
                    box.x0 + clip[0] * box.width,
                    box.y0 + clip[1] * box.height,
                    box.x0 + clip[2] * box.width,
                    box.y0 + clip[3] * box.height,
                )
                pix = page.get_pixmap(clip=rect, dpi=args.render_dpi)
                data = pix.tobytes("png")
                checksum = hashlib.sha256(data).hexdigest()
                name = args.render_name or f"render-hal{page_number:03d}.png"
                name = f"{Path(name).stem}-hal{page_number:03d}.png" if args.render_name else name

                (out_dir / name).write_bytes(data)

                entry = {
                    "book": pdf_path.name,
                    "page": page_number,
                    "xref": None,
                    "w": pix.width,
                    "h": pix.height,
                    "bytes": len(data),
                    "file": name,
                    "checksum": checksum[:16],
                    "kind": "render",
                    "clip": clip,
                    "dpi": args.render_dpi,
                    "url": "/" + out_dir.as_posix().split("public/", 1)[-1] + "/" + name
                    if "public/" in out_dir.as_posix()
                    else f"/{out_dir.as_posix()}/{name}",
                }

                rendered.append(entry)
                assets.append(entry)
                manifest["count"] = len(assets)
        finally:
            doc.close()

        manifest["rendered"] = rendered

    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"buku      : {pdf_path.name}")
    print(f"halaman   : {total_pages}")
    print(f"gambar    : {len(assets)} disimpan -> {out_dir}")
    print(f"dilewati  : {skipped}")
    print(f"manifest  : {manifest_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
