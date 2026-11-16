/**
 * Mesin permainan client-side.
 *
 * Server tetap menilai ulang pilihan ganda saat sinkronisasi. Tipe interaktif
 * memakai penilaian client, sedangkan uraian ditandai `ungraded` dan tidak
 * masuk skor sesi sampai dinilai AI/guru.
 */

export type GameQuestionType =
    | 'multiple_choice'
    | 'multiple_answer'
    | 'drag_drop'
    | 'matching'
    | 'puzzle'
    | 'simulation'
    | 'essay';

export interface GameOption {
    id: number;
    label: string | null;
    text: string;
    order: number;
    is_correct: boolean;
}

export interface GameQuestion {
    id: number;
    type: GameQuestionType;
    type_label: string;
    question: string;
    media_url: string | null;
    hint: string | null;
    explanation: string | null;
    points: number;
    time_limit: number | null;
    order: number;
    options: GameOption[];
    payload: unknown;
    correct_answer: Record<string, unknown> | null;
    rubric: Array<{ point: string; weight: number }> | null;
}

export interface GameResponse {
    option_id?: number;
    option_ids?: number[];
    order?: string[];
    pairs?: Record<string, string>;
    text?: string;
}

export interface EvaluatedAnswer {
    questionId: number;
    response: GameResponse;
    isCorrect: boolean;
    pointsEarned: number;
    ungraded: boolean;
    expected: string | null;
    timeSpent: number;
    answeredAt: string;
}

export interface Evaluation {
    isCorrect: boolean;
    pointsEarned: number;
    ungraded: boolean;
    expected: string | null;
}

export interface GameSummary {
    totalScore: number;
    earnedPoints: number;
    maxScore: number;
    correctCount: number;
    wrongCount: number;
    unansweredCount: number;
    totalQuestions: number;
    bestStreak: number;
    durationSeconds: number;
    isPassed: boolean;
}

export interface OrderingPiece {
    id: string;
    text: string;
}

export interface MatchingPair {
    id: string;
    left: string;
    right: string;
}

export interface SessionAnswerPayload {
    question_id: number;
    user_answer: GameResponse;
    time_spent: number;
    answered_at: string;
    is_correct: boolean;
    points_earned: number;
}

function isRecord(value: unknown): value is Record<string, unknown> {
    return typeof value === 'object' && value !== null && !Array.isArray(value);
}

export function isOrderingType(type: GameQuestionType): boolean {
    return type === 'drag_drop' || type === 'puzzle';
}

export function isMatchingType(type: GameQuestionType): boolean {
    return type === 'matching';
}

export function shuffleWithSeed<T>(items: T[], seed: number): T[] {
    const copy = [...items];
    let state = Math.abs(seed) || 1;

    for (let index = copy.length - 1; index > 0; index -= 1) {
        state = (state * 1664525 + 1013904223) >>> 0;
        const swapIndex = state % (index + 1);
        [copy[index], copy[swapIndex]] = [copy[swapIndex], copy[index]];
    }

    return copy;
}

export function orderingPieces(question: GameQuestion): OrderingPiece[] {
    if (Array.isArray(question.payload)) {
        const pieces = question.payload
            .map((item, index): OrderingPiece | null => {
                if (typeof item === 'string') {
                    return { id: `piece-${index}`, text: item };
                }

                if (isRecord(item) && typeof item.text === 'string') {
                    return {
                        id: String(item.id ?? `piece-${index}`),
                        text: item.text,
                    };
                }

                return null;
            })
            .filter((piece): piece is OrderingPiece => piece !== null);

        if (pieces.length > 0) {
            return pieces;
        }
    }

    return question.options.map((option) => ({
        id: String(option.id),
        text: option.text,
    }));
}

export function expectedOrder(question: GameQuestion): string[] {
    const configured = question.correct_answer?.order;

    if (Array.isArray(configured)) {
        return configured.map(String);
    }

    return orderingPieces(question).map((piece) => piece.id);
}

export function initialOrder(question: GameQuestion): string[] {
    const pieces = orderingPieces(question);

    if (pieces.length <= 1) {
        return pieces.map((piece) => piece.id);
    }

    return shuffleWithSeed(pieces, question.id).map((piece) => piece.id);
}

export function matchingPairs(question: GameQuestion): MatchingPair[] {
    if (Array.isArray(question.payload)) {
        const pairs = question.payload
            .map((item, index): MatchingPair | null => {
                if (
                    isRecord(item) &&
                    typeof item.left === 'string' &&
                    typeof item.right === 'string'
                ) {
                    return {
                        id: String(item.id ?? `pair-${index}`),
                        left: item.left,
                        right: item.right,
                    };
                }

                return null;
            })
            .filter((pair): pair is MatchingPair => pair !== null);

        if (pairs.length > 0) {
            return pairs;
        }
    }

    return [];
}

export function expectedPairs(
    question: GameQuestion,
): Record<string, string> {
    const configured = question.correct_answer?.pairs;

    if (isRecord(configured)) {
        return Object.fromEntries(
            Object.entries(configured).map(([key, value]) => [
                String(key),
                String(value),
            ]),
        );
    }

    return Object.fromEntries(
        matchingPairs(question).map((pair) => [pair.id, pair.right]),
    );
}

export function matchingRightOptions(question: GameQuestion): string[] {
    return Array.from(
        new Set(matchingPairs(question).map((pair) => pair.right)),
    );
}

