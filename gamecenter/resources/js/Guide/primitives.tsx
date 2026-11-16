import type { PropsWithChildren, ReactNode } from 'react';

import { cn } from '@/lib/utils';

export function H2({ id, children }: PropsWithChildren<{ id: string }>) {
    return (
        <h2 id={id} className="scroll-mt-24">
            {children}
        </h2>
    );
}

export function H3({ children }: PropsWithChildren) {
    return <h3>{children}</h3>;
}

const CALLOUT_STYLES = {
    catatan: {
        box: 'border-rule bg-canvas/70',
        label: 'text-ink/45',
        icon: 'text-ink/35',
    },
    tips: {
        box: 'border-red/20 bg-red-tint/70',
        label: 'text-red',
        icon: 'text-red',
    },
    penting: {
        box: 'border-red/45 bg-red-tint',
        label: 'text-red',
        icon: 'text-red',
    },
} as const;

interface CalloutProps extends PropsWithChildren {
    tone?: keyof typeof CALLOUT_STYLES;
    title: string;
}

export function Callout({ tone = 'catatan', title, children }: CalloutProps) {
    const styles = CALLOUT_STYLES[tone];

    return (
        <aside
            className={cn(
                'flex gap-2.5 rounded-xl border px-3 py-2.5 text-[11.5px] leading-relaxed text-ink/65',
                styles.box,
            )}
        >
            <InfoIcon className={cn('mt-0.5 h-4 w-4 shrink-0', styles.icon)} />
            <div className="min-w-0">
                <p
                    className={cn(
                        'text-[9px] font-bold tracking-[0.14em] uppercase',
                        styles.label,
                    )}
                >
                    {title}
                </p>
                <div className="mt-1 space-y-1.5">{children}</div>
            </div>
        </aside>
    );
}

export function Steps({ steps }: { steps: ReactNode[] }) {
    return (
        <ol className="my-2 grid gap-2.5">
            {steps.map((step, index) => (
                <li key={index} className="flex gap-2.5">
                    <span className="grid h-5 w-5 shrink-0 place-items-center rounded-full bg-red-tint text-[9.5px] font-black text-red">
                        {index + 1}
                    </span>
                    <div className="min-w-0 pt-0.5 text-[11.5px] leading-relaxed text-ink/65">
                        {step}
                    </div>
                </li>
            ))}
        </ol>
    );
}

interface DataTableProps {
    head: string[];
    rows: ReactNode[][];
    caption?: string;
}

export function DataTable({ head, rows, caption }: DataTableProps) {
    return (
        <div className="scroll-quiet overflow-x-auto rounded-xl border border-rule">
            <table>
                {caption && <caption>{caption}</caption>}
                <thead>
                    <tr>
                        {head.map((cell) => (
                            <th key={cell} scope="col">
                                {cell}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {rows.map((row, index) => (
                        <tr key={index}>
                            {row.map((cell, cellIndex) => (
                                <td key={cellIndex}>{cell}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export function Kbd({ children }: PropsWithChildren) {
    return (
        <kbd className="inline-flex min-w-5 items-center justify-center rounded-[5px] border border-rule bg-canvas px-1.5 py-0.5 font-sans text-[9.5px] font-bold text-ink/55 shadow-[0_1px_0_0_var(--color-rule)]">
            {children}
        </kbd>
    );
}

function InfoIcon({ className }: { className?: string }) {
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
            <path d="M12 11v5M12 8h.01" />
        </svg>
    );
}
