import { useMemo, useState } from 'react';

import type {
    ChartBlock,
    DiagramBlock,
    TimelineBlock,
} from '@/lib/material/blocks';
import { cn } from '@/lib/utils';
import { Inline } from '@/Components/Material/Blocks/TextBlocks';
import { renderDiagramSvg } from '@/lib/material/diagram';

/**
 * Blok visual non-interaktif: `diagram`, `chart`, dan `timeline` (plan §4.1).
 *
 * Prinsip yang dijaga:
 * - Setiap visual punya teks alternatif (`desc`, `caption`, atau ringkasan
 *   data) supaya pembaca layar tetap mendapat isinya (plan §7.2).
 * - Tidak ada pustaka grafik: `chart` digambar sebagai SVG sendiri agar ringan
 *   dan tetap tampil saat offline.
 * - Mermaid dimuat malas (dynamic import); bila gagal, kode diagram
 *   ditampilkan apa adanya, bukan kotak kosong.
 */

const CHART_COLORS = [
    'var(--color-red)',
    '#0f766e',
    '#b45309',
    '#4f46e5',
    '#0891b2',
    '#be123c',
];

const CHART_HEIGHT = 240;
const CHART_WIDTH = 460;
const PAD = { top: 16, right: 12, bottom: 36, left: 44 };

function Card({
    label,
    children,
}: {
    label: string;
    children: React.ReactNode;
}) {
    return (
        <figure className="rounded-xl border border-rule bg-surface px-3 py-2.5">
            <figcaption className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                {label}
            </figcaption>
            {children}
        </figure>
    );
}

/* ------------------------------------------------------------------ *
 * Diagram (subset Mermaid → SVG sendiri)
 * ------------------------------------------------------------------ */

/**
 * SVG dari konten guru tetap dibersihkan dari elemen aktif sebelum
 * disisipkan: skrip, iframe/foreignObject, dan atribut `on*` dibuang.
 */
function sanitizeSvg(raw: string): string {
    if (typeof window === 'undefined') {
        return '';
    }

    const parsed = new DOMParser().parseFromString(raw, 'image/svg+xml');
    const root = parsed.documentElement;

    if (!root || root.nodeName.toLowerCase() !== 'svg') {
        return '';
    }

    root.querySelectorAll('script, foreignObject, iframe').forEach((node) => {
        node.remove();
    });

    root.querySelectorAll('*').forEach((node) => {
        for (const attr of [...node.attributes]) {
            if (attr.name.startsWith('on')) {
                node.removeAttribute(attr.name);
            }
        }
    });

    return root.outerHTML;
}

export function DiagramBlockView({ block }: { block: DiagramBlock }) {
    const markup = useMemo(
        () =>
            block.engine === 'svg'
                ? sanitizeSvg(block.code)
                : renderDiagramSvg(block.code) ?? '',
        [block.code, block.engine],
    );

    return (
        <Card label="Diagram">
            {markup ? (
                <div
                    className="diagram-figure mt-1.5 overflow-x-auto"
                    role="img"
                    aria-label={block.desc ?? 'Diagram materi'}
                    dangerouslySetInnerHTML={{ __html: markup }}
                />
            ) : (
                <div className="mt-1.5">
                    {block.desc && (
                        <p className="text-[10.5px] leading-relaxed font-medium text-ink/60">
                            {block.desc}
                        </p>
                    )}

                    <pre className="mt-1 overflow-x-auto rounded-lg bg-canvas/70 px-2 py-1.5 text-[9.5px] leading-relaxed text-ink/60">
                        <code>{block.code}</code>
                    </pre>

                    <p className="mt-1 text-[9px] font-semibold text-ink/35">
                        Kode diagram tidak dapat digambar — isi di atas adalah
                        sumbernya.
                    </p>
                </div>
            )}
        </Card>
    );
}

/* ------------------------------------------------------------------ *
 * Grafik (SVG sendiri)
 * ------------------------------------------------------------------ */

function niceMax(value: number): number {
    if (value <= 0) {
        return 1;
    }

    const magnitude = 10 ** Math.floor(Math.log10(value));
    const step = [1, 2, 2.5, 5, 10].find(
        (candidate) => candidate * magnitude >= value,
    );

    return (step ?? 10) * magnitude;
}

