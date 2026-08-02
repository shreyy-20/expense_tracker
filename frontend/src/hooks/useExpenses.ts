import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  fetchExpenses,
  createExpense,
  updateExpense,
  deleteExpense,
  bulkDeleteExpenses,
  fetchCategories,
  addCategory,
  removeCategory,
} from '../api/expenses';
import { ExpenseCreateInput, ExpenseUpdateInput, ExpenseQueryParams } from '../types/expense';
import toast from 'react-hot-toast';

export function useExpenses(params: ExpenseQueryParams = {}) {
  return useQuery({
    queryKey: ['expenses', params],
    queryFn: () => fetchExpenses(params),
  });
}

export function useCreateExpense() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (data: ExpenseCreateInput) => createExpense(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['expenses'] });
      queryClient.invalidateQueries({ queryKey: ['stats'] });
      toast.success('Expense added successfully!');
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to create expense');
    },
  });
}

export function useUpdateExpense() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: ExpenseUpdateInput }) => updateExpense(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['expenses'] });
      queryClient.invalidateQueries({ queryKey: ['stats'] });
      toast.success('Expense updated!');
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to update expense');
    },
  });
}

export function useDeleteExpense() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: string) => deleteExpense(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['expenses'] });
      queryClient.invalidateQueries({ queryKey: ['stats'] });
      toast.success('Expense deleted!');
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to delete expense');
    },
  });
}

export function useBulkDeleteExpenses() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (ids: string[]) => bulkDeleteExpenses(ids),
    onSuccess: (_, ids) => {
      queryClient.invalidateQueries({ queryKey: ['expenses'] });
      queryClient.invalidateQueries({ queryKey: ['stats'] });
      toast.success(`${ids.length} expenses deleted!`);
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to bulk delete expenses');
    },
  });
}

export function useCategories() {
  return useQuery({
    queryKey: ['categories'],
    queryFn: fetchCategories,
  });
}

export function useAddCategory() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (name: string) => addCategory(name),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories'] });
      toast.success('Category added!');
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to add category');
    },
  });
}

export function useRemoveCategory() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (name: string) => removeCategory(name),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categories'] });
      toast.success('Category removed!');
    },
    onError: (err: Error) => {
      toast.error(err.message || 'Failed to remove category');
    },
  });
}
