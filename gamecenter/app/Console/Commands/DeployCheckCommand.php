<?php

namespace App\Console\Commands;

use Exception;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Route;
use Throwable;

/**
 * Memeriksa kesiapan aplikasi sebelum diluncurkan ke produksi.
 *
 * Perintah ini tidak mengubah apa pun; ia hanya membaca konfigurasi,
 * ekstensi PHP, izin tulis folder, dan kelengkapan aset build.
 */
class DeployCheckCommand extends Command
{
    protected $signature = 'gamecenter:deploy-check
                            {--strict : Perlakukan peringatan sebagai kegagalan (untuk CI)}';

    protected $description = 'Periksa kesiapan deploy produksi Game Center';

    /** @var array<int, array{level: string, label: string, detail: string}> */
    private array $results = [];

    public function handle(): int
    {
        $this->newLine();
        $this->line('  <options=bold>Game Center — Pemeriksaan Kesiapan Deploy</>');
        $this->newLine();

        $this->checkPhp();
        $this->checkExtensions();
        $this->checkEnvironment();
        $this->checkStorage();
        $this->checkAssets();
        $this->checkDatabase();
        $this->checkRoutes();

        return $this->renderSummary();
    }

    private function checkPhp(): void
    {
        version_compare(PHP_VERSION, '8.3.0', '>=')
            ? $this->reportPass('PHP', PHP_VERSION)
            : $this->reportFail('PHP', PHP_VERSION.' (butuh 8.3+)');
    }

    private function checkExtensions(): void
    {
        $required = [
            'ctype', 'curl', 'dom', 'fileinfo', 'filter', 'hash',
            'mbstring', 'openssl', 'pcre', 'pdo', 'session', 'tokenizer', 'xml',
        ];

        $missing = array_values(array_filter(
            $required,
            fn (string $extension): bool => ! extension_loaded($extension),
        ));

        $missing === []
            ? $this->reportPass('Ekstensi PHP', count($required).' ekstensi wajib tersedia')
            : $this->reportFail('Ekstensi PHP', 'hilang: '.implode(', ', $missing));
    }

    private function checkEnvironment(): void
    {
        $env = (string) config('app.env');
        $debug = (bool) config('app.debug');

        $env === 'production'
            ? $this->reportPass('APP_ENV', $env)
            : $this->reportWarn('APP_ENV', $env.' (produksi seharusnya "production")');

        $debug === false
            ? $this->reportPass('APP_DEBUG', 'false')
            : $this->reportWarn('APP_DEBUG', 'true — jangan dipakai di produksi');

        $key = (string) config('app.key');

        $key !== ''
            ? $this->reportPass('APP_KEY', 'terisi')
            : $this->reportFail('APP_KEY', 'kosong — jalankan "php artisan key:generate"');

        $url = (string) config('app.url');
        $isHttps = str_starts_with($url, 'https://');
        $isLocal = str_contains($url, 'localhost') || str_contains($url, '127.0.0.1') || str_contains($url, '.test');

        if ($isHttps && ! $isLocal) {
            $this->reportPass('APP_URL', $url);
        } else {
            $this->reportWarn('APP_URL', $url.' (produksi seharusnya https dan domain asli)');
        }

        config('session.secure') === true || $isHttps
            ? $this->reportPass('SESSION_SECURE_COOKIE', 'aktif')
            : $this->reportWarn('SESSION_SECURE_COOKIE', 'nonaktif — cookie sesi bisa terkirim lewat http');
    }

    private function checkStorage(): void
    {
        $paths = [
            'storage/app' => storage_path('app'),
            'storage/framework/cache' => storage_path('framework/cache'),
            'storage/framework/sessions' => storage_path('framework/sessions'),
            'storage/framework/views' => storage_path('framework/views'),
            'storage/logs' => storage_path('logs'),
            'bootstrap/cache' => base_path('bootstrap/cache'),
        ];

        $notWritable = [];

        foreach ($paths as $label => $path) {
            if (! File::isDirectory($path) || ! File::isWritable($path)) {
                $notWritable[] = $label;
            }
        }

        $notWritable === []
            ? $this->reportPass('Folder tulis', count($paths).' folder dapat ditulis')
            : $this->reportFail('Folder tulis', 'tidak dapat ditulis: '.implode(', ', $notWritable));

        File::exists(public_path('storage'))
            ? $this->reportPass('storage:link', 'symlink tersedia')
            : $this->reportWarn('storage:link', 'belum dibuat — jalankan "php artisan storage:link" bila ada unggahan');
    }

