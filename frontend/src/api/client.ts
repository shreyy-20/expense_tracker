import axios from 'axios';

const rawBaseURL = (import.meta.env.VITE_API_URL || '').replace(/\/+$/, '');
const apiBaseURL = rawBaseURL ? `${rawBaseURL}/api/v1` : '/api/v1';

export const apiClient = axios.create({
  baseURL: apiBaseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    const message = error.response?.data?.error?.message || error.message || 'An unexpected error occurred';
    return Promise.reject(new Error(message));
  }
);
