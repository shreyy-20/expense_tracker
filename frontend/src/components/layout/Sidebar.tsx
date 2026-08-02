import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Receipt, Settings, Wallet, Sun, Moon } from 'lucide-react';
import { useTheme } from '../../context/ThemeContext';
import { cn } from '../../utils/cn';

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ isOpen, onClose }) => {
  const { theme, toggleTheme } = useTheme();

  const navItems = [
    { to: '/', label: 'Dashboard', icon: LayoutDashboard },
    { to: '/expenses', label: 'Expenses', icon: Receipt },
    { to: '/settings', label: 'Settings', icon: Settings },
  ];

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-40 lg:hidden"
          onClick={onClose}
        />
      )}

      <aside
        className={cn(
          'fixed lg:static inset-y-0 left-0 z-50 w-64 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 flex flex-col transition-transform duration-200 ease-in-out lg:translate-x-0',
          isOpen ? 'translate-x-0' : '-translate-x-full'
        )}
      >
        {/* Brand */}
        <div className="flex items-center gap-3 px-6 py-5 border-b border-slate-100 dark:border-slate-800">
          <div className="p-2 rounded-xl bg-brand-600 text-white shadow-md shadow-brand-500/20">
            <Wallet className="w-6 h-6" />
          </div>
          <div>
            <h1 className="font-bold text-base text-slate-900 dark:text-slate-100 tracking-tight">
              ExpenseTracker
            </h1>
            <p className="text-[10px] uppercase font-semibold text-brand-600 dark:text-brand-400 tracking-wider">
              Smart Analytics
            </p>
          </div>
        </div>

        {/* Navigation */}
        <nav className="flex-1 px-4 py-6 space-y-1">
          {navItems.map(({ to, label, icon: Icon }) => (
            <NavLink
              key={to}
              to={to}
              onClick={onClose}
              className={({ isActive }) =>
                cn(
                  'flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all',
                  isActive
                    ? 'bg-brand-50 dark:bg-brand-950/50 text-brand-600 dark:text-brand-400 shadow-sm'
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800/50 hover:text-slate-900 dark:hover:text-slate-200'
                )
              }
            >
              <Icon className="w-5 h-5" />
              {label}
            </NavLink>
          ))}
        </nav>

        {/* Footer / Theme Toggle */}
        <div className="p-4 border-t border-slate-100 dark:border-slate-800">
          <button
            onClick={toggleTheme}
            className="flex items-center justify-between w-full px-3.5 py-2.5 rounded-xl text-sm font-medium text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          >
            <span className="flex items-center gap-3">
              {theme === 'dark' ? <Moon className="w-4 h-4" /> : <Sun className="w-4 h-4" />}
              {theme === 'dark' ? 'Dark Mode' : 'Light Mode'}
            </span>
            <span className="text-xs text-slate-400 dark:text-slate-500 capitalize">
              {theme}
            </span>
          </button>
        </div>
      </aside>
    </>
  );
};
