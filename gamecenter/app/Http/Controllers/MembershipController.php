<?php

namespace App\Http\Controllers;

use App\Enums\BillingCycle;
use App\Enums\MembershipStatus;
use App\Http\Requests\StoreMembershipRequest;
use App\Models\Membership;
use App\Models\MembershipPlan;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\ValidationException;
use Inertia\Inertia;
use Inertia\Response;

class MembershipController extends Controller
{
    public function index(Request $request): Response
    {
        $user = $request->user();

        $plans = MembershipPlan::query()
            ->active()
            ->ordered()
            ->get()
            ->map(fn (MembershipPlan $plan) => [
                'id' => $plan->id,
                'slug' => $plan->slug,
                'name' => $plan->name,
                'tier' => $plan->tier,
                'tagline' => $plan->tagline,
                'price_monthly' => $plan->price_monthly,
                'price_yearly' => $plan->price_yearly,
                'features' => $plan->features ?? [],
                'is_featured' => $plan->is_featured,
            ]);

        $pending = $user
            ? $user->memberships()->with('plan')->pending()->latest('id')->first()
            : null;

        $history = $user
            ? $user->memberships()
                ->with('plan')
                ->whereIn('status', [
                    MembershipStatus::Active->value,
                    MembershipStatus::Expired->value,
                    MembershipStatus::Rejected->value,
                ])
                ->latest('id')
                ->limit(12)
                ->get()
            : collect();

        return Inertia::render('Membership/Index', [
            'plans' => $plans->values(),
            'current' => $user?->membershipSummary(),
            'pending' => $pending ? $this->record($pending) : null,
            'history' => $history
                ->map(fn (Membership $membership) => $this->record($membership))
                ->values(),
            'bank' => config('membership.bank'),
        ]);
    }

    public function store(StoreMembershipRequest $request): RedirectResponse
    {
        $user = $request->user();
        $data = $request->validated();
        $cycle = BillingCycle::from($data['billing_cycle']);

        $plan = MembershipPlan::query()->active()->find($data['plan_id']);

        if (! $plan) {
            throw ValidationException::withMessages([
                'plan_id' => 'Paket tersebut tidak tersedia.',
            ]);
        }

        if ($plan->tier === 'free' || $plan->priceFor($cycle) <= 0) {
            throw ValidationException::withMessages([
                'plan_id' => 'Paket gratis otomatis aktif untuk semua akun.',
            ]);
        }

        $active = $user->activeMembership()->with('plan')->first();
        $currentRank = $active?->plan
            ? $active->plan->rank()
            : MembershipPlan::TIER_RANK['free'];

        if ($plan->rank() <= $currentRank) {
            throw ValidationException::withMessages([
                'plan_id' => 'Paket ini setara atau lebih rendah dari paket aktifmu.',
            ]);
        }

        if ($user->memberships()->pending()->exists()) {
            throw ValidationException::withMessages([
                'plan_id' => 'Masih ada pengajuan yang menunggu verifikasi admin.',
            ]);
        }

        $membership = Membership::create([
            'user_id' => $user->id,
            'membership_plan_id' => $plan->id,
            'status' => MembershipStatus::Pending,
            'billing_cycle' => $cycle,
            'amount' => $plan->priceFor($cycle),
            'payment_method' => 'bank_transfer',
            'note' => $data['note'] ?? null,
        ]);

        return redirect()
            ->route('membership.index')
            ->with('success', "Pengajuan paket {$plan->name} diterima. Kode referensi: {$membership->reference}.");
    }

    /**
     * @return array<string, mixed>
     */
    private function record(Membership $membership): array
    {
        return [
            'id' => $membership->id,
            'plan_name' => $membership->plan?->name,
            'plan_slug' => $membership->plan?->slug,
            'tier' => $membership->plan?->tier,
            'billing_cycle' => $membership->billing_cycle->value,
            'amount' => $membership->amount,
            'status' => $membership->status->value,
            'status_label' => $membership->status->label(),
            'reference' => $membership->reference,
            'note' => $membership->note,
            'admin_note' => $membership->admin_note,
            'created_at' => $membership->created_at?->toIso8601String(),
            'starts_at' => $membership->starts_at?->toIso8601String(),
            'ends_at' => $membership->ends_at?->toIso8601String(),
        ];
    }
}
