<?php

namespace Tests\Feature;

use Illuminate\Support\Facades\Artisan;
use Tests\TestCase;

class DeployCheckCommandTest extends TestCase
{
    /**
     * @return array{code: int, output: string}
     */
    private function runCheck(array $options = []): array
    {
        $code = Artisan::call('gamecenter:deploy-check', $options + ['--no-ansi' => true]);

        // Buang kode ANSI agar teks bisa dicari apa adanya.
        $output = (string) preg_replace('/\e\[[0-9;]*m/', '', Artisan::output());

        return ['code' => $code, 'output' => $output];
    }

    public function test_deploy_check_command_reports_every_section(): void
    {
        $result = $this->runCheck();

        $this->assertSame(0, $result['code']);

        $fragments = [
            'Pemeriksaan Kesiapan Deploy',
            'PHP',
            'Ekstensi',
            'APP_KEY',
            'Folder tulis',
            'Aset build',
            'Koneksi database',
            'Route inti',
            'Hasil:',
        ];

        foreach ($fragments as $fragment) {
            $this->assertStringContainsString($fragment, $result['output'], "Output tidak memuat: {$fragment}");
        }
    }

    public function test_deploy_check_reports_missing_assets_as_failure(): void
    {
        // Saat manifest build tidak ada, pemeriksaan harus melaporkan kegagalan
        // (bukan lolos diam-diam), karena aset adalah syarat deploy.
        $manifest = public_path('build/manifest.json');

        if (! file_exists($manifest)) {
            $this->markTestSkipped('Manifest build memang belum ada.');
        }

        $backup = (string) file_get_contents($manifest);
        unlink($manifest);

        try {
            $result = $this->runCheck(['--strict' => true]);

            $this->assertSame(1, $result['code']);
            $this->assertStringContainsString('npm run build', $result['output']);
        } finally {
            file_put_contents($manifest, $backup);
        }
    }

    public function test_strict_mode_fails_when_only_warnings_remain(): void
    {
        // Di lingkungan test APP_ENV=testing & APP_DEBUG=true, jadi ada
        // peringatan. Mode strict memperlakukan peringatan sebagai kegagalan
        // supaya CI tidak meloloskan konfigurasi yang belum siap produksi.
        $result = $this->runCheck(['--strict' => true]);

        $this->assertSame(1, $result['code']);
        $this->assertStringContainsString('0 gagal', $result['output']);
        $this->assertStringContainsString('Mode strict', $result['output']);
    }

    public function test_non_strict_mode_passes_with_warnings_only(): void
    {
        $result = $this->runCheck();

        $this->assertSame(0, $result['code']);
        $this->assertStringContainsString('0 gagal', $result['output']);
        $this->assertStringContainsString('Siap deploy', $result['output']);
    }

    public function test_production_env_template_has_safe_defaults(): void
    {
        $path = base_path('.env.production.example');

        $this->assertFileExists($path);

        $contents = (string) file_get_contents($path);

        $this->assertStringContainsString('APP_ENV=production', $contents);
        $this->assertStringContainsString('APP_DEBUG=false', $contents);
        $this->assertStringContainsString('SESSION_ENCRYPT=true', $contents);
        $this->assertStringContainsString('SESSION_SECURE_COOKIE=true', $contents);

        // Tidak boleh ada kredensial nyata atau default lokal.
        $this->assertStringNotContainsString('DB_PASSWORD=root', $contents);
        $this->assertStringNotContainsString('DB_USERNAME=root', $contents);
        $this->assertStringNotContainsString('APP_URL=http://', $contents);
    }
}
