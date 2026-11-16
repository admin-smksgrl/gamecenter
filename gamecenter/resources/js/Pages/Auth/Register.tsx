import { Head, Link, useForm } from '@inertiajs/react';
import type { FormEvent } from 'react';

import AppLayout from '@/Layouts/AppLayout';
import { firstValidationMessage } from '@/lib/friendly-error';
import { toast } from '@/lib/toast';

const INPUT =
    'mt-1 w-full rounded-xl border border-rule bg-canvas px-3 py-2.5 text-[16px] font-medium text-ink outline-none transition-colors placeholder:text-ink/30 focus:border-red/60 focus:ring-2 focus:ring-red/15 sm:text-[13px]';

const LABEL =
    'text-[9.5px] font-bold tracking-[0.14em] text-ink/40 uppercase';

const ERROR = 'mt-1 text-[10.5px] font-semibold text-red';

export default function Register({ redirect }: { redirect?: string | null }) {
    const form = useForm({
        name: '',
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
    });

    const loginHref = redirect
        ? `/masuk?redirect=${encodeURIComponent(redirect)}`
        : '/masuk';

    function submit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        form.post(
            redirect ? `/daftar?redirect=${encodeURIComponent(redirect)}` : '/daftar',
            {
                onFinish: () =>
                    form.reset('password', 'password_confirmation'),
                onError: (errors) => {
                    toast.error(
                        'Pendaftaran belum berhasil',
                        firstValidationMessage(errors) ??
                            'Periksa kembali data yang kamu isi, lalu coba lagi.',
                    );
                },
            },
        );
    }

    return (
        <>
            <Head title="Daftar" />

            <AppLayout>
                <div className="no-bar min-h-0 flex-1 overflow-y-auto">
                    <div className="mx-auto grid w-full max-w-4xl gap-4 px-3 py-6 sm:px-5 sm:py-10 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:gap-8">
                        <section className="hidden lg:block">
                            <span className="inline-flex items-center gap-1.5 rounded-full bg-red-tint px-2.5 py-1 text-[9.5px] font-bold tracking-[0.16em] text-red uppercase">
                                Daftar
                            </span>
                            <h1 className="display mt-3 text-[clamp(30px,3.4vw,44px)] leading-[1.02] text-ink">
                                Mulai{' '}
                                <span className="italic text-red">gratis</span>,
                                naik level kapan saja.
                            </h1>
                            <p className="mt-3 max-w-sm text-[12px] font-medium text-ink/45">
                                Buat akun siswa untuk menyimpan progres,
                                mengumpulkan XP dan koin, lalu ajukan paket
                                keanggotaan saat siap.
                            </p>

                            <ul className="mt-5 flex flex-col gap-2">
                                {[
                                    'Pendaftaran tanpa biaya, paket Gratis langsung aktif.',
                                    'Data belajar tersimpan di akunmu.',
                                    'Upgrade paket via transfer bank dan verifikasi admin.',
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

                        <section className="rounded-2xl border border-rule bg-surface p-5 shadow-card sm:p-6">
                            <div className="flex items-center gap-2">
                                <span className="grid h-8 w-8 place-items-center rounded-lg bg-red text-white">
                                    <CapIcon className="h-4 w-4" />
                                </span>
                                <div>
                                    <h2 className="text-[15px] font-bold text-ink">
                                        Buat akun siswa
                                    </h2>
                                    <p className="text-[9.5px] font-semibold tracking-[0.1em] text-ink/35 uppercase">
                                        Ruang Belajar
                                    </p>
                                </div>
                            </div>

                            <form onSubmit={submit} className="mt-4 flex flex-col gap-3">
                                <div>
                                    <label htmlFor="name" className={LABEL}>
                                        Nama lengkap
                                    </label>
                                    <input
                                        id="name"
                                        type="text"
                                        autoComplete="name"
                                        autoFocus
                                        required
                                        value={form.data.name}
                                        onChange={(event) =>
                                            form.setData('name', event.target.value)
                                        }
                                        placeholder="Budi Santoso"
                                        className={INPUT}
                                    />
                                    {form.errors.name && (
                                        <p className={ERROR}>{form.errors.name}</p>
                                    )}
                                </div>

                                <div className="grid gap-3 sm:grid-cols-2">
                                    <div>
                                        <label htmlFor="username" className={LABEL}>
                                            Username
                                        </label>
                                        <input
                                            id="username"
                                            type="text"
                                            autoComplete="username"
                                            required
                                            value={form.data.username}
                                            onChange={(event) =>
                                                form.setData(
                                                    'username',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="budi"
                                            className={INPUT}
                                        />
                                        {form.errors.username && (
                                            <p className={ERROR}>
                                                {form.errors.username}
                                            </p>
                                        )}
                                    </div>

                                    <div>
                                        <label htmlFor="email" className={LABEL}>
                                            Email
                                        </label>
                                        <input
                                            id="email"
                                            type="email"
                                            autoComplete="email"
                                            required
                                            value={form.data.email}
                                            onChange={(event) =>
                                                form.setData(
                                                    'email',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="budi@email.com"
                                            className={INPUT}
                                        />
                                        {form.errors.email && (
                                            <p className={ERROR}>
                                                {form.errors.email}
                                            </p>
                                        )}
                                    </div>
                                </div>

                                <div className="grid gap-3 sm:grid-cols-2">
                                    <div>
                                        <label htmlFor="password" className={LABEL}>
                                            Kata sandi
                                        </label>
                                        <input
                                            id="password"
                                            type="password"
                                            autoComplete="new-password"
                                            required
                                            value={form.data.password}
                                            onChange={(event) =>
                                                form.setData(
                                                    'password',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="Minimal 8 karakter"
                                            className={INPUT}
                                        />
                                        {form.errors.password && (
                                            <p className={ERROR}>
                                                {form.errors.password}
                                            </p>
                                        )}
                                    </div>

                                    <div>
                                        <label
                                            htmlFor="password_confirmation"
                                            className={LABEL}
                                        >
                                            Ulangi kata sandi
                                        </label>
                                        <input
                                            id="password_confirmation"
                                            type="password"
                                            autoComplete="new-password"
                                            required
                                            value={form.data.password_confirmation}
                                            onChange={(event) =>
                                                form.setData(
                                                    'password_confirmation',
                                                    event.target.value,
                                                )
                                            }
                                            placeholder="Ulangi kata sandi"
                                            className={INPUT}
                                        />
                                    </div>
                                </div>

                                <button
                                    type="submit"
                                    disabled={form.processing}
                                    className="mt-1 inline-flex w-full items-center justify-center rounded-xl bg-red px-3 py-2.5 text-[12px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:opacity-60"
                                >
                                    {form.processing
                                        ? 'Membuat akun...'
                                        : 'Daftar gratis'}
                                </button>
                            </form>

                            <p className="mt-4 text-center text-[11px] font-medium text-ink/45">
                                Sudah punya akun?{' '}
                                <Link
                                    href={loginHref}
                                    className="font-bold text-red transition-opacity hover:opacity-70"
                                >
                                    Masuk
                                </Link>
                            </p>

                            <p className="mt-1 text-center text-[10px] font-medium text-ink/30">
                                Dengan mendaftar kamu setuju memakai akun
                                dengan bijak.
                            </p>
                        </section>
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
