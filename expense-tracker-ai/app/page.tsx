'use client';

import { useState, useEffect } from 'react';
import { storageUtils } from '@/lib/storage';
import { calculateSummary, formatCurrency } from '@/lib/analytics';
import { Expense } from '@/types/expense';
import SummaryCard from '@/components/SummaryCard';
import CategoryChart from '@/components/CategoryChart';
import ExpenseForm from '@/components/ExpenseForm';
import LoadingSpinner from '@/components/ui/LoadingSpinner';

export default function DashboardPage() {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    loadExpenses();
  }, []);

  const loadExpenses = () => {
    setIsLoading(true);
    const data = storageUtils.getExpenses();
    setExpenses(data);
    setIsLoading(false);
  };

  const handleAddExpense = (expenseData: Omit<Expense, 'id' | 'createdAt' | 'updatedAt'>) => {
    storageUtils.addExpense(expenseData);
    loadExpenses();
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[50vh]">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  const summary = calculateSummary(expenses);

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold text-secondary-900 mb-2">Dashboard</h1>
        <p className="text-secondary-600">Track and manage your expenses</p>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <SummaryCard
          title="Total Spending"
          value={formatCurrency(summary.total)}
          icon="💵"
          color="blue"
        />
        <SummaryCard
          title="This Month"
          value={formatCurrency(summary.monthlyTotal)}
          icon="📅"
          color="green"
        />
        <SummaryCard
          title="Average Expense"
          value={formatCurrency(summary.averageExpense)}
          icon="📊"
          color="purple"
        />
        <SummaryCard
          title="Total Expenses"
          value={summary.expenseCount.toString()}
          icon="🧾"
          color="orange"
        />
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Add Expense Form */}
        <div>
          <ExpenseForm onSubmit={handleAddExpense} />
        </div>

        {/* Category Breakdown */}
        <div>
          <CategoryChart
            categoryBreakdown={summary.categoryBreakdown}
            total={summary.total}
          />
        </div>
      </div>

      {/* Top Category */}
      {summary.topCategory && (
        <div className="bg-gradient-to-r from-primary-50 to-primary-100 rounded-lg p-6 border border-primary-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-primary-600 mb-1">Top Spending Category</p>
              <p className="text-2xl font-bold text-primary-900">{summary.topCategory.category}</p>
            </div>
            <div className="text-right">
              <p className="text-3xl font-bold text-primary-700">
                {formatCurrency(summary.topCategory.amount)}
              </p>
              <p className="text-sm text-primary-600">
                {((summary.topCategory.amount / summary.total) * 100).toFixed(1)}% of total
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
