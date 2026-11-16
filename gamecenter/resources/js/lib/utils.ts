export function cn(...classes: Array<string | false | null | undefined>): string {
    return classes.filter(Boolean).join(' ');
}

/**
 * Warna mapel tidak lagi berwarna-warni. Setiap mapel memakai aksen
 * jenjang (`--color-red` ditimpa `data-level-theme`), jadi seluruh kartu
 * dalam satu jenjang seragam: SMA/SMK biru, TK amber, dan seterusnya.
 * Parameter `color` dipertahankan agar pemanggil lama tetap berjalan dan
 * nilainya diabaikan dengan sengaja.
 */
export interface SubjectTheme {
    border: string;
    tile: string;
}

export const DEFAULT_SUBJECT_THEME: SubjectTheme = {
    border: 'border-red/20',
    tile: 'bg-red-tint',
};

export function subjectTheme(_color?: string | null): SubjectTheme {
    return DEFAULT_SUBJECT_THEME;
}

export const DIFFICULTY_META: Record<
    string,
    { label: string; className: string; dot: string; hint: string }
> = {
    easy: {
        label: 'Mudah',
        className: 'bg-red text-white ring-red',
        dot: 'bg-red',
        hint: 'Pemanasan',
    },
    medium: {
        label: 'Sedang',
        className: 'bg-ink/5 text-ink/70 ring-ink/15',
        dot: 'bg-ink/40',
        hint: 'Naik level',
    },
    hard: {
        label: 'Sulit',
        className: 'bg-ink text-surface ring-ink',
        dot: 'bg-ink',
        hint: 'Uji nyali',
    },
};

export function formatNumber(value: number): string {
    return new Intl.NumberFormat('id-ID').format(value);
}

export function formatRupiah(value: number): string {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        maximumFractionDigits: 0,
    }).format(value);
}

export function formatDateId(value: string | null): string {
    if (!value) {
        return '—';
    }

    return new Intl.DateTimeFormat('id-ID', {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        timeZone: 'Asia/Jakarta',
    }).format(new Date(value));
}
