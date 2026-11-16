<?php

namespace App\Http\Controllers;

use Inertia\Inertia;
use Inertia\Response;

class GuideController extends Controller
{
    /**
     * Pusat bantuan publik. Isi topik tinggal di sisi klien agar ringan.
     */
    public function __invoke(?string $page = null): Response
    {
        return Inertia::render('Guide/Show', [
            'page' => $page ?? 'pengenalan',
        ]);
    }
}
