{{--
    Kartu pengguna di footer sidebar panel admin.

    Berisi avatar, nama, badge peran, dan tombol keluar.
    Tombol keluar memakai form POST (bukan tautan GET) supaya logout
    tidak bisa terpicu oleh prefetch atau tautan berbagi, dan meminta
    konfirmasi lebih dulu.
--}}
@php
    $user = filament()->auth()->user();
    $role = $user?->role;
    $roleLabel = $role?->label() ?? 'Pengguna';
    $name = $user?->name ?? 'Pengguna';
    $initial = mb_strtoupper(mb_substr(trim($name), 0, 1));
    $logoutUrl = filament()->getLogoutUrl();
@endphp

@if ($user)
    <div class="gc-user-card">
        <div class="gc-user-card-top">
            <span class="gc-user-card-avatar" aria-hidden="true">
                {{ $initial }}
            </span>

            <span class="gc-user-card-copy">
                <span class="gc-user-card-name" title="{{ $name }}">
                    {{ $name }}
                </span>
                <span class="gc-user-card-role">{{ $roleLabel }}</span>
            </span>
        </div>

        {{--
            Konfirmasi dua langkah.

            Tombol "Keluar" hanya membuka dialog; tombol "Ya, keluar"
            yang benar-benar mengirim form. Pengiriman programatik
            (form.submit()) dipakai supaya tidak bergantung pada
            `SubmitEvent.submitter` yang bisa bernilai null dan pada
            value atribut data-* yang kosong.
        --}}
        <form
            method="POST"
            action="{{ $logoutUrl }}"
            class="gc-user-card-form"
            x-data="{
                asking: false,
                open() { this.asking = true; },
                close() { this.asking = false; },
                confirm() { this.asking = false; this.$root.submit(); },
            }"
            x-on:submit.prevent
        >
            @csrf

            <button
                type="button"
                class="gc-user-card-logout"
                x-on:click="open()"
                :aria-expanded="asking.toString()"
            >
                <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.9"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    aria-hidden="true"
                >
                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                    <path d="m16 17 5-5-5-5" />
                    <path d="M21 12H9" />
                </svg>
                Keluar
            </button>

            {{-- Konfirmasi: "Ya, keluar" lalu langsung keluar dan kembali ke beranda. --}}
            <div
                x-cloak
                x-show="asking"
                x-on:keydown.escape.window="close()"
                class="gc-user-card-confirm"
                role="dialog"
                aria-modal="true"
                aria-labelledby="gc-user-card-confirm-title"
            >
                <p id="gc-user-card-confirm-title" class="gc-user-card-confirm-title">
                    Keluar dari panel?
                </p>
                <p class="gc-user-card-confirm-body">
                    Kamu akan kembali ke halaman Game Center.
                </p>

                <div class="gc-user-card-confirm-actions">
                    <button
                        type="button"
                        class="gc-user-card-cancel"
                        x-on:click="close()"
                    >
                        Batal
                    </button>
                    <button
                        type="button"
                        class="gc-user-card-confirm-yes"
                        x-on:click="confirm()"
                    >
                        Ya, keluar
                    </button>
                </div>
            </div>
        </form>
    </div>
@endif
