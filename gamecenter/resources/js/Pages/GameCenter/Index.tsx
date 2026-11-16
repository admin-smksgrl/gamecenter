import { Head, Link, usePage } from '@inertiajs/react';
import { useEffect, useMemo, useRef, useState } from 'react';
import type { FormEvent, ReactNode } from 'react';

import AppLayout from '@/Layouts/AppLayout';
import { LEVEL_GROUPS, groupOf, isMergedGroup } from '@/lib/level-groups';
import { resolveLevelTheme } from '@/lib/level-theme';
import { offlineDb } from '@/lib/offline/offline-db';
import { DIFFICULTY_META, cn, formatNumber, subjectTheme } from '@/lib/utils';
import type { PageProps } from '@/types';

type Difficulty = 'easy' | 'medium' | 'hard';

const MODES: Difficulty[] = ['easy', 'medium', 'hard'];

const WIDE_PAGE_SIZE = 12;
const COMPACT_PAGE_SIZE = 8;

const PLAY_STORAGE_KEY = 'gamecenter.play-session';
const MAX_GROUP_PLAYERS = 8;

type PlayMode = 'solo' | 'group';

interface PlaySession {
    mode: PlayMode;
    name: string;
    members: string[];
}

function loadPlaySession(): PlaySession | null {
    if (typeof window === 'undefined') {
        return null;
    }

    try {
        const raw = window.localStorage.getItem(PLAY_STORAGE_KEY);

        if (!raw) {
            return null;
        }

        const data = JSON.parse(raw) as Partial<PlaySession>;

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
        // Sesi lama yang rusak diabaikan.
    }

    return null;
}

function storePlaySession(session: PlaySession | null) {
    try {
        if (session) {
            window.localStorage.setItem(
                PLAY_STORAGE_KEY,
                JSON.stringify(session),
            );
        } else {
            window.localStorage.removeItem(PLAY_STORAGE_KEY);
        }
    } catch {
        // Penyimpanan lokal bisa diblokir; sesi tetap jalan di memori.
    }
}

function usePageSize(): number {
    const [pageSize, setPageSize] = useState(() =>
        window.innerWidth >= 1024 ? WIDE_PAGE_SIZE : COMPACT_PAGE_SIZE,
    );

    useEffect(() => {
        function handleResize() {
            setPageSize(
                window.innerWidth >= 1024
                    ? WIDE_PAGE_SIZE
                    : COMPACT_PAGE_SIZE,
            );
        }

        window.addEventListener('resize', handleResize);

        return () => window.removeEventListener('resize', handleResize);
    }, []);

    return pageSize;
}

interface AssessmentProp {
    id: number;
    difficulty: Difficulty;
    duration: number;
    questions_count: number;
}

interface ChapterProp {
    id: number;
    code: string | null;
    title: string;
    description: string | null;
    materials_count: number;
    assessments: AssessmentProp[];
}

interface SubjectProp {
    id: number;
    name: string;
    slug: string;
    group: string | null;
    icon: string | null;
    color: string | null;
    chapters_count: number;
    chapters: ChapterProp[];
}

interface ClassProp {
    id: number;
    name: string;
    slug: string;
    grade_level: number;
    phase: string | null;
    subjects: SubjectProp[];
}

interface LevelProp {
    id: number;
    name: string;
    slug: string;
    short_name: string | null;
    description: string | null;
    theme: string;
    icon: string | null;
    classes: ClassProp[];
}

interface StatsProp {
    levels: number;
    classes: number;
    subjects: number;
    chapters: number;
    materials: number;
    questions: number;
}

interface RecentProp {
    chapter_id: number;
    chapter_title: string | null;
    subject_name: string | null;
    subject_icon: string | null;
    subject_color: string | null;
    level_name: string | null;
    level_theme: string;
    best_score: number;
    status: string;
    assessment_id: number | null;
}

interface Props {
    levels: LevelProp[];
    stats: StatsProp;
    recent: RecentProp[];
    /** Jenjang milik pengguna; dipakai sebagai pilihan awal agar tema langsung sesuai. */
    defaultLevel?: string | null;
    [key: string]: unknown;
}

interface MenuOption {
    value: string;
    label: string;
    hint?: string;
    icon?: ReactNode;
}

function totalQuestions(subject: SubjectProp, mode: Difficulty): number {
    return subject.chapters.reduce(
        (total, chapter) =>
            total +
            (chapter.assessments.find(
                (assessment) => assessment.difficulty === mode,
            )?.questions_count ?? 0),
        0,
    );
}

