<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" class="h-full">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
        <meta name="theme-color" content="#e60012">
        <meta name="color-scheme" content="light dark">

        <script>
            (function () {
                try {
                    var stored = localStorage.getItem('gamecenter.theme');
                    var dark = stored
                        ? stored === 'dark'
                        : window.matchMedia('(prefers-color-scheme: dark)').matches;

                    document.documentElement.classList.toggle('dark', dark);
                    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';

                    var meta = document.querySelector('meta[name="theme-color"]');
                    if (meta) {
                        meta.setAttribute('content', dark ? '#0e0c0d' : '#e60012');
                    }
                } catch (error) {
                    // Theme falls back to the light palette.
                }
            })();
        </script>

        <title inertia>{{ config('app.name', 'Game Center Edukasi') }}</title>

        <link rel="manifest" href="/manifest.webmanifest">
        <link rel="icon" href="/favicon.ico" sizes="any">
        <link rel="icon" type="image/svg+xml" href="/icon.svg">
        <link rel="apple-touch-icon" href="/icon.svg">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-title" content="Ruang Belajar">

        @viteReactRefresh
        @vite(['resources/css/app.css', 'resources/js/app.tsx'])
        @inertiaHead
    </head>
    <body class="h-full overflow-hidden bg-canvas font-sans text-ink antialiased">
        @inertia
    </body>
</html>
