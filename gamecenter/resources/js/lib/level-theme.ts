export type LevelThemeKey =
    | 'playful'
    | 'adventure'
    | 'scifi'
    | 'professional'
    | 'default';

export interface LevelThemeMeta {
    key: LevelThemeKey;
    label: string;
    tagline: string;
    emoji: string;
    accent: string;
    soft: string;
}

/**
 * Tema visual per jenjang. Nilai warna utama juga dipetakan ke token
 * `--color-red*` lewat `data-level-theme` di app.css, sehingga seluruh
 * komponen yang memakai kelas `red` otomatis mengikuti tema jenjang.
 *
 * Semua jenjang memakai satu identitas: merah #e60012 di atas putih.
 * Palet per jenjang sudah dihapus agar tidak ada warna yang bertumpuk.
 */
export const LEVEL_THEMES: Record<LevelThemeKey, LevelThemeMeta> = {
    playful: {
        key: 'playful',
        label: 'Ceria',
        tagline: 'Bentuk, warna, dan gerak yang ramah anak.',
        emoji: '🧸',
        accent: '#e60012',
        soft: '#ffebec',
    },
    adventure: {
        key: 'adventure',
        label: 'Petualangan',
        tagline: 'Belajar sambil menjelajah dunia sekitar.',
        emoji: '🎨',
        accent: '#e60012',
        soft: '#ffebec',
    },
    scifi: {
        key: 'scifi',
        label: 'Penjelajah',
        tagline: 'Logika, angka, dan eksperimen ala ilmuwan.',
        emoji: '🚀',
        accent: '#e60012',
        soft: '#ffebec',
    },
    professional: {
        key: 'professional',
        label: 'Fokus',
        tagline: 'Rapi, tenang, dan siap menghadapi ujian.',
        emoji: '🎓',
        accent: '#e60012',
        soft: '#ffebec',
    },
    default: {
        key: 'default',
        label: 'Ruang Belajar',
        tagline: 'Belajar dengan cara yang menyenangkan.',
        emoji: '📚',
        accent: '#e60012',
        soft: '#ffebec',
    },
};

export function resolveLevelTheme(
    theme: string | null | undefined,
): LevelThemeMeta {
    return (
        LEVEL_THEMES[(theme ?? 'default') as LevelThemeKey] ??
        LEVEL_THEMES.default
    );
}
