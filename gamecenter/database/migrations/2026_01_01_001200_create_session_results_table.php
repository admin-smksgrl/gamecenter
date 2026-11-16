<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('session_results', function (Blueprint $table) {
            $table->id();
            $table->foreignId('game_session_id')
                ->unique()
                ->constrained('game_sessions')
                ->cascadeOnDelete();
            $table->unsignedInteger('total_score')->default(0);
            $table->unsignedInteger('max_score')->default(0);
            $table->unsignedSmallInteger('correct_count')->default(0);
            $table->unsignedSmallInteger('wrong_count')->default(0);
            $table->unsignedSmallInteger('unanswered_count')->default(0);
            $table->unsignedInteger('xp_earned')->default(0);
            $table->unsignedInteger('coins_earned')->default(0);
            $table->boolean('is_passed')->default(false);
            $table->json('detailed_results')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('session_results');
    }
};
