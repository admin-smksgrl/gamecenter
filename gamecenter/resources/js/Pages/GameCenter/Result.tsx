import { Head, Link } from '@inertiajs/react';

import AppLayout from '@/Layouts/AppLayout';
import {
    DIFFICULTY_META,
    cn,
    formatDateId,
    formatNumber,
    subjectTheme,
} from '@/lib/utils';

interface ResultSession {
    id: number;
    mode: string;
    score: number;
    correct_answers: number;
    total_questions: number;
    duration_seconds: number;
    completed_at: string | null;
}

interface ResultContext {
    assessment_title: string | null;
    chapter_title: string | null;
    chapter_code: string | null;
    subject_name: string | null;
    subject_icon: string | null;
    subject_color: string | null;
    class_name: string | null;
    level_name: string | null;
    level_theme: string;
}

interface ResultSummary {
    total_score: number;
    max_score: number;
    correct_count: number;
    wrong_count: number;
    unanswered_count: number;
    xp_earned: number;
    coins_earned: number;
    is_passed: boolean;
}

interface AnswerReview {
    id: number;
    question: string | null;
    type: string | null;
    type_label: string | null;
    is_correct: boolean;
    ungraded: boolean;
    points_earned: number;
    user_answer: unknown;
    expected: string | null;
    explanation: string | null;
    time_spent: number;
}

interface Props {
    session: ResultSession;
    context: ResultContext;
    summary: ResultSummary;
    answers: AnswerReview[];
    [key: string]: unknown;
}

function formatDuration(seconds: number): string {
    const minutes = Math.floor(seconds / 60);
    const rest = seconds % 60;

    return `${minutes} menit ${String(rest).padStart(2, '0')} detik`;
}

function answerText(value: unknown): string | null {
    if (value === null || value === undefined) {
        return null;
    }

    if (typeof value === 'string') {
        return value.trim() === '' ? null : value;
    }

    if (typeof value === 'number' || typeof value === 'boolean') {
        return String(value);
    }

    if (Array.isArray(value)) {
        const parts = value
            .map((item) => answerText(item))
            .filter((item): item is string => item !== null);

        return parts.length > 0 ? parts.join(' · ') : null;
    }

    if (typeof value === 'object') {
        const entries = Object.values(value as Record<string, unknown>)
            .map((item) => answerText(item))
            .filter((item): item is string => item !== null);

        return entries.length > 0 ? entries.join(' · ') : null;
    }

    return null;
}

function StatTile({
    label,
    value,
    tone,
}: {
    label: string;
    value: string;
    tone?: 'good' | 'bad' | 'neutral';
}) {
    return (
        <div className="rounded-2xl border border-rule bg-surface px-3 py-2.5 text-center">
            <p
                className={cn(
                    'font-serif text-[21px] leading-none font-semibold tabular-nums',
                    tone === 'good' && 'text-red',
                    tone === 'bad' && 'text-red',
                    (!tone || tone === 'neutral') && 'text-ink',
                )}
            >
                {value}
            </p>
            <p className="mt-1 text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                {label}
            </p>
        </div>
    );
}

