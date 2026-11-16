import { useEffect, useId, useRef, useState } from 'react';

type MermaidApi = typeof import('mermaid').default;

let mermaidLoader: Promise<MermaidApi> | null = null;

function loadMermaid(): Promise<MermaidApi> {
    mermaidLoader ??= import('mermaid').then((module) => module.default);

    return mermaidLoader;
}

const LIGHT_THEME = {
    background: '#ffffff',
    primaryColor: '#ffffff',
    primaryTextColor: '#171114',
    primaryBorderColor: '#e6dfdf',
    secondaryColor: '#ffebec',
    secondaryTextColor: '#b8000f',
    secondaryBorderColor: '#f3c9cc',
    tertiaryColor: '#f5f2f2',
    tertiaryTextColor: '#514a4e',
    tertiaryBorderColor: '#e6dfdf',
    lineColor: '#b8000f',
    textColor: '#171114',
    edgeLabelBackground: '#ffffff',
    fontSize: '12.5px',
};

const DARK_THEME = {
    background: '#171214',
    primaryColor: '#231c1f',
    primaryTextColor: '#f7f1f2',
    primaryBorderColor: '#4a3c41',
    secondaryColor: '#3b1014',
    secondaryTextColor: '#ff8b92',
    secondaryBorderColor: '#6b1a22',
    tertiaryColor: '#1d1719',
    tertiaryTextColor: '#c7bcc0',
    tertiaryBorderColor: '#2d2629',
    lineColor: '#ff3945',
    textColor: '#f7f1f2',
    edgeLabelBackground: '#171214',
    fontSize: '12.5px',
};

interface MermaidDiagramProps {
    chart: string;
    caption?: string;
}

export default function MermaidDiagram({ chart, caption }: MermaidDiagramProps) {
    const reactId = useId();
    const baseId = useRef(
        `mermaid-${reactId.replace(/[^a-zA-Z0-9]/g, '') || 'diagram'}`,
    );
    const [svg, setSvg] = useState('');
    const [failed, setFailed] = useState(false);
    const [themeTick, setThemeTick] = useState(0);

    useEffect(() => {
        const observer = new MutationObserver(() => {
            setThemeTick((tick) => tick + 1);
        });

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['class'],
        });

        return () => observer.disconnect();
    }, []);

    useEffect(() => {
        let cancelled = false;
        const dark = document.documentElement.classList.contains('dark');

        // Diagram ikut warna jenjang yang sedang aktif, bukan merah tetap.
        const levelRoot = document.querySelector('[data-level-theme]');
        const styles = levelRoot ? getComputedStyle(levelRoot) : null;
        const accent =
            styles?.getPropertyValue('--level-accent').trim() ||
            (dark ? '#ff3945' : '#e60012');
        const tint =
            styles?.getPropertyValue('--color-red-tint').trim() ||
            (dark ? '#3b1014' : '#ffebec');
        const base = dark ? DARK_THEME : LIGHT_THEME;
        const themeVariables = {
            ...base,
            secondaryColor: tint,
            secondaryTextColor: accent,
            secondaryBorderColor: accent,
            lineColor: accent,
        };

        setFailed(false);

        loadMermaid()
            .then(async (mermaid) => {
                mermaid.initialize({
                    startOnLoad: false,
                    securityLevel: 'strict',
                    theme: 'base',
                    fontFamily:
                        "'Instrument Sans Variable', ui-sans-serif, system-ui, sans-serif",
                    flowchart: {
                        useMaxWidth: true,
                        nodeSpacing: 26,
                        rankSpacing: 30,
                    },
                    themeVariables,
                });

                const { svg: rendered } = await mermaid.render(
                    `${baseId.current}-${themeTick}`,
                    chart,
                );

                if (!cancelled) {
                    setSvg(rendered);
                }
            })
            .catch(() => {
                if (!cancelled) {
                    setFailed(true);
                }
            });

        return () => {
            cancelled = true;
        };
    }, [chart, themeTick]);

    return (
        <figure className="my-1 overflow-hidden rounded-xl border border-rule bg-surface">
            <div className="overflow-hidden p-4 sm:p-5">
                {/* Chart strings are static app content; never pass user input here. */}
                {failed ? (
                    <p className="px-1 py-6 text-center text-[11.5px] font-medium text-ink/40">
                        Diagram tidak dapat dimuat. Versi teks tersedia di
                        sekitar bagian ini.
                    </p>
                ) : svg ? (
                    <div
                        role="img"
                        aria-label={caption ?? 'Diagram panduan'}
                        className="mermaid-figure mx-auto w-full max-w-full [&_svg]:h-auto [&_svg]:max-w-full"
                        dangerouslySetInnerHTML={{ __html: svg }}
                    />
                ) : (
                    <div className="flex min-h-28 items-center justify-center gap-2 text-[11px] font-semibold text-ink/35">
                        <span className="h-2 w-2 animate-pulse rounded-full bg-red" />
                        Memuat diagram…
                    </div>
                )}
            </div>
            {caption && (
                <figcaption className="border-t border-rule/70 bg-canvas/60 px-3 py-1.5 text-[10px] font-semibold text-ink/40">
                    {caption}
                </figcaption>
            )}
        </figure>
    );
}
