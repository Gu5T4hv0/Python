export type Locale = 'pt' | 'en';

// MVP helper: resolve locale from query param only (default: pt)
export function resolveLocale(
  searchParams?: Record<string, string | string[] | undefined>
): Locale {
  const raw = (searchParams?.['lang'] as string) || '';
  const candidate = raw.toLowerCase();
  return candidate === 'en' ? 'en' : 'pt';
}