export default function Index({ levels, stats, recent, defaultLevel }: Props) {
    const { version } = usePage<PageProps>().props;

    // Mulai dari jenjang pengguna supaya tema tidak tercampur dengan jenjang lain.
    const initialLevel = useMemo(
        () =>
            levels.find((level) => level.slug === defaultLevel) ??
            levels[0],
        [levels, defaultLevel],
    );

    const [activeGroupSlug, setActiveGroupSlug] = useState<string>(
        initialLevel ? groupOf(initialLevel.slug).slug : '',
    );
    const [activeClassId, setActiveClassId] = useState<number | null>(
        initialLevel?.classes[0]?.id ?? null,
    );
    const [activeGroup, setActiveGroup] = useState<string>('semua');
    const [activeSubject, setActiveSubject] = useState<string>('semua');
    const [activeMode, setActiveMode] = useState<Difficulty>('easy');
    const [search, setSearch] = useState('');
    const [searchOpen, setSearchOpen] = useState(false);
    const [openSubject, setOpenSubject] = useState<SubjectProp | null>(null);
    const [page, setPage] = useState(1);
    const [playSession, setPlaySession] = useState<PlaySession | null>(
        loadPlaySession,
    );
    const [playDialog, setPlayDialog] = useState<PlayMode | null>(null);

    const listRef = useRef<HTMLDivElement>(null);
    const pageSize = usePageSize();

    /** Grup jenjang terpilih; SMA-SMK berisi dua jenjang sekaligus. */
    const activeLevelGroup = useMemo(
        () =>
            LEVEL_GROUPS.find((group) => group.slug === activeGroupSlug) ??
            (initialLevel ? groupOf(initialLevel.slug) : LEVEL_GROUPS[0]),
        [activeGroupSlug, initialLevel],
    );

    /** Jenjang yang tercakup grup terpilih. */
    const activeLevels = useMemo(
        () =>
            activeLevelGroup.levels
                .map((slug) => levels.find((level) => level.slug === slug))
                .filter((level): level is LevelProp => Boolean(level)),
        [activeLevelGroup, levels],
    );

    const activeLevel = activeLevels[0] ?? levels[0];

    /** Seluruh kelas dari jenjang dalam grup (SMA + SMK saat digabung). */
    const activeClasses = useMemo(
        () =>
            activeLevels.flatMap((level) =>
                level.classes.map((classRoom) => ({
                    classRoom,
                    level,
                })),
            ),
        [activeLevels],
    );

    const activeClass = useMemo(() => {
        if (activeClasses.length === 0) {
            return undefined;
        }

        return (
            activeClasses.find((item) => item.classRoom.id === activeClassId)
                ?.classRoom ?? activeClasses[0].classRoom
        );
    }, [activeClasses, activeClassId]);

    const groups = useMemo(() => {
        if (!activeClass) {
            return [];
        }

        return Array.from(
            new Set(
                activeClass.subjects
                    .map((subject) => subject.group)
                    .filter((group): group is string => Boolean(group)),
            ),
        );
    }, [activeClass]);

    const groupCounts = useMemo(() => {
        const counts = new Map<string, number>();

        activeClass?.subjects.forEach((subject) => {
            if (!subject.group) {
                return;
            }

            counts.set(subject.group, (counts.get(subject.group) ?? 0) + 1);
        });

        return counts;
    }, [activeClass]);

    const modeTotals = useMemo(() => {
        const totals: Record<Difficulty, number> = {
            easy: 0,
            medium: 0,
            hard: 0,
        };

        activeClass?.subjects.forEach((subject) => {
            subject.chapters.forEach((chapter) => {
                chapter.assessments.forEach((assessment) => {
                    totals[assessment.difficulty] += assessment.questions_count;
                });
            });
        });

        return totals;
    }, [activeClass]);

    const searchMatches = useMemo(() => {
        if (!activeClass) {
            return 0;
        }

        const term = search.trim().toLowerCase();

        if (term === '') {
            return activeClass.subjects.length;
        }

        return activeClass.subjects.filter((subject) =>
            subject.name.toLowerCase().includes(term),
        ).length;
    }, [activeClass, search]);

    const subjects = useMemo(() => {
        if (!activeClass) {
            return [];
        }

        const term = search.trim().toLowerCase();

        return activeClass.subjects.filter((subject) => {
            const matchesGroup =
                activeGroup === 'semua' || subject.group === activeGroup;
            const matchesSubject =
                activeSubject === 'semua' ||
                String(subject.id) === activeSubject;
            const matchesSearch =
                term === '' || subject.name.toLowerCase().includes(term);

            return matchesGroup && matchesSubject && matchesSearch;
        });
    }, [activeClass, activeGroup, activeSubject, search]);

    const chapterTotal =
        activeClass?.subjects.reduce(
            (total, subject) => total + subject.chapters_count,
            0,
        ) ?? 0;

    // Jumlah soal mengikuti kelas yang sedang dibuka, bukan total seluruh situs,
    // supaya jenjang tanpa materi tidak menampilkan angka milik jenjang lain.
    const questionTotal =
        activeClass?.subjects.reduce(
            (total, subject) =>
                total +
                subject.chapters.reduce(
                    (sum, chapter) =>
                        sum +
                        chapter.assessments.reduce(
                            (count, assessment) =>
                                count + assessment.questions_count,
                            0,
                        ),
                    0,
                ),
            0,
        ) ?? 0;

    const totalPages = Math.max(1, Math.ceil(subjects.length / pageSize));
    const currentPage = Math.min(page, totalPages);
    const pageStart = (currentPage - 1) * pageSize;
    const pageSubjects = subjects.slice(pageStart, pageStart + pageSize);

    const isFiltering =
        activeGroup !== 'semua' ||
        activeSubject !== 'semua' ||
        search.trim() !== '';

    useEffect(() => {
        setPage(1);
    }, [activeGroupSlug, activeClassId, activeGroup, activeSubject, search, pageSize]);

    useEffect(() => {
        listRef.current?.scrollTo({ top: 0 });
    }, [currentPage, activeGroupSlug, activeClassId, activeGroup, activeSubject, search]);

    useEffect(() => {
        // Simpan katalog terakhir agar jelajah materi tetap tersedia offline.
        void offlineDb
            .saveCatalog({ levels, stats, version })
            .catch(() => undefined);
    }, [levels, stats, version]);

    function goToPage(next: number) {
        setPage(Math.min(Math.max(1, next), totalPages));
    }

    useEffect(() => {
        function handleShortcut(event: KeyboardEvent) {
            const target = event.target as HTMLElement | null;
            const isTyping =
                target instanceof HTMLInputElement ||
                target instanceof HTMLTextAreaElement ||
                target?.isContentEditable;

            if (event.key === '/' && !isTyping) {
                event.preventDefault();
                setSearchOpen(true);
            }
        }

        window.addEventListener('keydown', handleShortcut);

        return () => window.removeEventListener('keydown', handleShortcut);
    }, []);

    function selectLevelGroup(slug: string) {
        const group = LEVEL_GROUPS.find((item) => item.slug === slug);

        if (!group) {
            return;
        }

        const firstLevel = group.levels
            .map((levelSlug) => levels.find((level) => level.slug === levelSlug))
            .find((level): level is LevelProp => Boolean(level));

        setActiveGroupSlug(group.slug);
        setActiveClassId(firstLevel?.classes[0]?.id ?? null);
        setActiveGroup('semua');
        setActiveSubject('semua');
        setSearch('');
        setOpenSubject(null);
    }

    function selectClass(id: number) {
        setActiveClassId(id);
        setActiveGroup('semua');
        setActiveSubject('semua');
        setOpenSubject(null);
    }

    function selectSubjectFilter(value: string) {
        setActiveSubject(value);
        setActiveGroup('semua');
        setSearch('');
        setOpenSubject(null);
    }

    function selectGroup(value: string) {
        setActiveGroup(value);
        setActiveSubject('semua');
    }

    function handleSearchChange(value: string) {
        setSearch(value);

        if (value.trim() !== '') {
            setActiveGroup('semua');
            setActiveSubject('semua');
        }
    }

    function clearSearch() {
        setSearch('');
    }

    function resetFilters() {
        setActiveGroup('semua');
        setActiveSubject('semua');
        setSearch('');
    }

    function selectSubject(subject: SubjectProp) {
        if (subject.chapters_count === 0) {
            return;
        }

        setOpenSubject(subject);
    }

    function startPlaySession(session: PlaySession) {
        setPlaySession(session);
        storePlaySession(session);
        setPlayDialog(null);
    }

    function endPlaySession() {
        setPlaySession(null);
        storePlaySession(null);
    }

    if (!activeLevel || !activeClass) {
        return (
            <AppLayout>
                <div className="grid flex-1 place-items-center px-6 text-center">
                    <p className="text-sm font-semibold text-ink/50">
                        Belum ada data kurikulum.
                    </p>
                </div>
            </AppLayout>
        );
    }

    const levelOptions: MenuOption[] = LEVEL_GROUPS.map((group) => {
        const groupLevels = group.levels
            .map((slug) => levels.find((level) => level.slug === slug))
            .filter((level): level is LevelProp => Boolean(level));
        const classCount = groupLevels.reduce(
            (total, level) => total + level.classes.length,
            0,
        );

        return {
            value: group.slug,
            label: group.label,
            hint: isMergedGroup(group)
                ? `${classCount} kelas · SMA & SMK`
                : `${classCount} kelas`,
            icon: (
                <span className="text-[14px] leading-none grayscale">
                    {groupLevels[0]?.icon ?? '📚'}
                </span>
            ),
        };
    });

    const nav = (
        <>
            <TopbarMenu
                ariaLabel="Pilih jenjang"
                label="Jenjang"
                value={activeLevelGroup.slug}
                onChange={selectLevelGroup}
                options={levelOptions}
            />
            <TopbarMenu
                ariaLabel="Pilih kelas"
                label="Kelas"
                value={String(activeClass.id)}
                onChange={(value) => selectClass(Number(value))}
                options={activeClasses.map(({ classRoom, level }) => ({
                    value: String(classRoom.id),
                    label: classRoom.name,
                    hint: isMergedGroup(activeLevelGroup)
                        ? level.name
                        : classRoom.phase
                          ? `Fase ${classRoom.phase}`
                          : `${classRoom.subjects.length} mapel`,
                    icon: <BookIcon className="h-3.5 w-3.5" />,
                }))}
            />
            <TopbarMenu
                ariaLabel="Pilih mata pelajaran"
                label="Mapel"
                value={activeSubject}
                onChange={selectSubjectFilter}
                options={[
                    {
                        value: 'semua',
                        label: 'Semua mapel',
                        hint: `${activeClass.subjects.length} pilihan`,
                        icon: <LayersIcon className="h-3.5 w-3.5" />,
                    },
                    ...activeClass.subjects.map((subject) => ({
                        value: String(subject.id),
                        label: subject.name,
                        hint:
                            subject.chapters_count > 0
                                ? `${subject.chapters_count} bab`
                                : 'Segera hadir',
                        icon: (
                            <span className="text-[13px] leading-none">
                                {subject.icon ?? '📘'}
                            </span>
                        ),
                    })),
                ]}
            />
            <span
                aria-hidden
                className="mx-1 hidden h-6 w-px shrink-0 bg-rule sm:block"
            />
            <TopbarMenu
                ariaLabel="Mode permainan"
                label="Mode"
                value={activeMode}
                align="right"
                className="ml-auto lg:ml-0"
                onChange={(value) => setActiveMode(value as Difficulty)}
                options={MODES.map((item) => ({
                    value: item,
                    label: DIFFICULTY_META[item].label,
                    hint: `${modeTotals[item]} soal`,
                    icon: (
                        <span
                            className={cn(
                                'h-1.5 w-1.5 rounded-full',
                                DIFFICULTY_META[item].dot,
                            )}
                        />
                    ),
                }))}
            />
        </>
    );

    return (
        <>
            <Head title="Materi Game" />

            <AppLayout
                nav={nav}
                levelTheme={activeLevel.theme}
                onSearch={() => setSearchOpen(true)}
                play={
                    <PlayControl
                        session={playSession}
                        onPick={setPlayDialog}
                        onEnd={endPlaySession}
                    />
                }
                footerCenter={
                    subjects.length > 0 ? (
                        <Pagination
                            page={currentPage}
                            totalPages={totalPages}
                            start={pageStart + 1}
                            end={pageStart + pageSubjects.length}
                            total={subjects.length}
                            onChange={goToPage}
                        />
                    ) : undefined
                }
            >
                <div className="mx-auto flex min-h-0 w-full max-w-[1640px] flex-1 flex-col gap-2.5 px-3 pt-3 pb-3 sm:gap-3.5 sm:px-5 sm:pt-4 sm:pb-4 lg:px-7">
                    {/* ── Ringkasan singkat ────────────────────────── */}
                    <section className="flex shrink-0 items-end justify-between gap-4">
                        <div className="min-w-0">
                            <span className="inline-flex items-center gap-1.5 rounded-full bg-red-tint px-2.5 py-1 text-[9.5px] font-bold tracking-[0.16em] text-red uppercase">
                                <SparkleIcon className="h-3 w-3" />
                                Katalog materi
                            </span>

                            <h1 className="display mt-2 text-[clamp(27px,3.1vw,40px)] leading-[1.02] text-ink">
                                Materi game{' '}
                                <span className="relative inline-block whitespace-nowrap">
                                    <span
                                        aria-hidden
                                        className="absolute inset-x-1 bottom-[0.08em] h-[0.3em] -rotate-1 rounded-full bg-red/15"
                                    />
                                    <span className="relative italic">
                                        pilihanmu
                                    </span>
                                </span>
                                <span className="text-red">.</span>
                            </h1>

                            <p className="mt-1.5 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-[11.5px] font-medium text-ink/45">
                                <span>
                                    <b className="font-bold text-ink/70">
                                        {activeClass.subjects.length}
                                    </b>{' '}
                                    mapel
                                </span>
                                <span className="text-ink/20">·</span>
                                <span>
                                    <b className="font-bold text-ink/70">
                                        {chapterTotal}
                                    </b>{' '}
                                    bab siap dimainkan
                                </span>
                                <span className="text-ink/20">·</span>
                                <span>
                                    <b className="font-bold text-ink/70">
                                        {formatNumber(questionTotal)}
                                    </b>{' '}
                                    soal
                                </span>
                            </p>
                        </div>

                        <p className="hidden shrink-0 items-center gap-1.5 pb-1 text-[10.5px] font-semibold text-ink/35 md:flex">
                            Tekan
                            <kbd className="grid h-5 w-5 place-items-center rounded-md border border-rule bg-surface text-[10px] font-bold text-ink/50">
                                /
                            </kbd>
                            untuk mencari
                        </p>
                    </section>

                    {recent.length > 0 && (
                        <section
                            aria-label="Lanjutkan belajar"
                            className="shrink-0"
                        >
                            <div className="mb-1.5 flex items-center justify-between gap-2">
                                <p className="flex items-center gap-1.5 text-[9px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                                    <SparkleIcon className="h-3 w-3 text-red" />
                                    Lanjutkan belajar
                                </p>
                                <Link
                                    href="/progres"
                                    className="text-[9.5px] font-bold text-red transition-colors hover:text-red-deep"
                                >
                                    Semua progres
                                </Link>
                            </div>

                            <div className="no-bar -mx-1 flex gap-2 overflow-x-auto px-1 pb-1">
                                {recent.map((item) => {
                                    const theme = subjectTheme(
                                        item.subject_color,
                                    );
                                    const level = resolveLevelTheme(
                                        item.level_theme,
                                    );
                                    const className = cn(
                                        'flex w-[220px] shrink-0 items-center gap-2 rounded-xl border bg-surface px-2.5 py-2 text-left transition-all',
                                        theme.border,
                                        item.assessment_id
                                            ? 'hover:-translate-y-0.5 hover:shadow-card'
                                            : 'opacity-70',
                                    );

                                    const body = (
                                        <>
                                            <span
                                                className={cn(
                                                    'grid h-8 w-8 shrink-0 place-items-center rounded-lg text-[15px]',
                                                    theme.tile,
                                                )}
                                            >
                                                {item.subject_icon ?? '📘'}
                                            </span>
                                            <span className="min-w-0 flex-1">
                                                <span className="block truncate text-[11px] font-bold text-ink">
                                                    {item.chapter_title ??
                                                        'Bab'}
                                                </span>
                                                <span className="mt-0.5 flex items-center gap-1 text-[9px] font-semibold text-ink/40">
                                                    <span aria-hidden>
                                                        {level.emoji}
                                                    </span>
                                                    <span className="truncate">
                                                        {item.subject_name ??
                                                            'Mapel'}
                                                    </span>
                                                    <span className="text-ink/20">
                                                        ·
                                                    </span>
                                                    <span className="shrink-0 font-bold text-red tabular-nums">
                                                        {item.best_score}
                                                    </span>
                                                </span>
                                            </span>
                                            <span className="shrink-0 rounded-full bg-canvas px-1.5 py-0.5 text-[8px] font-bold text-ink/45 ring-1 ring-rule">
                                                {item.status === 'completed'
                                                    ? 'Selesai'
                                                    : 'Lanjut'}
                                            </span>
                                        </>
                                    );

                                    return item.assessment_id ? (
                                        <Link
                                            key={item.chapter_id}
                                            href={`/main/${item.assessment_id}`}
                                            className={className}
                                        >
                                            {body}
                                        </Link>
                                    ) : (
                                        <div
                                            key={item.chapter_id}
                                            className={className}
                                        >
                                            {body}
                                        </div>
                                    );
                                })}
                            </div>
                        </section>
                    )}

                    {/* ── Chip kelompok mapel ──────────────────────── */}
                    <section
                        aria-label="Filter kelompok mapel"
                        className="flex shrink-0 items-center gap-2"
                    >
                        <div className="no-bar -mx-1 flex min-w-0 flex-1 items-center gap-1.5 overflow-x-auto px-1 pb-0.5">
                            <GroupChip
                                label="Semua"
                                count={activeClass.subjects.length}
                                isActive={activeGroup === 'semua'}
                                onClick={() => selectGroup('semua')}
                            />
                            {groups.map((group) => (
                                <GroupChip
                                    key={group}
                                    label={group}
                                    count={groupCounts.get(group) ?? 0}
                                    isActive={activeGroup === group}
                                    onClick={() => selectGroup(group)}
                                />
                            ))}
                            {search.trim() !== '' && (
                                <button
                                    type="button"
                                    onClick={clearSearch}
                                    aria-label={`Hapus pencarian ${search.trim()}`}
                                    className="inline-flex shrink-0 items-center gap-1.5 rounded-full bg-red-tint px-3 py-1.5 text-[10.5px] font-bold text-red transition-colors hover:bg-red hover:text-white"
                                >
                                    <SearchIcon className="h-3 w-3" />
                                    <span className="max-w-[160px] truncate">
                                        Cari: “{search.trim()}”
                                    </span>
                                    <CloseIcon className="h-3 w-3 opacity-60" />
                                </button>
                            )}
                        </div>
                    </section>

                    {chapterTotal === 0 && !isFiltering && (
                        <div className="flex shrink-0 items-center gap-2 rounded-xl border border-rule bg-red-tint px-3 py-2 text-[11px] font-semibold text-red">
                            <SparkleIcon className="h-3.5 w-3.5 shrink-0" />
                            <span>
                                Materi {activeLevelGroup.label} sedang
                                disiapkan. Pilih jenjang lain untuk mulai
                                bermain sekarang.
                            </span>
                        </div>
                    )}

                    {/* ── Kartu materi (fokus utama) ───────────────── */}
                    <section
                        aria-label="Daftar mata pelajaran"
                        className="relative min-h-0 flex-1"
                    >
                        <div
                            ref={listRef}
                            className="no-bar h-full overflow-y-auto overscroll-contain"
                        >
                            {subjects.length === 0 ? (
                                <EmptyState
                                    onReset={resetFilters}
                                    isFiltering={isFiltering}
                                />
                            ) : (
                                <div className="grid auto-rows-[minmax(108px,auto)] grid-cols-2 gap-2.5 pb-1 sm:auto-rows-[minmax(116px,auto)] sm:gap-3 md:grid-cols-3 lg:grid-cols-4">
                                    {pageSubjects.map((subject, index) => (
                                        <SubjectCard
                                            key={subject.id}
                                            subject={subject}
                                            index={index}
                                            mode={activeMode}
                                            isOpen={
                                                openSubject?.id === subject.id
                                            }
                                            onSelect={() =>
                                                selectSubject(subject)
                                            }
                                        />
                                    ))}
                                </div>
                            )}
                        </div>
                    </section>
                </div>
            </AppLayout>

            {openSubject && (
                <ChapterSheet
                    subject={openSubject}
                    mode={activeMode}
                    onModeChange={setActiveMode}
                    onClose={() => setOpenSubject(null)}
                />
            )}

            {searchOpen && (
                <SearchPalette
                    query={search}
                    resultCount={searchMatches}
                    onQueryChange={handleSearchChange}
                    onClose={() => setSearchOpen(false)}
                />
            )}

            {playDialog && (
                <PlaySetupDialog
                    mode={playDialog}
                    initial={playSession}
                    onSubmit={startPlaySession}
                    onClose={() => setPlayDialog(null)}
                />
            )}
        </>
    );
}

