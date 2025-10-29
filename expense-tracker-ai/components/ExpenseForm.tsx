'use client';

import { useState, useEffect } from 'react';
import { Category, CATEGORIES, Expense } from '@/types/expense';
import Input from './ui/Input';
import Select from './ui/Select';
import Button from './ui/Button';
import Card from './ui/Card';

interface ExpenseFormProps {
  onSubmit: (expense: Omit<Expense, 'id' | 'createdAt' | 'updatedAt'>) => void;
  initialData?: Expense;
  onCancel?: () => void;
}

export default function ExpenseForm({ onSubmit, initialData, onCancel }: ExpenseFormProps) {
  const [formData, setFormData] = useState({
    date: initialData?.date || new Date().toISOString().split('T')[0],
    amount: initialData?.amount?.toString() || '',
    category: initialData?.category || 'Food' as Category,
    description: initialData?.description || '',
  });

  const [errors, setErrors] = useState({
    date: '',
    amount: '',
    description: '',
  });

  const [isSubmitting, setIsSubmitting] = useState(false);

  const validateForm = (): boolean => {
    const newErrors = {
      date: '',
      amount: '',
      description: '',
    };

    let isValid = true;

    // Validate date
    if (!formData.date) {
      newErrors.date = 'Date is required';
      isValid = false;
    }

    // Validate amount
    if (!formData.amount) {
      newErrors.amount = 'Amount is required';
      isValid = false;
    } else if (isNaN(Number(formData.amount)) || Number(formData.amount) <= 0) {
      newErrors.amount = 'Amount must be a positive number';
      isValid = false;
    }

    // Validate description
    if (!formData.description.trim()) {
      newErrors.description = 'Description is required';
      isValid = false;
    } else if (formData.description.trim().length < 3) {
      newErrors.description = 'Description must be at least 3 characters';
      isValid = false;
    }

    setErrors(newErrors);
    return isValid;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setIsSubmitting(true);

    try {
      onSubmit({
        date: formData.date,
        amount: Number(formData.amount),
        category: formData.category,
        description: formData.description.trim(),
      });

      // Reset form if not editing
      if (!initialData) {
        setFormData({
          date: new Date().toISOString().split('T')[0],
          amount: '',
          category: 'Food',
          description: '',
        });
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const categoryOptions = CATEGORIES.map(cat => ({
    value: cat,
    label: cat,
  }));

  return (
    <Card>
      <h2 className="text-xl font-bold text-secondary-900 mb-6">
        {initialData ? 'Edit Expense' : 'Add New Expense'}
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Input
            type="date"
            label="Date"
            value={formData.date}
            onChange={(e) => setFormData({ ...formData, date: e.target.value })}
            error={errors.date}
            max={new Date().toISOString().split('T')[0]}
          />

          <Input
            type="number"
            label="Amount ($)"
            placeholder="0.00"
            step="0.01"
            value={formData.amount}
            onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
            error={errors.amount}
          />
        </div>

        <Select
          label="Category"
          value={formData.category}
          onChange={(e) => setFormData({ ...formData, category: e.target.value as Category })}
          options={categoryOptions}
        />

        <Input
          type="text"
          label="Description"
          placeholder="What was this expense for?"
          value={formData.description}
          onChange={(e) => setFormData({ ...formData, description: e.target.value })}
          error={errors.description}
          maxLength={200}
        />

        <div className="flex gap-3 pt-4">
          <Button
            type="submit"
            disabled={isSubmitting}
            className="flex-1"
          >
            {isSubmitting ? 'Saving...' : (initialData ? 'Update Expense' : 'Add Expense')}
          </Button>

          {onCancel && (
            <Button
              type="button"
              variant="secondary"
              onClick={onCancel}
            >
              Cancel
            </Button>
          )}
        </div>
      </form>
    </Card>
  );
}
