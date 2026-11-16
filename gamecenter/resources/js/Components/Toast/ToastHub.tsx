import { usePage } from '@inertiajs/react';
import { useEffect, useRef, useSyncExternalStore } from 'react';

import {
    dismissToast,
    getToastServerSnapshot,
    getToasts,
    subscribeToasts,
    toast,
    type ToastItem,
    type ToastTone,
} from '@/lib/toast';
import { cn } from '@/lib/utils';
import type { PageProps } from '@/types';

const TONE_STYLE: Record<
    ToastTone,
    { wrap: string; icon: string; iconWrap: string }
> = {
    success: {
        wrap: 'border-red/30',
        icon: 'text-red',
        iconWrap: 'bg-red-tint',
    },
    error: {
        wrap: 'border-red/35',
        icon: 'text-red',
        iconWrap: 'bg-red-tint',
    },
    warning: {
        wrap: 'border-ink/20',
        icon: 'text-ink/65',
        iconWrap: 'bg-ink/[0.06]',
    },
    info: {
        wrap: 'border-rule',
        icon: 'text-ink/55',
        iconWrap: 'bg-ink/[0.06]',
    },
};

export default function ToastHub() {
    const toasts = useSyncExternalStore(
        subscribeToasts,
        getToasts,
        getToastServerSnapshot,
    );

    useFlashToasts();

    return (
        <div
            aria-live="polite"
            aria-atomic="false"
            className="pointer-events-none fixed inset-x-0 top-3 z-[90] flex flex-col items-center gap-2 px-3 sm:px-0"
        >
            {toasts.map((item) => (
                <ToastCard key={item.id} item={item} />
            ))}
        </div>
    );
}

function useFlashToasts() {
    const page = usePage<PageProps>();
    const { flash } = page.props;
    const url = page.url;
    const lastSignature = useRef<string | null>(null);

    useEffect(() => {
        const entries: Array<[ToastTone, string | null | undefined]> = [
            ['success', flash?.success],
            ['error', flash?.error],
            ['info', flash?.info],
        ];

        const messages = entries.filter(
            (entry): entry is [ToastTone, string] =>
                typeof entry[1] === 'string' && entry[1].trim() !== '',
        );

        if (messages.length === 0) {
            return;
        }

        const signature = `${url}::${messages
            .map(([tone, message]) => `${tone}:${message}`)
            .join('|')}`;

        if (signature === lastSignature.current) {
            return;
        }

        lastSignature.current = signature;

        for (const [tone, message] of messages) {
            toast.show({ tone, title: message });
        }
    }, [flash?.success, flash?.error, flash?.info, url]);
}

function ToastCard({ item }: { item: ToastItem }) {
    useEffect(() => {
        if (item.duration <= 0) {
            return;
        }

        const timer = window.setTimeout(
            () => dismissToast(item.id),
            item.duration,
        );

        return () => window.clearTimeout(timer);
    }, [item.id, item.duration]);

    const style = TONE_STYLE[item.tone];

    return (
        <div
            role={item.tone === 'error' ? 'alert' : 'status'}
            className={cn(
                'animate-drop pointer-events-auto flex w-full max-w-sm items-start gap-2.5 rounded-xl border bg-surface p-3 shadow-card sm:w-[22rem]',
                style.wrap,
            )}
        >
            <span
                aria-hidden
                className={cn(
                    'mt-px grid h-7 w-7 shrink-0 place-items-center rounded-lg',
                    style.iconWrap,
                    style.icon,
                )}
            >
                <ToneIcon tone={item.tone} />
            </span>

            <div className="min-w-0 flex-1 pt-0.5">
                <p className="text-[11.5px] leading-snug font-bold text-ink">
                    {item.title}
                </p>
                {item.description && (
                    <p className="mt-0.5 text-[10.5px] leading-relaxed font-medium text-ink/55">
                        {item.description}
                    </p>
                )}
            </div>

            <button
                type="button"
                onClick={() => dismissToast(item.id)}
                aria-label="Tutup pemberitahuan"
                className="-mt-1 -mr-1 grid h-6 w-6 shrink-0 place-items-center rounded-md text-ink/35 transition-colors hover:bg-ink/[0.06] hover:text-ink/70"
            >
                <svg
                    aria-hidden
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    className="h-3 w-3"
                >
                    <path d="m6 6 12 12M18 6 6 18" />
                </svg>
            </button>
        </div>
    );
}

function ToneIcon({ tone }: { tone: ToastTone }) {
    const className = 'h-3.5 w-3.5';

    if (tone === 'success') {
        return (
            <svg
                aria-hidden
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2.2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className={className}
            >
                <path d="m4.5 12.5 4.5 4.5L19.5 6.5" />
            </svg>
        );
    }

    if (tone === 'error') {
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
                <path d="M12 8v5M12 16.2v.1" />
            </svg>
        );
    }

    if (tone === 'warning') {
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
                <path d="M12 4.5 21 20H3L12 4.5Z" />
                <path d="M12 10v4M12 17.2v.1" />
            </svg>
        );
    }

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
            <path d="M12 11v5M12 7.8v.1" />
        </svg>
    );
}
