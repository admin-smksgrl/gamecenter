<?php

namespace App\Filament\Resources\Chapters;

use App\Filament\Resources\Chapters\Pages\ListChapters;
use App\Filament\Resources\Chapters\Pages\ViewChapter;
use App\Models\Chapter;
use App\Models\LearningMaterial;
use App\Models\Question;
use Filament\Actions\ViewAction;
use Filament\Facades\Filament;
use Filament\Infolists\Components\TextEntry;
use Filament\Resources\Resource;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Columns\IconColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\HtmlString;

/**
 * Halaman tinjau materi SMA/SMK.
 *
 * Sengaja hanya-baca: isi chapter berasal dari berkas JSON
 * (`database/seeders/data/sma-smk`), bukan diketik di panel. Bila guru
 * menemukan kesalahan, perbaikannya dilakukan di JSON lalu
 * `php artisan gamecenter:materi-import` dijalankan ulang.
 */
class ChapterResource extends Resource
{
    protected static ?string $model = Chapter::class;

    protected static string|\BackedEnum|null $navigationIcon = Heroicon::OutlinedBookOpen;

    protected static string|\UnitEnum|null $navigationGroup = 'Materi';

    protected static ?string $navigationLabel = 'Chapter materi';

    protected static ?string $modelLabel = 'Chapter';

    protected static ?string $pluralModelLabel = 'Chapter materi';

    protected static ?int $navigationSort = 10;

    protected static ?string $recordTitleAttribute = 'title';

    public static function canCreate(): bool
    {
        return false;
    }

    public static function canEdit(mixed $record): bool
    {
        return false;
    }

    public static function canDelete(mixed $record): bool
    {
        return false;
    }

    public static function canViewAny(): bool
    {
        return Filament::auth()->check();
    }

    public static function getEloquentQuery(): Builder
    {
        return parent::getEloquentQuery()->with(['subject.classRoom.educationLevel']);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->defaultSort('subject_id')
            ->columns([
                TextColumn::make('subject.classRoom.educationLevel.name')
                    ->label('Jenjang')
                    ->badge()
                    ->color('gray')
                    ->sortable(),
                TextColumn::make('subject.classRoom.name')
                    ->label('Kelas')
                    ->sortable(),
                TextColumn::make('subject.name')
                    ->label('Mapel')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('code')
                    ->label('Kode')
                    ->badge()
                    ->color('info')
                    ->searchable(),
                TextColumn::make('title')
                    ->label('Judul')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('materials_count')
                    ->label('Materi')
                    ->counts('materials')
                    ->alignCenter(),
                TextColumn::make('questions_total')
                    ->label('Soal')
                    ->state(fn (Chapter $record): int => (int) $record->assessments()
                        ->withCount('questions')
                        ->get()
                        ->sum('questions_count'))
                    ->badge()
                    ->color(fn (int $state): string => $state === 0 ? 'danger' : 'success')
                    ->alignCenter(),
                TextColumn::make('estimated_minutes')
                    ->label('Menit')
                    ->alignCenter()
                    ->sortable(),
                IconColumn::make('is_active')
                    ->label('Aktif')
                    ->boolean(),
            ])
            ->filters([
                SelectFilter::make('education_level')
                    ->label('Jenjang')
                    ->relationship('subject.classRoom.educationLevel', 'name'),
                SelectFilter::make('subject_id')
                    ->label('Mapel')
                    ->relationship('subject', 'name')
                    ->searchable(),
            ])
            ->recordActions([
                ViewAction::make()->label('Tinjau'),
            ])
            ->emptyStateHeading('Belum ada chapter')
            ->emptyStateDescription('Jalankan php artisan gamecenter:materi-import untuk memasukkan materi.');
    }

