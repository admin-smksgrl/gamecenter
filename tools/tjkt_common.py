"""Pembantu penulisan bab Dasar-Dasar TJKT (Fase E, jenjang SMK).

Membungkus `pjok_common` agar seluruh blok dan skema payload konsisten dengan
mapel lain, lalu menyetel `subject='tjkt'` dan `folder='tjkt'`.
"""
from pjok_common import *  # noqa: F401,F403
from pjok_common import write_chapter as _write_chapter


def write_chapter(chapter):
    _write_chapter(chapter, subject='tjkt', folder='tjkt', level='smk')
