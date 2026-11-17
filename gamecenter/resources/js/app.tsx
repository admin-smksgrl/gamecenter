import '../css/app.css';

import { createInertiaApp } from '@inertiajs/react';
import type { ComponentType, ReactNode } from 'react';
import { createRoot } from 'react-dom/client';

import {
    friendlyHttpError,
    friendlyNetworkError,
} from '@/lib/friendly-error';
import { retryConnection } from '@/lib/connection';
import { toast } from '@/lib/toast';

const appName = import.meta.env.VITE_APP_NAME || 'Game Center Edukasi';

if (import.meta.env.PROD && 'serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        void navigator.serviceWorker
            .register('/sw.js')
            .catch(() => undefined);
    });
}

type InertiaHttpExceptionDetail = {
    response?: { status?: number };
};

if (typeof document !== 'undefined') {
    // Ganti dialog teknis bawaan Inertia dengan toast berbahasa awam.
    document.addEventListener('inertia:httpException', (event) => {
        const detail = (event as CustomEvent<InertiaHttpExceptionDetail>)
            .detail;
        const status = detail?.response?.status ?? 0;
        const friendly = friendlyHttpError(status);

        toast.error(friendly.title, friendly.description);

        if (status === 419) {
            window.setTimeout(() => window.location.reload(), 2600);
        }

        event.preventDefault();
    });

    document.addEventListener('inertia:networkError', (event) => {
        const friendly = friendlyNetworkError();

        // Toast tetap terbuka sampai siswa menutupnya atau menekan Coba lagi,
        // karena kegagalan jaringan butuh tindakan lanjutan.
        toast.show({
            tone: 'error',
            title: friendly.title,
            description: friendly.description,
            duration: 0,
            action: { label: 'Coba lagi', onClick: () => void retryConnection() },
        });
        event.preventDefault();
    });
}

type InertiaPage = ComponentType<any> & {
    layout?: (page: ReactNode) => ReactNode;
};

const pages = import.meta.glob<{ default: InertiaPage }>(
    './Pages/**/*.tsx',
);

createInertiaApp({
    title: (title) => (title ? `${title} — ${appName}` : appName),
    resolve: (name) => {
        const page = pages[`./Pages/${name}.tsx`];

        if (!page) {
            throw new Error(`Halaman tidak ditemukan: ${name}`);
        }

        return page().then((module) => module.default);
    },
    setup({ el, App, props }) {
        if (!el) {
            return;
        }

        createRoot(el).render(<App {...props} />);
    },
    progress: {
        color: '#74182b',
    },
});
