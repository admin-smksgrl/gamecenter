<?php

namespace App\Http\Controllers\Auth;

use App\Enums\UserRole;
use App\Http\Controllers\Auth\Concerns\RedirectsAfterAuth;
use App\Http\Controllers\Controller;
use App\Http\Requests\Auth\RegisterRequest;
use App\Models\User;
use Illuminate\Auth\Events\Registered;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Str;
use Inertia\Inertia;
use Inertia\Response;
use Symfony\Component\HttpFoundation\Response as SymfonyResponse;

class RegisteredUserController extends Controller
{
    use RedirectsAfterAuth;

    public function create(Request $request): Response
    {
        return Inertia::render('Auth/Register', [
            'redirect' => $this->safeRedirect($request),
        ]);
    }

    public function store(RegisterRequest $request): RedirectResponse|SymfonyResponse
    {
        $data = $request->validated();

        $user = User::create([
            'name' => $data['name'],
            'username' => $data['username'],
            'email' => Str::lower($data['email']),
            'password' => $data['password'],
            'role' => UserRole::Student,
            'is_active' => true,
        ]);

        event(new Registered($user));

        Auth::login($user);
        $request->session()->regenerate();

        $response = $this->redirectAfterAuth($request);

        return $response instanceof RedirectResponse
            ? $response->with('success', 'Akun berhasil dibuat. Selamat bergabung!')
            : $response;
    }
}
