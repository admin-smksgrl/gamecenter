export interface FriendlyError {
    title: string;
    description: string;
}

const GENERIC: FriendlyError = {
    title: 'Ada yang belum berjalan',
    description:
        'Coba lagi sebentar lagi. Kalau masih gagal, muat ulang halaman ini.',
};

/**
 * Ubah kode status HTTP menjadi penjelasan yang bisa dimengerti pengguna awam.
 * Hindari istilah teknis seperti "CSRF", "exception", atau "server error".
 */
export function friendlyHttpError(status: number): FriendlyError {
    switch (status) {
        case 401:
            return {
                title: 'Sesi kamu sudah berakhir',
                description:
                    'Silakan masuk lagi supaya bisa melanjutkan belajar.',
            };
        case 403:
            return {
                title: 'Kamu belum punya akses',
                description:
                    'Halaman ini khusus untuk akun tertentu. Coba masuk dengan akun yang sesuai.',
            };
        case 404:
            return {
                title: 'Halaman tidak ditemukan',
                description:
                    'Tautan yang kamu buka mungkin sudah berubah atau dihapus. Kembali ke beranda untuk melanjutkan.',
            };
        case 419:
            return {
                title: 'Sesi kamu sudah berakhir',
                description:
                    'Demi keamanan, halaman akan dimuat ulang otomatis. Setelah itu silakan coba lagi.',
            };
        case 429:
            return {
                title: 'Terlalu banyak percobaan',
                description:
                    'Tunggu sebentar, lalu coba lagi. Ini dilakukan supaya akunmu tetap aman.',
            };
        case 500:
            return {
                title: 'Ada gangguan di server',
                description:
                    'Data yang sudah tersimpan tetap aman. Coba lagi beberapa saat lagi.',
            };
        case 502:
        case 503:
        case 504:
            return {
                title: 'Layanan sedang sibuk',
                description:
                    'Coba lagi dalam beberapa saat. Kami sedang menyiapkan layanan kembali.',
            };
        default:
            return GENERIC;
    }
}

export function friendlyNetworkError(): FriendlyError {
    return {
        title: 'Tidak tersambung ke server',
        description:
            'Periksa koneksi internetmu, lalu coba lagi. Permainan yang tersimpan di perangkat tetap aman.',
    };
}

export function friendlyError(error: unknown): FriendlyError {
    if (error instanceof Error) {
        const message = error.message.toLowerCase();

        if (
            message.includes('network') ||
            message.includes('fetch') ||
            message.includes('load failed') ||
            message.includes('failed to fetch')
        ) {
            return friendlyNetworkError();
        }
    }

    return GENERIC;
}

/** Ambil pesan validasi pertama yang tidak kosong. */
export function firstValidationMessage(
    errors: Record<string, string> | null | undefined,
): string | null {
    if (!errors) {
        return null;
    }

    for (const value of Object.values(errors)) {
        if (typeof value === 'string' && value.trim() !== '') {
            return value;
        }
    }

    return null;
}

export function friendlySyncError(message: string | null): FriendlyError {
    if (!message) {
        return {
            title: 'Data belum terkirim',
            description:
                'Permainanmu tetap tersimpan di perangkat ini. Kami akan mencoba mengirimnya lagi.',
        };
    }

    if (message.toLowerCase().includes('masuk')) {
        return {
            title: 'Masuk untuk menyimpan progres',
            description:
                'Progresmu sudah tersimpan di perangkat ini. Masuk ke akun supaya bisa disimpan permanen.',
        };
    }

    return {
        title: 'Data belum terkirim',
        description:
            'Permainanmu tetap tersimpan di perangkat ini. Kami akan mencoba mengirimnya lagi saat koneksi stabil.',
    };
}
