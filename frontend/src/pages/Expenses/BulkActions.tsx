import React from 'react';
import { Trash2 } from 'lucide-react';
import { Button } from '../../components/ui/Button';

interface BulkActionsProps {
  selectedCount: number;
  onClearSelection: () => void;
  onBulkDelete: () => void;
}

export const BulkActions: React.FC<BulkActionsProps> = ({
  selectedCount,
  onClearSelection,
  onBulkDelete,
}) => {
  if (selectedCount === 0) return null;

  return (
    <div className="flex items-center justify-between px-4 py-2.5 bg-brand-50 dark:bg-brand-950/40 border border-brand-200 dark:border-brand-900 rounded-xl text-xs">
      <span className="font-medium text-brand-700 dark:text-brand-300">
        {selectedCount} item{selectedCount > 1 ? 's' : ''} selected
      </span>
      <div className="flex items-center gap-2">
        <Button variant="ghost" size="sm" onClick={onClearSelection}>
          Clear
        </Button>
        <Button variant="danger" size="sm" onClick={onBulkDelete} icon={<Trash2 className="w-3.5 h-3.5" />}>
          Delete Selected
        </Button>
      </div>
    </div>
  );
};
