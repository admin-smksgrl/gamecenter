/*
 * Service Worker — Game Center Edukasi (offline-first app shell).
 *
 * Strategi:
 * - Navigasi: network-first, fallback ke halaman HTML ter-cache, lalu
 *   /offline.html bila belum pernah dibuka.
 * - Aset statis (/build, font, ikon): cache-first.
 * - Request Inertia (X-Inertia): diteruskan langsung ke jaringan tanpa
 *   intercept (respons JSON tidak di-cache agar data pengguna tidak
 *   tersimpan di perangkat bersama, dan kegagalan jaringan tetap terbaca
 *   sebagai error jaringan oleh Inertia).
 * - POST /keluar: bersihkan cache halaman berisi data pengguna.
 *
 * Naikkan CACHE_VERSION setiap rilis agar cache lama dibuang.
 */

const CACHE_VERSION = '0.33.0';
const SHELL_CACHE = `gamecenter-shell-${CACHE_VERSION}`;
const PAGE_CACHE = `gamecenter-pages-${CACHE_VERSION}`;
const ASSET_CACHE = `gamecenter-assets-${CACHE_VERSION}`;
const OFFLINE_URL = '/offline.html';
const MAX_PAGE_ENTRIES = 30;
const PRECACHE = [OFFLINE_URL, '/manifest.webmanifest', '/icon.svg'];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches
            .open(SHELL_CACHE)
            .then((cache) => cache.addAll(PRECACHE))
            .then(() => self.skipWaiting()),
    );
});

self.addEventListener('activate', (event) => {
    const keep = [SHELL_CACHE, PAGE_CACHE, ASSET_CACHE];

    event.waitUntil(
        caches
            .keys()
            .then((keys) =>
                Promise.all(
                    keys
                        .filter((key) => !keep.includes(key))
                        .map((key) => caches.delete(key)),
                ),
            )
            .then(() => self.clients.claim()),
    );
});

self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);

    if (request.method !== 'GET') {
        if (request.method === 'POST' && url.pathname === '/keluar') {
            event.waitUntil(clearPrivateCaches());
        }

        return;
    }

    if (url.origin !== self.location.origin) {
        return;
    }

    if (
        url.pathname.startsWith('/admin') ||
        url.pathname.startsWith('/api/') ||
        url.pathname.startsWith('/sanctum') ||
        url.pathname === '/up'
    ) {
        return;
    }

    // Kunjungan Inertia (X-Inertia) sengaja TIDAK di-intercept. Saat server
    // tidak terjangkau, biarkan fetch gagal secara alami supaya aplikasi
    // menampilkan pesan "Tidak tersambung ke server", bukan pesan 503
    // "Layanan sedang sibuk" yang menyesatkan (lihat changelog 0.22.1).
    if (request.headers.get('X-Inertia')) {
        return;
    }

    if (request.mode === 'navigate') {
        event.respondWith(handleNavigation(request));

        return;
    }

    if (isStaticAsset(url.pathname)) {
        event.respondWith(cacheFirst(request));

        return;
    }

    event.respondWith(staleWhileRevalidate(request));
});

/**
 * Background Sync: beri tahu tab yang terbuka untuk mengirim antrean
 * IndexedDB (antrean & auth tetap ditangani konteks halaman).
 */
self.addEventListener('sync', (event) => {
    if (event.tag !== 'gamecenter-sync') {
        return;
    }

    event.waitUntil(
        self.clients
            .matchAll({ type: 'window', includeUncontrolled: true })
            .then((clients) => {
                clients.forEach((client) => {
                    client.postMessage({ type: 'gamecenter:sync' });
                });
            }),
    );
});

async function handleNavigation(request) {
    try {
        const response = await fetch(request);

        if (response.ok && isHtml(response)) {
            const cache = await caches.open(PAGE_CACHE);

            await cache.put(request, response.clone());
            await trimCache(PAGE_CACHE, MAX_PAGE_ENTRIES);
        }

        return response;
    } catch {
        const cached = await caches.match(request);

        if (cached) {
            return cached;
        }

        const offline = await caches.match(OFFLINE_URL);

        return offline ?? Response.error();
    }
}

async function cacheFirst(request) {
    const cached = await caches.match(request);

    if (cached) {
        return cached;
    }

    const response = await fetch(request);

    if (response.ok) {
        const cache = await caches.open(ASSET_CACHE);

        await cache.put(request, response.clone());
    }

    return response;
}

async function staleWhileRevalidate(request) {
    const cache = await caches.open(ASSET_CACHE);
    const cached = await cache.match(request);
    const network = fetch(request)
        .then((response) => {
            if (response.ok) {
                void cache.put(request, response.clone());
            }

            return response;
        })
        .catch(() => null);

    return cached ?? (await network) ?? Response.error();
}

async function clearPrivateCaches() {
    await caches.delete(PAGE_CACHE);
}

async function trimCache(cacheName, maxEntries) {
    const cache = await caches.open(cacheName);
    const keys = await cache.keys();

    if (keys.length <= maxEntries) {
        return;
    }

    await Promise.all(
        keys
            .slice(0, keys.length - maxEntries)
            .map((request) => cache.delete(request)),
    );
}

function isHtml(response) {
    return (response.headers.get('Content-Type') || '').includes('text/html');
}

function isStaticAsset(pathname) {
    return (
        pathname.startsWith('/build/') ||
        pathname.startsWith('/fonts/') ||
        pathname.startsWith('/css/') ||
        pathname.startsWith('/js/') ||
        // Gambar buku ajar hasil ekstraksi (plan §6.0) ikut di-cache supaya
        // blok visual tetap tampil saat offline.
        pathname.startsWith('/media/') ||
        /\.(?:css|js|woff2?|ttf|png|jpe?g|svg|ico|webp)$/i.test(pathname)
    );
}
