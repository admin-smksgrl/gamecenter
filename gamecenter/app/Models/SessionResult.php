<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable([
    'game_session_id', 'total_score', 'max_score', 'correct_count', 'wrong_count',
    'unanswered_count', 'xp_earned', 'coins_earned', 'is_passed', 'detailed_results',
])]
class SessionResult extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'total_score' => 'integer',
            'max_score' => 'integer',
            'correct_count' => 'integer',
            'wrong_count' => 'integer',
            'unanswered_count' => 'integer',
            'xp_earned' => 'integer',
            'coins_earned' => 'integer',
            'is_passed' => 'boolean',
            'detailed_results' => 'array',
        ];
    }

    public function gameSession(): BelongsTo
    {
        return $this->belongsTo(GameSession::class);
    }
}
