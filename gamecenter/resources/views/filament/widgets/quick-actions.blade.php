<x-filament-widgets::widget class="gc-widget-stretch">
    <div class="gc-card">
        <div class="gc-quick-head">
            <p class="gc-eyebrow">Akses cepat</p>
            <h3 class="gc-quick-title">Langkah berikutnya</h3>
        </div>

        <div class="gc-quick-list">
            @foreach ($links as $link)
                <a
                    href="{{ $link['url'] }}"
                    class="gc-quick-link"
                    @if ($link['external']) target="_blank" rel="noreferrer" @endif
                >
                    <span class="gc-quick-icon" aria-hidden="true">
                        <x-filament::icon :icon="$link['icon']" />
                    </span>

                    <span class="gc-quick-copy">
                        <span class="gc-quick-label">{{ $link['label'] }}</span>
                        <span class="gc-quick-hint">{{ $link['hint'] }}</span>
                    </span>

                    <svg
                        class="gc-quick-arrow"
                        width="12"
                        height="12"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2.2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        aria-hidden="true"
                    >
                        @if ($link['external'])
                            <path d="M7 17 17 7" />
                            <path d="M7 7h10v10" />
                        @else
                            <path d="M5 12h14" />
                            <path d="m13 6 6 6-6 6" />
                        @endif
                    </svg>
                </a>
            @endforeach
        </div>

        <p class="gc-quick-note">
            @if ($isAdmin)
                Pengajuan yang disetujui langsung mengaktifkan paket anggota. Pastikan
                nominal dan siklus tagihan sudah sesuai sebelum menyetujui.
            @else
                Pantau grafik aktivitas untuk melihat ritme kelas, lalu tinjau
                pengajuan keanggotaan bersama admin bila diperlukan.
            @endif
        </p>
    </div>
</x-filament-widgets::widget>
