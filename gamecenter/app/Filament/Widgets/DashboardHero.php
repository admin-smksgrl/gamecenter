<?php

namespace App\Filament\Widgets;

use App\Models\GameSession;
use App\Models\LearningMaterial;
use App\Models\Membership;
use App\Models\User;
use Filament\Facades\Filament;
use Filament\Widgets\Widget;
use Illuminate\Support\Str;

class DashboardHero extends Widget
{
    protected string $view = 'filament.widgets.dashboard-hero';

    protected int | string | array $columnSpan = 'full';

    protected static ?bool $isLazyLoaded = false;

    protected static ?int $sort = -30;

    protected function getViewData(): array
    {
        $user = Filament::auth()->user();
        $name = trim((string) ($user?->name ?? ''));
        $displayName = $name !== ''
            ? Str::of($name)->before('(')->trim()->toString()
            : 'Kawan';
        $isAdmin = (bool) $user?->isAdmin();
        $hour = (int) now()->format('H');

        $greeting = match (true) {
            $hour < 11 => 'Selamat pagi',
            $hour < 15 => 'Selamat siang',
            $hour < 18 => 'Selamat sore',
            default => 'Selamat malam',
        };

        return [
            'displayName' => $displayName,
            'greeting' => $greeting,
            'isAdmin' => $isAdmin,
            'dateLabel' => now()->locale('id')->translatedFormat('l, j F Y'),
            'sessionsToday' => GameSession::query()
                ->where('status', 'completed')
                ->whereDate('completed_at', today())
                ->count(),
            'activeStudents' => User::query()->students()->active()->count(),
            'activeMaterials' => LearningMaterial::query()->active()->count(),
            'pendingRequests' => $isAdmin ? Membership::query()->pending()->count() : 0,
        ];
    }
}
