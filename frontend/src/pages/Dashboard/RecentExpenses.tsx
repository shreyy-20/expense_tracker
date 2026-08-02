import React from 'react';
import { Expense } from '../../types/expense';
import { formatCurrency, formatDate } from '../../utils/formatters';
import { useCurrency } from '../../context/CurrencyContext';
import { Badge } from '../../components/ui/Badge';

interface RecentExpensesProps {
  expenses?: Expense[];
  isLoading: boolean;
}

export const RecentExpenses: React.FC<RecentExpensesProps> = ({ expenses, isLoading }) => {
  const { currency } = useCurrency();

  if (isLoading) {
    return null;
  }

  if (!expenses || expenses.length === 0) {
    return null;
  }

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft">
      <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100 mb-4">
        Recent Expenses
      </h3>
      <div className="divide-y divide-slate-100 dark:divide-slate-800">
        {expenses.slice(0, 5).map((exp) => (
          <div key={exp.id} className="py-3 flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-slate-900 dark:text-slate-100">{exp.title}</p>
              <p className="text-xs text-slate-400">{formatDate(exp.date)}</p>
            </div>
            <div className="flex items-center gap-3">
              <Badge category={exp.category} />
              <span className="text-sm font-semibold text-slate-900 dark:text-slate-100">
                {formatCurrency(exp.amount, currency)}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
