<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Auth\Concerns\RedirectsAfterAuth;
use App\Http\Controllers\Controller;
use App\Http\Requests\Auth\LoginRequest;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Inertia\Inertia;
use Inertia\Response;
use Symfony\Component\HttpFoundation\Response as SymfonyResponse;

class AuthenticatedSessionController extends Controller
{
    use RedirectsAfterAuth;

    public function create(Request $request): Response
    {
        return Inertia::render('Auth/Login', [
            'redirect' => $this->safeRedirect($request),
        ]);
    }

    public function store(LoginRequest $request): RedirectResponse|SymfonyResponse
    {
        $request->authenticate();
        $request->session()->regenerate();

        $response = $this->redirectAfterAuth($request);

        // Inertia::location() mengembalikan Response biasa (tanpa ->with()),
        // jadi flash hanya ditempel bila memang redirect biasa.
        return $response instanceof RedirectResponse
            ? $response->with('success', 'Berhasil masuk. Selamat bermain!')
            : $response;
    }

    public function destroy(Request $request): RedirectResponse
    {
        Auth::guard('web')->logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return redirect()->route('home')->with('info', 'Kamu sudah keluar.');
    }
}
