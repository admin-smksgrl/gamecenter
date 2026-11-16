<?php

namespace Database\Seeders;

use App\Enums\BillingCycle;
use App\Enums\MembershipStatus;
use App\Models\Membership;
use App\Models\MembershipPlan;
use App\Models\User;
use Illuminate\Database\Seeder;

class MembershipSeeder extends Seeder
{
    public function run(): void
    {
        $student = User::query()->where('username', 'siswa')->first();
        $teacher = User::query()->where('username', 'guru')->first();
        $admin = User::query()->where('username', 'admin')->first();

        $standard = MembershipPlan::query()->where('slug', 'standard')->first();
        $professional = MembershipPlan::query()->where('slug', 'professional')->first();

        if ($student && $standard) {
            Membership::firstOrCreate(
                [
                    'user_id' => $student->id,
                    'membership_plan_id' => $standard->id,
                    'status' => MembershipStatus::Active->value,
                ],
                [
                    'reference' => Membership::generateReference(),
                    'billing_cycle' => BillingCycle::Monthly->value,
                    'amount' => $standard->price_monthly,
                    'payment_method' => 'bank_transfer',
                    'starts_at' => now(),
                    'ends_at' => now()->addMonth(),
                    'approved_at' => now(),
                    'approved_by' => $admin?->id,
                    'admin_note' => 'Data demo: paket aktif hasil persetujuan admin.',
                ],
            );
        }

        if ($teacher && $professional) {
            Membership::firstOrCreate(
                [
                    'user_id' => $teacher->id,
                    'membership_plan_id' => $professional->id,
                    'status' => MembershipStatus::Pending->value,
                ],
                [
                    'reference' => Membership::generateReference(),
                    'billing_cycle' => BillingCycle::Monthly->value,
                    'amount' => $professional->price_monthly,
                    'payment_method' => 'bank_transfer',
                    'note' => 'Data demo: pengajuan upgrade untuk antrean admin.',
                ],
            );
        }
    }
}
