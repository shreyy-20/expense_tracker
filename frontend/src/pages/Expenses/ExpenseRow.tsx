import React from 'react';
import { Pencil, Trash2 } from 'lucide-react';
import { Expense } from '../../types/expense';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { useCurrency } from '../../context/CurrencyContext';
import { Badge } from '../../components/ui/Badge';

interface ExpenseRowProps {
  expense: Expense;
  isSelected: boolean;
  onToggleSelect: (id: string) => void;
  onEdit: (expense: Expense) => void;
  onDelete: (id: string) => void;
}

export const ExpenseRow: React.FC<ExpenseRowProps> = ({
  expense,
  isSelected,
  onToggleSelect,
  onEdit,
  onDelete,
}) => {
  const { currency } = useCurrency();

  return (
    <tr className="hover:bg-slate-50/80 dark:hover:bg-slate-800/40 transition-colors group border-b border-slate-100 dark:border-slate-800">
      <td className="p-4 w-10">
        <input
          type="checkbox"
          checked={isSelected}
          onChange={() => onToggleSelect(expense.id)}
          className="rounded border-slate-300 dark:border-slate-700 text-brand-600 focus:ring-brand-500"
        />
      </td>
      <td className="p-4">
        <div className="font-medium text-sm text-slate-900 dark:text-slate-100">{expense.title}</div>
      </td>
      <td className="p-4">
        <Badge category={expense.category} />
      </td>
      <td className="p-4 text-xs text-slate-500 dark:text-slate-400">
        {formatDate(expense.date)}
      </td>
      <td className="p-4 font-semibold text-sm text-slate-900 dark:text-slate-100 text-right">
        {formatCurrency(expense.amount, currency)}
      </td>
      <td className="p-4 text-right">
        <div className="flex items-center justify-end gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
          <button
            onClick={() => onEdit(expense)}
            className="p-1.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg"
          >
            <Pencil className="w-4 h-4" />
          </button>
          <button
            onClick={() => onDelete(expense.id)}
            className="p-1.5 text-slate-400 hover:text-red-600 dark:hover:text-red-400 hover:bg-red-50 dark:hover:bg-red-950/40 rounded-lg"
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </td>
    </tr>
  );
};
