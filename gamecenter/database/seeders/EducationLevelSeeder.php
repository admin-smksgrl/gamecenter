<?php

namespace Database\Seeders;

use App\Models\EducationLevel;
use Illuminate\Database\Seeder;

class EducationLevelSeeder extends Seeder
{
    public function run(): void
    {
        $levels = [
            [
                'name' => 'PAUD',
                'slug' => 'paud',
                'short_name' => 'PAUD',
                'description' => 'Pendidikan Anak Usia Dini (3–4 tahun)',
                'theme' => 'default',
                'icon' => '🧸',
                'order' => 1,
            ],
            [
                'name' => 'TK',
                'slug' => 'tk',
                'short_name' => 'TK',
                'description' => 'Taman Kanak-Kanak (4–6 tahun)',
                'theme' => 'default',
                'icon' => '🎨',
                'order' => 2,
            ],
            [
                'name' => 'SD-MI',
                'slug' => 'sd',
                'short_name' => 'SD',
                'description' => 'Sekolah Dasar / Madrasah Ibtidaiyah (Fase A–C)',
                'theme' => 'default',
                'icon' => '✏️',
                'order' => 3,
            ],
            [
                'name' => 'SMP-MTs',
                'slug' => 'smp',
                'short_name' => 'SMP',
                'description' => 'Sekolah Menengah Pertama / Madrasah Tsanawiyah (Fase D)',
                'theme' => 'default',
                'icon' => '🚀',
                'order' => 4,
            ],
            [
                'name' => 'SMA',
                'slug' => 'sma',
                'short_name' => 'SMA',
                'description' => 'Sekolah Menengah Atas (Fase E–F)',
                'theme' => 'default',
                'icon' => '🎓',
                'order' => 5,
            ],
            [
                'name' => 'SMK',
                'slug' => 'smk',
                'short_name' => 'SMK',
                'description' => 'Sekolah Menengah Kejuruan (Fase E–F)',
                'theme' => 'default',
                'icon' => '🛠️',
                'order' => 6,
            ],
        ];

        foreach ($levels as $level) {
            EducationLevel::updateOrCreate(['slug' => $level['slug']], $level);
        }
    }
}