function TopbarMenu({
    ariaLabel,
    label,
    value,
    options,
    onChange,
    align = 'left',
    className,
}: {
    ariaLabel: string;
    label: string;
    value: string;
    options: MenuOption[];
    onChange: (value: string) => void;
    align?: 'left' | 'right';
    className?: string;
}) {
    const [open, setOpen] = useState(false);
    const rootRef = useRef<HTMLDivElement>(null);

    const current = options.find((option) => option.value === value);

    useEffect(() => {
        if (!open) {
            return;
        }

        function handlePointer(event: PointerEvent) {
            if (
                rootRef.current &&
                !rootRef.current.contains(event.target as Node)
            ) {
                setOpen(false);
            }
        }

        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                setOpen(false);
            }
        }

        document.addEventListener('pointerdown', handlePointer);
        window.addEventListener('keydown', handleKey);

        return () => {
            document.removeEventListener('pointerdown', handlePointer);
            window.removeEventListener('keydown', handleKey);
        };
    }, [open]);

    return (
        <div ref={rootRef} className={cn('relative shrink-0', className)}>
            <button
                type="button"
                aria-label={ariaLabel}
                aria-haspopup="menu"
                aria-expanded={open}
                onClick={() => setOpen((isOpen) => !isOpen)}
                className={cn(
                    'flex h-8 items-center gap-1.5 rounded-lg px-2 text-left transition-colors',
                    open
                        ? 'bg-red-tint text-red'
                        : 'text-ink/60 hover:bg-red-tint/70 hover:text-red',
                )}
            >
                <span className="flex flex-col leading-none">
                    <span className="text-[7.5px] font-bold tracking-[0.18em] uppercase opacity-55">
                        {label}
                    </span>
                    <span className="mt-1 flex items-center gap-1 text-[11.5px] font-bold text-ink">
                        {current?.icon}
                        <span className="max-w-[76px] truncate sm:max-w-[124px]">
                            {current?.label}
                        </span>
                    </span>
                </span>
                <ChevronDownIcon
                    className={cn(
                        'h-3 w-3 shrink-0 text-ink/30 transition-transform duration-200',
                        open && 'rotate-180 text-red',
                    )}
                />
            </button>

            {open && (
                <div
                    role="menu"
                    aria-label={ariaLabel}
                    className={cn(
                        'scroll-quiet absolute top-[calc(100%+8px)] z-40 max-h-[min(60vh,420px)] w-60 overflow-y-auto rounded-xl border border-rule bg-surface p-1 shadow-sheet',
                        align === 'right' ? 'right-0' : 'left-0',
                    )}
                >
                    {options.map((option) => {
                        const isActive = option.value === value;

                        return (
                            <button
                                key={option.value}
                                type="button"
                                role="menuitemradio"
                                aria-checked={isActive}
                                onClick={() => {
                                    onChange(option.value);
                                    setOpen(false);
                                }}
                                className={cn(
                                    'flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left transition-colors',
                                    isActive
                                        ? 'bg-red-tint text-red'
                                        : 'text-ink/65 hover:bg-canvas hover:text-ink',
                                )}
                            >
                                <span className="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-surface ring-1 ring-rule/80">
                                    {option.icon ?? (
                                        <span className="h-1.5 w-1.5 rounded-full bg-current" />
                                    )}
                                </span>
                                <span className="min-w-0 flex-1">
                                    <span className="block truncate text-[12px] font-semibold">
                                        {option.label}
                                    </span>
                                    {option.hint && (
                                        <span className="block text-[9.5px] font-medium text-ink/35">
                                            {option.hint}
                                        </span>
                                    )}
                                </span>
                                {isActive && (
                                    <CheckIcon className="h-3.5 w-3.5 shrink-0" />
                                )}
                            </button>
                        );
                    })}
                </div>
            )}
        </div>
    );
}

