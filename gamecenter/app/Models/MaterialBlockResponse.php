<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

/**
 * Satu baris = satu blok interaktif yang dikerjakan seorang siswa pada satu
 * materi. Skor blok bersifat formatif (plan §3.4.1) dan tidak menambah skor
 * sesi resmi.
 */
#[Fillable([
    'user_id', 'material_id', 'block_id', 'block_type', 'score', 'max_score',
    'attempts', 'is_completed', 'details', 'first_completed_at',
    'last_answered_at',
])]
class MaterialBlockResponse extends Model
{
    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'score' => 'integer',
            'max_score' => 'integer',
            'attempts' => 'integer',
            'is_completed' => 'boolean',
            'details' => 'array',
            'first_completed_at' => 'datetime',
            'last_answered_at' => 'datetime',
        ];
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function material(): BelongsTo
    {
        return $this->belongsTo(LearningMaterial::class, 'material_id');
    }
}
