<?php

namespace App\Models;

use App\Enums\QuestionType;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable([
    'assessment_id', 'type', 'question', 'media_url', 'options', 'correct_answer',
    'rubric', 'explanation', 'hint', 'points', 'time_limit', 'ai_assisted', 'order',
])]
class Question extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'type' => QuestionType::class,
            'options' => 'array',
            'correct_answer' => 'array',
            'rubric' => 'array',
            'points' => 'integer',
            'time_limit' => 'integer',
            'ai_assisted' => 'boolean',
            'order' => 'integer',
        ];
    }

    public function assessment(): BelongsTo
    {
        return $this->belongsTo(Assessment::class);
    }

    public function questionOptions(): HasMany
    {
        return $this->hasMany(QuestionOption::class)->orderBy('order');
    }

    public function answers(): HasMany
    {
        return $this->hasMany(SessionAnswer::class);
    }

    public function isObjective(): bool
    {
        return $this->type !== QuestionType::Essay;
    }
}
