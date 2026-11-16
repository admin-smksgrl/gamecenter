<?php

namespace App\Enums;

enum Difficulty: string
{
    case Easy = 'easy';
    case Medium = 'medium';
    case Hard = 'hard';

    public function label(): string
    {
        return match ($this) {
            self::Easy => 'Mudah',
            self::Medium => 'Sedang',
            self::Hard => 'Sulit',
        };
    }

    public function questionCount(): int
    {
        return match ($this) {
            self::Easy => 5,
            self::Medium => 10,
            self::Hard => 15,
        };
    }

    public function pointsPerQuestion(): int
    {
        return match ($this) {
            self::Easy => 10,
            self::Medium => 20,
            self::Hard => 30,
        };
    }

    public function streakMultiplier(): int
    {
        return match ($this) {
            self::Easy => 2,
            self::Medium => 3,
            self::Hard => 5,
        };
    }

    public function timePerQuestion(): int
    {
        // detik per soal
        return match ($this) {
            self::Easy => 90,
            self::Medium => 75,
            self::Hard => 60,
        };
    }

    public function hintAvailable(): bool
    {
        return $this !== self::Hard;
    }

    public static function values(): array
    {
        return array_map(fn (self $case) => $case->value, self::cases());
    }
}
