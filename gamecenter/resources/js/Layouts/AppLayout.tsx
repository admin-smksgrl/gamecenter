import { Link, router, usePage } from '@inertiajs/react';
import { useEffect, useRef, useState } from 'react';
import type { PropsWithChildren, ReactNode } from 'react';

import ToastHub from '@/Components/Toast/ToastHub';
import { useOfflineSync } from '@/Hooks/useOfflineSync';
import { friendlySyncError } from '@/lib/friendly-error';
import { offlineDb } from '@/lib/offline/offline-db';
import { toast } from '@/lib/toast';
import { useTheme } from '@/lib/useTheme';
import { cn, formatDateId, formatNumber } from '@/lib/utils';
import type { AuthUser, PageProps } from '@/types';

interface AppLayoutProps extends PropsWithChildren {
    nav?: ReactNode;
    play?: ReactNode;
    footerCenter?: ReactNode;
    onSearch?: () => void;
    levelTheme?: string;
}

export default function AppLayout({
    children,
    nav,
    play,
    footerCenter,
    onSearch,
    levelTheme,
}: AppLayoutProps) {
    const { auth, version } = usePage<PageProps>().props;
    const user = auth.user;

    // Halaman tanpa `levelTheme` (mis. panduan) tetap memakai warna jenjang
    // pengguna, bukan warna dasar, supaya tidak ada warna lain yang menyelinap.
    const themeKey = levelTheme ?? user?.level_theme ?? 'default';
    const { theme, toggleTheme } = useTheme();
    const sync = useOfflineSync(Boolean(user));

    const lastSyncError = useRef<string | null>(null);

    // Warna bilah peramban mengikuti jenjang yang sedang dibuka, termasuk
    // saat pengguna berpindah jenjang tanpa mengubah mode terang/gelap.
    useEffect(() => {
        const levelRoot = document.querySelector('[data-level-theme]');

        if (!levelRoot) {
            return;
        }

        const accent = getComputedStyle(levelRoot)
            .getPropertyValue('--color-red')
            .trim();

        const dark = document.documentElement.classList.contains('dark');

        document
            .querySelector('meta[name="theme-color"]')
            ?.setAttribute('content', dark ? '#0e0c0d' : accent || '#e60012');
    }, [themeKey]);

    useEffect(() => {
        if (!sync.lastError) {
            lastSyncError.current = null;

            return;
        }

        if (lastSyncError.current === sync.lastError) {
            return;
        }

        lastSyncError.current = sync.lastError;

        const friendly = friendlySyncError(sync.lastError);
        toast.warning(friendly.title, friendly.description);
    }, [sync.lastError]);

    const initials = user
        ? user.name
              .split(' ')
              .filter(Boolean)
              .slice(0, 2)
              .map((part) => part[0])
              .join('')
              .toUpperCase()
        : '';

    return (
        <div
            data-level-theme={themeKey}
            className="dot-grid relative flex h-dvh flex-col overflow-hidden bg-canvas text-ink"
        >
            <div
                aria-hidden
                className="pointer-events-none absolute inset-0 overflow-hidden"
            >
                <div className="absolute -top-40 -left-28 h-96 w-96 rounded-full bg-red/[0.06] blur-3xl" />
                <div className="absolute top-24 -right-40 h-[28rem] w-[28rem] rounded-full bg-ink/[0.05] blur-3xl" />
                <div className="absolute -bottom-48 left-1/3 h-[24rem] w-[24rem] rounded-full bg-red/[0.04] blur-3xl" />
            </div>

            <header className="relative z-30 shrink-0 border-b border-rule bg-surface">
                <div aria-hidden className="h-[3px] bg-red" />

                <div className="flex flex-wrap items-center gap-x-3 gap-y-1.5 px-3 py-2 sm:px-5 lg:h-16 lg:flex-nowrap lg:py-0">
                    <Link href="/" className="group flex items-center gap-2.5">
                        <span className="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-red text-white shadow-[0_8px_18px_-12px_var(--level-glow-strong)] ring-1 ring-white/15 transition-transform duration-300 group-hover:-rotate-6 group-hover:scale-105">
                            <CapIcon className="h-5 w-5" />
                        </span>
                        <span className="flex flex-col leading-none">
                            <span className="text-[16px] font-bold tracking-[-0.01em] text-ink">
                                Ruang Belajar
                            </span>
                            <span className="mt-1 text-[8.5px] font-bold tracking-[0.24em] text-ink/40 uppercase">
                                Game Center
                            </span>
                        </span>
                    </Link>

                    <div className="order-last flex w-full min-w-0 items-center gap-0.5 sm:gap-1 lg:order-none lg:w-auto lg:flex-1 lg:pl-3">
                        {nav}
                        {nav && (
                            <Link
                                href="/panduan"
                                aria-label="Panduan"
                                title="Panduan"
                                className="inline-flex h-8 shrink-0 items-center gap-1.5 rounded-lg px-2 text-[10.5px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-red hover:ring-red/40 lg:hidden"
                            >
                                <BookIcon className="h-3.5 w-3.5" />
                                <span className="hidden sm:inline">Panduan</span>
                            </Link>
                        )}
                    </div>

                    <div className="ml-auto flex items-center gap-1.5 sm:gap-2">
                        {play}

                        <Link
                            href="/panduan"
                            aria-label="Panduan"
                            title="Panduan"
                            className={`${
                                nav ? 'hidden lg:inline-flex' : 'inline-flex'
                            } h-9 shrink-0 items-center gap-1.5 rounded-lg px-2.5 text-[10.5px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-red hover:ring-red/40`}
                        >
                            <BookIcon className="h-4 w-4" />
                            <span
                                className={
                                    nav ? 'hidden xl:inline' : 'hidden sm:inline'
                                }
                            >
                                Panduan
                            </span>
                        </Link>

                        <button
                            type="button"
                            onClick={toggleTheme}
                            aria-label={
                                theme === 'dark'
                                    ? 'Aktifkan mode terang'
                                    : 'Aktifkan mode gelap'
                            }
                            title={
                                theme === 'dark'
                                    ? 'Mode terang'
                                    : 'Mode gelap'
                            }
                            className="grid h-9 w-9 shrink-0 place-items-center rounded-lg text-ink/60 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red"
                        >
                            {theme === 'dark' ? (
                                <SunIcon className="h-4 w-4" />
                            ) : (
                                <MoonIcon className="h-4 w-4" />
                            )}
                        </button>

                        {onSearch && (
                            <button
                                type="button"
                                onClick={onSearch}
                                aria-label="Cari mata pelajaran"
                                className="grid h-9 w-9 shrink-0 place-items-center rounded-lg text-ink/60 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red"
                            >
                                <SearchIcon className="h-4 w-4" />
                            </button>
                        )}

                        {user ? (
                            <>
                                <span className="hidden h-8 items-center gap-1.5 rounded-full border border-rule bg-surface px-2.5 text-[11px] font-bold tabular-nums text-ink sm:inline-flex">
                                    <CoinIcon className="h-3.5 w-3.5 text-red" />
                                    {formatNumber(user.coins)}
                                </span>

                                <span className="hidden h-8 items-center gap-1.5 rounded-full border border-rule bg-surface px-2.5 text-[11px] font-bold tabular-nums text-ink sm:inline-flex">
                                    <BoltIcon className="h-3.5 w-3.5 text-red" />
                                    {formatNumber(user.xp)}
                                    <span className="text-[8.5px] font-bold tracking-[0.1em] text-ink/35">
                                        XP
                                    </span>
                                </span>

                                <UserMenu user={user} initials={initials} />
                            </>
                        ) : (
                            <>
                                <Link
                                    href="/daftar"
                                    className="hidden h-8 items-center rounded-lg px-2.5 text-[10px] font-bold tracking-[0.1em] text-ink/55 uppercase ring-1 ring-rule transition-colors hover:text-red hover:ring-red/40 sm:inline-flex"
                                >
                                    Daftar
                                </Link>
                                <Link
                                    href="/masuk"
                                    aria-label="Masuk"
                                    title="Masuk"
                                    className="inline-flex h-9 shrink-0 items-center gap-1.5 rounded-lg bg-red px-2.5 text-[10.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                >
                                    <UserIcon className="h-3.5 w-3.5" />
                                    <span className="hidden sm:inline">Masuk</span>
                                </Link>
                            </>
                        )}
                    </div>
                </div>
            </header>

            <div className="relative z-10 flex min-h-0 flex-1 flex-col">
                {children}
            </div>

            <footer className="relative z-10 grid shrink-0 grid-cols-[1fr_auto_1fr] items-center gap-2 border-t border-rule bg-surface px-3 py-1.5 text-[9.5px] font-semibold tracking-[0.02em] text-ink/40 sm:gap-3 sm:px-5">
                <span className="min-w-0 justify-self-start truncate whitespace-nowrap">
                    <span className="hidden sm:inline">Ruang belajar </span>
                    <b className="font-bold text-ink/65 tabular-nums">
                        v.{version}
                    </b>
                    <SyncStatus
                        sync={sync}
                        canSync={Boolean(user)}
                    />
                </span>

                <div className="flex min-w-0 items-center justify-center">
                    {footerCenter}
                </div>

                <span className="col-start-3 min-w-0 justify-self-end truncate text-right whitespace-nowrap">
                    <span className="hidden sm:inline">
                        created &amp; developed by{' '}
                    </span>
                    <span className="sm:hidden">by </span>
                    <b className="font-bold text-red">haraki</b>
                </span>
            </footer>

            <ToastHub />
        </div>
    );
}

