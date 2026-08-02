import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'react-hot-toast';
import { ThemeProvider } from './context/ThemeContext';
import { CurrencyProvider } from './context/CurrencyContext';
import { Layout } from './components/layout/Layout';
import { Dashboard } from './pages/Dashboard/Dashboard';
import { Expenses } from './pages/Expenses/Expenses';
import { Settings } from './pages/Settings/Settings';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
      staleTime: 30000,
    },
  },
});

export const App: React.FC = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <CurrencyProvider>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route index element={<Dashboard />} />
                <Route path="expenses" element={<Expenses />} />
                <Route path="settings" element={<Settings />} />
              </Route>
            </Routes>
          </BrowserRouter>
          <Toaster position="bottom-right" toastOptions={{ duration: 3000 }} />
        </CurrencyProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
};
