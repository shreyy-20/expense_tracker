export interface PaginationMeta {
  page: number;
  per_page: number;
  total_items: number;
  total_pages: number;
  has_next: boolean;
  has_prev: boolean;
}

export interface ApiResponse<T> {
  status: 'success' | 'error';
  data: T;
  pagination?: PaginationMeta;
  message?: string;
}

export interface ApiErrorResponse {
  status: 'error';
  error: {
    code: string;
    message: string;
    details?: Array<{ field?: string; message: string; type: string }>;
  };
  request_id?: string;
}
