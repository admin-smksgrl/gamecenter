import { Head, Link, usePage } from '@inertiajs/react';
import { useEffect, useMemo, useRef, useState } from 'react';

import DragDropGame from '@/Components/Game/DragDropGame';
import MatchGame from '@/Components/Game/MatchGame';
import MaterialViewer from '@/Components/Game/MaterialViewer';
import type { MaterialProp } from '@/Components/Game/MaterialViewer';
import QuizGame from '@/Components/Game/QuizGame';
import SimulationGame from '@/Components/Game/SimulationGame';
import AppLayout from '@/Layouts/AppLayout';
import {
    buildSessionAnswers,
    evaluateQuestion,
    hasResponse,
    initialOrder,
    isMatchingType,
    isOrderingType,
    summarizeGame,
} from '@/lib/game/game-engine';
import type {
    EvaluatedAnswer,
    GameQuestion,
    GameResponse,
    GameSummary,
} from '@/lib/game/game-engine';
import {
    coinsForXp,
    levelForXp,
    levelProgress,
    sessionBadges,
} from '@/lib/game/gamification';
import { offlineDb } from '@/lib/offline/offline-db';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { syncService } from '@/lib/offline/sync-service';
import {
    DIFFICULTY_META,
    cn,
    formatNumber,
    subjectTheme,
} from '@/lib/utils';
import type { PageProps } from '@/types';

type Difficulty = 'easy' | 'medium' | 'hard';

type PlayIdentity =
    | { mode: 'solo'; name: string; members: [] }
    | { mode: 'group'; name: string; members: string[] };

type Phase = 'intro' | 'playing' | 'finished';

type SaveState = 'idle' | 'queued' | 'guest' | 'error';

interface AssessmentProp {
    id: number;
    title: string;
    difficulty: Difficulty;
    duration: number;
    passing_score: number;
    question_count: number;
}

interface ContextProp {
    chapter_id: number;
    chapter_title: string;
    chapter_code: string | null;
    subject_name: string;
    subject_icon: string | null;
    subject_color: string | null;
    subject_group: string | null;
    class_name: string;
    level_name: string;
    level_theme: string;
}

interface ProgressProp {
    status: string;
    best_score: number;
    attempts: number;
    materials_read: number;
}

interface Props {
    assessment: AssessmentProp;
    context: ContextProp;
    questions: GameQuestion[];
    materials: MaterialProp[];
    progress: ProgressProp | null;
    [key: string]: unknown;
}

const PLAY_STORAGE_KEY = 'gamecenter.play-session';

function loadPlayIdentity(): PlayIdentity | null {
    if (typeof window === 'undefined') {
        return null;
    }

    try {
        const raw = window.localStorage.getItem(PLAY_STORAGE_KEY);

        if (!raw) {
            return null;
        }

        const data = JSON.parse(raw) as Partial<PlayIdentity>;

        if (
            data.mode === 'solo' &&
            typeof data.name === 'string' &&
            data.name.trim() !== ''
        ) {
            return { mode: 'solo', name: data.name.trim(), members: [] };
        }

        if (
            data.mode === 'group' &&
            typeof data.name === 'string' &&
            data.name.trim() !== '' &&
            Array.isArray(data.members)
        ) {
            const members = data.members
                .filter(
                    (member): member is string =>
                        typeof member === 'string' && member.trim() !== '',
                )
                .map((member) => member.trim());

            if (members.length >= 2) {
                return { mode: 'group', name: data.name.trim(), members };
            }
        }
    } catch {
        // Sesi bermain lama yang rusak diabaikan.
    }

    return null;
}

function formatClock(totalSeconds: number): string {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;

    return `${minutes}:${String(seconds).padStart(2, '0')}`;
}

function formatDuration(totalSeconds: number): string {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;

    if (minutes === 0) {
        return `${seconds} detik`;
    }

    return seconds > 0 ? `${minutes} m ${seconds} d` : `${minutes} menit`;
}

