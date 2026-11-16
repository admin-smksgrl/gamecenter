import { useState } from 'react';

import {
    expectedPairs,
    matchingPairs,
    matchingRightOptions,
    shuffleWithSeed,
} from '@/lib/game/game-engine';
import type { GameQuestion, GameResponse } from '@/lib/game/game-engine';
import { cn } from '@/lib/utils';

interface MatchGameProps {
    question: GameQuestion;
    response: GameResponse | null;
    onChange: (response: GameResponse) => void;
    disabled: boolean;
    revealed: boolean;
}

export default function MatchGame({
    question,
    response,
    onChange,
    disabled,
    revealed,
}: MatchGameProps) {
    const [selectedLeft, setSelectedLeft] = useState<string | null>(null);
    const pairs = matchingPairs(question);
    const expected = expectedPairs(question);
    const rights = shuffleWithSeed(matchingRightOptions(question), question.id);
    const mapping = response?.pairs ?? {};

    function assign(leftId: string, right: string) {
        if (disabled || revealed) {
            return;
        }

        const next: Record<string, string> = {};

        for (const [key, value] of Object.entries(mapping)) {
            if (value !== right && key !== leftId) {
                next[key] = value;
            }
        }

        next[leftId] = right;
        onChange({ pairs: next });
        setSelectedLeft(null);
    }

    function clear(leftId: string) {
        if (disabled || revealed) {
            return;
        }

        const next = { ...mapping };
        delete next[leftId];
        onChange({ pairs: next });
    }

    if (pairs.length === 0) {
        return (
            <p className="rounded-2xl border border-rule bg-canvas/50 px-4 py-5 text-center text-[12px] font-semibold text-ink/45">
                Soal ini belum memiliki pasangan untuk dijodohkan.
            </p>
        );
    }

    return (
        <div className="space-y-3">
            <p className="text-[10.5px] font-semibold text-ink/45">
                Pilih kartu kiri, lalu pilih pasangannya di kolom kanan.
            </p>

            <div className="grid gap-3 sm:grid-cols-2">
                <div className="grid content-start gap-2">
                    {pairs.map((pair) => {
                        const value = mapping[pair.id];
                        const isSelected = selectedLeft === pair.id;
                        const isCorrect = revealed && value === expected[pair.id];

                        return (
                            <div
                                key={pair.id}
                                className={cn(
                                    'rounded-2xl border bg-surface p-2.5 transition-all',
                                    isSelected
                                        ? 'border-red shadow-[0_0_0_1px_var(--color-red)]'
                                        : 'border-rule',
                                    revealed &&
                                        isCorrect &&
                                        'border-red/60 bg-red-tint',
                                    revealed &&
                                        !isCorrect &&
                                        'border-red/40 bg-red-tint/50',
                                )}
                            >
                                <button
                                    type="button"
                                    disabled={disabled || revealed}
                                    onClick={() =>
                                        setSelectedLeft((current) =>
                                            current === pair.id ? null : pair.id,
                                        )
                                    }
                                    className="flex w-full items-center gap-2 text-left"
                                >
                                    <span
                                        className={cn(
                                            'grid h-6 w-6 shrink-0 place-items-center rounded-md text-[9px] font-black ring-1',
                                            isSelected
                                                ? 'bg-red text-white ring-red'
                                                : 'bg-canvas text-ink/40 ring-rule',
                                        )}
                                    >
                                        {revealed
                                            ? isCorrect
                                                ? '✓'
                                                : '×'
                                            : pair.id.replace(/\D/g, '') ||
                                              '•'}
                                    </span>
                                    <span className="min-w-0 flex-1 text-[12px] leading-snug font-bold text-ink/75">
                                        {pair.left}
                                    </span>
                                </button>

                                <div className="mt-2 flex items-center gap-1.5">
                                    {value ? (
                                        <span
                                            className={cn(
                                                'flex min-w-0 flex-1 items-center gap-1 rounded-lg px-2 py-1 text-[10.5px] font-semibold',
                                                revealed && isCorrect
                                                    ? 'bg-red text-white'
                                                    : 'bg-red-tint text-red',
                                            )}
                                        >
                                            <span className="truncate">
                                                {value}
                                            </span>
                                        </span>
                                    ) : (
                                        <span className="flex-1 rounded-lg border border-dashed border-rule px-2 py-1 text-[10px] font-semibold text-ink/30">
                                            Belum dipasangkan
                                        </span>
                                    )}

                                    {value && !revealed && (
                                        <button
                                            type="button"
                                            onClick={() => clear(pair.id)}
                                            aria-label={`Lepas pasangan ${pair.left}`}
                                            className="grid h-6 w-6 shrink-0 place-items-center rounded-md text-[11px] font-bold text-ink/35 transition-colors hover:bg-red-tint hover:text-red"
                                        >
                                            ×
                                        </button>
                                    )}
                                </div>

                                {revealed && !isCorrect && (
                                    <p className="mt-1.5 text-[9.5px] font-semibold text-red">
                                        Jawaban: {expected[pair.id]}
                                    </p>
                                )}
                            </div>
                        );
                    })}
                </div>

                <div className="grid content-start gap-2">
                    {rights.map((right) => {
                        const usedBy = Object.entries(mapping).find(
                            ([, value]) => value === right,
                        )?.[0];
                        const canAssign =
                            selectedLeft !== null && !disabled && !revealed;

                        return (
                            <button
                                key={right}
                                type="button"
                                disabled={!canAssign}
                                onClick={() => {
                                    if (selectedLeft) {
                                        assign(selectedLeft, right);
                                    }
                                }}
                                className={cn(
                                    'rounded-2xl border px-3 py-2.5 text-left text-[12px] leading-snug font-semibold transition-all',
                                    usedBy
                                        ? 'border-red/30 bg-red-tint/60 text-ink/70'
                                        : 'border-rule bg-surface text-ink/65',
                                    canAssign &&
                                        'hover:border-red/40 hover:bg-red-tint/30',
                                    !canAssign &&
                                        !usedBy &&
                                        'cursor-default opacity-65',
                                )}
                            >
                                {right}
                                {usedBy && (
                                    <span className="mt-1 block text-[9px] font-bold tracking-[0.1em] text-red uppercase">
                                        Sudah dipakai
                                    </span>
                                )}
                            </button>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}