function SearchPalette({
    query,
    resultCount,
    onQueryChange,
    onClose,
}: {
    query: string;
    resultCount: number;
    onQueryChange: (value: string) => void;
    onClose: () => void;
}) {
    const inputRef = useRef<HTMLInputElement>(null);

    useEffect(() => {
        inputRef.current?.focus();

        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                onClose();
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    }, [onClose]);

    return (
        <div
            role="dialog"
            aria-modal="true"
            aria-label="Pencarian materi"
            className="fixed inset-0 z-50 flex justify-center px-3"
        >
            <button
                type="button"
                aria-label="Tutup pencarian"
                onClick={onClose}
                className="absolute inset-0 animate-veil-in bg-black/45 backdrop-blur-[2px]"
            />

            <div className="relative mt-[12vh] h-fit w-[min(560px,100%)] animate-rise overflow-hidden rounded-2xl border border-rule bg-surface shadow-sheet">
                <div className="flex items-center gap-3 border-b border-rule px-4 py-3">
                    <SearchIcon className="h-4 w-4 shrink-0 text-red" />
                    <input
                        ref={inputRef}
                        type="search"
                        value={query}
                        onChange={(event) => onQueryChange(event.target.value)}
                        onKeyDown={(event) => {
                            if (event.key === 'Enter') {
                                onClose();
                            }
                        }}
                        placeholder="Cari mata pelajaran…"
                        aria-label="Cari mata pelajaran"
                        autoFocus
                        className="w-full bg-transparent text-[13.5px] font-medium text-ink placeholder:text-ink/35 focus:outline-none"
                    />
                    {query !== '' && (
                        <button
                            type="button"
                            onClick={() => onQueryChange('')}
                            aria-label="Hapus kata kunci"
                            className="grid h-6 w-6 shrink-0 place-items-center rounded-full bg-canvas text-ink/45 transition-colors hover:bg-red-tint hover:text-red"
                        >
                            <CloseIcon className="h-3 w-3" />
                        </button>
                    )}
                </div>

                <div className="flex items-center justify-between gap-3 px-4 py-2.5 text-[10.5px] font-semibold text-ink/40">
                    <span>
                        <b className="font-bold text-ink/70">{resultCount}</b>{' '}
                        mapel cocok
                    </span>
                    <span className="flex items-center gap-1">
                        <kbd className="rounded-md border border-rule bg-canvas px-1.5 py-0.5 text-[9.5px] font-bold text-ink/45">
                            esc
                        </kbd>
                        untuk menutup
                    </span>
                </div>
            </div>
        </div>
    );
}

