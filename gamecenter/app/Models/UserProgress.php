<?php

namespace App\Models;

use App\Enums\ProgressStatus;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable([
    'user_id', 'chapter_id', 'status', 'progress_percentage', 'total_time_spent',
    'best_score', 'materials_read', 'attempts', 'last_accessed_at', 'completed_at',
])]
class UserProgress extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'status' => ProgressStatus::class,
            'progress_percentage' => 'integer',
            'total_time_spent' => 'integer',
            'best_score' => 'integer',
            'materials_read' => 'integer',
            'attempts' => 'integer',
            'last_accessed_at' => 'datetime',
            'completed_at' => 'datetime',
        ];
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function chapter(): BelongsTo
    {
        return $this->belongsTo(Chapter::class);
    }

    public function scopeCompleted(Builder $query): Builder
    {
        return $query->where('status', ProgressStatus::Completed);
    }
}
