<?php

namespace App\Console\Commands;

use App\Services\Materi\MateriImporter;
use App\Services\Materi\MateriImportResult;
use App\Services\Materi\MateriValidationException;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;
use Throwable;

/**
 * Impor materi SMA/SMK dari berkas JSON ke database.
 *
 * Contoh:
 *   php artisan gamecenter:materi-import
 *   php artisan gamecenter:materi-import fase-e/matematika.json
 *   php artisan gamecenter:materi-import --dry-run
 */
class MateriImportCommand extends Command
{
    protected $signature = 'gamecenter:materi-import
        {path? : Berkas atau folder relatif terhadap database/seeders/data/sma-smk}
        {--dry-run : Hanya memeriksa skema, tidak menulis ke database}';

    protected $description = 'Impor materi SMA/SMK dari JSON (idempoten)';

    public function handle(MateriImporter $importer): int
    {
        $root = database_path('seeders/data/sma-smk');
        $target = $this->argument('path');

        if (! File::isDirectory($root)) {
            $this->reportFail("Folder materi tidak ada: {$root}");

            return self::FAILURE;
        }

        $files = $this->resolveFiles($root, $target);

        if ($files === []) {
            $this->reportFail($target
                ? "Tidak ada berkas .json di {$target}"
                : 'Tidak ada berkas .json untuk diimpor.');

            return self::FAILURE;
        }

        $dryRun = (bool) $this->option('dry-run');
        $failures = 0;
        $totals = new MateriImportResult;
        $started = microtime(true);

        $this->newLine();
        $this->line('  <options=bold>Game Center — Impor Materi SMA/SMK</options=bold>');
        $this->line($dryRun ? '  Mode: periksa saja (dry-run)' : '  Mode: tulis ke database');
        $this->newLine();

        foreach ($files as $file) {
            $relative = $this->relativePath($root, $file);

            try {
                $payload = $this->readJson($file);

                if ($dryRun) {
                    $this->validateOnly($importer, $payload, $file);
                    $this->reportPass($relative, new MateriImportResult, true, count($payload['chapters']));

                    continue;
                }

                $result = $importer->import($payload, $file);
                $this->accumulate($totals, $result);
                $this->reportPass($relative, $result, false);
            } catch (MateriValidationException $exception) {
                $failures++;
                $this->reportFail($relative);

                foreach ($exception->problems as $problem) {
                    $this->line("      <fg=red>•</> {$problem}");
                }
            } catch (Throwable $exception) {
                $failures++;
                $this->reportFail($relative . ' — ' . $exception->getMessage());
            }
        }

        $this->newLine();

        if ($dryRun) {
            $this->line(sprintf(
                '  Diperiksa: %d berkas, %d gagal. Tidak ada yang ditulis.',
                count($files),
                $failures,
            ));
        } else {
            $this->line('  ' . $totals->summary());
        }

        $elapsed = number_format(microtime(true) - $started, 2);
        $this->line("  Selesai dalam {$elapsed} detik.");
        $this->newLine();

        return $failures === 0 ? self::SUCCESS : self::FAILURE;
    }

    /**
     * @return array<int, string>
     */
    private function resolveFiles(string $root, ?string $target): array
    {
        if ($target === null) {
            return collect(File::allFiles($root))
                ->filter(fn ($file) => $file->getExtension() === 'json')
                ->map(fn ($file) => $file->getPathname())
                ->sort()
                ->values()
                ->all();
        }

        $path = $root . DIRECTORY_SEPARATOR . str_replace(['/', '\\'], DIRECTORY_SEPARATOR, $target);

        if (File::isFile($path)) {
            return [$path];
        }

        if (File::isDirectory($path)) {
            return collect(File::allFiles($path))
                ->filter(fn ($file) => $file->getExtension() === 'json')
                ->map(fn ($file) => $file->getPathname())
                ->sort()
                ->values()
                ->all();
        }

        return [];
    }

    /**
     * @return array<string, mixed>
     */
    private function readJson(string $file): array
    {
        $raw = File::get($file);
        $decoded = json_decode($raw, true);

        if (! is_array($decoded)) {
            throw MateriValidationException::plain(
                basename($file) . ' bukan JSON yang sah: ' . json_last_error_msg(),
            );
        }

        return $decoded;
    }

    private function relativePath(string $root, string $file): string
    {
        return str_replace('\\', '/', ltrim(str_replace($root, '', $file), '/\\'));
    }

    /**
     * Pada dry-run tidak ada satu baris pun yang ditulis: cukup periksa skema.
     *
     * @param  array<string, mixed>  $payload
     */
    private function validateOnly(MateriImporter $importer, array $payload, string $file): void
    {
        $problems = app(\App\Services\Materi\MateriSchema::class)->problems($payload);

        if ($problems !== []) {
            throw MateriValidationException::inFile($file, $problems);
        }
    }

    private function reportPass(string $name, MateriImportResult $result, bool $dryRun, int $chapterCount = 0): void
    {
        $detail = $dryRun
            ? sprintf('%d chapter, skema valid', $chapterCount)
            : $result->summary();

        $this->line("  <fg=green>✓</> <options=bold>{$name}</options=bold> — {$detail}");
    }

    private function reportFail(string $message): void
    {
        $this->line("  <fg=red>×</> {$message}");
    }

    private function accumulate(MateriImportResult $totals, MateriImportResult $result): void
    {
        $totals->chaptersCreated += $result->chaptersCreated;
        $totals->chaptersUpdated += $result->chaptersUpdated;
        $totals->materialsCreated += $result->materialsCreated;
        $totals->materialsUpdated += $result->materialsUpdated;
        $totals->assessmentsCreated += $result->assessmentsCreated;
        $totals->assessmentsUpdated += $result->assessmentsUpdated;
        $totals->questionsCreated += $result->questionsCreated;
        $totals->questionsUpdated += $result->questionsUpdated;
        $totals->optionsCreated += $result->optionsCreated;

        foreach ($result->warnings as $warning) {
            $totals->addWarning($warning);
        }
    }

    private function countChapters(MateriImportResult $result): int
    {
        return $result->chaptersCreated + $result->chaptersUpdated;
    }
}