import { useEffect, useSyncExternalStore } from 'react';

import { syncService } from '@/lib/offline/sync-service';

export function useOfflineSync(enabled: boolean) {
    const state = useSyncExternalStore(
        syncService.subscribe,
        syncService.snapshot,
        syncService.snapshot,
    );

    useEffect(() => {
        syncService.start();
    }, []);

    useEffect(() => {
        syncService.setEnabled(enabled);
    }, [enabled]);

    return {
        ...state,
        syncNow: () => syncService.flush('manual'),
    };
}
