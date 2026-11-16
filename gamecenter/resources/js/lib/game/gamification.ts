import type { GameQuestion, GameSummary } from './game-engine';

export const LEVEL_THRESHOLDS = [
    { level: 1, xp: 0, title: 'Pemula' },
    { level: 2, xp: 100, title: 'Pemain' },
    { level: 3, xp: 250, title: 'Ahli' },
    { level: 4, xp: 500, title: 'Master' },
    { level: 5, xp: 1000, title: 'Legenda' },
];

export interface LevelProgress {
    level: number;
    title: string;
    previousXp: number;
    nextXp: number | null;
    progressPercent: number;
    xpToNextLevel: number | null;
}

export interface SessionBadge {
    slug: string;
    title: string;
    icon: string;
    description: string;
}

export interface BadgeContext {
    subjectName: string;
    difficulty: string;
    questions: GameQuestion[];
}

export function levelForXp(xp: number): number {
    return LEVEL_THRESHOLDS.reduce(
        (level, entry) => (xp >= entry.xp ? entry.level : level),
        1,
    );
}

export function levelProgress(xp: number): LevelProgress {
    const current =
        [...LEVEL_THRESHOLDS]
            .reverse()
            .find((entry) => xp >= entry.xp) ?? LEVEL_THRESHOLDS[0];
    const next =
        LEVEL_THRESHOLDS.find((entry) => entry.level === current.level + 1) ??
        null;

    const span = next ? next.xp - current.xp : 0;
    const progressPercent = next
        ? Math.min(100, Math.round(((xp - current.xp) / span) * 100))
        : 100;

    return {
        level: current.level,
        title: current.title,
        previousXp: current.xp,
        nextXp: next?.xp ?? null,
        progressPercent,
        xpToNextLevel: next ? Math.max(0, next.xp - xp) : null,
    };
}

export function coinsForXp(xp: number): number {
    return Math.floor(xp / 5);
}

export function sessionBadges(
    summary: GameSummary,
    context: BadgeContext,
): SessionBadge[] {
    const badges: SessionBadge[] = [];
    const perfect = summary.maxScore > 0 && summary.totalScore === 100;
    const hasSimulation = context.questions.some(
        (question) => question.type === 'simulation',
    );

    if (summary.totalQuestions - summary.unansweredCount > 0) {
        badges.push({
            slug: 'first-step',
            title: 'Langkah Pertama',
            icon: '🌱',
            description: 'Menyelesaikan soal pada sesi ini.',
        });
    }

    if (perfect) {
        badges.push({
            slug: 'perfect-score',
            title: 'Sempurna!',
            icon: '🏆',
            description: 'Semua soal inti terjawab benar.',
        });
    }

    if (summary.bestStreak >= 3) {
        badges.push({
            slug: 'streak-3',
            title: 'Pemanasan',
            icon: '🔥',
            description: 'Tiga jawaban benar berturut-turut.',
        });
    }

    if (summary.bestStreak >= 10) {
        badges.push({
            slug: 'streak-10',
            title: 'Tak Terbendung',
            icon: '⚡',
            description: 'Sepuluh jawaban benar berturut-turut.',
        });
    }

    if (
        perfect &&
        context.difficulty === 'hard' &&
        context.subjectName.toLowerCase().includes('matematika')
    ) {
        badges.push({
            slug: 'math-genius',
            title: 'Jenius Matematika',
            icon: '🧮',
            description: 'Nilai sempurna pada mode sulit Matematika.',
        });
    }

    if (hasSimulation && summary.totalScore >= 80) {
        badges.push({
            slug: 'case-master',
            title: 'Ahli Studi Kasus',
            icon: '🧠',
            description: 'Menuntaskan simulasi dengan nilai di atas 80.',
        });
    }

    return badges;
}
