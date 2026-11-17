import { useState } from 'react';

import type { LabelBlock } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { useBlockAnswer } from '@/lib/material/useBlockAnswer';
import { cn } from '@/lib/utils';
import { Inline } from '@/Components/Material/Blocks/TextBlocks';

interface LabelBlockProps {
    block: LabelBlock;
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}

/**
 * Aktivitas "beri label" pada gambar buku (plan §4.1 & §7.2).
 *
 * Alurnya dipilih agar bisa dipakai tanpa drag: pilih label → ketuk titik.
 * Semua kontrol berupa tombol sehingga bisa dioperasikan keyboard dan pembaca
 * layar, sementara posisi titik tetap ternormalisasi (0..1) supaya akurat di
 * layar kecil maupun besar.
 */
export default function LabelBlockView({
    block,
    materialId,
    onRecord,
}: LabelBlockProps) {
    const blockId = block.id ?? 'label';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'label',
        onRecord,
    });

    const [selectedChoice, setSelectedChoice] = useState<string | null>(null);
    const [assignments, setAssignments] = useState<Record<string, string>>({});
    const [revealed, setRevealed] = useState(false);

    const total = block.targets.length;
    const correctCount = block.targets.filter(
        (target) => assignments[target.id] === target.answer,
    ).length;
    const allAssigned = block.targets.every((target) => assignments[target.id]);

    function assign(targetId: string) {
        if (revealed || !selectedChoice) {
            return;
        }

        setAssignments((current) => ({
            ...current,
            [targetId]: selectedChoice,
        }));
    }

    function check() {
        const score = total === 0 ? 0 : Math.round((correctCount / total) * 100);

        record(score, { assignments, correct: correctCount, total });
        setRevealed(true);
    }

    function reset() {
        setAssignments({});
        setSelectedChoice(null);
        setRevealed(false);
    }

    return (
        <section
            aria-label="Beri label"
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Beri label
            </p>

            <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                {block.prompt}
            </p>

            <div className="mt-1.5 flex flex-wrap gap-1">
                {block.choices.map((choice) => {
                    const used = Object.values(assignments).includes(choice);
                    const isSelected = selectedChoice === choice;

                    return (
                        <button
                            key={choice}
                            type="button"
                            onClick={() => setSelectedChoice(choice)}
                            aria-pressed={isSelected}
                            disabled={revealed}
                            className={cn(
                                'inline-flex h-7 items-center rounded-lg border px-2 text-[9.5px] font-bold transition-colors',
                                isSelected
                                    ? 'border-red bg-red text-white'
                                    : used
                                      ? 'border-rule bg-canvas/40 text-ink/35'
                                      : 'border-rule bg-canvas/60 text-ink/70 hover:border-red/40',
                            )}
                        >
                            {choice}
                        </button>
                    );
                })}
            </div>

            <div className="relative mt-1.5 overflow-hidden rounded-lg border border-rule bg-canvas/40">
                <img
                    src={block.image_url}
                    alt="Gambar untuk diberi label"
                    loading="lazy"
                    className="block w-full"
                />

                {block.targets.map((target, index) => {
                    const assigned = assignments[target.id];
                    const isCorrect = assigned === target.answer;
                    const showState = revealed && assigned;

                    return (
                        <button
                            key={target.id}
                            type="button"
                            onClick={() => assign(target.id)}
                            aria-label={`Titik ${index + 1}${
                                assigned ? `: ${assigned}` : ''
                            }${revealed ? (isCorrect ? ' benar' : ' belum tepat') : ''}`}
                            style={{
                                left: `${target.x * 100}%`,
                                top: `${target.y * 100}%`,
                            }}
                            className={cn(
                                'absolute flex h-6 min-w-6 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border px-1 text-[9px] font-bold shadow-sm transition-colors',
                                showState
                                    ? isCorrect
                                        ? 'border-emerald-600 bg-emerald-600 text-white'
                                        : 'border-red bg-red text-white'
                                    : assigned
                                      ? 'border-red/60 bg-white text-ink'
                                      : 'border-red/50 bg-white/95 text-red hover:bg-red hover:text-white',
                            )}
                        >
                            {assigned ? assigned.slice(0, 8) : index + 1}
                        </button>
                    );
                })}
            </div>

            <div aria-live="polite" className="mt-1.5">
                {revealed && (
                    <div className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5">
                        <p
                            className={cn(
                                'text-[10px] font-bold',
                                correctCount === total
                                    ? 'text-emerald-700'
                                    : 'text-red',
                            )}
                        >
                            {correctCount === total ? (
                                <Inline
                                    text={
                                        block.feedback?.correct ??
                                        'Semua label tepat.'
                                    }
                                />
                            ) : (
                                <Inline
                                    text={
                                        block.feedback?.wrong ??
                                        `${correctCount} dari ${total} label tepat.`
                                    }
                                />
                            )}
                        </p>

                        <ul className="mt-0.5 grid gap-0.5">
                            {block.targets.map((target, index) => (
                                <li
                                    key={`answer-${target.id}`}
                                    className="text-[9.5px] font-medium text-ink/55"
                                >
                                    Titik {index + 1}: {target.answer}
                                </li>
                            ))}
                        </ul>
                    </div>
                )}

                {!revealed && selectedChoice && (
                    <p className="text-[9.5px] font-medium text-ink/45">
                        Label “{selectedChoice}” dipilih — ketuk titik pada gambar.
                    </p>
                )}
            </div>

            <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                <p className="text-[9px] font-medium text-ink/35">
                    {result
                        ? `Terbaik ${result.score} · ${result.attempts}× dicoba`
                        : `Latihan formatif — ${total} titik.`}
                </p>

                {revealed ? (
                    <button
                        type="button"
                        onClick={reset}
                        className="inline-flex h-7 items-center rounded-lg border border-rule bg-surface px-2.5 text-[9.5px] font-bold text-ink/60"
                    >
                        Coba lagi
                    </button>
                ) : (
                    <button
                        type="button"
                        onClick={check}
                        disabled={!allAssigned}
                        className="inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white disabled:bg-ink/15 disabled:text-ink/40"
                    >
                        Periksa
                    </button>
                )}
            </div>
        </section>
    );
}