function PlayControl({
    session,
    onPick,
    onEnd,
}: {
    session: PlaySession | null;
    onPick: (mode: PlayMode) => void;
    onEnd: () => void;
}) {
    const [open, setOpen] = useState(false);
    const rootRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!open) {
            return;
        }

        function handlePointer(event: PointerEvent) {
            if (
                rootRef.current &&
                !rootRef.current.contains(event.target as Node)
            ) {
                setOpen(false);
            }
        }

        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                setOpen(false);
            }
        }

        document.addEventListener('pointerdown', handlePointer);
        window.addEventListener('keydown', handleKey);

        return () => {
            document.removeEventListener('pointerdown', handlePointer);
            window.removeEventListener('keydown', handleKey);
        };
    }, [open]);

    const label = session
        ? session.mode === 'solo'
            ? session.name
            : `${session.name} · ${session.members.length}`
        : 'Bermain';

    return (
        <div ref={rootRef} className="relative shrink-0 max-lg:order-last">
            <button
                type="button"
                aria-label={
                    session ? `Menu bermain, sesi ${label}` : 'Menu bermain'
                }
                aria-haspopup="menu"
                aria-expanded={open}
                onClick={() => setOpen((isOpen) => !isOpen)}
                className="inline-flex h-9 items-center justify-center gap-1.5 rounded-lg bg-red px-2.5 text-white shadow-fab transition-colors hover:bg-red-deep"
            >
                <GamepadIcon className="h-4 w-4 shrink-0" />
                <span className="hidden max-w-[112px] truncate text-[10.5px] font-bold tracking-[0.02em] sm:inline">
                    {session ? label : 'Bermain'}
                </span>
                <ChevronDownIcon
                    className={cn(
                        'hidden h-3 w-3 shrink-0 opacity-70 transition-transform duration-200 sm:block',
                        open && 'rotate-180',
                    )}
                />
            </button>

            {open && (
                <div
                    role="menu"
                    aria-label="Menu bermain"
                    className="absolute top-[calc(100%+8px)] right-0 z-40 w-64 rounded-xl border border-rule bg-surface p-1 shadow-sheet"
                >
                    {session && (
                        <div className="mb-1 rounded-lg bg-canvas px-2.5 py-2">
                            <p className="text-[8.5px] font-bold tracking-[0.16em] text-ink/35 uppercase">
                                Sesi aktif
                            </p>
                            <p className="mt-0.5 truncate text-[11.5px] font-bold text-ink">
                                {session.name}
                                <span className="ml-1 font-semibold text-ink/40">
                                    {session.mode === 'solo'
                                        ? '· pribadi'
                                        : `· ${session.members.length} pemain`}
                                </span>
                            </p>
                            {session.mode === 'group' && (
                                <p className="mt-0.5 line-clamp-2 text-[9.5px] leading-snug font-medium text-ink/45">
                                    {session.members.join(', ')}
                                </p>
                            )}
                        </div>
                    )}

                    <button
                        type="button"
                        role="menuitem"
                        onClick={() => {
                            onPick('solo');
                            setOpen(false);
                        }}
                        className="flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left transition-colors hover:bg-canvas"
                    >
                        <span className="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-red-tint text-red">
                            <UserIcon className="h-3.5 w-3.5" />
                        </span>
                        <span className="min-w-0 flex-1">
                            <span className="block text-[12px] font-semibold text-ink">
                                Main pribadi
                            </span>
                            <span className="block text-[9.5px] font-medium text-ink/35">
                                Tulis namamu, main sendiri
                            </span>
                        </span>
                    </button>

                    <button
                        type="button"
                        role="menuitem"
                        onClick={() => {
                            onPick('group');
                            setOpen(false);
                        }}
                        className="flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left transition-colors hover:bg-canvas"
                    >
                        <span className="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-red-tint text-red">
                            <UsersIcon className="h-3.5 w-3.5" />
                        </span>
                        <span className="min-w-0 flex-1">
                            <span className="block text-[12px] font-semibold text-ink">
                                Bermain kelompok
                            </span>
                            <span className="block text-[9.5px] font-medium text-ink/35">
                                Nama kelompok + nama pemain
                            </span>
                        </span>
                    </button>

                    {session && (
                        <>
                            <span
                                aria-hidden
                                className="my-1 block h-px bg-rule/80"
                            />
                            <button
                                type="button"
                                role="menuitem"
                                onClick={() => {
                                    onEnd();
                                    setOpen(false);
                                }}
                                className="flex w-full items-center gap-2.5 rounded-lg px-2 py-1.5 text-left text-ink/55 transition-colors hover:bg-red-tint hover:text-red"
                            >
                                <span className="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-surface ring-1 ring-rule/80">
                                    <CloseIcon className="h-3.5 w-3.5" />
                                </span>
                                <span className="min-w-0 flex-1">
                                    <span className="block text-[12px] font-semibold">
                                        Akhiri sesi
                                    </span>
                                    <span className="block text-[9.5px] font-medium text-ink/35">
                                        Hapus pemain dari topbar
                                    </span>
                                </span>
                            </button>
                        </>
                    )}
                </div>
            )}
        </div>
    );
}

function PlaySetupDialog({
    mode,
    initial,
    onSubmit,
    onClose,
}: {
    mode: PlayMode;
    initial: PlaySession | null;
    onSubmit: (session: PlaySession) => void;
    onClose: () => void;
}) {
    const [playerName, setPlayerName] = useState(
        initial?.mode === 'solo' ? initial.name : '',
    );
    const [groupName, setGroupName] = useState(
        initial?.mode === 'group' ? initial.name : '',
    );
    const [members, setMembers] = useState<string[]>(
        initial?.mode === 'group' && initial.members.length >= 2
            ? initial.members
            : ['', ''],
    );

    useEffect(() => {
        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                onClose();
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    }, [onClose]);

    const isSolo = mode === 'solo';
    const namedMembers = members
        .map((member) => member.trim())
        .filter((member) => member !== '');
    const isValid = isSolo
        ? playerName.trim() !== ''
        : groupName.trim() !== '' && namedMembers.length >= 2;

    function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        if (!isValid) {
            return;
        }

        if (isSolo) {
            onSubmit({ mode: 'solo', name: playerName.trim(), members: [] });

            return;
        }

        onSubmit({
            mode: 'group',
            name: groupName.trim(),
            members: namedMembers,
        });
    }

    function updateMember(index: number, value: string) {
        setMembers((current) =>
            current.map((member, position) =>
                position === index ? value : member,
            ),
        );
    }

    function addMember() {
        setMembers((current) =>
            current.length >= MAX_GROUP_PLAYERS ? current : [...current, ''],
        );
    }

    function removeMember(index: number) {
        setMembers((current) =>
            current.length <= 2
                ? current
                : current.filter((_, position) => position !== index),
        );
    }

    const inputClass =
        'h-10 w-full rounded-lg border border-rule bg-surface px-3 text-[12.5px] font-medium text-ink transition-colors placeholder:text-ink/30 focus:border-red/40 focus:ring-2 focus:ring-red/10 focus:outline-none';

    return (
        <div
            role="dialog"
            aria-modal="true"
            aria-label={isSolo ? 'Main pribadi' : 'Bermain kelompok'}
            className="fixed inset-0 z-50 flex items-start justify-center px-3"
        >
            <button
                type="button"
                aria-label="Tutup pengaturan bermain"
                onClick={onClose}
                className="absolute inset-0 animate-veil-in bg-black/45 backdrop-blur-[2px]"
            />

            <form
                onSubmit={handleSubmit}
                className="relative mt-[10vh] flex max-h-[78vh] w-[min(460px,100%)] animate-rise flex-col overflow-hidden rounded-2xl border border-rule bg-surface shadow-sheet"
            >
                <div className="flex items-start gap-3 border-b border-rule px-4 py-4 sm:px-5">
                    <span className="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-red-tint text-red">
                        {isSolo ? (
                            <UserIcon className="h-5 w-5" />
                        ) : (
                            <UsersIcon className="h-5 w-5" />
                        )}
                    </span>
                    <div className="min-w-0 flex-1">
                        <p className="text-[8.5px] font-bold tracking-[0.18em] text-ink/35 uppercase">
                            Sesi permainan
                        </p>
                        <h2 className="display mt-0.5 text-[21px] leading-tight text-ink">
                            {isSolo ? 'Main pribadi' : 'Bermain kelompok'}
                        </h2>
                    </div>
                    <button
                        type="button"
                        onClick={onClose}
                        aria-label="Tutup"
                        className="grid h-8 w-8 shrink-0 place-items-center rounded-lg text-ink/40 transition-colors hover:bg-red-tint hover:text-red"
                    >
                        <CloseIcon className="h-4 w-4" />
                    </button>
                </div>

                <div className="scroll-quiet flex-1 overflow-y-auto px-4 py-4 sm:px-5">
                    {isSolo ? (
                        <label className="block">
                            <span className="mb-1.5 block text-[9.5px] font-bold tracking-[0.14em] text-ink/40 uppercase">
                                Nama pemain
                            </span>
                            <input
                                type="text"
                                value={playerName}
                                onChange={(event) =>
                                    setPlayerName(event.target.value)
                                }
                                placeholder="Tulis namamu…"
                                maxLength={40}
                                autoComplete="off"
                                autoFocus
                                className={inputClass}
                            />
                            <span className="mt-1.5 block text-[10.5px] font-medium text-ink/35">
                                Nama ini tampil di topbar selama sesi
                                bermain.
                            </span>
                        </label>
                    ) : (
                        <>
                            <label className="block">
                                <span className="mb-1.5 block text-[9.5px] font-bold tracking-[0.14em] text-ink/40 uppercase">
                                    Nama kelompok
                                </span>
                                <input
                                    type="text"
                                    value={groupName}
                                    onChange={(event) =>
                                        setGroupName(event.target.value)
                                    }
                                    placeholder="Contoh: Tim Merah"
                                    maxLength={40}
                                    autoComplete="off"
                                    autoFocus
                                    className={inputClass}
                                />
                            </label>

                            <div className="mt-4">
                                <div className="flex items-center justify-between gap-2">
                                    <span className="text-[9.5px] font-bold tracking-[0.14em] text-ink/40 uppercase">
                                        Pemain
                                    </span>
                                    <span className="text-[9.5px] font-semibold text-ink/35">
                                        Minimal 2 · maks {MAX_GROUP_PLAYERS}
                                    </span>
                                </div>

                                <div className="mt-1.5 space-y-1.5">
                                    {members.map((member, index) => (
                                        <div
                                            key={index}
                                            className="flex items-center gap-1.5"
                                        >
                                            <span className="grid h-9 w-7 shrink-0 place-items-center rounded-md bg-canvas text-[10px] font-bold text-ink/35 tabular-nums">
                                                {String(index + 1).padStart(
                                                    2,
                                                    '0',
                                                )}
                                            </span>
                                            <input
                                                type="text"
                                                value={member}
                                                onChange={(event) =>
                                                    updateMember(
                                                        index,
                                                        event.target.value,
                                                    )
                                                }
                                                placeholder={`Nama pemain ${index + 1}`}
                                                maxLength={40}
                                                autoComplete="off"
                                                className={cn(
                                                    inputClass,
                                                    'h-9',
                                                )}
                                            />
                                            <button
                                                type="button"
                                                onClick={() =>
                                                    removeMember(index)
                                                }
                                                disabled={members.length <= 2}
                                                aria-label={`Hapus pemain ${index + 1}`}
                                                className="grid h-9 w-9 shrink-0 place-items-center rounded-lg text-ink/35 transition-colors hover:bg-red-tint hover:text-red disabled:pointer-events-none disabled:opacity-25"
                                            >
                                                <CloseIcon className="h-3.5 w-3.5" />
                                            </button>
                                        </div>
                                    ))}
                                </div>

                                <button
                                    type="button"
                                    onClick={addMember}
                                    disabled={members.length >= MAX_GROUP_PLAYERS}
                                    className="mt-2 inline-flex items-center gap-1 rounded-lg px-2 py-1.5 text-[10.5px] font-bold text-red transition-colors hover:bg-red-tint disabled:pointer-events-none disabled:opacity-35"
                                >
                                    <PlusIcon className="h-3 w-3" />
                                    Tambah pemain
                                </button>
                            </div>
                        </>
                    )}
                </div>

                <div className="flex items-center justify-between gap-2 border-t border-rule bg-canvas/50 px-4 py-3 sm:px-5">
                    <p className="hidden text-[10px] font-medium text-ink/35 sm:block">
                        Tersimpan di perangkat ini
                    </p>
                    <div className="ml-auto flex items-center gap-1.5">
                        <button
                            type="button"
                            onClick={onClose}
                            className="rounded-lg px-3 py-2 text-[10.5px] font-bold text-ink/50 transition-colors hover:bg-canvas hover:text-ink"
                        >
                            Batal
                        </button>
                        <button
                            type="submit"
                            disabled={!isValid}
                            className="inline-flex items-center gap-1.5 rounded-lg bg-red px-3.5 py-2 text-[10.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:pointer-events-none disabled:opacity-35"
                        >
                            <PlayIcon className="h-3 w-3" />
                            Mulai bermain
                        </button>
                    </div>
                </div>
            </form>
        </div>
    );
}


