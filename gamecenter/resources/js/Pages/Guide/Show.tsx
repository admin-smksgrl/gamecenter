import { Head, Link } from '@inertiajs/react';
import { useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';

import AppLayout from '@/Layouts/AppLayout';
import {
    GUIDE_GROUPS,
    GUIDE_PAGES,
    findGuidePage,
    guideNeighbours,
} from '@/Guide/pages';
import type { GuidePage } from '@/Guide/pages';
import { cn } from '@/lib/utils';

interface GuideProps {
    page: string;
}

function matchesQuery(page: GuidePage, term: string): boolean {
    if (term === '') {
        return true;
    }

    const haystack = [
        page.title,
        page.summary,
        page.group,
        ...page.keywords,
    ]
        .join(' ')
        .toLowerCase();

    return haystack.includes(term);
}

export default function GuideShow({ page }: GuideProps) {
    const current = findGuidePage(page);
    const active = current ?? GUIDE_PAGES[0];
    const notFound = current === null;
    const [query, setQuery] = useState('');
    const [drawerOpen, setDrawerOpen] = useState(false);
    const mainRef = useRef<HTMLDivElement>(null);

    const term = query.trim().toLowerCase();
    const neighbours = guideNeighbours(active.slug);

    const resultCount = useMemo(
        () => GUIDE_PAGES.filter((item) => matchesQuery(item, term)).length,
        [term],
    );

    useEffect(() => {
        mainRef.current?.scrollTo({ top: 0 });
        setDrawerOpen(false);
        setQuery('');
    }, [active.slug]);

    useEffect(() => {
        if (!drawerOpen) {
            return;
        }

        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                setDrawerOpen(false);
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    }, [drawerOpen]);

    return (
        <AppLayout>
            <Head
                title={
                    notFound ? 'Topik tidak ditemukan' : `${active.title} — Panduan`
                }
            />

            <div className="flex min-h-0 flex-1">
                <aside className="no-bar hidden w-60 shrink-0 overflow-y-auto border-r border-rule bg-surface/55 lg:block xl:w-64">
                    <div className="px-3 py-4">
                        <GuideSidebar
                            activeSlug={current?.slug ?? null}
                            query={query}
                            onQueryChange={setQuery}
                            resultCount={resultCount}
                        />
                    </div>
                </aside>

                <div
                    ref={mainRef}
                    className="no-bar min-h-0 flex-1 overflow-y-auto"
                >
                    <div className="mx-auto flex w-full max-w-6xl gap-7 px-3 py-4 sm:px-5 sm:py-6 lg:gap-9 lg:px-7">
                        <article className="min-w-0 flex-1">
                            <div className="flex items-center gap-2 lg:hidden">
                                <button
                                    type="button"
                                    onClick={() => setDrawerOpen(true)}
                                    className="inline-flex h-8 shrink-0 items-center gap-1.5 rounded-lg border border-rule bg-surface px-2.5 text-[10.5px] font-bold text-ink/65 transition-colors hover:text-red"
                                >
                                    <ListIcon className="h-3.5 w-3.5" />
                                    Daftar panduan
                                </button>
                                <span className="min-w-0 truncate text-[9.5px] font-semibold text-ink/30">
                                    Panduan /{' '}
                                    {notFound
                                        ? 'Topik tidak ditemukan'
                                        : active.title}
                                </span>
                            </div>

                            <div className="mt-3 flex flex-wrap items-center gap-1.5 text-[9px] font-bold tracking-[0.1em] text-ink/30 uppercase lg:mt-0">
                                <Link
                                    href="/panduan"
                                    className="transition-colors hover:text-red"
                                >
                                    Panduan
                                </Link>
                                <span aria-hidden>/</span>
                                <span>
                                    {notFound ? 'Tidak ditemukan' : active.group}
                                </span>
                            </div>

                            <h1 className="display mt-2 text-[26px] leading-[1.1] text-ink sm:text-[32px]">
                                {notFound ? 'Topik tidak ditemukan' : active.title}
                            </h1>
                            <p className="mt-1.5 max-w-2xl text-[11.5px] leading-relaxed font-medium text-ink/50 sm:text-[12px]">
                                {notFound
                                    ? 'Halaman yang kamu cari tidak tersedia di panduan. Pilih topik lain dari daftar.'
                                    : active.summary}
                            </p>
                            {!notFound && (
                                <div className="mt-2.5 flex flex-wrap items-center gap-1.5">
                                    <span className="inline-flex items-center gap-1 rounded-full bg-red-tint px-2 py-0.5 text-[8.5px] font-bold tracking-[0.08em] text-red uppercase">
                                        {active.group}
                                    </span>
                                    <span className="text-[9px] font-semibold text-ink/30">
                                        Diperbarui {active.updated}
                                    </span>
                                </div>
                            )}

                            {notFound ? (
                                <div className="mt-5 rounded-xl border border-red/25 bg-red-tint/60 px-3.5 py-3 text-[11.5px] leading-relaxed text-ink/65">
                                    <p>
                                        Topik{' '}
                                        <code className="rounded border border-rule bg-surface px-1 py-0.5 font-mono text-[10px] text-ink/70">
                                            {page}
                                        </code>{' '}
                                        tidak ada. Kembali ke{' '}
                                        <Link
                                            href="/panduan"
                                            className="font-bold text-red underline underline-offset-2"
                                        >
                                            pengenalan panduan
                                        </Link>
                                        .
                                    </p>
                                </div>
                            ) : (
                                <div className="guide-prose mt-5">
                                    {active.content}
                                </div>
                            )}

                            <nav
                                aria-label="Navigasi topik"
                                className="mt-7 grid gap-2 border-t border-rule pt-4 sm:grid-cols-2"
                            >
                                {neighbours.previous ? (
                                    <Link
                                        href={`/panduan/${neighbours.previous.slug}`}
                                        className="group rounded-xl border border-rule bg-surface px-3 py-2.5 transition-colors hover:border-red/30 hover:bg-red-tint/35"
                                    >
                                        <span className="text-[8.5px] font-bold tracking-[0.14em] text-ink/30 uppercase">
                                            Sebelumnya
                                        </span>
                                        <span className="mt-0.5 flex items-center gap-1.5 text-[11.5px] font-bold text-ink group-hover:text-red">
                                            <span aria-hidden>←</span>
                                            {neighbours.previous.title}
                                        </span>
                                    </Link>
                                ) : (
                                    <span aria-hidden />
                                )}

                                {neighbours.next ? (
                                    <Link
                                        href={`/panduan/${neighbours.next.slug}`}
                                        className="group rounded-xl border border-rule bg-surface px-3 py-2.5 text-right transition-colors hover:border-red/30 hover:bg-red-tint/35"
                                    >
                                        <span className="text-[8.5px] font-bold tracking-[0.14em] text-ink/30 uppercase">
                                            Selanjutnya
                                        </span>
                                        <span className="mt-0.5 flex items-center justify-end gap-1.5 text-[11.5px] font-bold text-ink group-hover:text-red">
                                            {neighbours.next.title}
                                            <span aria-hidden>→</span>
                                        </span>
                                    </Link>
                                ) : (
                                    <span aria-hidden />
                                )}
                            </nav>
                        </article>

                        <aside className="hidden w-48 shrink-0 xl:block">
                            <div className="sticky top-0">
                                {!notFound && (
                                    <>
                                        <p className="text-[8.5px] font-bold tracking-[0.16em] text-ink/30 uppercase">
                                            Di halaman ini
                                        </p>
                                        <ul className="mt-2 grid gap-1 border-l border-rule pl-2.5">
                                            {active.headings.map((heading) => (
                                                <li key={heading.id}>
                                                    <a
                                                        href={`#${heading.id}`}
                                                        className="block py-0.5 text-[10px] leading-snug font-semibold text-ink/45 transition-colors hover:text-red"
                                                    >
                                                        {heading.label}
                                                    </a>
                                                </li>
                                            ))}
                                        </ul>
                                    </>
                                )}
                                <div
                                    className={`rounded-xl border border-rule bg-surface p-2.5 ${
                                        notFound ? '' : 'mt-4'
                                    }`}
                                >
                                    <p className="text-[9.5px] font-bold text-ink/60">
                                        Butuh bantuan lain?
                                    </p>
                                    <p className="mt-1 text-[9px] leading-relaxed font-medium text-ink/40">
                                        Baca masalah umum atau hubungi
                                        guru/admin sekolahmu.
                                    </p>
                                    <Link
                                        href="/panduan/masalah-umum"
                                        className="mt-2 inline-flex text-[9.5px] font-bold text-red hover:underline"
                                    >
                                        Buka masalah umum →
                                    </Link>
                                </div>
                            </div>
                        </aside>
                    </div>
                </div>
            </div>

            {drawerOpen &&
                createPortal(
                    <div className="fixed inset-0 z-[60] lg:hidden">
                        <button
                            type="button"
                            aria-label="Tutup daftar panduan"
                            onClick={() => setDrawerOpen(false)}
                            className="animate-veil-in absolute inset-0 bg-black/45"
                        />
                        <div className="animate-sheet-left absolute inset-y-0 left-0 w-[min(84vw,19rem)] overflow-hidden border-r border-rule bg-surface shadow-[24px_0_60px_-32px_rgb(0_0_0_/_0.55)]">
                            <div className="flex h-full flex-col">
                                <div className="flex items-center justify-between gap-2 border-b border-rule px-3 py-2.5">
                                    <div>
                                        <p className="text-[12.5px] font-bold text-ink">
                                            Daftar panduan
                                        </p>
                                        <p className="text-[9px] font-medium text-ink/35">
                                            {GUIDE_PAGES.length} topik bantuan
                                        </p>
                                    </div>
                                    <button
                                        type="button"
                                        onClick={() => setDrawerOpen(false)}
                                        aria-label="Tutup"
                                        className="grid h-8 w-8 place-items-center rounded-lg text-ink/50 ring-1 ring-rule hover:text-red"
                                    >
                                        <CloseIcon className="h-4 w-4" />
                                    </button>
                                </div>
                                <div className="no-bar min-h-0 flex-1 overflow-y-auto p-3">
                                    <GuideSidebar
                                        activeSlug={current?.slug ?? null}
                                        query={query}
                                        onQueryChange={setQuery}
                                        resultCount={resultCount}
                                        onNavigate={() => setDrawerOpen(false)}
                                    />
                                </div>
                            </div>
                        </div>
                    </div>,
                    document.body,
                )}
        </AppLayout>
    );
}

interface GuideSidebarProps {
    activeSlug: string | null;
    query: string;
    onQueryChange: (value: string) => void;
    resultCount: number;
    onNavigate?: () => void;
}

function GuideSidebar({
    activeSlug,
    query,
    onQueryChange,
    resultCount,
    onNavigate,
}: GuideSidebarProps) {
    const term = query.trim().toLowerCase();

    return (
        <div className="flex flex-col">
            <div className="flex items-center gap-2 px-1">
                <span className="grid h-7 w-7 place-items-center rounded-lg bg-red text-white">
                    <BookIcon className="h-4 w-4" />
                </span>
                <div>
                    <p className="text-[12px] font-bold text-ink">Panduan</p>
                    <p className="text-[8.5px] font-bold tracking-[0.14em] text-ink/30 uppercase">
                        Pusat bantuan
                    </p>
                </div>
            </div>

            <label className="relative mt-3 block">
                <span className="sr-only">Cari topik panduan</span>
                <SearchIcon className="pointer-events-none absolute top-1/2 left-2.5 h-3.5 w-3.5 -translate-y-1/2 text-ink/30" />
                <input
                    type="search"
                    value={query}
                    onChange={(event) => onQueryChange(event.target.value)}
                    placeholder="Cari topik…"
                    className="h-8 w-full rounded-lg border border-rule bg-canvas/70 pr-2.5 pl-8 text-[16px] font-medium text-ink placeholder:text-ink/30 focus:border-red/40 focus:ring-2 focus:ring-red/10 focus:outline-none lg:text-[10.5px]"
                />
            </label>

            <nav aria-label="Topik panduan" className="mt-3 grid gap-3">
                {GUIDE_GROUPS.map((group) => {
                    const pages = GUIDE_PAGES.filter(
                        (page) =>
                            page.group === group && matchesQuery(page, term),
                    );

                    if (pages.length === 0) {
                        return null;
                    }

                    return (
                        <div key={group}>
                            <p className="px-1.5 text-[8.5px] font-bold tracking-[0.16em] text-ink/30 uppercase">
                                {group}
                            </p>
                            <ul className="mt-1 grid gap-0.5">
                                {pages.map((page) => {
                                    const isActive = page.slug === activeSlug;

                                    return (
                                        <li key={page.slug}>
                                            <Link
                                                href={`/panduan/${page.slug}`}
                                                onClick={onNavigate}
                                                aria-current={
                                                    isActive ? 'page' : undefined
                                                }
                                                className={cn(
                                                    'flex items-center gap-2 rounded-lg px-2 py-1.5 text-[10.5px] leading-snug font-semibold transition-colors',
                                                    isActive
                                                        ? 'bg-red-tint text-red'
                                                        : 'text-ink/55 hover:bg-canvas hover:text-ink',
                                                )}
                                            >
                                                <span
                                                    className={cn(
                                                        'h-1 w-1 shrink-0 rounded-full',
                                                        isActive
                                                            ? 'bg-red'
                                                            : 'bg-ink/20',
                                                    )}
                                                />
                                                <span className="min-w-0">
                                                    {page.title}
                                                </span>
                                            </Link>
                                        </li>
                                    );
                                })}
                            </ul>
                        </div>
                    );
                })}

                {resultCount === 0 && (
                    <p className="rounded-lg bg-canvas/70 px-2.5 py-3 text-center text-[10px] font-medium text-ink/40">
                        Tidak ada topik yang cocok dengan “{query.trim()}”.
                    </p>
                )}
            </nav>
        </div>
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
            <path d="M4.5 5.5A2.5 2.5 0 0 1 7 3h12.5v16H7a2.5 2.5 0 0 0-2.5 2.5V5.5Z" />
            <path d="M4.5 5.5v13M8 7h7M8 10.5h5" />
        </svg>
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

function ListIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.9"
            strokeLinecap="round"
            className={className}
        >
            <path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01" />
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
            strokeLinecap="round"
            className={className}
        >
            <path d="m6 6 12 12M18 6 6 18" />
        </svg>
    );
}
