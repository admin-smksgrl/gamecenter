<?php

namespace App\Filament\Widgets;

use App\Models\GameSession;
use Filament\Widgets\ChartWidget;
use Illuminate\Support\Carbon;

class SessionActivityChart extends ChartWidget
{
    protected ?string $heading = 'Aktivitas 7 hari';

    protected ?string $description = 'Sesi belajar yang selesai setiap hari.';

    protected ?string $maxHeight = '260px';

    protected int | string | array $columnSpan = [
        'default' => 1,
        'md' => 2,
        'xl' => 2,
    ];

    protected static ?bool $isLazyLoaded = false;

    protected static ?int $sort = -10;

    protected function getData(): array
    {
        $days = collect(range(6, 0))
            ->map(fn (int $offset) => today()->subDays($offset));

        $counts = GameSession::query()
            ->where('status', 'completed')
            ->where('completed_at', '>=', today()->subDays(6))
            ->selectRaw('DATE(completed_at) as day, COUNT(*) as total')
            ->groupBy('day')
            ->pluck('total', 'day');

        return [
            'datasets' => [
                [
                    'label' => 'Sesi selesai',
                    'data' => $days
                        ->map(fn (Carbon $day) => (int) ($counts[$day->toDateString()] ?? 0))
                        ->all(),
                    'fill' => true,
                    'pointRadius' => 0,
                    'pointHoverRadius' => 4,
                    'borderWidth' => 2,
                ],
            ],
            'labels' => $days
                ->map(fn (Carbon $day) => $day->locale('id')->isoFormat('ddd'))
                ->all(),
        ];
    }

    protected function getOptions(): array
    {
        return [
            'maintainAspectRatio' => false,
            'plugins' => [
                'legend' => ['display' => false],
            ],
            'scales' => [
                'x' => [
                    'grid' => ['display' => false],
                    'border' => ['display' => false],
                ],
                'y' => [
                    'beginAtZero' => true,
                    'border' => ['display' => false],
                    'grid' => ['drawTicks' => false],
                    'ticks' => [
                        'precision' => 0,
                        'maxTicksLimit' => 4,
                    ],
                ],
            ],
            'elements' => [
                'line' => [
                    'tension' => 0.4,
                    'borderWidth' => 2,
                ],
                'point' => [
                    'radius' => 0,
                    'hoverRadius' => 4,
                ],
            ],
        ];
    }

    protected function getType(): string
    {
        return 'line';
    }
}
