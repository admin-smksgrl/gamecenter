<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AdminDashboardTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_dashboard_shows_the_themed_overview_and_membership_queue(): void
    {
        $admin = User::factory()->admin()->create();

        $this->actingAs($admin)
            ->get('/admin')
            ->assertOk()
            ->assertSee('Ringkasan')
            ->assertSee('Ruang belajar')
            ->assertSee('Akses cepat')
            ->assertSee('Sesi selesai')
            ->assertSee('Pengajuan menunggu')
            ->assertSee('Pengajuan upgrade terbaru')
            ->assertSee('Tinjau pengajuan');
    }

    public function test_teacher_dashboard_hides_membership_management(): void
    {
        $teacher = User::factory()->teacher()->create();

        $this->actingAs($teacher)
            ->get('/admin')
            ->assertOk()
            ->assertSee('Materi aktif')
            ->assertSee('Akses cepat')
            ->assertDontSee('Pengajuan upgrade terbaru')
            ->assertDontSee('Tinjau pengajuan');
    }
}
