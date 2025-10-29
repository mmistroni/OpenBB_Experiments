import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  fullWidth?: boolean;
}

export default function Input({
  label,
  error,
  fullWidth = true,
  className = '',
  ...props
}: InputProps) {
  const inputId = props.id || `input-${Math.random().toString(36).substring(7)}`;

  return (
    <div className={fullWidth ? 'w-full' : ''}>
      {label && (
        <label htmlFor={inputId} className="block text-sm font-medium text-secondary-700 mb-1">
          {label}
        </label>
      )}
      <input
        id={inputId}
        className={`
          w-full px-4 py-2 border rounded-lg
          focus:ring-2 focus:ring-primary-500 focus:border-primary-500
          disabled:bg-secondary-50 disabled:cursor-not-allowed
          ${error ? 'border-red-500' : 'border-secondary-300'}
          ${className}
        `}
        {...props}
      />
      {error && (
        <p className="mt-1 text-sm text-red-600">{error}</p>
      )}
    </div>
  );
}
