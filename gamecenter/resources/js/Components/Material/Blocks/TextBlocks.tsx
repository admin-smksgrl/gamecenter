import type {
    CalloutBlock,
    CodeBlock,
    HeadingBlock,
    ListBlock,
    ParagraphBlock,
    TableBlock,
} from '@/lib/material/blocks';
import { cn } from '@/lib/utils';

/**
 * Renderer inline ringan: `**tebal**` dan `` `kode` ``.
 *
 * Dipakai bersama oleh materi lama (markdown) dan blok baru supaya penulisan
 * teks di kedua jalur tetap sama.
 */
export function Inline({ text }: { text: string }) {
    const parts = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);

    return (
        <>
            {parts.map((part, index) => {
                if (part.startsWith('**') && part.endsWith('**')) {
                    return <strong key={index}>{part.slice(2, -2)}</strong>;
                }

                if (part.startsWith('`') && part.endsWith('`')) {
                    return <code key={index}>{part.slice(1, -1)}</code>;
                }

                return <span key={index}>{part}</span>;
            })}
        </>
    );
}

export function HeadingBlockView({ block }: { block: HeadingBlock }) {
    const level = block.level ?? 3;

    if (level >= 4) {
        return (
            <h4>
                <Inline text={block.text} />
            </h4>
        );
    }

    // Level 2 dan 3 memakai gaya heading materi yang sudah ada agar tampilan
    // materi lama dan baru tidak berbeda.
    return (
        <h3>
            <Inline text={block.text} />
        </h3>
    );
}

export function ParagraphBlockView({ block }: { block: ParagraphBlock }) {
    return (
        <p>
            <Inline text={block.text} />
        </p>
    );
}

export function ListBlockView({ block }: { block: ListBlock }) {
    const items = Array.isArray(block.items) ? block.items : [];

    if (items.length === 0) {
        return null;
    }

    if (block.ordered) {
        return (
            <ol>
                {items.map((item, index) => (
                    <li key={index}>
                        <Inline text={String(item)} />
                    </li>
                ))}
            </ol>
        );
    }

    return (
        <ul>
            {items.map((item, index) => (
                <li key={index}>
                    <Inline text={String(item)} />
                </li>
            ))}
        </ul>
    );
}

export function TableBlockView({ block }: { block: TableBlock }) {
    const rows = (Array.isArray(block.rows) ? block.rows : []).filter(
        (row): row is string[] => Array.isArray(row) && row.length > 0,
    );

    if (rows.length === 0) {
        return null;
    }

    const [head, ...body] = rows;

    return (
        <table>
            <thead>
                <tr>
                    {head.map((cell, index) => (
                        <th key={index}>
                            <Inline text={String(cell)} />
                        </th>
                    ))}
                </tr>
            </thead>
            {body.length > 0 && (
                <tbody>
                    {body.map((row, rowIndex) => (
                        <tr key={rowIndex}>
                            {row.map((cell, cellIndex) => (
                                <td key={cellIndex}>
                                    <Inline text={String(cell)} />
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            )}
        </table>
    );
}

const CALLOUT_STYLE: Record<string, { wrapper: string; label: string }> = {
    info: {
        wrapper: 'border-ink/15 bg-canvas',
        label: 'ℹ️ Info',
    },
    success: {
        wrapper: 'border-emerald-500/30 bg-emerald-50/60',
        label: '✅ Kunci',
    },
    warn: {
        wrapper: 'border-amber-400/40 bg-amber-50/70',
        label: '⚠️ Perhatian',
    },
    danger: {
        wrapper: 'border-red/30 bg-red-tint',
        label: '⛔ Jangan',
    },
};

export function CalloutBlockView({ block }: { block: CalloutBlock }) {
    const tone = block.tone ?? 'info';
    const style = CALLOUT_STYLE[tone] ?? CALLOUT_STYLE.info;

    return (
        <div
            role="note"
            className={cn(
                'rounded-xl border px-3 py-2.5 text-[11px] leading-relaxed',
                style.wrapper,
            )}
        >
            <p className="mb-0.5 text-[8.5px] font-bold tracking-[0.1em] uppercase opacity-60">
                {style.label}
            </p>
            <p className="font-medium">
                <Inline text={block.text} />
            </p>
        </div>
    );
}

export function CodeBlockView({ block }: { block: CodeBlock }) {
    return (
        <figure>
            {block.language && (
                <figcaption className="mb-1 text-[8.5px] font-bold tracking-[0.1em] text-ink/35 uppercase">
                    {block.language}
                </figcaption>
            )}
            <pre>
                <code>{block.text}</code>
            </pre>
        </figure>
    );
}
