<?php

namespace App\Enums;

enum MaterialType: string
{
    case Text = 'text';
    case Video = 'video';
    case Image = 'image';
    case Audio = 'audio';
    case Interactive = 'interactive';
    case Visual = 'visual';
    case Scenario = 'scenario';
    case Game = 'game';

    public function label(): string
    {
        return match ($this) {
            self::Text => 'Teks',
            self::Video => 'Video',
            self::Image => 'Gambar',
            self::Audio => 'Audio',
            self::Interactive => 'Interaktif',
            self::Visual => 'Visual',
            self::Scenario => 'Skenario',
            self::Game => 'Mini Game',
        };
    }

    public static function values(): array
    {
        return array_map(fn (self $case) => $case->value, self::cases());
    }
}