function SyncStatus({
    sync,
    canSync,
}: {
    sync: ReturnType<typeof useOfflineSync>;
    canSync: boolean;
}) {
    const { online, syncing, pending, lastError } = sync;

    let label: string | null = null;
    let tone = 'text-ink/45';
    let dot = 'bg-ink/25';

    if (!online) {
        label = pending > 0 ? `Offline · ${pending}` : 'Offline';
        tone = 'text-red';
        dot = 'bg-red';
    } else if (syncing) {
        label = 'Menyinkronkan…';
        tone = 'text-red';
        dot = 'animate-pulse bg-red';
    } else if (pending > 0) {
        label = `${pending} tersimpan`;
        tone = 'text-red';
        dot = 'bg-red';
    } else if (lastError) {
        label = 'Sinkron tertunda';
        dot = 'bg-ink/35';
    }

    if (label === null) {
        return null;
    }

    return (
        <span
            role="status"
            aria-live="polite"
            className="ml-1.5 inline-flex items-center gap-1 align-middle"
        >
            <span
                aria-hidden
                className={cn('h-1.5 w-1.5 shrink-0 rounded-full', dot)}
            />
            <button
                type="button"
                disabled={!canSync || !online || syncing || pending === 0}
                onClick={() => {
                    void sync.syncNow();
                }}
                title={
                    canSync
                        ? 'Klik untuk menyinkronkan data tersimpan'
                        : 'Masuk untuk menyinkronkan data'
                }
                className={cn(
                    'underline-offset-2 transition-colors hover:underline disabled:cursor-default disabled:no-underline',
                    tone,
                )}
            >
                {label}
            </button>
        </span>
    );
}

