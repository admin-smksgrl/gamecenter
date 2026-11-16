import { Head, Link, useForm } from '@inertiajs/react';
import type { FormEvent } from 'react';

import AppLayout from '@/Layouts/AppLayout';
import { firstValidationMessage } from '@/lib/friendly-error';
import { toast } from '@/lib/toast';

const INPUT =
    'h-9 w-full rounded-lg border border-rule bg-canvas px-2.5 text-[16px] leading-6 font-medium text-ink outline-none transition-colors placeholder:text-ink/35 focus:border-red/60 focus:ring-2 focus:ring-red/15 sm:h-8 sm:text-[12.5px] sm:leading-5';

const LABEL = 'sr-only';

const ERROR = 'mt-0.5 text-[9.5px] font-semibold text-red';

export default function Login({ redirect }: { redirect?: string | null }) {
    const form = useForm({
        login: '',
        password: '',
        remember: false,
    });

    const registerHref = redirect
        ? `/daftar?redirect=${encodeURIComponent(redirect)}`
        : '/daftar';

    function submit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        form.post(
            redirect
                ? `/masuk?redirect=${encodeURIComponent(redirect)}`
                : '/masuk',
            {
                onFinish: () => form.reset('password'),
                onError: (errors) => {
                    toast.error(
                        'Belum bisa masuk',
                        firstValidationMessage(errors) ??
                            'Periksa kembali email/username dan kata sandi, lalu coba lagi.',
                    );
                },
            },
        );
    }

    return (
        <>
            <Head title="Masuk" />

            <AppLayout>
                <div className="no-bar min-h-0 flex-1 overflow-y-auto">
                    <div className="mx-auto flex min-h-full w-full max-w-3xl items-center px-3 py-4 sm:px-5 sm:py-6">
                        <div className="grid w-full gap-4 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:gap-8">
                            <section className="hidden lg:block">
                                <span className="inline-flex items-center gap-1.5 rounded-full bg-red-tint px-2.5 py-1 text-[9.5px] font-bold tracking-[0.16em] text-red uppercase">
                                    Masuk
                                </span>
                                <h1 className="display mt-2.5 text-[clamp(26px,2.8vw,36px)] leading-[1.04] text-ink">
                                    Lanjutkan{' '}
                                    <span className="italic text-red">
                                        petualangan
                                    </span>{' '}
                                    belajarmu.
                                </h1>
                                <p className="mt-2.5 max-w-sm text-[11.5px] font-medium text-ink/45">
                                    Masuk untuk menyimpan XP dan koin,
                                    mengajukan paket keanggotaan, dan mengikuti
                                    kelas dari gurumu.
                                </p>

                                <ul className="mt-4 flex flex-col gap-1.5">
                                    {[
                                        'Paket gratis aktif otomatis untuk semua akun.',
                                        'Progres dan riwayat bermain tersimpan.',
                                        'Upgrade paket kapan saja dari halaman keanggotaan.',
                                    ].map((item) => (
                                        <li
                                            key={item}
                                            className="flex items-start gap-2 text-[11px] font-medium text-ink/60"
                                        >
                                            <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-red" />
                                            {item}
                                        </li>
                                    ))}
                                </ul>
                            </section>

                            <section className="mx-auto w-full max-w-sm rounded-xl border border-rule bg-surface p-3 shadow-card sm:p-3.5">
                                <div className="flex items-center gap-1.5">
                                    <span className="grid h-5 w-5 place-items-center rounded-md bg-red text-white">
                                        <CapIcon className="h-2.5 w-2.5" />
                                    </span>
                                    <h2 className="text-[12.5px] leading-none font-bold text-ink">
                                        Masuk
                                    </h2>
                                    <span className="ml-auto text-[8px] font-bold tracking-[0.12em] text-ink/30 uppercase">
                                        Ruang Belajar
                                    </span>
                                </div>

                                <form
                                    onSubmit={submit}
                                    className="mt-2 flex flex-col gap-1.5"
                                >
                                    <div>
                                        <label
                                            htmlFor="login"
                                            className={LABEL}
                                        >
                                            Email atau username
                                        </label>
                                        <input
                                            id="login"
                                            type="text"
                                            autoComplete="username"
                                            autoFocus
                                            required
                                            value={form.data.login}
                                            onChange={(event) =>
                                                form.setData(
                                                    'login',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="Email atau username"
                                            className={INPUT}
                                        />
                                        {form.errors.login && (
                                            <p className={ERROR}>
                                                {form.errors.login}
                                            </p>
                                        )}
                                    </div>

                                    <div>
                                        <label
                                            htmlFor="password"
                                            className={LABEL}
                                        >
                                            Kata sandi
                                        </label>
                                        <input
                                            id="password"
                                            type="password"
                                            autoComplete="current-password"
                                            required
                                            value={form.data.password}
                                            onChange={(event) =>
                                                form.setData(
                                                    'password',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="Kata sandi"
                                            className={INPUT}
                                        />
                                        {form.errors.password && (
                                            <p className={ERROR}>
                                                {form.errors.password}
                                            </p>
                                        )}
                                    </div>

                                    <div className="flex items-center gap-2">
                                        <label className="flex shrink-0 items-center gap-1 text-[9.5px] font-semibold text-ink/55">
                                            <input
                                                type="checkbox"
                                                checked={form.data.remember}
                                                onChange={(event) =>
                                                    form.setData(
                                                        'remember',
                                                        event.target.checked,
                                                    )
                                                }
                                                className="h-3 w-3 accent-red"
                                            />
                                            Ingat
                                        </label>

                                        <button
                                            type="submit"
                                            disabled={form.processing}
                                            className="ml-auto inline-flex h-8 shrink-0 items-center justify-center rounded-lg bg-red px-5 text-[11.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:opacity-60"
                                        >
                                            {form.processing
                                                ? 'Memeriksa...'
                                                : 'Masuk'}
                                        </button>
                                    </div>
                                </form>

                                <p className="mt-2 flex flex-wrap items-center justify-center gap-x-1 border-t border-rule/60 pt-2 text-center text-[9.5px] font-medium text-ink/45">
                                    <span>Belum punya akun?</span>
                                    <Link
                                        href={registerHref}
                                        className="font-bold text-red transition-opacity hover:opacity-70"
                                    >
                                        Daftar gratis
                                    </Link>
                                    <span className="text-ink/25">·</span>
                                    <Link
                                        href="/"
                                        className="font-semibold text-ink/40 transition-colors hover:text-red"
                                    >
                                        Ke beranda
                                    </Link>
                                </p>

                                <p className="mt-1 text-center text-[9px] font-medium text-ink/35">
                                    Admin dan guru juga masuk di sini, otomatis
                                    diarahkan ke panel.
                                </p>
                            </section>
                        </div>
                    </div>
                </div>
            </AppLayout>
        </>
    );
}

function CapIcon({ className }: { className?: string }) {
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
            <path d="M22 10 12 5 2 10l10 5 10-5Z" />
            <path d="M6 12v4.5c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V12" />
            <path d="M22 10v5" />
        </svg>
    );
}
