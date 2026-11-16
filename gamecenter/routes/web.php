<?php

use App\Http\Controllers\Auth\AuthenticatedSessionController;
use App\Http\Controllers\Auth\RegisteredUserController;
use App\Http\Controllers\GameCenterController;
use App\Http\Controllers\GuideController;
use App\Http\Controllers\MembershipController;
use App\Http\Controllers\PlayController;
use App\Http\Controllers\ProgressController;
use App\Http\Controllers\ResultController;
use Illuminate\Support\Facades\Route;

Route::get('/', [GameCenterController::class, 'index'])->name('home');

Route::get('/main/{assessment}', [PlayController::class, 'show'])
    ->whereNumber('assessment')
    ->name('play.show');

Route::middleware('guest')->group(function () {
    Route::get('/masuk', [AuthenticatedSessionController::class, 'create'])->name('login');
    Route::post('/masuk', [AuthenticatedSessionController::class, 'store'])
        ->middleware('throttle:10,1')
        ->name('login.store');

    Route::get('/daftar', [RegisteredUserController::class, 'create'])->name('register');
    Route::post('/daftar', [RegisteredUserController::class, 'store'])
        ->middleware('throttle:10,1')
        ->name('register.store');
});

Route::post('/keluar', [AuthenticatedSessionController::class, 'destroy'])
    ->middleware('auth')
    ->name('logout');

Route::middleware('auth')->group(function () {
    Route::get('/progres', [ProgressController::class, 'index'])
        ->name('progress.index');

    Route::get('/hasil/{gameSession}', [ResultController::class, 'show'])
        ->whereNumber('gameSession')
        ->name('result.show');
});

Route::get('/panduan/{page?}', GuideController::class)
    ->where('page', '[a-z0-9-]+')
    ->name('guide.show');

Route::get('/keanggotaan', [MembershipController::class, 'index'])
    ->name('membership.index');

Route::post('/keanggotaan/ajukan', [MembershipController::class, 'store'])
    ->middleware('auth')
    ->name('membership.store');
