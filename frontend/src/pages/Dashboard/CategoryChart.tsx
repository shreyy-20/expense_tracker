import React from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import { CategoryStat } from '../../types/expense';
import { CATEGORY_COLORS, DEFAULT_CATEGORY_COLOR } from '../../utils/constants';
import { formatCurrency } from '../../utils/formatters';
import { useCurrency } from '../../context/CurrencyContext';
import { Skeleton } from '../../components/ui/Skeleton';

interface CategoryChartProps {
  data?: CategoryStat[];
  isLoading: boolean;
}

export const CategoryChart: React.FC<CategoryChartProps> = ({ data, isLoading }) => {
  const { currency } = useCurrency();

  if (isLoading) {
    return <Skeleton className="h-80 w-full rounded-2xl" />;
  }

  if (!data || data.length === 0) {
    return (
      <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 h-80 flex items-center justify-center text-sm text-slate-400">
        No category data available yet.
      </div>
    );
  }

  const chartData = data.map((item) => ({
    name: item.category,
    value: item.total,
    color: (CATEGORY_COLORS[item.category] || DEFAULT_CATEGORY_COLOR).dot,
  }));

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft">
      <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100 mb-6">
        Expenses by Category
      </h3>
      <div className="h-64 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={chartData}
              cx="50%"
              cy="50%"
              innerRadius={55}
              outerRadius={80}
              paddingAngle={4}
              dataKey="value"
            >
              {chartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
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
            <Legend verticalAlign="bottom" height={36} iconType="circle" wrapperStyle={{ fontSize: '11px' }} />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
