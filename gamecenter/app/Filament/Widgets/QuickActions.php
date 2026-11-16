<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\MembershipPlans\MembershipPlanResource;
use App\Filament\Resources\Memberships\MembershipResource;
use App\Models\Membership;
use Filament\Facades\Filament;
use Filament\Support\Icons\Heroicon;
use Filament\Widgets\Widget;

class QuickActions extends Widget
{
    protected string $view = 'filament.widgets.quick-actions';

    protected int | string | array $columnSpan = 1;

    protected static ?bool $isLazyLoaded = false;

    protected static ?int $sort = 0;

    protected function getViewData(): array
    {
        $isAdmin = Filament::auth()->user()?->isAdmin() ?? false;

        $links = [];

        if ($isAdmin) {
            $pending = Membership::query()->pending()->count();

            $links[] = [
                'label' => 'Tinjau pengajuan',
                'hint' => $pending > 0
                    ? $pending.' pengajuan menunggu verifikasi'
                    : 'Tidak ada pengajuan baru',
                'url' => MembershipResource::getUrl('index'),
                'icon' => Heroicon::OutlinedInbox,
                'external' => false,
            ];

            $links[] = [
                'label' => 'Kelola paket',
                'hint' => 'Atur harga dan fitur keanggotaan',
                'url' => MembershipPlanResource::getUrl('index'),
                'icon' => Heroicon::OutlinedCreditCard,
                'external' => false,
            ];
        }

        if (! $isAdmin) {
            $links[] = [
                'label' => 'Panduan materi',
                'hint' => 'Alur belajar dan materi siswa',
                'url' => url('/panduan/menjelajah-materi'),
                'icon' => Heroicon::OutlinedAcademicCap,
                'external' => true,
            ];

            $links[] = [
                'label' => 'Keanggotaan siswa',
                'hint' => 'Paket yang dilihat siswa',
                'url' => url('/keanggotaan'),
                'icon' => Heroicon::OutlinedCreditCard,
                'external' => true,
            ];
        }

        $links[] = [
            'label' => 'Panduan aplikasi',
            'hint' => 'Alur belajar dan operasional',
            'url' => url('/panduan'),
            'icon' => Heroicon::OutlinedBookOpen,
            'external' => true,
        ];

        $links[] = [
            'label' => 'Situs belajar',
            'hint' => 'Lihat tampilan yang dipakai siswa',
            'url' => url('/'),
            'icon' => Heroicon::OutlinedGlobeAlt,
            'external' => true,
        ];

        return [
            'isAdmin' => $isAdmin,
            'links' => $links,
        ];
    }
}
