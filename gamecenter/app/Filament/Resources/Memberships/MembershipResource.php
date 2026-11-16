<?php

namespace App\Filament\Resources\Memberships;

use App\Enums\BillingCycle;
use App\Enums\MembershipStatus;
use App\Filament\Resources\Memberships\Pages\ListMemberships;
use App\Models\Membership;
use App\Models\User;
use Filament\Actions\Action;
use Filament\Facades\Filament;
use Filament\Forms\Components\Textarea;
use Filament\Notifications\Notification;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Number;

class MembershipResource extends Resource
{
    protected static ?string $model = Membership::class;

    protected static string|\BackedEnum|null $navigationIcon = Heroicon::OutlinedBanknotes;

    protected static string|\UnitEnum|null $navigationGroup = 'Keanggotaan';

    protected static ?string $navigationLabel = 'Pengajuan upgrade';

    protected static ?string $modelLabel = 'Membership';

    protected static ?string $pluralModelLabel = 'Membership';

    protected static ?int $navigationSort = 20;

    protected static ?string $recordTitleAttribute = 'reference';

    public static function canViewAny(): bool
    {
        return Filament::auth()->user()?->isAdmin() ?? false;
    }

    public static function canCreate(): bool
    {
        return false;
    }

    public static function canEdit(Model $record): bool
    {
        return false;
    }

    public static function canDelete(Model $record): bool
    {
        return false;
    }

    public static function getNavigationBadge(): ?string
    {
        if (! static::canViewAny()) {
            return null;
        }

        $pending = Membership::query()->pending()->count();

        return $pending > 0 ? (string) $pending : null;
    }

    public static function getNavigationBadgeColor(): ?string
    {
        return 'warning';
    }

    public static function form(Schema $schema): Schema
    {
        return $schema;
    }

    public static function table(Table $table): Table
    {
        return $table
            ->defaultSort('created_at', 'desc')
            ->emptyStateHeading('Belum ada pengajuan')
            ->emptyStateDescription('Pengajuan upgrade dari halaman keanggotaan akan muncul di sini.')
            ->columns([
                TextColumn::make('user.name')
                    ->label('Anggota')
                    ->description(fn (Membership $record) => $record->user?->email)
                    ->searchable()
                    ->sortable(),
                TextColumn::make('plan.name')
                    ->label('Paket')
                    ->badge()
                    ->color(fn (Membership $record) => match ($record->plan?->tier) {
                        'enterprise' => 'danger',
                        'professional' => 'warning',
                        'standard' => 'info',
                        default => 'gray',
                    }),
                TextColumn::make('billing_cycle')
                    ->label('Siklus')
                    ->formatStateUsing(fn (BillingCycle|string $state) => $state instanceof BillingCycle
                        ? $state->label()
                        : BillingCycle::from($state)->label()),
                TextColumn::make('amount')
                    ->label('Nominal')
                    ->formatStateUsing(fn (int $state) => Number::currency($state, 'IDR', 'id')),
                TextColumn::make('status')
                    ->badge()
                    ->formatStateUsing(fn (MembershipStatus|string $state) => $state instanceof MembershipStatus
                        ? $state->label()
                        : MembershipStatus::from($state)->label())
                    ->color(fn (MembershipStatus|string $state) => $state instanceof MembershipStatus
                        ? $state->color()
                        : MembershipStatus::from($state)->color()),
                TextColumn::make('reference')
                    ->label('Referensi')
                    ->copyable()
                    ->searchable(),
                TextColumn::make('created_at')
                    ->label('Diajukan')
                    ->dateTime('d M Y H:i')
                    ->sortable(),
            ])
            ->filters([
                SelectFilter::make('status')
                    ->label('Status')
                    ->options([
                        MembershipStatus::Pending->value => MembershipStatus::Pending->label(),
                        MembershipStatus::Active->value => MembershipStatus::Active->label(),
                        MembershipStatus::Expired->value => MembershipStatus::Expired->label(),
                        MembershipStatus::Rejected->value => MembershipStatus::Rejected->label(),
                    ]),
            ])
            ->recordActions([
                Action::make('approve')
                    ->label('Setujui')
                    ->icon(Heroicon::OutlinedCheckCircle)
                    ->color('success')
                    ->visible(fn (Membership $record) => $record->status === MembershipStatus::Pending)
                    ->requiresConfirmation()
                    ->modalHeading('Setujui pengajuan upgrade')
                    ->modalDescription(fn (Membership $record) => "Aktifkan paket {$record->plan?->name} untuk {$record->user?->name} ({$record->billing_cycle->label()})?")
                    ->modalSubmitActionLabel('Setujui')
                    ->schema([
                        Textarea::make('admin_note')
                            ->label('Catatan admin (opsional)')
                            ->rows(3),
                    ])
                    ->action(function (Membership $record, array $data): void {
                        /** @var User|null $admin */
                        $admin = Filament::auth()->user();

                        if (! $admin) {
                            return;
                        }

                        $record->approve($admin, $data['admin_note'] ?? null);

                        Notification::make()
                            ->success()
                            ->title('Pengajuan disetujui')
                            ->body('Paket anggota sudah aktif.')
                            ->send();
                    }),
                Action::make('reject')
                    ->label('Tolak')
                    ->icon(Heroicon::OutlinedXCircle)
                    ->color('danger')
                    ->visible(fn (Membership $record) => $record->status === MembershipStatus::Pending)
                    ->requiresConfirmation()
                    ->modalHeading('Tolak pengajuan upgrade')
                    ->modalDescription('Pengajuan akan ditandai ditolak dan user dapat mengajukan ulang.')
                    ->modalSubmitActionLabel('Tolak pengajuan')
                    ->schema([
                        Textarea::make('admin_note')
                            ->label('Alasan penolakan')
                            ->required()
                            ->rows(3),
                    ])
                    ->action(function (Membership $record, array $data): void {
                        /** @var User|null $admin */
                        $admin = Filament::auth()->user();

                        if (! $admin) {
                            return;
                        }

                        $record->reject($admin, $data['admin_note']);

                        Notification::make()
                            ->success()
                            ->title('Pengajuan ditolak')
                            ->send();
                    }),
            ]);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListMemberships::route('/'),
        ];
    }
}
