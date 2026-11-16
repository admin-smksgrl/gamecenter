<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('user_progress', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')
                ->constrained('users')
                ->cascadeOnDelete();
            $table->foreignId('chapter_id')
                ->constrained('chapters')
                ->cascadeOnDelete();
            $table->string('status', 20)->default('not_started'); // not_started, in_progress, completed
            $table->unsignedTinyInteger('progress_percentage')->default(0); // 0..100
            $table->unsignedInteger('total_time_spent')->default(0);        // detik
            $table->unsignedSmallInteger('best_score')->default(0);
            $table->unsignedSmallInteger('attempts')->default(0);
            $table->timestamp('last_accessed_at')->nullable();
            $table->timestamp('completed_at')->nullable();
            $table->timestamps();

            $table->unique(['user_id', 'chapter_id']);
            $table->index(['user_id', 'status']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('user_progress');
    }
};
