'use client';

import { usePathname, useSearchParams, useRouter } from 'next/navigation';

export default function LanguageSwitcher() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const router = useRouter();

  const setLocale = (locale: 'pt' | 'en') => {
    const params = new URLSearchParams(searchParams?.toString());
    params.set('lang', locale);
    // Also drop a cookie for simple persistence
    document.cookie = `locale=${locale}; path=/; max-age=${60 * 60 * 24 * 365}`;
    router.push(`${pathname}?${params.toString()}`);
  };

  return (
    <div className="flex items-center gap-2 justify-center mt-4">
      <button onClick={() => setLocale('pt')} className="px-2 py-1 text-sm rounded border">PT</button>
      <button onClick={() => setLocale('en')} className="px-2 py-1 text-sm rounded border">EN</button>
    </div>
  );
}
