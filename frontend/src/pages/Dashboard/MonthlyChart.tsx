import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { MonthlyStat } from '../../types/expense';
import { formatCurrency, formatMonthYear } from '../../utils/formatters';
import { useCurrency } from '../../context/CurrencyContext';
import { Skeleton } from '../../components/ui/Skeleton';

interface MonthlyChartProps {
  data?: MonthlyStat[];
  isLoading: boolean;
}

export const MonthlyChart: React.FC<MonthlyChartProps> = ({ data, isLoading }) => {
  const { currency } = useCurrency();

  if (isLoading) {
    return <Skeleton className="h-80 w-full rounded-2xl" />;
  }

  if (!data || data.length === 0) {
    return (
      <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 h-80 flex items-center justify-center text-sm text-slate-400">
        No monthly data available yet.
      </div>
    );
  }

  const chartData = data.map((d) => ({
    name: formatMonthYear(d.month),
    total: d.total,
  }));

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft">
      <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100 mb-6">
        Monthly Spending Trends
      </h3>
      <div className="h-64 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#334155" opacity={0.15} />
            <XAxis dataKey="name" stroke="#94a3b8" fontSize={11} tickLine={false} axisLine={false} />
            <YAxis stroke="#94a3b8" fontSize={11} tickLine={false} axisLine={false} tickFormatter={(val) => `$${val}`} />
            <Tooltip
              formatter={(value: number) => [formatCurrency(value, currency), 'Total']}
              contentStyle={{
                backgroundColor: '#0f172a',
                border: 'none',
                borderRadius: '0.75rem',
                color: '#f8fafc',
                fontSize: '12px',
              }}
            />
            <Bar dataKey="total" fill="#6366f1" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