function chartSummary(block: ChartBlock): string {
    if (block.desc) {
        return block.desc;
    }

    const parts = block.data.map((point) => `${point.label} ${point.value}`);

    return `${block.title ?? 'Grafik'}: ${parts.join(', ')}`;
}

export function ChartBlockView({ block }: { block: ChartBlock }) {
    const summary = chartSummary(block);
    const innerHeight = CHART_HEIGHT - PAD.top - PAD.bottom;

    const max = niceMax(Math.max(...block.data.map((point) => point.value)));

    // Label sumbu dibulatkan lalu diunikkan: nilai kecil (mis. 0,05) sering
    // tampil dobel bila hanya dipotong satu desimal.
    const ticks = [...new Set([0, 0.25, 0.5, 0.75, 1].map((ratio) =>
        String(Number((ratio * max).toFixed(3))),
    ))].map(Number);

    const yOf = (value: number) =>
        PAD.top + innerHeight - (value / max) * innerHeight;

    return (
        <Card label={block.kind === 'pie' ? 'Diagram lingkaran' : 'Grafik'}>
            {block.title && (
                <p className="mt-1 text-[11.5px] leading-snug font-bold text-ink">
                    {block.title}
                </p>
            )}

            <div className="mt-1.5">
                {block.kind === 'pie' ? (
                    <PieChart block={block} summary={summary} />
                ) : (
                    <svg
                        viewBox={`0 0 ${CHART_WIDTH} ${CHART_HEIGHT}`}
                        className="h-auto max-w-full"
                        role="img"
                        aria-label={summary}
                    >
                        {ticks.map((tick) => (
                            <g key={tick}>
                                <line
                                    x1={PAD.left}
                                    x2={CHART_WIDTH - PAD.right}
                                    y1={yOf(tick)}
                                    y2={yOf(tick)}
                                    stroke="currentColor"
                                    strokeOpacity={tick === 0 ? 0.35 : 0.12}
                                    strokeWidth={1}
                                />
                                <text
                                    x={PAD.left - 6}
                                    y={yOf(tick) + 3}
                                    textAnchor="end"
                                    className="fill-current text-[9px] opacity-45"
                                >
                                    {tick}
                                </text>
                            </g>
                        ))}

                        {block.kind === 'bar' ? (
                            <BarMarks block={block} max={max} yOf={yOf} />
                        ) : (
                            <LineMarks block={block} yOf={yOf} />
                        )}
                    </svg>
                )}
            </div>

            {block.kind === 'pie' && block.desc && (
                <p className="mt-1 text-[10px] leading-relaxed font-medium text-ink/55">
                    {block.desc}
                </p>
            )}
        </Card>
    );
}

function BarMarks({
    block,
    max,
    yOf,
}: {
    block: ChartBlock;
    max: number;
    yOf: (value: number) => number;
}) {
    const innerWidth = CHART_WIDTH - PAD.left - PAD.right;
    const slot = innerWidth / block.data.length;
    const barWidth = Math.min(46, slot * 0.62);

    return (
        <>
            {block.data.map((point, index) => {
                const x = PAD.left + slot * index + (slot - barWidth) / 2;
                const top = yOf(Math.max(point.value, 0));

                return (
                    <g key={`${point.label}-${index}`}>
                        <rect
                            x={x}
                            y={top}
                            width={barWidth}
                            height={Math.max(
                                CHART_HEIGHT - PAD.bottom - top,
                                0,
                            )}
                            rx={4}
                            fill={CHART_COLORS[index % CHART_COLORS.length]}
                            opacity={0.85}
                        />
                        <text
                            x={x + barWidth / 2}
                            y={yOf(point.value) - 4}
                            textAnchor="middle"
                            className="fill-current text-[9px] font-bold opacity-70"
                        >
                            {point.value}
                        </text>
                        <text
                            x={x + barWidth / 2}
                            y={CHART_HEIGHT - PAD.bottom + 12}
                            textAnchor="middle"
                            className="fill-current text-[9px] opacity-55"
                        >
                            {point.label.length > 12
                                ? `${point.label.slice(0, 11)}…`
                                : point.label}
                        </text>
                    </g>
                );
            })}
            <title>{`Nilai maksimum ${max}`}</title>
        </>
    );
}

