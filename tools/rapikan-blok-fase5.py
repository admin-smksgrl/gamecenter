"""Fase 5.1 batch 1R — pulihkan teks materi yang hilang dari layar.

Masalah: `MaterialViewer` merender `blocks` **atau** markdown, bukan keduanya.
Batch 2-6 hanya menambahkan blok interaktif, sehingga teks asli materi tidak
pernah tampil. Skrip ini mengubah markdown `content` menjadi blok teks
(`heading`, `paragraph`, `list`, `table`, `callout`, `code`) lalu menyisipkan
blok interaktif yang sudah ada pada bagian yang paling relevan.

Jalankan dari folder gamecenter:

    python ../tools/rapikan-blok-fase5.py            # laporan saja
    python ../tools/rapikan-blok-fase5.py --apply    # tulis perubahan
"""
import io
import json
import os
import re
import sys

BASE = 'database/seeders/data/sma-smk/fase-e/'

TEXT_TYPES = {'heading', 'paragraph', 'list', 'table', 'callout', 'code'}
PRE_TRAINING = {'glossary', 'flashcards'}
CLOSING = {'scenario', 'challenge'}

HEADING_RE = re.compile(r'^(#{2,6})\s+(.*)$')
LIST_RE = re.compile(r'^(-{1}\s|\*\s|\+\s|\d+\.\s)')
TABLE_SEP_RE = re.compile(r'^\|[\s:\-|]+\|$')
ITALIC_RE = re.compile(r'(?<!\*)\*(?!\*)([^*\n]+)\*(?!\*)')


def clean(text):
    """Rapikan markup inline yang tidak didukung renderer (miring)."""
    text = ITALIC_RE.sub(r'\1', text)
    text = text.replace('\\*', '*')
    return re.sub(r'\s+', ' ', text).strip()


def parse_markdown(md):
    """Ubah markdown materi menjadi daftar blok teks."""
    lines = (md or '').replace('\r\n', '\n').split('\n')
    blocks = []
    i = 0

    while i < len(lines):
        raw = lines[i]
        s = raw.strip()

        if not s:
            i += 1
            continue

        # Pagar kode
        if s.startswith('```'):
            language = s[3:].strip() or None
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1  # lewati pagar penutup
            block = {'type': 'code', 'text': '\n'.join(code).strip('\n')}
            if language:
                block['language'] = language
            blocks.append(block)
            continue

        # Judul
        m = HEADING_RE.match(s)
        if m:
            level = min(max(len(m.group(1)), 2), 4)
            blocks.append({'type': 'heading', 'level': level, 'text': clean(m.group(2))})
            i += 1
            continue

        # Tabel
        if s.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = lines[i].strip()
                if not TABLE_SEP_RE.match(row):
                    cells = [clean(cell.strip()) for cell in row.strip('|').split('|')]
                    if cells:
                        rows.append(cells)
                i += 1
            if len(rows) >= 2:
                blocks.append({'type': 'table', 'rows': rows})
            elif rows:
                blocks.append({'type': 'paragraph', 'text': ' '.join(rows[0])})
            continue

        # Kutipan -> callout
        if s.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip().lstrip('>').strip())
                i += 1
            text = clean(' '.join(part for part in buf if part))
            if text:
                blocks.append({'type': 'callout', 'tone': 'info', 'text': text})
            continue

        # Daftar
        if LIST_RE.match(s):
            ordered = bool(re.match(r'^\d+\.\s', s))
            items = []
            while i < len(lines):
                t = lines[i].strip()
                m_item = re.match(r'^(-|\*|\+|\d+\.)\s+(.*)$', t)
                if m_item:
                    items.append(clean(m_item.group(2)))
                    i += 1
                    continue
                if not t and i + 1 < len(lines) and LIST_RE.match(lines[i + 1].strip()):
                    i += 1
                    continue
                break
            items = [item for item in items if item]
            if items:
                blocks.append({'type': 'list', 'ordered': ordered, 'items': items})
            continue

        # Paragraf
        buf = []
        while i < len(lines):
            t = lines[i].strip()
            if not t:
                break
            if (
                HEADING_RE.match(t)
                or t.startswith('|')
                or t.startswith('>')
                or t.startswith('```')
                or LIST_RE.match(t)
            ):
                break
            buf.append(t)
            i += 1
        text = clean(' '.join(buf))
        if text:
            blocks.append({'type': 'paragraph', 'text': text})
        elif not buf:
            i += 1

    return blocks


def words(text):
    return re.findall(r'[\w\u00C0-\uFFFF]+', text or '')


