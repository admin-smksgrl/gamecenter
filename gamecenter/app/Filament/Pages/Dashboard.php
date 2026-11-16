<?php

namespace App\Filament\Pages;

use App\Filament\Widgets\DashboardHero;
use App\Filament\Widgets\DashboardStats;
use App\Filament\Widgets\LatestMembershipRequests;
use App\Filament\Widgets\QuickActions;
use App\Filament\Widgets\SessionActivityChart;
use Filament\Pages\Dashboard as BaseDashboard;
use Filament\Support\Enums\Width;

class Dashboard extends BaseDashboard
{
    protected static ?string $title = 'Ringkasan';

    protected static ?string $navigationLabel = 'Ringkasan';

    protected ?string $subheading = 'Pantau ritme belajar dan operasional dari satu tempat.';

    protected Width | string | null $maxContentWidth = Width::ScreenTwoExtraLarge;

    public function getWidgets(): array
    {
        return [
            DashboardHero::class,
            DashboardStats::class,
            SessionActivityChart::class,
            QuickActions::class,
            LatestMembershipRequests::class,
        ];
    }

    public function getColumns(): int | array
    {
        return [
            'default' => 1,
            'md' => 2,
            'xl' => 3,
        ];
    }
}
