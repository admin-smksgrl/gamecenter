<?php

namespace Database\Seeders;

use App\Enums\UserRole;
use App\Models\ClassRoom;
use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    public function run(): void
    {
        $smaKelas10 = ClassRoom::query()
            ->where('slug', 'kelas-10')
            ->whereHas('educationLevel', fn ($query) => $query->where('slug', 'sma'))
            ->first();

        $smkKelas10 = ClassRoom::query()
            ->where('slug', 'kelas-10')
            ->whereHas('educationLevel', fn ($query) => $query->where('slug', 'smk'))
            ->first();

        User::updateOrCreate(
            ['username' => 'admin'],
            [
                'name' => 'Administrator',
                'email' => 'admin@gamecenter.test',
                'password' => Hash::make('password'),
                'role' => UserRole::Admin,
                'class_id' => null,
                'is_active' => true,
                'email_verified_at' => now(),
            ],
        );

        User::updateOrCreate(
            ['username' => 'guru'],
            [
                'name' => 'Bu Sari (Guru)',
                'email' => 'guru@gamecenter.test',
                'password' => Hash::make('password'),
                'role' => UserRole::Teacher,
                'class_id' => null,
                'is_active' => true,
                'email_verified_at' => now(),
            ],
        );

        User::updateOrCreate(
            ['username' => 'siswa'],
            [
                'name' => 'Budi Santoso',
                'email' => 'siswa@gamecenter.test',
                'password' => Hash::make('password'),
                'role' => UserRole::Student,
                'class_id' => $smaKelas10?->id,
                'xp' => 120,
                'level' => 2,
                'coins' => 45,
                'streak_days' => 3,
                'is_active' => true,
                'email_verified_at' => now(),
            ],
        );

        User::updateOrCreate(
            ['username' => 'siswa-smk'],
            [
                'name' => 'Rina Wulandari',
                'email' => 'smk@gamecenter.test',
                'password' => Hash::make('password'),
                'role' => UserRole::Student,
                'class_id' => $smkKelas10?->id,
                'xp' => 40,
                'level' => 1,
                'coins' => 10,
                'streak_days' => 1,
                'is_active' => true,
                'email_verified_at' => now(),
            ],
        );
    }
}
