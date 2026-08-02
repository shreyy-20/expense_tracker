import React from 'react';
import { Search, X } from 'lucide-react';
import { cn } from '../../utils/cn';

interface SearchInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  value: string;
  onChangeValue: (value: string) => void;
}

export const SearchInput: React.FC<SearchInputProps> = ({
  value,
  onChangeValue,
  className,
  placeholder = 'Search expenses...',
  ...props
}) => {
  return (
    <div className={cn('relative flex items-center', className)}>
      <Search className="absolute left-3 w-4 h-4 text-slate-400" />
      <input
        type="text"
        value={value}
        onChange={(e) => onChangeValue(e.target.value)}
        placeholder={placeholder}
        className="w-full pl-9 pr-8 py-2 text-sm bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-500/20 focus:border-brand-500 placeholder-slate-400 text-slate-900 dark:text-slate-100 transition-colors"
        {...props}
      />
      {value && (
        <button
          onClick={() => onChangeValue('')}
          className="absolute right-2.5 p-0.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
        >
          <X className="w-3.5 h-3.5" />
        </button>
      )}
    </div>
  );
};
