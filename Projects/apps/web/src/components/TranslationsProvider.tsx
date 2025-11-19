'use client';

import React, { createContext, useContext, useMemo } from 'react';
import type { Messages } from '@/lib/getMessages';
import type { Locale } from '@/lib/i18n';

interface TranslationContextValue {
  locale: Locale;
  messages: Messages;
  t: (key: string) => string;
}

const TranslationContext = createContext<TranslationContextValue | undefined>(
  undefined,
);

export function TranslationsProvider({
  locale,
  messages,
  children,
}: {
  locale: Locale;
  messages: Messages;
  children: React.ReactNode;
}) {
  const value = useMemo<TranslationContextValue>(
    () => ({
      locale,
      messages,
      t: (key: string) => messages[key] ?? key,
    }),
    [locale, messages],
  );

  return (
    <TranslationContext.Provider value={value}>
      {children}
    </TranslationContext.Provider>
  );
}

export function useTranslation() {
  const ctx = useContext(TranslationContext);
  if (!ctx) {
    throw new Error('useTranslation must be used within TranslationsProvider');
  }
  return ctx;
}
