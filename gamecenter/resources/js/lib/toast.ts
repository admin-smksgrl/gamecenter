export type ToastTone = 'success' | 'error' | 'info' | 'warning';

/** Tombol opsional pada toast, misalnya "Coba lagi" setelah gagal tersambung. */
export interface ToastAction {
    label: string;
    onClick: () => void;
}

export interface ToastInput {
    tone?: ToastTone;
    title: string;
    description?: string | null;
    /** Durasi tampil dalam milidetik. Isi 0 agar toast tidak menutup sendiri. */
    duration?: number;
    action?: ToastAction | null;
}

export interface ToastItem {
    id: number;
    tone: ToastTone;
    title: string;
    description: string | null;
    duration: number;
    action: ToastAction | null;
}

type Listener = () => void;
type ToastFn = (
    title: string,
    description?: string | null,
    duration?: number,
) => number;

const MAX_VISIBLE = 4;
const EMPTY: ToastItem[] = [];

const listeners = new Set<Listener>();

let toasts: ToastItem[] = EMPTY;
let nextId = 0;

function emit(): void {
    for (const listener of listeners) {
        listener();
    }
}

export function subscribeToasts(listener: Listener): () => void {
    listeners.add(listener);

    return () => {
        listeners.delete(listener);
    };
}

export function getToasts(): ToastItem[] {
    return toasts;
}

/** Snapshot stabil untuk render di server / sebelum hidrasi. */
export function getToastServerSnapshot(): ToastItem[] {
    return EMPTY;
}

export function dismissToast(id: number): void {
    const next = toasts.filter((item) => item.id !== id);

    if (next.length === toasts.length) {
        return;
    }

    toasts = next.length > 0 ? next : EMPTY;
    emit();
}

export function clearToasts(): void {
    if (toasts.length === 0) {
        return;
    }

    toasts = EMPTY;
    emit();
}

export function pushToast(input: ToastInput): number {
    const tone = input.tone ?? 'info';
    const id = ++nextId;

    const item: ToastItem = {
        id,
        tone,
        title: input.title,
        description: input.description?.trim() || null,
        duration:
            input.duration ??
            (tone === 'error' ? (input.action ? 12000 : 7000) : 4800),
        action: input.action ?? null,
    };

    toasts = [...toasts, item].slice(-MAX_VISIBLE);
    emit();

    return id;
}

const success: ToastFn = (title, description, duration) =>
    pushToast({ tone: 'success', title, description, duration });

const error: ToastFn = (title, description, duration) =>
    pushToast({ tone: 'error', title, description, duration });

const info: ToastFn = (title, description, duration) =>
    pushToast({ tone: 'info', title, description, duration });

const warning: ToastFn = (title, description, duration) =>
    pushToast({ tone: 'warning', title, description, duration });

export const toast = {
    success,
    error,
    info,
    warning,
    show: pushToast,
    dismiss: dismissToast,
    clear: clearToasts,
};
