/**
 * Model data blok materi interaktif (plan-materi-interaktif §3.2).
 *
 * Satu materi menyimpan `blocks` sebagai array berurutan. Renderer merangkai
 * dari atas ke bawah. Berkas ini hanya berisi **tipe dan normalisasi**; tidak
 * ada komponen React di sini supaya bisa diuji dan dipakai di luar renderer.
 *
 * Aturan yang dijaga:
 * - `id` blok opsional tetapi wajib unik di dalam satu materi bila diisi
 *   (dipakai untuk menyimpan jawaban siswa).
 * - Blok aktivitas tidak pernah menentukan skor sesi resmi.
 * - Gambar hasil ekstraksi PDF wajib menyertakan `image_source`.
 */

export type MaterialBlockTone = 'info' | 'success' | 'warn' | 'danger';

/**
 * Jejak aset gambar hasil ekstraksi buku ajar (plan §6.0).
 * Validator server menolak blok visual tanpa `book` + `page`.
 */
export interface MaterialImageSource {
    book: string;
    page: number;
    figure?: string;
}

interface BlockBase {
    id?: string;
}

/* ------------------------------------------------------------------ *
 * Blok teks (tanpa interaksi)
 * ------------------------------------------------------------------ */

export interface HeadingBlock extends BlockBase {
    type: 'heading';
    text: string;
    level?: 2 | 3 | 4;
}

export interface ParagraphBlock extends BlockBase {
    type: 'paragraph';
    text: string;
}

export interface ListBlock extends BlockBase {
    type: 'list';
    items: string[];
    ordered?: boolean;
}

export interface TableBlock extends BlockBase {
    type: 'table';
    /** Baris pertama dipakai sebagai header. */
    rows: string[][];
}

export interface CalloutBlock extends BlockBase {
    type: 'callout';
    text: string;
    tone?: MaterialBlockTone;
}

export interface CodeBlock extends BlockBase {
    type: 'code';
    text: string;
    language?: string;
}

/* ------------------------------------------------------------------ *
 * Visual learning (Fase 3)
 * ------------------------------------------------------------------ */

export interface DiagramBlock extends BlockBase {
    type: 'diagram';
    /**
     * `mermaid` = subset sintaks `graph TD/LR` yang dirender sendiri oleh
     * `lib/material/diagram.ts` (tanpa pustaka Mermaid di halaman materi).
     * `svg` = SVG manual dari penulis materi, disanitasi sebelum disisipkan.
     */
    engine: 'mermaid' | 'svg';
    code: string;
    /** Teks alternatif setara untuk pembaca layar (plan §7.2). */
    desc?: string;
}

export interface ChartPoint {
    label: string;
    value: number;
}

export interface ChartBlock extends BlockBase {
    type: 'chart';
    kind: 'bar' | 'line' | 'pie';
    title?: string;
    data: ChartPoint[];
    desc?: string;
}

export interface HotspotPoint {
    id: string;
    /** Posisi ternormalisasi 0..1 agar akurat di resolusi berbeda. */
    x: number;
    y: number;
    label: string;
    body?: string;
}

export interface HotspotsBlock extends BlockBase {
    type: 'hotspots';
    image_url: string;
    image_source?: MaterialImageSource;
    caption?: string;
    points: HotspotPoint[];
}

export interface TimelineItem {
    when: string;
    title: string;
    body?: string;
}

export interface TimelineBlock extends BlockBase {
    type: 'timeline';
    items: TimelineItem[];
}

/* ------------------------------------------------------------------ *
 * Hafalan (Fase 2)
 * ------------------------------------------------------------------ */

export interface GlossaryTerm {
    term: string;
    definition: string;
}

export interface GlossaryBlock extends BlockBase {
    type: 'glossary';
    terms: GlossaryTerm[];
}

export interface Flashcard {
    front: string;
    back: string;
}

export interface FlashcardsBlock extends BlockBase {
    type: 'flashcards';
    cards: Flashcard[];
}

/* ------------------------------------------------------------------ *
 * Aktivitas (Fase 2 & 4)
 * ------------------------------------------------------------------ */

export interface BlockFeedback {
    correct?: string;
    wrong?: string;
}

export interface SortBlock extends BlockBase {
    type: 'sort';
    prompt: string;
    items: Array<{ id: string; text: string }>;
    /** Urutan id yang benar. */
    answer: string[];
    feedback?: BlockFeedback;
}

export interface CategorizeBucket {
    id: string;
    label: string;
}

export interface CategorizeItem {
    id: string;
    text: string;
    bucket: string;
}

export interface CategorizeBlock extends BlockBase {
    type: 'categorize';
    prompt: string;
    buckets: CategorizeBucket[];
    items: CategorizeItem[];
    feedback?: BlockFeedback;
}

export interface LabelTarget {
    id: string;
    x: number;
    y: number;
    answer: string;
}

export interface LabelBlock extends BlockBase {
    type: 'label';
    prompt: string;
    image_url: string;
    image_source?: MaterialImageSource;
    targets: LabelTarget[];
    choices: string[];
    feedback?: BlockFeedback;
}

export interface CheckpointChoice {
    id: string;
    text: string;
    correct?: boolean;
}

export interface CheckpointBlock extends BlockBase {
    type: 'checkpoint';
    question: string;
    choices: CheckpointChoice[];
    explanation?: string;
    feedback?: BlockFeedback;
}

