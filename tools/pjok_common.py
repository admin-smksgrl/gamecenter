"""Pembangun berkas materi PJOK Kelas X (Fase E).

Dipakai oleh `tulis-pjok-1.py` ... `tulis-pjok-8.py`. Semua `content` markdown
diturunkan dari blok teks yang sama lewat `materi_fase_e.markdown`, sehingga
`MateriContentFidelityTest` tidak menemukan teks yang hilang.

Jalankan dari folder `gamecenter`:

    python ../tools/tulis-pjok-1.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from materi_fase_e import materi, simpan  # noqa: E402


def _with_hint(question, hint):
    if hint:
        question['hint'] = hint

    return question


def mc(fact):
    """fact = (pertanyaan, jawaban benar, [pengecoh], penjelasan, hint)."""
    question, correct, wrong, explanation, hint = fact

    payload = {
        'type': 'multiple_choice',
        'question': question,
        'options': [{'text': correct, 'correct': True}]
        + [{'text': text} for text in wrong],
        'explanation': explanation,
    }

    return _with_hint(payload, hint)


def ma(item):
    """item = (pertanyaan, [jawaban benar], [pengecoh], penjelasan, hint)."""
    question, corrects, wrongs, explanation, hint = item

    payload = {
        'type': 'multiple_answer',
        'question': question,
        'options': [{'text': text, 'correct': True} for text in corrects]
        + [{'text': text, 'correct': False} for text in wrongs],
        'explanation': explanation,
    }

    return _with_hint(payload, hint)


def matching(question, pairs, explanation, hint=None):
    """Pasangan memakai bentuk `left`/`right` yang dibaca MatchGame."""
    options = [
        {'id': f'm{index}', 'left': left, 'right': right}
        for index, (left, right) in enumerate(pairs)
    ]
    correct = {
        'pairs': {f'm{index}': right for index, (_, right) in enumerate(pairs)}
    }

    payload = {
        'type': 'matching',
        'question': question,
        'options': options,
        'correct': correct,
        'explanation': explanation,
    }

    return _with_hint(payload, hint)


def drag(question, steps, explanation, hint=None):
    options = [{'id': f'd{index}', 'text': text} for index, text in enumerate(steps)]
    correct = {'order': [option['id'] for option in options]}

    payload = {
        'type': 'drag_drop',
        'question': question,
        'options': options,
        'correct': correct,
        'explanation': explanation,
    }

    return _with_hint(payload, hint)


def puzzle(question, steps, explanation, hint=None):
    options = [{'id': f'p{index}', 'text': text} for index, text in enumerate(steps)]
    correct = {'order': [option['id'] for option in options]}

    payload = {
        'type': 'puzzle',
        'question': question,
        'options': options,
        'correct': correct,
        'explanation': explanation,
    }

    return _with_hint(payload, hint)


def checkpoint(block_id, data):
    """data = (pertanyaan, [(pilihan, benar?)], penjelasan)."""
    question, choices, explanation = data

    return {
        'type': 'checkpoint',
        'id': block_id,
        'question': question,
        'choices': [
            {'id': f'c{index}', 'text': text, 'correct': True}
            if correct
            else {'id': f'c{index}', 'text': text}
            for index, (text, correct) in enumerate(choices)
        ],
        'explanation': explanation,
    }


def _tanpa_hint(question):
    question.pop('hint', None)

    return question


def build_assessments(chapter):
    facts = chapter['facts']
    multi = chapter['multi']
    pairs = chapter['pairs']
    steps = chapter['steps']

    easy = [
        mc(facts[0]),
        mc(facts[1]),
        mc(facts[2]),
        ma(multi[0]),
        ma(multi[1]),
    ]

    medium = [
        mc(facts[3]),
        mc(facts[4]),
        ma(multi[2]),
        ma(multi[3]),
        matching(
            'Pasangkan istilah dasar pada bab ini dengan pengertian yang tepat.',
            pairs[0:4],
            'Istilah harus dipasangkan sesuai pengertiannya, bukan sekadar diingat urutannya.',
            'Baca ulang glosarium di awal materi.',
        ),
        drag(*steps[0]),
        puzzle(*steps[1]),
        mc(facts[5]),
        mc(facts[6]),
        ma(multi[4]),
    ]

    hard = [
        _tanpa_hint(mc(facts[7])),
        _tanpa_hint(mc(facts[8])),
        _tanpa_hint(mc(facts[9])),
        _tanpa_hint(mc(facts[10])),
        _tanpa_hint(mc(facts[11])),
        _tanpa_hint(ma(multi[5])),
        _tanpa_hint(ma(multi[6])),
        matching(
            'Pasangkan istilah lanjutan pada bab ini dengan pengertian yang benar.',
            pairs[4:8],
            'Istilah lanjutan menuntut pemahaman, bukan hafalan urutan.',
        ),
        _tanpa_hint(drag(*steps[2])),
        _tanpa_hint(puzzle(*steps[3])),
        _tanpa_hint(mc(facts[12])),
        _tanpa_hint(mc(facts[13])),
        _tanpa_hint(ma(multi[7])),
        matching(
            'Pasangkan seluruh istilah pada bab ini dengan pengertiannya.',
            pairs[0:6],
            'Pasangan yang lengkap menunjukkan pemahaman menyeluruh atas istilah bab.',
        ),
        _tanpa_hint(drag(*steps[4])),
    ]

    return [
        {
            'difficulty': 'easy',
            'title': f"{chapter['title']} — Mudah",
            'passing_score': 60,
            'questions': easy,
        },
        {
            'difficulty': 'medium',
            'title': f"{chapter['title']} — Sedang",
            'passing_score': 70,
            'questions': medium,
        },
        {
            'difficulty': 'hard',
            'title': f"{chapter['title']} — Sulit",
            'passing_score': 80,
            'questions': hard,
        },
    ]


def build_materials(chapter):
    slug = chapter['slug']
    intro = chapter['intro']
    concept = chapter['concept']
    practice = chapter['practice']

    intro_blocks = [
        {
            'type': 'glossary',
            'id': f'{slug}-glosarium',
            'terms': chapter['glossary'],
        },
        {'type': 'heading', 'level': 2, 'text': intro['title']},
    ]
    intro_blocks += [{'type': 'paragraph', 'text': text} for text in intro['paragraphs']]
    intro_blocks += [
        {
            'type': 'diagram',
            'id': f'{slug}-diagram',
            'engine': 'mermaid',
            'title': intro['diagram'][0],
            'code': intro['diagram'][1],
        },
        {'type': 'callout', 'tone': 'info', 'text': intro['callout']},
        checkpoint(f'{slug}-cp-1', intro['checkpoint']),
    ]

    concept_blocks = [
        {'type': 'heading', 'level': 2, 'text': concept['title']},
    ]
    concept_blocks += [{'type': 'paragraph', 'text': text} for text in concept['paragraphs']]
    concept_blocks += [
        {'type': 'table', 'rows': concept['table']},
        concept['visual'],
        concept['activity'],
        {'type': 'heading', 'level': 3, 'text': concept['subtitle']},
        {'type': 'list', 'items': concept['list']},
        checkpoint(f'{slug}-cp-2', concept['checkpoint']),
    ]

    practice_blocks = [
        {'type': 'heading', 'level': 2, 'text': practice['title']},
    ]
    practice_blocks += [{'type': 'paragraph', 'text': text} for text in practice['paragraphs']]
    practice_blocks += [
        practice['scenario'],
        {
            'type': 'flashcards',
            'id': f'{slug}-kartu',
            'cards': practice['flashcards'],
        },
        checkpoint(f'{slug}-cp-3', practice['checkpoint']),
        practice['challenge'],
    ]

    return [
        materi(
            intro['material_title'],
            intro_blocks,
            jenis='text',
            duration=intro.get('duration', 240),
            source=chapter['source'],
        ),
        materi(
            concept['material_title'],
            concept_blocks,
            jenis='text',
            duration=concept.get('duration', 300),
            source=chapter['source'],
        ),
        materi(
            practice['material_title'],
            practice_blocks,
            jenis='interactive',
            duration=practice.get('duration', 240),
            source=chapter['source'],
        ),
    ]


def write_chapter(chapter):
    payload = {
        'schema_version': 1,
        'level': 'sma',
        'class': 'kelas-10',
        'subject': 'pjok',
        'phase': 'E',
        'chapters': [
            {
                'code': chapter['code'],
                'title': chapter['title'],
                'description': chapter['description'],
                'learning_objectives': chapter['objectives'],
                'estimated_minutes': chapter['minutes'],
                'source_reference': chapter['source'],
                'materials': build_materials(chapter),
                'assessments': build_assessments(chapter),
            }
        ],
    }

    simpan(f"pjok/{chapter['slug']}.json", payload)


def scenario(block_id, title, start, nodes):
    return {
        'type': 'scenario',
        'id': block_id,
        'title': title,
        'start': start,
        'nodes': nodes,
    }


def sort_block(block_id, prompt, items, answer, correct, wrong):
    return {
        'type': 'sort',
        'id': block_id,
        'prompt': prompt,
        'items': [{'id': item_id, 'text': text} for item_id, text in items],
        'answer': answer,
        'feedback': {'correct': correct, 'wrong': wrong},
    }


def categorize_block(block_id, prompt, buckets, items, correct, wrong):
    return {
        'type': 'categorize',
        'id': block_id,
        'prompt': prompt,
        'buckets': [{'id': bucket_id, 'label': label} for bucket_id, label in buckets],
        'items': [
            {'id': item_id, 'text': text, 'bucket': bucket}
            for item_id, text, bucket in items
        ],
        'feedback': {'correct': correct, 'wrong': wrong},
    }


def challenge_block(block_id, title, time_limit, items, correct, wrong):
    return {
        'type': 'challenge',
        'id': block_id,
        'title': title,
        'time_limit': time_limit,
        'items': [{'question': question, 'answer': answer} for question, answer in items],
        'feedback': {'correct': correct, 'wrong': wrong},
    }


def chart_block(block_id, title, kind, data):
    return {
        'type': 'chart',
        'id': block_id,
        'title': title,
        'kind': kind,
        'data': [{'label': label, 'value': value} for label, value in data],
    }


def timeline_block(block_id, items):
    return {
        'type': 'timeline',
        'id': block_id,
        'items': [
            {'when': when, 'title': title, 'body': body}
            for when, title, body in items
        ],
    }
