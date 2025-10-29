import React from 'react';

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string;
  error?: string;
  options: { value: string; label: string }[];
  fullWidth?: boolean;
}

export default function Select({
  label,
  error,
  options,
  fullWidth = true,
  className = '',
  ...props
}: SelectProps) {
  const selectId = props.id || `select-${Math.random().toString(36).substring(7)}`;

  return (
    <div className={fullWidth ? 'w-full' : ''}>
      {label && (
        <label htmlFor={selectId} className="block text-sm font-medium text-secondary-700 mb-1">
          {label}
        </label>
      )}
      <select
        id={selectId}
        className={`
          w-full px-4 py-2 border rounded-lg
          focus:ring-2 focus:ring-primary-500 focus:border-primary-500
          disabled:bg-secondary-50 disabled:cursor-not-allowed
          ${error ? 'border-red-500' : 'border-secondary-300'}
          ${className}
        `}
        {...props}
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error && (
        <p className="mt-1 text-sm text-red-600">{error}</p>
      )}
    </div>
  );
}
