import React, { createContext, useContext, useState } from 'react';

interface CurrencyContextType {
  currency: string;
  setCurrency: (code: string) => void;
}

const CurrencyContext = createContext<CurrencyContextType | undefined>(undefined);

export const CurrencyProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [currency, setCurrencyState] = useState<string>(() => {
    return localStorage.getItem('currency') || 'USD';
  });

  const setCurrency = (code: string) => {
    setCurrencyState(code);
    localStorage.setItem('currency', code);
  };

  return (
    <CurrencyContext.Provider value={{ currency, setCurrency }}>
      {children}
    </CurrencyContext.Provider>
  );
};

export function useCurrency() {
  const context = useContext(CurrencyContext);
  if (!context) throw new Error('useCurrency must be used within a CurrencyProvider');
  return context;
}
