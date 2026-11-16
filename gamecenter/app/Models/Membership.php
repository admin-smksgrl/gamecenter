<?php

namespace App\Models;

use App\Enums\BillingCycle;
use App\Enums\MembershipStatus;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

#[Fillable([
    'user_id', 'membership_plan_id', 'status', 'billing_cycle', 'amount',
    'payment_method', 'note',
])]
class Membership extends Model
{
    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'status' => MembershipStatus::class,
            'billing_cycle' => BillingCycle::class,
            'amount' => 'integer',
            'starts_at' => 'datetime',
            'ends_at' => 'datetime',
            'approved_at' => 'datetime',
        ];
    }

    protected static function booted(): void
    {
        static::creating(function (self $membership) {
            if (blank($membership->reference)) {
                $membership->reference = self::generateReference();
            }
        });
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function plan(): BelongsTo
    {
        return $this->belongsTo(MembershipPlan::class, 'membership_plan_id');
    }

    public function approvedBy(): BelongsTo
    {
        return $this->belongsTo(User::class, 'approved_by');
    }

    public function scopePending(Builder $query): Builder
    {
        return $query->where('status', MembershipStatus::Pending);
    }

    public function scopeActive(Builder $query): Builder
    {
        return $query
            ->where('status', MembershipStatus::Active)
            ->where('ends_at', '>', now());
    }

    /**
     * Aktifkan pengajuan dan kedaluwarsakan paket aktif sebelumnya.
     */
    public function approve(User $admin, ?string $note = null): void
    {
        DB::transaction(function () use ($admin, $note): void {
            $startedAt = now();

            static::query()
                ->where('user_id', $this->user_id)
                ->whereKeyNot($this->getKey())
                ->where('status', MembershipStatus::Active)
                ->update([
                    'status' => MembershipStatus::Expired,
                    'updated_at' => now(),
                ]);

            $this->forceFill([
                'status' => MembershipStatus::Active,
                'starts_at' => $startedAt,
                'ends_at' => $startedAt->copy()->addMonths($this->billing_cycle->months()),
                'approved_at' => $startedAt,
                'approved_by' => $admin->getKey(),
                'admin_note' => $note,
            ])->save();
        });
    }

    public function reject(User $admin, string $note): void
    {
        $this->forceFill([
            'status' => MembershipStatus::Rejected,
            'approved_at' => now(),
            'approved_by' => $admin->getKey(),
            'admin_note' => $note,
        ])->save();
    }

    public static function generateReference(): string
    {
        do {
            $reference = 'GC-'.Str::upper(Str::random(6));
        } while (static::query()->where('reference', $reference)->exists());

        return $reference;
    }
}
