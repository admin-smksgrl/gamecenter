import { useCallback, useEffect, useRef, useState } from 'react';

import type { ChallengeBlock } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { useBlockAnswer } from '@/lib/material/useBlockAnswer';
import { cn } from '@/lib/utils';

interface ChallengeBlockProps {
    block: ChallengeBlock;
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}

interface Attempt {
    question: string;
    given: string;
    expected: string;
    correct: boolean;
}

/** Jawaban dianggap sama walau beda huruf besar/kecil, spasi, atau tanda baca. */
export function normalizeAnswer(value: string): string {
    return value
        .toLowerCase()
        .replace(/[^a-z0-9/+.-]/g, '')
        .trim();
}

/**
 * Tantangan kilat (plan §4.6).
 *
 * Timer 60–120 detik, 5–8 butir singkat, rekor pribadi disimpan bersama skor
 * blok. Timer **boleh dimatikan** sebelum mulai (plan §7.2) supaya waktu tidak
 * menjadi satu-satunya hambatan; umpan balik akhir menampilkan butir yang
 * salah beserta jawaban benarnya.
 */
export default function ChallengeBlockView({
    block,
    materialId,
    onRecord,
}: ChallengeBlockProps) {
    const blockId = block.id ?? 'challenge';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'challenge',
        onRecord,
    });

    const limit = block.time_limit ?? 0;
    const total = block.items.length;

    const [phase, setPhase] = useState<'idle' | 'playing' | 'done'>('idle');
    const [useTimer, setUseTimer] = useState(limit > 0);
    const [seconds, setSeconds] = useState(limit);
    const [index, setIndex] = useState(0);
    const [answer, setAnswer] = useState('');
    const [attempts, setAttempts] = useState<Attempt[]>([]);
    const recorded = useRef(false);

    const finish = useCallback(
        (finalAttempts: Attempt[]) => {
            setPhase('done');

            if (recorded.current) {
                return;
            }

            recorded.current = true;

            const correct = finalAttempts.filter((item) => item.correct).length;
            const percent =
                finalAttempts.length === 0
                    ? 0
                    : Math.round((correct / total) * 100);

            record(percent, {
                correct,
                total,
                answered: finalAttempts.length,
                results: finalAttempts,
            });
        },
        [record, total],
    );

    // Hitung mundur; berhenti sendiri saat waktu habis.
    useEffect(() => {
        if (phase !== 'playing' || !useTimer || limit <= 0) {
            return;
        }

        const timer = window.setInterval(() => {
            setSeconds((current) => {
                if (current <= 1) {
                    window.clearInterval(timer);
                    setAttempts((currentAttempts) => {
                        finish(currentAttempts);

                        return currentAttempts;
                    });

                    return 0;
                }

                return current - 1;
            });
        }, 1000);

        return () => window.clearInterval(timer);
    }, [phase, useTimer, limit, finish]);

    function start() {
        recorded.current = false;
        setPhase('playing');
        setSeconds(limit);
        setIndex(0);
        setAnswer('');
        setAttempts([]);
    }

    function submit() {
        const item = block.items[index];

        if (!item) {
            return;
        }

        const nextAttempts: Attempt[] = [
            ...attempts,
            {
                question: item.question,
                given: answer,
                expected: item.answer,
                correct:
                    normalizeAnswer(answer) === normalizeAnswer(item.answer),
            },
        ];

        setAttempts(nextAttempts);
        setAnswer('');

        if (index + 1 >= total) {
            finish(nextAttempts);
            return;
        }

        setIndex(index + 1);
    }

    function skip() {
        submit();
    }

    const correctCount = attempts.filter((item) => item.correct).length;

    if (phase === 'idle') {
        return (
            <section
                aria-label="Tantangan kilat"
                className="rounded-xl border border-rule bg-surface px-3 py-2.5"
            >
                <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                    Tantangan kilat
                </p>

                <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                    {block.title ?? 'Tantangan kilat'}
                </p>

                <p className="mt-0.5 text-[10px] leading-relaxed font-medium text-ink/55">
                    {total} butir singkat
                    {limit > 0 ? ` · ${limit} detik` : ''}. Tidak masuk nilai —
                    murni latihan mandiri.
                </p>

                {limit > 0 && (
                    <label className="mt-1.5 flex items-center gap-1.5 text-[10px] font-semibold text-ink/60">
                        <input
                            type="checkbox"
                            checked={useTimer}
                            onChange={(event) => setUseTimer(event.target.checked)}
                            className="accent-[var(--color-red)]"
                        />
                        Pakai batas waktu (boleh dimatikan)
                    </label>
                )}

                <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                    <p className="text-[9px] font-medium text-ink/35">
                        {result
                            ? `Rekor ${result.score}% · ${result.attempts}× dimainkan`
                            : 'Rekor pribadi tersimpan di perangkat ini.'}
                    </p>

                    <button
                        type="button"
                        onClick={start}
                        className="inline-flex h-7 items-center rounded-lg bg-red px-3 text-[9.5px] font-bold text-white"
                    >
                        Mulai
                    </button>
                </div>
            </section>
        );
    }

    if (phase === 'playing') {
        const item = block.items[index];

        return (
            <section
                aria-label="Tantangan kilat"
                className="rounded-xl border border-rule bg-surface px-3 py-2.5"
            >
                <div className="flex items-center justify-between">
                    <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                        Butir {index + 1} / {total}
                    </p>

                    {useTimer && limit > 0 && (
                        <p
                            aria-live="off"
                            className={cn(
                                'text-[10px] font-bold tabular-nums',
                                seconds <= 10 ? 'text-red' : 'text-ink/45',
                            )}
                        >
                            {seconds}s
                        </p>
                    )}
                </div>

                <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                    {item?.question}
                </p>

                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        submit();
                    }}
                    className="mt-1.5 flex gap-1.5"
                >
                    <input
                        // Fokus otomatis agar bisa langsung mengetik.
                        autoFocus
                        value={answer}
                        onChange={(event) => setAnswer(event.target.value)}
                        aria-label={`Jawaban butir ${index + 1}`}
                        placeholder="Jawaban singkat…"
                        className="h-8 min-w-0 flex-1 rounded-lg border border-rule bg-canvas/60 px-2.5 text-[10.5px] font-semibold text-ink outline-none focus:border-red/50"
                    />

                    <button
                        type="submit"
                        disabled={answer.trim() === ''}
                        className="inline-flex h-8 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white disabled:bg-ink/15 disabled:text-ink/40"
                    >
                        Kirim
                    </button>
                </form>

                <div className="mt-1 flex items-center justify-between">
                    <button
                        type="button"
                        onClick={skip}
                        className="text-[9px] font-semibold text-ink/35 underline-offset-2 hover:underline"
                    >
                        Lewati butir ini
                    </button>

                    <p className="text-[9px] font-medium text-ink/35">
                        {correctCount} benar
                    </p>
                </div>
            </section>
        );
    }

    return (
        <section
            aria-label="Hasil tantangan"
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Hasil tantangan
            </p>

            <p
                aria-live="polite"
                className="mt-1 text-[11.5px] leading-snug font-bold text-ink"
            >
                {correctCount} dari {total} benar
            </p>

            <p className="mt-0.5 text-[10px] font-medium text-ink/55">
                {block.feedback?.correct &&
                    correctCount === total &&
                    block.feedback.correct}
                {correctCount < total &&
                    (block.feedback?.wrong ??
                        'Periksa butir yang belum tepat di bawah.')}
            </p>

            {attempts.some((item) => !item.correct) && (
                <ul className="mt-1 grid gap-1">
                    {attempts
                        .filter((item) => !item.correct)
                        .map((item, position) => (
                            <li
                                key={`wrong-${position}`}
                                className="rounded-lg border border-rule bg-canvas/50 px-2 py-1"
                            >
                                <p className="text-[10px] font-semibold text-ink/75">
                                    {item.question}
                                </p>
                                <p className="text-[9.5px] font-medium text-ink/45">
                                    Jawabanmu: {item.given || '—'} · seharusnya{' '}
                                    <strong className="text-ink/70">
                                        {item.expected}
                                    </strong>
                                </p>
                            </li>
                        ))}
                </ul>
            )}

            <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                <p className="text-[9px] font-medium text-ink/35">
                    {result
                        ? `Rekor ${result.score}% · ${result.attempts}× dimainkan`
                        : 'Latihan mandiri — tidak masuk nilai.'}
                </p>

                <button
                    type="button"
                    onClick={start}
                    className="inline-flex h-7 items-center rounded-lg border border-rule bg-surface px-2.5 text-[9.5px] font-bold text-ink/60"
                >
                    Main lagi
                </button>
            </div>
        </section>
    );
}
