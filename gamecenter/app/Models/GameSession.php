<?php

namespace App\Models;

use App\Enums\Difficulty;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;

#[Fillable([
    'client_uuid', 'user_id', 'assessment_id', 'mode', 'score', 'correct_answers',
    'total_questions', 'duration_seconds', 'status', 'synced', 'started_at', 'completed_at',
])]
class GameSession extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'mode' => Difficulty::class,
            'score' => 'integer',
            'correct_answers' => 'integer',
            'total_questions' => 'integer',
            'duration_seconds' => 'integer',
            'synced' => 'boolean',
            'started_at' => 'datetime',
            'completed_at' => 'datetime',
        ];
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function assessment(): BelongsTo
    {
        return $this->belongsTo(Assessment::class);
    }

    public function answers(): HasMany
    {
        return $this->hasMany(SessionAnswer::class);
    }

    public function result(): HasOne
    {
        return $this->hasOne(SessionResult::class);
    }
}