function GroupChip({
    label,
    count,
    isActive,
    onClick,
}: {
    label: string;
    count: number;
    isActive: boolean;
    onClick: () => void;
}) {
    return (
        <button
            type="button"
            onClick={onClick}
            aria-pressed={isActive}
            className={cn(
                'inline-flex shrink-0 items-center gap-1.5 rounded-full px-3 py-1.5 text-[10.5px] font-bold transition-all',
                isActive
                    ? 'bg-red text-white shadow-fab'
                    : 'border border-rule/80 bg-surface text-ink/50 hover:border-red/30 hover:text-ink',
            )}
        >
            {label}
            <span
                className={cn(
                    'rounded-full px-1.5 py-px text-[9px] font-bold tabular-nums',
                    isActive
                        ? 'bg-white/20 text-white'
                        : 'bg-canvas text-ink/35',
                )}
            >
                {count}
            </span>
        </button>
    );
}

function pageWindow(page: number, totalPages: number): Array<number | null> {
    if (totalPages <= 7) {
        return Array.from({ length: totalPages }, (_, index) => index + 1);
    }

    const window = new Set<number>([1, totalPages, page]);

    if (page <= 3) {
        window.add(2).add(3).add(4);
    } else if (page >= totalPages - 2) {
        window.add(totalPages - 1).add(totalPages - 2).add(totalPages - 3);
    } else {
        window.add(page - 1).add(page + 1);
    }

    const sorted = [...window]
        .filter((item) => item >= 1 && item <= totalPages)
        .sort((a, b) => a - b);

    const result: Array<number | null> = [];

    sorted.forEach((item, index) => {
        if (index > 0 && item - sorted[index - 1] > 1) {
            result.push(null);
        }

        result.push(item);
    });

    return result;
}

function Pagination({
    page,
    totalPages,
    start,
    end,
    total,
    onChange,
}: {
    page: number;
    totalPages: number;
    start: number;
    end: number;
    total: number;
    onChange: (page: number) => void;
}) {
    const pages = pageWindow(page, totalPages);

    return (
        <nav
            aria-label="Navigasi halaman mapel"
            className="flex min-w-0 items-center justify-center gap-2 sm:gap-3"
        >
            <p className="hidden min-w-0 truncate text-[10px] font-semibold text-ink/40 md:block">
                Menampilkan{' '}
                <b className="font-bold text-ink/70">
                    {start}–{end}
                </b>{' '}
                dari <b className="font-bold text-ink/70">{total}</b> mapel
            </p>

            <span className="text-[9.5px] font-semibold text-ink/40 tabular-nums whitespace-nowrap md:hidden">
                {start}–{end} / {total}
            </span>

            <div className="flex shrink-0 items-center gap-1">
                <button
                    type="button"
                    onClick={() => onChange(page - 1)}
                    disabled={page <= 1}
                    aria-label="Halaman sebelumnya"
                    className="grid h-6 w-6 place-items-center rounded-md bg-surface text-ink/50 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red disabled:pointer-events-none disabled:opacity-35"
                >
                    <ChevronLeftIcon className="h-3 w-3" />
                </button>

                <div className="hidden items-center gap-1 sm:flex">
                    {pages.map((item, index) =>
                        item === null ? (
                            <span
                                key={`gap-${index}`}
                                aria-hidden
                                className="px-1 text-[10px] font-bold text-ink/25"
                            >
                                …
                            </span>
                        ) : (
                            <button
                                key={item}
                                type="button"
                                onClick={() => onChange(item)}
                                aria-label={`Halaman ${item}`}
                                aria-current={
                                    item === page ? 'page' : undefined
                                }
                                className={cn(
                                    'h-6 min-w-6 rounded-md px-1.5 text-[9.5px] font-bold tabular-nums transition-colors',
                                    item === page
                                        ? 'bg-red text-white shadow-fab'
                                        : 'bg-surface text-ink/50 ring-1 ring-rule hover:bg-red-tint hover:text-red',
                                )}
                            >
                                {item}
                            </button>
                        ),
                    )}
                </div>

                <span className="min-w-8 px-0.5 text-center text-[9.5px] font-bold text-ink/55 tabular-nums sm:hidden">
                    {page} / {totalPages}
                </span>

                <button
                    type="button"
                    onClick={() => onChange(page + 1)}
                    disabled={page >= totalPages}
                    aria-label="Halaman berikutnya"
                    className="grid h-6 w-6 place-items-center rounded-md bg-surface text-ink/50 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red disabled:pointer-events-none disabled:opacity-35"
                >
                    <ChevronRightIcon className="h-3 w-3" />
                </button>
            </div>
        </nav>
    );
}

