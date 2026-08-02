import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { ExpenseForm } from '../pages/Expenses/ExpenseForm';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
};

describe('ExpenseForm', () => {
  it('renders modal when open', () => {
    const handleSubmit = vi.fn();
    const handleClose = vi.fn();

    render(
      <ExpenseForm
        isOpen={true}
        onClose={handleClose}
        onSubmit={handleSubmit}
        isLoading={false}
      />,
      { wrapper: createWrapper() }
    );

    expect(screen.getByText('Add New Expense')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('e.g. Grocery Store')).toBeInTheDocument();
  });
});
