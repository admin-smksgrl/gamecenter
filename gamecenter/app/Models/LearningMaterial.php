<?php

namespace App\Models;

use App\Enums\MaterialType;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

#[Fillable([
    'chapter_id', 'type', 'title', 'content', 'blocks', 'media_url', 'media_type',
    'duration', 'order', 'source_reference', 'is_active',
])]
class LearningMaterial extends Model
{
    use HasFactory;

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'type' => MaterialType::class,
            'blocks' => 'array',
            'duration' => 'integer',
            'order' => 'integer',
            'is_active' => 'boolean',
        ];
    }

    public function chapter(): BelongsTo
    {
        return $this->belongsTo(Chapter::class);
    }

    /**
     * Skor blok interaktif (formatif) yang dikirim siswa untuk materi ini.
     */
    public function blockResponses(): HasMany
    {
        return $this->hasMany(MaterialBlockResponse::class, 'material_id');
    }

    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', true);
    }
}
