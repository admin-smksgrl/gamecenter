<?php

namespace Tests\Feature;

use App\Models\MembershipPlan;
use App\Models\User;
use Filament\Facades\Filament;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class FilamentAccessTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();

        Filament::setCurrentPanel(Filament::getPanel('admin'));
    }

    public function test_guest_is_redirected_to_the_main_login_page_from_the_panel(): void
    {
        $this->get('/admin')->assertRedirect('/masuk');
        $this->get('/admin/login')->assertNotFound();
    }

    public function test_main_login_page_is_served_at_masuk(): void
    {
        $this->get('/masuk')
            ->assertOk()
            ->assertSee('data-page="app"', false);
    }

    public function test_admin_can_login_from_the_main_page_with_username(): void
    {
        $admin = User::factory()->admin()->create([
            'username' => 'admin-panel',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'admin-panel',
            'password' => 'password',
        ])->assertRedirect('/admin');

        $this->assertAuthenticatedAs($admin);
    }

    /**
     * Inertia harus diminta memuat ulang penuh ke panel (409), bukan 302,
     * supaya klien Inertia tidak menampilkan dialog error generik.
     */
    public function test_login_from_the_main_page_sends_an_inertia_location_visit_to_the_panel(): void
    {
        User::factory()->admin()->create([
            'username' => 'admin-panel',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'admin-panel',
            'password' => 'password',
        ], [
            'X-Inertia' => 'true',
            'X-Inertia-Version' => '1',
        ])->assertStatus(409)
            ->assertHeader('X-Inertia-Location', '/admin');
    }

    public function test_teacher_logged_in_from_the_main_page_goes_to_the_panel(): void
    {
        $teacher = User::factory()->teacher()->create([
            'username' => 'guru-panel',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'guru-panel',
            'password' => 'password',
        ])->assertRedirect('/admin');

        $this->assertAuthenticatedAs($teacher);
    }

    public function test_admin_can_login_from_the_main_page_with_email(): void
    {
        $admin = User::factory()->admin()->create([
            'email' => 'admin-panel@example.com',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'admin-panel@example.com',
            'password' => 'password',
        ])->assertRedirect('/admin');

        $this->assertAuthenticatedAs($admin);
    }

    public function test_main_login_page_rejects_a_wrong_password(): void
    {
        User::factory()->admin()->create([
            'username' => 'admin-panel',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'admin-panel',
            'password' => 'kata-sandi-salah',
        ])->assertSessionHasErrors('login');

        $this->assertGuest();
    }

    public function test_student_logged_in_from_the_main_page_goes_home(): void
    {
        $student = User::factory()->create([
            'username' => 'siswa-login',
            'password' => 'password',
        ]);

        $this->post('/masuk', [
            'login' => 'siswa-login',
            'password' => 'password',
        ])->assertRedirect('/');

        $this->assertAuthenticatedAs($student);
    }

    public function test_admin_can_open_the_dashboard(): void
    {
        $admin = User::factory()->admin()->create();

        $this->actingAs($admin)->get('/admin')->assertOk();
    }

    public function test_teacher_can_open_the_dashboard(): void
    {
        $teacher = User::factory()->teacher()->create();

        $this->actingAs($teacher)->get('/admin')->assertOk();
    }

    public function test_student_is_forbidden_from_the_panel(): void
    {
        $student = User::factory()->create();

        $this->actingAs($student)->get('/admin')->assertForbidden();
    }

    public function test_inactive_admin_is_forbidden_from_the_panel(): void
    {
        $admin = User::factory()->admin()->create(['is_active' => false]);

        $this->actingAs($admin)->get('/admin')->assertForbidden();
    }

    public function test_admin_can_access_the_membership_resources(): void
    {
        $admin = User::factory()->admin()->create();
        $plan = MembershipPlan::create([
            'slug' => 'standard',
            'name' => 'Standard',
            'tier' => 'standard',
            'price_monthly' => 29000,
            'price_yearly' => 290000,
            'features' => ['Fitur dasar'],
            'is_active' => true,
        ]);

        $this->actingAs($admin)->get('/admin/memberships')->assertOk();
        $this->actingAs($admin)->get('/admin/membership-plans')->assertOk();
        $this->actingAs($admin)->get('/admin/membership-plans/create')->assertOk();
        $this->actingAs($admin)
            ->get("/admin/membership-plans/{$plan->id}/edit")
            ->assertOk();
    }

    public function test_chapter_review_page_is_read_only_and_lists_content(): void
    {
        $this->seed([
            \Database\Seeders\EducationLevelSeeder::class,
            \Database\Seeders\ClassSeeder::class,
            \Database\Seeders\SubjectSeeder::class,
        ]);

        app(\App\Services\Materi\MateriImporter::class)->import(
            json_decode(
                file_get_contents(database_path('seeders/data/sma-smk/fase-e/matematika/ma-1.1-eksponen.json')),
                true,
                512,
                JSON_THROW_ON_ERROR,
            ),
        );

        $admin = User::factory()->admin()->create();
        $chapter = \App\Models\Chapter::query()->where('code', 'MA 1.1')->firstOrFail();

        $this->actingAs($admin)->get('/admin/chapters')->assertOk()->assertSee('Eksponen');
        $this->actingAs($admin)->get("/admin/chapters/{$chapter->id}")
            ->assertOk()
            ->assertSee('Tujuan pembelajaran')
            ->assertSee('Mengidentifikasi sifat-sifat eksponen');

        // Halaman tinjau tidak boleh menyediakan pembuatan/penyuntingan:
        // materi berasal dari JSON, bukan diketik di panel.
        $this->actingAs($admin)->get('/admin/chapters/create')->assertNotFound();
    }

    public function test_teacher_cannot_access_the_membership_resources(): void
    {
        $teacher = User::factory()->teacher()->create();

        $this->actingAs($teacher)->get('/admin/memberships')->assertForbidden();
        $this->actingAs($teacher)->get('/admin/membership-plans')->assertForbidden();
    }

    public function test_sidebar_shows_a_user_card_with_name_role_and_logout(): void
    {
        $admin = User::factory()->admin()->create(['name' => 'Administrator']);

        $this->actingAs($admin)
            ->get('/admin')
            ->assertOk()
            ->assertSee('gc-user-card', false)
            ->assertSee('Administrator')
            ->assertSee('Keluar')
            ->assertSee('/admin/logout')
            ->assertSee('Keluar dari panel?')
            // Tombol konfirmasi tidak boleh pakai atribut data-* kosong:
            // dataset bernilai "" bersifat falsy sehingga submit tertahan.
            ->assertDontSee('data-confirm', false)
            ->assertSee('this.$root.submit()', false)
            // Kartu menggantikan user menu bawaan Filament.
            ->assertDontSee('fi-user-menu-trigger', false);
    }

    public function test_teacher_sees_their_own_role_on_the_user_card(): void
    {
        $teacher = User::factory()->teacher()->create(['name' => 'Bu Sari']);

        $this->actingAs($teacher)
            ->get('/admin')
            ->assertOk()
            ->assertSee('Bu Sari')
            ->assertSee('Guru');
    }

    public function test_logging_out_from_the_panel_returns_to_the_game_center_home(): void
    {
        $admin = User::factory()->admin()->create();

        $this->actingAs($admin)
            ->post('/admin/logout')
            ->assertRedirect('/');

        $this->assertGuest();
    }

    public function test_guest_cannot_hit_the_panel_logout_route(): void
    {
        $this->post('/admin/logout')->assertRedirect('/masuk');

        $this->assertGuest();
    }
}