function UserMenu({ user, initials }: { user: AuthUser; initials: string }) {
    const [open, setOpen] = useState(false);
    const rootRef = useRef<HTMLSpanElement>(null);

    useEffect(() => {
        if (!open) {
            return;
        }

        function handlePointer(event: PointerEvent) {
            if (
                rootRef.current &&
                event.target instanceof Node &&
                !rootRef.current.contains(event.target)
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

    const membership = user.membership;
    const isPaid = membership.tier !== 'free' && membership.status === 'active';
    const canAccessPanel = user.role === 'admin' || user.role === 'teacher';

    const itemClass =
        'flex items-center gap-2.5 rounded-lg px-2.5 py-1.5 text-[11.5px] font-semibold text-ink/65 transition-colors hover:bg-canvas hover:text-ink';

    function logout() {
        setOpen(false);
        void offlineDb.clearUserData().catch(() => undefined);
        router.post('/keluar');
    }

    return (
        <span ref={rootRef} className="relative ml-0.5 shrink-0">
            <button
                type="button"
                aria-label={`Menu akun ${user.name}`}
                aria-haspopup="menu"
                aria-expanded={open}
                onClick={() => setOpen((isOpen) => !isOpen)}
                className="relative grid h-9 w-9 shrink-0 place-items-center rounded-full bg-red text-[10.5px] font-bold text-white ring-2 ring-red-tint transition-transform hover:scale-105"
            >
                {initials || '·'}
                <span className="absolute -right-1 -bottom-1 rounded-full bg-ink px-1 py-px text-[8px] leading-tight font-black text-surface ring-2 ring-surface">
                    {user.level}
                </span>
            </button>

            {open && (
                <div
                    role="menu"
                    aria-label="Menu akun"
                    className="absolute top-[calc(100%+8px)] right-0 z-50 w-64 rounded-xl border border-rule bg-surface p-1 shadow-sheet"
                >
                    <div className="border-b border-rule/70 px-2.5 pt-1.5 pb-2">
                        <p className="truncate text-[12.5px] font-bold text-ink">
                            {user.name}
                        </p>
                        <p className="truncate text-[10px] font-medium text-ink/40">
                            @{user.username}
                        </p>
                        <div className="mt-1.5 flex flex-wrap items-center gap-1.5">
                            <span className="inline-flex items-center gap-1 rounded-full bg-red-tint px-2 py-0.5 text-[8.5px] font-bold tracking-[0.08em] text-red uppercase">
                                {isPaid ? membership.plan_name : 'Paket gratis'}
                            </span>
                            {isPaid && membership.ends_at && (
                                <span className="text-[9px] font-medium text-ink/35">
                                    s.d. {formatDateId(membership.ends_at)}
                                </span>
                            )}
                        </div>
                    </div>

                    <Link
                        href="/keanggotaan"
                        role="menuitem"
                        onClick={() => setOpen(false)}
                        className={`mt-1 ${itemClass}`}
                    >
                        <CardIcon
                            className={`h-3.5 w-3.5 ${
                                isPaid ? 'text-ink/40' : 'text-red'
                            }`}
                        />
                        <span className="flex-1">
                            {isPaid ? 'Keanggotaan' : 'Upgrade keanggotaan'}
                        </span>
                        {!isPaid && (
                            <span className="h-1.5 w-1.5 rounded-full bg-red" />
                        )}
                    </Link>

                    <Link
                        href="/progres"
                        role="menuitem"
                        onClick={() => setOpen(false)}
                        className={itemClass}
                    >
                        <ChartIcon className="h-3.5 w-3.5 text-ink/40" />
                        Progres &amp; lencana
                    </Link>

                    <Link
                        href="/panduan"
                        role="menuitem"
                        onClick={() => setOpen(false)}
                        className={itemClass}
                    >
                        <BookIcon className="h-3.5 w-3.5 text-ink/40" />
                        Panduan
                    </Link>

                    {canAccessPanel && (
                        <a href="/admin" role="menuitem" className={itemClass}>
                            <GearIcon className="h-3.5 w-3.5 text-ink/40" />
                            {user.role === 'admin' ? 'Panel admin' : 'Panel guru'}
                        </a>
                    )}

                    <div className="my-1 h-px bg-rule/70" />

                    <button
                        type="button"
                        role="menuitem"
                        onClick={logout}
                        className="flex w-full items-center gap-2.5 rounded-lg px-2.5 py-1.5 text-left text-[11.5px] font-semibold text-red transition-colors hover:bg-red-tint"
                    >
                        <LogoutIcon className="h-3.5 w-3.5" />
                        Keluar
                    </button>
                </div>
            )}
        </span>
    );
}

function ChartIcon({ className }: { className?: string }) {
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
            <path d="M4 20V4" />
            <path d="M4 20h16" />
            <path d="M8 16v-4M12.5 16V8M17 16v-6" />
        </svg>
    );
}

function CapIcon({ className }: { className?: string }) {
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
            <path d="M22 10 12 5 2 10l10 5 10-5Z" />
            <path d="M6 12v4.5c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V12" />
            <path d="M22 10v5" />
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

function CoinIcon({ className }: { className?: string }) {
    return (
        <svg
            aria-hidden
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            className={className}
        >
            <circle cx="12" cy="12" r="8.5" />
            <path
                d="M12 8.5v7M10 10.2h2.6a1.5 1.5 0 0 1 0 3H10.8a1.5 1.5 0 0 0 0 3H13"
                strokeLinecap="round"
            />
        </svg>
    );
}

function MoonIcon({ className }: { className?: string }) {
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
            <path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8Z" />
        </svg>
    );
}

function SunIcon({ className }: { className?: string }) {
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
            <circle cx="12" cy="12" r="4.2" />
            <path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4" />
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
            <circle cx="12" cy="8" r="3.6" />
            <path d="M4.5 20a7.5 7.5 0 0 1 15 0" />
        </svg>
    );
}

function CardIcon({ className }: { className?: string }) {
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
            <rect x="3" y="5.5" width="18" height="13" rx="2.5" />
            <path d="M3 9.5h18M7 15h3" />
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
            <path d="M4.5 5.5A2.5 2.5 0 0 1 7 3h12.5v16H7a2.5 2.5 0 0 0-2.5 2.5V5.5Z" />
            <path d="M4.5 5.5v13M8 7h7M8 10.5h5" />
        </svg>
    );
}

function GearIcon({ className }: { className?: string }) {
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
            <circle cx="12" cy="12" r="3.2" />
            <path d="M19.4 15a1.7 1.7 0 0 0 .34 1.87l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06A1.7 1.7 0 0 0 15 19.4a1.7 1.7 0 0 0-1 1.55V21a2 2 0 1 1-4 0v-.09a1.7 1.7 0 0 0-1.11-1.55 1.7 1.7 0 0 0-1.87.34l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.7 1.7 0 0 0 4.6 15a1.7 1.7 0 0 0-1.55-1H3a2 2 0 1 1 0-4h.09A1.7 1.7 0 0 0 4.6 8.89a1.7 1.7 0 0 0-.34-1.87l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.7 1.7 0 0 0 9 4.6a1.7 1.7 0 0 0 1-1.55V3a2 2 0 1 1 4 0v.09a1.7 1.7 0 0 0 1 1.55 1.7 1.7 0 0 0 1.87-.34l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.7 1.7 0 0 0 19.4 9c.16.38.25.79.25 1.2 0 .32-.05.64-.15.94Z" />
        </svg>
    );
}

function LogoutIcon({ className }: { className?: string }) {
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
            <path d="M9 4H6.5A2.5 2.5 0 0 0 4 6.5v11A2.5 2.5 0 0 0 6.5 20H9" />
            <path d="M14 8l4 4-4 4M18 12H9" />
        </svg>
    );
}
