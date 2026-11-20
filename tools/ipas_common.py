"""Pembangun berkas materi Projek IPAS Kelas X (Fase E).

Memakai ulang pembangun blok dan asesmen dari `pjok_common`, hanya mapel dan
folder tujuan yang berbeda. Jalankan dari folder `gamecenter`:

    python ../tools/tulis-ipas-1.py
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
    # Projek IPAS adalah mapel jenjang SMK/MAK, jadi level-nya `smk`.
    _write_chapter(chapter, subject='ipas', folder='ipas', level='smk')
