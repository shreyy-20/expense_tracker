import React, { useState } from 'react';
import { Plus, X } from 'lucide-react';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { useCategories, useAddCategory, useRemoveCategory } from '../../hooks/useExpenses';
import { DEFAULT_CATEGORIES } from '../../utils/constants';

export const CategoryManager: React.FC = () => {
  const [newCategory, setNewCategory] = useState('');
  const { data: categoriesList } = useCategories();
  const categories = categoriesList && categoriesList.length > 0 ? categoriesList : DEFAULT_CATEGORIES;

  const addMutation = useAddCategory();
  const removeMutation = useRemoveCategory();

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newCategory.trim()) return;
    await addMutation.mutateAsync(newCategory.trim());
    setNewCategory('');
  };

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft space-y-4">
      <div>
        <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100">
          Category Manager
        </h3>
        <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
          Add custom categories to organize your expenses.
        </p>
      </div>

      <form onSubmit={handleAdd} className="flex gap-3">
        <input
          type="text"
          value={newCategory}
          onChange={(e) => setNewCategory(e.target.value)}
          placeholder="New Category Name..."
          className="flex-1 px-3 py-2 text-sm bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 text-slate-900 dark:text-slate-100"
        />
        <Button type="submit" isLoading={addMutation.isPending} icon={<Plus className="w-4 h-4" />}>
          Add Category
        </Button>
      </form>

      <div className="flex flex-wrap gap-2 pt-2">
        {categories.map((cat) => (
          <div key={cat} className="inline-flex items-center gap-1">
            <Badge category={cat} />
            <button
              onClick={() => removeMutation.mutate(cat)}
              className="p-0.5 text-slate-400 hover:text-red-500 transition-colors"
              title="Remove Category"
            >
              <X className="w-3 h-3" />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
