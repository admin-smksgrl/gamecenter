import { useState } from 'react';

import type { CategorizeBlock, SortBlock } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { useBlockAnswer } from '@/lib/material/useBlockAnswer';
import { cn } from '@/lib/utils';

interface ActivityProps<T> {
    block: T;
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}

/**
 * Blok drag & drop (plan §4.2).
 *
 * Prinsip aksesibilitas §7.2: drag **bukan** satu-satunya jalan. Urutan bisa
 * diubah dengan tombol naik/turun, dan pengelompokan bisa dipilih dengan
 * tombol keranjang (berfungsi juga untuk layar sentuh).
 */

interface RowStyleOptions {
    revealed: boolean;
    isCorrect: boolean;
    isDragging: boolean;
}

function rowStyle({ revealed, isCorrect, isDragging }: RowStyleOptions): string {
    if (revealed) {
        return isCorrect
            ? 'border-emerald-500/50 bg-emerald-50/70'
            : 'border-red/40 bg-red-tint';
    }

    return cn(
        'border-rule bg-canvas/40',
        isDragging && 'border-red/50 bg-canvas opacity-70',
    );
}

export function SortBlockView({
    block,
    materialId,
    onRecord,
}: ActivityProps<SortBlock>) {
    const blockId = block.id ?? 'sort';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'sort',
        onRecord,
    });

    const [order, setOrder] = useState<string[]>(() =>
        block.items.map((item) => item.id),
    );
    const [dragging, setDragging] = useState<string | null>(null);
    const [revealed, setRevealed] = useState(false);

    const texts = new Map(block.items.map((item) => [item.id, item.text]));

    function move(from: number, to: number) {
        if (to < 0 || to >= order.length || from === to) {
            return;
        }

        setOrder((current) => {
            const next = [...current];
            const [moved] = next.splice(from, 1);
            next.splice(to, 0, moved);

            return next;
        });
        setRevealed(false);
    }

    function dropOn(targetId: string) {
        if (dragging === null || dragging === targetId) {
            setDragging(null);

            return;
        }

        const from = order.indexOf(dragging);
        const to = order.indexOf(targetId);
        setDragging(null);
        move(from, to);
    }

    function check() {
        const correctCount = order.filter(
            (id, index) => block.answer[index] === id,
        ).length;
        const score = Math.round((correctCount / order.length) * 100);

        record(score, { order, correct: block.answer });
        setRevealed(true);
    }

    return (
        <section
            aria-label="Urutkan"
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Urutkan
            </p>
            <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                {block.prompt}
            </p>

            <ol className="mt-1.5 grid gap-1">
                {order.map((id, index) => {
                    const isCorrect = block.answer[index] === id;

                    return (
                        <li
                            key={id}
                            draggable={!revealed}
                            onDragStart={() => setDragging(id)}
                            onDragEnd={() => setDragging(null)}
                            onDragOver={(event) => event.preventDefault()}
                            onDrop={() => dropOn(id)}
                            className={cn(
                                'flex items-center gap-2 rounded-lg border px-2.5 py-1.5',
                                rowStyle({
                                    revealed,
                                    isCorrect,
                                    isDragging: dragging === id,
                                }),
                            )}
                        >
                            <span className="grid h-5 w-5 shrink-0 place-items-center rounded-md bg-surface text-[9px] font-bold text-ink/50 ring-1 ring-rule">
                                {index + 1}
                            </span>
                            <span className="min-w-0 flex-1 text-[10.5px] leading-snug font-medium text-ink">
                                {texts.get(id) ?? id}
                            </span>
                            <span className="flex shrink-0 items-center gap-1">
                                <button
                                    type="button"
                                    onClick={() => move(index, index - 1)}
                                    disabled={index === 0 || revealed}
                                    aria-label={`Naikkan "${texts.get(id) ?? id}"`}
                                    className="grid h-6 w-6 place-items-center rounded-md border border-rule bg-surface text-[9px] font-bold text-ink/60 disabled:opacity-30"
                                >
                                    ↑
                                </button>
                                <button
                                    type="button"
                                    onClick={() => move(index, index + 1)}
                                    disabled={index === order.length - 1 || revealed}
                                    aria-label={`Turunkan "${texts.get(id) ?? id}"`}
                                    className="grid h-6 w-6 place-items-center rounded-md border border-rule bg-surface text-[9px] font-bold text-ink/60 disabled:opacity-30"
                                >
                                    ↓
                                </button>
                            </span>
                        </li>
                    );
                })}
            </ol>

            <div aria-live="polite" className="mt-1.5">
                {revealed && (
                    <p className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5 text-[10px] font-medium text-ink/60">
                        {block.feedback?.correct && block.feedback?.wrong
                            ? order.every((id, index) => block.answer[index] === id)
                                ? block.feedback.correct
                                : `${block.feedback.wrong} Butir hijau sudah di posisi benar.`
                            : 'Periksa warna butir untuk melihat posisi yang benar.'}
                    </p>
                )}
            </div>

            <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                <p className="text-[9px] font-medium text-ink/35">
                    {result
                        ? `Terbaik ${result.score} · ${result.attempts}× dicoba`
                        : 'Geser, atau pakai tombol ↑ ↓.'}
                </p>

                <div className="flex items-center gap-1.5">
                    {revealed && (
                        <button
                            type="button"
                            onClick={() => setRevealed(false)}
                            className="inline-flex h-7 items-center rounded-lg border border-rule bg-surface px-2.5 text-[9.5px] font-bold text-ink/60"
                        >
                            Uraikan lagi
                        </button>
                    )}
                    <button
                        type="button"
                        onClick={check}
                        disabled={revealed}
                        className="inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white disabled:bg-ink/15 disabled:text-ink/40"
                    >
                        Periksa urutan
                    </button>
                </div>
            </div>
        </section>
    );
}

