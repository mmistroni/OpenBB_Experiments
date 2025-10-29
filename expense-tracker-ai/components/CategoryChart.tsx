'use client';

import { Category, CATEGORY_COLORS, CATEGORY_ICONS } from '@/types/expense';
import { formatCurrency } from '@/lib/analytics';
import Card from './ui/Card';

interface CategoryChartProps {
  categoryBreakdown: Record<Category, number>;
  total: number;
}

export default function CategoryChart({ categoryBreakdown, total }: CategoryChartProps) {
  // Sort categories by amount (descending)
  const sortedCategories = (Object.keys(categoryBreakdown) as Category[])
    .filter(cat => categoryBreakdown[cat] > 0)
    .sort((a, b) => categoryBreakdown[b] - categoryBreakdown[a]);

  if (sortedCategories.length === 0) {
    return (
      <Card>
        <h3 className="text-lg font-bold text-secondary-900 mb-4">Spending by Category</h3>
        <div className="text-center py-12 text-secondary-500">
          No expenses recorded yet
        </div>
      </Card>
    );
  }

  return (
    <Card>
      <h3 className="text-lg font-bold text-secondary-900 mb-4">Spending by Category</h3>
      <div className="space-y-4">
        {sortedCategories.map((category) => {
          const amount = categoryBreakdown[category];
          const percentage = total > 0 ? (amount / total) * 100 : 0;

          return (
            <div key={category}>
              <div className="flex items-center justify-between mb-1">
                <div className="flex items-center gap-2">
                  <span className="text-lg">{CATEGORY_ICONS[category]}</span>
                  <span className="text-sm font-medium text-secondary-700">{category}</span>
                </div>
                <div className="text-right">
                  <p className="text-sm font-semibold text-secondary-900">
                    {formatCurrency(amount)}
                  </p>
                  <p className="text-xs text-secondary-500">
                    {percentage.toFixed(1)}%
                  </p>
                </div>
              </div>
              <div className="w-full bg-secondary-200 rounded-full h-2 overflow-hidden">
                <div
                  className="h-full rounded-full transition-all duration-500"
                  style={{
                    width: `${percentage}%`,
                    backgroundColor: CATEGORY_COLORS[category],
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </Card>
  );
}