function SubjectCard({
    subject,
    index,
    mode,
    isOpen,
    onSelect,
}: {
    subject: SubjectProp;
    index: number;
    mode: Difficulty;
    isOpen: boolean;
    onSelect: () => void;
}) {
    const hasContent = subject.chapters_count > 0;
    const questions = totalQuestions(subject, mode);
    const isPlayable = hasContent && questions > 0;
    const theme = subjectTheme(subject.color);

    return (
        <button
            type="button"
            onClick={onSelect}
            disabled={!hasContent}
            aria-haspopup={hasContent ? 'dialog' : undefined}
            style={{ animationDelay: `${Math.min(index, 14) * 30}ms` }}
            className={cn(
                'group relative flex min-w-0 animate-rise flex-col overflow-hidden rounded-xl border bg-surface p-3 text-left transition-all duration-300 sm:p-3.5',
                theme.border,
                hasContent
                    ? 'cursor-pointer shadow-card hover:-translate-y-0.5 hover:shadow-lift active:translate-y-0'
                    : 'cursor-default',
                isOpen && 'ring-2 ring-red/20',
            )}
        >
            <span className="relative flex items-start justify-between gap-2">
                <span
                    className={cn(
                        'grid h-9 w-9 shrink-0 place-items-center rounded-lg text-[18px] leading-none transition-transform duration-300 sm:h-10 sm:w-10 sm:text-[20px]',
                        theme.tile,
                        hasContent
                            ? 'group-hover:-rotate-6 group-hover:scale-105'
                            : 'opacity-70',
                    )}
                >
                    {subject.icon ?? '📘'}
                </span>
                <span
                    className={cn(
                        'rounded-full px-1.5 py-0.5 text-[8.5px] font-bold tracking-wide',
                        hasContent
                            ? 'bg-red text-white'
                            : 'bg-ink/[0.04] text-ink/40',
                    )}
                >
                    {hasContent ? `${subject.chapters_count} bab` : 'Segera'}
                </span>
            </span>

            <span className="relative mt-2 flex min-h-0 flex-1 items-center">
                <span
                    className={cn(
                        'line-clamp-2 text-[13px] leading-[1.3] font-bold tracking-[-0.01em] sm:text-[13.5px]',
                        hasContent ? 'text-ink' : 'text-ink/60',
                    )}
                >
                    {subject.name}
                </span>
            </span>

            <span className="relative mt-2 flex items-center justify-between gap-2">
                <span className="flex min-w-0 items-center gap-1.5">
                    <span className="truncate text-[8.5px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                        {subject.group ?? 'Umum'}
                    </span>
                    {hasContent && (
                        <span
                            className={cn(
                                'inline-flex shrink-0 items-center gap-0.5 text-[10px] font-semibold tabular-nums',
                                isPlayable ? 'text-ink/55' : 'text-ink/35',
                            )}
                        >
                            <BoltIcon
                                className={cn(
                                    'h-2.5 w-2.5',
                                    isPlayable ? 'text-red' : 'text-ink/25',
                                )}
                            />
                            {questions} soal
                        </span>
                    )}
                </span>

                {hasContent && (
                    <span className="grid h-6 w-6 shrink-0 place-items-center rounded-full text-red ring-1 ring-red/20 transition-colors duration-300 group-hover:bg-red group-hover:text-white">
                        <ArrowUpRightIcon className="h-3 w-3" />
                    </span>
                )}
            </span>
        </button>
    );
}

function EmptyState({
    onReset,
    isFiltering,
}: {
    onReset: () => void;
    isFiltering: boolean;
}) {
    return (
        <div className="grid min-h-full place-items-center px-4 py-10">
            <div className="w-full max-w-sm rounded-3xl border border-rule bg-surface/80 px-8 py-10 text-center shadow-card backdrop-blur">
                <span className="mx-auto grid h-14 w-14 place-items-center rounded-2xl bg-red-tint text-red ring-1 ring-red/10">
                    <SearchIcon className="h-6 w-6" />
                </span>
                <p className="mt-3 text-[16px] font-bold text-ink">
                    Materi tidak ditemukan
                </p>
                <p className="mx-auto mt-1 max-w-sm text-[11.5px] leading-relaxed text-ink/45">
                    Coba kata kunci lain, ganti jenjang, atau kembali ke semua
                    mata pelajaran.
                </p>
                {isFiltering && (
                    <button
                        type="button"
                        onClick={onReset}
                        className="mt-4 rounded-full bg-red px-4 py-2 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase shadow-fab transition-colors hover:bg-red-deep"
                    >
                        Bersihkan filter
                    </button>
                )}
            </div>
        </div>
    );
}

