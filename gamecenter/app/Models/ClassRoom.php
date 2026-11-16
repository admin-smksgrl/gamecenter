<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable([
    'education_level_id', 'name', 'slug', 'grade_level', 'phase', 'order', 'is_active',
])]
class ClassRoom extends Model
{
    use HasFactory;

    protected $table = 'classes';

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'grade_level' => 'integer',
            'order' => 'integer',
            'is_active' => 'boolean',
        ];
    }

    public function educationLevel(): BelongsTo
    {
        return $this->belongsTo(EducationLevel::class);
    }

    public function subjects(): HasMany
    {
        return $this->hasMany(Subject::class, 'class_id')->orderBy('order');
    }

    public function users(): HasMany
    {
        return $this->hasMany(User::class, 'class_id');
    }

    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', true);
    }
}
