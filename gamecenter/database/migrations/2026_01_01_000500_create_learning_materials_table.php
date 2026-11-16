<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('learning_materials', function (Blueprint $table) {
            $table->id();
            $table->foreignId('chapter_id')
                ->constrained('chapters')
                ->cascadeOnDelete();
            $table->string('type', 30)->default('text'); // text, video, image, audio, interactive, game
            $table->string('title');
            $table->longText('content')->nullable();      // markdown / HTML ter-sanitasi
            $table->json('blocks')->nullable();           // konten terstruktur untuk game
            $table->string('media_url')->nullable();
            $table->string('media_type', 30)->nullable();
            $table->unsignedSmallInteger('duration')->default(0); // detik
            $table->unsignedSmallInteger('order')->default(0);
            $table->string('source_reference')->nullable(); // "BS Matematika KLS X hal. 12"
            $table->boolean('is_active')->default(true);
            $table->timestamps();

            $table->index(['chapter_id', 'type']);
            $table->index(['is_active', 'order']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('learning_materials');
    }
};
