import { apiClient } from './client';
import { SummaryStats, MonthlyStat, CategoryStat } from '../types/expense';
import { ApiResponse } from '../types/api';

export async function fetchSummaryStats(): Promise<SummaryStats> {
  const response = await apiClient.get<ApiResponse<SummaryStats>>('/stats/summary');
  return response.data.data;
}

export async function fetchMonthlyStats(): Promise<MonthlyStat[]> {
  const response = await apiClient.get<ApiResponse<MonthlyStat[]>>('/stats/monthly');
  return response.data.data;
}

export async function fetchCategoryStats(): Promise<CategoryStat[]> {
  const response = await apiClient.get<ApiResponse<CategoryStat[]>>('/stats/categories');
  return response.data.data;
}
