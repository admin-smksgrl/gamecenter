<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AuthTest extends TestCase
{
    use RefreshDatabase;

    public function test_login_and_register_pages_are_available(): void
    {
        $this->get('/masuk')->assertOk();
        $this->get('/daftar')->assertOk();
    }

    public function test_student_can_register_and_is_logged_in(): void
    {
        $response = $this->post('/daftar', [
            'name' => 'Budi Santoso',
            'username' => 'budi',
            'email' => 'budi@example.com',
            'password' => 'password123',
            'password_confirmation' => 'password123',
        ]);

        $response->assertRedirect('/');
        $this->assertAuthenticated();

        $this->assertDatabaseHas('users', [
            'username' => 'budi',
            'email' => 'budi@example.com',
            'role' => 'student',
            'is_active' => true,
        ]);
    }

    public function test_registration_rejects_duplicate_username_and_email(): void
    {
        User::factory()->create([
            'username' => 'budi',
            'email' => 'budi@example.com',
        ]);

        $this->post('/daftar', [
            'name' => 'Budi Lain',
            'username' => 'budi',
            'email' => 'budi@example.com',
            'password' => 'password123',
            'password_confirmation' => 'password123',
        ])->assertSessionHasErrors(['username', 'email']);

        $this->assertGuest();
    }

    public function test_user_can_login_with_username(): void
    {
        $user = User::factory()->create(['username' => 'siswa']);

        $this->post('/masuk', [
            'login' => 'siswa',
            'password' => 'password',
        ])->assertRedirect('/');

        $this->assertAuthenticatedAs($user);
    }

    public function test_user_can_login_with_email(): void
    {
        $user = User::factory()->create(['email' => 'siswa@example.com']);

        $this->post('/masuk', [
            'login' => 'siswa@example.com',
            'password' => 'password',
        ])->assertRedirect('/');

        $this->assertAuthenticatedAs($user);
    }

    public function test_wrong_password_is_rejected(): void
    {
        User::factory()->create(['username' => 'siswa']);

        $this->post('/masuk', [
            'login' => 'siswa',
            'password' => 'bukan-password',
        ])->assertSessionHasErrors('login');

        $this->assertGuest();
    }

    public function test_inactive_user_cannot_login(): void
    {
        User::factory()->create([
            'username' => 'nonaktif',
            'is_active' => false,
        ]);

        $this->post('/masuk', [
            'login' => 'nonaktif',
            'password' => 'password',
        ])->assertSessionHasErrors('login');

        $this->assertGuest();
    }

    public function test_internal_redirect_is_respected_after_login(): void
    {
        User::factory()->create(['username' => 'siswa']);

        $this->post('/masuk?redirect=%2Fkeanggotaan', [
            'login' => 'siswa',
            'password' => 'password',
        ])->assertRedirect('/keanggotaan');
    }

    public function test_external_redirect_is_ignored_after_login(): void
    {
        User::factory()->create(['username' => 'siswa']);

        $this->post('/masuk?redirect=%2F%2Fevil.example', [
            'login' => 'siswa',
            'password' => 'password',
        ])->assertRedirect('/');
    }

    public function test_user_can_logout(): void
    {
        $user = User::factory()->create();

        $this->actingAs($user)
            ->post('/keluar')
            ->assertRedirect('/');

        $this->assertGuest();
    }
}
