import React from 'react';
import { Menu, Plus } from 'lucide-react';
import { Button } from '../ui/Button';

interface HeaderProps {
  onOpenSidebar: () => void;
  onAddExpense?: () => void;
}

export const Header: React.FC<HeaderProps> = ({ onOpenSidebar, onAddExpense }) => {
  return (
    <header className="sticky top-0 z-30 flex items-center justify-between px-6 py-4 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 lg:justify-end">
      <button
        onClick={onOpenSidebar}
        className="p-2 -ml-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-200 lg:hidden"
      >
        <Menu className="w-6 h-6" />
      </button>

      {onAddExpense && (
        <Button onClick={onAddExpense} icon={<Plus className="w-4 h-4" />} size="sm">
          Add Expense
        </Button>
      )}
    </header>
  );
};
