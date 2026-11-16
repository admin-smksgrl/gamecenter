<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia as Assert;
use Tests\TestCase;

class GuideTest extends TestCase
{
    use RefreshDatabase;

    public function test_guest_can_open_the_default_guide_topic(): void
    {
        $this->get('/panduan')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Guide/Show')
                ->where('page', 'pengenalan'));
    }

    public function test_guide_deep_links_are_public(): void
    {
        $this->get('/panduan/upgrade')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Guide/Show')
                ->where('page', 'upgrade'));
    }

    public function test_unknown_slug_is_passed_through_for_the_client_404_state(): void
    {
        $this->get('/panduan/topik-tidak-ada')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Guide/Show')
                ->where('page', 'topik-tidak-ada'));
    }
}
