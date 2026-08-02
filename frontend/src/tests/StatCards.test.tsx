import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { StatCards } from '../pages/Dashboard/StatCards';
import { CurrencyProvider } from '../context/CurrencyContext';

describe('StatCards', () => {
  it('renders stats correctly', () => {
    const mockStats = {
      total_amount: 1500.5,
      total_count: 10,
      average_amount: 150.05,
      highest_expense: { title: 'Rent', amount: 800, date: '2024-07-01' },
      lowest_expense: { title: 'Coffee', amount: 5, date: '2024-07-02' },
      top_category: 'Housing',
      currency: 'USD',
    };

    render(
      <CurrencyProvider>
        <StatCards stats={mockStats} isLoading={false} />
      </CurrencyProvider>
    );

    expect(screen.getByText('Total Expenses')).toBeInTheDocument();
    expect(screen.getByText('Housing')).toBeInTheDocument();
  });
});
