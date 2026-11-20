"""Pembantu penulisan bab Dasar-Dasar Animasi (Fase E, jenjang SMK).

Membungkus `pjok_common` agar seluruh blok dan skema payload konsisten dengan
mapel lain, lalu menyetel `subject='animasi'` dan `folder='animasi'`.
"""
from pjok_common import *  # noqa: F401,F403
from pjok_common import write_chapter as _write_chapter


def write_chapter(chapter):
    _write_chapter(chapter, subject='animasi', folder='animasi', level='smk')
