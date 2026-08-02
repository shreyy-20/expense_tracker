/**
 * Format currency amount with ISO 4217 code and user locale.
 */
export function formatCurrency(amount: number, currencyCode: string = 'USD'): string {
  try {
    return new Intl.NumberFormat(undefined, {
      style: 'currency',
      currency: currencyCode,
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(amount);
  } catch (_e) {
    return `$${amount.toFixed(2)}`;
  }
}

/**
 * Format date string (YYYY-MM-DD) into locale-aware format.
 */
export function formatDate(dateString: string, options?: Intl.DateTimeFormatOptions): string {
  if (!dateString) return '';
  try {
    const [year, month, day] = dateString.split('-').map(Number);
    const date = new Date(year, month - 1, day);
    const defaultOptions: Intl.DateTimeFormatOptions = {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    };
    return new Intl.DateTimeFormat(undefined, options || defaultOptions).format(date);
  } catch (_e) {
    return dateString;
  }
}

/**
 * Format YYYY-MM month string into Month Year (e.g., "2024-07" -> "Jul 2024").
 */
export function formatMonthYear(yearMonth: string): string {
  if (!yearMonth || !yearMonth.includes('-')) return yearMonth;
  const [year, month] = yearMonth.split('-').map(Number);
  const date = new Date(year, month - 1, 1);
  return new Intl.DateTimeFormat(undefined, { month: 'short', year: 'numeric' }).format(date);
}
