'use client';

import { useEffect } from 'react';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'info';
  onClose: () => void;
  duration?: number;
}

export default function Toast({ message, type = 'info', onClose, duration = 3000 }: ToastProps) {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  const typeStyles = {
    success: 'bg-green-500 text-white',
    error: 'bg-red-500 text-white',
    info: 'bg-blue-500 text-white',
  };

  const icons = {
    success: '✓',
    error: '✕',
    info: 'ℹ',
  };

  return (
    <div className="fixed bottom-4 right-4 z-50 animate-slide-up">
      <div className={`${typeStyles[type]} px-6 py-4 rounded-lg shadow-lg flex items-center gap-3 min-w-[300px]`}>
        <span className="text-xl">{icons[type]}</span>
        <p className="flex-1 font-medium">{message}</p>
        <button
          onClick={onClose}
          className="text-white hover:opacity-75 transition-opacity"
        >
          ✕
        </button>
      </div>
    </div>
  );
}
