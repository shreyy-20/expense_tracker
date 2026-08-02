import React from 'react';
import { SearchInput } from '../../components/ui/SearchInput';
import { Select } from '../../components/ui/Select';
import { useCategories } from '../../hooks/useExpenses';
import { DEFAULT_CATEGORIES } from '../../utils/constants';

interface ExpenseFiltersProps {
  search: string;
  onSearchChange: (val: string) => void;
  category: string;
  onCategoryChange: (val: string) => void;
  sortBy: string;
  onSortByChange: (val: string) => void;
  sortOrder: string;
  onSortOrderChange: (val: string) => void;
}

export const ExpenseFilters: React.FC<ExpenseFiltersProps> = ({
  search,
  onSearchChange,
  category,
  onCategoryChange,
  sortBy,
  onSortByChange,
  sortOrder,
  onSortOrderChange,
}) => {
  const { data: categoriesList } = useCategories();
  const categories = categoriesList && categoriesList.length > 0 ? categoriesList : DEFAULT_CATEGORIES;

  const categoryOptions = [
    { value: '', label: 'All Categories' },
    ...categories.map((c) => ({ value: c, label: c })),
  ];

  const sortOptions = [
    { value: 'date', label: 'Sort by Date' },
    { value: 'amount', label: 'Sort by Amount' },
    { value: 'title', label: 'Sort by Title' },
    { value: 'category', label: 'Sort by Category' },
  ];

  return (
    <div className="flex flex-col md:flex-row gap-3 items-stretch md:items-center justify-between p-4 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft">
      <div className="flex-1 max-w-md">
        <SearchInput value={search} onChangeValue={onSearchChange} />
      </div>
      <div className="flex items-center gap-3">
        <Select
          value={category}
          onChange={(e) => onCategoryChange(e.target.value)}
          options={categoryOptions}
          className="w-40"
        />
        <Select
          value={sortBy}
          onChange={(e) => onSortByChange(e.target.value)}
          options={sortOptions}
          className="w-40"
        />
        <Select
          value={sortOrder}
          onChange={(e) => onSortOrderChange(e.target.value)}
          options={[
            { value: 'desc', label: 'Descending' },
            { value: 'asc', label: 'Ascending' },
          ]}
          className="w-32"
        />
      </div>
    </div>
  );
};
