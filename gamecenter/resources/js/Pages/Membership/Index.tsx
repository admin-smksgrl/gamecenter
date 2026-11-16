import { Head, Link, useForm, usePage } from '@inertiajs/react';
import { useEffect, useState } from 'react';
import type { FormEvent } from 'react';

import AppLayout from '@/Layouts/AppLayout';
import { cn, formatDateId, formatRupiah } from '@/lib/utils';
import type {
    BillingCycle,
    MembershipInfo,
    MembershipPlan,
    MembershipRecord,
    PageProps,
} from '@/types';

type MembershipPageProps = {
    plans: MembershipPlan[];
    current: MembershipInfo | null;
    pending: MembershipRecord | null;
    history: MembershipRecord[];
    bank: BankInfo;
};

type BankInfo = {
    name: string;
    account_number: string;
    account_holder: string;
};

const TIER_RANK: Record<string, number> = {
    free: 0,
    standard: 1,
    professional: 2,
    enterprise: 3,
};

const STATUS_CLASS: Record<string, string> = {
    pending: 'bg-ink/5 text-ink/55 ring-ink/10',
    active: 'bg-red text-white ring-red',
    expired: 'bg-ink/5 text-ink/35 ring-ink/10',
    rejected: 'bg-red-tint text-red ring-red/25',
};

const CTA_BASE =
    'mt-3 inline-flex w-full items-center justify-center rounded-lg px-3 py-2 text-[11.5px] font-bold transition-colors';
const CTA_PRIMARY = `${CTA_BASE} bg-red text-white shadow-fab hover:bg-red-deep`;
const CTA_DISABLED = `${CTA_BASE} cursor-default bg-ink/5 text-ink/40 ring-1 ring-rule/70`;

