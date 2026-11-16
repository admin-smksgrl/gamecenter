<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

#[Fillable([
    'game_session_id', 'question_id', 'user_answer', 'is_correct', 'points_earned',
    'time_spent', 'ai_feedback', 'answered_at',
])]
class SessionAnswer extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'user_answer' => 'array',
            'is_correct' => 'boolean',
            'points_earned' => 'integer',
            'time_spent' => 'integer',
            'ai_feedback' => 'array',
            'answered_at' => 'datetime',
        ];
    }

    public function gameSession(): BelongsTo
    {
        return $this->belongsTo(GameSession::class);
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(Question::class);
    }
}
