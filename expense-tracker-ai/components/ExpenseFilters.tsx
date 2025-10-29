'use client';

import { Category, CATEGORIES } from '@/types/expense';
import Input from './ui/Input';
import Select from './ui/Select';
import Button from './ui/Button';
import Card from './ui/Card';

interface ExpenseFiltersProps {
  searchQuery: string;
  category: Category | 'All';
  startDate: string;
  endDate: string;
  onSearchChange: (query: string) => void;
  onCategoryChange: (category: Category | 'All') => void;
  onStartDateChange: (date: string) => void;
  onEndDateChange: (date: string) => void;
  onReset: () => void;
}

export default function ExpenseFilters({
  searchQuery,
  category,
  startDate,
  endDate,
  onSearchChange,
  onCategoryChange,
  onStartDateChange,
  onEndDateChange,
  onReset,
}: ExpenseFiltersProps) {
  const categoryOptions = [
    { value: 'All', label: 'All Categories' },
    ...CATEGORIES.map(cat => ({ value: cat, label: cat })),
  ];

  return (
    <Card>
      <div className="space-y-4">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-bold text-secondary-900">Filters</h3>
          <Button variant="outline" size="sm" onClick={onReset}>
            Reset
          </Button>
        </div>

        <Input
          type="text"
          placeholder="Search expenses..."
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
        />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Select
            label="Category"
            value={category}
            onChange={(e) => onCategoryChange(e.target.value as Category | 'All')}
            options={categoryOptions}
          />

          <Input
            type="date"
            label="Start Date"
            value={startDate}
            onChange={(e) => onStartDateChange(e.target.value)}
          />

          <Input
            type="date"
            label="End Date"
            value={endDate}
            onChange={(e) => onEndDateChange(e.target.value)}
          />
        </div>
      </div>
    </Card>
  );
}
