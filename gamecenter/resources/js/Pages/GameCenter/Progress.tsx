import { Head, Link } from '@inertiajs/react';
import type { ReactNode } from 'react';

import AppLayout from '@/Layouts/AppLayout';
import {
    DIFFICULTY_META,
    cn,
    formatDateId,
    formatNumber,
    subjectTheme,
} from '@/lib/utils';

interface ProgressUser {
    name: string;
    username: string;
    xp: number;
    coins: number;
    level: number;
    level_title: string;
    streak_days: number;
    class_name: string | null;
    education_level: string | null;
    level_theme: string;
    level_progress: {
        percent: number;
        xp_to_next: number | null;
    };
}

interface ProgressStats {
    sessions: number;
    completed_chapters: number;
    materials_read: number;
    total_minutes: number;
    average_score: number;
    best_score: number;
    achievements_unlocked: number;
    achievements_total: number;
}

interface ActivityDay {
    date: string;
    label: string;
    sessions: number;
    score: number;
}

interface ChapterProgress {
    chapter_id: number;
    chapter_title: string | null;
    chapter_code: string | null;
    subject_name: string | null;
    subject_icon: string | null;
    subject_color: string | null;
    class_name: string | null;
    level_name: string | null;
    level_slug: string | null;
    level_theme: string;
    status: string;
    status_label: string;
    best_score: number;
    attempts: number;
    materials_read: number;
    total_time_spent: number;
    last_accessed_at: string | null;
    assessment_id: number | null;
}

interface SessionHistory {
    id: number;
    assessment_title: string | null;
    chapter_title: string | null;
    subject_name: string | null;
    subject_icon: string | null;
    subject_color: string | null;
    mode: string;
    score: number;
    correct_answers: number;
    total_questions: number;
    duration_seconds: number;
    xp_earned: number;
    coins_earned: number;
    is_passed: boolean;
    completed_at: string | null;
    result_url: string;
}

interface AchievementItem {
    id: number;
    slug: string;
    title: string;
    description: string;
    icon: string;
    category: string;
    requirement_type: string;
    requirement_value: number;
    xp_reward: number;
    coin_reward: number;
    unlocked: boolean;
    unlocked_at: string | null;
}

interface Props {
    user: ProgressUser;
    stats: ProgressStats;
    activity: ActivityDay[];
    progress: ChapterProgress[];
    sessions: SessionHistory[];
    achievements: AchievementItem[];
    [key: string]: unknown;
}

const STATUS_CLASS: Record<string, string> = {
    completed: 'bg-red text-white',
    in_progress: 'bg-red/10 text-red',
    not_started: 'bg-ink/5 text-ink/45',
};

function formatMinutes(minutes: number): string {
    if (minutes < 60) {
        return `${minutes} mnt`;
    }

    const hours = Math.floor(minutes / 60);
    const rest = minutes % 60;

    return rest === 0 ? `${hours} jam` : `${hours}j ${rest}m`;
}

function formatDuration(seconds: number): string {
    const minutes = Math.floor(seconds / 60);
    const rest = seconds % 60;

    return `${minutes}:${String(rest).padStart(2, '0')}`;
}

function StatCard({
    label,
    value,
    hint,
    accent,
}: {
    label: string;
    value: string;
    hint?: string;
    accent?: boolean;
}) {
    return (
        <div
            className={cn(
                'rounded-2xl border px-3.5 py-3',
                accent
                    ? 'border-red/20 bg-red-tint/60'
                    : 'border-rule bg-surface',
            )}
        >
            <p className="text-[8.5px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                {label}
            </p>
            <p
                className={cn(
                    'mt-1 font-serif text-[24px] leading-none font-semibold tabular-nums',
                    accent ? 'text-red' : 'text-ink',
                )}
            >
                {value}
            </p>
            {hint && (
                <p className="mt-1 text-[9px] font-medium text-ink/35">
                    {hint}
                </p>
            )}
        </div>
    );
}

