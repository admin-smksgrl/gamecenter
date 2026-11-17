<?php

namespace App\Filament\Resources\Chapters\Pages;

use App\Filament\Resources\Chapters\ChapterResource;
use App\Services\Materi\BlockPracticeReport;
use Filament\Actions\Action;
use Filament\Resources\Pages\ViewRecord;
use Filament\Support\Icons\Heroicon;

class ViewChapter extends ViewRecord
{
    protected static string $resource = ChapterResource::class;

    public function getTitle(): string
    {
        return (string) $this->getRecord()->title;
    }

    /**
     * Ekspor CSV skor blok (plan Fase 5.4).
     *
     * Guru dapat mengunduh rekap formatif per siswa × blok untuk satu chapter,
     * lalu mengolahnya di spreadsheet. Tidak menyentuh nilai sesi/rapor.
     *
     * @return array<int, Action>
     */
    protected function getHeaderActions(): array
    {
        return [
            Action::make('exportBlockScores')
                ->label('Ekspor CSV skor blok')
                ->icon(Heroicon::OutlinedArrowDownTray)
                ->visible(fn (): bool => $this->blockResponseCount() > 0)
                ->action(function (BlockPracticeReport $report) {
                    $chapter = $this->getRecord();

                    return response()->streamDownload(
                        fn () => print $report->chapterCsv($chapter),
                        'skor-blok-' . $chapter->code . '.csv',
                        ['Content-Type' => 'text/csv; charset=UTF-8'],
                    );
                }),
        ];
    }

    private function blockResponseCount(): int
    {
        return $this->getRecord()
            ->materials()
            ->whereHas('blockResponses')
            ->count();
    }
}