    public static function infolist(Schema $schema): Schema
    {
        return $schema->components([
            Section::make('Identitas')
                ->columnSpanFull()
                ->columns(3)
                ->schema([
                    TextEntry::make('code')->label('Kode')->badge()->color('info'),
                    TextEntry::make('subject.name')->label('Mapel'),
                    TextEntry::make('subject.classRoom.educationLevel.name')->label('Jenjang'),
                    TextEntry::make('title')->label('Judul')->columnSpanFull(),
                    TextEntry::make('description')->label('Deskripsi')->columnSpanFull()->placeholder('—'),
                    TextEntry::make('estimated_minutes')->label('Estimasi')->suffix(' menit'),
                    TextEntry::make('materials_count')
                        ->label('Materi')
                        ->state(fn (Chapter $record): int => $record->materials()->count()),
                    TextEntry::make('questions_total')
                        ->label('Total soal')
                        ->state(fn (Chapter $record): int => (int) $record->assessments()
                            ->withCount('questions')
                            ->get()
                            ->sum('questions_count')),
                ]),
            Section::make('Tujuan pembelajaran')
                ->columnSpanFull()
                ->schema([
                    TextEntry::make('learning_objectives')
                        ->hiddenLabel()
                        ->extraAttributes(['class' => 'gc-infolist-block'])
                        ->state(fn (Chapter $record): HtmlString => new HtmlString(
                            '<ol class="list-decimal ps-5 space-y-1">'
                            . collect($record->learning_objectives ?? [])
                                ->map(fn (string $objective): string => '<li>' . e($objective) . '</li>')
                                ->implode('')
                            . '</ol>'
                        )),
                ]),
            Section::make('Materi')
                ->columnSpanFull()
                ->schema([
                    TextEntry::make('materials')
                        ->hiddenLabel()
                        ->extraAttributes(['class' => 'gc-infolist-block'])
                        ->state(fn (Chapter $record): HtmlString => new HtmlString(
                            $record->materials->isEmpty()
                                ? '<p class="text-sm text-gray-500">Belum ada materi.</p>'
                                : '<table class="w-full table-fixed text-sm"><colgroup>'
                                    . '<col style="width:3rem"><col style="width:38%">'
                                    . '<col style="width:12%"><col>'
                                    . '</colgroup><thead><tr class="text-left text-gray-500">'
                                    . '<th class="py-1 pe-3">#</th><th class="py-1 pe-3">Judul</th>'
                                    . '<th class="py-1 pe-3">Tipe</th><th class="py-1">Sumber</th></tr></thead><tbody>'
                                    . $record->materials->map(fn (LearningMaterial $material, int $i): string => '<tr class="border-t border-gray-200 align-top dark:border-white/10">'
                                        . '<td class="py-2 pe-3 tabular-nums">' . ($i + 1) . '</td>'
                                        . '<td class="py-2 pe-3 break-words">' . e($material->title) . '</td>'
                                        . '<td class="py-2 pe-3">' . e($material->type->label()) . '</td>'
                                        . '<td class="py-2 break-words text-gray-500">' . e($material->source_reference ?? '—') . '</td>'
                                        . '</tr>')
                                        ->implode('')
                                    . '</tbody></table>'
                        )),
                ]),
            Section::make('Asesmen & soal')
                ->columnSpanFull()
                ->schema([
                    TextEntry::make('assessments')
                        ->hiddenLabel()
                        ->extraAttributes(['class' => 'gc-infolist-block'])
                        ->state(fn (Chapter $record): HtmlString => new HtmlString(
                            $record->assessments->isEmpty()
                                ? '<p class="text-sm text-gray-500">Belum ada asesmen.</p>'
                                : $record->assessments->map(fn ($assessment): string => self::assessmentBlock($assessment))
                                    ->implode('')
                        )),
                ]),
        ]);
    }

    /**
     * Satu blok ringkas: judul asesmen, lalu daftar soal beserta tipe & kunci.
     */
    private static function assessmentBlock(mixed $assessment): string
    {
        $questions = $assessment->questions;

        $header = sprintf(
            '<div class="mt-4 first:mt-0"><p class="font-medium">%s — %d soal, lulus %d</p>',
            e($assessment->difficulty->label()),
            $questions->count(),
            (int) $assessment->passing_score,
        );

        $rows = $questions->map(fn (Question $question, int $i): string => sprintf(
            '<tr class="border-t border-gray-200 align-top dark:border-white/10">'
            . '<td class="py-2 pe-3 tabular-nums text-gray-500">%d</td>'
            . '<td class="py-2 pe-3 break-words">%s</td>'
            . '<td class="py-2 pe-3 text-gray-500">%s</td>'
            . '<td class="py-2 break-words text-gray-500">%s</td></tr>',
            $i + 1,
            e($question->question),
            e($question->type->label()),
            e(self::answerPreview($question)),
        ))->implode('');

        return $header
            . '<table class="w-full table-fixed text-sm"><colgroup>'
            . '<col style="width:2.5rem"><col>'
            . '<col style="width:9rem"><col style="width:11rem">'
            . '</colgroup><thead><tr class="text-left text-gray-500">'
            . '<th class="py-1 pe-3">#</th><th class="py-1 pe-3">Soal</th>'
            . '<th class="py-1 pe-3">Tipe</th><th class="py-1">Kunci</th>'
            . '</tr></thead><tbody>' . $rows . '</tbody></table></div>';
    }

    private static function answerPreview(Question $question): string
    {
        $answer = $question->correct_answer ?? [];

        if (isset($answer['text'])) {
            return (string) $answer['text'];
        }

        if (isset($answer['texts'])) {
            return implode(', ', (array) $answer['texts']);
        }

        if (isset($answer['order'])) {
            return implode(' → ', (array) $answer['order']);
        }

        if (isset($answer['map'])) {
            return collect((array) $answer['map'])
                ->map(fn ($value, $key): string => "{$key}:{$value}")
                ->implode(', ');
        }

        return '—';
    }

    public static function getPages(): array
    {
        return [
            'index' => ListChapters::route('/'),
            'view' => ViewChapter::route('/{record}'),
        ];
    }
}
