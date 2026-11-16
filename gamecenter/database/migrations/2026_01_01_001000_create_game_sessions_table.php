<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('game_sessions', function (Blueprint $table) {
            $table->id();
            $table->uuid('client_uuid')->unique(); // idempotency untuk sync offline
            $table->foreignId('user_id')
                ->constrained('users')
                ->cascadeOnDelete();
            $table->foreignId('assessment_id')
                ->constrained('assessments')
                ->cascadeOnDelete();
            $table->string('mode', 10)->default('easy'); // easy, medium, hard
            $table->unsignedSmallInteger('score')->default(0);            // 0..100
            $table->unsignedSmallInteger('correct_answers')->default(0);
            $table->unsignedSmallInteger('total_questions')->default(0);
            $table->unsignedInteger('duration_seconds')->default(0);     // waktu bermain
            $table->string('status', 20)->default('completed');          // in_progress, completed, abandoned
            $table->boolean('synced')->default(false);
            $table->timestamp('started_at')->nullable();
            $table->timestamp('completed_at')->nullable();
            $table->timestamps();

            $table->index(['user_id', 'completed_at']);
            $table->index(['assessment_id', 'status']);
            $table->index(['user_id', 'synced']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('game_sessions');
    }
};
