export type Category =
  | 'Food'
  | 'Transportation'
  | 'Entertainment'
  | 'Shopping'
  | 'Bills'
  | 'Other';

export interface Expense {
  id: string;
  date: string; // ISO date string
  amount: number;
  category: Category;
  description: string;
  createdAt: string;
  updatedAt: string;
}

export interface ExpenseFormData {
  date: string;
  amount: string;
  category: Category;
  description: string;
}

export interface ExpenseFilters {
  category?: Category | 'All';
  startDate?: string;
  endDate?: string;
  searchQuery?: string;
}

export interface ExpenseSummary {
  total: number;
  monthlyTotal: number;
  categoryBreakdown: Record<Category, number>;
  topCategory: {
    category: Category;
    amount: number;
  } | null;
  averageExpense: number;
  expenseCount: number;
}

export const CATEGORIES: Category[] = [
  'Food',
  'Transportation',
  'Entertainment',
  'Shopping',
  'Bills',
  'Other',
];

export const CATEGORY_COLORS: Record<Category, string> = {
  Food: '#ef4444',
  Transportation: '#3b82f6',
  Entertainment: '#8b5cf6',
  Shopping: '#ec4899',
  Bills: '#f59e0b',
  Other: '#6b7280',
};

export const CATEGORY_ICONS: Record<Category, string> = {
  Food: '🍽️',
  Transportation: '🚗',
  Entertainment: '🎬',
  Shopping: '🛍️',
  Bills: '💰',
  Other: '📦',
};
