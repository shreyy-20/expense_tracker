import React from 'react';
import { Expense } from '../../types/expense';
import { ExpenseRow } from './ExpenseRow';
import { Skeleton } from '../../components/ui/Skeleton';
import { EmptyState } from '../../components/ui/EmptyState';
import { Receipt } from 'lucide-react';

interface ExpenseTableProps {
  expenses?: Expense[];
  isLoading: boolean;
  selectedIds: string[];
  onToggleSelectAll: () => void;
  onToggleSelect: (id: string) => void;
  onEdit: (expense: Expense) => void;
  onDelete: (id: string) => void;
  onAddFirst: () => void;
}

export const ExpenseTable: React.FC<ExpenseTableProps> = ({
  expenses,
  isLoading,
  selectedIds,
  onToggleSelectAll,
  onToggleSelect,
  onEdit,
  onDelete,
  onAddFirst,
}) => {
  if (isLoading) {
    return (
      <div className="p-4 space-y-3 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800">
        {[1, 2, 3, 4, 5].map((i) => (
          <Skeleton key={i} className="h-12 w-full" />
        ))}
      </div>
    );
  }

  if (!expenses || expenses.length === 0) {
    return (
      <EmptyState
        icon={Receipt}
        title="No expenses found"
        description="Get started by adding your first expense or clear search filters."
        actionLabel="Add Expense"
        onAction={onAddFirst}
      />
    );
  }

  const isAllSelected = expenses.length > 0 && selectedIds.length === expenses.length;

  return (
    <div className="overflow-x-auto bg-white dark:bg-slate-900 rounded-t-2xl border border-slate-200 dark:border-slate-800 border-b-0">
      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="border-b border-slate-200 dark:border-slate-800 text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 bg-slate-50/50 dark:bg-slate-800/30">
            <th className="p-4 w-10">
              <input
                type="checkbox"
                checked={isAllSelected}
                onChange={onToggleSelectAll}
                className="rounded border-slate-300 dark:border-slate-700 text-brand-600 focus:ring-brand-500"
              />
            </th>
            <th className="p-4">Title</th>
            <th className="p-4">Category</th>
            <th className="p-4">Date</th>
            <th className="p-4 text-right">Amount</th>
            <th className="p-4 text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {expenses.map((exp) => (
            <ExpenseRow
              key={exp.id}
              expense={exp}
              isSelected={selectedIds.includes(exp.id)}
              onToggleSelect={onToggleSelect}
              onEdit={onEdit}
              onDelete={onDelete}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
};
