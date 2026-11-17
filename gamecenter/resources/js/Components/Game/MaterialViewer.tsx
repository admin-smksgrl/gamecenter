import { useEffect, useMemo, useState } from 'react';

import BlockRenderer from '@/Components/Material/BlockRenderer';
import { Inline } from '@/Components/Material/Blocks/TextBlocks';
import { normalizeBlocks, legacyValueBlocks } from '@/lib/material/blocks';
import type { MaterialBlockPayload } from '@/lib/material/store';
import { cn } from '@/lib/utils';

export interface MaterialProp {
    id: number;
    type: string;
    type_label: string;
    title: string;
    content: string | null;
    /** Blok interaktif (plan-materi-interaktif §3.2). Kosong = pakai markdown. */
    blocks: unknown[] | null;
    media_url: string | null;
    media_type: string | null;
    duration: number | null;
    order: number;
    source_reference: string | null;
}

interface MaterialViewerProps {
    materials: MaterialProp[];
    chapterId: number;
    initialRead: number;
    isLoggedIn: boolean;
    onRead: (readCount: number) => void;
    /** Dipanggil setiap blok aktivitas selesai diperiksa (plan §3.4.2). */
    onBlockRecord?: (payload: MaterialBlockPayload) => void;
}

const TYPE_ICON: Record<string, string> = {
    text: '📖',
    video: '🎬',
    image: '🖼️',
    audio: '🔊',
    interactive: '🧩',
    visual: '📊',
    scenario: '🎭',
    game: '🎮',
};

type Block =
    | { kind: 'heading'; text: string }
    | { kind: 'list'; items: string[] }
    | { kind: 'code'; text: string }
    | { kind: 'table'; rows: string[][] }
    | { kind: 'paragraph'; text: string };

function storageKey(chapterId: number): string {
    return `gamecenter.materials.${chapterId}`;
}

function loadReadIds(key: string): number[] {
    if (typeof window === 'undefined') {
        return [];
    }

    try {
        const raw = window.localStorage.getItem(key);
        const parsed = raw ? (JSON.parse(raw) as unknown) : [];

        return Array.isArray(parsed)
            ? parsed.filter((id): id is number => typeof id === 'number')
            : [];
    } catch {
        return [];
    }
}

function saveReadIds(key: string, ids: number[]) {
    try {
        window.localStorage.setItem(key, JSON.stringify(ids));
    } catch {
        // Penyimpanan lokal bisa diblokir; status baca tetap di memori.
    }
}

function parseBlocks(content: string): Block[] {
    const lines = content.replace(/\r\n/g, '\n').split('\n');
    const blocks: Block[] = [];
    let index = 0;

    while (index < lines.length) {
        const line = lines[index];
        const trimmed = line.trim();

        if (trimmed === '') {
            index += 1;
            continue;
        }

        if (trimmed.startsWith('```')) {
            const code: string[] = [];
            index += 1;

            while (index < lines.length && !lines[index].trim().startsWith('```')) {
                code.push(lines[index]);
                index += 1;
            }

            index += 1;
            blocks.push({ kind: 'code', text: code.join('\n') });
            continue;
        }

        if (trimmed.startsWith('### ')) {
            blocks.push({ kind: 'heading', text: trimmed.slice(4).trim() });
            index += 1;
            continue;
        }

        if (trimmed.startsWith('## ')) {
            blocks.push({ kind: 'heading', text: trimmed.slice(3).trim() });
            index += 1;
            continue;
        }

        if (trimmed.startsWith('- ')) {
            const items: string[] = [];

            while (
                index < lines.length &&
                lines[index].trim().startsWith('- ')
            ) {
                items.push(lines[index].trim().slice(2).trim());
                index += 1;
            }

            blocks.push({ kind: 'list', items });
            continue;
        }

        if (trimmed.startsWith('|')) {
            const rows: string[][] = [];

            while (
                index < lines.length &&
                lines[index].trim().startsWith('|')
            ) {
                const row = lines[index].trim();
                index += 1;

                if (/^[|\s:-]+$/.test(row)) {
                    continue;
                }

                rows.push(
                    row
                        .replace(/^\|/, '')
                        .replace(/\|$/, '')
                        .split('|')
                        .map((cell) => cell.trim()),
                );
            }

            if (rows.length > 0) {
                blocks.push({ kind: 'table', rows });
            }

            continue;
        }

        const paragraph: string[] = [];

        while (
            index < lines.length &&
            lines[index].trim() !== '' &&
            !lines[index].trim().startsWith('#') &&
            !lines[index].trim().startsWith('- ') &&
            !lines[index].trim().startsWith('|') &&
            !lines[index].trim().startsWith('```')
        ) {
            paragraph.push(lines[index].trim());
            index += 1;
        }

        blocks.push({ kind: 'paragraph', text: paragraph.join(' ') });
    }

    return blocks;
}

