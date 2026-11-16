<?php

use App\Http\Controllers\Api\SyncController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes (Sanctum)
|--------------------------------------------------------------------------
| Server hanya memvalidasi & menyimpan. Komputasi game dilakukan di client.
| Antrean offline dikirim sebagai batch ke POST /api/sync.
*/

Route::get('/health', fn () => response()->json([
    'status' => 'ok',
    'time' => now()->toIso8601String(),
]));

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/user', fn (Request $request) => $request->user());

    Route::post('/sync', SyncController::class)
        ->middleware('throttle:60,1')
        ->name('api.sync');
});
