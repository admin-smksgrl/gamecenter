<?php

namespace Tests\Feature;

use App\Enums\BillingCycle;
use App\Enums\MembershipStatus;
use App\Models\Membership;
use App\Models\MembershipPlan;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia as Assert;
use Tests\TestCase;

class MembershipTest extends TestCase
{
    use RefreshDatabase;

    public function test_guest_can_browse_membership_plans(): void
    {
        $this->createPlan('free');
        $this->createPlan('standard');
        $this->createPlan('professional');

        $this->get('/keanggotaan')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Membership/Index')
                ->has('plans', 3)
                ->where('current', null)
                ->where('pending', null)
                ->has('history', 0));
    }

    public function test_guest_is_redirected_to_login_when_requesting_an_upgrade(): void
    {
        $plan = $this->createPlan('standard');

        $this->post('/keanggotaan/ajukan', [
            'plan_id' => $plan->id,
            'billing_cycle' => 'monthly',
        ])->assertRedirect('/masuk');
    }

    public function test_student_can_request_a_paid_upgrade_with_price_snapshot(): void
    {
        $student = User::factory()->create();
        $plan = $this->createPlan('standard');

        $this->actingAs($student)
            ->post('/keanggotaan/ajukan', [
                'plan_id' => $plan->id,
                'billing_cycle' => 'yearly',
                'note' => 'Transfer BCA',
            ])
            ->assertRedirect('/keanggotaan')
            ->assertSessionHas('success');

        $membership = Membership::query()->firstOrFail();

        $this->assertSame($student->id, $membership->user_id);
        $this->assertSame($plan->id, $membership->membership_plan_id);
        $this->assertSame(MembershipStatus::Pending, $membership->status);
        $this->assertSame(BillingCycle::Yearly, $membership->billing_cycle);
        $this->assertSame(290000, $membership->amount);
        $this->assertStringStartsWith('GC-', $membership->reference);
        $this->assertSame('Transfer BCA', $membership->note);
    }

    public function test_free_plan_cannot_be_requested(): void
    {
        $student = User::factory()->create();
        $free = $this->createPlan('free');

        $this->actingAs($student)
            ->post('/keanggotaan/ajukan', [
                'plan_id' => $free->id,
                'billing_cycle' => 'monthly',
            ])
            ->assertSessionHasErrors('plan_id');

        $this->assertSame(0, Membership::query()->count());
    }

    public function test_duplicate_pending_request_is_rejected(): void
    {
        $student = User::factory()->create();
        $standard = $this->createPlan('standard');
        $professional = $this->createPlan('professional');

        Membership::create([
            'user_id' => $student->id,
            'membership_plan_id' => $standard->id,
            'status' => MembershipStatus::Pending,
            'billing_cycle' => BillingCycle::Monthly,
            'amount' => $standard->price_monthly,
            'payment_method' => 'bank_transfer',
        ]);

        $this->actingAs($student)
            ->post('/keanggotaan/ajukan', [
                'plan_id' => $professional->id,
                'billing_cycle' => 'monthly',
            ])
            ->assertSessionHasErrors('plan_id');

        $this->assertSame(
            1,
            Membership::query()->where('user_id', $student->id)->count(),
        );
    }

    public function test_requested_plan_must_be_higher_than_current_membership(): void
    {
        $student = User::factory()->create();
        $admin = User::factory()->admin()->create();
        $standard = $this->createPlan('standard');
        $professional = $this->createPlan('professional');

        $this->activateMembership($student, $standard, $admin);

        $this->actingAs($student)
            ->post('/keanggotaan/ajukan', [
                'plan_id' => $standard->id,
                'billing_cycle' => 'monthly',
            ])
            ->assertSessionHasErrors('plan_id');

        $this->actingAs($student)
            ->post('/keanggotaan/ajukan', [
                'plan_id' => $professional->id,
                'billing_cycle' => 'monthly',
            ])
            ->assertSessionHasNoErrors()
            ->assertRedirect('/keanggotaan');
    }

    public function test_admin_approval_activates_membership_and_expires_previous_plan(): void
    {
        $student = User::factory()->create();
        $admin = User::factory()->admin()->create();
        $standard = $this->createPlan('standard');
        $professional = $this->createPlan('professional');

        $previous = $this->activateMembership($student, $standard, $admin);

        $pending = Membership::create([
            'user_id' => $student->id,
            'membership_plan_id' => $professional->id,
            'status' => MembershipStatus::Pending,
            'billing_cycle' => BillingCycle::Monthly,
            'amount' => $professional->price_monthly,
            'payment_method' => 'bank_transfer',
        ]);

        $pending->approve($admin, 'Pembayaran terverifikasi');

        $this->assertSame(
            MembershipStatus::Expired,
            $previous->fresh()->status,
        );

        $pending->refresh();

        $this->assertSame(MembershipStatus::Active, $pending->status);
        $this->assertSame($admin->id, $pending->approved_by);
        $this->assertSame('Pembayaran terverifikasi', $pending->admin_note);
        $this->assertNotNull($pending->starts_at);
        $this->assertTrue($pending->ends_at->greaterThan(now()->addDays(27)));
    }

    public function test_admin_can_reject_a_request(): void
    {
        $student = User::factory()->create();
        $admin = User::factory()->admin()->create();
        $standard = $this->createPlan('standard');

        $pending = Membership::create([
            'user_id' => $student->id,
            'membership_plan_id' => $standard->id,
            'status' => MembershipStatus::Pending,
            'billing_cycle' => BillingCycle::Monthly,
            'amount' => $standard->price_monthly,
            'payment_method' => 'bank_transfer',
        ]);

        $pending->reject($admin, 'Bukti transfer tidak cocok');

        $pending->refresh();

        $this->assertSame(MembershipStatus::Rejected, $pending->status);
        $this->assertSame($admin->id, $pending->approved_by);
        $this->assertSame('Bukti transfer tidak cocok', $pending->admin_note);
    }

    public function test_active_membership_is_shared_with_inertia_pages(): void
    {
        $student = User::factory()->create();
        $admin = User::factory()->admin()->create();
        $standard = $this->createPlan('standard');

        $this->activateMembership($student, $standard, $admin);

        $this->actingAs($student)
            ->get('/keanggotaan')
            ->assertInertia(fn (Assert $page) => $page
                ->where('auth.user.membership.plan_slug', 'standard')
                ->where('auth.user.membership.tier', 'standard')
                ->where('auth.user.membership.status', 'active'));
    }

    private function createPlan(string $tier): MembershipPlan
    {
        $prices = [
            'free' => [0, 0],
            'standard' => [29000, 290000],
            'professional' => [99000, 990000],
            'enterprise' => [499000, 4990000],
        ];

        [$monthly, $yearly] = $prices[$tier];

        return MembershipPlan::create([
            'slug' => $tier,
            'name' => ucfirst($tier),
            'tier' => $tier,
            'tagline' => "Paket {$tier}",
            'description' => "Paket {$tier} untuk anggota.",
            'price_monthly' => $monthly,
            'price_yearly' => $yearly,
            'features' => ['Fitur dasar'],
            'limits' => ['max_group_players' => 2],
            'is_featured' => $tier === 'professional',
            'is_active' => true,
            'sort_order' => MembershipPlan::TIER_RANK[$tier] ?? 0,
        ]);
    }

    private function activateMembership(
        User $student,
        MembershipPlan $plan,
        User $admin,
    ): Membership {
        $membership = Membership::create([
            'user_id' => $student->id,
            'membership_plan_id' => $plan->id,
            'status' => MembershipStatus::Pending,
            'billing_cycle' => BillingCycle::Monthly,
            'amount' => $plan->price_monthly,
            'payment_method' => 'bank_transfer',
        ]);

        $membership->approve($admin);

        return $membership;
    }
}
