<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;

    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        $this->call([
            EducationLevelSeeder::class,
            ClassSeeder::class,
            SubjectSeeder::class,
            AchievementSeeder::class,
            CuratedContentSeeder::class,
            SmaSmkMaterialSeeder::class,
            UserSeeder::class,
            MembershipPlanSeeder::class,
            MembershipSeeder::class,
        ]);
    }
}
