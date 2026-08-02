export const DEFAULT_CATEGORIES = [
  'Food & Dining',
  'Transportation',
  'Housing',
  'Utilities',
  'Healthcare',
  'Entertainment',
  'Shopping',
  'Education',
  'Travel',
  'Personal Care',
  'Insurance',
  'Savings & Investments',
  'Gifts & Donations',
  'Other',
];

export const CATEGORY_COLORS: Record<string, { bg: string; text: string; dot: string }> = {
  'Food & Dining': { bg: 'bg-amber-50 dark:bg-amber-950/40', text: 'text-amber-700 dark:text-amber-400', dot: '#f59e0b' },
  'Transportation': { bg: 'bg-blue-50 dark:bg-blue-950/40', text: 'text-blue-700 dark:text-blue-400', dot: '#3b82f6' },
  'Housing': { bg: 'bg-purple-50 dark:bg-purple-950/40', text: 'text-purple-700 dark:text-purple-400', dot: '#8b5cf6' },
  'Utilities': { bg: 'bg-emerald-50 dark:bg-emerald-950/40', text: 'text-emerald-700 dark:text-emerald-400', dot: '#10b981' },
  'Healthcare': { bg: 'bg-red-50 dark:bg-red-950/40', text: 'text-red-700 dark:text-red-400', dot: '#ef4444' },
  'Entertainment': { bg: 'bg-pink-50 dark:bg-pink-950/40', text: 'text-pink-700 dark:text-pink-400', dot: '#ec4899' },
  'Shopping': { bg: 'bg-teal-50 dark:bg-teal-950/40', text: 'text-teal-700 dark:text-teal-400', dot: '#14b8a6' },
  'Education': { bg: 'bg-indigo-50 dark:bg-indigo-950/40', text: 'text-indigo-700 dark:text-indigo-400', dot: '#6366f1' },
  'Travel': { bg: 'bg-sky-50 dark:bg-sky-950/40', text: 'text-sky-700 dark:text-sky-400', dot: '#0ea5e9' },
  'Personal Care': { bg: 'bg-fuchsia-50 dark:bg-fuchsia-950/40', text: 'text-fuchsia-700 dark:text-fuchsia-400', dot: '#d946ef' },
  'Insurance': { bg: 'bg-slate-100 dark:bg-slate-800', text: 'text-slate-700 dark:text-slate-300', dot: '#64748b' },
  'Savings & Investments': { bg: 'bg-green-50 dark:bg-green-950/40', text: 'text-green-700 dark:text-green-400', dot: '#22c55e' },
  'Gifts & Donations': { bg: 'bg-rose-50 dark:bg-rose-950/40', text: 'text-rose-700 dark:text-rose-400', dot: '#f43f5e' },
  'Other': { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-700 dark:text-gray-300', dot: '#6b7280' },
};

export const DEFAULT_CATEGORY_COLOR = {
  bg: 'bg-indigo-50 dark:bg-indigo-950/40',
  text: 'text-indigo-700 dark:text-indigo-400',
  dot: '#6366f1',
};

export const SUPPORTED_CURRENCIES = [
  { code: 'USD', symbol: '$', name: 'US Dollar' },
  { code: 'EUR', symbol: '€', name: 'Euro' },
  { code: 'GBP', symbol: '£', name: 'British Pound' },
  { code: 'CAD', symbol: 'CA$', name: 'Canadian Dollar' },
  { code: 'AUD', symbol: 'A$', name: 'Australian Dollar' },
  { code: 'JPY', symbol: '¥', name: 'Japanese Yen' },
  { code: 'INR', symbol: '₹', name: 'Indian Rupee' },
  { code: 'CNY', symbol: 'CN¥', name: 'Chinese Yuan' },
  { code: 'CHF', symbol: 'CHF', name: 'Swiss Franc' },
  { code: 'BRL', symbol: 'R$', name: 'Brazilian Real' },
];
