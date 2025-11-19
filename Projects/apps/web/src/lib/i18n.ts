export const LOCALES = ['pt-BR', 'en'] as const;

export type Locale = (typeof LOCALES)[number];

export const DEFAULT_LOCALE: Locale = 'pt-BR';

export function normalizeLocale(input: string | null | undefined): Locale {
  const value = (input || '').toLowerCase();
  if (value.startsWith('pt')) return 'pt-BR';
  return 'en';
}