export default function Play({
    assessment,
    context,
    questions,
    materials,
    progress,
}: Props) {
    const { auth } = usePage<PageProps>().props;
    const user = auth.user;
    const [identity] = useState<PlayIdentity | null>(loadPlayIdentity);
    const [phase, setPhase] = useState<Phase>('intro');
    const [currentIndex, setCurrentIndex] = useState(0);
    const [answers, setAnswers] = useState<Record<number, EvaluatedAnswer>>({});
    const [drafts, setDrafts] = useState<Record<number, GameResponse>>({});
    const [startedAt, setStartedAt] = useState<string | null>(null);
    const [finishedAt, setFinishedAt] = useState<string | null>(null);
    const [now, setNow] = useState(() => Date.now());
    const [openHint, setOpenHint] = useState<number | null>(null);
    const [saveState, setSaveState] = useState<SaveState>('idle');

    const finishedGuardRef = useRef(false);
    const questionStartedAtRef = useRef(Date.now());

    const question = questions[currentIndex];
    const answered = question ? answers[question.id] : undefined;
    const revealed = Boolean(answered);
    const theme = subjectTheme(context.subject_color);
    const difficulty = DIFFICULTY_META[assessment.difficulty];
    const essayCount = questions.filter(
        (item) => item.type === 'essay',
    ).length;
    const gradedCount = questions.length - essayCount;
    const totalPoints = questions
        .filter((item) => item.type !== 'essay')
        .reduce((total, item) => total + item.points, 0);

    const draft = useMemo<GameResponse | null>(() => {
        if (!question) {
            return null;
        }

        const saved = drafts[question.id];

        if (saved) {
            return saved;
        }

        if (isOrderingType(question.type)) {
            return { order: initialOrder(question) };
        }

        return null;
    }, [drafts, question]);

    const elapsedSeconds = startedAt
        ? Math.max(0, Math.floor((now - Date.parse(startedAt)) / 1000))
        : 0;
    const remainingSeconds = Math.max(
        0,
        assessment.duration - elapsedSeconds,
    );
    const answeredCount = Object.keys(answers).length;

    const summary = useMemo<GameSummary | null>(() => {
        if (!startedAt || !finishedAt) {
            return null;
        }

        return summarizeGame(
            questions,
            answers,
            assessment.passing_score,
            startedAt,
            finishedAt,
        );
    }, [
        answers,
        assessment.passing_score,
        finishedAt,
        questions,
        startedAt,
    ]);

    useEffect(() => {
        const cache = async () => {
            try {
                const cachedAt = new Date().toISOString();

                await offlineDb.put('assessments', {
                    id: assessment.id,
                    chapter_id: context.chapter_id,
                    difficulty: assessment.difficulty,
                    duration: assessment.duration,
                    passing_score: assessment.passing_score,
                    cachedAt,
                });

                for (const item of questions) {
                    await offlineDb.put('questions', {
                        id: item.id,
                        assessment_id: assessment.id,
                        type: item.type,
                        question: item.question,
                        options: item.options,
                        payload: item.payload,
                        correct_answer: item.correct_answer,
                        points: item.points,
                        time_limit: item.time_limit,
                        order: item.order,
                        cachedAt,
                    });
                }
            } catch {
                // Cache offline bersifat best-effort; permainan tetap berjalan.
            }
        };

        void cache();
    }, [assessment, context.chapter_id, questions]);

    useEffect(() => {
        if (phase !== 'playing') {
            return;
        }

        const interval = window.setInterval(() => setNow(Date.now()), 1000);

        return () => window.clearInterval(interval);
    }, [phase]);

    useEffect(() => {
        questionStartedAtRef.current = Date.now();
    }, [currentIndex, phase]);

    useEffect(() => {
        if (phase === 'playing' && remainingSeconds === 0) {
            finishGame();
        }
    });

    function startGame() {
        finishedGuardRef.current = false;
        setAnswers({});
        setDrafts({});
        setCurrentIndex(0);
        setStartedAt(new Date().toISOString());
        setFinishedAt(null);
        setNow(Date.now());
        setSaveState('idle');
        setOpenHint(null);
        setPhase('playing');
    }

    function goTo(index: number) {
        if (index < 0 || index >= questions.length || phase !== 'playing') {
            return;
        }

        setCurrentIndex(index);
    }

    function updateDraft(response: GameResponse) {
        if (!question) {
            return;
        }

        setDrafts((current) => ({ ...current, [question.id]: response }));
    }

    function checkCurrent() {
        if (!question || revealed || !draft || !hasResponse(question, draft)) {
            return;
        }

        const evaluation = evaluateQuestion(question, draft);
        const timeSpent = Math.max(
            1,
            Math.round(
                (Date.now() - questionStartedAtRef.current) / 1000,
            ),
        );

        setAnswers((current) => ({
            ...current,
            [question.id]: {
                questionId: question.id,
                response: draft,
                ...evaluation,
                timeSpent,
                answeredAt: new Date().toISOString(),
            },
        }));
    }

    function nextQuestion() {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex((index) => index + 1);

            return;
        }

        finishGame();
    }

    function finishGame() {
        if (finishedGuardRef.current || phase !== 'playing' || !startedAt) {
            return;
        }

        finishedGuardRef.current = true;

        const completedAt = new Date().toISOString();
        const nextSummary = summarizeGame(
            questions,
            answers,
            assessment.passing_score,
            startedAt,
            completedAt,
        );

        setFinishedAt(completedAt);
        setPhase('finished');
        void persistResult(completedAt, nextSummary);
    }

    async function persistResult(
        completedAt: string,
        nextSummary: GameSummary,
    ) {
        if (!startedAt) {
            return;
        }

        if (!user) {
            setSaveState('guest');

            return;
        }

        try {
            const record = await syncService.enqueue('session', {
                assessment_id: assessment.id,
                mode: assessment.difficulty,
                duration_seconds: nextSummary.durationSeconds,
                started_at: startedAt,
                completed_at: completedAt,
                answers: buildSessionAnswers(questions, answers),
            });

            if (!record) {
                setSaveState('error');

                return;
            }

            setSaveState('queued');

            await offlineDb
                .put('sessions', {
                    uuid: record.uuid,
                    userId: user.id,
                    assessmentId: assessment.id,
                    mode: assessment.difficulty,
                    score: nextSummary.totalScore,
                    correctAnswers: nextSummary.correctCount,
                    totalQuestions: nextSummary.totalQuestions,
                    durationSeconds: nextSummary.durationSeconds,
                    startedAt,
                    completedAt,
                    synced: false,
                })
                .catch(() => undefined);
        } catch {
            setSaveState('error');
        }
    }

    function handleMaterialRead(readCount: number) {
        if (!user) {
            return;
        }

        void syncService
            .enqueue('progress', {
                chapter_id: context.chapter_id,
                status: 'in_progress',
                materials_read: readCount,
                last_accessed_at: new Date().toISOString(),
            })
            .catch(() => undefined);
    }

    /**
     * Skor blok interaktif bersifat formatif (plan §3.4): disimpan untuk siswa
     * dan guru, tetapi tidak menambah skor sesi. Tamu tetap mendapat progres
     * lokal lewat `lib/material/store`; hanya pengguna masuk yang disinkronkan.
     */
    function handleBlockRecord(payload: MaterialBlockPayload) {
        if (!user) {
            return;
        }

        void syncService
            .enqueue('material_block', { ...payload })
            .catch(() => undefined);
    }

    const stageProps = question
        ? {
              question,
              response: draft,
              onChange: updateDraft,
              disabled: revealed,
              revealed,
          }
        : null;

    const isAtLastQuestion = currentIndex === questions.length - 1;
    const ready = question ? hasResponse(question, draft) : false;

    return (
        <>
            <Head title={`${assessment.title} — Bermain`} />

            <AppLayout levelTheme={context.level_theme}>
                <div className="scroll-quiet min-h-0 flex-1 overflow-y-auto">
                    {phase === 'intro' && (
                        <IntroPanel
                            assessment={assessment}
                            context={context}
                            identity={identity}
                            progress={progress}
                            questions={questions}
                            materials={materials}
                            essayCount={essayCount}
                            gradedCount={gradedCount}
                            totalPoints={totalPoints}
                            isLoggedIn={Boolean(user)}
                            userName={user?.name ?? null}
                            userXp={user?.xp ?? 0}
                            onStart={startGame}
                            onMaterialRead={handleMaterialRead}
                            onBlockRecord={handleBlockRecord}
                        />
                    )}

                    {phase === 'playing' && question && stageProps && (
                        <div className="mx-auto flex w-full max-w-6xl flex-col gap-3 px-3 py-3 sm:px-5 sm:py-4">
                            <div className="flex flex-wrap items-center justify-between gap-2">
                                <div className="flex min-w-0 items-center gap-2.5">
                                    <Link
                                        href="/"
                                        onClick={(event) => {
                                            if (
                                                answeredCount > 0 &&
                                                !window.confirm(
                                                    'Keluar sekarang? Jawaban yang belum diselesaikan akan hilang.',
                                                )
                                            ) {
                                                event.preventDefault();
                                            }
                                        }}
                                        className="grid h-8 w-8 shrink-0 place-items-center rounded-lg bg-surface text-ink/45 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red"
                                        aria-label="Kembali ke katalog"
                                    >
                                        <ArrowLeftIcon className="h-3.5 w-3.5" />
                                    </Link>

                                    <div className="min-w-0">
                                        <p className="truncate text-[9px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                                            {context.level_name} ·{' '}
                                            {context.class_name} ·{' '}
                                            {context.subject_name}
                                        </p>
                                        <p className="truncate text-[13px] font-bold text-ink">
                                            {context.chapter_title}
                                        </p>
                                    </div>
                                </div>

                                <div className="flex items-center gap-1.5">
                                    <span
                                        className={cn(
                                            'inline-flex h-8 items-center gap-1.5 rounded-lg px-2.5 text-[10px] font-bold tracking-[0.08em] uppercase ring-1',
                                            difficulty.className,
                                        )}
                                    >
                                        <span
                                            aria-hidden
                                            className="h-1.5 w-1.5 rounded-full bg-current opacity-60"
                                        />
                                        {difficulty.label}
                                    </span>
                                    <span
                                        className={cn(
                                            'inline-flex h-8 items-center gap-1.5 rounded-lg border px-2.5 text-[11px] font-bold tabular-nums',
                                            remainingSeconds <= 60
                                                ? 'border-red/30 bg-red-tint text-red'
                                                : 'border-rule bg-surface text-ink/65',
                                        )}
                                        role="timer"
                                        aria-live="off"
                                    >
                                        <ClockIcon className="h-3.5 w-3.5" />
                                        {formatClock(remainingSeconds)}
                                    </span>
                                </div>
                            </div>

                            <div className="flex items-center gap-2">
                                <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-ink/[0.06]">
                                    <div
                                        className="h-full rounded-full bg-red transition-[width] duration-300"
                                        style={{
                                            width: `${Math.round(
                                                (answeredCount /
                                                    questions.length) *
                                                    100,
                                            )}%`,
                                        }}
                                    />
                                </div>
                                <span className="shrink-0 text-[9.5px] font-bold text-ink/40 tabular-nums">
                                    {answeredCount}/{questions.length}
                                </span>
                            </div>

                            <div className="grid gap-3 lg:grid-cols-[minmax(0,1fr)_270px]">
                                <section className="overflow-hidden rounded-3xl border border-rule bg-surface shadow-card">
                                    <header className="flex flex-wrap items-start justify-between gap-2 border-b border-rule bg-canvas/30 px-4 py-3 sm:px-5">
                                        <div className="flex min-w-0 items-center gap-2.5">
                                            <span
                                                className={cn(
                                                    'grid h-10 w-10 shrink-0 place-items-center rounded-xl text-[19px]',
                                                    theme.tile,
                                                )}
                                            >
                                                {context.subject_icon ?? '📘'}
                                            </span>
                                            <div className="min-w-0">
                                                <p className="text-[9px] font-bold tracking-[0.14em] text-red uppercase">
                                                    Soal {currentIndex + 1} dari{' '}
                                                    {questions.length}
                                                </p>
                                                <p className="truncate text-[11px] font-semibold text-ink/40">
                                                    {context.chapter_code
                                                        ? `${context.chapter_code} · `
                                                        : ''}
                                                    {context.subject_group ??
                                                        'Umum'}
                                                </p>
                                            </div>
                                        </div>

                                        <div className="flex flex-wrap items-center gap-1.5">
                                            <span className="rounded-full bg-canvas px-2 py-1 text-[9px] font-bold text-ink/45 ring-1 ring-rule">
                                                {question.type_label}
                                            </span>
                                            <span className="rounded-full bg-red-tint px-2 py-1 text-[9px] font-bold text-red">
                                                {question.points} poin
                                            </span>
                                        </div>
                                    </header>

                                    <div className="px-4 pt-4 pb-5 sm:px-5">
                                        <div className="flex items-start gap-3">
                                            <span className="hidden pt-1 font-serif text-[28px] leading-none text-red/20 sm:block">
                                                “
                                            </span>
                                            <h1 className="display min-w-0 flex-1 text-[clamp(18px,2.4vw,26px)] leading-[1.22] text-ink">
                                                {question.question}
                                            </h1>
                                        </div>

                                        {question.media_url && (
                                            <img
                                                src={question.media_url}
                                                alt=""
                                                className="mt-3 max-h-52 w-full rounded-2xl border border-rule object-cover"
                                            />
                                        )}

                                        {question.hint && (
                                            <div className="mt-3">
                                                <button
                                                    type="button"
                                                    onClick={() =>
                                                        setOpenHint(
                                                            openHint ===
                                                                question.id
                                                                ? null
                                                                : question.id,
                                                        )
                                                    }
                                                    className="inline-flex items-center gap-1.5 rounded-full bg-canvas px-2.5 py-1 text-[9.5px] font-bold text-ink/45 ring-1 ring-rule transition-colors hover:text-red"
                                                >
                                                    <span aria-hidden>💡</span>
                                                    {openHint === question.id
                                                        ? 'Sembunyikan petunjuk'
                                                        : 'Lihat petunjuk'}
                                                </button>
                                                {openHint === question.id && (
                                                    <p className="mt-2 rounded-xl border border-rule bg-canvas px-3 py-2 text-[11px] leading-relaxed font-medium text-ink/65">
                                                        {question.hint}
                                                    </p>
                                                )}
                                            </div>
                                        )}

                                        <div className="mt-4">
                                            {question.type === 'simulation' &&
                                            question.options.length > 0 ? (
                                                <SimulationGame
                                                    key={question.id}
                                                    {...stageProps}
                                                />
                                            ) : isOrderingType(
                                                  question.type,
                                              ) ? (
                                                <DragDropGame
                                                    key={question.id}
                                                    {...stageProps}
                                                />
                                            ) : isMatchingType(
                                                  question.type,
                                              ) ? (
                                                <MatchGame
                                                    key={question.id}
                                                    {...stageProps}
                                                />
                                            ) : (
                                                <QuizGame
                                                    key={question.id}
                                                    {...stageProps}
                                                />
                                            )}
                                        </div>

                                        {answered && (
                                            <FeedbackPanel
                                                answer={answered}
                                                question={question}
                                                isLast={isAtLastQuestion}
                                            />
                                        )}

                                        <div className="mt-4 flex flex-wrap items-center justify-between gap-2 border-t border-rule pt-3">
                                            <div className="flex items-center gap-1.5">
                                                <button
                                                    type="button"
                                                    onClick={() =>
                                                        goTo(currentIndex - 1)
                                                    }
                                                    disabled={currentIndex === 0}
                                                    className="inline-flex h-8 items-center gap-1 rounded-lg px-2.5 text-[10px] font-bold text-ink/45 ring-1 ring-rule transition-colors hover:text-red disabled:pointer-events-none disabled:opacity-30"
                                                >
                                                    <ArrowLeftIcon className="h-3 w-3" />
                                                    Sebelumnya
                                                </button>
                                            </div>

                                            {!answered ? (
                                                <button
                                                    type="button"
                                                    onClick={checkCurrent}
                                                    disabled={!ready}
                                                    className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-red px-4 text-[11px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:pointer-events-none disabled:opacity-35"
                                                >
                                                    Periksa jawaban
                                                    <CheckIcon className="h-3.5 w-3.5" />
                                                </button>
                                            ) : (
                                                <button
                                                    type="button"
                                                    onClick={nextQuestion}
                                                    className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-red px-4 text-[11px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                                >
                                                    {isAtLastQuestion
                                                        ? 'Lihat hasil'
                                                        : 'Soal berikutnya'}
                                                    <ArrowRightIcon className="h-3.5 w-3.5" />
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                </section>

                                <aside className="grid content-start gap-3">
                                    <div className="rounded-2xl border border-rule bg-surface p-3.5 shadow-card">
                                        <div className="flex items-center justify-between gap-2">
                                            <p className="text-[9px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                                                Peta soal
                                            </p>
                                            <span className="text-[9px] font-semibold text-ink/35">
                                                {answeredCount} terjawab
                                            </span>
                                        </div>

                                        <div className="mt-2.5 flex flex-wrap gap-1.5">
                                            {questions.map((item, index) => {
                                                const result = answers[item.id];
                                                const isCurrent =
                                                    index === currentIndex;

                                                return (
                                                    <button
                                                        key={item.id}
                                                        type="button"
                                                        onClick={() =>
                                                            goTo(index)
                                                        }
                                                        aria-label={`Soal ${index + 1}`}
                                                        aria-current={
                                                            isCurrent
                                                                ? 'step'
                                                                : undefined
                                                        }
                                                        className={cn(
                                                            'grid h-7 w-7 place-items-center rounded-lg text-[9.5px] font-bold tabular-nums ring-1 transition-all',
                                                            !result &&
                                                                'bg-canvas text-ink/40 ring-rule hover:text-red',
                                                            result?.ungraded &&
                                                                'bg-ink/[0.06] text-ink/55 ring-ink/15',
                                                            result &&
                                                                !result.ungraded &&
                                                                result.isCorrect &&
                                                                'bg-red text-white ring-red',
                                                            result &&
                                                                !result.ungraded &&
                                                                !result.isCorrect &&
                                                                'bg-red-tint text-red ring-red/30',
                                                            isCurrent &&
                                                                'scale-110 shadow-fab',
                                                        )}
                                                    >
                                                        {index + 1}
                                                    </button>
                                                );
                                            })}
                                        </div>

                                        <div className="mt-3 grid gap-1.5 text-[9px] font-semibold text-ink/40">
                                            <Legend
                                                className="bg-red"
                                                label="Benar"
                                            />
                                            <Legend
                                                className="bg-red-tint ring-1 ring-red/40"
                                                label="Perlu diperbaiki"
                                            />
                                            <Legend
                                                className="bg-ink/25"
                                                label="Uraian"
                                            />
                                        </div>
                                    </div>

                                    <div className="rounded-2xl border border-rule bg-canvas/40 p-3.5">
                                        <p className="text-[9px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                                            Sesi bermain
                                        </p>
                                        <p className="mt-1.5 truncate text-[12px] font-bold text-ink">
                                            {identity
                                                ? identity.name
                                                : (user?.name ?? 'Tamu')}
                                        </p>
                                        <p className="mt-0.5 text-[10px] leading-relaxed font-medium text-ink/40">
                                            {identity?.mode === 'group'
                                                ? `${identity.members.length} pemain · skor tim`
                                                : identity
                                                  ? 'Mode pribadi'
                                                  : user
                                                    ? 'Mode pribadi'
                                                    : 'Masuk untuk menyimpan progres'}
                                        </p>
                                        {identity?.mode === 'group' && (
                                            <p className="mt-1.5 line-clamp-2 text-[9.5px] leading-relaxed text-ink/35">
                                                {identity.members.join(', ')}
                                            </p>
                                        )}
                                    </div>

                                    <div className="rounded-2xl border border-red/15 bg-red-tint/50 p-3.5">
                                        <p className="text-[9px] font-bold tracking-[0.16em] text-red uppercase">
                                            Target
                                        </p>
                                        <p className="mt-1.5 font-serif text-[22px] leading-none font-semibold text-red">
                                            {assessment.passing_score}
                                            <span className="ml-1 text-[10px] font-bold">
                                                KKM
                                            </span>
                                        </p>
                                        <p className="mt-1 text-[10px] leading-relaxed font-medium text-ink/45">
                                            {answeredCount > 0
                                                ? `${answeredCount} soal sudah dikunci. Kamu bisa kembali lewat peta soal.`
                                                : 'Jawab dengan teliti. Setiap soal bisa diperiksa sekali.'}
                                        </p>
                                    </div>
                                </aside>
                            </div>
                        </div>
                    )}

                    {phase === 'finished' && summary && (
                        <ResultPanel
                            assessment={assessment}
                            context={context}
                            identity={identity}
                            questions={questions}
                            answers={answers}
                            summary={summary}
                            saveState={saveState}
                            isLoggedIn={Boolean(user)}
                            userName={user?.name ?? null}
                            userXp={user?.xp ?? 0}
                            onRestart={startGame}
                        />
                    )}
                </div>
            </AppLayout>
        </>
    );
}

function IntroPanel({
    assessment,
    context,
    identity,
    progress,
    questions,
    materials,
    essayCount,
    gradedCount,
    totalPoints,
    isLoggedIn,
    userName,
    userXp,
    onStart,
    onMaterialRead,
    onBlockRecord,
}: {
    assessment: AssessmentProp;
    context: ContextProp;
    identity: PlayIdentity | null;
    progress: ProgressProp | null;
    questions: GameQuestion[];
    materials: MaterialProp[];
    essayCount: number;
    gradedCount: number;
    totalPoints: number;
    isLoggedIn: boolean;
    userName: string | null;
    userXp: number;
    onStart: () => void;
    onMaterialRead: (readCount: number) => void;
    onBlockRecord: (payload: MaterialBlockPayload) => void;
}) {
    const theme = subjectTheme(context.subject_color);
    const difficulty = DIFFICULTY_META[assessment.difficulty];
    const mechanics = Array.from(
        new Set(questions.map((question) => question.type_label)),
    );
    const level = levelProgress(userXp);

    return (
        <div className="mx-auto w-full max-w-5xl px-3 py-4 sm:px-5 sm:py-6">
            <Link
                href="/"
                className="inline-flex items-center gap-1.5 text-[10.5px] font-bold text-ink/45 transition-colors hover:text-red"
            >
                <ArrowLeftIcon className="h-3.5 w-3.5" />
                Kembali ke jelajah materi
            </Link>

            <section className="relative mt-3 overflow-hidden rounded-[28px] border border-rule bg-surface shadow-card">
                <span
                    aria-hidden
                    className="pointer-events-none absolute -top-24 -right-16 h-72 w-72 rounded-full bg-red/10 blur-3xl"
                />
                <span
                    aria-hidden
                    className="pointer-events-none absolute -bottom-28 -left-16 h-64 w-64 rounded-full bg-ink/[0.04] blur-3xl"
                />

                <div className="relative grid gap-6 p-5 sm:p-7 lg:grid-cols-[minmax(0,1fr)_310px] lg:items-end">
                    <div className="min-w-0">
                        <div className="flex flex-wrap items-center gap-2">
                            <span className="inline-flex items-center gap-1.5 rounded-full bg-red-tint px-2.5 py-1 text-[9px] font-bold tracking-[0.14em] text-red uppercase">
                                <span aria-hidden>🎮</span>
                                Siap dimainkan
                            </span>
                            <span
                                className={cn(
                                    'rounded-full px-2 py-1 text-[9px] font-bold tracking-[0.08em] uppercase ring-1',
                                    difficulty.className,
                                )}
                            >
                                Mode {difficulty.label}
                            </span>
                        </div>

                        <div className="mt-4 flex items-start gap-3.5">
                            <span
                                className={cn(
                                    'grid h-16 w-16 shrink-0 place-items-center rounded-2xl text-[32px] leading-none shadow-card sm:h-20 sm:w-20 sm:text-[38px]',
                                    theme.tile,
                                )}
                            >
                                {context.subject_icon ?? '📘'}
                            </span>
                            <div className="min-w-0">
                                <p className="text-[9.5px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                                    {context.level_name} ·{' '}
                                    {context.class_name} ·{' '}
                                    {context.subject_name}
                                </p>
                                <h1 className="display mt-1 text-[clamp(26px,4vw,42px)] leading-[1.03] tracking-[-0.03em] text-ink">
                                    {context.chapter_title}
                                    <span className="text-red">.</span>
                                </h1>
                                <p className="mt-2 max-w-xl text-[12px] leading-relaxed font-medium text-ink/50">
                                    {assessment.title}. Jawab soal, kumpulkan
                                    poin, lalu lihat hasilmu. Progres tersimpan
                                    otomatis dan disinkronkan saat online.
                                </p>
                            </div>
                        </div>

                        <div className="mt-5 flex flex-wrap gap-1.5">
                            {mechanics.map((mechanic) => (
                                <span
                                    key={mechanic}
                                    className="rounded-full bg-canvas px-2.5 py-1 text-[9.5px] font-semibold text-ink/45 ring-1 ring-rule"
                                >
                                    {mechanic}
                                </span>
                            ))}
                        </div>

                        <dl className="mt-5 grid grid-cols-2 gap-2 sm:grid-cols-4">
                            <MiniStat
                                label="Soal inti"
                                value={String(gradedCount)}
                            />
                            <MiniStat
                                label="Uraian"
                                value={essayCount > 0 ? String(essayCount) : '—'}
                            />
                            <MiniStat
                                label="Waktu"
                                value={`${Math.ceil(assessment.duration / 60)} m`}
                            />
                            <MiniStat
                                label="Poin"
                                value={formatNumber(totalPoints)}
                            />
                        </dl>
                    </div>

                    <div className="rounded-2xl border border-rule bg-canvas/45 p-4">
                        <p className="text-[9px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                            Pemain
                        </p>
                        <p className="mt-1.5 truncate font-serif text-[21px] leading-tight font-semibold text-ink">
                            {identity ? identity.name : (userName ?? 'Tamu')}
                        </p>
                        <p className="mt-1 text-[10.5px] leading-relaxed font-medium text-ink/45">
                            {identity?.mode === 'group'
                                ? `${identity.members.length} pemain dalam satu tim`
                                : identity
                                  ? 'Sesi pribadi tersimpan di perangkat ini'
                                  : isLoggedIn
                                    ? 'Kamu bermain sebagai pengguna masuk'
                                    : 'Masuk agar hasil masuk ke profilmu'}
                        </p>

                        {identity?.mode === 'group' && (
                            <p className="mt-2 line-clamp-3 rounded-lg bg-surface px-2.5 py-2 text-[9.5px] leading-relaxed text-ink/40 ring-1 ring-rule">
                                {identity.members.join(' · ')}
                            </p>
                        )}

                        {progress && (
                            <div className="mt-3 rounded-xl bg-surface px-3 py-2 ring-1 ring-rule">
                                <div className="flex items-center justify-between gap-2 text-[9px] font-bold tracking-[0.08em] text-ink/40 uppercase">
                                    <span>Rekor bab</span>
                                    <span className="text-red">
                                        {progress.best_score}
                                    </span>
                                </div>
                                <p className="mt-1 text-[9.5px] font-medium text-ink/35">
                                    {progress.attempts} percobaan tercatat
                                </p>
                            </div>
                        )}

                        {isLoggedIn && (
                            <div className="mt-3">
                                <div className="flex items-center justify-between text-[9px] font-bold text-ink/40">
                                    <span>Level {level.level}</span>
                                    <span>
                                        {level.xpToNextLevel === null
                                            ? 'Maksimal'
                                            : `${level.xpToNextLevel} XP lagi`}
                                    </span>
                                </div>
                                <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-ink/[0.07]">
                                    <div
                                        className="h-full rounded-full bg-red"
                                        style={{
                                            width: `${level.progressPercent}%`,
                                        }}
                                    />
                                </div>
                            </div>
                        )}

                        <button
                            type="button"
                            onClick={onStart}
                            className="mt-4 inline-flex h-11 w-full items-center justify-center gap-2 rounded-xl bg-red px-5 text-[12px] font-bold tracking-[0.04em] text-white uppercase shadow-fab transition-all hover:-translate-y-0.5 hover:bg-red-deep"
                        >
                            <PlayIcon className="h-4 w-4" />
                            Mulai bermain
                        </button>

                        <p className="mt-2 text-center text-[9px] leading-relaxed font-medium text-ink/35">
                            Bisa dimainkan offline. Uraian disimpan untuk
                            penilaian lanjutan.
                        </p>
                    </div>
                </div>
            </section>

            <MaterialViewer
                materials={materials}
                chapterId={context.chapter_id}
                initialRead={progress?.materials_read ?? 0}
                isLoggedIn={isLoggedIn}
                onRead={onMaterialRead}
                onBlockRecord={onBlockRecord}
            />

            <div className="mt-3 grid gap-2 sm:grid-cols-3">
                <InfoCard
                    icon="⏱"
                    title="Waktu terbatas"
                    text={`Total ${formatClock(assessment.duration)} untuk seluruh soal. Timer berjalan setelah kamu menekan mulai.`}
                />
                <InfoCard
                    icon="🔒"
                    title="Sekali periksa"
                    text="Jawaban dikunci setelah diperiksa. Gunakan peta soal untuk meninjau jawaban sebelumnya."
                />
                <InfoCard
                    icon="☁️"
                    title="Sinkron offline"
                    text="Hasil disimpan di perangkat lalu dikirim ke server saat koneksi kembali tersedia."
                />
            </div>
        </div>
    );
}

function MiniStat({ label, value }: { label: string; value: string }) {
    return (
        <div className="rounded-xl border border-rule bg-surface px-2.5 py-2">
            <dt className="text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                {label}
            </dt>
            <dd className="mt-0.5 font-serif text-[17px] leading-none font-semibold text-ink">
                {value}
            </dd>
        </div>
    );
}

function InfoCard({
    icon,
    title,
    text,
}: {
    icon: string;
    title: string;
    text: string;
}) {
    return (
        <div className="rounded-2xl border border-rule bg-surface/80 px-3.5 py-3">
            <p className="flex items-center gap-1.5 text-[10px] font-bold text-ink/65">
                <span aria-hidden>{icon}</span>
                {title}
            </p>
            <p className="mt-1 text-[10px] leading-relaxed font-medium text-ink/40">
                {text}
            </p>
        </div>
    );
}

function FeedbackPanel({
    answer,
    question,
    isLast,
}: {
    answer: EvaluatedAnswer;
    question: GameQuestion;
    isLast: boolean;
}) {
    if (answer.ungraded) {
        return (
            <div className="mt-4 rounded-2xl border border-rule bg-canvas px-4 py-3">
                <p className="text-[10.5px] font-bold text-ink/65">
                    Jawaban uraian tersimpan
                </p>
                <p className="mt-1 text-[11px] leading-relaxed font-medium text-ink/55">
                    Uraian tidak masuk skor sesi ini. Guru atau penilaian AI
                    akan meninjaunya pada tahap berikutnya.
                </p>
            </div>
        );
    }

    return (
        <div
            className={cn(
                'mt-4 rounded-2xl border px-4 py-3',
                answer.isCorrect
                    ? 'border-red/30 bg-red-tint'
                    : 'border-rule bg-canvas',
            )}
        >
            <div className="flex flex-wrap items-center justify-between gap-2">
                <p
                    className={cn(
                        'text-[10.5px] font-bold',
                        answer.isCorrect
                            ? 'text-red'
                            : 'text-ink/55',
                    )}
                >
                    {answer.isCorrect
                        ? `Tepat! +${answer.pointsEarned} poin`
                        : 'Belum tepat'}
                </p>
                {!answer.isCorrect && answer.expected && (
                    <p className="text-[10px] font-semibold text-ink/50">
                        Jawaban: {answer.expected}
                    </p>
                )}
            </div>

            {question.explanation && (
                <p className="mt-1.5 text-[11.5px] leading-relaxed font-medium text-ink/60">
                    {question.explanation}
                </p>
            )}

            {isLast && (
                <p className="mt-2 text-[9.5px] font-semibold text-ink/35">
                    Tekan “Lihat hasil” untuk menutup sesi.
                </p>
            )}
        </div>
    );
}

function Legend({ className, label }: { className: string; label: string }) {
    return (
        <span className="flex items-center gap-1.5">
            <span
                aria-hidden
                className={cn('h-2 w-2 rounded-sm', className)}
            />
            {label}
        </span>
    );
}

function ResultPanel({
    assessment,
    context,
    identity,
    questions,
    answers,
    summary,
    saveState,
    isLoggedIn,
    userName,
    userXp,
    onRestart,
}: {
    assessment: AssessmentProp;
    context: ContextProp;
    identity: PlayIdentity | null;
    questions: GameQuestion[];
    answers: Record<number, EvaluatedAnswer>;
    summary: GameSummary;
    saveState: SaveState;
    isLoggedIn: boolean;
    userName: string | null;
    userXp: number;
    onRestart: () => void;
}) {
    const theme = subjectTheme(context.subject_color);
    const badges = sessionBadges(summary, {
        subjectName: context.subject_name,
        difficulty: assessment.difficulty,
        questions,
    });
    const nextXp = userXp + summary.earnedPoints;
    const level = levelProgress(nextXp);
    const earnedLevel = levelForXp(nextXp);
    const coins = coinsForXp(summary.earnedPoints);
    const essayCount = questions.filter(
        (question) => question.type === 'essay',
    ).length;

    return (
        <div className="mx-auto w-full max-w-5xl px-3 py-4 sm:px-5 sm:py-6">
            <section className="relative overflow-hidden rounded-[28px] border border-rule bg-surface p-5 shadow-card sm:p-7">
                <span
                    aria-hidden
                    className="pointer-events-none absolute -top-24 -right-20 h-72 w-72 rounded-full bg-red/10 blur-3xl"
                />

                <div className="relative flex flex-wrap items-center justify-between gap-3">
                    <div className="flex items-center gap-2.5">
                        <span
                            className={cn(
                                'grid h-11 w-11 place-items-center rounded-2xl text-[22px]',
                                theme.tile,
                            )}
                        >
                            {context.subject_icon ?? '📘'}
                        </span>
                        <div>
                            <p className="text-[9px] font-bold tracking-[0.16em] text-ink/35 uppercase">
                                {context.chapter_title} ·{' '}
                                {identity?.name ?? userName ?? 'Sesi selesai'}
                            </p>
                            <h1 className="display text-[24px] leading-tight text-ink sm:text-[30px]">
                                {summary.isPassed ? 'Kerja bagus' : 'Terus coba'}
                                <span className="text-red">.</span>
                            </h1>
                        </div>
                    </div>

                    <span
                        className={cn(
                            'rounded-full px-3 py-1.5 text-[9px] font-bold tracking-[0.12em] uppercase ring-1',
                            summary.isPassed
                                ? 'bg-red text-white ring-red'
                                : 'bg-canvas text-ink/55 ring-rule',
                        )}
                    >
                        {summary.isPassed ? 'Lulus KKM' : 'Belum lulus KKM'}
                    </span>
                </div>

                <div className="relative mt-5 grid gap-5 lg:grid-cols-[210px_minmax(0,1fr)] lg:items-center">
                    <ScoreRing score={summary.totalScore} />

                    <div className="grid gap-2.5">
                        <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
                            <ResultStat
                                label="Benar"
                                value={String(summary.correctCount)}
                                tone="text-red"
                            />
                            <ResultStat
                                label="Salah"
                                value={String(summary.wrongCount)}
                                tone="text-ink/55"
                            />
                            <ResultStat
                                label="Kosong"
                                value={String(summary.unansweredCount)}
                                tone="text-ink/55"
                            />
                            <ResultStat
                                label="Waktu"
                                value={formatDuration(summary.durationSeconds)}
                                tone="text-ink/55"
                            />
                        </div>

                        <div className="grid gap-2 sm:grid-cols-2">
                            <div className="rounded-2xl border border-rule bg-canvas/40 px-3.5 py-3">
                                <p className="text-[9px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                                    Hadiah sesi
                                </p>
                                <div className="mt-1.5 flex flex-wrap items-center gap-2">
                                    <span className="inline-flex items-center gap-1 rounded-full bg-red-tint px-2 py-1 text-[10px] font-bold text-red">
                                        +{formatNumber(summary.earnedPoints)} XP
                                    </span>
                                    <span className="inline-flex items-center gap-1 rounded-full bg-canvas px-2 py-1 text-[10px] font-bold text-ink/55 ring-1 ring-rule">
                                        +{formatNumber(coins)} koin
                                    </span>
                                    {isLoggedIn && (
                                        <span className="text-[9.5px] font-semibold text-ink/35">
                                            Level {earnedLevel}
                                        </span>
                                    )}
                                </div>
                                <p className="mt-1.5 text-[9px] leading-relaxed font-medium text-ink/35">
                                    {summary.maxScore} poin inti ·{' '}
                                    {essayCount > 0
                                        ? `${essayCount} uraian menunggu penilaian`
                                        : 'tanpa uraian'}
                                </p>
                            </div>

                            <div className="rounded-2xl border border-rule bg-canvas/40 px-3.5 py-3">
                                <p className="text-[9px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                                    Progres level
                                </p>
                                <div className="mt-1.5 flex items-center justify-between text-[10px] font-bold text-ink/55">
                                    <span>
                                        Level {level.level} · {level.title}
                                    </span>
                                    <span>
                                        {level.xpToNextLevel === null
                                            ? 'Maksimal'
                                            : `${level.xpToNextLevel} XP lagi`}
                                    </span>
                                </div>
                                <div className="mt-1.5 h-1.5 overflow-hidden rounded-full bg-ink/[0.07]">
                                    <div
                                        className="h-full rounded-full bg-red"
                                        style={{
                                            width: `${level.progressPercent}%`,
                                        }}
                                    />
                                </div>
                                <p className="mt-1.5 text-[9px] font-medium text-ink/35">
                                    {isLoggedIn
                                        ? `Perkiraan total ${formatNumber(nextXp)} XP setelah sinkron`
                                        : 'Masuk untuk menyimpan XP ke profil'}
                                </p>
                            </div>
                        </div>

                        <SyncNotice saveState={saveState} isLoggedIn={isLoggedIn} />
                    </div>
                </div>

                {badges.length > 0 && (
                    <div className="relative mt-4 flex flex-wrap gap-2 border-t border-rule pt-4">
                        {badges.map((badge) => (
                            <span
                                key={badge.slug}
                                title={badge.description}
                                className="inline-flex items-center gap-1.5 rounded-full bg-canvas px-2.5 py-1 text-[9.5px] font-bold text-ink/55 ring-1 ring-rule"
                            >
                                <span aria-hidden>{badge.icon}</span>
                                {badge.title}
                            </span>
                        ))}
                    </div>
                )}
            </section>

            <div className="mt-3 flex flex-wrap gap-2">
                <button
                    type="button"
                    onClick={onRestart}
                    className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-red px-4 text-[11px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                >
                    <PlayIcon className="h-3.5 w-3.5" />
                    Main lagi
                </button>
                <Link
                    href="/"
                    className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-surface px-4 text-[11px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-red"
                >
                    <ArrowLeftIcon className="h-3.5 w-3.5" />
                    Jelajah materi
                </Link>
                {isLoggedIn && (
                    <Link
                        href="/progres"
                        className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-surface px-4 text-[11px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-red"
                    >
                        Lihat progres
                    </Link>
                )}
                {!isLoggedIn && (
                    <Link
                        href="/masuk"
                        className="inline-flex h-9 items-center gap-1.5 rounded-xl bg-canvas px-4 text-[11px] font-bold text-red ring-1 ring-red/20 transition-colors hover:bg-red-tint"
                    >
                        Masuk untuk menyimpan
                    </Link>
                )}
            </div>

            <section className="mt-4 rounded-2xl border border-rule bg-surface shadow-card">
                <div className="flex items-center justify-between gap-2 border-b border-rule px-4 py-3">
                    <div>
                        <h2 className="font-serif text-[18px] font-semibold tracking-[-0.02em] text-ink">
                            Tinjau jawaban
                        </h2>
                        <p className="mt-0.5 text-[9.5px] font-medium text-ink/40">
                            {summary.totalQuestions} soal inti ·{' '}
                            {essayCount} uraian
                        </p>
                    </div>
                </div>

                <div className="divide-y divide-rule/70">
                    {questions.map((question, index) => {
                        const answer = answers[question.id];

                        return (
                            <ReviewRow
                                key={question.id}
                                index={index}
                                question={question}
                                answer={answer}
                            />
                        );
                    })}
                </div>
            </section>
        </div>
    );
}

function ScoreRing({ score }: { score: number }) {
    const radius = 52;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (Math.min(100, score) / 100) * circumference;

    return (
        <div className="relative mx-auto grid h-[150px] w-[150px] place-items-center">
            <svg
                viewBox="0 0 120 120"
                className="absolute inset-0 h-full w-full -rotate-90"
                aria-hidden
            >
                <circle
                    cx="60"
                    cy="60"
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="8"
                    className="text-ink/[0.06]"
                />
                <circle
                    cx="60"
                    cy="60"
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="8"
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={offset}
                    className="text-red transition-[stroke-dashoffset] duration-700"
                />
            </svg>
            <div className="text-center">
                <p className="font-serif text-[42px] leading-none font-semibold tracking-[-0.04em] text-ink">
                    {score}
                </p>
                <p className="mt-1 text-[8.5px] font-bold tracking-[0.16em] text-ink/35 uppercase">
                    Skor sesi
                </p>
            </div>
        </div>
    );
}

function ResultStat({
    label,
    value,
    tone,
}: {
    label: string;
    value: string;
    tone: string;
}) {
    return (
        <div className="rounded-xl border border-rule bg-canvas/40 px-2.5 py-2">
            <p className="text-[8px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                {label}
            </p>
            <p className={cn('mt-0.5 font-serif text-[16px] font-semibold', tone)}>
                {value}
            </p>
        </div>
    );
}

function SyncNotice({
    saveState,
    isLoggedIn,
}: {
    saveState: SaveState;
    isLoggedIn: boolean;
}) {
    if (saveState === 'queued') {
        return (
            <div className="rounded-xl border border-red/25 bg-red-tint px-3 py-2 text-[10px] leading-relaxed font-semibold text-red">
                Hasil masuk antrean sinkronisasi. Server akan menghitung ulang
                jawaban objektif saat perangkat online.
            </div>
        );
    }

    if (saveState === 'guest' || !isLoggedIn) {
        return (
            <div className="rounded-xl border border-rule bg-canvas px-3 py-2 text-[10px] leading-relaxed font-semibold text-ink/60">
                Sesi tamu tidak dikirim ke server. Masuk agar XP, koin, dan
                progres bab tersimpan.
            </div>
        );
    }

    if (saveState === 'error') {
        return (
            <div className="rounded-xl border border-ink/15 bg-canvas px-3 py-2 text-[10px] leading-relaxed font-semibold text-ink/60">
                Hasil belum bisa masuk antrean lokal. Coba lagi setelah
                penyimpanan perangkat tersedia.
            </div>
        );
    }

    return null;
}

function ReviewRow({
    index,
    question,
    answer,
}: {
    index: number;
    question: GameQuestion;
    answer: EvaluatedAnswer | undefined;
}) {
    return (
        <div className="flex items-start gap-3 px-4 py-3">
            <span className="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-canvas text-[9.5px] font-bold text-ink/40 ring-1 ring-rule">
                {index + 1}
            </span>

            <div className="min-w-0 flex-1">
                <div className="flex flex-wrap items-center gap-1.5">
                    <span className="text-[8.5px] font-bold tracking-[0.1em] text-ink/35 uppercase">
                        {question.type_label}
                    </span>
                    {answer ? (
                        <span
                            className={cn(
                                'rounded-full px-1.5 py-0.5 text-[8px] font-bold',
                                answer.ungraded
                                    ? 'bg-ink/[0.06] text-ink/60'
                                    : answer.isCorrect
                                      ? 'bg-red text-white'
                                      : 'bg-canvas text-ink/45 ring-1 ring-rule',
                            )}
                        >
                            {answer.ungraded
                                ? 'Uraian'
                                : answer.isCorrect
                                  ? `+${answer.pointsEarned} poin`
                                  : 'Salah'}
                        </span>
                    ) : (
                        <span className="rounded-full bg-canvas px-1.5 py-0.5 text-[8px] font-bold text-ink/35">
                            Kosong
                        </span>
                    )}
                </div>

                <p className="mt-1 text-[11.5px] leading-snug font-semibold text-ink/70">
                    {question.question}
                </p>

                {answer?.response.text && (
                    <p className="mt-1 line-clamp-3 rounded-lg bg-canvas/60 px-2.5 py-1.5 text-[10.5px] leading-relaxed text-ink/50">
                        {answer.response.text}
                    </p>
                )}

                {answer && !answer.isCorrect && answer.expected && (
                    <p className="mt-1 text-[9.5px] font-semibold text-ink/40">
                        Jawaban: {answer.expected}
                    </p>
                )}
            </div>
        </div>
    );
}

function ArrowLeftIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="M19 12H5M11 6l-6 6 6 6" />
        </svg>
    );
}

function ArrowRightIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="M5 12h14M13 6l6 6-6 6" />
        </svg>
    );
}

function CheckIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.4"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="m5 12 4.5 4.5L19 7" />
        </svg>
    );
}

function ClockIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            className={className}
        >
            <circle cx="12" cy="12" r="8.5" />
            <path d="M12 7.5V12l3 2" />
        </svg>
    );
}

function PlayIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="currentColor"
            className={className}
        >
            <path d="M8 5.5v13l11-6.5-11-6.5Z" />
        </svg>
    );
}
