<?php

namespace Database\Seeders;

use App\Models\ClassRoom;
use App\Models\Subject;
use Illuminate\Database\Seeder;

class SubjectSeeder extends Seeder
{
    /**
     * Mata pelajaran per jenjang/kelas.
     *
     * @var array<string, array<int, array{name: string, slug: string, group: string, icon: string, color: string}>>
     */
    private array $catalog = [
        'paud' => [
            ['name' => 'Mengenal Bentuk & Warna', 'slug' => 'bentuk-warna', 'group' => 'Dasar', 'icon' => '🔺', 'color' => 'rose'],
            ['name' => 'Angka & Berhitung', 'slug' => 'angka-berhitung', 'group' => 'Kognitif', 'icon' => '🔢', 'color' => 'amber'],
            ['name' => 'Huruf & Membaca', 'slug' => 'huruf-membaca', 'group' => 'Bahasa', 'icon' => '🅰️', 'color' => 'sky'],
            ['name' => 'Anggota Tubuh', 'slug' => 'anggota-tubuh', 'group' => 'Diri Sendiri', 'icon' => '🙋', 'color' => 'emerald'],
            ['name' => 'Hewan & Tanaman', 'slug' => 'hewan-tanaman', 'group' => 'Lingkungan', 'icon' => '🐘', 'color' => 'lime'],
            ['name' => 'Lagu & Gerak', 'slug' => 'lagu-gerak', 'group' => 'Seni', 'icon' => '🎵', 'color' => 'violet'],
        ],
        'tk' => [
            ['name' => 'Literasi Awal', 'slug' => 'literasi-awal', 'group' => 'Bahasa', 'icon' => '📚', 'color' => 'sky'],
            ['name' => 'Numerasi Awal', 'slug' => 'numerasi-awal', 'group' => 'Kognitif', 'icon' => '🔢', 'color' => 'amber'],
            ['name' => 'Sains Sederhana', 'slug' => 'sains-sederhana', 'group' => 'Kognitif', 'icon' => '🔬', 'color' => 'emerald'],
            ['name' => 'Sosial Emosional', 'slug' => 'sosial-emosional', 'group' => 'Sikap', 'icon' => '🤝', 'color' => 'rose'],
            ['name' => 'Motorik & Kesehatan', 'slug' => 'motorik-kesehatan', 'group' => 'Jasmani', 'icon' => '🏃', 'color' => 'lime'],
            ['name' => 'Seni & Kreativitas', 'slug' => 'seni-kreativitas', 'group' => 'Seni', 'icon' => '🎨', 'color' => 'violet'],
        ],
        'sd' => [
            ['name' => 'Pendidikan Agama dan Budi Pekerti', 'slug' => 'pai', 'group' => 'Wajib', 'icon' => '🕌', 'color' => 'emerald'],
            ['name' => 'Pendidikan Pancasila', 'slug' => 'pancasila', 'group' => 'Wajib', 'icon' => '🇮🇩', 'color' => 'rose'],
            ['name' => 'Bahasa Indonesia', 'slug' => 'bahasa-indonesia', 'group' => 'Wajib', 'icon' => '📖', 'color' => 'amber'],
            ['name' => 'Matematika', 'slug' => 'matematika', 'group' => 'Wajib', 'icon' => '➗', 'color' => 'blue'],
            ['name' => 'Ilmu Pengetahuan Alam dan Sosial', 'slug' => 'ipas', 'group' => 'Wajib', 'icon' => '🔬', 'color' => 'teal'],
            ['name' => 'Bahasa Inggris', 'slug' => 'bahasa-inggris', 'group' => 'Wajib', 'icon' => '🔤', 'color' => 'indigo'],
            ['name' => 'PJOK', 'slug' => 'pjok', 'group' => 'Wajib', 'icon' => '⚽', 'color' => 'lime'],
            ['name' => 'Seni Budaya', 'slug' => 'seni-budaya', 'group' => 'Seni', 'icon' => '🎭', 'color' => 'violet'],
        ],
        'smp' => [
            ['name' => 'Pendidikan Agama dan Budi Pekerti', 'slug' => 'pai', 'group' => 'Wajib', 'icon' => '🕌', 'color' => 'emerald'],
            ['name' => 'Pendidikan Pancasila', 'slug' => 'pancasila', 'group' => 'Wajib', 'icon' => '🇮🇩', 'color' => 'rose'],
            ['name' => 'Bahasa Indonesia', 'slug' => 'bahasa-indonesia', 'group' => 'Wajib', 'icon' => '📖', 'color' => 'amber'],
            ['name' => 'Matematika', 'slug' => 'matematika', 'group' => 'Wajib', 'icon' => '➗', 'color' => 'blue'],
            ['name' => 'Ilmu Pengetahuan Alam', 'slug' => 'ipa', 'group' => 'Wajib', 'icon' => '🔬', 'color' => 'teal'],
            ['name' => 'Ilmu Pengetahuan Sosial', 'slug' => 'ips', 'group' => 'Wajib', 'icon' => '🌏', 'color' => 'green'],
            ['name' => 'Bahasa Inggris', 'slug' => 'bahasa-inggris', 'group' => 'Wajib', 'icon' => '🔤', 'color' => 'indigo'],
            ['name' => 'Informatika', 'slug' => 'informatika', 'group' => 'Wajib', 'icon' => '💻', 'color' => 'cyan'],
            ['name' => 'PJOK', 'slug' => 'pjok', 'group' => 'Wajib', 'icon' => '⚽', 'color' => 'lime'],
            ['name' => 'Prakarya', 'slug' => 'prakarya', 'group' => 'Keterampilan', 'icon' => '🛠️', 'color' => 'red'],
            ['name' => 'Seni Budaya', 'slug' => 'seni-budaya', 'group' => 'Seni', 'icon' => '🎭', 'color' => 'violet'],
        ],
        'sma' => [
            ['name' => 'Pendidikan Agama Islam dan Budi Pekerti', 'slug' => 'pai', 'group' => 'Wajib', 'icon' => '🕌', 'color' => 'emerald'],
            ['name' => 'Pendidikan Pancasila', 'slug' => 'pancasila', 'group' => 'Wajib', 'icon' => '🇮🇩', 'color' => 'rose'],
            ['name' => 'Bahasa Indonesia', 'slug' => 'bahasa-indonesia', 'group' => 'Wajib', 'icon' => '📖', 'color' => 'amber'],
            ['name' => 'Matematika', 'slug' => 'matematika', 'group' => 'Wajib', 'icon' => '➗', 'color' => 'blue'],
            ['name' => 'Bahasa Inggris', 'slug' => 'bahasa-inggris', 'group' => 'Wajib', 'icon' => '🔤', 'color' => 'indigo'],
            ['name' => 'Sejarah', 'slug' => 'sejarah', 'group' => 'Wajib', 'icon' => '🏛️', 'color' => 'stone'],
            ['name' => 'Informatika', 'slug' => 'informatika', 'group' => 'Wajib', 'icon' => '💻', 'color' => 'cyan'],
            ['name' => 'PJOK', 'slug' => 'pjok', 'group' => 'Wajib', 'icon' => '⚽', 'color' => 'lime'],
            ['name' => 'Fisika', 'slug' => 'fisika', 'group' => 'IPA', 'icon' => '🧪', 'color' => 'violet'],
            ['name' => 'Kimia', 'slug' => 'kimia', 'group' => 'IPA', 'icon' => '⚗️', 'color' => 'fuchsia'],
            ['name' => 'Biologi', 'slug' => 'biologi', 'group' => 'IPA', 'icon' => '🧬', 'color' => 'teal'],
            ['name' => 'Ekonomi', 'slug' => 'ekonomi', 'group' => 'IPS', 'icon' => '💰', 'color' => 'yellow'],
            ['name' => 'Geografi', 'slug' => 'geografi', 'group' => 'IPS', 'icon' => '🌍', 'color' => 'green'],
            ['name' => 'Sosiologi', 'slug' => 'sosiologi', 'group' => 'IPS', 'icon' => '👥', 'color' => 'orange'],
            ['name' => 'Antropologi', 'slug' => 'antropologi', 'group' => 'Bahasa', 'icon' => '🗿', 'color' => 'slate'],
            ['name' => 'Prakarya dan Kewirausahaan', 'slug' => 'prakarya', 'group' => 'Keterampilan', 'icon' => '🛠️', 'color' => 'red'],
            ['name' => 'Seni Budaya', 'slug' => 'seni-budaya', 'group' => 'Seni', 'icon' => '🎭', 'color' => 'violet'],
        ],
        'smk' => [
            ['name' => 'Pendidikan Agama Islam dan Budi Pekerti', 'slug' => 'pai', 'group' => 'Wajib', 'icon' => '🕌', 'color' => 'emerald'],
            ['name' => 'Pendidikan Pancasila', 'slug' => 'pancasila', 'group' => 'Wajib', 'icon' => '🇮🇩', 'color' => 'rose'],
            ['name' => 'Bahasa Indonesia', 'slug' => 'bahasa-indonesia', 'group' => 'Wajib', 'icon' => '📖', 'color' => 'amber'],
            ['name' => 'Matematika', 'slug' => 'matematika', 'group' => 'Wajib', 'icon' => '➗', 'color' => 'blue'],
            ['name' => 'Bahasa Inggris', 'slug' => 'bahasa-inggris', 'group' => 'Wajib', 'icon' => '🔤', 'color' => 'indigo'],
            ['name' => 'Informatika', 'slug' => 'informatika', 'group' => 'Wajib', 'icon' => '💻', 'color' => 'cyan'],
            ['name' => 'PJOK', 'slug' => 'pjok', 'group' => 'Wajib', 'icon' => '⚽', 'color' => 'lime'],
            ['name' => 'Projek IPAS', 'slug' => 'ipas', 'group' => 'Wajib', 'icon' => '🔬', 'color' => 'teal'],
            ['name' => 'Pemrograman Dasar', 'slug' => 'pemrograman-dasar', 'group' => 'Kejuruan', 'icon' => '⌨️', 'color' => 'sky'],
            ['name' => 'Prakarya dan Kewirausahaan', 'slug' => 'prakarya', 'group' => 'Keterampilan', 'icon' => '🛠️', 'color' => 'red'],
            ['name' => 'Seni Budaya', 'slug' => 'seni-budaya', 'group' => 'Seni', 'icon' => '🎭', 'color' => 'violet'],
        ],
    ];

    public function run(): void
    {
        $classes = ClassRoom::with('educationLevel')->get();

        foreach ($classes as $class) {
            $levelSlug = $class->educationLevel?->slug;

            if ($levelSlug === null || ! isset($this->catalog[$levelSlug])) {
                continue;
            }

            foreach ($this->catalog[$levelSlug] as $index => $subject) {
                // Pemrograman Dasar hanya untuk SMK kelas 10.
                if ($subject['slug'] === 'pemrograman-dasar' && $class->grade_level !== 10) {
                    continue;
                }

                Subject::updateOrCreate(
                    [
                        'class_id' => $class->id,
                        'slug' => $subject['slug'],
                    ],
                    [
                        'name' => $subject['name'],
                        'group' => $subject['group'],
                        'icon' => $subject['icon'],
                        'color' => $subject['color'],
                        'order' => $index + 1,
                        'is_active' => true,
                    ],
                );
            }
        }
    }
}
