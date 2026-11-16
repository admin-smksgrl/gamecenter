import { useEffect, useState } from 'react';

export type Theme = 'light' | 'dark';

const STORAGE_KEY = 'gamecenter.theme';

function currentTheme(): Theme {
    if (typeof document === 'undefined') {
        return 'light';
    }

    return document.documentElement.classList.contains('dark')
        ? 'dark'
        : 'light';
}

export function useTheme() {
    const [theme, setTheme] = useState<Theme>(currentTheme);

    useEffect(() => {
        const dark = theme === 'dark';

        document.documentElement.classList.toggle('dark', dark);
        document.documentElement.style.colorScheme = theme;
        // Warna bilah peramban mengikuti aksen jenjang yang sedang aktif.
        const levelRoot =
            document.querySelector('[data-level-theme]') ??
            document.documentElement;
        const accent = getComputedStyle(levelRoot)
            .getPropertyValue('--color-red')
            .trim();

        document
            .querySelector('meta[name="theme-color"]')
            ?.setAttribute(
                'content',
                dark ? '#0e0c0d' : accent || '#e60012',
            );

        try {
            window.localStorage.setItem(STORAGE_KEY, theme);
        } catch {
            // Storage can be blocked in private WebViews; theme still applies.
        }
    }, [theme]);

    return {
        theme,
        toggleTheme: () =>
            setTheme((value) => (value === 'dark' ? 'light' : 'dark')),
    };
}
