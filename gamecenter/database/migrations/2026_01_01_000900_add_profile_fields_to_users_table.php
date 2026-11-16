<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->string('username', 50)->nullable()->unique()->after('name');
            $table->string('role', 20)->default('student')->after('password'); // student, teacher, admin
            $table->foreignId('class_id')->nullable()->after('role')
                ->constrained('classes')->nullOnDelete();
            $table->string('avatar')->nullable()->after('class_id');
            $table->unsignedInteger('xp')->default(0)->after('avatar');
            $table->unsignedTinyInteger('level')->default(1)->after('xp');
            $table->unsignedInteger('coins')->default(0)->after('level');
            $table->unsignedSmallInteger('streak_days')->default(0)->after('coins');
            $table->timestamp('last_played_at')->nullable()->after('streak_days');
            $table->boolean('is_active')->default(true)->after('last_played_at');

            $table->index(['role', 'is_active']);
            $table->index('xp');
        });
    }

    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropForeign(['class_id']);
            $table->dropColumn([
                'username', 'role', 'class_id', 'avatar', 'xp', 'level',
                'coins', 'streak_days', 'last_played_at', 'is_active',
            ]);
        });
    }
};
