import { useCallback, useState } from 'react';

import type { MaterialBlockPayload, StoredBlockResult } from './store';
import { getBlockResult, recordBlockResult, toBlockPayload } from './store';

interface UseBlockAnswerOptions {
    materialId: number;
    blockId: string;
    blockType: string;
    /** Dipanggil setiap selesai memeriksa agar induk bisa mengantrekan sync. */
    onRecord?: (payload: MaterialBlockPayload) => void;
}

interface UseBlockAnswerResult {
    result: StoredBlockResult | null;
    record: (score: number, details?: unknown, completed?: boolean) => void;
}

/**
 * Menyatukan penyimpanan lokal dan pelaporan ke induk untuk satu blok.
 *
 * Blok aktivitas wajib memakai hook ini supaya skor selalu tersimpan walau
 * siswa belum masuk atau sedang offline.
 */
export function useBlockAnswer({
    materialId,
    blockId,
    blockType,
    onRecord,
}: UseBlockAnswerOptions): UseBlockAnswerResult {
    const [result, setResult] = useState<StoredBlockResult | null>(() =>
        getBlockResult(materialId, blockId),
    );

    const record = useCallback(
        (score: number, details?: unknown, completed = true) => {
            const next = recordBlockResult({
                materialId,
                blockId,
                score,
                details,
                completed,
            });

            setResult(next);
            onRecord?.(toBlockPayload(materialId, blockId, blockType, next));
        },
        [materialId, blockId, blockType, onRecord],
    );

    return { result, record };
}
