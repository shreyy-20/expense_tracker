import { apiClient } from './client';
import { Expense, ExpenseCreateInput, ExpenseUpdateInput, ExpenseQueryParams } from '../types/expense';
import { ApiResponse, PaginationMeta } from '../types/api';

export async function fetchExpenses(params: ExpenseQueryParams): Promise<{ items: Expense[]; pagination: PaginationMeta }> {
  const response = await apiClient.get<ApiResponse<Expense[]>>('/expenses', { params });
  return {
    items: response.data.data,
    pagination: response.data.pagination!,
  };
}

export async function fetchExpenseById(id: string): Promise<Expense> {
  const response = await apiClient.get<ApiResponse<Expense>>(`/expenses/${id}`);
  return response.data.data;
}

export async function createExpense(data: ExpenseCreateInput): Promise<Expense> {
  const response = await apiClient.post<ApiResponse<Expense>>('/expenses', data);
  return response.data.data;
}

export async function updateExpense(id: string, data: ExpenseUpdateInput): Promise<Expense> {
  const response = await apiClient.patch<ApiResponse<Expense>>(`/expenses/${id}`, data);
  return response.data.data;
}

export async function deleteExpense(id: string): Promise<void> {
  await apiClient.delete(`/expenses/${id}`);
}

export async function bulkDeleteExpenses(ids: string[]): Promise<void> {
  await apiClient.delete('/expenses', { data: { ids } });
}

export async function exportExpenses(): Promise<Expense[]> {
  const response = await apiClient.post<ApiResponse<Expense[]>>('/expenses/export');
  return response.data.data;
}

export async function importExpenses(expenses: ExpenseCreateInput[]): Promise<{ imported: number; skipped: number }> {
  const response = await apiClient.post<ApiResponse<{ imported: number; skipped: number }>>('/expenses/import', { expenses });
  return response.data.data;
}

export async function fetchCategories(): Promise<string[]> {
  const response = await apiClient.get<ApiResponse<string[]>>('/expenses/categories/list');
  return response.data.data;
}

export async function addCategory(name: string): Promise<string[]> {
  const response = await apiClient.post<ApiResponse<string[]>>('/expenses/categories', { name });
  return response.data.data;
}

export async function removeCategory(name: string): Promise<string[]> {
  const response = await apiClient.delete<ApiResponse<string[]>>(`/expenses/categories/${encodeURIComponent(name)}`);
  return response.data.data;
}
