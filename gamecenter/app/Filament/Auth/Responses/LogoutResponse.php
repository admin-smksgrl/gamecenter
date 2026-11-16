<?php

namespace App\Filament\Auth\Responses;

use Filament\Auth\Http\Responses\Contracts\LogoutResponse as Responsable;
use Illuminate\Http\RedirectResponse;

class LogoutResponse implements Responsable
{
    /**
     * Setelah keluar dari panel, pengguna dikembalikan ke aplikasi
     * Game Center (beranda), bukan ke halaman login admin.
     */
    public function toResponse($request): RedirectResponse
    {
        return redirect()
            ->route('home')
            ->with('info', 'Kamu sudah keluar dari panel.');
    }
}
