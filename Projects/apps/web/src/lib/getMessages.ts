import type { Locale } from './i18n';

export type Messages = Record<string, string>;

export async function getMessages(locale: Locale): Promise<Messages> {
  try {
    const mod = await import(`../../public/locales/${locale}/common.json`);
    return (mod as any).default as Messages;
  } catch {
    return {};
  }
}
