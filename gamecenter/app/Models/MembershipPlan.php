<?php

namespace App\Models;

use App\Enums\BillingCycle;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable([
    'slug', 'name', 'tier', 'tagline', 'description', 'price_monthly',
    'price_yearly', 'features', 'limits', 'is_featured', 'is_active', 'sort_order',
])]
class MembershipPlan extends Model
{
    public const TIER_RANK = [
        'free' => 0,
        'standard' => 1,
        'professional' => 2,
        'enterprise' => 3,
    ];

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'price_monthly' => 'integer',
            'price_yearly' => 'integer',
            'features' => 'array',
            'limits' => 'array',
            'is_featured' => 'boolean',
            'is_active' => 'boolean',
            'sort_order' => 'integer',
        ];
    }

    public function memberships(): HasMany
    {
        return $this->hasMany(Membership::class);
    }

    public function priceFor(BillingCycle $cycle): int
    {
        return $cycle === BillingCycle::Yearly
            ? $this->price_yearly
            : $this->price_monthly;
    }

    public function rank(): int
    {
        return self::TIER_RANK[$this->tier] ?? 0;
    }

    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', true);
    }

    public function scopeOrdered(Builder $query): Builder
    {
        return $query->orderBy('sort_order')->orderBy('price_monthly');
    }
}
