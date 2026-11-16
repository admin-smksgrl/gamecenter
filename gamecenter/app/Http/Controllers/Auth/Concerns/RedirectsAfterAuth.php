<?php

namespace App\Http\Controllers\Auth\Concerns;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Symfony\Component\HttpFoundation\Response;

trait RedirectsAfterAuth
{
    /**
     * Terima hanya path internal agar parameter redirect tidak dipakai
     * untuk open redirect.
     */
    protected function safeRedirect(Request $request): ?string
    {
        $redirect = $request->query('redirect');

        if (
            ! is_string($redirect)
            || $redirect === ''
            || $redirect[0] !== '/'
            || str_starts_with($redirect, '//')
            || str_contains($redirect, '\\')
            || str_contains($redirect, "\n")
            || str_contains($redirect, "\r")
        ) {
            return null;
        }

        return $redirect;
    }

    protected function redirectAfterAuth(Request $request): RedirectResponse|Response
    {
        $target = $this->safeRedirect($request);

        if ($target !== null) {
            return str_starts_with($target, '/admin')
                ? Inertia::location($target)
                : redirect()->to($target);
        }

        // Satu halaman login untuk semua peran: admin/guru langsung ke panel.
        // Panel Filament adalah aplikasi terpisah (bukan halaman Inertia),
        // jadi pakai Inertia::location agar browser memuat ulang penuh
        // dan tidak memunculkan dialog error generik.
        $user = $request->user();

        if ($user !== null && ($user->isAdmin() || $user->isTeacher())) {
            return Inertia::location('/admin');
        }

        return redirect()->intended(route('home'));
    }
}