function ChapterSheet({
    subject,
    mode,
    onModeChange,
    onClose,
}: {
    subject: SubjectProp;
    mode: Difficulty;
    onModeChange: (mode: Difficulty) => void;
    onClose: () => void;
}) {
    const closeRef = useRef<HTMLButtonElement>(null);

    useEffect(() => {
        closeRef.current?.focus();
    }, []);

    useEffect(() => {
        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                onClose();
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    }, [onClose]);

    const materialTotal = subject.chapters.reduce(
        (total, chapter) => total + chapter.materials_count,
        0,
    );
    const theme = subjectTheme(subject.color);

    return (
        <div
            role="dialog"
            aria-modal="true"
            aria-label={`Bab ${subject.name}`}
            className="fixed inset-0 z-40"
        >
            <button
                type="button"
                aria-label="Tutup panel"
                onClick={onClose}
                className="absolute inset-0 animate-veil-in bg-black/45 backdrop-blur-[2px]"
            />

            <div className="absolute inset-y-0 right-0 flex w-full max-w-[480px] animate-sheet-in flex-col overflow-hidden bg-surface shadow-sheet sm:rounded-l-[28px]">
                <div className="relative shrink-0 overflow-hidden border-b border-rule px-5 pt-5 pb-4 sm:px-6">
                    <span
                        aria-hidden
                        className="pointer-events-none absolute -top-16 -right-10 h-44 w-44 rounded-full bg-red/10 opacity-70 blur-3xl"
                    />

                    <div className="relative flex items-start gap-3">
                        <span
                            className={cn(
                                'grid h-12 w-12 shrink-0 place-items-center rounded-2xl text-[24px] leading-none',
                                theme.tile,
                            )}
                        >
                            {subject.icon ?? '📘'}
                        </span>

                        <div className="min-w-0 flex-1">
                            <p className="text-[9.5px] font-bold tracking-[0.16em] text-ink/40 uppercase">
                                {subject.group ?? 'Umum'} ·{' '}
                                {subject.chapters_count} bab · {materialTotal}{' '}
                                materi
                            </p>
                            <h2 className="display mt-1 text-[23px] leading-tight tracking-[-0.015em] text-ink">
                                {subject.name}
                            </h2>
                        </div>

                        <button
                            ref={closeRef}
                            type="button"
                            onClick={onClose}
                            aria-label="Tutup"
                            className="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-canvas text-ink/50 transition-colors hover:bg-red-tint hover:text-red"
                        >
                            <CloseIcon className="h-3.5 w-3.5" />
                        </button>
                    </div>

                    <div
                        role="group"
                        aria-label="Mode permainan"
                        className="relative mt-4 flex items-center gap-1 rounded-xl bg-canvas p-1 ring-1 ring-rule/70"
                    >
                        {MODES.map((item) => {
                            const meta = DIFFICULTY_META[item];
                            const isActive = item === mode;
                            const count = subject.chapters.reduce(
                                (total, chapter) =>
                                    total +
                                    (chapter.assessments.find(
                                        (assessment) =>
                                            assessment.difficulty === item,
                                    )?.questions_count ?? 0),
                                0,
                            );

                            return (
                                <button
                                    key={item}
                                    type="button"
                                    onClick={() => onModeChange(item)}
                                    aria-pressed={isActive}
                                    className={cn(
                                        'flex flex-1 items-center justify-center gap-1.5 rounded-lg px-2 py-1.5 text-[10px] font-bold tracking-[0.04em] uppercase transition-all',
                                        isActive
                                            ? 'bg-red text-white shadow-fab'
                                            : 'text-ink/40 hover:text-ink/65',
                                    )}
                                >
                                    <span
                                        aria-hidden
                                        className={cn(
                                            'h-1.5 w-1.5 rounded-full',
                                            isActive ? 'bg-white/80' : meta.dot,
                                            !isActive && 'opacity-40',
                                        )}
                                    />
                                    {meta.label}
                                    <span
                                        aria-hidden
                                        className={cn(
                                            'text-[9.5px] font-semibold tabular-nums',
                                            isActive
                                                ? 'text-white/60'
                                                : 'text-ink/25',
                                        )}
                                    >
                                        {count}
                                    </span>
                                </button>
                            );
                        })}
                    </div>
                </div>

                <div className="scroll-quiet flex-1 space-y-2.5 overflow-y-auto px-5 py-4 sm:px-6">
                    {subject.chapters.map((chapter, index) => {
                        const assessment = chapter.assessments.find(
                            (item) => item.difficulty === mode,
                        );
                        const meta = DIFFICULTY_META[mode];

                        return (
                            <article
                                key={chapter.id}
                                className="rounded-2xl border border-rule bg-surface p-4 transition-all hover:border-red/25 hover:shadow-card"
                            >
                                <div className="flex items-start gap-3">
                                    <span className="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-canvas font-serif text-[13px] font-semibold tabular-nums text-ink/55 ring-1 ring-rule">
                                        {String(index + 1).padStart(2, '0')}
                                    </span>

                                    <div className="min-w-0 flex-1">
                                        <div className="flex items-center justify-between gap-2">
                                            <p className="truncate text-[9.5px] font-bold tracking-[0.14em] text-red uppercase">
                                                Bab{' '}
                                                {String(index + 1).padStart(
                                                    2,
                                                    '0',
                                                )}
                                                {chapter.code
                                                    ? ` · ${chapter.code}`
                                                    : ''}
                                            </p>
                                            <span
                                                className={cn(
                                                    'shrink-0 rounded-full px-2 py-0.5 text-[9px] font-bold ring-1',
                                                    assessment
                                                        ? meta.className
                                                        : 'bg-canvas text-ink/35 ring-rule',
                                                )}
                                            >
                                                {assessment
                                                    ? `${assessment.questions_count} soal`
                                                    : 'Belum siap'}
                                            </span>
                                        </div>

                                        <h3 className="mt-1 text-[15px] leading-snug font-bold tracking-[-0.01em] text-ink">
                                            {chapter.title}
                                        </h3>

                                        {chapter.description && (
                                            <p className="mt-1 line-clamp-2 text-[11.5px] leading-relaxed text-ink/50">
                                                {chapter.description}
                                            </p>
                                        )}

                                        <div className="mt-2.5 flex flex-wrap items-center justify-between gap-2">
                                            <div className="flex flex-wrap items-center gap-1.5">
                                                <MetaChip
                                                    icon={
                                                        <BookIcon className="h-3 w-3" />
                                                    }
                                                >
                                                    {chapter.materials_count}{' '}
                                                    materi
                                                </MetaChip>
                                                <MetaChip
                                                    icon={
                                                        <ClockIcon className="h-3 w-3" />
                                                    }
                                                >
                                                    {assessment
                                                        ? `${Math.max(
                                                              1,
                                                              Math.round(
                                                                  assessment.duration /
                                                                      60,
                                                              ),
                                                          )} menit`
                                                        : '—'}
                                                </MetaChip>
                                                <MetaChip
                                                    icon={
                                                        <LayersIcon className="h-3 w-3" />
                                                    }
                                                >
                                                    3 tingkat
                                                </MetaChip>
                                            </div>

                                            {assessment && (
                                                <Link
                                                    href={`/main/${assessment.id}`}
                                                    className="inline-flex h-8 shrink-0 items-center gap-1.5 rounded-lg bg-red px-3 text-[10px] font-bold tracking-[0.04em] text-white uppercase shadow-fab transition-all hover:-translate-y-0.5 hover:bg-red-deep"
                                                >
                                                    Main
                                                    <PlayIcon className="h-3 w-3" />
                                                </Link>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            </article>
                        );
                    })}
                </div>

                <div className="flex shrink-0 items-center gap-2 border-t border-rule bg-canvas/60 px-5 py-3 text-[10.5px] font-medium text-ink/45 sm:px-6">
                    <span
                        aria-hidden
                        className="h-1.5 w-1.5 shrink-0 rounded-full bg-red"
                    />
                    Pilih tingkat kesulitan, lalu tekan Main pada bab yang
                    siap. Progres tersimpan otomatis, termasuk saat offline.
                </div>
            </div>
        </div>
    );
}

function MetaChip({ icon, children }: { icon: ReactNode; children: ReactNode }) {
    return (
        <span className="inline-flex items-center gap-1 rounded-full bg-canvas px-2 py-1 text-[9.5px] font-semibold text-ink/45">
            {icon}
            {children}
        </span>
    );
}

function SearchIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.9"
            className={className}
        >
            <circle cx="11" cy="11" r="7" />
            <path d="m20 20-3.5-3.5" strokeLinecap="round" />
        </svg>
    );
}

function ChevronDownIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            className={className}
        >
            <path
                d="m6 9 6 6 6-6"
                strokeLinecap="round"
                strokeLinejoin="round"
            />
        </svg>
    );
}

function ChevronLeftIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            className={className}
        >
            <path
                d="m14 6-6 6 6 6"
                strokeLinecap="round"
                strokeLinejoin="round"
            />
        </svg>
    );
}

function ChevronRightIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            className={className}
        >
            <path
                d="m10 6 6 6-6 6"
                strokeLinecap="round"
                strokeLinejoin="round"
            />
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
            className={className}
        >
            <path
                d="m5 12.5 4.5 4.5L19 7.5"
                strokeLinecap="round"
                strokeLinejoin="round"
            />
        </svg>
    );
}

function SparkleIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="currentColor"
            className={className}
        >
            <path d="M12 2.5c.6 4.6 2.9 6.9 7.5 7.5-4.6.6-6.9 2.9-7.5 7.5-.6-4.6-2.9-6.9-7.5-7.5 4.6-.6 6.9-2.9 7.5-7.5Z" />
            <path d="M19 15.5c.3 2.2 1.3 3.2 3.5 3.5-2.2.3-3.2 1.3-3.5 3.5-.3-2.2-1.3-3.2-3.5-3.5 2.2-.3 3.2-1.3 3.5-3.5Z" />
        </svg>
    );
}

function BoltIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="currentColor"
            className={className}
        >
            <path d="M13.5 2 4 13.6h6.2L9.8 22 20 10.2h-6.6L13.5 2Z" />
        </svg>
    );
}

function ArrowUpRightIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            className={className}
        >
            <path
                d="M7 17 17 7M9 7h8v8"
                strokeLinecap="round"
                strokeLinejoin="round"
            />
        </svg>
    );
}

function BookIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V4H6.5A2.5 2.5 0 0 0 4 6.5v13Z" />
            <path d="M8 7h8M8 11h5" />
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
            strokeWidth="1.8"
            strokeLinecap="round"
            className={className}
        >
            <circle cx="12" cy="12" r="8.5" />
            <path d="M12 7.5V12l3 2" />
        </svg>
    );
}

function LayersIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="m12 3 9 5-9 5-9-5 9-5Z" />
            <path d="m3 13 9 5 9-5" />
        </svg>
    );
}

function CloseIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            className={className}
        >
            <path d="M6 6l12 12M18 6 6 18" strokeLinecap="round" />
        </svg>
    );
}

function GamepadIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.9"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <path d="M7.5 7h9a5 5 0 0 1 4.9 4.1l.6 3.4a3 3 0 0 1-5.4 2.2L15.2 15H8.8l-1.4 1.7a3 3 0 0 1-5.4-2.2l.6-3.4A5 5 0 0 1 7.5 7Z" />
            <path d="M8 10v3M6.5 11.5h3M15.5 11h.01M17.5 12.5h.01" />
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
            <path d="M8 5.5v13a1 1 0 0 0 1.5.86l10-6.5a1 1 0 0 0 0-1.72l-10-6.5A1 1 0 0 0 8 5.5Z" />
        </svg>
    );
}

function UserIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.9"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <circle cx="12" cy="8" r="3.5" />
            <path d="M5 20c0-3.3 3.1-5.5 7-5.5s7 2.2 7 5.5" />
        </svg>
    );
}

function UsersIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.9"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={className}
        >
            <circle cx="9" cy="8.5" r="3" />
            <path d="M3 19.5c0-3 2.7-5 6-5s6 2 6 5" />
            <path d="M16 5.7a3 3 0 0 1 0 5.6M17.5 14.9c2.1.6 3.5 2.3 3.5 4.6" />
        </svg>
    );
}

function PlusIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.2"
            strokeLinecap="round"
            className={className}
        >
            <path d="M12 5v14M5 12h14" />
        </svg>
    );
}
