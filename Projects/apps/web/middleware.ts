import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { DEFAULT_LOCALE, normalizeLocale, LOCALES } from './src/lib/i18n';

const PUBLIC_FILE = /\.(.*)$/;

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Ignore API, Next internals and public files
  if (
    pathname.startsWith('/api') ||
    pathname.startsWith('/_next') ||
    PUBLIC_FILE.test(pathname)
  ) {
    return NextResponse.next();
  }

  // If path already includes a locale, continue
  const hasLocalePrefix = LOCALES.some((locale) =>
    pathname === `/${locale}` || pathname.startsWith(`/${locale}/`),
  );

  if (hasLocalePrefix) {
    return NextResponse.next();
  }

  // Detect country from infra headers (Vercel, Cloudflare, etc.)
  const countryHeader =
    request.headers.get('x-vercel-ip-country') ||
    request.headers.get('cf-ipcountry') ||
    request.headers.get('x-country') ||
    '';

  let locale = DEFAULT_LOCALE;

  if (countryHeader) {
    const country = countryHeader.toUpperCase();
    locale = country === 'BR' ? 'pt-BR' : 'en';
  } else {
    const acceptLanguage = request.headers.get('accept-language');
    locale = normalizeLocale(acceptLanguage);
  }

  const url = request.nextUrl.clone();
  url.pathname = `/${locale}${pathname}`;
  return NextResponse.redirect(url);
}

export const config = {
  matcher: ['/((?!_next/|api/|.*\\..*).*)'],
};
