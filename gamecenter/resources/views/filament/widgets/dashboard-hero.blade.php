@php
    use App\Filament\Resources\MembershipPlans\MembershipPlanResource;
    use App\Filament\Resources\Memberships\MembershipResource;
@endphp

<x-filament-widgets::widget>
    <div class="gc-hero">
        <div class="gc-hero-dots" aria-hidden="true"></div>

        <div class="gc-hero-inner">
            <div class="gc-hero-copy">
                <span class="gc-hero-date">
                    <span class="gc-hero-date-dot" aria-hidden="true"></span>
                    {{ $dateLabel }}
                </span>

                <h2 class="gc-display gc-hero-title">
                    {{ $greeting }}, <em>{{ $displayName }}</em>.
                </h2>

                <p class="gc-hero-text">
                    @if ($isAdmin)
                        Pantau aktivitas belajar, tinjau pengajuan keanggotaan, dan
                        jaga ritme kelas dari satu tempat.
                    @else
                        Pantau aktivitas belajar siswa dan kelola materi agar kelas
                        tetap berjalan sesuai ritme.
                    @endif
                </p>

                <div class="gc-hero-actions">
                    @if ($isAdmin)
                        <a
                            href="{{ MembershipResource::getUrl('index') }}"
                            class="gc-hero-btn gc-hero-btn-solid"
                        >
                            Tinjau pengajuan
                            @if ($pendingRequests > 0)
                                <span class="gc-hero-count">{{ $pendingRequests }}</span>
                            @endif
                        </a>

                        <a
                            href="{{ MembershipPlanResource::getUrl('index') }}"
                            class="gc-hero-btn gc-hero-btn-ghost"
                        >
                            Kelola paket
                        </a>
                    @endif

                    <a
                        href="{{ url('/') }}"
                        target="_blank"
                        rel="noreferrer"
                        class="gc-hero-btn gc-hero-btn-ghost"
                    >
                        Buka situs
                        <svg
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
                            <path d="M7 17 17 7" />
                            <path d="M7 7h10v10" />
                        </svg>
                    </a>
                </div>
            </div>

            <dl class="gc-hero-side">
                <div class="gc-hero-stat">
                    <dt>Sesi hari ini</dt>
                    <dd>{{ number_format($sessionsToday, 0, ',', '.') }}</dd>
                </div>

                <div class="gc-hero-stat">
                    <dt>Siswa aktif</dt>
                    <dd>{{ number_format($activeStudents, 0, ',', '.') }}</dd>
                </div>

                <div class="gc-hero-stat">
                    <dt>{{ $isAdmin ? 'Menunggu' : 'Materi aktif' }}</dt>
                    <dd>
                        {{ number_format($isAdmin ? $pendingRequests : $activeMaterials, 0, ',', '.') }}
                    </dd>
                </div>
            </dl>
        </div>
    </div>
</x-filament-widgets::widget>
