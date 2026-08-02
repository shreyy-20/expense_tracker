import React from 'react';
import { DollarSign, Receipt, TrendingUp, Tag } from 'lucide-react';
import { SummaryStats } from '../../types/expense';
import { formatCurrency } from '../../utils/formatters';
import { useCurrency } from '../../context/CurrencyContext';
import { Skeleton } from '../../components/ui/Skeleton';

interface StatCardsProps {
  stats?: SummaryStats;
  isLoading: boolean;
}

export const StatCards: React.FC<StatCardsProps> = ({ stats, isLoading }) => {
  const { currency } = useCurrency();

  if (isLoading || !stats) {
    return (
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {[1, 2, 3, 4].map((i) => (
          <Skeleton key={i} className="h-32 w-full rounded-2xl" />
        ))}
      </div>
    );
  }

  const cards = [
    {
      title: 'Total Expenses',
      value: formatCurrency(stats.total_amount, currency),
      subtitle: `${stats.total_count} total entries`,
      icon: DollarSign,
      color: 'bg-brand-500/10 text-brand-600 dark:text-brand-400',
    },
    {
      title: 'Average Expense',
      value: formatCurrency(stats.average_amount, currency),
      subtitle: 'Per transaction',
      icon: TrendingUp,
      color: 'bg-blue-500/10 text-blue-600 dark:text-blue-400',
    },
    {
      title: 'Total Transactions',
      value: stats.total_count.toString(),
      subtitle: 'Recorded expenses',
      icon: Receipt,
      color: 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400',
    },
    {
      title: 'Top Category',
      value: stats.top_category || 'N/A',
      subtitle: stats.highest_expense ? `Max: ${formatCurrency(stats.highest_expense.amount, currency)}` : 'No expenses yet',
      icon: Tag,
      color: 'bg-purple-500/10 text-purple-600 dark:text-purple-400',
    },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {cards.map((card) => {
        const Icon = card.icon;
        return (
          <div
            key={card.title}
            className="p-5 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-soft hover:shadow-medium transition-all"
          >
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">
                {card.title}
              </span>
              <div className={`p-2.5 rounded-xl ${card.color}`}>
                <Icon className="w-5 h-5" />
              </div>
            </div>
            <div className="text-2xl font-bold text-slate-900 dark:text-slate-100 tracking-tight">
              {card.value}
            </div>
            <p className="text-xs text-slate-400 dark:text-slate-500 mt-1">{card.subtitle}</p>
          </div>
        );
      })}
    </div>
  );
};
