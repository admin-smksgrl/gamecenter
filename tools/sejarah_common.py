"""Pembantu penulisan bab Sejarah (Fase E, jenjang SMA/SMK).

Membungkus `pjok_common` agar seluruh blok dan skema payload konsisten dengan
mapel lain, lalu menyetel `subject='sejarah'` dan `folder='sejarah'`.
"""
from pjok_common import *  # noqa: F401,F403
from pjok_common import write_chapter as _write_chapter


def write_chapter(chapter):
    _write_chapter(chapter, subject='sejarah', folder='sejarah', level='sma')
