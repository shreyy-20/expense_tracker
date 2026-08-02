import React from 'react';
import { ExportImport } from './ExportImport';
import { CategoryManager } from './CategoryManager';
import { useCurrency } from '../../context/CurrencyContext';
import { useTheme } from '../../context/ThemeContext';
import { Select } from '../../components/ui/Select';
import { SUPPORTED_CURRENCIES } from '../../utils/constants';

export const Settings: React.FC = () => {
  const { currency, setCurrency } = useCurrency();
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="space-y-6 max-w-4xl">
      <div>
        <h2 className="text-2xl font-bold text-slate-900 dark:text-slate-100 tracking-tight">
          Application Settings
        </h2>
        <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
          Customize currency, themes, categories, and data backups.
        </p>
      </div>

      {/* Preferences */}
      <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft space-y-4">
        <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100">
          General Preferences
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Select
            label="Preferred Currency"
            value={currency}
            onChange={(e) => setCurrency(e.target.value)}
            options={SUPPORTED_CURRENCIES.map((c) => ({
              value: c.code,
              label: `${c.name} (${c.symbol})`,
            }))}
          />

          <div>
            <label className="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">
              Color Theme
            </label>
            <button
              onClick={toggleTheme}
              className="w-full px-3 py-2 text-sm text-left bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-900 dark:text-slate-100 capitalize hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors"
            >
              Current: {theme} Mode
            </button>
          </div>
        </div>
      </div>

      <CategoryManager />

      <ExportImport />
    </div>
  );
};
