<?php

namespace Database\Seeders;

use App\Models\Achievement;
use Illuminate\Database\Seeder;

class AchievementSeeder extends Seeder
{
    public function run(): void
    {
        $achievements = [
            [
                'slug' => 'first-step',
                'title' => 'Langkah Pertama',
                'description' => 'Menyelesaikan sesi permainan pertamamu.',
                'icon' => '🌱',
                'category' => 'completion',
                'requirement_type' => 'sessions_completed',
                'requirement_value' => 1,
                'xp_reward' => 20,
                'coin_reward' => 10,
                'order' => 1,
            ],
            [
                'slug' => 'perfect-score',
                'title' => 'Sempurna!',
                'description' => 'Mendapatkan nilai 100 dalam satu sesi.',
                'icon' => '🏆',
                'category' => 'score',
                'requirement_type' => 'perfect_score',
                'requirement_value' => 1,
                'xp_reward' => 50,
                'coin_reward' => 25,
                'order' => 2,
            ],
            [
                'slug' => 'streak-3',
                'title' => 'Pemanasan',
                'description' => 'Menjawab benar 3 soal berturut-turut.',
                'icon' => '🔥',
                'category' => 'streak',
                'requirement_type' => 'answer_streak',
                'requirement_value' => 3,
                'xp_reward' => 15,
                'coin_reward' => 5,
                'order' => 3,
            ],
            [
                'slug' => 'streak-10',
                'title' => 'Tak Terbendung',
                'description' => 'Menjawab benar 10 soal berturut-turut.',
                'icon' => '⚡',
                'category' => 'streak',
                'requirement_type' => 'answer_streak',
                'requirement_value' => 10,
                'xp_reward' => 60,
                'coin_reward' => 30,
                'order' => 4,
            ],
            [
                'slug' => 'chapter-master',
                'title' => 'Penakluk Bab',
                'description' => 'Menyelesaikan semua tingkat kesulitan dalam satu bab.',
                'icon' => '📚',
                'category' => 'completion',
                'requirement_type' => 'chapter_all_difficulties',
                'requirement_value' => 3,
                'xp_reward' => 80,
                'coin_reward' => 40,
                'order' => 5,
            ],
            [
                'slug' => 'math-genius',
                'title' => 'Jenius Matematika',
                'description' => 'Mendapatkan nilai sempurna pada mode sulit Matematika.',
                'icon' => '🧮',
                'category' => 'score',
                'requirement_type' => 'perfect_hard_math',
                'requirement_value' => 1,
                'xp_reward' => 100,
                'coin_reward' => 50,
                'order' => 6,
            ],
            [
                'slug' => 'case-master',
                'title' => 'Ahli Studi Kasus',
                'description' => 'Menyelesaikan studi kasus SMA/SMK dengan nilai di atas 80.',
                'icon' => '🧠',
                'category' => 'score',
                'requirement_type' => 'simulation_above_80',
                'requirement_value' => 80,
                'xp_reward' => 100,
                'coin_reward' => 60,
                'order' => 7,
            ],
            [
                'slug' => 'bookworm',
                'title' => 'Kutu Buku',
                'description' => 'Membaca 10 materi pembelajaran.',
                'icon' => '📖',
                'category' => 'completion',
                'requirement_type' => 'materials_read',
                'requirement_value' => 10,
                'xp_reward' => 40,
                'coin_reward' => 20,
                'order' => 8,
            ],
        ];

        foreach ($achievements as $achievement) {
            Achievement::updateOrCreate(['slug' => $achievement['slug']], $achievement);
        }
    }
}
