import { useState } from 'react';

import type { FlashcardsBlock, GlossaryBlock } from '@/lib/material/blocks';

/**
 * Blok hafalan: glosarium (pre-training) dan kartu hafalan.
 * Keduanya **tidak dinilai** — tidak ada skor yang dikirim ke server.
 */

export function GlossaryBlockView({ block }: { block: GlossaryBlock }) {
    const terms = Array.isArray(block.terms) ? block.terms : [];

    if (terms.length === 0) {
        return null;
    }

    return (
        <section className="rounded-xl border border-rule bg-surface px-3 py-2.5">
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Glosarium · klik istilah
            </p>

            <dl className="mt-1 grid gap-1">
                {terms.map((term, index) => (
                    <div key={index}>
                        <dt>
                            <details className="group">
                                <summary className="flex cursor-pointer list-none items-center gap-1 text-[11px] font-bold text-ink marker:hidden">
                                    <span
                                        aria-hidden
                                        className="text-[8px] text-ink/30 transition-transform group-open:rotate-90"
                                    >
                                        ▶
                                    </span>
                                    {term.term}
                                </summary>
                                <dd className="mt-0.5 pl-3 text-[10.5px] leading-relaxed font-medium text-ink/55">
                                    {term.definition}
                                </dd>
                            </details>
                        </dt>
                    </div>
                ))}
            </dl>
        </section>
    );
}

export function FlashcardsBlockView({ block }: { block: FlashcardsBlock }) {
    const cards = Array.isArray(block.cards) ? block.cards : [];
    const [flipped, setFlipped] = useState<Record<number, boolean>>({});
    const [known, setKnown] = useState<Record<number, boolean>>({});

    if (cards.length === 0) {
        return null;
    }

    const remaining = cards
        .map((card, index) => ({ card, index }))
        .filter(({ index }) => !known[index]);

    return (
        <section className="rounded-xl border border-rule bg-surface px-3 py-2.5">
            <div className="flex items-center justify-between gap-2">
                <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                    Kartu hafalan
                </p>
                <p className="text-[9px] font-bold text-ink/35">
                    {remaining.length}/{cards.length} tersisa
                </p>
            </div>

            {remaining.length === 0 ? (
                <p className="mt-1.5 text-[10.5px] font-semibold text-ink/60">
                    Semua kartu sudah ditandai ingat.
                </p>
            ) : (
                <ul className="mt-1.5 grid gap-1.5">
                    {remaining.map(({ card, index }) => {
                        const isFlipped = flipped[index] === true;

                        return (
                            <li
                                key={index}
                                className="rounded-lg border border-rule bg-canvas/50 px-2.5 py-2"
                            >
                                <button
                                    type="button"
                                    onClick={() =>
                                        setFlipped((current) => ({
                                            ...current,
                                            [index]: !current[index],
                                        }))
                                    }
                                    aria-pressed={isFlipped}
                                    className="block w-full text-left"
                                >
                                    <span className="text-[8px] font-bold tracking-[0.1em] text-ink/30 uppercase">
                                        {isFlipped ? 'Jawaban' : 'Pertanyaan'}
                                    </span>
                                    <span className="mt-0.5 block text-[11px] leading-snug font-semibold text-ink">
                                        {isFlipped ? card.back : card.front}
                                    </span>
                                </button>

                                {isFlipped && (
                                    <button
                                        type="button"
                                        onClick={() =>
                                            setKnown((current) => ({
                                                ...current,
                                                [index]: true,
                                            }))
                                        }
                                        className="mt-1.5 inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white"
                                    >
                                        Sudah ingat
                                    </button>
                                )}
                            </li>
                        );
                    })}
                </ul>
            )}

            {remaining.length === 0 && (
                <button
                    type="button"
                    onClick={() => {
                        setKnown({});
                        setFlipped({});
                    }}
                    className="mt-2 text-[9.5px] font-bold text-ink/40 underline underline-offset-2"
                >
                    Ulangi semua kartu
                </button>
            )}
        </section>
    );
}