function LineMarks({
    block,
    yOf,
}: {
    block: ChartBlock;
    yOf: (value: number) => number;
}) {
    const innerWidth = CHART_WIDTH - PAD.left - PAD.right;
    const step =
        block.data.length > 1 ? innerWidth / (block.data.length - 1) : 0;

    const points = block.data.map((point, index) => ({
        x: PAD.left + step * index,
        y: yOf(point.value),
        ...point,
    }));

    return (
        <>
            <polyline
                points={points.map((point) => `${point.x},${point.y}`).join(' ')}
                fill="none"
                stroke="var(--color-red)"
                strokeWidth={2}
                strokeLinejoin="round"
            />

            {points.map((point, index) => (
                <g key={`${point.label}-${index}`}>
                    <circle
                        cx={point.x}
                        cy={point.y}
                        r={3.4}
                        fill="var(--color-red)"
                    />
                    <text
                        x={point.x}
                        y={CHART_HEIGHT - PAD.bottom + 12}
                        textAnchor="middle"
                        className="fill-current text-[9px] opacity-55"
                    >
                        {point.label.length > 12
                            ? `${point.label.slice(0, 11)}…`
                            : point.label}
                    </text>
                </g>
            ))}
        </>
    );
}

function PieChart({ block, summary }: { block: ChartBlock; summary: string }) {
    const total = block.data.reduce(
        (sum, point) => sum + Math.max(point.value, 0),
        0,
    );
    const center = { x: 110, y: 105 };
    const radius = 78;

    let angle = -Math.PI / 2;

    return (
        <div className="flex flex-wrap items-center gap-3">
            <svg
                viewBox="0 0 220 210"
                className="h-auto w-[210px] max-w-full"
                role="img"
                aria-label={summary}
            >
                {total <= 0 ? (
                    <circle
                        cx={center.x}
                        cy={center.y}
                        r={radius}
                        fill="none"
                        stroke="currentColor"
                        strokeOpacity={0.2}
                    />
                ) : (
                    block.data.map((point, index) => {
                        const value = Math.max(point.value, 0);
                        const sweep = (value / total) * Math.PI * 2;
                        const start = angle;
                        const end = angle + sweep;
                        angle = end;

                        if (sweep <= 0) {
                            return null;
                        }

                        const x0 = center.x + radius * Math.cos(start);
                        const y0 = center.y + radius * Math.sin(start);
                        const x1 = center.x + radius * Math.cos(end);
                        const y1 = center.y + radius * Math.sin(end);
                        const largeArc = sweep > Math.PI ? 1 : 0;

                        const path =
                            block.data.length === 1
                                ? `M ${center.x} ${center.y - radius} A ${radius} ${radius} 0 1 1 ${center.x - 0.01} ${center.y - radius} Z`
                                : `M ${center.x} ${center.y} L ${x0} ${y0} A ${radius} ${radius} 0 ${largeArc} 1 ${x1} ${y1} Z`;

                        return (
                            <path
                                key={`${point.label}-${index}`}
                                d={path}
                                fill={CHART_COLORS[index % CHART_COLORS.length]}
                                opacity={0.85}
                                stroke="#ffffff"
                                strokeWidth={1.5}
                            />
                        );
                    })
                )}
            </svg>

            <ul className="grid flex-1 gap-1 text-[10px] font-medium text-ink/70">
                {block.data.map((point, index) => (
                    <li
                        key={`${point.label}-${index}`}
                        className="flex items-center gap-1.5"
                    >
                        <span
                            aria-hidden="true"
                            className="size-2.5 shrink-0 rounded-sm"
                            style={{
                                backgroundColor:
                                    CHART_COLORS[index % CHART_COLORS.length],
                            }}
                        />
                        <span className="flex-1">{point.label}</span>
                        <span className="font-bold text-ink/80">
                            {point.value}
                            {total > 0 && (
                                <span className="ml-1 font-medium text-ink/40">
                                    {Math.round((point.value / total) * 100)}%
                                </span>
                            )}
                        </span>
                    </li>
                ))}
            </ul>
        </div>
    );
}

/* ------------------------------------------------------------------ *
 * Lini masa
 * ------------------------------------------------------------------ */

