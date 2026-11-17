import { useEffect, useMemo, useRef, useState } from 'react';

import type { ScenarioBlock, ScenarioChoice } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { useBlockAnswer } from '@/lib/material/useBlockAnswer';
import { cn } from '@/lib/utils';
import { Inline } from '@/Components/Material/Blocks/TextBlocks';

interface ScenarioBlockProps {
    block: ScenarioBlock;
    materialId: number;
    onRecord?: (payload: MaterialBlockPayload) => void;
}

interface Decision {
    nodeId: string;
    nodeText: string;
    choice: string;
    feedback?: string;
    score: number;
}

const OUTCOME_LABEL: Record<string, string> = {
    good: 'Keputusan yang baik',
    neutral: 'Bisa lebih baik',
    bad: 'Kurang tepat',
};

/**
 * Skenario bercabang (plan §4.4).
 *
 * Alurnya: baca situasi → pilih tindakan → baca umpan balik → lanjut. Setiap
 * pilihan berupa `<button>` supaya bisa dioperasikan keyboard, dan seluruh
 * riwayat keputusan ditampilkan lagi di akhir sebagai ringkasan. Skor yang
 * disimpan adalah **skor pembentukan karakter**, bukan nilai akademik.
 */
export default function ScenarioBlockView({
    block,
    materialId,
    onRecord,
}: ScenarioBlockProps) {
    const blockId = block.id ?? 'scenario';
    const { result, record } = useBlockAnswer({
        materialId,
        blockId,
        blockType: 'scenario',
        onRecord,
    });

    const nodesById = useMemo(
        () => new Map(block.nodes.map((node) => [node.id, node])),
        [block.nodes],
    );

    const [currentId, setCurrentId] = useState(block.start);
    const [decisions, setDecisions] = useState<Decision[]>([]);
    const [pending, setPending] = useState<ScenarioChoice | null>(null);
    const [maxScore, setMaxScore] = useState(0);
    const recorded = useRef(false);

    const current = nodesById.get(currentId) ?? nodesById.get(block.start);
    const finished = current !== undefined && current.end === true;

    const earned = decisions.reduce((sum, decision) => sum + decision.score, 0);
    const percent =
        maxScore <= 0 ? 0 : Math.round((Math.min(earned, maxScore) / maxScore) * 100);

    // Simpan hasil sekali saat skenario selesai.
    useEffect(() => {
        if (!finished || recorded.current) {
            return;
        }

        recorded.current = true;
        record(percent, {
            path: decisions.map((decision) => decision.nodeId),
            choices: decisions.map((decision) => decision.choice),
            score: earned,
            maxScore,
        });
    }, [finished, percent, decisions, earned, maxScore, record]);

    function choose(choice: ScenarioChoice) {
        const node = current;

        if (!node) {
            return;
        }

        setDecisions((history) => [
            ...history,
            {
                nodeId: node.id,
                nodeText: node.text,
                choice: choice.text,
                feedback: choice.feedback,
                score: Number(choice.score ?? 0),
            },
        ]);

        setMaxScore((best) =>
            best +
            Math.max(
                Number(choice.score ?? 0),
                ...(node.choices ?? []).map((option) => Number(option.score ?? 0)),
                0,
            ),
        );
        setPending(choice);
    }

    function advance(choice: ScenarioChoice) {
        setPending(null);

        if (choice.next && nodesById.has(choice.next)) {
            setCurrentId(choice.next);
        }
    }

    function restart() {
        recorded.current = false;
        setCurrentId(block.start);
        setDecisions([]);
        setPending(null);
        setMaxScore(0);
    }

    if (!current) {
        return (
            <p className="rounded-lg border border-dashed border-rule px-2.5 py-1.5 text-[10px] font-semibold text-ink/40">
                Skenario tidak punya node awal yang valid.
            </p>
        );
    }

    if (finished) {
        return (
            <section
                aria-label="Ringkasan skenario"
                className="rounded-xl border border-rule bg-surface px-3 py-2.5"
            >
                <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                    Skenario selesai
                </p>

                <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                    <Inline text={current.text} />
                </p>

                {current.outcome && (
                    <p
                        className={cn(
                            'mt-1 inline-flex items-center rounded-full px-2 py-0.5 text-[9px] font-bold',
                            current.outcome === 'good' &&
                                'bg-emerald-100 text-emerald-800',
                            current.outcome === 'neutral' &&
                                'bg-amber-100 text-amber-800',
                            current.outcome === 'bad' && 'bg-red-tint text-red',
                        )}
                    >
                        {OUTCOME_LABEL[current.outcome] ?? current.outcome}
                    </p>
                )}

                <p className="mt-1.5 text-[10px] font-semibold text-ink/55">
                    Skor keputusan {earned} dari {maxScore} ({percent}%)
                </p>

                <ol className="mt-1 grid gap-1">
                    {decisions.map((decision, index) => (
                        <li
                            key={`${decision.nodeId}-${index}`}
                            className="rounded-lg border border-rule bg-canvas/50 px-2 py-1"
                        >
                            <p className="text-[9px] font-bold text-ink/40">
                                Langkah {index + 1}
                            </p>
                            <p className="text-[10px] font-semibold text-ink/80">
                                {decision.choice}
                            </p>
                            {decision.feedback && (
                                <p className="mt-0.5 text-[9.5px] leading-relaxed font-medium text-ink/50">
                                    <Inline text={decision.feedback} />
                                </p>
                            )}
                        </li>
                    ))}
                </ol>

                <div className="mt-1.5 flex flex-wrap items-center justify-between gap-2">
                    <p className="text-[9px] font-medium text-ink/35">
                        {result
                            ? `Terbaik ${result.score}% · ${result.attempts}× dimainkan`
                            : 'Latihan pengambilan keputusan — tidak masuk nilai.'}
                    </p>

                    <button
                        type="button"
                        onClick={restart}
                        className="inline-flex h-7 items-center rounded-lg border border-rule bg-surface px-2.5 text-[9.5px] font-bold text-ink/60"
                    >
                        Ulangi skenario
                    </button>
                </div>
            </section>
        );
    }

    return (
        <section
            aria-label={`Skenario: ${block.title}`}
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <p className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Skenario · langkah {decisions.length + 1}
            </p>

            <p className="mt-0.5 text-[11px] font-bold text-ink">{block.title}</p>

            <p
                aria-live="polite"
                className="mt-1 rounded-lg bg-canvas/60 px-2.5 py-1.5 text-[10.5px] leading-relaxed font-medium text-ink/75"
            >
                <Inline text={current.text} />
            </p>

            {pending ? (
                <div className="mt-1.5">
                    {pending.feedback && (
                        <p className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5 text-[10px] leading-relaxed font-medium text-ink/60">
                            <Inline text={pending.feedback} />
                        </p>
                    )}

                    <button
                        type="button"
                        onClick={() => advance(pending)}
                        className="mt-1 inline-flex h-7 items-center rounded-lg bg-red px-2.5 text-[9.5px] font-bold text-white"
                    >
                        {pending.next ? 'Lanjut' : 'Lihat ringkasan'}
                    </button>
                </div>
            ) : (
                <div className="mt-1.5 grid gap-1">
                    {(current.choices ?? []).map((choice, index) => (
                        <button
                            key={`${current.id}-choice-${index}`}
                            type="button"
                            onClick={() => choose(choice)}
                            className="flex w-full items-start gap-2 rounded-lg border border-rule bg-canvas/40 px-2.5 py-1.5 text-left text-[10.5px] font-medium text-ink/80 transition-colors hover:border-red/40 hover:bg-canvas/70"
                        >
                            <span
                                aria-hidden="true"
                                className="mt-0.5 flex size-4 shrink-0 items-center justify-center rounded-full bg-red/10 text-[8.5px] font-bold text-red"
                            >
                                {index + 1}
                            </span>
                            <span>{choice.text}</span>
                        </button>
                    ))}
                </div>
            )}

            <p className="mt-1.5 text-[9px] font-medium text-ink/35">
                {result
                    ? `Terbaik ${result.score}% · ${result.attempts}× dimainkan`
                    : 'Setiap pilihan punya konsekuensi — baca umpan baliknya.'}
            </p>
        </section>
    );
}
