/**
 * Skema IndexedDB sisi client (offline-first).
 *
 * Nama store dan versi harus disinkronkan dengan `public/sw.js`
 * (cache app shell) dan `offline-db.ts` (pembuatan object store).
 */

export const OFFLINE_DB_NAME = 'gamecenter-offline';
export const OFFLINE_DB_VERSION = 1;

export const OFFLINE_STORES = {
    catalog: 'catalog',
    materials: 'materials',
    questions: 'questions',
    assessments: 'assessments',
    progress: 'progress',
    sessions: 'sessions',
    syncQueue: 'syncQueue',
    settings: 'userSettings',
} as const;

export type OfflineStoreName =
    (typeof OFFLINE_STORES)[keyof typeof OFFLINE_STORES];

export type SyncItemType = 'session' | 'progress' | 'answer';

export type SyncItemStatus = 'pending' | 'sending' | 'failed';

export interface SyncQueueRecord {
    uuid: string;
    type: SyncItemType;
    payload: Record<string, unknown>;
    status: SyncItemStatus;
    attempts: number;
    createdAt: string;
    updatedAt: string;
    lastError: string | null;
}

export interface CachedCatalog<TStats = Record<string, number>> {
    id: 'catalog';
    levels: unknown[];
    stats: TStats;
    version: string;
    cachedAt: string;
}

export interface CachedMaterial {
    id: number;
    chapter_id: number;
    type: string;
    title: string;
    content: string | null;
    blocks: unknown[] | null;
    duration: number | null;
    order: number | null;
    cachedAt: string;
}

export interface CachedAssessment {
    id: number;
    chapter_id: number;
    difficulty: string;
    duration: number;
    passing_score: number;
    cachedAt: string;
}

export interface CachedQuestion {
    id: number;
    assessment_id: number;
    type: string;
    question: string;
    options: unknown[] | null;
    points: number;
    time_limit: number | null;
    order: number | null;
    cachedAt: string;
}

export interface CachedProgress {
    id: string;
    userId: number;
    chapterId: number;
    status: string;
    progressPercentage: number;
    totalTimeSpent: number;
    bestScore: number;
    lastAccessedAt: string | null;
}

export interface CachedSession {
    uuid: string;
    userId: number;
    assessmentId: number;
    mode: string;
    score: number;
    correctAnswers: number;
    totalQuestions: number;
    durationSeconds: number;
    startedAt: string | null;
    completedAt: string | null;
    synced: boolean;
}

export interface SettingsRecord<T = unknown> {
    key: string;
    value: T;
    updatedAt: string;
}