export interface ScenarioChoice {
    text: string;
    next?: string;
    score?: number;
    feedback?: string;
}

export interface ScenarioNode {
    id: string;
    text: string;
    choices?: ScenarioChoice[];
    end?: boolean;
    outcome?: 'good' | 'bad' | 'neutral';
}

export interface ScenarioBlock extends BlockBase {
    type: 'scenario';
    title: string;
    start: string;
    nodes: ScenarioNode[];
}

export interface ChallengeItem {
    question: string;
    answer: string;
}

export interface ChallengeBlock extends BlockBase {
    type: 'challenge';
    title?: string;
    time_limit?: number;
    items: ChallengeItem[];
    feedback?: BlockFeedback;
}

/* ------------------------------------------------------------------ *
 * Union & normalisasi
 * ------------------------------------------------------------------ */

export type MaterialTextBlock =
    | HeadingBlock
    | ParagraphBlock
    | ListBlock
    | TableBlock
    | CalloutBlock
    | CodeBlock;

export type MaterialVisualBlock =
    | DiagramBlock
    | ChartBlock
    | HotspotsBlock
    | TimelineBlock;

export type MaterialRecallBlock = GlossaryBlock | FlashcardsBlock;

export type MaterialActivityBlock =
    | SortBlock
    | CategorizeBlock
    | LabelBlock
    | CheckpointBlock
    | ScenarioBlock
    | ChallengeBlock;

export type MaterialBlock =
    | MaterialTextBlock
    | MaterialVisualBlock
    | MaterialRecallBlock
    | MaterialActivityBlock;

export type MaterialBlockType = MaterialBlock['type'];

/**
 * Daftar tipe yang dikenal renderer. Dipakai untuk menolak blok asing saat
 * normalisasi supaya satu blok rusak tidak menjatuhkan seluruh materi.
 */
export const MATERIAL_BLOCK_TYPES: readonly MaterialBlockType[] = [
    'heading',
    'paragraph',
    'list',
    'table',
    'callout',
    'code',
    'diagram',
    'chart',
    'hotspots',
    'timeline',
    'glossary',
    'flashcards',
    'sort',
    'categorize',
    'label',
    'checkpoint',
    'scenario',
    'challenge',
];

const TEXT_BLOCK_TYPES: readonly MaterialBlockType[] = [
    'heading',
    'paragraph',
    'list',
    'table',
    'callout',
    'code',
];

const ACTIVITY_BLOCK_TYPES: readonly MaterialBlockType[] = [
    'sort',
    'categorize',
    'label',
    'checkpoint',
    'scenario',
    'challenge',
];

export function isTextBlock(block: MaterialBlock): block is MaterialTextBlock {
    return TEXT_BLOCK_TYPES.includes(block.type);
}

export function isActivityBlock(
    block: MaterialBlock,
): block is MaterialActivityBlock {
    return ACTIVITY_BLOCK_TYPES.includes(block.type);
}

export function isMaterialBlockType(value: unknown): value is MaterialBlockType {
    return (
        typeof value === 'string' &&
        (MATERIAL_BLOCK_TYPES as readonly string[]).includes(value)
    );
}

/**
 * Blok dianggap valid bila berupa objek dengan `type` yang dikenal. Bentuk
 * detail per tipe diverifikasi validator server (`MateriSchema`); renderer
 * hanya perlu tahu cara merangkainya.
 */
export function isMaterialBlock(value: unknown): value is MaterialBlock {
    return (
        typeof value === 'object' &&
        value !== null &&
        isMaterialBlockType((value as { type?: unknown }).type)
    );
}

/**
 * Bentuk blok lama: `{ type, value }` berisi pasangan petunjuk/jawaban yang
 * dulu hanya ditampilkan sebagai daftar. Masih dipakai materi PAUD/TK, jadi
 * harus tetap tampil sama (backward compatible).
 */
export interface LegacyValueBlock {
    type: string;
    value: string;
}

/**
 * Menyaring nilai `blocks` dari server agar renderer hanya menerima blok yang
 * dikenal. Blok asing dibuang tanpa melempar galat — materi lama tidak boleh
 * rusak karena satu blok salah tulis.
 */
export function normalizeBlocks(value: unknown): MaterialBlock[] {
    if (!Array.isArray(value)) {
        return [];
    }

    return value.filter(isMaterialBlock);
}

/**
 * Blok gaya lama (`{ type, value }`) yang bukan bagian dari skema baru.
 * Ditampilkan ulang sebagai daftar sederhana seperti sebelumnya.
 */
export function legacyValueBlocks(value: unknown): LegacyValueBlock[] {
    if (!Array.isArray(value)) {
        return [];
    }

    return value.filter((item): item is LegacyValueBlock => {
        if (typeof item !== 'object' || item === null) {
            return false;
        }

        const block = item as { type?: unknown; value?: unknown };

        return (
            typeof block.value === 'string' && !isMaterialBlockType(block.type)
        );
    });
}

/**
 * Kunci React: `id` blok bila ada, jika tidak indeks urutan.
 */
export function materialBlockKey(block: MaterialBlock, index: number): string {
    return block.id ? `${block.id}#${index}` : `block-${index}`;
}

/**
 * Materi dianggap punya blok render-able hanya bila hasil normalisasi tidak
 * kosong. Dipakai `MaterialViewer` untuk memilih jalur render.
 */
export function hasRenderableBlocks(value: unknown): boolean {
    return normalizeBlocks(value).length > 0;
}
