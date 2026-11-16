import type { GameQuestion, GameResponse } from '@/lib/game/game-engine';
import { cn } from '@/lib/utils';

interface SimulationGameProps {
    question: GameQuestion;
    response: GameResponse | null;
    onChange: (response: GameResponse) => void;
    disabled: boolean;
    revealed: boolean;
}

const DECISION_LABELS = ['A', 'B', 'C', 'D', 'E', 'F'];

export default function SimulationGame({
    question,
    response,
    onChange,
    disabled,
    revealed,
}: SimulationGameProps) {
    if (question.options.length === 0) {
        return (
            <p className="rounded-2xl border border-rule bg-canvas/50 px-4 py-5 text-center text-[12px] font-semibold text-ink/45">
                Skenario ini belum memiliki pilihan keputusan.
            </p>
        );
    }

    return (
        <div className="space-y-3">
            <div className="flex items-center gap-2 rounded-xl border border-rule bg-canvas px-3 py-2 text-[10.5px] font-semibold text-ink/60">
                <span aria-hidden>🧭</span>
                Ambil satu keputusan terbaik untuk skenario di atas.
            </div>

            <div className="grid gap-2">
                {question.options.map((option, index) => {
                    const selected = response?.option_id === option.id;
                    const isCorrectOption = option.is_correct;

                    return (
                        <button
                            key={option.id}
                            type="button"
                            disabled={disabled || revealed}
                            onClick={() => onChange({ option_id: option.id })}
                            aria-pressed={selected}
                            className={cn(
                                'group flex items-stretch gap-3 overflow-hidden rounded-2xl border bg-surface text-left transition-all',
                                !revealed &&
                                    selected &&
                                    'border-red shadow-[0_0_0_1px_var(--color-red)]',
                                !revealed &&
                                    !selected &&
                                    'border-rule hover:border-red/35 hover:bg-red-tint/20',
                                revealed &&
                                    isCorrectOption &&
                                    'border-red/60 bg-red-tint',
                                revealed &&
                                    selected &&
                                    !isCorrectOption &&
                                    'border-red bg-red-tint',
                                revealed &&
                                    !selected &&
                                    !isCorrectOption &&
                                    'border-rule opacity-55',
                            )}
                        >
                            <span
                                className={cn(
                                    'grid w-11 shrink-0 place-items-center text-[13px] font-black',
                                    selected
                                        ? 'bg-red text-white'
                                        : 'bg-canvas text-ink/40',
                                    revealed &&
                                        isCorrectOption &&
                                        'bg-red text-white',
                                )}
                            >
                                {revealed && isCorrectOption
                                    ? '✓'
                                    : revealed && selected && !isCorrectOption
                                      ? '×'
                                      : DECISION_LABELS[index]}
                            </span>

                            <span className="min-w-0 flex-1 py-3 pr-3.5 text-[12.5px] leading-snug font-semibold text-ink/75">
                                {option.text}
                            </span>
                        </button>
                    );
                })}
            </div>
        </div>
    );
}
