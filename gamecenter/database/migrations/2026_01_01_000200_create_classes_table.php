<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('classes', function (Blueprint $table) {
            $table->id();
            $table->foreignId('education_level_id')
                ->constrained('education_levels')
                ->cascadeOnDelete();
            $table->string('name', 50);           // "Kelas 10", "Kelompok A"
            $table->string('slug', 50);           // "kelas-10"
            $table->unsignedTinyInteger('grade_level'); // 1..12 (0 untuk PAUD/TK)
            $table->string('phase', 5)->nullable();     // Fase A..F (Kurikulum Merdeka)
            $table->unsignedSmallInteger('order')->default(0);
            $table->boolean('is_active')->default(true);
            $table->timestamps();

            $table->unique(['education_level_id', 'slug']);
            $table->index(['is_active', 'order']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('classes');
    }
};
