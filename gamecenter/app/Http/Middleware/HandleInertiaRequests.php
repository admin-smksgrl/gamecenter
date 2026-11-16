<?php

namespace App\Http\Middleware;

use Illuminate\Http\Request;
use Inertia\Middleware;

class HandleInertiaRequests extends Middleware
{
    /**
     * The root template that is loaded on the first page visit.
     */
    protected $rootView = 'app';

    /**
     * Determine the asset version.
     */
    public function version(Request $request): ?string
    {
        return parent::version($request);
    }

    /**
     * Define the props that are shared by default.
     *
     * @return array<string, mixed>
     */
    public function share(Request $request): array
    {
        $user = $request->user();

        return [
            ...parent::share($request),
            'version' => $this->appVersion(),
            'app' => [
                'name' => config('app.name'),
                'locale' => app()->getLocale(),
                'env' => app()->environment(),
            ],
            'auth' => [
                'user' => $user ? [
                    'id' => $user->id,
                    'name' => $user->name,
                    'username' => $user->username,
                    'email' => $user->email,
                    'role' => $user->role,
                    'xp' => (int) $user->xp,
                    'level' => (int) $user->level,
                    'coins' => (int) $user->coins,
                    'avatar' => $user->avatar,
                    'class_id' => $user->class_id,
                    'class_name' => $user->classRoom?->name,
                    'education_level' => $user->classRoom?->educationLevel?->name,
                    'education_level_slug' => $user->classRoom?->educationLevel?->slug,
                    'level_theme' => $user->classRoom?->educationLevel?->theme ?? 'default',
                    'membership' => $user->membershipSummary(),
                ] : null,
            ],
            'flash' => [
                'success' => fn () => $request->session()->get('success'),
                'error' => fn () => $request->session()->get('error'),
                'info' => fn () => $request->session()->get('info'),
            ],
        ];
    }

    /**
     * Read the current release version from the first changelog heading.
     */
    protected function appVersion(): string
    {
        $changelog = @file_get_contents(base_path('changelog.md'));

        if (
            $changelog !== false
            && preg_match('/^#+\s*\[?v?(\d+\.\d+\.\d+)/mi', $changelog, $matches) === 1
        ) {
            return $matches[1];
        }

        return '0.0.0';
    }
}