export function TimelineBlockView({ block }: { block: TimelineBlock }) {
    return (
        <Card label="Lini masa">
            <ol className="mt-1.5 space-y-0">
                {block.items.map((item, index) => {
                    const last = index === block.items.length - 1;

                    return (
                        <li key={`${item.when}-${index}`} className="flex gap-2.5">
                            <div className="flex flex-col items-center">
                                <span
                                    aria-hidden="true"
                                    className={cn(
                                        'mt-1 size-2 shrink-0 rounded-full',
                                        'bg-red',
                                    )}
                                />
                                {!last && (
                                    <span
                                        aria-hidden="true"
                                        className="my-0.5 w-px flex-1 bg-rule"
                                    />
                                )}
                            </div>

                            <div className={cn('min-w-0 flex-1', !last && 'pb-2.5')}>
                                <p className="text-[9px] font-bold tracking-wide text-red uppercase">
                                    {item.when}
                                </p>
                                <p className="text-[11px] leading-snug font-bold text-ink">
                                    {item.title}
                                </p>
                                {item.body && (
                                    <p className="mt-0.5 text-[10px] leading-relaxed font-medium text-ink/55">
                                        <Inline text={item.body} />
                                    </p>
                                )}
                            </div>
                        </li>
                    );
                })}
            </ol>
        </Card>
    );
}

/* ------------------------------------------------------------------ *
 * Gambar berlabel (hotspots)
 * ------------------------------------------------------------------ */

export function HotspotsBlockView({
    block,
}: {
    block: import('@/lib/material/blocks').HotspotsBlock;
}) {
    const [opened, setOpened] = useState<string[]>([]);
    const [active, setActive] = useState<string | null>(null);

    const activePoint = block.points.find((point) => point.id === active);

    function open(id: string) {
        setActive(id);
        setOpened((current) =>
            current.includes(id) ? current : [...current, id],
        );
    }

    return (
        <figure
            className="rounded-xl border border-rule bg-surface px-3 py-2.5"
        >
            <figcaption className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                Gambar berlabel · ketuk titik untuk membaca
            </figcaption>

            <div className="relative mt-1.5 overflow-hidden rounded-lg border border-rule bg-canvas/40">
                <img
                    src={block.image_url}
                    alt={block.caption ?? 'Gambar materi'}
                    loading="lazy"
                    className="block w-full"
                />

                {block.points.map((point, index) => {
                    const isActive = active === point.id;
                    const isOpen = opened.includes(point.id);

                    return (
                        <button
                            key={point.id}
                            type="button"
                            onClick={() => open(point.id)}
                            aria-pressed={isActive}
                            aria-label={`Titik ${index + 1}: ${point.label}`}
                            style={{
                                left: `${point.x * 100}%`,
                                top: `${point.y * 100}%`,
                            }}
                            className={cn(
                                'absolute flex size-6 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border text-[9px] font-bold shadow-sm transition-colors',
                                isActive
                                    ? 'border-red bg-red text-white'
                                    : isOpen
                                      ? 'border-red/40 bg-white text-red'
                                      : 'border-red/50 bg-white/95 text-red hover:bg-red hover:text-white',
                            )}
                        >
                            {index + 1}
                        </button>
                    );
                })}
            </div>

            <div aria-live="polite" className="mt-1.5">
                {activePoint ? (
                    <div className="rounded-lg border border-rule bg-canvas/60 px-2.5 py-1.5">
                        <p className="text-[10px] font-bold text-ink">
                            {activePoint.label}
                        </p>
                        {activePoint.body && (
                            <p className="mt-0.5 text-[10px] leading-relaxed font-medium text-ink/60">
                                <Inline text={activePoint.body} />
                            </p>
                        )}
                    </div>
                ) : (
                    <p className="text-[9.5px] font-medium text-ink/40">
                        {block.caption}
                    </p>
                )}
            </div>

            <p className="mt-1 text-[9px] font-medium text-ink/35">
                Terbuka {opened.length} dari {block.points.length} titik
            </p>

            {/* Daftar teks: pembaca layar & pengguna keyboard tidak bergantung
                pada posisi titik di gambar (plan §7.2). */}
            <details className="mt-1">
                <summary className="cursor-pointer text-[9px] font-bold text-ink/40">
                    Daftar titik
                </summary>
                <dl className="mt-1 space-y-1">
                    {block.points.map((point) => (
                        <div key={`list-${point.id}`}>
                            <dt className="text-[9.5px] font-bold text-ink/70">
                                {point.label}
                            </dt>
                            <dd className="text-[9.5px] leading-relaxed font-medium text-ink/50">
                                {point.body ? <Inline text={point.body} /> : '—'}
                            </dd>
                        </div>
                    ))}
                </dl>
            </details>
        </figure>
    );
}
