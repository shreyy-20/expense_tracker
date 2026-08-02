import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { Sidebar } from './Sidebar';
import { Header } from './Header';
import { ExpenseForm } from '../../pages/Expenses/ExpenseForm';
import { useCreateExpense } from '../../hooks/useExpenses';

export const Layout: React.FC = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const createMutation = useCreateExpense();

  return (
    <div className="flex min-h-screen bg-slate-50 dark:bg-slate-950">
      <Sidebar isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />

      <div className="flex-1 flex flex-col min-w-0">
        <Header
          onOpenSidebar={() => setIsSidebarOpen(true)}
          onAddExpense={() => setIsAddModalOpen(true)}
        />

        <main className="flex-1 p-4 md:p-6 lg:p-8 max-w-7xl w-full mx-auto animate-fadeIn">
          <Outlet />
        </main>
      </div>

      <ExpenseForm
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        onSubmit={async (data) => {
          await createMutation.mutateAsync(data);
          setIsAddModalOpen(false);
        }}
        isLoading={createMutation.isPending}
      />
    </div>
  );
};