def text_words(blocks):
    count = 0
    for block in blocks:
        kind = block.get('type')
        if kind in ('heading', 'paragraph', 'callout', 'code'):
            count += len(words(block.get('text')))
        elif kind == 'list':
            for item in block.get('items') or []:
                count += len(words(str(item)))
        elif kind == 'table':
            for row in block.get('rows') or []:
                for cell in row:
                    count += len(words(str(cell)))
    return count


def split_segments(blocks):
    """Pecah blok teks menjadi segmen, satu segmen per judul."""
    segments = []
    for block in blocks:
        if block.get('type') == 'heading' and segments:
            segments.append([])
        if not segments:
            segments.append([])
        segments[-1].append(block)
    return [segment for segment in segments if segment]


def block_tokens(block):
    """Kata kunci blok untuk mencocokkan dengan segmen teks."""
    parts = []

    def walk(value):
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            for item in value.values():
                walk(item)

    for key in ('title', 'prompt', 'question', 'caption', 'explanation', 'code'):
        if key in block:
            walk(block[key])

    return {w.lower() for w in words(' '.join(parts)) if len(w) >= 4}


def segment_tokens(segment):
    return {w.lower() for w in words(json.dumps(segment, ensure_ascii=False)) if len(w) >= 4}


def place_blocks(text_blocks, interactive):
    """Sisipkan blok interaktif ke segmen yang paling relevan."""
    segments = split_segments(text_blocks)
    if not segments:
        return list(interactive)

    assignments = [[] for _ in segments]
    closing = []
    pre = []

    for block in interactive:
        kind = block.get('type')
        if kind in PRE_TRAINING:
            pre.append(block)
            continue
        if kind in CLOSING:
            closing.append(block)
            continue

        tokens = block_tokens(block)
        best_index = 0
        best_score = -1
        for index, segment in enumerate(segments):
            score = len(tokens & segment_tokens(segment))
            if score > best_score:
                best_score, best_index = score, index
        assignments[best_index].append(block)

    result = list(pre)
    for index, segment in enumerate(segments):
        result.extend(segment)
        result.extend(assignments[index])
    result.extend(closing)
    return result


def process(material):
    content = material.get('content') or ''
    blocks = material.get('blocks') or []

    text_blocks = [b for b in blocks if b.get('type') in TEXT_TYPES]
    interactive = [b for b in blocks if b.get('type') not in TEXT_TYPES]

    before = text_words(text_blocks)
    total = len(words(re.sub(r'[|#>*-]', ' ', content)))

    parsed = parse_markdown(content)
    after = text_words(parsed)

    # Sudah cukup lengkap: jangan sentuh supaya tidak mengubah karya manual.
    if total > 0 and before >= total * 0.9:
        return None, before, total, after

    if not parsed:
        return None, before, total, after

    material['blocks'] = place_blocks(parsed, interactive)
    return material, before, total, after


def main():
    apply = '--apply' in sys.argv
    only = None
    for arg in sys.argv[1:]:
        if arg.startswith('--only='):
            only = arg.split('=', 1)[1]

    changed = 0
    skipped = 0
    skipped_list = []
    low = []

    for root, _dirs, files in os.walk(BASE):
        for name in sorted(files):
            if not name.endswith('.json'):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, BASE).replace('\\', '/')
            if only and only not in rel:
                continue

            data = json.load(io.open(path, encoding='utf-8'))
            touched = False

            for chapter in data.get('chapters', []):
                for index, material in enumerate(chapter.get('materials', [])):
                    if not material.get('blocks'):
                        continue
                    updated, before, total, after = process(material)
                    if updated is None:
                        skipped += 1
                        skipped_list.append((rel, index, before, total))
                        continue
                    touched = True
                    changed += 1
                    if total and after < total * 0.8:
                        low.append((rel, index, before, total, after))

            if touched and apply:
                io.open(path, 'w', encoding='utf-8').write(
                    json.dumps(data, indent=2, ensure_ascii=False) + '\n'
                )

    verb = 'ditulis' if apply else 'akan diubah (dry-run)'
    print(f'{changed} materi {verb}, {skipped} dilewati (teks sudah lengkap).')
    for rel, index, before, total in skipped_list:
        print(f'  dilewati: {rel}[{index}] teks {before} / konten {total} kata')
    if low:
        print('\nPerlu tinjauan manual (kata blok < 80% kata konten):')
        for rel, index, before, total, after in low:
            print(f'  {rel}[{index}] teks {before} -> {after} / konten {total}')
    if not apply:
        print('\nTambahkan --apply untuk menulis perubahan.')


if __name__ == '__main__':
    main()
