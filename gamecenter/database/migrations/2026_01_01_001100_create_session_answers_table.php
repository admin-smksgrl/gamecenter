<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('session_answers', function (Blueprint $table) {
            $table->id();
            $table->foreignId('game_session_id')
                ->constrained('game_sessions')
                ->cascadeOnDelete();
            $table->foreignId('question_id')
                ->constrained('questions')
                ->cascadeOnDelete();
            $table->json('user_answer')->nullable();
            $table->boolean('is_correct')->default(false);
            $table->unsignedSmallInteger('points_earned')->default(0);
            $table->unsignedInteger('time_spent')->default(0); // detik
            $table->json('ai_feedback')->nullable();           // hasil evaluasi essay
            $table->timestamp('answered_at')->nullable();
            $table->timestamps();

            $table->unique(['game_session_id', 'question_id']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('session_answers');
    }
};
