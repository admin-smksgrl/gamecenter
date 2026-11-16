<?php

namespace App\Enums;

enum QuestionType: string
{
    case MultipleChoice = 'multiple_choice';
    case MultipleAnswer = 'multiple_answer';
    case DragDrop = 'drag_drop';
    case Matching = 'matching';
    case Puzzle = 'puzzle';
    case Simulation = 'simulation';
    case Essay = 'essay';

    public function label(): string
    {
        return match ($this) {
            self::MultipleChoice => 'Pilihan Ganda',
            self::MultipleAnswer => 'Pilihan Ganda Kompleks',
            self::DragDrop => 'Tarik & Letakkan',
            self::Matching => 'Menjodohkan',
            self::Puzzle => 'Puzzle',
            self::Simulation => 'Simulasi',
            self::Essay => 'Uraian',
        };
    }

    public static function values(): array
    {
        return array_map(fn (self $case) => $case->value, self::cases());
    }
}
