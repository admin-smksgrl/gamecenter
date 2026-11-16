<?php

namespace App\Services\Materi;

/**
 * Ringkasan hasil satu kali impor.
 *
 * Angka "created" dan "updated" dipisah agar operator bisa membedakan
 * impor pertama (semua created) dari impor ulang yang idempoten
 * (semua updated, tidak ada created).
 */
class MateriImportResult
{
    public int $chaptersCreated = 0;

    public int $chaptersUpdated = 0;

    public int $materialsCreated = 0;

    public int $materialsUpdated = 0;

    public int $assessmentsCreated = 0;

    public int $assessmentsUpdated = 0;

    public int $questionsCreated = 0;

    public int $questionsUpdated = 0;

    public int $optionsCreated = 0;

    /**
     * @var array<int, string>
     */
    public array $warnings = [];

    public function addWarning(string $message): void
    {
        $this->warnings[] = $message;
    }

    /**
     * True bila tidak ada baris baru sama sekali — tanda impor idempoten.
     */
    public function isRepeat(): bool
    {
        return $this->chaptersCreated === 0
            && $this->materialsCreated === 0
            && $this->assessmentsCreated === 0
            && $this->questionsCreated === 0;
    }

    /**
     * @return array<string, int>
     */
    public function toArray(): array
    {
        return [
            'chapters_created' => $this->chaptersCreated,
            'chapters_updated' => $this->chaptersUpdated,
            'materials_created' => $this->materialsCreated,
            'materials_updated' => $this->materialsUpdated,
            'assessments_created' => $this->assessmentsCreated,
            'assessments_updated' => $this->assessmentsUpdated,
            'questions_created' => $this->questionsCreated,
            'questions_updated' => $this->questionsUpdated,
            'options_created' => $this->optionsCreated,
            'warnings' => $this->warnings,
        ];
    }

    public function summary(): string
    {
        return sprintf(
            'chapter %d baru/%d diperbarui, materi %d/%d, asesmen %d/%d, soal %d/%d, opsi %d',
            $this->chaptersCreated,
            $this->chaptersUpdated,
            $this->materialsCreated,
            $this->materialsUpdated,
            $this->assessmentsCreated,
            $this->assessmentsUpdated,
            $this->questionsCreated,
            $this->questionsUpdated,
            $this->optionsCreated,
        );
    }
}
