<?php

namespace Database\Seeders;

use App\Models\ClassRoom;
use App\Models\EducationLevel;
use Illuminate\Database\Seeder;

class ClassSeeder extends Seeder
{
    /**
     * Struktur kelas per jenjang mengikuti Kurikulum Merdeka.
     *
     * @var array<string, array{suffixes: array<int, array{name: string, slug: string, grade: int, phase: ?string}>, start_order: int}>
     */
    private array $structure = [
        'paud' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'Kelompok Bermain', 'slug' => 'kb', 'grade' => 0, 'phase' => null],
            ],
        ],
        'tk' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'TK A', 'slug' => 'tk-a', 'grade' => 0, 'phase' => null],
                ['name' => 'TK B', 'slug' => 'tk-b', 'grade' => 0, 'phase' => null],
            ],
        ],
        'sd' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'Kelas 1', 'slug' => 'kelas-1', 'grade' => 1, 'phase' => 'A'],
                ['name' => 'Kelas 2', 'slug' => 'kelas-2', 'grade' => 2, 'phase' => 'A'],
                ['name' => 'Kelas 3', 'slug' => 'kelas-3', 'grade' => 3, 'phase' => 'B'],
                ['name' => 'Kelas 4', 'slug' => 'kelas-4', 'grade' => 4, 'phase' => 'B'],
                ['name' => 'Kelas 5', 'slug' => 'kelas-5', 'grade' => 5, 'phase' => 'C'],
                ['name' => 'Kelas 6', 'slug' => 'kelas-6', 'grade' => 6, 'phase' => 'C'],
            ],
        ],
        'smp' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'Kelas 7', 'slug' => 'kelas-7', 'grade' => 7, 'phase' => 'D'],
                ['name' => 'Kelas 8', 'slug' => 'kelas-8', 'grade' => 8, 'phase' => 'D'],
                ['name' => 'Kelas 9', 'slug' => 'kelas-9', 'grade' => 9, 'phase' => 'D'],
            ],
        ],
        'sma' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'Kelas 10', 'slug' => 'kelas-10', 'grade' => 10, 'phase' => 'E'],
                ['name' => 'Kelas 11', 'slug' => 'kelas-11', 'grade' => 11, 'phase' => 'F'],
                ['name' => 'Kelas 12', 'slug' => 'kelas-12', 'grade' => 12, 'phase' => 'F'],
            ],
        ],
        'smk' => [
            'start_order' => 1,
            'suffixes' => [
                ['name' => 'Kelas 10', 'slug' => 'kelas-10', 'grade' => 10, 'phase' => 'E'],
                ['name' => 'Kelas 11', 'slug' => 'kelas-11', 'grade' => 11, 'phase' => 'F'],
                ['name' => 'Kelas 12', 'slug' => 'kelas-12', 'grade' => 12, 'phase' => 'F'],
            ],
        ],
    ];

    public function run(): void
    {
        $levels = EducationLevel::all()->keyBy('slug');

        foreach ($this->structure as $levelSlug => $config) {
            $level = $levels->get($levelSlug);

            if ($level === null) {
                continue;
            }

            foreach ($config['suffixes'] as $index => $class) {
                ClassRoom::updateOrCreate(
                    [
                        'education_level_id' => $level->id,
                        'slug' => $class['slug'],
                    ],
                    [
                        'name' => $class['name'],
                        'grade_level' => $class['grade'],
                        'phase' => $class['phase'],
                        'order' => $config['start_order'] + $index,
                        'is_active' => true,
                    ],
                );
            }
        }
    }
}
