import { Expense } from '@/types/expense';

const STORAGE_KEY = 'expense-tracker-expenses';

export const storageUtils = {
  /**
   * Get all expenses from localStorage
   */
  getExpenses: (): Expense[] => {
    if (typeof window === 'undefined') return [];

    try {
      const data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return [];
    }
  },

  /**
   * Save all expenses to localStorage
   */
  saveExpenses: (expenses: Expense[]): void => {
    if (typeof window === 'undefined') return;

    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(expenses));
    } catch (error) {
      console.error('Error writing to localStorage:', error);
    }
  },

  /**
   * Add a new expense
   */
  addExpense: (expense: Omit<Expense, 'id' | 'createdAt' | 'updatedAt'>): Expense => {
    const expenses = storageUtils.getExpenses();
    const now = new Date().toISOString();

    const newExpense: Expense = {
      ...expense,
      id: crypto.randomUUID(),
      createdAt: now,
      updatedAt: now,
    };

    expenses.push(newExpense);
    storageUtils.saveExpenses(expenses);

    return newExpense;
  },

  /**
   * Update an existing expense
   */
  updateExpense: (id: string, updates: Partial<Omit<Expense, 'id' | 'createdAt' | 'updatedAt'>>): Expense | null => {
    const expenses = storageUtils.getExpenses();
    const index = expenses.findIndex(e => e.id === id);

    if (index === -1) return null;

    const updatedExpense: Expense = {
      ...expenses[index],
      ...updates,
      updatedAt: new Date().toISOString(),
    };

    expenses[index] = updatedExpense;
    storageUtils.saveExpenses(expenses);

    return updatedExpense;
  },

  /**
   * Delete an expense
   */
  deleteExpense: (id: string): boolean => {
    const expenses = storageUtils.getExpenses();
    const filtered = expenses.filter(e => e.id !== id);

    if (filtered.length === expenses.length) return false;

    storageUtils.saveExpenses(filtered);
    return true;
  },

  /**
   * Get a single expense by ID
   */
  getExpenseById: (id: string): Expense | null => {
    const expenses = storageUtils.getExpenses();
    return expenses.find(e => e.id === id) || null;
  },

  /**
   * Clear all expenses
   */
  clearAllExpenses: (): void => {
    if (typeof window === 'undefined') return;
    localStorage.removeItem(STORAGE_KEY);
  },
};
