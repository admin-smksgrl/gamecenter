<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('questions', function (Blueprint $table) {
            $table->id();
            $table->foreignId('assessment_id')
                ->constrained('assessments')
                ->cascadeOnDelete();
            $table->string('type', 30)->default('multiple_choice');
            // multiple_choice, multiple_answer, drag_drop, matching, puzzle, simulation, essay
            $table->text('question');
            $table->string('media_url')->nullable();
            $table->json('options')->nullable();          // payload mentah untuk drag/matching/puzzle
            $table->json('correct_answer')->nullable();   // kunci jawaban (bentuk fleksibel)
            $table->json('rubric')->nullable();           // rubrik penilaian essay
            $table->text('explanation')->nullable();
            $table->string('hint')->nullable();
            $table->unsignedSmallInteger('points')->default(10);
            $table->unsignedSmallInteger('time_limit')->nullable(); // detik per soal
            $table->boolean('ai_assisted')->default(false);         // essay dinilai AI
            $table->unsignedSmallInteger('order')->default(0);
            $table->timestamps();

            $table->index(['assessment_id', 'order']);
            $table->index('type');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('questions');
    }
};