function choiceExpectedLabel(question: GameQuestion): string | null {
    const correct = question.options.filter((option) => option.is_correct);

    if (correct.length === 0) {
        return null;
    }

    return correct
        .map((option) =>
            option.label ? `${option.label}. ${option.text}` : option.text,
        )
        .join(' · ');
}

export function expectedAnswerLabel(question: GameQuestion): string | null {
    if (question.type === 'essay') {
        return null;
    }

    if (isOrderingType(question.type)) {
        const pieces = new Map(
            orderingPieces(question).map((piece) => [piece.id, piece.text]),
        );

        return expectedOrder(question)
            .map((id) => pieces.get(id) ?? id)
            .join(' → ');
    }

    if (isMatchingType(question.type)) {
        const pairs = matchingPairs(question);
        const expected = expectedPairs(question);

        return pairs
            .map((pair) => `${pair.left} → ${expected[pair.id] ?? '—'}`)
            .join(' · ');
    }

    return choiceExpectedLabel(question);
}

export function evaluateQuestion(
    question: GameQuestion,
    response: GameResponse,
): Evaluation {
    const expected = expectedAnswerLabel(question);

    if (question.type === 'essay') {
        return {
            isCorrect: false,
            pointsEarned: 0,
            ungraded: true,
            expected: null,
        };
    }

    let isCorrect = false;

    if (question.type === 'multiple_choice' || question.type === 'simulation') {
        const correctIds = question.options
            .filter((option) => option.is_correct)
            .map((option) => option.id);

        isCorrect =
            typeof response.option_id === 'number' &&
            correctIds.includes(response.option_id);
    }

    if (question.type === 'multiple_answer') {
        const selected = Array.from(new Set(response.option_ids ?? [])).sort(
            (left, right) => left - right,
        );
        const correct = question.options
            .filter((option) => option.is_correct)
            .map((option) => option.id)
            .sort((left, right) => left - right);

        isCorrect =
            correct.length > 0 &&
            selected.length === correct.length &&
            selected.every((id, index) => id === correct[index]);
    }

    if (isOrderingType(question.type)) {
        const correct = expectedOrder(question);
        const selected = response.order ?? [];

        isCorrect =
            correct.length > 0 &&
            selected.length === correct.length &&
            selected.every((id, index) => id === correct[index]);
    }

    if (isMatchingType(question.type)) {
        const pairs = matchingPairs(question);
        const correct = expectedPairs(question);
        const selected = response.pairs ?? {};

        isCorrect =
            pairs.length > 0 &&
            pairs.every((pair) => selected[pair.id] === correct[pair.id]);
    }

    return {
        isCorrect,
        pointsEarned: isCorrect ? question.points : 0,
        ungraded: false,
        expected,
    };
}

export function hasResponse(
    question: GameQuestion,
    response: GameResponse | null,
): boolean {
    if (!response) {
        return false;
    }

    if (question.type === 'essay') {
        return (response.text ?? '').trim().length > 0;
    }

    if (question.type === 'multiple_choice' || question.type === 'simulation') {
        return typeof response.option_id === 'number';
    }

    if (question.type === 'multiple_answer') {
        return (response.option_ids ?? []).length > 0;
    }

    if (isOrderingType(question.type)) {
        return (response.order ?? []).length > 0;
    }

    if (isMatchingType(question.type)) {
        return Object.keys(response.pairs ?? {}).length > 0;
    }

    return false;
}

export function summarizeGame(
    questions: GameQuestion[],
    answers: Record<number, EvaluatedAnswer>,
    passingScore: number,
    startedAt: string,
    finishedAt: string,
): GameSummary {
    const graded = questions.filter(
        (question) => question.type !== 'essay',
    );

    let earnedPoints = 0;
    let correctCount = 0;
    let answeredCount = 0;
    let bestStreak = 0;
    let currentStreak = 0;

    for (const question of graded) {
        const answer = answers[question.id];

        if (answer) {
            answeredCount += 1;
            earnedPoints += answer.pointsEarned;

            if (answer.isCorrect) {
                correctCount += 1;
                currentStreak += 1;
                bestStreak = Math.max(bestStreak, currentStreak);
            } else {
                currentStreak = 0;
            }
        } else {
            currentStreak = 0;
        }
    }

    const maxScore = graded.reduce(
        (total, question) => total + question.points,
        0,
    );
    const totalScore =
        maxScore > 0 ? Math.round((earnedPoints / maxScore) * 100) : 0;
    const started = new Date(startedAt).getTime();
    const finished = new Date(finishedAt).getTime();

    return {
        totalScore,
        earnedPoints,
        maxScore,
        correctCount,
        wrongCount: answeredCount - correctCount,
        unansweredCount: Math.max(0, graded.length - answeredCount),
        totalQuestions: graded.length,
        bestStreak,
        durationSeconds:
            Number.isFinite(started) && Number.isFinite(finished)
                ? Math.max(0, Math.round((finished - started) / 1000))
                : 0,
        isPassed: totalScore >= passingScore,
    };
}

export function buildSessionAnswers(
    questions: GameQuestion[],
    answers: Record<number, EvaluatedAnswer>,
): SessionAnswerPayload[] {
    return questions.flatMap((question) => {
        const answer = answers[question.id];

        if (!answer) {
            return [];
        }

        return [
            {
                question_id: question.id,
                user_answer: answer.response,
                time_spent: answer.timeSpent,
                answered_at: answer.answeredAt,
                is_correct: answer.isCorrect,
                points_earned: answer.pointsEarned,
            },
        ];
    });
}
