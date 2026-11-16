<?php

namespace Database\Seeders;

use App\Services\Materi\MateriImporter;
use App\Services\Materi\MateriValidationException;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\File;

/**
 * Impor seluruh materi SMA/SMK dari `database/seeders/data/sma-smk/**\/*.json`.
 *
 * Seeder ini sengaja tipis: semua logika ada di `MateriImporter` supaya
 * hasil `db:seed` dan `gamecenter:materi-import` selalu identik.
 */
class SmaSmkMaterialSeeder extends Seeder
{
    public function run(): void
    {
        $root = database_path('seeders/data/sma-smk');

        if (! File::isDirectory($root)) {
            $this->command?->warn("Folder materi tidak ada: {$root}");

            return;
        }

        $files = collect(File::allFiles($root))
            ->filter(fn ($file) => $file->getExtension() === 'json')
            ->sortBy(fn ($file) => $file->getPathname())
            ->values();

        if ($files->isEmpty()) {
            $this->command?->warn('Tidak ada berkas materi untuk diimpor.');

            return;
        }

        $importer = app(MateriImporter::class);
        $imported = 0;
        $failed = 0;

        foreach ($files as $file) {
            $relative = str_replace('\\', '/', ltrim(str_replace($root, '', $file->getPathname()), '/\\'));

            try {
                $payload = json_decode(File::get($file->getPathname()), true, 512, JSON_THROW_ON_ERROR);

                if (! is_array($payload)) {
                    throw MateriValidationException::plain("{$relative} bukan objek JSON.");
                }

                $result = $importer->import($payload, $file->getPathname());
                $imported++;

                $this->command?->info("  ✓ {$relative} — {$result->summary()}");
            } catch (MateriValidationException $exception) {
                $failed++;
                $this->command?->error("  × {$relative}");

                foreach ($exception->problems as $problem) {
                    $this->command?->line("      • {$problem}");
                }
            } catch (\JsonException $exception) {
                $failed++;
                $this->command?->error("  × {$relative} — JSON tidak sah: {$exception->getMessage()}");
            }
        }

        $this->command?->info("Materi SMA/SMK: {$imported} berkas diimpor, {$failed} gagal.");
    }
}
