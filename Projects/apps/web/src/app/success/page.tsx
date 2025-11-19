import { headers } from 'next/headers';
import { redirect } from 'next/navigation';
import { DEFAULT_LOCALE, normalizeLocale } from '@/lib/i18n';

export default async function SuccessPage() {
  const h = await headers();
  let locale = DEFAULT_LOCALE;

  // 1) Prefer explicit locale cookie set by the app (LanguageSwitcher)
  const cookieHeader = h.get('cookie') || '';
  const localeMatch = cookieHeader.match(/(?:^|;\s*)locale=([^;]+)/);
  if (localeMatch?.[1]) {
    const cookieLocale = decodeURIComponent(localeMatch[1]);
    if (cookieLocale === 'pt-BR' || cookieLocale === 'en') {
      locale = cookieLocale;
    }
  } else {
    // 2) Fallback to geolocation headers
    const countryHeader =
      h.get('x-vercel-ip-country') ||
      h.get('cf-ipcountry') ||
      h.get('x-country') ||
      '';

    if (countryHeader) {
      const country = countryHeader.toUpperCase();
      locale = country === 'BR' ? 'pt-BR' : 'en';
    } else {
      // 3) Final fallback: Accept-Language
      const acceptLanguage = h.get('accept-language');
      locale = normalizeLocale(acceptLanguage);
    }
  }

  redirect(`/${locale}/success`);
}
