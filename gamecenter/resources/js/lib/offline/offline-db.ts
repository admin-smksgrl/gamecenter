import {
    CachedCatalog,
    OFFLINE_DB_NAME,
    OFFLINE_DB_VERSION,
    OFFLINE_STORES,
    OfflineStoreName,
    SettingsRecord,
    SyncItemStatus,
    SyncItemType,
    SyncQueueRecord,
} from './db-schema';

export function createSyncUuid(): string {
    if (typeof crypto !== 'undefined' && 'randomUUID' in crypto) {
        return crypto.randomUUID();
    }

    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (char) => {
        const random = (Math.random() * 16) | 0;
        const value = char === 'x' ? random : (random & 0x3) | 0x8;

        return value.toString(16);
    });
}

function createStores(db: IDBDatabase): void {
    if (!db.objectStoreNames.contains(OFFLINE_STORES.catalog)) {
        db.createObjectStore(OFFLINE_STORES.catalog, { keyPath: 'id' });
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.materials)) {
        const store = db.createObjectStore(OFFLINE_STORES.materials, {
            keyPath: 'id',
        });

        store.createIndex('chapter_id', 'chapter_id');
        store.createIndex('type', 'type');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.questions)) {
        const store = db.createObjectStore(OFFLINE_STORES.questions, {
            keyPath: 'id',
        });

        store.createIndex('assessment_id', 'assessment_id');
        store.createIndex('type', 'type');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.assessments)) {
        const store = db.createObjectStore(OFFLINE_STORES.assessments, {
            keyPath: 'id',
        });

        store.createIndex('chapter_id', 'chapter_id');
        store.createIndex('difficulty', 'difficulty');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.progress)) {
        const store = db.createObjectStore(OFFLINE_STORES.progress, {
            keyPath: 'id',
        });

        store.createIndex('userId', 'userId');
        store.createIndex('chapterId', 'chapterId');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.sessions)) {
        const store = db.createObjectStore(OFFLINE_STORES.sessions, {
            keyPath: 'uuid',
        });

        store.createIndex('userId', 'userId');
        store.createIndex('status', 'status');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.syncQueue)) {
        const store = db.createObjectStore(OFFLINE_STORES.syncQueue, {
            keyPath: 'uuid',
        });

        store.createIndex('status', 'status');
        store.createIndex('createdAt', 'createdAt');
    }

    if (!db.objectStoreNames.contains(OFFLINE_STORES.settings)) {
        db.createObjectStore(OFFLINE_STORES.settings, { keyPath: 'key' });
    }
}

function transactionDone(transaction: IDBTransaction): Promise<void> {
    return new Promise((resolve, reject) => {
        transaction.oncomplete = () => resolve();
        transaction.onerror = () =>
            reject(transaction.error ?? new Error('Transaksi IndexedDB gagal.'));
        transaction.onabort = () =>
            reject(transaction.error ?? new Error('Transaksi IndexedDB dibatalkan.'));
    });
}

class OfflineDB {
    private dbPromise: Promise<IDBDatabase> | null = null;

    isSupported(): boolean {
        return (
            typeof window !== 'undefined' &&
            typeof window.indexedDB !== 'undefined'
        );
    }

    private openDatabase(): Promise<IDBDatabase> {
        if (!this.isSupported()) {
            return Promise.reject(new Error('IndexedDB tidak tersedia.'));
        }

        if (this.dbPromise) {
            return this.dbPromise;
        }

        this.dbPromise = new Promise<IDBDatabase>((resolve, reject) => {
            const request = window.indexedDB.open(
                OFFLINE_DB_NAME,
                OFFLINE_DB_VERSION,
            );

            request.onupgradeneeded = () => createStores(request.result);

            request.onsuccess = () => {
                const db = request.result;

                db.onversionchange = () => db.close();

                resolve(db);
            };

            request.onerror = () =>
                reject(request.error ?? new Error('Gagal membuka IndexedDB.'));
        });

        this.dbPromise.catch(() => {
            this.dbPromise = null;
        });

        return this.dbPromise;
    }

    async get<T>(store: OfflineStoreName, key: IDBValidKey): Promise<T | undefined> {
        const db = await this.openDatabase();

        return new Promise<T | undefined>((resolve, reject) => {
            const request = db
                .transaction(store, 'readonly')
                .objectStore(store)
                .get(key);

            request.onsuccess = () => resolve(request.result as T | undefined);
            request.onerror = () => reject(request.error);
        });
    }

    async getAll<T>(store: OfflineStoreName): Promise<T[]> {
        const db = await this.openDatabase();

        return new Promise<T[]>((resolve, reject) => {
            const request = db
                .transaction(store, 'readonly')
                .objectStore(store)
                .getAll();

            request.onsuccess = () => resolve(request.result as T[]);
            request.onerror = () => reject(request.error);
        });
    }

