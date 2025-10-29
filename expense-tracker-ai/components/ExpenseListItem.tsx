'use client';

import { Expense, CATEGORY_ICONS, CATEGORY_COLORS } from '@/types/expense';
import { formatCurrency } from '@/lib/analytics';
import { format } from 'date-fns';
import Button from './ui/Button';

interface ExpenseListItemProps {
  expense: Expense;
  onEdit: (expense: Expense) => void;
  onDelete: (id: string) => void;
}

export default function ExpenseListItem({ expense, onEdit, onDelete }: ExpenseListItemProps) {
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this expense?')) {
      onDelete(expense.id);
    }
  };

  return (
    <div className="bg-white border border-slate-200 rounded-lg p-4 hover:shadow-md transition-shadow">
      <div className="flex items-start justify-between">
        <div className="flex items-start gap-3 flex-1">
          <div
            className="p-2 rounded-lg text-2xl"
            style={{ backgroundColor: `${CATEGORY_COLORS[expense.category]}20` }}
          >
            {CATEGORY_ICONS[expense.category]}
          </div>

          <div className="flex-1 min-w-0">
            <div className="flex items-start justify-between gap-2 mb-1">
              <h4 className="font-semibold text-secondary-900 truncate">
                {expense.description}
              </h4>
              <p className="font-bold text-lg text-secondary-900 whitespace-nowrap">
                {formatCurrency(expense.amount)}
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-3 text-sm text-secondary-600">
              <span className="flex items-center gap-1">
                📅 {format(new Date(expense.date), 'MMM dd, yyyy')}
              </span>
              <span
                className="px-2 py-0.5 rounded-full text-xs font-medium"
                style={{
                  backgroundColor: `${CATEGORY_COLORS[expense.category]}20`,
                  color: CATEGORY_COLORS[expense.category],
                }}
              >
                {expense.category}
              </span>
            </div>
          </div>
        </div>

        <div className="flex gap-2 ml-4">
          <Button
            variant="outline"
            size="sm"
            onClick={() => onEdit(expense)}
          >
            Edit
          </Button>
          <Button
            variant="danger"
            size="sm"
            onClick={handleDelete}
          >
            Delete
          </Button>
        </div>
      </div>
    </div>
  );
}