export default function Result({
    session,
    context,
    summary,
    answers,
}: Props) {
    const theme = subjectTheme(context.subject_color);
    const passed = summary.is_passed;
    const percent =
        summary.max_score > 0
            ? Math.min(
                  100,
                  Math.round((summary.total_score / summary.max_score) * 100),
              )
            : session.score;

    return (
        <>
            <Head title="Hasil Sesi" />

            <AppLayout levelTheme={context.level_theme}>
                <div className="scroll-quiet min-h-0 flex-1 overflow-y-auto">
                    <div className="mx-auto w-full max-w-[860px] px-3 pt-4 pb-10 sm:px-5 sm:pt-6">
                        {/* ── Header hasil ───────────────────────── */}
                        <header className="relative overflow-hidden rounded-[26px] border border-rule bg-surface shadow-card">
                            <span
                                aria-hidden
                                className="level-orb pointer-events-none absolute -top-20 -right-12 h-48 w-48 rounded-full blur-2xl"
                            />

                            <div className="flex flex-wrap items-center gap-3 border-b border-rule px-4 py-3.5 sm:px-6">
                                <span
                                    className={cn(
                                        'grid h-11 w-11 shrink-0 place-items-center rounded-xl text-[20px]',
                                        theme.tile,
                                    )}
                                >
                                    {context.subject_icon ?? '📘'}
                                </span>
                                <div className="min-w-0 flex-1">
                                    <p className="text-[8.5px] font-bold tracking-[0.16em] text-ink/35 uppercase">
                                        {context.level_name ?? 'Ruang belajar'}
                                        {context.class_name
                                            ? ` · ${context.class_name}`
                                            : ''}
                                    </p>
                                    <h1 className="display mt-0.5 truncate text-[20px] leading-tight text-ink">
                                        {context.chapter_title ??
                                            context.assessment_title ??
                                            'Hasil sesi'}
                                    </h1>
                                    <p className="mt-0.5 text-[10px] font-semibold text-ink/40">
                                        {context.subject_name ?? 'Mapel'} ·{' '}
                                        {DIFFICULTY_META[session.mode]?.label ??
                                            session.mode}{' '}
                                        ·{' '}
                                        {formatDateId(session.completed_at)}
                                    </p>
                                </div>

                                <span
                                    className={cn(
                                        'shrink-0 rounded-full px-2.5 py-1 text-[9px] font-bold',
                                        passed
                                            ? 'bg-red text-white'
                                            : 'bg-canvas text-ink/55 ring-1 ring-rule',
                                    )}
                                >
                                    {passed ? '✓ Lulus' : 'Belum lulus'}
                                </span>
                            </div>

                            <div className="flex flex-wrap items-center gap-5 px-4 py-5 sm:px-6">
                                <div className="flex items-center gap-4">
                                    <div className="relative grid h-[92px] w-[92px] place-items-center">
                                        <svg
                                            aria-hidden
                                            viewBox="0 0 100 100"
                                            className="absolute inset-0 -rotate-90"
                                        >
                                            <circle
                                                cx="50"
                                                cy="50"
                                                r="44"
                                                fill="none"
                                                strokeWidth="8"
                                                className="stroke-ink/[0.07]"
                                            />
                                            <circle
                                                cx="50"
                                                cy="50"
                                                r="44"
                                                fill="none"
                                                strokeWidth="8"
                                                strokeLinecap="round"
                                                strokeDasharray={`${percent * 2.764} 276.4`}
                                                className={cn(
                                                    passed
                                                        ? 'stroke-red'
                                                        : 'stroke-ink/30',
                                                )}
                                            />
                                        </svg>
                                        <div className="text-center">
                                            <p className="font-serif text-[30px] leading-none font-semibold text-ink tabular-nums">
                                                {session.score}
                                            </p>
                                            <p className="text-[8px] font-bold tracking-[0.12em] text-ink/30 uppercase">
                                                Skor
                                            </p>
                                        </div>
                                    </div>

                                    <div className="min-w-0">
                                        <p className="display text-[19px] leading-tight text-ink">
                                            {passed
                                                ? 'Kerja bagus! 🎉'
                                                : 'Hampir sampai! 💪'}
                                        </p>
                                        <p className="mt-1 max-w-[260px] text-[10.5px] font-medium text-ink/45">
                                            {passed
                                                ? 'Kamu menjawab sebagian besar soal dengan benar. Lanjutkan ke tantangan berikutnya.'
                                                : 'Baca ulang materi dan coba lagi. Setiap percobaan menambah pengalaman.'}
                                        </p>
                                        <p className="mt-1.5 text-[9.5px] font-semibold text-ink/35">
                                            {formatDuration(
                                                session.duration_seconds,
                                            )}{' '}
                                            · {answers.length} soal
                                        </p>
                                    </div>
                                </div>

                                <div className="ml-auto grid grid-cols-2 gap-1.5 sm:grid-cols-4">
                                    <StatTile
                                        label="Benar"
                                        value={String(summary.correct_count)}
                                        tone="good"
                                    />
                                    <StatTile
                                        label="Salah"
                                        value={String(summary.wrong_count)}
                                        tone="bad"
                                    />
                                    <StatTile
                                        label="Kosong"
                                        value={String(
                                            summary.unanswered_count,
                                        )}
                                    />
                                    <StatTile
                                        label="XP"
                                        value={`+${formatNumber(
                                            summary.xp_earned,
                                        )}`}
                                    />
                                </div>
                            </div>

                            <div className="flex flex-wrap items-center gap-2 border-t border-rule bg-canvas/40 px-4 py-3 sm:px-6">
                                <span className="inline-flex items-center gap-1.5 rounded-full bg-surface px-2.5 py-1 text-[9.5px] font-bold text-ink/55 ring-1 ring-rule">
                                    <span aria-hidden>🪙</span>
                                    +{formatNumber(summary.coins_earned)} koin
                                </span>
                                <span className="inline-flex items-center gap-1.5 rounded-full bg-surface px-2.5 py-1 text-[9.5px] font-bold text-ink/55 ring-1 ring-rule">
                                    <span aria-hidden>⭐</span>
                                    {summary.total_score}/{summary.max_score}{' '}
                                    poin
                                </span>
                                <span className="inline-flex items-center gap-1.5 rounded-full bg-surface px-2.5 py-1 text-[9.5px] font-bold text-ink/55 ring-1 ring-rule">
                                    <span aria-hidden>📚</span>
                                    {session.correct_answers}/
                                    {session.total_questions} jawaban benar
                                </span>

                                <div className="ml-auto flex flex-wrap items-center gap-1.5">
                                    <Link
                                        href="/progres"
                                        className="inline-flex h-8 items-center rounded-lg bg-red px-3.5 text-[10px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                    >
                                        Lihat progres
                                    </Link>
                                    <Link
                                        href="/"
                                        className="inline-flex h-8 items-center rounded-lg bg-surface px-3.5 text-[10px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-red"
                                    >
                                        Jelajah materi
                                    </Link>
                                </div>
                            </div>
                        </header>

                        {/* ── Pembahasan jawaban ─────────────────── */}
                        <section className="mt-4">
                            <div className="mb-2 flex items-end justify-between gap-3">
                                <div>
                                    <p className="text-[8.5px] font-bold tracking-[0.16em] text-red uppercase">
                                        Pembahasan
                                    </p>
                                    <h2 className="display mt-0.5 text-[18px] leading-tight text-ink">
                                        Tinjau jawabanmu
                                    </h2>
                                </div>
                                <p className="text-[9.5px] font-semibold text-ink/35">
                                    {answers.filter((answer) => answer.is_correct)
                                        .length}{' '}
                                    benar dari {answers.length} soal
                                </p>
                            </div>

                            {answers.length === 0 ? (
                                <p className="rounded-2xl border border-dashed border-rule bg-surface/60 px-4 py-6 text-center text-[10.5px] font-medium text-ink/40">
                                    Detail jawaban tidak tersedia untuk sesi
                                    ini.
                                </p>
                            ) : (
                                <ul className="grid gap-2">
                                    {answers.map((answer, index) => {
                                        const userAnswer = answerText(
                                            answer.user_answer,
                                        );

                                        return (
                                            <li
                                                key={answer.id}
                                                className={cn(
                                                    'rounded-2xl border bg-surface px-3.5 py-3 shadow-card',
                                                    answer.ungraded
                                                        ? 'border-rule'
                                                        : answer.is_correct
                                                          ? 'border-red/30'
                                                          : 'border-rule',
                                                )}
                                            >
                                                <div className="flex items-start gap-2.5">
                                                    <span
                                                        className={cn(
                                                            'grid h-6 w-6 shrink-0 place-items-center rounded-lg text-[10px] font-bold',
                                                            answer.ungraded
                                                                ? 'bg-ink/[0.06] text-ink/60'
                                                                : answer.is_correct
                                                                  ? 'bg-red text-white'
                                                                  : 'bg-canvas text-ink/45 ring-1 ring-rule',
                                                        )}
                                                    >
                                                        {answer.ungraded
                                                            ? '…'
                                                            : answer.is_correct
                                                              ? '✓'
                                                              : '✕'}
                                                    </span>

                                                    <div className="min-w-0 flex-1">
                                                        <div className="flex flex-wrap items-center gap-x-2 gap-y-0.5">
                                                            <span className="text-[8px] font-bold tracking-[0.12em] text-ink/30 uppercase">
                                                                Soal{' '}
                                                                {index + 1} ·{' '}
                                                                {answer.type_label ??
                                                                    answer.type ??
                                                                    'Soal'}
                                                            </span>
                                                            <span className="text-[8.5px] font-bold text-ink/35 tabular-nums">
                                                                {
                                                                    answer.points_earned
                                                                }{' '}
                                                                poin
                                                            </span>
                                                            {answer.ungraded && (
                                                                <span className="rounded-full bg-ink/[0.06] px-1.5 py-0.5 text-[8px] font-bold text-ink/55">
                                                                    Menunggu
                                                                    penilaian
                                                                </span>
                                                            )}
                                                        </div>

                                                        <p className="mt-1 text-[12px] leading-snug font-bold text-ink">
                                                            {answer.question ??
                                                                'Soal'}
                                                        </p>

                                                        <div className="mt-1.5 grid gap-1 text-[10px] font-medium">
                                                            <p className="text-ink/45">
                                                                <span className="font-bold text-ink/60">
                                                                    Jawabanmu:
                                                                </span>{' '}
                                                                {userAnswer ??
                                                                    'Tidak dijawab'}
                                                            </p>

                                                            {!answer.is_correct &&
                                                                answer.expected && (
                                                                    <p className="text-red">
                                                                        <span className="font-bold">
                                                                            Kunci:
                                                                        </span>{' '}
                                                                        {
                                                                            answer.expected
                                                                        }
                                                                    </p>
                                                                )}
                                                        </div>

                                                        {answer.explanation && (
                                                            <p className="mt-1.5 rounded-lg bg-canvas/70 px-2.5 py-1.5 text-[9.5px] leading-relaxed font-medium text-ink/50">
                                                                {
                                                                    answer.explanation
                                                                }
                                                            </p>
                                                        )}
                                                    </div>

                                                    <span className="shrink-0 text-[8.5px] font-semibold text-ink/25 tabular-nums">
                                                        {answer.time_spent}s
                                                    </span>
                                                </div>
                                            </li>
                                        );
                                    })}
                                </ul>
                            )}
                        </section>
                    </div>
                </div>
            </AppLayout>
        </>
    );
}
