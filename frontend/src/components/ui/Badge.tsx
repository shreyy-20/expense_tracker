import React from 'react';
import { cn } from '../../utils/cn';
import { CATEGORY_COLORS, DEFAULT_CATEGORY_COLOR } from '../../utils/constants';

interface BadgeProps {
  category: string;
  className?: string;
  showDot?: boolean;
}

export const Badge: React.FC<BadgeProps> = ({ category, className, showDot = true }) => {
  const style = CATEGORY_COLORS[category] || DEFAULT_CATEGORY_COLOR;

  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-medium border border-transparent transition-colors',
        style.bg,
        style.text,
        className
      )}
    >
      {showDot && (
        <span
          className="w-1.5 h-1.5 rounded-full shrink-0"
          style={{ backgroundColor: style.dot }}
        />
      )}
      {category}
    </span>
  );
};