export default function MembershipIndex() {
    const { plans, current, pending, history, bank, auth } =
        usePage<PageProps<MembershipPageProps>>().props;
    const user = auth.user;

    const [cycle, setCycle] = useState<BillingCycle>('monthly');
    const [selected, setSelected] = useState<MembershipPlan | null>(null);
    const [copied, setCopied] = useState<string | null>(null);

    const form = useForm<{
        plan_id: number;
        billing_cycle: BillingCycle;
        note: string;
    }>({
        plan_id: 0,
        billing_cycle: 'monthly',
        note: '',
    });

    const currentRank = TIER_RANK[current?.tier ?? 'free'] ?? 0;
    const isFreeMember = user !== null && current?.tier === 'free';
    const featuredPlan =
        plans.find((plan) => plan.is_featured) ??
        plans.find((plan) => plan.tier !== 'free');

    useEffect(() => {
        if (!selected) {
            return;
        }

        function handleKey(event: KeyboardEvent) {
            if (event.key === 'Escape') {
                setSelected(null);
            }
        }

        window.addEventListener('keydown', handleKey);

        return () => window.removeEventListener('keydown', handleKey);
    }, [selected]);

    function priceFor(plan: MembershipPlan): number {
        return cycle === 'yearly' ? plan.price_yearly : plan.price_monthly;
    }

    function openDialog(plan: MembershipPlan) {
        form.setData({
            plan_id: plan.id,
            billing_cycle: cycle,
            note: '',
        });
        form.clearErrors();
        setSelected(plan);
    }

    async function copyText(text: string, key: string) {
        try {
            await navigator.clipboard.writeText(text);
            setCopied(key);
            window.setTimeout(
                () => setCopied((value) => (value === key ? null : value)),
                2000,
            );
        } catch {
            setCopied(null);
        }
    }

    function submitUpgrade(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        form.post('/keanggotaan/ajukan', {
            preserveScroll: true,
            onSuccess: () => {
                setSelected(null);
                form.reset();
            },
        });
    }

    function renderCta(plan: MembershipPlan) {
        const planRank = TIER_RANK[plan.tier] ?? 0;

        if (plan.tier === 'free') {
            return user ? (
                <span className={CTA_DISABLED}>Termasuk semua akun</span>
            ) : (
                <Link href="/daftar" className={CTA_PRIMARY}>
                    Daftar gratis
                </Link>
            );
        }

        if (pending) {
            return <span className={CTA_DISABLED}>Menunggu verifikasi admin</span>;
        }

        if (user && planRank <= currentRank) {
            return (
                <span className={CTA_DISABLED}>
                    {planRank === currentRank ? 'Paket aktifmu' : 'Sudah termasuk paketmu'}
                </span>
            );
        }

        if (!user) {
            return (
                <Link
                    href="/masuk?redirect=%2Fkeanggotaan"
                    className={CTA_PRIMARY}
                >
                    Masuk untuk upgrade
                </Link>
            );
        }

        return (
            <button
                type="button"
                onClick={() => openDialog(plan)}
                className={CTA_PRIMARY}
            >
                Upgrade paket
            </button>
        );
    }

    return (
        <>
            <Head title="Keanggotaan" />

            <AppLayout>
                <div className="no-bar min-h-0 flex-1 overflow-y-auto">
                    <div className="mx-auto w-full max-w-[1240px] px-3 py-4 sm:px-5 sm:py-6 lg:px-7">
                        <section className="flex flex-wrap items-end justify-between gap-x-4 gap-y-3">
                            <div className="min-w-0">
                                <span className="inline-flex items-center gap-1.5 rounded-full bg-red-tint px-2.5 py-1 text-[9.5px] font-bold tracking-[0.16em] text-red uppercase">
                                    Keanggotaan
                                </span>
                                <h1 className="display mt-2 text-[clamp(25px,3vw,38px)] leading-[1.03] text-ink">
                                    Naik level dengan{' '}
                                    <span className="italic text-red">paketmu</span>.
                                </h1>
                                <p className="mt-1.5 max-w-2xl text-[11.5px] font-medium text-ink/45">
                                    Tamu tetap bebas bermain. Masuk sebagai anggota
                                    untuk ikut kelas, bermain kelompok, dan mengikuti
                                    laporan belajar.
                                </p>
                            </div>

                            <div className="flex flex-col items-start gap-2 sm:items-end">
                                {user ? (
                                    <div className="flex flex-wrap items-center gap-1.5">
                                        <span className="inline-flex items-center gap-1.5 rounded-full border border-rule bg-surface px-2.5 py-1 text-[10px] font-semibold text-ink/60">
                                            <span className="h-1.5 w-1.5 rounded-full bg-red" />
                                            {current?.plan_name ?? 'Paket Gratis'}
                                            {current?.status === 'active' &&
                                                current.ends_at && (
                                                    <span className="text-ink/35">
                                                        · s.d.{' '}
                                                        {formatDateId(
                                                            current.ends_at,
                                                        )}
                                                    </span>
                                                )}
                                        </span>

                                        {isFreeMember && !pending && featuredPlan && (
                                            <button
                                                type="button"
                                                onClick={() =>
                                                    openDialog(featuredPlan)
                                                }
                                                className="inline-flex h-7 items-center gap-1 rounded-full bg-red px-2.5 text-[9.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                            >
                                                <BoltIcon className="h-3 w-3" />
                                                Upgrade sekarang
                                            </button>
                                        )}
                                    </div>
                                ) : (
                                    <div className="flex items-center gap-1.5">
                                        <Link
                                            href="/masuk?redirect=%2Fkeanggotaan"
                                            className="inline-flex h-8 items-center rounded-lg bg-red px-2.5 text-[10.5px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep"
                                        >
                                            Masuk
                                        </Link>
                                        <Link
                                            href="/daftar"
                                            className="inline-flex h-8 items-center rounded-lg px-2.5 text-[10.5px] font-bold text-ink/60 ring-1 ring-rule transition-colors hover:text-red hover:ring-red/40"
                                        >
                                            Daftar
                                        </Link>
                                    </div>
                                )}

                                <div className="flex items-center gap-1.5">
                                    <div
                                        role="group"
                                        aria-label="Siklus tagihan"
                                        className="inline-flex rounded-full border border-rule bg-surface p-0.5"
                                    >
                                        {(['monthly', 'yearly'] as const).map(
                                            (value) => (
                                                <button
                                                    key={value}
                                                    type="button"
                                                    aria-pressed={cycle === value}
                                                    onClick={() => setCycle(value)}
                                                    className={cn(
                                                        'rounded-full px-3 py-1 text-[10px] font-bold tracking-[0.08em] uppercase transition-colors',
                                                        cycle === value
                                                            ? 'bg-red text-white shadow-fab'
                                                            : 'text-ink/45 hover:text-ink',
                                                    )}
                                                >
                                                    {value === 'monthly'
                                                        ? 'Bulanan'
                                                        : 'Tahunan'}
                                                </button>
                                            ),
                                        )}
                                    </div>
                                    <span className="rounded-full bg-red-tint px-1.5 py-0.5 text-[8.5px] font-bold text-red">
                                        2 bln gratis
                                    </span>
                                </div>
                            </div>
                        </section>

                        {pending && (
                            <section className="mt-4 rounded-xl border border-red/25 bg-red-tint/60 p-3 sm:p-4">
                                <div className="flex flex-wrap items-start justify-between gap-3">
                                    <div className="min-w-0">
                                        <span className="text-[9px] font-bold tracking-[0.16em] text-red uppercase">
                                            Menunggu verifikasi
                                        </span>
                                        <h2 className="mt-1 text-[13.5px] font-bold text-ink">
                                            {pending.plan_name} ·{' '}
                                            {pending.billing_cycle === 'yearly'
                                                ? 'Tahunan'
                                                : 'Bulanan'}
                                        </h2>
                                        <p className="mt-1 text-[10.5px] font-medium text-ink/55">
                                            Transfer{' '}
                                            <b className="text-ink">
                                                {formatRupiah(pending.amount)}
                                            </b>{' '}
                                            ke rekening di bawah, lalu tunggu
                                            persetujuan admin.
                                        </p>
                                    </div>

                                    <div className="flex items-center gap-1.5 rounded-lg border border-red/20 bg-surface px-2.5 py-1.5">
                                        <span className="text-[10.5px] font-bold text-ink tabular-nums">
                                            {pending.reference}
                                        </span>
                                        <button
                                            type="button"
                                            onClick={() =>
                                                copyText(
                                                    pending.reference,
                                                    'pending-ref',
                                                )
                                            }
                                            aria-label="Salin kode referensi"
                                            className="text-[9px] font-bold text-red uppercase transition-opacity hover:opacity-70"
                                        >
                                            {copied === 'pending-ref' ? (
                                                'Tersalin'
                                            ) : (
                                                <CopyIcon className="h-3 w-3" />
                                            )}
                                        </button>
                                    </div>
                                </div>

                                <BankDetails
                                    bank={bank}
                                    copied={copied}
                                    onCopy={copyText}
                                    copyKey="pending-bank"
                                />

                                {pending.note && (
                                    <p className="mt-2.5 text-[10px] font-medium text-ink/50">
                                        Catatanmu: {pending.note}
                                    </p>
                                )}
                            </section>
                        )}

                        <section
                            aria-label="Daftar paket keanggotaan"
                            className="mt-4 grid gap-2.5 sm:grid-cols-2 sm:gap-3 xl:grid-cols-4"
                        >
                            {plans.map((plan) => {
                                const price = priceFor(plan);
                                const isActivePlan =
                                    user !== null &&
                                    plan.tier !== 'free' &&
                                    (TIER_RANK[plan.tier] ?? 0) === currentRank &&
                                    current?.status === 'active';

                                return (
                                    <article
                                        key={plan.id}
                                        className={cn(
                                            'relative flex flex-col rounded-xl border bg-surface p-3.5 shadow-card',
                                            plan.is_featured
                                                ? 'border-red/55 ring-1 ring-red/15'
                                                : 'border-rule',
                                        )}
                                    >
                                        {plan.is_featured && (
                                            <span className="absolute -top-2 right-3 rounded-full bg-red px-2 py-0.5 text-[8.5px] font-bold tracking-[0.12em] text-white uppercase">
                                                Rekomendasi
                                            </span>
                                        )}

                                        <div className="flex items-start justify-between gap-2">
                                            <div className="min-w-0">
                                                <h2 className="text-[14px] font-bold text-ink">
                                                    {plan.name}
                                                </h2>
                                                <p className="mt-0.5 text-[9px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                                                    {plan.tier}
                                                </p>
                                            </div>
                                            {isActivePlan && (
                                                <span className="rounded-full bg-red-tint px-2 py-0.5 text-[8.5px] font-bold text-red uppercase">
                                                    Aktif
                                                </span>
                                            )}
                                        </div>

                                        <p className="mt-1.5 min-h-[15px] text-[10.5px] font-medium text-ink/45">
                                            {plan.tagline}
                                        </p>

                                        <div className="mt-2 flex items-baseline gap-1">
                                            <span className="display text-[22px] leading-none text-ink">
                                                {price === 0
                                                    ? 'Gratis'
                                                    : formatRupiah(price)}
                                            </span>
                                            {price > 0 && (
                                                <span className="text-[9.5px] font-semibold text-ink/35">
                                                    {cycle === 'yearly'
                                                        ? '/tahun'
                                                        : '/bulan'}
                                                </span>
                                            )}
                                        </div>

                                        {cycle === 'yearly' &&
                                            plan.price_yearly > 0 && (
                                                <p className="mt-1 text-[9.5px] font-semibold text-red">
                                                    Hemat{' '}
                                                    {formatRupiah(
                                                        Math.max(
                                                            0,
                                                            plan.price_monthly *
                                                                12 -
                                                                plan.price_yearly,
                                                        ),
                                                    )}
                                                    /tahun
                                                </p>
                                            )}

                                        <ul className="mt-3 flex flex-1 flex-col gap-1.5">
                                            {plan.features.map((feature) => (
                                                <li
                                                    key={feature}
                                                    className="flex items-start gap-1.5 text-[10.5px] font-medium text-ink/65"
                                                >
                                                    <CheckIcon className="mt-0.5 h-3 w-3 shrink-0 text-red" />
                                                    <span
                                                        className={cn(
                                                            feature
                                                                .toLowerCase()
                                                                .includes(
                                                                    '(segera)',
                                                                ) && 'text-ink/40',
                                                        )}
                                                    >
                                                        {feature}
                                                    </span>
                                                </li>
                                            ))}
                                        </ul>

                                        {renderCta(plan)}
                                    </article>
                                );
                            })}
                        </section>

                        {user && history.length > 0 && (
                            <section className="mt-5">
                                <div className="flex items-end justify-between gap-3">
                                    <h2 className="display text-[18px] text-ink">
                                        Riwayat keanggotaan
                                    </h2>
                                    <p className="text-[10px] font-semibold text-ink/35">
                                        {history.length} pengajuan terakhir
                                    </p>
                                </div>

                                <div className="mt-2 divide-y divide-rule/70 overflow-hidden rounded-xl border border-rule bg-surface">
                                    {history.map((record) => (
                                        <div
                                            key={record.id}
                                            className="flex flex-wrap items-center gap-x-3 gap-y-1.5 px-3 py-2.5"
                                        >
                                            <div className="min-w-0 flex-1">
                                                <p className="text-[12px] font-bold text-ink">
                                                    {record.plan_name ?? 'Paket'}
                                                    <span className="ml-1 text-[9px] font-semibold tracking-[0.1em] text-ink/35 uppercase">
                                                        {record.billing_cycle ===
                                                        'yearly'
                                                            ? 'Tahunan'
                                                            : 'Bulanan'}
                                                    </span>
                                                </p>
                                                <p className="mt-0.5 text-[9.5px] font-medium text-ink/40">
                                                    {record.reference} ·{' '}
                                                    {formatDateId(
                                                        record.created_at,
                                                    )}
                                                </p>
                                                {record.status === 'active' &&
                                                    record.ends_at && (
                                                        <p className="mt-0.5 text-[9.5px] font-medium text-ink/40">
                                                            Aktif s.d.{' '}
                                                            {formatDateId(
                                                                record.ends_at,
                                                            )}
                                                        </p>
                                                    )}
                                                {record.admin_note && (
                                                    <p className="mt-1 text-[10px] font-medium text-red">
                                                        Catatan admin:{' '}
                                                        {record.admin_note}
                                                    </p>
                                                )}
                                            </div>

                                            <span className="text-[11.5px] font-bold text-ink/70 tabular-nums">
                                                {formatRupiah(record.amount)}
                                            </span>

                                            <span
                                                className={cn(
                                                    'rounded-full px-2 py-0.5 text-[9px] font-bold tracking-[0.08em] uppercase ring-1',
                                                    STATUS_CLASS[record.status],
                                                )}
                                            >
                                                {record.status_label}
                                            </span>
                                        </div>
                                    ))}
                                </div>
                            </section>
                        )}
                    </div>
                </div>
            </AppLayout>

            {selected && (
                <div
                    role="dialog"
                    aria-modal="true"
                    aria-label={`Ajukan paket ${selected.name}`}
                    onClick={(event) => {
                        if (event.target === event.currentTarget) {
                            setSelected(null);
                        }
                    }}
                    className="fixed inset-0 z-50 grid place-items-center bg-black/45 p-3 backdrop-blur-[2px]"
                >
                    <div className="max-h-[88vh] w-full max-w-lg overflow-y-auto rounded-2xl border border-rule bg-surface p-4 shadow-sheet sm:p-5">
                        <div className="flex items-start justify-between gap-3">
                            <div className="min-w-0">
                                <p className="text-[9px] font-bold tracking-[0.16em] text-red uppercase">
                                    Ajukan upgrade
                                </p>
                                <h2 className="mt-1 text-[16px] font-bold text-ink">
                                    {selected.name}
                                </h2>
                                <p className="mt-0.5 text-[10.5px] font-medium text-ink/45">
                                    {formatRupiah(
                                        form.data.billing_cycle === 'yearly'
                                            ? selected.price_yearly
                                            : selected.price_monthly,
                                    )}{' '}
                                    /{' '}
                                    {form.data.billing_cycle === 'yearly'
                                        ? 'tahun'
                                        : 'bulan'}
                                </p>
                            </div>
                            <button
                                type="button"
                                onClick={() => setSelected(null)}
                                aria-label="Tutup dialog"
                                className="grid h-8 w-8 shrink-0 place-items-center rounded-lg text-ink/50 ring-1 ring-rule transition-colors hover:bg-red-tint hover:text-red"
                            >
                                <CloseIcon className="h-3.5 w-3.5" />
                            </button>
                        </div>

                        <p className="mt-3 text-[10.5px] font-medium text-ink/55">
                            Transfer sesuai nominal ke rekening berikut, lalu
                            kirim pengajuan. Admin akan memverifikasi dan
                            mengaktifkan paketmu.
                        </p>

                        <BankDetails
                            bank={bank}
                            copied={copied}
                            onCopy={copyText}
                            copyKey="dialog-bank"
                        />

                        <form onSubmit={submitUpgrade} className="mt-3">
                            <label
                                htmlFor="membership-note"
                                className="text-[9.5px] font-bold tracking-[0.14em] text-ink/40 uppercase"
                            >
                                Catatan (opsional)
                            </label>
                            <textarea
                                id="membership-note"
                                rows={3}
                                maxLength={500}
                                value={form.data.note}
                                onChange={(event) =>
                                    form.setData('note', event.target.value)
                                }
                                placeholder="Contoh: transfer dari BCA a.n. Budi, jam 19.30"
                                className="mt-1 w-full resize-none rounded-xl border border-rule bg-canvas px-3 py-2 text-[16px] font-medium text-ink outline-none transition-colors placeholder:text-ink/30 focus:border-red/60 focus:ring-2 focus:ring-red/15 sm:text-[12.5px]"
                            />
                            {form.errors.note && (
                                <p className="mt-1 text-[10.5px] font-semibold text-red">
                                    {form.errors.note}
                                </p>
                            )}
                            {(form.errors.plan_id ||
                                form.errors.billing_cycle) && (
                                <p className="mt-1 text-[10.5px] font-semibold text-red">
                                    {form.errors.plan_id ??
                                        form.errors.billing_cycle}
                                </p>
                            )}

                            <div className="mt-3 flex gap-1.5">
                                <button
                                    type="button"
                                    onClick={() => setSelected(null)}
                                    className="inline-flex flex-1 items-center justify-center rounded-lg px-3 py-2 text-[11px] font-bold text-ink/55 ring-1 ring-rule transition-colors hover:text-ink"
                                >
                                    Batal
                                </button>
                                <button
                                    type="submit"
                                    disabled={form.processing}
                                    className="inline-flex flex-[1.6] items-center justify-center rounded-lg bg-red px-3 py-2 text-[11px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:opacity-60"
                                >
                                    {form.processing
                                        ? 'Mengirim...'
                                        : 'Kirim pengajuan'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </>
    );
}

function BankDetails({
    bank,
    copied,
    onCopy,
    copyKey,
}: {
    bank: BankInfo;
    copied: string | null;
    onCopy: (text: string, key: string) => void;
    copyKey: string;
}) {
    return (
        <div className="mt-3 grid gap-1.5 sm:grid-cols-3">
            <div className="rounded-lg border border-rule bg-canvas px-2.5 py-1.5">
                <p className="text-[8.5px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                    Bank
                </p>
                <p className="mt-0.5 text-[11px] font-bold text-ink">
                    {bank.name}
                </p>
            </div>
            <div className="flex items-center justify-between gap-1 rounded-lg border border-rule bg-canvas px-2.5 py-1.5">
                <div className="min-w-0">
                    <p className="text-[8.5px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                        Nomor rekening
                    </p>
                    <p className="mt-0.5 truncate text-[11px] font-bold text-ink tabular-nums">
                        {bank.account_number}
                    </p>
                </div>
                <button
                    type="button"
                    onClick={() => onCopy(bank.account_number, copyKey)}
                    aria-label="Salin nomor rekening"
                    className="shrink-0 text-[9px] font-bold text-red uppercase transition-opacity hover:opacity-70"
                >
                    {copied === copyKey ? 'Tersalin' : 'Salin'}
                </button>
            </div>
            <div className="rounded-lg border border-rule bg-canvas px-2.5 py-1.5">
                <p className="text-[8.5px] font-bold tracking-[0.14em] text-ink/35 uppercase">
                    Atas nama
                </p>
                <p className="mt-0.5 truncate text-[11px] font-bold text-ink">
                    {bank.account_holder}
                </p>
            </div>
        </div>
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
            <path d="m4.5 12.5 5 5 10-11" />
        </svg>
    );
}

function CopyIcon({ className }: { className?: string }) {
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
            <rect x="9" y="9" width="11" height="11" rx="2" />
            <path d="M5 15V6a2 2 0 0 1 2-2h9" />
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
            strokeWidth="2.2"
            strokeLinecap="round"
            className={className}
        >
            <path d="M6 6l12 12M18 6 6 18" />
        </svg>
    );
}
