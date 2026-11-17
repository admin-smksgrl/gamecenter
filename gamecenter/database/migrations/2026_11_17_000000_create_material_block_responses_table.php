<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

/**
 * Menyimpan hasil kerja blok interaktif materi (plan-materi-interaktif §3.4.1).
 *
 * Skor blok bersifat **formatif**: tidak pernah masuk `game_sessions.total_score`.
 * Kunci unik (user_id, material_id, block_id) membuat pengiriman ulang dari
 * antrean offline idempoten.
 */
return new class extends Migration
{
    public function up(): void
    {
        Schema::create('material_block_responses', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')
                ->constrained('users')
                ->cascadeOnDelete();
            $table->foreignId('material_id')
                ->constrained('learning_materials')
                ->cascadeOnDelete();

            $table->string('block_id', 64);   // id blok di dalam JSON materi
            $table->string('block_type', 32); // checkpoint, sort, categorize, ...

            $table->unsignedSmallInteger('score')->default(0);     // 0..100
            $table->unsignedSmallInteger('max_score')->default(100);
            $table->unsignedSmallInteger('attempts')->default(1);
            $table->boolean('is_completed')->default(false);

            $table->json('details')->nullable(); // jawaban terakhir per butir
            $table->timestamp('first_completed_at')->nullable();
            $table->timestamp('last_answered_at')->nullable();
            $table->timestamps();

            $table->unique(['user_id', 'material_id', 'block_id']);
            $table->index(['user_id', 'block_type']);
            $table->index(['material_id', 'block_type']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('material_block_responses');
    }
};
