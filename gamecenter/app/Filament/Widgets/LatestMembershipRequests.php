<?php

namespace App\Filament\Widgets;

use App\Enums\MembershipStatus;
use App\Filament\Resources\Memberships\MembershipResource;
use App\Models\Membership;
use Filament\Actions\Action;
use Filament\Facades\Filament;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Filament\Widgets\TableWidget;
use Illuminate\Support\Number;

class LatestMembershipRequests extends TableWidget
{
    protected int | string | array $columnSpan = 'full';

    protected static ?bool $isLazyLoaded = false;

    protected static ?int $sort = 10;

    public static function canView(): bool
    {
        return Filament::auth()->user()?->isAdmin() ?? false;
    }

    public function table(Table $table): Table
    {
        return $table
            ->heading('Pengajuan upgrade terbaru')
            ->description('Pantau permintaan keanggotaan yang masuk dari halaman siswa.')
            ->query(
                Membership::query()
                    ->with(['user', 'plan'])
                    ->latest()
                    ->limit(5),
            )
            ->paginated(false)
            ->recordUrl(fn (Membership $record): string => MembershipResource::getUrl('index'))
            ->emptyStateHeading('Belum ada pengajuan')
            ->emptyStateDescription('Pengajuan upgrade dari halaman keanggotaan akan muncul di sini.')
            ->emptyStateIcon(Heroicon::OutlinedInbox)
            ->columns([
                TextColumn::make('user.name')
                    ->label('Anggota')
                    ->description(fn (Membership $record) => $record->user?->email),
                TextColumn::make('plan.name')
                    ->label('Paket')
                    ->badge()
                    ->color(fn (Membership $record) => match ($record->plan?->tier) {
                        'enterprise' => 'danger',
                        'professional' => 'warning',
                        'standard' => 'info',
                        default => 'gray',
                    }),
                TextColumn::make('amount')
                    ->label('Nominal')
                    ->formatStateUsing(fn (int $state) => Number::currency($state, 'IDR', 'id'))
                    ->visibleFrom('md'),
                TextColumn::make('status')
                    ->label('Status')
                    ->badge()
                    ->visibleFrom('sm')
                    ->formatStateUsing(fn (MembershipStatus | string $state) => $state instanceof MembershipStatus
                        ? $state->label()
                        : MembershipStatus::from($state)->label())
                    ->color(fn (MembershipStatus | string $state) => $state instanceof MembershipStatus
                        ? $state->color()
                        : MembershipStatus::from($state)->color()),
                TextColumn::make('created_at')
                    ->label('Diajukan')
                    ->since()
                    ->visibleFrom('md')
                    ->tooltip(fn (Membership $record) => $record->created_at?->format('d M Y H:i')),
            ])
            ->headerActions([
                Action::make('viewAll')
                    ->label('Lihat semua')
                    ->icon(Heroicon::OutlinedArrowRight)
                    ->color('gray')
                    ->url(MembershipResource::getUrl('index')),
            ]);
    }
}
