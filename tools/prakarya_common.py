"""Pembangun berkas materi Prakarya Kelas X (Fase E).

Memakai ulang pembangun blok dan asesmen dari `pjok_common`, hanya mapel dan
folder tujuan yang berbeda. Jalankan dari folder `gamecenter`:

    python ../tools/tulis-pra-1.py
"""
from pjok_common import (  # noqa: F401
    categorize_block,
    challenge_block,
    chart_block,
    scenario,
    sort_block,
    timeline_block,
    write_chapter as _write_chapter,
)


def write_chapter(chapter):
    _write_chapter(chapter, subject='prakarya', folder='prakarya')
