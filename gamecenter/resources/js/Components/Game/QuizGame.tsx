import { useEffect } from 'react';

import type { GameQuestion, GameResponse } from '@/lib/game/game-engine';
import { cn } from '@/lib/utils';

interface QuizGameProps {
    question: GameQuestion;
    response: GameResponse | null;
    onChange: (response: GameResponse) => void;
    disabled: boolean;
    revealed: boolean;
}

export default function QuizGame({
    question,
    response,
    onChange,
    disabled,
    revealed,
}: QuizGameProps) {
    const isMultiple = question.type === 'multiple_answer';

    useEffect(() => {
        if (disabled || revealed || question.type === 'essay') {
            return;
        }

        function handleKey(event: KeyboardEvent) {
            if (
                event.ctrlKey ||
                event.metaKey ||
                event.altKey ||
                event.target instanceof HTMLTextAreaElement ||
                event.target instanceof HTMLInputElement
            ) {
                return;
            }

            const index = Number(event.key) - 1;
            const option = question.options[index];

            if (!option) {
                return;
            }

            event.preventDefault();
            selectOption(option.id);
        }

        function selectOption(optionId: number) {
            if (isMultiple) {
                const selected = new Set(response?.option_ids ?? []);

                if (selected.has(optionId)) {
                    selected.delete(optionId);
                } else {
                    selected.add(optionId);
                }

                onChange({ option_ids: Array.from(selected) });
            } else {
                onChange({ option_id: optionId });
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    });

    if (question.type === 'essay') {
        return (
            <div className="space-y-3">
                <textarea
                    value={response?.text ?? ''}
                    onChange={(event) => onChange({ text: event.target.value })}
                    readOnly={disabled || revealed}
                    rows={7}
                    placeholder="Tulis jawabanmu di sini…"
                    className="w-full resize-y rounded-2xl border border-rule bg-canvas/50 px-4 py-3 text-[13px] leading-relaxed text-ink outline-none transition-colors placeholder:text-ink/30 focus:border-red focus:bg-surface disabled:opacity-80"
                />

                <div className="flex items-center justify-between gap-3 text-[10px] font-semibold text-ink/40">
                    <span>Jawaban uraian disimpan untuk penilaian lanjutan.</span>
                    <span className="tabular-nums">
                        {(response?.text ?? '').trim().length} karakter
                    </span>
                </div>

                {question.rubric && question.rubric.length > 0 && (
                    <div className="rounded-2xl border border-rule bg-canvas/50 p-4">
                        <p className="text-[9px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                            Panduan penilaian
                        </p>
                        <ul className="mt-2 grid gap-1.5">
                            {question.rubric.map((item) => (
                                <li
                                    key={item.point}
                                    className="flex items-start gap-2 text-[11.5px] leading-relaxed text-ink/60"
                                >
                                    <span className="mt-1.5 h-1 w-1 shrink-0 rounded-full bg-red" />
                                    <span className="flex-1">{item.point}</span>
                                    <span className="shrink-0 font-bold text-ink/35 tabular-nums">
                                        {item.weight}%
                                    </span>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        );
    }

    return (
        <div className="grid gap-2">
            {isMultiple && (
                <p className="text-[10.5px] font-semibold text-ink/45">
                    Pilih semua jawaban yang benar.
                </p>
            )}

            {question.options.map((option, index) => {
                const selected = isMultiple
                    ? (response?.option_ids ?? []).includes(option.id)
                    : response?.option_id === option.id;
                const isCorrectOption = option.is_correct;

                return (
                    <button
                        key={option.id}
                        type="button"
                        disabled={disabled || revealed}
                        onClick={() => {
                            if (disabled || revealed) {
                                return;
                            }

                            if (isMultiple) {
                                const selectedIds = new Set(
                                    response?.option_ids ?? [],
                                );

                                if (selectedIds.has(option.id)) {
                                    selectedIds.delete(option.id);
                                } else {
                                    selectedIds.add(option.id);
                                }

                                onChange({
                                    option_ids: Array.from(selectedIds),
                                });
                            } else {
                                onChange({ option_id: option.id });
                            }
                        }}
                        aria-pressed={selected}
                        className={cn(
                            'group flex items-start gap-3 rounded-2xl border px-3.5 py-3 text-left transition-all sm:px-4',
                            'disabled:cursor-default',
                            !revealed &&
                                selected &&
                                'border-red bg-red-tint shadow-[0_0_0_1px_var(--color-red)]',
                            !revealed &&
                                !selected &&
                                'border-rule bg-surface hover:border-red/35 hover:bg-red-tint/30',
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
                                'border-rule bg-surface opacity-55',
                        )}
                    >
                        <span
                            className={cn(
                                'grid h-7 w-7 shrink-0 place-items-center rounded-lg text-[10.5px] font-black ring-1 transition-colors',
                                selected
                                    ? 'bg-red text-white ring-red'
                                    : 'bg-canvas text-ink/45 ring-rule',
                                revealed &&
                                    isCorrectOption &&
                                    'bg-red text-white ring-red',
                                revealed &&
                                    selected &&
                                    !isCorrectOption &&
                                    'bg-red text-white ring-red',
                            )}
                        >
                            {revealed && isCorrectOption
                                ? '✓'
                                : revealed && selected && !isCorrectOption
                                  ? '×'
                                  : (option.label ?? index + 1)}
                        </span>

                        <span className="min-w-0 flex-1 pt-0.5 text-[13px] leading-snug font-semibold text-ink/75">
                            {option.text}
                        </span>

                        <kbd
                            className={cn(
                                'mt-0.5 hidden h-5 w-5 shrink-0 place-items-center rounded-md border border-rule bg-canvas text-[9px] font-bold text-ink/30 sm:grid',
                                selected && 'border-red/20 bg-white/60 text-red',
                            )}
                        >
                            {index + 1}
                        </kbd>
                    </button>
                );
            })}
        </div>
    );
}