function SectionTitle({
    eyebrow,
    title,
    action,
}: {
    eyebrow: string;
    title: string;
    action?: ReactNode;
}) {
    return (
        <div className="mb-2 flex items-end justify-between gap-3">
            <div className="min-w-0">
                <p className="text-[8.5px] font-bold tracking-[0.16em] text-red uppercase">
                    {eyebrow}
                </p>
                <h2 className="display mt-0.5 text-[18px] leading-tight text-ink">
                    {title}
                </h2>
            </div>
            {action}
        </div>
    );
}

export default function Progress({
    user,
    stats,
    activity,
    progress,
    sessions,
    achievements,
}: Props) {
    const maxActivity = Math.max(1, ...activity.map((day) => day.sessions));
    const unlocked = achievements.filter((item) => item.unlocked);

    return (
        <>
            <Head title="Progres & Lencana" />

            <AppLayout levelTheme={user.level_theme}>
                <div className="scroll-quiet min-h-0 flex-1 overflow-y-auto">
                    <div className="mx-auto w-full max-w-[1080px] px-3 pt-4 pb-10 sm:px-5 sm:pt-6">
                        {/* ── Header ─────────────────────────────── */}
                        <header className="overflow-hidden rounded-[24px] border border-rule bg-surface shadow-card">
                            <div className="relative flex flex-wrap items-center gap-4 px-4 py-5 sm:px-6">
                                <span
                                    aria-hidden
                                    className="level-orb pointer-events-none absolute -top-16 -right-10 h-40 w-40 rounded-full blur-2xl"
                                />

                                <div className="grid h-14 w-14 shrink-0 place-items-center rounded-2xl bg-red text-[22px] font-bold text-white shadow-fab">
                                    {user.name.charAt(0).toUpperCase()}
                                </div>

                                <div className="min-w-0 flex-1">
                                    <p className="text-[9px] font-bold tracking-[0.16em] text-ink/35 uppercase">
                                        {user.education_level ?? 'Ruang belajar'}
                                        {user.class_name
                                            ? ` · ${user.class_name}`
                                            : ''}
                                    </p>
                                    <h1 className="display mt-0.5 truncate text-[24px] leading-tight text-ink">
                                        {user.name}
                                    </h1>
                                    <p className="mt-0.5 text-[10.5px] font-semibold text-ink/40">
                                        Level {user.level} · {user.level_title}
                                    </p>
                                </div>

                                <div className="flex shrink-0 items-center gap-2">
                                    <div className="rounded-xl border border-rule bg-canvas px-3 py-2 text-center">
                                        <p className="text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                                            XP
                                        </p>
                                        <p className="mt-0.5 font-serif text-[18px] leading-none font-semibold text-ink tabular-nums">
                                            {formatNumber(user.xp)}
                                        </p>
                                    </div>
                                    <div className="rounded-xl border border-rule bg-canvas px-3 py-2 text-center">
                                        <p className="text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                                            Koin
                                        </p>
                                        <p className="mt-0.5 font-serif text-[18px] leading-none font-semibold text-ink tabular-nums">
                                            {formatNumber(user.coins)}
                                        </p>
                                    </div>
                                    <div className="rounded-xl border border-rule bg-canvas px-3 py-2 text-center">
                                        <p className="text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                                            Streak
                                        </p>
                                        <p className="mt-0.5 font-serif text-[18px] leading-none font-semibold text-ink tabular-nums">
                                            {user.streak_days}
                                        </p>
                                    </div>
                                </div>

                                <div className="w-full">
                                    <div className="flex items-center justify-between text-[9.5px] font-bold text-ink/40">
                                        <span>Progres level</span>
                                        <span className="text-red">
                                            {user.level_progress.percent}%
                                        </span>
                                    </div>
                                    <div className="mt-1 h-2 overflow-hidden rounded-full bg-ink/[0.07]">
                                        <div
                                            className="h-full rounded-full bg-red transition-[width] duration-500"
                                            style={{
                                                width: `${user.level_progress.percent}%`,
                                            }}
                                        />
                                    </div>
                                    <p className="mt-1 text-[9.5px] font-medium text-ink/35">
                                        {user.level_progress.xp_to_next === null
                                            ? 'Level tertinggi tercapai. Pertahankan!'
                                            : `${formatNumber(
                                                  user.level_progress.xp_to_next,
                                              )} XP lagi menuju level ${
                                                  user.level + 1
                                              }`}
                                    </p>
                                </div>
                            </div>
                        </header>

                        {/* ── Statistik ──────────────────────────── */}
                        <section
                            aria-label="Statistik belajar"
                            className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-6"
                        >
                            <StatCard
                                label="Sesi selesai"
                                value={formatNumber(stats.sessions)}
                                accent
                            />
                            <StatCard
                                label="Bab tuntas"
                                value={formatNumber(stats.completed_chapters)}
                            />
                            <StatCard
                                label="Materi dibaca"
                                value={formatNumber(stats.materials_read)}
                            />
                            <StatCard
                                label="Waktu belajar"
                                value={formatMinutes(stats.total_minutes)}
                            />
                            <StatCard
                                label="Rata-rata"
                                value={String(stats.average_score)}
                                hint={`Terbaik ${stats.best_score}`}
                            />
                            <StatCard
                                label="Lencana"
                                value={`${stats.achievements_unlocked}/${stats.achievements_total}`}
                            />
                        </section>

                        <div className="mt-4 grid gap-4 lg:grid-cols-[1.15fr_0.85fr]">
                            <div className="min-w-0">
                                {/* ── Aktivitas mingguan ─────────── */}
                                <section className="rounded-[22px] border border-rule bg-surface p-4 shadow-card">
                                    <SectionTitle
                                        eyebrow="7 hari terakhir"
                                        title="Ritme belajarmu"
                                    />

                                    <div className="mt-3 flex items-end justify-between gap-1.5">
                                        {activity.map((day) => {
                                            const height =
                                                day.sessions === 0
                                                    ? 6
                                                    : Math.max(
                                                          14,
                                                          Math.round(
                                                              (day.sessions /
                                                                  maxActivity) *
                                                                  100,
                                                          ),
                                                      );

                                            return (
                                                <div
                                                    key={day.date}
                                                    className="flex min-w-0 flex-1 flex-col items-center gap-1"
                                                >
                                                    <span className="text-[8.5px] font-bold text-ink/35 tabular-nums">
                                                        {day.sessions > 0
                                                            ? day.sessions
                                                            : ''}
                                                    </span>
                                                    <div className="flex h-[92px] w-full items-end">
                                                        <div
                                                            className={cn(
                                                                'w-full rounded-t-lg transition-[height] duration-500',
                                                                day.sessions > 0
                                                                    ? 'bg-red'
                                                                    : 'bg-ink/10',
                                                            )}
                                                            style={{
                                                                height: `${height}%`,
                                                            }}
                                                            title={`${day.sessions} sesi · rata-rata ${day.score}`}
                                                        />
                                                    </div>
                                                    <span className="text-[8.5px] font-semibold text-ink/40">
                                                        {day.label}
                                                    </span>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </section>

                                {/* ── Progres bab ────────────────── */}
                                <section className="mt-4">
                                    <SectionTitle
                                        eyebrow="Perjalanan materi"
                                        title="Progres per bab"
                                        action={
                                            <Link
                                                href="/"
                                                className="shrink-0 text-[9.5px] font-bold text-red transition-colors hover:text-red-deep"
                                            >
                                                Jelajah materi
                                            </Link>
                                        }
                                    />

                                    {progress.length === 0 ? (
                                        <div className="rounded-2xl border border-dashed border-rule bg-surface/60 px-4 py-8 text-center">
                                            <p className="text-[22px]">🌱</p>
                                            <p className="mt-1.5 text-[12px] font-bold text-ink/60">
                                                Belum ada bab yang dimulai
                                            </p>
                                            <p className="mt-0.5 text-[10.5px] font-medium text-ink/35">
                                                Pilih satu materi dan mainkan
                                                sesi pertamamu.
                                            </p>
                                            <Link
                                                href="/"
                                                className="mt-3 inline-flex h-8 items-center rounded-lg bg-red px-3.5 text-[10.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                            >
                                                Mulai belajar
                                            </Link>
                                        </div>
                                    ) : (
                                        <ul className="grid gap-2">
                                            {progress.map((row) => {
                                                const theme = subjectTheme(
                                                    row.subject_color,
                                                );

                                                return (
                                                    <li
                                                        key={row.chapter_id}
                                                        className={cn(
                                                            'flex flex-wrap items-center gap-3 rounded-2xl border bg-surface px-3 py-2.5 shadow-card',
                                                            theme.border,
                                                        )}
                                                    >
                                                        <span
                                                            className={cn(
                                                                'grid h-9 w-9 shrink-0 place-items-center rounded-xl text-[16px]',
                                                                theme.tile,
                                                            )}
                                                        >
                                                            {row.subject_icon ??
                                                                '📘'}
                                                        </span>

                                                        <div className="min-w-0 flex-1">
                                                            <p className="truncate text-[12px] font-bold text-ink">
                                                                {row.chapter_title ??
                                                                    'Bab'}
                                                            </p>
                                                            <p className="mt-0.5 flex flex-wrap items-center gap-x-1.5 text-[9px] font-semibold text-ink/40">
                                                                <span className="truncate">
                                                                    {row.subject_name ??
                                                                        'Mapel'}
                                                                </span>
                                                                <span className="text-ink/20">
                                                                    ·
                                                                </span>
                                                                <span>
                                                                    {row.materials_read}{' '}
                                                                    materi
                                                                </span>
                                                                <span className="text-ink/20">
                                                                    ·
                                                                </span>
                                                                <span>
                                                                    {row.attempts}x
                                                                    main
                                                                </span>
                                                            </p>
                                                        </div>

                                                        <div className="flex shrink-0 items-center gap-2">
                                                            <span className="text-right">
                                                                <span className="block font-serif text-[17px] leading-none font-semibold text-ink tabular-nums">
                                                                    {
                                                                        row.best_score
                                                                    }
                                                                </span>
                                                                <span className="text-[8px] font-bold tracking-[0.1em] text-ink/30 uppercase">
                                                                    Skor
                                                                </span>
                                                            </span>
                                                            <span
                                                                className={cn(
                                                                    'rounded-full px-2 py-0.5 text-[8.5px] font-bold',
                                                                    STATUS_CLASS[
                                                                        row
                                                                            .status
                                                                    ] ??
                                                                        'bg-ink/5 text-ink/45',
                                                                )}
                                                            >
                                                                {
                                                                    row.status_label
                                                                }
                                                            </span>
                                                            {row.assessment_id ? (
                                                                <Link
                                                                    href={`/main/${row.assessment_id}`}
                                                                    className="inline-flex h-8 items-center rounded-lg bg-red px-3 text-[10px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                                                >
                                                                    {row.status ===
                                                                    'completed'
                                                                        ? 'Ulangi'
                                                                        : 'Lanjut'}
                                                                </Link>
                                                            ) : null}
                                                        </div>
                                                    </li>
                                                );
                                            })}
                                        </ul>
                                    )}
                                </section>

                                {/* ── Riwayat sesi ───────────────── */}
                                <section className="mt-4">
                                    <SectionTitle
                                        eyebrow="Jejak latihan"
                                        title="Sesi terakhir"
                                    />

                                    {sessions.length === 0 ? (
                                        <p className="rounded-2xl border border-dashed border-rule bg-surface/60 px-4 py-6 text-center text-[10.5px] font-medium text-ink/40">
                                            Riwayat sesi akan muncul setelah
                                            kamu menyelesaikan permainan.
                                        </p>
                                    ) : (
                                        <ul className="grid gap-1.5">
                                            {sessions.map((session) => {
                                                const theme = subjectTheme(
                                                    session.subject_color,
                                                );

                                                return (
                                                    <li key={session.id}>
                                                        <Link
                                                            href={
                                                                session.result_url
                                                            }
                                                            className="flex items-center gap-2.5 rounded-xl border border-rule bg-surface px-3 py-2 transition-all hover:-translate-y-0.5 hover:shadow-card"
                                                        >
                                                            <span
                                                                className={cn(
                                                                    'grid h-8 w-8 shrink-0 place-items-center rounded-lg text-[14px]',
                                                                    theme.tile,
                                                                )}
                                                            >
                                                                {session.subject_icon ??
                                                                    '📘'}
                                                            </span>

                                                            <span className="min-w-0 flex-1">
                                                                <span className="block truncate text-[11px] font-bold text-ink">
                                                                    {session.chapter_title ??
                                                                        session.assessment_title ??
                                                                        'Sesi'}
                                                                </span>
                                                                <span className="mt-0.5 flex flex-wrap items-center gap-x-1.5 text-[9px] font-semibold text-ink/35">
                                                                    <span>
                                                                        {formatDateId(
                                                                            session.completed_at,
                                                                        )}
                                                                    </span>
                                                                    <span className="text-ink/20">
                                                                        ·
                                                                    </span>
                                                                    <span>
                                                                        {DIFFICULTY_META[
                                                                            session
                                                                                .mode
                                                                        ]
                                                                            ?.label ??
                                                                            session.mode}
                                                                    </span>
                                                                    <span className="text-ink/20">
                                                                        ·
                                                                    </span>
                                                                    <span className="tabular-nums">
                                                                        {formatDuration(
                                                                            session.duration_seconds,
                                                                        )}
                                                                    </span>
                                                                </span>
                                                            </span>

                                                            <span className="shrink-0 text-right">
                                                                <span
                                                                    className={cn(
                                                                        'block font-serif text-[16px] leading-none font-semibold tabular-nums',
                                                                        session.is_passed
                                                                            ? 'text-red'
                                                                            : 'text-ink/70',
                                                                    )}
                                                                >
                                                                    {session.score}
                                                                </span>
                                                                <span className="text-[8px] font-bold text-ink/30 tabular-nums">
                                                                    +
                                                                    {
                                                                        session.xp_earned
                                                                    }{' '}
                                                                    XP
                                                                </span>
                                                            </span>
                                                        </Link>
                                                    </li>
                                                );
                                            })}
                                        </ul>
                                    )}
                                </section>
                            </div>

                            {/* ── Lencana ────────────────────────── */}
                            <section className="min-w-0">
                                <SectionTitle
                                    eyebrow={`${unlocked.length} dari ${achievements.length} terbuka`}
                                    title="Koleksi lencana"
                                />

                                <div className="grid grid-cols-2 gap-2">
                                    {achievements.map((achievement) => (
                                        <div
                                            key={achievement.id}
                                            className={cn(
                                                'relative flex flex-col items-start gap-1 rounded-2xl border px-3 py-3 transition-colors',
                                                achievement.unlocked
                                                    ? 'border-red/20 bg-red-tint/50'
                                                    : 'border-rule bg-surface/60',
                                            )}
                                        >
                                            <span
                                                className={cn(
                                                    'grid h-9 w-9 place-items-center rounded-xl text-[18px] ring-1',
                                                    achievement.unlocked
                                                        ? 'bg-surface ring-red/20'
                                                        : 'bg-canvas ring-rule grayscale',
                                                )}
                                            >
                                                {achievement.icon}
                                            </span>
                                            <p
                                                className={cn(
                                                    'mt-1 text-[11px] leading-tight font-bold',
                                                    achievement.unlocked
                                                        ? 'text-ink'
                                                        : 'text-ink/45',
                                                )}
                                            >
                                                {achievement.title}
                                            </p>
                                            <p className="text-[9px] leading-snug font-medium text-ink/35">
                                                {achievement.description}
                                            </p>
                                            <p className="mt-auto pt-1 text-[8.5px] font-bold tracking-[0.08em] text-ink/30 uppercase">
                                                {achievement.unlocked
                                                    ? `Terbuka ${formatDateId(
                                                          achievement.unlocked_at,
                                                      )}`
                                                    : `+${achievement.xp_reward} XP`}
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            </section>
                        </div>
                    </div>
                </div>
            </AppLayout>
        </>
    );
}
