import React from 'react';
import { StatCards } from './StatCards';
import { MonthlyChart } from './MonthlyChart';
import { CategoryChart } from './CategoryChart';
import { RecentExpenses } from './RecentExpenses';
import { useSummaryStats, useMonthlyStats, useCategoryStats } from '../../hooks/useStats';
import { useExpenses } from '../../hooks/useExpenses';

export const Dashboard: React.FC = () => {
  const { data: summary, isLoading: isSummaryLoading } = useSummaryStats();
  const { data: monthly, isLoading: isMonthlyLoading } = useMonthlyStats();
  const { data: categories, isLoading: isCategoriesLoading } = useCategoryStats();
  const { data: expensesData, isLoading: isExpensesLoading } = useExpenses({ per_page: 5, sort_by: 'date', sort_order: 'desc' });

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900 dark:text-slate-100 tracking-tight">
          Dashboard Overview
        </h2>
        <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
          Track and analyze your spending trends in real time.
        </p>
      </div>

      <StatCards stats={summary} isLoading={isSummaryLoading} />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <MonthlyChart data={monthly} isLoading={isMonthlyLoading} />
        <CategoryChart data={categories} isLoading={isCategoriesLoading} />
      </div>

      <RecentExpenses expenses={expensesData?.items} isLoading={isExpensesLoading} />
    </div>
  );
};
