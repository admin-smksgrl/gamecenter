<?php

namespace App\Services\Materi;

use RuntimeException;

/**
 * Dilempar ketika berkas materi tidak sesuai skema.
 *
 * Pesan selalu menyebut lokasi masalah (mis. "chapters[2].assessments[0]")
 * supaya penulis materi tahu persis bagian mana yang harus diperbaiki.
 */
class MateriValidationException extends RuntimeException
{
    /**
     * @param  array<int, string>  $problems
     */
    private function __construct(
        string $message,
        public readonly array $problems = [],
        public readonly ?string $sourceFile = null,
    ) {
        parent::__construct($message);
    }

    public static function plain(string $message): self
    {
        return new self($message);
    }

    /**
     * @param  array<int, string>  $problems
     */
    public static function inFile(string $file, array $problems): self
    {
        $count = count($problems);
        $first = $problems[0] ?? 'tidak diketahui';

        $message = sprintf(
            '%s memiliki %d masalah: %s%s',
            basename($file),
            $count,
            $first,
            $count > 1 ? ' (dan ' . ($count - 1) . ' lainnya)' : '',
        );

        return new self($message, $problems, $file);
    }
}
