"""Pembantu penulisan bab Pendidikan Kepercayaan (Fase E, jenjang SMA/SMK).

Membungkus `pjok_common` agar seluruh blok dan skema payload konsisten dengan
mapel lain, lalu menyetel `subject='kepercayaan'` dan `folder='kepercayaan'`.
"""
from pjok_common import *  # noqa: F401,F403
from pjok_common import write_chapter as _write_chapter


def write_chapter(chapter):
    # Mapel ini tersedia di jenjang SMA maupun SMK; konten dipasang di SMA.
    _write_chapter(chapter, subject='kepercayaan', folder='kepercayaan', level='sma')
