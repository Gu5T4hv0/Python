import type { ReactNode } from 'react';
import type { Locale } from '@/lib/i18n';
import { getMessages } from '@/lib/getMessages';
import { TranslationsProvider } from '@/components/TranslationsProvider';

export default async function LocaleLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: { locale: Locale };
}) {
  const locale = params.locale;
  const messages = await getMessages(locale);

  return (
    <TranslationsProvider locale={locale} messages={messages}>
      {children}
    </TranslationsProvider>
  );
}
