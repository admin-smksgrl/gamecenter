import { toast } from '@/lib/toast';

/**
 * Cek ulang koneksi ke server setelah Inertia gagal mengambil halaman.
 *
 * Toast "Tidak tersambung ke server" memberi tombol **Coba lagi**; tombol itu
 * memanggil fungsi ini. Kita sengaja mengecek `/up` lebih dulu supaya tidak
 * memuat ulang halaman saat server masih mati — reload dalam keadaan itu hanya
 * memunculkan halaman galat peramban yang membingungkan.
 */
export async function retryConnection(): Promise<void> {
    if (typeof navigator !== 'undefined' && navigator.onLine === false) {
        toast.error(
            'Masih offline',
            'Sambungkan internetmu dulu, lalu tekan Coba lagi.',
        );

        return;
    }

    try {
        const response = await fetch('/up', {
            method: 'GET',
            cache: 'no-store',
            headers: { Accept: 'application/json' },
        });

        if (response.ok) {
            window.location.reload();

            return;
        }

        toast.error(
            'Server belum siap',
            'Tunggu beberapa saat, lalu tekan Coba lagi.',
        );
    } catch {
        toast.error(
            'Masih tidak tersambung',
            'Periksa koneksi internetmu, lalu tekan Coba lagi.',
        );
    }
}
