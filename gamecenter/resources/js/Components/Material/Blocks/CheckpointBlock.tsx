import { useState } from 'react';

import type { CheckpointBlock } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { useBlockAnswer } from '@/lib/material/useBlockAnswer';
import { cn } from '@/lib/utils';

interface CheckpointBlockProps {
    block: CheckpointBlock;
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}

/**
 * Kuis formatif di tengah materi (plan §4.3).
 *
 * Umpan balik selalu menjelaskan alasan, boleh diulang tanpa batas, dan tidak
 * masuk skor sesi resmi. Percobaan pertama tetap tercatat di `attempts`.
 */
export default function CheckpointBlockView({
    block,
    materialId,
    onRecord,
}: CheckpointBlockProps) {
    const blockId = block.id ?? 'checkpoint';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'checkpoint',
        onRecord,
    });

    const [selected, setSelected] = useState<string | null>(null);
    const [revealed, setRevealed] = useState(false);

    const correctChoice = block.choices.find((choice) => choice.correct === true);
    const isCorrect = revealed && selected !== null && selected === correctChoice?.id;

    function check() {
        if (selected === null) {
            return;
        }

        record(selected === correctChoice?.id ? 100 : 0, {
            selected,
            correct: correctChoice?.id ?? null,
        });
        setRevealed(true);
    }

    return (
        <section
            aria-label="Cek pemahaman"
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <fieldset>
                <legend className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                    Cek pemahaman
                </legend>

                <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                    {block.question}
                </p>

                <div className="mt-1.5 grid gap-1">
                    {block.choices.map((choice) => {
                        const chosen = selected === choice.id;
                        const showCorrect =
                            revealed && choice.correct === true;
                        const showWrong =
                            revealed && chosen && choice.correct !== true;

                        return (
                            <label
                                key={choice.id}
                                className={cn(
                                    'flex cursor-pointer items-start gap-2 rounded-lg border px-2.5 py-1.5 text-[10.5px] font-medium transition-colors',
                                    showCorrect &&
                                        'border-emerald-500/50 bg-emerald-50/70 text-ink',
                                    showWrong && 'border-red/40 bg-red-tint text-ink',
                                    !showCorrect &&
                                        !showWrong &&
                                        (chosen
                                            ? 'border-red/40 bg-canvas'
                                            : 'border-rule bg-canvas/40 hover:bg-canvas/70'),
                                )}
                            >
                                <input
                                    type="radio"
                                    name={`checkpoint-${materialId}-${blockId}`}
                                    value={choice.id}
                                    checked={chosen}
                                    onChange={() => setSelected(choice.id)}
                                    disabled={revealed}
                                    className="mt-0.5 accent-[var(--color-red)]"
                                />
                                <span>{choice.text}</span>
                            </label>
                        );
                    })}
                </div>
            </fieldset>

            <div aria-live="polite" className="mt-1.5">
                {revealed && (
                    <div className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5">
                        <p
                            className={cn(
                                'text-[10px] font-bold',
                                isCorrect ? 'text-emerald-700' : 'text-red',
                            )}
                        >
                            {isCorrect
                                ? block.feedback?.correct ?? 'Benar.'
                                : block.feedback?.wrong ?? 'Belum tepat.'}
                        </p>
                        {block.explanation && (
                            <p className="mt-0.5 text-[10px] leading-relaxed font-medium text-ink/55">
                                {block.explanation}
                            </p>
                        )}
                    </div>
                )}
            </div>

            <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                <p className="text-[9px] font-medium text-ink/35">
                    {result
                        ? `Terbaik ${result.score} · ${result.attempts}× dicoba`
                        : 'Latihan formatif — tidak masuk nilai.'}
                </p>

                {revealed ? (
                    <button
                        type="button"
                        onClick={() => {
                            setRevealed(false);
                            setSelected(null);
                        }}
                        className="inline-flex h-7 items-center rounded-lg border border-rule bg-surface px-2.5 text-[9.5px] font-bold text-ink/60"
                    >
                        Coba lagi
                    </button>
                ) : (
                    <button
                        type="button"
                        onClick={check}
                        disabled={selected === null}
                        className="inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white disabled:bg-ink/15 disabled:text-ink/40"
                    >
                        Periksa
                    </button>
                )}
            </div>
        </section>
    );
}
