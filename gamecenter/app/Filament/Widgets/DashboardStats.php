<?php

namespace App\Filament\Widgets;

use App\Models\GameSession;
use App\Models\LearningMaterial;
use App\Models\Membership;
use App\Models\Question;
use App\Models\User;
use Filament\Facades\Filament;
use Filament\Widgets\StatsOverviewWidget;
use Filament\Widgets\StatsOverviewWidget\Stat;
use Illuminate\Support\Carbon;

class DashboardStats extends StatsOverviewWidget
{
    protected static ?bool $isLazyLoaded = false;

    protected static ?int $sort = -20;

    protected int | array | null $columns = [
        'default' => 2,
        'xl' => 4,
    ];

    protected function getStats(): array
    {
        $days = collect(range(6, 0))
            ->map(fn (int $offset) => today()->subDays($offset));

        $sessionsByDay = GameSession::query()
            ->where('status', 'completed')
            ->where('completed_at', '>=', today()->subDays(6))
            ->selectRaw('DATE(completed_at) as day, COUNT(*) as total')
            ->groupBy('day')
            ->pluck('total', 'day');

        $scoresByDay = GameSession::query()
            ->where('status', 'completed')
            ->where('completed_at', '>=', today()->subDays(6))
            ->selectRaw('DATE(completed_at) as day, AVG(score) as average')
            ->groupBy('day')
            ->pluck('average', 'day');

        $studentsByDay = User::query()
            ->students()
            ->where('created_at', '>=', today()->subDays(6))
            ->selectRaw('DATE(created_at) as day, COUNT(*) as total')
            ->groupBy('day')
            ->pluck('total', 'day');

        $sessionSeries = $days
            ->map(fn (Carbon $day) => (float) ($sessionsByDay[$day->toDateString()] ?? 0))
            ->all();

        $scoreSeries = $days
            ->map(fn (Carbon $day) => round((float) ($scoresByDay[$day->toDateString()] ?? 0)))
            ->all();

        $studentSeries = $days
            ->map(fn (Carbon $day) => (float) ($studentsByDay[$day->toDateString()] ?? 0))
            ->all();

        $completedSessions = GameSession::query()
            ->where('status', 'completed')
            ->count();

        $sessionsToday = GameSession::query()
            ->where('status', 'completed')
            ->whereDate('completed_at', today())
            ->count();

        $averageScore = (int) round(
            (float) (GameSession::query()
                ->where('status', 'completed')
                ->avg('score') ?? 0)
        );

        $stats = [
            Stat::make('Sesi selesai', number_format($completedSessions, 0, ',', '.'))
                ->description($sessionsToday.' sesi hari ini')
                ->descriptionIcon('heroicon-m-arrow-trending-up')
                ->chart($sessionSeries)
                ->color('primary'),
            Stat::make('Siswa aktif', number_format(User::query()->students()->active()->count(), 0, ',', '.'))
                ->description(number_format(User::query()->students()->count(), 0, ',', '.').' akun terdaftar')
                ->descriptionIcon('heroicon-m-user-group')
                ->chart($studentSeries)
                ->color('info'),
            Stat::make('Rata-rata skor', $averageScore)
                ->description('Dari '.number_format($completedSessions, 0, ',', '.').' sesi dinilai')
                ->descriptionIcon('heroicon-m-academic-cap')
                ->chart($scoreSeries)
                ->color('success'),
        ];

        if (Filament::auth()->user()?->isAdmin()) {
            $pendingByDay = Membership::query()
                ->where('created_at', '>=', today()->subDays(6))
                ->selectRaw('DATE(created_at) as day, COUNT(*) as total')
                ->groupBy('day')
                ->pluck('total', 'day');

            $pendingSeries = $days
                ->map(fn (Carbon $day) => (float) ($pendingByDay[$day->toDateString()] ?? 0))
                ->all();

            $stats[] = Stat::make(
                'Pengajuan menunggu',
                number_format(Membership::query()->pending()->count(), 0, ',', '.'),
            )
                ->description(Membership::query()->active()->count().' membership aktif')
                ->descriptionIcon('heroicon-m-clock')
                ->chart($pendingSeries)
                ->color('warning');
        } else {
            $stats[] = Stat::make(
                'Materi aktif',
                number_format(LearningMaterial::query()->active()->count(), 0, ',', '.'),
            )
                ->description(number_format(Question::query()->count(), 0, ',', '.').' soal di bank soal')
                ->descriptionIcon('heroicon-m-book-open')
                ->color('warning');
        }

        return $stats;
    }
}
