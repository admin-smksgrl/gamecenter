"""Pembentuk berkas materi fase-e dari daftar blok.

Tujuan: `content` (markdown) selalu diturunkan dari blok teks yang sama, supaya
`MateriContentFidelityTest` tidak pernah menemukan materi yang kehilangan teks
saat `MaterialViewer` memilih jalur blok.

Jalankan dari folder `gamecenter`:

    python ../tools/materi_fase_e.py   # tidak langsung; dipakai skrip bab

Skrip bab memanggil `simpan()` di akhir.
"""
import io
import json
import os

BASE = 'database/seeders/data/sma-smk/fase-e/'

TEXT_TYPES = ('heading', 'paragraph', 'list', 'table', 'callout', 'code')


def markdown(blocks):
    """Ubah blok teks menjadi markdown; blok interaktif/visual dilewati."""
    lines = []

    for block in blocks:
        kind = block.get('type')

        if kind == 'heading':
            lines.append('#' * int(block.get('level', 2)) + ' ' + block['text'])
        elif kind in ('paragraph', 'callout', 'code'):
            lines.append(block['text'])
        elif kind == 'list':
            marker = '1.' if block.get('ordered') else '-'
            lines.extend(f'{marker} {item}' for item in block['items'])
        elif kind == 'table':
            rows = block['rows']
            lines.append('| ' + ' | '.join(rows[0]) + ' |')
            lines.append('|' + '|'.join(['---'] * len(rows[0])) + '|')
            lines.extend('| ' + ' | '.join(row) + ' |' for row in rows[1:])
        else:
            continue

        lines.append('')

    return '\n'.join(lines).strip()


def materi(title, blocks, *, jenis='text', duration=240, source=None):
    return {
        'type': jenis,
        'title': title,
        'duration': duration,
        'source_reference': source,
        'content': markdown(blocks),
        'blocks': blocks,
    }


def simpan(path, payload):
    full = BASE + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, 'w', encoding='utf-8').write(
        json.dumps(payload, indent=2, ensure_ascii=False) + '\n'
    )
    print(f'tulis {full}: {os.path.getsize(full)} byte')
