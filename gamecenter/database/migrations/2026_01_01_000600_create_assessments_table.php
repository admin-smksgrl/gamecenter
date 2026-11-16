<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('assessments', function (Blueprint $table) {
            $table->id();
            $table->foreignId('chapter_id')
                ->constrained('chapters')
                ->cascadeOnDelete();
            $table->string('title');
            $table->string('difficulty', 10)->default('easy'); // easy, medium, hard
            $table->unsignedSmallInteger('duration')->default(600);   // detik
            $table->unsignedSmallInteger('passing_score')->default(70); // 0..100
            $table->unsignedSmallInteger('order')->default(0);
            $table->boolean('is_active')->default(true);
            $table->timestamps();

            $table->unique(['chapter_id', 'difficulty']);
            $table->index(['difficulty', 'is_active']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('assessments');
    }
};
