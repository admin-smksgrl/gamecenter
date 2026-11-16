<!DOCTYPE html>
<html lang="id">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="robots" content="noindex">
        <title>@yield('title', 'Ada kendala') — Ruang Belajar</title>
        <style>
            :root {
                color-scheme: light;
                --canvas: #f5f2f2;
                --surface: #ffffff;
                --ink: #171114;
                --ink-soft: #6b6167;
                --rule: #e6dfdf;
                --red: #e60012;
                --red-deep: #b8000f;
                --red-tint: #ffebec;
                --shadow: 0 1px 2px rgb(23 17 20 / 0.04),
                    0 24px 48px -28px rgb(23 17 20 / 0.35);
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    color-scheme: dark;
                    --canvas: #0e0c0d;
                    --surface: #171214;
                    --ink: #f7f1f2;
                    --ink-soft: #b9adb2;
                    --rule: #2d2629;
                    --red: #ff3945;
                    --red-deep: #d2101c;
                    --red-tint: #3b1014;
                    --shadow: 0 1px 2px rgb(0 0 0 / 0.5),
                        0 24px 48px -28px rgb(0 0 0 / 0.9);
                }
            }

            * {
                box-sizing: border-box;
            }

            html,
            body {
                height: 100%;
            }

            body {
                margin: 0;
                display: grid;
                place-items: center;
                padding: 24px;
                background-color: var(--canvas);
                background-image: radial-gradient(
                    color-mix(in srgb, var(--ink) 7%, transparent) 1px,
                    transparent 1.1px
                );
                background-size: 24px 24px;
                color: var(--ink);
                font-family: 'Instrument Sans', ui-sans-serif, system-ui,
                    -apple-system, 'Segoe UI', sans-serif;
                -webkit-font-smoothing: antialiased;
            }

            .shell {
                width: 100%;
                max-width: 28rem;
            }

            .brand {
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 18px;
            }

            .mark {
                display: grid;
                place-items: center;
                width: 38px;
                height: 38px;
                border-radius: 12px;
                background-color: var(--red);
                color: #ffffff;
                box-shadow: 0 8px 18px -12px var(--red-deep);
            }

            .brand-text {
                display: flex;
                flex-direction: column;
                line-height: 1;
            }

            .brand-text strong {
                font-size: 16px;
                font-weight: 700;
                letter-spacing: -0.01em;
            }

            .brand-text small {
                margin-top: 5px;
                font-size: 8.5px;
                font-weight: 700;
                letter-spacing: 0.24em;
                text-transform: uppercase;
                color: var(--ink-soft);
            }

            .card {
                border: 1px solid var(--rule);
                border-radius: 20px;
                background-color: var(--surface);
                padding: 28px;
                box-shadow: var(--shadow);
            }

            .code {
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                background-color: var(--red-tint);
                padding: 5px 11px;
                font-size: 10px;
                font-weight: 800;
                letter-spacing: 0.16em;
                text-transform: uppercase;
                color: var(--red);
            }

            h1 {
                margin: 16px 0 0;
                font-size: clamp(24px, 5vw, 32px);
                line-height: 1.08;
                letter-spacing: -0.025em;
            }

            .message {
                margin: 12px 0 0;
                font-size: 13px;
                line-height: 1.65;
                font-weight: 500;
                color: var(--ink-soft);
            }

            .actions {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 22px;
            }

            .actions a,
            .actions button {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 38px;
                border-radius: 10px;
                padding: 8px 14px;
                font-family: inherit;
                font-size: 12px;
                font-weight: 700;
                text-decoration: none;
                cursor: pointer;
                transition: background-color 140ms ease, color 140ms ease;
            }

            .primary {
                border: 1px solid var(--red);
                background-color: var(--red);
                color: #ffffff;
            }

            .primary:hover {
                background-color: var(--red-deep);
                border-color: var(--red-deep);
            }

            .ghost {
                border: 1px solid var(--rule);
                background-color: transparent;
                color: var(--ink-soft);
            }

            .ghost:hover {
                background-color: var(--canvas);
                color: var(--ink);
            }

            .hint {
                margin: 18px 0 0;
                padding-top: 14px;
                border-top: 1px solid var(--rule);
                font-size: 11px;
                line-height: 1.6;
                font-weight: 500;
                color: var(--ink-soft);
            }

            .foot {
                margin: 18px 0 0;
                text-align: center;
                font-size: 10px;
                font-weight: 600;
                letter-spacing: 0.04em;
                color: var(--ink-soft);
            }

            :focus-visible {
                outline: 2px solid var(--red);
                outline-offset: 2px;
            }
        </style>
    </head>
    <body>
        <main class="shell">
            <div class="brand">
                <span class="mark" aria-hidden="true">
                    <svg
                        viewBox="0 0 24 24"
                        width="21"
                        height="21"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="1.8"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    >
                        <path d="M22 10 12 5 2 10l10 5 10-5Z" />
                        <path d="M6 12v4.5c0 1.4 2.7 2.5 6 2.5s6-1.1 6-2.5V12" />
                        <path d="M22 10v5" />
                    </svg>
                </span>
                <span class="brand-text">
                    <strong>Ruang Belajar</strong>
                    <small>Game Center</small>
                </span>
            </div>

            <section class="card">
                <span class="code">@yield('code', 'Kendala')</span>
                <h1>@yield('title', 'Ada kendala')</h1>
                <p class="message">@yield('message')</p>

                <div class="actions">
                    <a class="primary" href="/">Kembali ke beranda</a>
                    <button
                        type="button"
                        class="ghost"
                        onclick="if (history.length > 1) { history.back(); } else { location.href = '/'; }"
                    >
                        Halaman sebelumnya
                    </button>
                </div>

                <p class="hint">
                    @yield('hint', 'Kalau masalah ini terus muncul, hubungi gurumu atau admin sekolah.')
                </p>
            </section>

            <p class="foot">Ruang Belajar · Game Center Edukasi</p>
        </main>
    </body>
</html>