function MaterialBody({ content }: { content: string }) {
    const blocks = useMemo(() => parseBlocks(content), [content]);

    return (
        <div className="material-prose">
            {blocks.map((block, index) => {
                if (block.kind === 'heading') {
                    return <h3 key={index}>{block.text}</h3>;
                }

                if (block.kind === 'list') {
                    return (
                        <ul key={index}>
                            {block.items.map((item, itemIndex) => (
                                <li key={itemIndex}>
                                    <Inline text={item} />
                                </li>
                            ))}
                        </ul>
                    );
                }

                if (block.kind === 'code') {
                    return (
                        <pre key={index}>
                            <code>{block.text}</code>
                        </pre>
                    );
                }

                if (block.kind === 'table') {
                    const [head, ...body] = block.rows;

                    return (
                        <table key={index}>
                            <thead>
                                <tr>
                                    {head.map((cell, cellIndex) => (
                                        <th key={cellIndex}>
                                            <Inline text={cell} />
                                        </th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {body.map((row, rowIndex) => (
                                    <tr key={rowIndex}>
                                        {row.map((cell, cellIndex) => (
                                            <td key={cellIndex}>
                                                <Inline text={cell} />
                                            </td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    );
                }

                return (
                    <p key={index}>
                        <Inline text={block.text} />
                    </p>
                );
            })}
        </div>
    );
}

/**
 * Memilih sumber render (plan §3.3):
 * - materi dengan blok baru → `BlockRenderer`;
 * - materi lama → markdown, ditambah daftar blok `{type, value}` bila ada
 *   (bentuk lama yang masih dipakai materi PAUD/TK).
 */
function MaterialContent({
    material,
    onBlockRecord,
}: {
    material: MaterialProp;
    onBlockRecord?: (payload: MaterialBlockPayload) => void;
}) {
    const blocks = useMemo(
        () => normalizeBlocks(material.blocks),
        [material.blocks],
    );
    const legacyBlocks = useMemo(
        () => legacyValueBlocks(material.blocks),
        [material.blocks],
    );

    if (blocks.length > 0) {
        return (
            <BlockRenderer
                blocks={blocks}
                materialId={material.id}
                onRecord={onBlockRecord}
            />
        );
    }

    return (
        <>
            {material.content && <MaterialBody content={material.content} />}

            {legacyBlocks.length > 0 && (
                <ul className="mt-2 grid gap-1">
                    {legacyBlocks.map((block, index) => (
                        <li
                            key={index}
                            className="rounded-lg bg-surface px-2.5 py-1.5 text-[10.5px] font-medium text-ink/55 ring-1 ring-rule"
                        >
                            {block.value}
                        </li>
                    ))}
                </ul>
            )}
        </>
    );
}

function formatMaterialDuration(seconds: number | null): string | null {
    if (!seconds || seconds <= 0) {
        return null;
    }

    const minutes = Math.max(1, Math.round(seconds / 60));

    return `${minutes} menit baca`;
}

export default function MaterialViewer({
    materials,
    chapterId,
    initialRead,
    isLoggedIn,
    onRead,
    onBlockRecord,
}: MaterialViewerProps) {
    const key = storageKey(chapterId);
    const [readIds, setReadIds] = useState<number[]>(() => loadReadIds(key));
    const [readCount, setReadCount] = useState<number>(() =>
        Math.max(0, Math.min(initialRead, materials.length)),
    );
    const [openId, setOpenId] = useState<number | null>(
        materials[0]?.id ?? null,
    );

    useEffect(() => {
        setReadCount((current) =>
            Math.max(current, Math.min(initialRead, materials.length)),
        );
    }, [initialRead, materials.length]);

    useEffect(() => {
        setReadCount((current) =>
            Math.max(current, Math.min(readIds.length, materials.length)),
        );
    }, [readIds, materials.length]);

    if (materials.length === 0) {
        return null;
    }

    const percent = Math.round((readCount / materials.length) * 100);

    function markRead(materialId: number) {
        if (readIds.includes(materialId)) {
            return;
        }

        const next = [...readIds, materialId];
        const nextCount = Math.min(materials.length, readCount + 1);

        setReadIds(next);
        setReadCount(nextCount);
        saveReadIds(key, next);
        onRead(nextCount);
    }

    return (
        <section className="mt-3 overflow-hidden rounded-[24px] border border-rule bg-surface shadow-card">
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-rule px-4 py-3.5 sm:px-5">
                <div className="min-w-0">
                    <p className="text-[9px] font-bold tracking-[0.16em] text-red uppercase">
                        Materi pembelajaran · 60%
                    </p>
                    <h2 className="display mt-0.5 text-[20px] leading-tight text-ink">
                        Baca dulu, main lebih mudah
                    </h2>
                    <p className="mt-0.5 text-[10.5px] font-medium text-ink/40">
                        {materials.length} materi singkat dari buku resmi.
                        Tandai yang sudah dibaca.
                    </p>
                </div>

                <div className="min-w-[140px] flex-1 sm:max-w-[220px]">
                    <div className="flex items-center justify-between text-[9.5px] font-bold text-ink/40">
                        <span>
                            {readCount}/{materials.length} dibaca
                        </span>
                        <span className="text-red">{percent}%</span>
                    </div>
                    <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-ink/[0.07]">
                        <div
                            className="h-full rounded-full bg-red transition-[width] duration-300"
                            style={{ width: `${percent}%` }}
                        />
                    </div>
                </div>
            </div>

            <div className="divide-y divide-rule/70">
                {materials.map((material, index) => {
                    const isOpen = openId === material.id;
                    const isRead = readIds.includes(material.id);
                    const duration = formatMaterialDuration(material.duration);

                    return (
                        <article key={material.id}>
                            <button
                                type="button"
                                onClick={() =>
                                    setOpenId(isOpen ? null : material.id)
                                }
                                aria-expanded={isOpen}
                                className="flex w-full items-start gap-3 px-4 py-3 text-left transition-colors hover:bg-canvas/50 sm:px-5"
                            >
                                <span className="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-canvas text-[17px] ring-1 ring-rule">
                                    {TYPE_ICON[material.type] ?? '📘'}
                                </span>

                                <span className="min-w-0 flex-1">
                                    <span className="flex flex-wrap items-center gap-1.5">
                                        <span className="text-[8.5px] font-bold tracking-[0.12em] text-ink/35 uppercase">
                                            Materi {index + 1} ·{' '}
                                            {material.type_label}
                                        </span>
                                        {isRead && (
                                            <span className="rounded-full bg-red-tint px-1.5 py-0.5 text-[8px] font-bold text-red">
                                                Sudah dibaca
                                            </span>
                                        )}
                                    </span>
                                    <span className="mt-0.5 block text-[12.5px] leading-snug font-bold text-ink">
                                        {material.title}
                                    </span>
                                    {duration && (
                                        <span className="mt-0.5 block text-[9.5px] font-medium text-ink/35">
                                            {duration}
                                        </span>
                                    )}
                                </span>

                                <span
                                    aria-hidden
                                    className={cn(
                                        'mt-1 shrink-0 text-[10px] font-bold text-ink/30 transition-transform duration-200',
                                        isOpen && 'rotate-180',
                                    )}
                                >
                                    ▾
                                </span>
                            </button>

                            {isOpen && (
                                <div className="px-4 pb-4 sm:px-5">
                                    <div className="rounded-xl border border-rule bg-canvas/40 px-3.5 py-3">
                                        {material.content ||
                                        (material.blocks?.length ?? 0) > 0 ? (
                                            <MaterialContent
                                                material={material}
                                                onBlockRecord={onBlockRecord}
                                            />
                                        ) : (
                                            <p className="text-[11px] font-medium text-ink/45">
                                                Materi ini berupa aktivitas
                                                interaktif. Ikuti petunjuk pada
                                                sesi bermain.
                                            </p>
                                        )}

                                        {material.source_reference && (
                                            <p className="mt-2 text-[9px] font-medium text-ink/30">
                                                Sumber: {material.source_reference}
                                            </p>
                                        )}
                                    </div>

                                    <div className="mt-2 flex flex-wrap items-center justify-between gap-2">
                                        <p className="text-[9.5px] font-medium text-ink/35">
                                            {isLoggedIn
                                                ? 'Progres baca ikut tersinkron saat online.'
                                                : 'Masuk agar progres baca tersimpan.'}
                                        </p>
                                        <button
                                            type="button"
                                            onClick={() =>
                                                markRead(material.id)
                                            }
                                            disabled={isRead}
                                            className="inline-flex h-8 items-center gap-1.5 rounded-lg bg-red px-3 text-[10px] font-bold text-white shadow-fab transition-colors hover:bg-red-deep disabled:pointer-events-none disabled:bg-red"
                                        >
                                            {isRead
                                                ? '✓ Sudah dibaca'
                                                : 'Tandai sudah dibaca'}
                                        </button>
                                    </div>
                                </div>
                            )}
                        </article>
                    );
                })}
            </div>
        </section>
    );
}