    private function checkAssets(): void
    {
        $manifest = public_path('build/manifest.json');

        if (! File::exists($manifest)) {
            $this->reportFail('Aset build', 'public/build/manifest.json tidak ada — jalankan "npm run build"');

            return;
        }

        $this->reportPass('Aset build', 'manifest.json tersedia');

        // Tema Filament dibangun terpisah dari bundel Inertia.
        $filamentTheme = null;

        try {
            $decoded = json_decode((string) File::get($manifest), true, 512, JSON_THROW_ON_ERROR);
            $filamentTheme = $decoded['resources/css/filament/admin/theme.css']['file'] ?? null;
        } catch (Throwable) {
            $this->reportWarn('Aset build', 'manifest.json tidak dapat dibaca');
        }

        $filamentTheme !== null && File::exists(public_path('build/'.$filamentTheme))
            ? $this->reportPass('Tema panel', $filamentTheme)
            : $this->reportWarn('Tema panel', 'tema admin tidak ditemukan di build');

        foreach (['sw.js', 'manifest.webmanifest', 'offline.html'] as $asset) {
            File::exists(public_path($asset))
                ? $this->reportPass('PWA '.$asset, 'tersedia')
                : $this->reportWarn('PWA '.$asset, 'tidak ditemukan di public/');
        }
    }

    private function checkDatabase(): void
    {
        try {
            DB::connection()->getPdo();

            $driver = (string) DB::connection()->getDriverName();
            $this->reportPass('Koneksi database', $driver);
        } catch (Exception $exception) {
            $this->reportFail('Koneksi database', $exception->getMessage());

            return;
        }

        try {
            $pending = count(app('migrator')->getMigrationFiles(database_path('migrations')))
                - count(DB::table('migrations')->pluck('migration')->all());

            $pending <= 0
                ? $this->reportPass('Migrasi', 'semua migrasi sudah dijalankan')
                : $this->reportWarn('Migrasi', $pending.' migrasi belum dijalankan');
        } catch (Throwable) {
            $this->reportWarn('Migrasi', 'tabel migrasi belum ada — jalankan "php artisan migrate --force"');
        }

        try {
            $users = DB::table('users')->count();
            $questions = DB::table('questions')->count();

            if ($users === 0 || $questions === 0) {
                $this->reportWarn('Data awal', "users={$users}, questions={$questions} — jalankan seeder");
            } else {
                $this->reportPass('Data awal', "users={$users}, questions={$questions}");
            }
        } catch (Throwable) {
            $this->reportWarn('Data awal', 'tabel inti belum ada');
        }
    }

    private function checkRoutes(): void
    {
        $login = Route::has('login');
        $home = Route::has('home');
        $logout = Route::has('filament.admin.auth.logout');

        $login && $home && $logout
            ? $this->reportPass('Route inti', 'login, home, logout panel tersedia')
            : $this->reportFail('Route inti', 'ada route yang hilang (login/home/logout panel)');
    }

    private function reportPass(string $label, string $detail): void
    {
        $this->results[] = ['level' => 'ok', 'label' => $label, 'detail' => $detail];
        $this->line("  <fg=green>✓</> <options=bold>{$label}</> — {$detail}");
    }

    private function reportWarn(string $label, string $detail): void
    {
        $this->results[] = ['level' => 'warn', 'label' => $label, 'detail' => $detail];
        $this->line("  <fg=yellow>!</> <options=bold>{$label}</> — {$detail}");
    }

    private function reportFail(string $label, string $detail): void
    {
        $this->results[] = ['level' => 'fail', 'label' => $label, 'detail' => $detail];
        $this->line("  <fg=red>×</> <options=bold>{$label}</> — {$detail}");
    }

    private function renderSummary(): int
    {
        $ok = count(array_filter($this->results, fn (array $row): bool => $row['level'] === 'ok'));
        $warn = count(array_filter($this->results, fn (array $row): bool => $row['level'] === 'warn'));
        $fail = count(array_filter($this->results, fn (array $row): bool => $row['level'] === 'fail'));

        $this->newLine();
        $this->line("  Hasil: <fg=green>{$ok} lulus</>, <fg=yellow>{$warn} peringatan</>, <fg=red>{$fail} gagal</>");
        $this->newLine();

        if ($fail > 0) {
            $this->error('  Belum siap deploy. Perbaiki item bertanda × di atas.');

            return self::FAILURE;
        }

        if ($warn > 0 && $this->option('strict')) {
            $this->error('  Mode strict: peringatan dianggap gagal.');

            return self::FAILURE;
        }

        $this->info('  Siap deploy. Tinjau peringatan di atas bila ada.');

        return self::SUCCESS;
    }
}