export function CategorizeBlockView({
    block,
    materialId,
    onRecord,
}: ActivityProps<CategorizeBlock>) {
    const blockId = block.id ?? 'categorize';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'categorize',
        onRecord,
    });

    const [assignments, setAssignments] = useState<Record<string, string>>({});
    const [revealed, setRevealed] = useState(false);

    const assignedCount = Object.keys(assignments).length;
    const allCorrect = block.items.every(
        (item) => assignments[item.id] === item.bucket,
    );

    function assign(itemId: string, bucketId: string) {
        setAssignments((current) => ({ ...current, [itemId]: bucketId }));
        setRevealed(false);
    }

    function check() {
        const correctCount = block.items.filter(
            (item) => assignments[item.id] === item.bucket,
        ).length;
        const score = Math.round((correctCount / block.items.length) * 100);

        record(score, { assignments });
        setRevealed(true);
    }

    return (
        <section
            aria-label="Kelompokkan"
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Kelompokkan
            </p>
            <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                {block.prompt}
            </p>

            <ul className="mt-1.5 grid gap-1">
                {block.items.map((item) => {
                    const chosen = assignments[item.id];
                    const isCorrect = chosen === item.bucket;

                    return (
                        <li
                            key={item.id}
                            className={cn(
                                'rounded-lg border px-2.5 py-1.5',
                                rowStyle({
                                    revealed,
                                    isCorrect,
                                    isDragging: false,
                                }),
                            )}
                        >
                            <p className="text-[10.5px] leading-snug font-medium text-ink">
                                {item.text}
                            </p>

                            <div
                                role="group"
                                aria-label={`Keranjang untuk "${item.text}"`}
                                className="mt-1 flex flex-wrap gap-1"
                            >
                                {block.buckets.map((bucket) => {
                                    const active = chosen === bucket.id;

                                    return (
                                        <button
                                            key={bucket.id}
                                            type="button"
                                            onClick={() => assign(item.id, bucket.id)}
                                            aria-pressed={active}
                                            disabled={revealed}
                                            className={cn(
                                                'rounded-md border px-2 py-0.5 text-[9.5px] font-bold transition-colors',
                                                active
                                                    ? 'border-red/50 bg-red text-white'
                                                    : 'border-rule bg-surface text-ink/55',
                                                revealed &&
                                                    active &&
                                                    !isCorrect &&
                                                    'border-red/40 bg-red-tint text-ink',
                                            )}
                                        >
                                            {bucket.label}
                                        </button>
                                    );
                                })}
                            </div>
                        </li>
                    );
                })}
            </ul>

            <div aria-live="polite" className="mt-1.5">
                {revealed && (
                    <p className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5 text-[10px] font-medium text-ink/60">
                        {allCorrect
                            ? block.feedback?.correct
                            : `${block.feedback?.wrong} Butir merah perlu dipindahkan.`}
                    </p>
                )}
            </div>

            <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                <p className="text-[9px] font-medium text-ink/35">
                    {result
                        ? `Terbaik ${result.score} · ${result.attempts}× dicoba`
                        : `${assignedCount}/${block.items.length} sudah dipilih.`}
                </p>

                <button
                    type="button"
                    onClick={check}
                    disabled={revealed || assignedCount < block.items.length}
                    className="inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white disabled:bg-ink/15 disabled:text-ink/40"
                >
                    Periksa
                </button>
            </div>
        </section>
    );
}