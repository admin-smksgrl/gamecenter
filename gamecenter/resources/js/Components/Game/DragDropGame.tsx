import { useState } from 'react';
import type { DragEvent } from 'react';

import {
    expectedOrder,
    initialOrder,
    orderingPieces,
} from '@/lib/game/game-engine';
import type { GameQuestion, GameResponse } from '@/lib/game/game-engine';
import { cn } from '@/lib/utils';

interface DragDropGameProps {
    question: GameQuestion;
    response: GameResponse | null;
    onChange: (response: GameResponse) => void;
    disabled: boolean;
    revealed: boolean;
}

export default function DragDropGame({
    question,
    response,
    onChange,
    disabled,
    revealed,
}: DragDropGameProps) {
    const [dragging, setDragging] = useState<number | null>(null);
    const pieces = orderingPieces(question);
    const pieceMap = new Map(pieces.map((piece) => [piece.id, piece]));
    const configuredOrder = response?.order ?? initialOrder(question);
    const knownOrder = configuredOrder.filter((id) => pieceMap.has(id));
    const order = [
        ...knownOrder,
        ...pieces
            .map((piece) => piece.id)
            .filter((id) => !knownOrder.includes(id)),
    ];
    const correctOrder = expectedOrder(question);

    function move(from: number, to: number) {
        if (disabled || revealed || from === to) {
            return;
        }

        const next = [...order];
        const [moved] = next.splice(from, 1);

        if (moved === undefined) {
            return;
        }

        next.splice(to, 0, moved);
        onChange({ order: next });
    }

    function handleDrop(event: DragEvent<HTMLLIElement>, to: number) {
        event.preventDefault();

        if (dragging !== null) {
            move(dragging, to);
        }

        setDragging(null);
    }

    if (pieces.length === 0) {
        return (
            <p className="rounded-2xl border border-rule bg-canvas/50 px-4 py-5 text-center text-[12px] font-semibold text-ink/45">
                Soal ini belum memiliki potongan yang bisa disusun.
            </p>
        );
    }

    return (
        <div className="space-y-2.5">
            <p className="text-[10.5px] font-semibold text-ink/45">
                Susun urutan yang benar. Tarik kartu atau gunakan tombol panah.
            </p>

            <ol className="grid gap-2">
                {order.map((id, index) => {
                    const piece = pieceMap.get(id);
                    const isCorrectPosition =
                        revealed && correctOrder[index] === id;

                    if (!piece) {
                        return null;
                    }

                    return (
                        <li
                            key={id}
                            draggable={!disabled && !revealed}
                            onDragStart={() => setDragging(index)}
                            onDragEnd={() => setDragging(null)}
                            onDragOver={(event) => event.preventDefault()}
                            onDrop={(event) => handleDrop(event, index)}
                            className={cn(
                                'flex items-center gap-2.5 rounded-2xl border bg-surface px-3 py-2.5 transition-all sm:px-3.5',
                                !revealed &&
                                    'border-rule hover:border-red/30',
                                dragging === index &&
                                    'border-red bg-red-tint opacity-70',
                                revealed &&
                                    isCorrectPosition &&
                                    'border-red/60 bg-red-tint',
                                revealed &&
                                    !isCorrectPosition &&
                                    'border-red/40 bg-red-tint/60',
                            )}
                        >
                            <span
                                className={cn(
                                    'grid h-7 w-7 shrink-0 place-items-center rounded-lg font-serif text-[11px] font-bold tabular-nums ring-1',
                                    revealed && isCorrectPosition
                                        ? 'bg-red text-white ring-red'
                                        : 'bg-canvas text-ink/45 ring-rule',
                                )}
                            >
                                {index + 1}
                            </span>

                            <span className="min-w-0 flex-1 text-[12.5px] leading-snug font-semibold text-ink/75">
                                {piece.text}
                            </span>

                            <span className="flex shrink-0 items-center gap-0.5">
                                <button
                                    type="button"
                                    disabled={disabled || revealed || index === 0}
                                    onClick={() => move(index, index - 1)}
                                    aria-label={`Naikkan ${piece.text}`}
                                    className="grid h-6 w-6 place-items-center rounded-md bg-canvas text-[11px] font-bold text-ink/45 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red disabled:pointer-events-none disabled:opacity-30"
                                >
                                    ↑
                                </button>
                                <button
                                    type="button"
                                    disabled={
                                        disabled ||
                                        revealed ||
                                        index === order.length - 1
                                    }
                                    onClick={() => move(index, index + 1)}
                                    aria-label={`Turunkan ${piece.text}`}
                                    className="grid h-6 w-6 place-items-center rounded-md bg-canvas text-[11px] font-bold text-ink/45 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red disabled:pointer-events-none disabled:opacity-30"
                                >
                                    ↓
                                </button>
                            </span>
                        </li>
                    );
                })}
            </ol>
        </div>
    );
}
