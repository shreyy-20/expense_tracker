import { useQuery } from '@tanstack/react-query';
import { fetchSummaryStats, fetchMonthlyStats, fetchCategoryStats } from '../api/stats';

export function useSummaryStats() {
  return useQuery({
    queryKey: ['stats', 'summary'],
    queryFn: fetchSummaryStats,
  });
}

export function useMonthlyStats() {
  return useQuery({
    queryKey: ['stats', 'monthly'],
    queryFn: fetchMonthlyStats,
  });
}

export function useCategoryStats() {
  return useQuery({
    queryKey: ['stats', 'categories'],
    queryFn: fetchCategoryStats,
  });
}
