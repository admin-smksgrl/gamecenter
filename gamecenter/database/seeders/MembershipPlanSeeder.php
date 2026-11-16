<?php

namespace Database\Seeders;

use App\Models\MembershipPlan;
use Illuminate\Database\Seeder;

class MembershipPlanSeeder extends Seeder
{
    public function run(): void
    {
        $plans = [
            [
                'slug' => 'free',
                'name' => 'Gratis',
                'tier' => 'free',
                'tagline' => 'Untuk mencoba dan bermain setiap hari',
                'price_monthly' => 0,
                'price_yearly' => 0,
                'features' => [
                    'Akses seluruh katalog materi PAUD–SMK',
                    'Main pribadi & kelompok (maks. 8 pemain)',
                    'XP, koin, dan pencapaian',
                    'Progres tersimpan di perangkat',
                ],
                'limits' => [
                    'group_players' => 8,
                    'saved_history' => false,
                ],
                'is_featured' => false,
                'sort_order' => 1,
            ],
            [
                'slug' => 'standard',
                'name' => 'Standard',
                'tier' => 'standard',
                'tagline' => 'Untuk pelajar yang ingin progres tercatat',
                'price_monthly' => 29000,
                'price_yearly' => 290000,
                'features' => [
                    'Semua fitur Gratis',
                    'Badge anggota Standard di profil',
                    'Riwayat hasil & progres tersimpan di akun (segera)',
                    'Akses konten baru lebih awal',
                    'Dukungan via email',
                ],
                'limits' => [
                    'group_players' => 8,
                    'saved_history' => true,
                ],
                'is_featured' => false,
                'sort_order' => 2,
            ],
            [
                'slug' => 'professional',
                'name' => 'Professional',
                'tier' => 'professional',
                'tagline' => 'Untuk guru dan kelas aktif',
                'price_monthly' => 99000,
                'price_yearly' => 990000,
                'features' => [
                    'Semua fitur Standard',
                    'Ruang guru: penugasan & bank soal (segera)',
                    'Laporan perkembangan hingga 40 siswa (segera)',
                    'Undangan kelas dengan kode (segera)',
                ],
                'limits' => [
                    'group_players' => 8,
                    'students' => 40,
                    'teacher_tools' => true,
                ],
                'is_featured' => true,
                'sort_order' => 3,
            ],
            [
                'slug' => 'enterprise',
                'name' => 'Enterprise',
                'tier' => 'enterprise',
                'tagline' => 'Untuk sekolah dan lembaga',
                'price_monthly' => 499000,
                'price_yearly' => 4990000,
                'features' => [
                    'Semua fitur Professional',
                    'Multi-guru & multi-kelas (segera)',
                    'Dashboard & ekspor laporan sekolah (segera)',
                    'Dukungan prioritas',
                    'Penyesuaian kurikulum internal',
                ],
                'limits' => [
                    'group_players' => 8,
                    'students' => 1000,
                    'teacher_tools' => true,
                    'multi_teacher' => true,
                ],
                'is_featured' => false,
                'sort_order' => 4,
            ],
        ];

        foreach ($plans as $plan) {
            MembershipPlan::updateOrCreate(
                ['slug' => $plan['slug']],
                [...$plan, 'is_active' => true],
            );
        }
    }
}
