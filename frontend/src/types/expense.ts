export interface Expense {
  id: string;
  title: string;
  amount: number;
  category: string;
  date: string; // YYYY-MM-DD
  created_at: string;
  updated_at: string;
}

export interface ExpenseCreateInput {
  title: string;
  amount: number;
  category: string;
  date: string;
}

export interface ExpenseUpdateInput {
  title?: string;
  amount?: number;
  category?: string;
  date?: string;
}

export interface SummaryStats {
  total_amount: number;
  total_count: number;
  average_amount: number;
  highest_expense: { title: string; amount: number; date: string } | null;
  lowest_expense: { title: string; amount: number; date: string } | null;
  top_category: string | null;
  currency: string;
}

export interface MonthlyStat {
  month: string; // YYYY-MM
  total: number;
  count: number;
}

export interface CategoryStat {
  category: string;
  total: number;
  count: number;
  percentage: number;
  average: number;
}

export interface ExpenseQueryParams {
  page?: number;
  per_page?: number;
  category?: string;
  search?: string;
  sort_by?: 'date' | 'amount' | 'title' | 'category' | 'created_at';
  sort_order?: 'asc' | 'desc';
  date_from?: string;
  date_to?: string;
  amount_min?: number;
  amount_max?: number;
}