    async count(store: OfflineStoreName): Promise<number> {
        const db = await this.openDatabase();

        return new Promise<number>((resolve, reject) => {
            const request = db
                .transaction(store, 'readonly')
                .objectStore(store)
                .count();

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async put<T>(store: OfflineStoreName, value: T): Promise<void> {
        const db = await this.openDatabase();
        const transaction = db.transaction(store, 'readwrite');

        transaction.objectStore(store).put(value);

        return transactionDone(transaction);
    }

    async delete(store: OfflineStoreName, key: IDBValidKey): Promise<void> {
        const db = await this.openDatabase();
        const transaction = db.transaction(store, 'readwrite');

        transaction.objectStore(store).delete(key);

        return transactionDone(transaction);
    }

    async deleteMany(
        store: OfflineStoreName,
        keys: IDBValidKey[],
    ): Promise<void> {
        if (keys.length === 0) {
            return;
        }

        const db = await this.openDatabase();
        const transaction = db.transaction(store, 'readwrite');
        const objectStore = transaction.objectStore(store);

        keys.forEach((key) => objectStore.delete(key));

        return transactionDone(transaction);
    }

    async clear(store: OfflineStoreName): Promise<void> {
        const db = await this.openDatabase();
        const transaction = db.transaction(store, 'readwrite');

        transaction.objectStore(store).clear();

        return transactionDone(transaction);
    }

    async saveCatalog<TStats>(catalog: {
        levels: unknown[];
        stats: TStats;
        version: string;
    }): Promise<void> {
        const record: CachedCatalog<TStats> = {
            id: 'catalog',
            levels: catalog.levels,
            stats: catalog.stats,
            version: catalog.version,
            cachedAt: new Date().toISOString(),
        };

        await this.put(OFFLINE_STORES.catalog, record);
    }

    async loadCatalog<TStats>(): Promise<CachedCatalog<TStats> | undefined> {
        return this.get<CachedCatalog<TStats>>(OFFLINE_STORES.catalog, 'catalog');
    }

    async setSetting<T>(key: string, value: T): Promise<void> {
        const record: SettingsRecord<T> = {
            key,
            value,
            updatedAt: new Date().toISOString(),
        };

        await this.put(OFFLINE_STORES.settings, record);
    }

    async getSetting<T>(key: string): Promise<T | undefined> {
        const record = await this.get<SettingsRecord<T>>(
            OFFLINE_STORES.settings,
            key,
        );

        return record?.value;
    }

    async queueSync(input: {
        type: SyncItemType;
        payload: Record<string, unknown>;
    }): Promise<SyncQueueRecord> {
        const now = new Date().toISOString();
        const record: SyncQueueRecord = {
            uuid: createSyncUuid(),
            type: input.type,
            payload: input.payload,
            status: 'pending',
            attempts: 0,
            createdAt: now,
            updatedAt: now,
            lastError: null,
        };

        await this.put(OFFLINE_STORES.syncQueue, record);

        return record;
    }

    async listSyncQueue(): Promise<SyncQueueRecord[]> {
        const records = await this.getAll<SyncQueueRecord>(
            OFFLINE_STORES.syncQueue,
        );

        return records.sort((left, right) =>
            left.createdAt.localeCompare(right.createdAt),
        );
    }

    async pendingSync(
        limit: number,
        includeExhausted = false,
        maxAttempts = 5,
    ): Promise<SyncQueueRecord[]> {
        const records = await this.listSyncQueue();

        return records
            .filter(
                (record) =>
                    record.status !== 'sending' &&
                    (includeExhausted || record.attempts < maxAttempts),
            )
            .slice(0, limit);
    }

    async queueCount(): Promise<number> {
        return this.count(OFFLINE_STORES.syncQueue);
    }

    async markSynced(uuids: string[]): Promise<void> {
        await this.deleteMany(OFFLINE_STORES.syncQueue, uuids);
    }

    async markSyncFailed(uuid: string, message: string | null): Promise<void> {
        const record = await this.get<SyncQueueRecord>(
            OFFLINE_STORES.syncQueue,
            uuid,
        );

        if (!record) {
            return;
        }

        const status: SyncItemStatus = 'failed';

        await this.put<SyncQueueRecord>(OFFLINE_STORES.syncQueue, {
            ...record,
            status,
            attempts: record.attempts + 1,
            lastError: message,
            updatedAt: new Date().toISOString(),
        });
    }

    /**
     * Hapus data milik pengguna saat keluar. Katalog publik tetap
     * tersimpan agar halaman jelajah masih bisa dibuka offline.
     */
    async clearUserData(): Promise<void> {
        await Promise.all([
            this.clear(OFFLINE_STORES.progress),
            this.clear(OFFLINE_STORES.sessions),
            this.clear(OFFLINE_STORES.syncQueue),
            this.clear(OFFLINE_STORES.settings),
        ]);
    }
}

export const offlineDb = new OfflineDB();
