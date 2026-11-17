/**
 * Penyimpanan jawaban blok materi di perangkat (plan-materi-interaktif §2.4).
 *
 * Fungsi:
 * - memberi umpan balik instan tanpa menunggu jaringan;
 * - menjaga jawaban tetap ada saat offline maupun saat pengguna belum masuk;
 * - menjadi sumber nilai kumulatif (`attempts`, skor terbaik) yang dikirim ke
 *   server lewat antrean sync, sehingga kiriman ulang bersifat idempoten.
 */

const STORAGE_PREFIX = 'gamecenter.blocks.';

export interface StoredBlockResult {
    /** 0..100 untuk blok ini. */
    score: number;
    maxScore: number;
    /** Jumlah total percobaan siswa pada blok ini. */
    attempts: number;
    completed: boolean;
    /** Jawaban terakhir per butir (dipakai pembahasan guru). */
    details?: unknown;
    updatedAt: string;
}

/** Bentuk payload yang dikirim ke `POST /api/sync` (kind `material_block`). */
export interface MaterialBlockPayload {
    material_id: number;
    block_id: string;
    block_type: string;
    score: number;
    max_score: number;
    attempts: number;
    is_completed: boolean;
    details?: unknown;
    last_answered_at: string;
}

type StoredBlocks = Record<string, StoredBlockResult>;

function storageKey(materialId: number): string {
    return `${STORAGE_PREFIX}${materialId}`;
}

function isStoredResult(value: unknown): value is StoredBlockResult {
    return (
        typeof value === 'object' &&
        value !== null &&
        typeof (value as StoredBlockResult).score === 'number' &&
        typeof (value as StoredBlockResult).attempts === 'number'
    );
}

function loadAll(materialId: number): StoredBlocks {
    if (typeof window === 'undefined') {
        return {};
    }

    try {
        const raw = window.localStorage.getItem(storageKey(materialId));

        if (!raw) {
            return {};
        }

        const parsed = JSON.parse(raw) as unknown;

        if (typeof parsed !== 'object' || parsed === null) {
            return {};
        }

        return Object.fromEntries(
            Object.entries(parsed as StoredBlocks).filter(([, value]) =>
                isStoredResult(value),
            ),
        );
    } catch {
        // Penyimpanan bisa diblokir (mode privat); progres tetap di memori.
        return {};
    }
}

function saveAll(materialId: number, all: StoredBlocks): void {
    try {
        window.localStorage.setItem(storageKey(materialId), JSON.stringify(all));
    } catch {
        // Diabaikan: nilai terbaru tetap dipakai di memori komponen.
    }
}

export function getBlockResult(
    materialId: number,
    blockId: string,
): StoredBlockResult | null {
    return loadAll(materialId)[blockId] ?? null;
}

export function loadBlockResults(materialId: number): StoredBlocks {
    return loadAll(materialId);
}

export interface RecordBlockInput {
    materialId: number;
    blockId: string;
    score: number;
    maxScore?: number;
    completed?: boolean;
    details?: unknown;
}

/**
 * Menyimpan satu percobaan baru: skor **terbaik** dipertahankan, `attempts`
 * bertambah, dan jawaban terakhir disimpan untuk pembahasan.
 */
export function recordBlockResult(input: RecordBlockInput): StoredBlockResult {
    const all = loadAll(input.materialId);
    const previous = all[input.blockId];
    const maxScore = Math.max(1, input.maxScore ?? 100);
    const score = Math.max(0, Math.min(maxScore, Math.round(input.score)));

    const next: StoredBlockResult = {
        score: Math.max(previous?.score ?? 0, score),
        maxScore: Math.max(previous?.maxScore ?? 0, maxScore),
        attempts: (previous?.attempts ?? 0) + 1,
        completed: (previous?.completed ?? false) || (input.completed ?? true),
        details: input.details ?? previous?.details,
        updatedAt: new Date().toISOString(),
    };

    all[input.blockId] = next;
    saveAll(input.materialId, all);

    return next;
}

export function toBlockPayload(
    materialId: number,
    blockId: string,
    blockType: string,
    result: StoredBlockResult,
): MaterialBlockPayload {
    return {
        material_id: materialId,
        block_id: blockId,
        block_type: blockType,
        score: result.score,
        max_score: result.maxScore,
        attempts: result.attempts,
        is_completed: result.completed,
        details: result.details,
        last_answered_at: result.updatedAt,
    };
}
