export type MembershipTier = 'free' | 'standard' | 'professional' | 'enterprise';

export type MembershipStatus = 'pending' | 'active' | 'expired' | 'rejected';

export type BillingCycle = 'monthly' | 'yearly';

export interface MembershipInfo {
    plan_slug: string | null;
    plan_name: string;
    tier: MembershipTier;
    status: 'free' | 'active';
    ends_at: string | null;
}

export interface MembershipPlan {
    id: number;
    slug: string;
    name: string;
    tier: MembershipTier;
    tagline: string | null;
    price_monthly: number;
    price_yearly: number;
    features: string[];
    is_featured: boolean;
}

export interface MembershipRecord {
    id: number;
    plan_name: string | null;
    plan_slug: string | null;
    tier: MembershipTier | null;
    billing_cycle: BillingCycle;
    amount: number;
    status: MembershipStatus;
    status_label: string;
    reference: string;
    note: string | null;
    admin_note: string | null;
    created_at: string | null;
    starts_at: string | null;
    ends_at: string | null;
}

export interface AuthUser {
    id: number;
    name: string;
    username: string;
    email: string | null;
    role: 'student' | 'teacher' | 'admin';
    xp: number;
    level: number;
    coins: number;
    avatar: string | null;
    class_id: number | null;
    class_name: string | null;
    education_level: string | null;
    education_level_slug: string | null;
    level_theme: string;
    membership: MembershipInfo;
}

export interface FlashMessage {
    success?: string | null;
    error?: string | null;
    info?: string | null;
}

export type PageProps<
    T extends Record<string, unknown> = Record<string, unknown>,
> = T & {
    version: string;
    app: {
        name: string;
        locale: string;
        env: string;
    };
    auth: {
        user: AuthUser | null;
    };
    flash: FlashMessage;
};
