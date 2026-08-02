import React, { useRef, useState } from 'react';
import { Download, Upload } from 'lucide-react';
import { Button } from '../../components/ui/Button';
import { exportExpenses, importExpenses } from '../../api/expenses';
import toast from 'react-hot-toast';
import { useQueryClient } from '@tanstack/react-query';

export const ExportImport: React.FC = () => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isImporting, setIsImporting] = useState(false);
  const queryClient = useQueryClient();

  const handleExport = async () => {
    try {
      const data = await exportExpenses();
      const jsonString = `data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(data, null, 2))}`;
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute('href', jsonString);
      downloadAnchor.setAttribute('download', `expenses_backup_${new Date().toISOString().split('T')[0]}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      toast.success('Expenses exported successfully!');
    } catch (_err) {
      toast.error('Failed to export expenses');
    }
  };

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setIsImporting(true);

    try {
      const reader = new FileReader();
      reader.onload = async (event) => {
        try {
          const parsed = JSON.parse(event.target?.result as string);
          const list = Array.isArray(parsed) ? parsed : parsed.expenses || [];
          if (list.length === 0) {
            toast.error('No valid expenses found in JSON');
            return;
          }
          const res = await importExpenses(list);
          queryClient.invalidateQueries({ queryKey: ['expenses'] });
          queryClient.invalidateQueries({ queryKey: ['stats'] });
          toast.success(`Imported ${res.imported} expenses!`);
        } catch (_parseErr) {
          toast.error('Invalid JSON format');
        } finally {
          setIsImporting(false);
        }
      };
      reader.readAsText(file);
    } catch (_e) {
      setIsImporting(false);
      toast.error('Failed to read file');
    }
  };

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-soft">
      <h3 className="text-base font-semibold text-slate-900 dark:text-slate-100 mb-1">
        Data Backup & Restore
      </h3>
      <p className="text-xs text-slate-500 dark:text-slate-400 mb-6">
        Export your expense records to JSON format or restore from a previous backup.
      </p>

      <div className="flex flex-wrap gap-4">
        <Button onClick={handleExport} variant="outline" icon={<Download className="w-4 h-4" />}>
          Export JSON
        </Button>

        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          accept=".json"
          className="hidden"
        />

        <Button
          onClick={() => fileInputRef.current?.click()}
          variant="secondary"
          isLoading={isImporting}
          icon={<Upload className="w-4 h-4" />}
        >
          Import JSON
        </Button>
      </div>
    </div>
  );
};
