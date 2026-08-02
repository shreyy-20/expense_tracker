import React, { useEffect, useState } from 'react';
import { Modal } from '../../components/ui/Modal';
import { Button } from '../../components/ui/Button';
import { Select } from '../../components/ui/Select';
import { Expense, ExpenseCreateInput } from '../../types/expense';
import { useCategories } from '../../hooks/useExpenses';
import { DEFAULT_CATEGORIES } from '../../utils/constants';

interface ExpenseFormProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (data: ExpenseCreateInput) => Promise<void>;
  initialData?: Expense | null;
  isLoading?: boolean;
}

export const ExpenseForm: React.FC<ExpenseFormProps> = ({
  isOpen,
  onClose,
  onSubmit,
  initialData,
  isLoading = false,
}) => {
  const { data: categoriesList } = useCategories();
  const categories = categoriesList && categoriesList.length > 0 ? categoriesList : DEFAULT_CATEGORIES;

  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState(categories[0] || 'Food & Dining');
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [errors, setErrors] = useState<Record<string, string>>({});

  useEffect(() => {
    if (initialData) {
      setTitle(initialData.title);
      setAmount(initialData.amount.toString());
      setCategory(initialData.category);
      setDate(initialData.date);
    } else {
      setTitle('');
      setAmount('');
      setCategory(categories[0] || 'Food & Dining');
      setDate(new Date().toISOString().split('T')[0]);
    }
    setErrors({});
  }, [initialData, isOpen, categories]);

  const validate = (): boolean => {
    const newErrors: Record<string, string> = {};
    if (!title.trim()) newErrors.title = 'Title is required';
    if (!amount || isNaN(Number(amount)) || Number(amount) <= 0) {
      newErrors.amount = 'Amount must be a positive number';
    }
    if (!category) newErrors.category = 'Category is required';
    if (!date) newErrors.date = 'Date is required';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validate()) return;
    await onSubmit({
      title: title.trim(),
      amount: parseFloat(amount),
      category,
      date,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={initialData ? 'Edit Expense' : 'Add New Expense'}
      description="Enter the transaction details below."
    >
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">
            Title
          </label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g. Grocery Store"
            className="w-full px-3 py-2 text-sm bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-900 dark:text-slate-100"
          />
          {errors.title && <p className="text-xs text-red-500 mt-1">{errors.title}</p>}
        </div>

        <div>
          <label className="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">
            Amount
          </label>
          <input
            type="number"
            step="0.01"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="0.00"
            className="w-full px-3 py-2 text-sm bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-900 dark:text-slate-100"
          />
          {errors.amount && <p className="text-xs text-red-500 mt-1">{errors.amount}</p>}
        </div>

        <Select
          label="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          options={categories.map((c) => ({ value: c, label: c }))}
        />

        <div>
          <label className="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">
            Date
          </label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            className="w-full px-3 py-2 text-sm bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-900 dark:text-slate-100"
          />
          {errors.date && <p className="text-xs text-red-500 mt-1">{errors.date}</p>}
        </div>

        <div className="flex justify-end gap-3 pt-4 border-t border-slate-100 dark:border-slate-800">
          <Button type="button" variant="outline" onClick={onClose} disabled={isLoading}>
            Cancel
          </Button>
          <Button type="submit" isLoading={isLoading}>
            {initialData ? 'Save Changes' : 'Add Expense'}
          </Button>
        </div>
      </form>
    </Modal>
  );
};
