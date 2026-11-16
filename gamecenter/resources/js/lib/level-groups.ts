/**
 * Pengelompokan jenjang untuk navigasi atas.
 *
 * Basis data tetap menyimpan jenjang secara terpisah (PAUD, TK, SD, SMP, SMA,
 * SMK) karena tiap jenjang punya rombel dan mata pelajaran sendiri. Di
 * navigasi, **SMA dan SMK digabung** menjadi satu pilihan `SMA-SMK` sebab yang
 * membedakan keduanya hanya sebagian mata pelajaran kejuruan. Kelas dari kedua
 * jenjang tetap muncul lengkap dan bisa dipilih satu per satu.
 */

export interface LevelGroup {
    slug: string;
    label: string;
    /** Slug jenjang yang tercakup, berurutan sesuai urutan tampil. */
    levels: string[];
}

export const LEVEL_GROUPS: LevelGroup[] = [
    { slug: 'paud', label: 'PAUD', levels: ['paud'] },
    { slug: 'tk', label: 'TK', levels: ['tk'] },
    { slug: 'sd', label: 'SD-MI', levels: ['sd'] },
    { slug: 'smp', label: 'SMP-MTs', levels: ['smp'] },
    { slug: 'sma-smk', label: 'SMA-SMK', levels: ['sma', 'smk'] },
];

const FALLBACK: LevelGroup = { slug: 'lainnya', label: 'Lainnya', levels: [] };

export function groupOf(levelSlug: string): LevelGroup {
    return (
        LEVEL_GROUPS.find((group) => group.levels.includes(levelSlug)) ?? {
            ...FALLBACK,
            levels: [levelSlug],
        }
    );
}

/** Label grup untuk sebuah jenjang, mis. `sma` → `SMA-SMK`. */
export function groupLabel(levelSlug: string): string {
    return groupOf(levelSlug).label;
}

/** Apakah grup ini menggabungkan lebih dari satu jenjang. */
export function isMergedGroup(group: LevelGroup): boolean {
    return group.levels.length > 1;
}