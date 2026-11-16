import { SyncItemType, SyncQueueRecord } from './db-schema';
import { offlineDb } from './offline-db';

export interface SyncSnapshot {
    online: boolean;
    syncing: boolean;
    pending: number;
    lastSyncedAt: string | null;
    lastError: string | null;
}

type SyncReason =
    | 'auto'
    | 'enabled'
    | 'enqueue'
    | 'online'
    | 'manual'
    | 'background';

interface SyncResult {
    uuid: string;
    status: 'completed' | 'failed';
    message?: string | null;
}

interface SyncResponse {
    results?: SyncResult[];
}

const SYNC_TAG = 'gamecenter-sync';
const BATCH_SIZE = 25;
const MAX_BATCHES = 4;
const MAX_AUTO_ATTEMPTS = 5;

type Listener = () => void;

class SyncService {
    private listeners = new Set<Listener>();

    private state: SyncSnapshot = {
        online: typeof navigator === 'undefined' ? true : navigator.onLine,
        syncing: false,
        pending: 0,
        lastSyncedAt: null,
        lastError: null,
    };

    private enabled = false;

    private started = false;

    private inFlight: Promise<void> | null = null;

    subscribe = (listener: Listener): (() => void) => {
        this.listeners.add(listener);

        return () => {
            this.listeners.delete(listener);
        };
    };

    snapshot = (): SyncSnapshot => this.state;

    start(): void {
        if (this.started || typeof window === 'undefined') {
            return;
        }

        this.started = true;

        window.addEventListener('online', this.handleOnline);
        window.addEventListener('offline', this.handleOffline);
        document.addEventListener('visibilitychange', this.handleVisibility);

        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.addEventListener(
                'message',
                this.handleServiceWorkerMessage,
            );
        }

        void this.refreshPending();
    }

    setEnabled(enabled: boolean): void {
        if (this.enabled === enabled) {
            if (enabled) {
                void this.refreshPending();
            }

            return;
        }

        this.enabled = enabled;

        if (enabled) {
            void this.refreshPending();
            void this.flush('enabled');
        }
    }

    async enqueue(
        type: SyncItemType,
        payload: Record<string, unknown>,
    ): Promise<SyncQueueRecord | null> {
        try {
            const record = await offlineDb.queueSync({ type, payload });

            this.setState({ pending: this.state.pending + 1 });
            void this.registerBackgroundSync();

            if (this.enabled && this.state.online) {
                void this.flush('enqueue');
            }

            return record;
        } catch {
            this.setState({
                lastError:
                    'Penyimpanan di perangkat tidak bisa dipakai. Progres mungkin tidak tersimpan saat offline.',
            });

            return null;
        }
    }

    flush(reason: SyncReason = 'auto'): Promise<void> {
        if (this.inFlight) {
            return this.inFlight;
        }

        if (!this.enabled || !this.state.online) {
            return Promise.resolve();
        }

        this.inFlight = this.runFlush(reason === 'manual').finally(() => {
            this.inFlight = null;
        });

        return this.inFlight;
    }

    async refreshPending(): Promise<void> {
        try {
            const pending = await offlineDb.queueCount();

            if (pending !== this.state.pending) {
                this.setState({ pending });
            }
        } catch {
            // IndexedDB bisa diblokir (mode privat); antrean dianggap kosong.
        }
    }

    private async runFlush(includeExhausted: boolean): Promise<void> {
        let syncedAny = false;

        try {
            for (let batch = 0; batch < MAX_BATCHES; batch += 1) {
                const items = await offlineDb
                    .pendingSync(
                        BATCH_SIZE,
                        includeExhausted,
                        MAX_AUTO_ATTEMPTS,
                    )
                    .catch(() => [] as SyncQueueRecord[]);

                if (items.length === 0) {
                    break;
                }

                this.setState({ syncing: true, lastError: null });

                const response = await this.post(items);

                if (response === null) {
                    break;
                }

                const completed: string[] = [];

                for (const result of response.results ?? []) {
                    if (result.status === 'completed') {
                        completed.push(result.uuid);
                    } else {
                        await offlineDb
                            .markSyncFailed(result.uuid, result.message ?? null)
                            .catch(() => undefined);
                    }
                }

                await offlineDb.markSynced(completed).catch(() => undefined);

                if (completed.length === 0) {
                    break;
                }

                syncedAny = true;

                if (items.length < BATCH_SIZE) {
                    break;
                }
            }
        } finally {
            await this.refreshPending();

            this.setState({
                syncing: false,
                lastSyncedAt: syncedAny
                    ? new Date().toISOString()
                    : this.state.lastSyncedAt,
            });
        }
    }

    private async post(items: SyncQueueRecord[]): Promise<SyncResponse | null> {
        try {
            const token = this.csrfToken();
            const response = await fetch('/api/sync', {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    ...(token ? { 'X-XSRF-TOKEN': token } : {}),
                },
                body: JSON.stringify({
                    items: items.map((item) => ({
                        uuid: item.uuid,
                        type: item.type,
                        recorded_at: item.createdAt,
                        payload: item.payload,
                    })),
                }),
            });

            if (response.status === 401 || response.status === 419) {
                this.setState({
                    lastError:
                        'Masuk dulu supaya progres tersimpan di akunmu.',
                });

                return null;
            }

            if (!response.ok) {
                this.setState({
                    lastError:
                        'Server belum menerima data tersimpan. Kami akan mencoba lagi nanti.',
                });

                return null;
            }

            return (await response.json()) as SyncResponse;
        } catch {
            this.setState({
                lastError:
                    'Belum tersambung ke server. Data tetap aman di perangkat ini.',
            });

            return null;
        }
    }

    private csrfToken(): string | null {
        if (typeof document === 'undefined') {
            return null;
        }

        const cookie = document.cookie
            .split('; ')
            .find((entry) => entry.startsWith('XSRF-TOKEN='));

        return cookie
            ? decodeURIComponent(cookie.slice('XSRF-TOKEN='.length))
            : null;
    }

    private registerBackgroundSync(): void {
        if (!('serviceWorker' in navigator)) {
            return;
        }

        navigator.serviceWorker.ready
            .then((registration) => {
                const sync = (
                    registration as ServiceWorkerRegistration & {
                        sync?: { register: (tag: string) => Promise<void> };
                    }
                ).sync;

                return sync?.register(SYNC_TAG);
            })
            .catch(() => undefined);
    }

    private handleOnline = (): void => {
        this.setState({ online: true, lastError: null });

        if (this.enabled) {
            void this.flush('online');
        }
    };

    private handleOffline = (): void => {
        this.setState({ online: false });
    };

    private handleVisibility = (): void => {
        if (document.visibilityState !== 'visible') {
            return;
        }

        void this.refreshPending();

        if (this.enabled) {
            void this.flush('auto');
        }
    };

    private handleServiceWorkerMessage = (event: MessageEvent): void => {
        if ((event.data as { type?: string } | null)?.type === 'gamecenter:sync') {
            void this.flush('background');
        }
    };

    private setState(patch: Partial<SyncSnapshot>): void {
        this.state = { ...this.state, ...patch };
        this.listeners.forEach((listener) => listener());
    }
}

export const syncService = new SyncService();
