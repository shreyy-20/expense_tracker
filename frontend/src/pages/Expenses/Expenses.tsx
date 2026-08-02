import React, { useState } from 'react';
import { ExpenseFilters } from './ExpenseFilters';
import { ExpenseTable } from './ExpenseTable';
import { BulkActions } from './BulkActions';
import { Pagination } from '../../components/ui/Pagination';
import { ExpenseForm } from './ExpenseForm';
import { ConfirmDialog } from '../../components/ui/ConfirmDialog';
import {
  useExpenses,
  useCreateExpense,
  useUpdateExpense,
  useDeleteExpense,
  useBulkDeleteExpenses,
} from '../../hooks/useExpenses';
import { Expense, ExpenseCreateInput } from '../../types/expense';
import { useDebounce } from '../../hooks/useDebounce';

export const Expenses: React.FC = () => {
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');
  const [sortBy, setSortBy] = useState('date');
  const [sortOrder, setSortOrder] = useState('desc');
  const [selectedIds, setSelectedIds] = useState<string[]>([]);

  const [isFormOpen, setIsFormOpen] = useState(false);
  const [editingExpense, setEditingExpense] = useState<Expense | null>(null);
  const [deletingId, setDeletingId] = useState<string | null>(null);
  const [isBulkConfirmOpen, setIsBulkConfirmOpen] = useState(false);

  const debouncedSearch = useDebounce(search, 300);

  const { data, isLoading } = useExpenses({
    page,
    per_page: 15,
    search: debouncedSearch,
    category: category || undefined,
    sort_by: sortBy as any,
    sort_order: sortOrder as any,
  });

  const createMutation = useCreateExpense();
  const updateMutation = useUpdateExpense();
  const deleteMutation = useDeleteExpense();
  const bulkDeleteMutation = useBulkDeleteExpenses();

  const handleToggleSelectAll = () => {
    if (!data?.items) return;
    if (selectedIds.length === data.items.length) {
      setSelectedIds([]);
    } else {
      setSelectedIds(data.items.map((i) => i.id));
    }
  };

  const handleToggleSelect = (id: string) => {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((i) => i !== id) : [...prev, id]
    );
  };

  const handleFormSubmit = async (formData: ExpenseCreateInput) => {
    if (editingExpense) {
      await updateMutation.mutateAsync({ id: editingExpense.id, data: formData });
    } else {
      await createMutation.mutateAsync(formData);
    }
    setIsFormOpen(false);
    setEditingExpense(null);
  };

  const handleDeleteConfirm = async () => {
    if (!deletingId) return;
    await deleteMutation.mutateAsync(deletingId);
    setDeletingId(null);
  };

  const handleBulkDeleteConfirm = async () => {
    await bulkDeleteMutation.mutateAsync(selectedIds);
    setSelectedIds([]);
    setIsBulkConfirmOpen(false);
  };

  return (
    <div className="space-y-4">
      <div>
        <h2 className="text-2xl font-bold text-slate-900 dark:text-slate-100 tracking-tight">
          Expenses Management
        </h2>
        <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
          View, filter, sort, and manage all your transactions.
        </p>
      </div>

      <ExpenseFilters
        search={search}
        onSearchChange={setSearch}
        category={category}
        onCategoryChange={setCategory}
        sortBy={sortBy}
        onSortByChange={setSortBy}
        sortOrder={sortOrder}
        onSortOrderChange={setSortOrder}
      />

      <BulkActions
        selectedCount={selectedIds.length}
        onClearSelection={() => setSelectedIds([])}
        onBulkDelete={() => setIsBulkConfirmOpen(true)}
      />

      <div className="shadow-soft rounded-2xl overflow-hidden">
        <ExpenseTable
          expenses={data?.items}
          isLoading={isLoading}
          selectedIds={selectedIds}
          onToggleSelectAll={handleToggleSelectAll}
          onToggleSelect={handleToggleSelect}
          onEdit={(expense) => {
            setEditingExpense(expense);
            setIsFormOpen(true);
          }}
          onDelete={(id) => setDeletingId(id)}
          onAddFirst={() => {
            setEditingExpense(null);
            setIsFormOpen(true);
          }}
        />
        {data?.pagination && (
          <Pagination
            page={data.pagination.page}
            totalPages={data.pagination.total_pages}
            totalItems={data.pagination.total_items}
            perPage={data.pagination.per_page}
            onPageChange={setPage}
          />
        )}
      </div>

      <ExpenseForm
        isOpen={isFormOpen}
        onClose={() => {
          setIsFormOpen(false);
          setEditingExpense(null);
        }}
        onSubmit={handleFormSubmit}
        initialData={editingExpense}
        isLoading={createMutation.isPending || updateMutation.isPending}
      />

      <ConfirmDialog
        isOpen={!!deletingId}
        onClose={() => setDeletingId(null)}
        onConfirm={handleDeleteConfirm}
        title="Delete Expense"
        message="Are you sure you want to delete this expense? This action cannot be undone."
        isLoading={deleteMutation.isPending}
      />

      <ConfirmDialog
        isOpen={isBulkConfirmOpen}
        onClose={() => setIsBulkConfirmOpen(false)}
        onConfirm={handleBulkDeleteConfirm}
        title="Delete Selected Expenses"
        message={`Are you sure you want to delete ${selectedIds.length} selected expenses? This action cannot be undone.`}
        isLoading={bulkDeleteMutation.isPending}
      />
    </div>
  );
};
