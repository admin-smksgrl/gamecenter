<?php

namespace App\Filament\Resources\MembershipPlans;

use App\Filament\Resources\MembershipPlans\Pages\CreateMembershipPlan;
use App\Filament\Resources\MembershipPlans\Pages\EditMembershipPlan;
use App\Filament\Resources\MembershipPlans\Pages\ListMembershipPlans;
use App\Models\MembershipPlan;
use Filament\Actions\EditAction;
use Filament\Facades\Filament;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Resources\Resource;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Columns\IconColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Number;

class MembershipPlanResource extends Resource
{
    protected static ?string $model = MembershipPlan::class;

    protected static string|\BackedEnum|null $navigationIcon = Heroicon::OutlinedCreditCard;

    protected static string|\UnitEnum|null $navigationGroup = 'Keanggotaan';

    protected static ?string $navigationLabel = 'Paket';

    protected static ?string $modelLabel = 'Paket';

    protected static ?string $pluralModelLabel = 'Paket keanggotaan';

    protected static ?int $navigationSort = 10;

    protected static ?string $recordTitleAttribute = 'name';

    public static function canViewAny(): bool
    {
        return Filament::auth()->user()?->isAdmin() ?? false;
    }

    public static function canCreate(): bool
    {
        return Filament::auth()->user()?->isAdmin() ?? false;
    }

    public static function canEdit(Model $record): bool
    {
        return Filament::auth()->user()?->isAdmin() ?? false;
    }

    public static function canDelete(Model $record): bool
    {
        return false;
    }

    public static function form(Schema $schema): Schema
    {
        return $schema->components([
            Section::make('Detail paket')
                ->columns(2)
                ->schema([
                    TextInput::make('name')
                        ->required()
                        ->maxLength(100),
                    TextInput::make('slug')
                        ->required()
                        ->maxLength(40)
                        ->unique(ignoreRecord: true),
                    Select::make('tier')
                        ->options([
                            'free' => 'Gratis',
                            'standard' => 'Standard',
                            'professional' => 'Professional',
                            'enterprise' => 'Enterprise',
                        ])
                        ->required(),
                    TextInput::make('tagline')
                        ->maxLength(160)
                        ->columnSpanFull(),
                    Textarea::make('description')
                        ->rows(3)
                        ->columnSpanFull(),
                    TextInput::make('price_monthly')
                        ->label('Harga bulanan')
                        ->numeric()
                        ->minValue(0)
                        ->prefix('Rp')
                        ->required(),
                    TextInput::make('price_yearly')
                        ->label('Harga tahunan')
                        ->numeric()
                        ->minValue(0)
                        ->prefix('Rp')
                        ->required(),
                    TagsInput::make('features')
                        ->label('Fitur')
                        ->placeholder('Tulis fitur lalu tekan Enter')
                        ->columnSpanFull(),
                    Toggle::make('is_featured')
                        ->label('Tampilkan sebagai unggulan'),
                    Toggle::make('is_active')
                        ->label('Aktif')
                        ->default(true),
                    TextInput::make('sort_order')
                        ->label('Urutan')
                        ->numeric()
                        ->default(0),
                ]),
        ]);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->defaultSort('sort_order')
            ->columns([
                TextColumn::make('name')
                    ->label('Paket')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('tier')
                    ->badge()
                    ->color(fn (string $state) => match ($state) {
                        'enterprise' => 'danger',
                        'professional' => 'warning',
                        'standard' => 'info',
                        default => 'gray',
                    }),
                TextColumn::make('price_monthly')
                    ->label('Bulanan')
                    ->formatStateUsing(fn (int $state) => Number::currency($state, 'IDR', 'id'))
                    ->sortable(),
                TextColumn::make('price_yearly')
                    ->label('Tahunan')
                    ->formatStateUsing(fn (int $state) => Number::currency($state, 'IDR', 'id'))
                    ->sortable(),
                TextColumn::make('memberships_count')
                    ->counts('memberships')
                    ->label('Membership')
                    ->sortable(),
                IconColumn::make('is_featured')
                    ->label('Unggulan')
                    ->boolean(),
                IconColumn::make('is_active')
                    ->label('Aktif')
                    ->boolean(),
                TextColumn::make('sort_order')
                    ->label('Urutan')
                    ->sortable(),
            ])
            ->recordActions([
                EditAction::make(),
            ]);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListMembershipPlans::route('/'),
            'create' => CreateMembershipPlan::route('/create'),
            'edit' => EditMembershipPlan::route('/{record}/edit'),
        ];
    }
}
