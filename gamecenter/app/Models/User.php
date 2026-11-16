<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use App\Enums\MembershipStatus;
use App\Enums\UserRole;
use Database\Factories\UserFactory;
use Filament\Models\Contracts\FilamentUser;
use Filament\Panel;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Attributes\Hidden;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;

#[Fillable([
    'name', 'username', 'email', 'password', 'role', 'class_id', 'avatar',
    'xp', 'level', 'coins', 'streak_days', 'last_played_at', 'is_active',
])]
#[Hidden(['password', 'remember_token'])]
class User extends Authenticatable implements FilamentUser
{
    /** @use HasFactory<UserFactory> */
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * Level thresholds: level => minimum XP.
     *
     * @var array<int, int>
     */
    public const LEVEL_THRESHOLDS = [
        1 => 0,
        2 => 100,
        3 => 250,
        4 => 500,
        5 => 1000,
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
            'role' => UserRole::class,
            'xp' => 'integer',
            'level' => 'integer',
            'coins' => 'integer',
            'streak_days' => 'integer',
            'is_active' => 'boolean',
            'last_played_at' => 'datetime',
        ];
    }

    public function classRoom(): BelongsTo
    {
        return $this->belongsTo(ClassRoom::class, 'class_id');
    }

    public function gameSessions(): HasMany
    {
        return $this->hasMany(GameSession::class);
    }

    public function progress(): HasMany
    {
        return $this->hasMany(UserProgress::class);
    }

    public function achievements(): BelongsToMany
    {
        return $this->belongsToMany(Achievement::class, 'user_achievements')
            ->withPivot('unlocked_at')
            ->withTimestamps();
    }

    public function syncQueue(): HasMany
    {
        return $this->hasMany(SyncQueue::class);
    }

    public function latestSession(): HasOne
    {
        return $this->hasOne(GameSession::class)->latestOfMany('completed_at');
    }

    public function memberships(): HasMany
    {
        return $this->hasMany(Membership::class);
    }

    public function activeMembership(): HasOne
    {
        return $this->hasOne(Membership::class)->ofMany(
            ['id' => 'max'],
            fn (Builder $query) => $query
                ->where('status', MembershipStatus::Active)
                ->where('ends_at', '>', now()),
        );
    }

    /**
     * Ringkasan paket aktif; user tanpa membership dianggap paket gratis.
     *
     * @return array<string, mixed>
     */
    public function membershipSummary(): array
    {
        $membership = $this->activeMembership;
        $plan = $membership?->plan
            ?? MembershipPlan::query()->where('slug', 'free')->first();

        return [
            'plan_slug' => $plan?->slug,
            'plan_name' => $plan?->name ?? 'Gratis',
            'tier' => $plan?->tier ?? 'free',
            'status' => $membership ? 'active' : 'free',
            'ends_at' => $membership?->ends_at?->toIso8601String(),
        ];
    }

    public function isAdmin(): bool
    {
        return $this->role === UserRole::Admin;
    }

    public function isTeacher(): bool
    {
        return $this->role === UserRole::Teacher;
    }

    public function isStudent(): bool
    {
        return $this->role === UserRole::Student;
    }

    /**
     * Hanya admin & guru yang boleh masuk panel Filament.
     */
    public function canAccessPanel(Panel $panel): bool
    {
        return $this->is_active && in_array($this->role, [UserRole::Admin, UserRole::Teacher], true);
    }

    /**
     * XP dibutuhkan untuk naik level berikutnya.
     */
    public function xpToNextLevel(): ?int
    {
        $next = self::LEVEL_THRESHOLDS[$this->level + 1] ?? null;

        return $next === null ? null : max(0, $next - $this->xp);
    }

    /**
     * Level berdasarkan total XP.
     */
    public static function levelForXp(int $xp): int
    {
        $level = 1;

        foreach (self::LEVEL_THRESHOLDS as $candidate => $threshold) {
            if ($xp >= $threshold) {
                $level = $candidate;
            }
        }

        return $level;
    }

    public function scopeStudents(Builder $query): Builder
    {
        return $query->where('role', UserRole::Student);
    }

    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', true);
    }
}
