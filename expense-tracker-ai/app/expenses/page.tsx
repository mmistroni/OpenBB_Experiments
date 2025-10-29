'use client';

import { useState, useEffect, useMemo } from 'react';
import { parseISO, isWithinInterval } from 'date-fns';
import { storageUtils } from '@/lib/storage';
import { exportToCSV, formatCurrency } from '@/lib/analytics';
import { Expense, Category } from '@/types/expense';
import ExpenseFilters from '@/components/ExpenseFilters';
import ExpenseListItem from '@/components/ExpenseListItem';
import ExpenseForm from '@/components/ExpenseForm';
import Button from '@/components/ui/Button';
import Card from '@/components/ui/Card';
import LoadingSpinner from '@/components/ui/LoadingSpinner';

export default function ExpensesPage() {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [editingExpense, setEditingExpense] = useState<Expense | null>(null);

  // Filter states
  const [searchQuery, setSearchQuery] = useState('');
  const [categoryFilter, setCategoryFilter] = useState<Category | 'All'>('All');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

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

  const handleUpdateExpense = (expenseData: Omit<Expense, 'id' | 'createdAt' | 'updatedAt'>) => {
    if (editingExpense) {
      storageUtils.updateExpense(editingExpense.id, expenseData);
      setEditingExpense(null);
      loadExpenses();
    }
  };

  const handleDeleteExpense = (id: string) => {
    storageUtils.deleteExpense(id);
    loadExpenses();
  };

  const handleResetFilters = () => {
    setSearchQuery('');
    setCategoryFilter('All');
    setStartDate('');
    setEndDate('');
  };

  const handleExport = () => {
    exportToCSV(filteredExpenses);
  };

  // Filter expenses
  const filteredExpenses = useMemo(() => {
    return expenses.filter(expense => {
      // Search filter
      if (searchQuery && !expense.description.toLowerCase().includes(searchQuery.toLowerCase())) {
        return false;
      }

      // Category filter
      if (categoryFilter !== 'All' && expense.category !== categoryFilter) {
        return false;
      }

      // Date range filter
      if (startDate || endDate) {
        const expenseDate = parseISO(expense.date);

        if (startDate && endDate) {
          const start = parseISO(startDate);
          const end = parseISO(endDate);
          if (!isWithinInterval(expenseDate, { start, end })) {
            return false;
          }
        } else if (startDate) {
          const start = parseISO(startDate);
          if (expenseDate < start) {
            return false;
          }
        } else if (endDate) {
          const end = parseISO(endDate);
          if (expenseDate > end) {
            return false;
          }
        }
      }

      return true;
    }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }, [expenses, searchQuery, categoryFilter, startDate, endDate]);

  const totalFiltered = filteredExpenses.reduce((sum, exp) => sum + exp.amount, 0);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[50vh]">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-secondary-900 mb-2">Expenses</h1>
          <p className="text-secondary-600">View and manage all your expenses</p>
        </div>
        <Button onClick={handleExport} variant="outline">
          📥 Export CSV
        </Button>
      </div>

      {/* Add/Edit Expense Form */}
      {editingExpense ? (
        <ExpenseForm
          initialData={editingExpense}
          onSubmit={handleUpdateExpense}
          onCancel={() => setEditingExpense(null)}
        />
      ) : (
        <ExpenseForm onSubmit={handleAddExpense} />
      )}

      {/* Filters */}
      <ExpenseFilters
        searchQuery={searchQuery}
        category={categoryFilter}
        startDate={startDate}
        endDate={endDate}
        onSearchChange={setSearchQuery}
        onCategoryChange={setCategoryFilter}
        onStartDateChange={setStartDate}
        onEndDateChange={setEndDate}
        onReset={handleResetFilters}
      />

      {/* Results Summary */}
      <div className="flex items-center justify-between px-4">
        <p className="text-secondary-600">
          Showing <span className="font-semibold">{filteredExpenses.length}</span> of{' '}
          <span className="font-semibold">{expenses.length}</span> expenses
        </p>
        <p className="text-lg font-semibold text-secondary-900">
          Total: {formatCurrency(totalFiltered)}
        </p>
      </div>

      {/* Expense List */}
      {filteredExpenses.length === 0 ? (
        <Card>
          <div className="text-center py-12">
            <p className="text-2xl mb-2">📭</p>
            <p className="text-secondary-500">
              {expenses.length === 0
                ? 'No expenses yet. Add your first expense above!'
                : 'No expenses match your filters'}
            </p>
          </div>
        </Card>
      ) : (
        <div className="space-y-3">
          {filteredExpenses.map(expense => (
            <ExpenseListItem
              key={expense.id}
              expense={expense}
              onEdit={setEditingExpense}
              onDelete={handleDeleteExpense}
            />
          ))}
        </div>
      )}
    </div>
  );
}
