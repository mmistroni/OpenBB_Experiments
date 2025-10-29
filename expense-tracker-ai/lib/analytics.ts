import { Expense, ExpenseSummary, Category, CATEGORIES } from '@/types/expense';
import { startOfMonth, endOfMonth, isWithinInterval, parseISO } from 'date-fns';

/**
 * Calculate expense summary and analytics
 */
export function calculateSummary(expenses: Expense[]): ExpenseSummary {
  const now = new Date();
  const monthStart = startOfMonth(now);
  const monthEnd = endOfMonth(now);

  // Filter expenses for current month
  const monthlyExpenses = expenses.filter(expense => {
    const expenseDate = parseISO(expense.date);
    return isWithinInterval(expenseDate, { start: monthStart, end: monthEnd });
  });

  // Calculate total
  const total = expenses.reduce((sum, expense) => sum + expense.amount, 0);
  const monthlyTotal = monthlyExpenses.reduce((sum, expense) => sum + expense.amount, 0);

  // Calculate category breakdown
  const categoryBreakdown: Record<Category, number> = {
    Food: 0,
    Transportation: 0,
    Entertainment: 0,
    Shopping: 0,
    Bills: 0,
    Other: 0,
  };

  expenses.forEach(expense => {
    categoryBreakdown[expense.category] += expense.amount;
  });

  // Find top category
  let topCategory: ExpenseSummary['topCategory'] = null;
  let maxAmount = 0;

  CATEGORIES.forEach(category => {
    if (categoryBreakdown[category] > maxAmount) {
      maxAmount = categoryBreakdown[category];
      topCategory = { category, amount: maxAmount };
    }
  });

  // Calculate average
  const averageExpense = expenses.length > 0 ? total / expenses.length : 0;

  return {
    total,
    monthlyTotal,
    categoryBreakdown,
    topCategory,
    averageExpense,
    expenseCount: expenses.length,
  };
}

/**
 * Format currency amount
 */
export function formatCurrency(amount: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(amount);
}

/**
 * Export expenses to CSV
 */
export function exportToCSV(expenses: Expense[]): void {
  if (expenses.length === 0) {
    alert('No expenses to export');
    return;
  }

  // CSV headers
  const headers = ['Date', 'Category', 'Amount', 'Description'];

  // CSV rows
  const rows = expenses.map(expense => [
    expense.date,
    expense.category,
    expense.amount.toString(),
    `"${expense.description.replace(/"/g, '""')}"`, // Escape quotes in description
  ]);

  // Combine headers and rows
  const csvContent = [
    headers.join(','),
    ...rows.map(row => row.join(',')),
  ].join('\n');

  // Create blob and download
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement('a');
  const url = URL.createObjectURL(blob);

  link.setAttribute('href', url);
  link.setAttribute('download', `expenses-${new Date().toISOString().split('T')[0]}.csv`);
  link.style.visibility = 'hidden';

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
