<?php

namespace App\Http\Requests\Sync;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class StoreSyncBatchRequest extends FormRequest
{
    public function authorize(): bool
    {
        return $this->user() !== null;
    }

    /**
     * @return array<string, mixed>
     */
    public function rules(): array
    {
        return [
            'items' => ['required', 'array', 'min:1', 'max:50'],
            'items.*.uuid' => ['required', 'uuid', 'distinct'],
            'items.*.type' => ['required', Rule::in(['session', 'progress', 'answer', 'material_block'])],
            'items.*.recorded_at' => ['nullable', 'date'],
            'items.*.payload' => ['required', 'array'],
        ];
    }
}
