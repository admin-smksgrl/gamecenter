<?php

namespace Tests\Concerns;

use Database\Seeders\AchievementSeeder;
use Database\Seeders\ClassSeeder;
use Database\Seeders\CuratedContentSeeder;
use Database\Seeders\DemoContentSeeder;
use Database\Seeders\EducationLevelSeeder;
use Database\Seeders\MembershipPlanSeeder;
use Database\Seeders\MembershipSeeder;
use Database\Seeders\SubjectSeeder;
use Database\Seeders\UserSeeder;

/**
 * Menyemai data contoh (demo) tanpa materi kurikulum SMA/SMK.
 *
 * Tes mesin game memeriksa isi demo secara spesifik ("Eksponen" punya 8 soal
 * sedang, ada tipe matching/puzzle/simulation, dua soal uraian, dan
 * seterusnya). Materi SMA/SMK yang sesungguhnya menggantikan chapter demo
 * tersebut, sehingga tes itu harus menyemai data demo saja — kalau tidak,
 * asersinya berubah setiap kali isi kurikulum diperbarui.
 */
trait SeedsDemoContent
{
    protected function seedDemoContent(): void
    {
        $this->seed([
            EducationLevelSeeder::class,
            ClassSeeder::class,
            SubjectSeeder::class,
            AchievementSeeder::class,
            DemoContentSeeder::class,
            CuratedContentSeeder::class,
            UserSeeder::class,
            MembershipPlanSeeder::class,
            MembershipSeeder::class,
        ]);
    }
}
