import { resolveLocale } from '@/lib/i18n';
import pt from '@/messages/pt';
import en from '@/messages/en';
import LanguageSwitcher from '@/components/LanguageSwitcher';

export default function CancelPage({
  searchParams,
}: {
  searchParams?: Record<string, string | string[] | undefined>;
}) {
  const locale = resolveLocale(searchParams);
  const m = locale === 'en' ? en : pt;

  return (
    <main className="min-h-screen flex items-center justify-center bg-yellow-50">
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <h1 className="text-2xl font-semibold text-yellow-700">{m.cancel_title}</h1>
        <p className="mt-2 text-gray-600">{m.cancel_desc}</p>
        <a href="/create-question" className="mt-6 inline-block text-white bg-yellow-600 hover:bg-yellow-700 px-4 py-2 rounded">{m.back_form}</a>
        <LanguageSwitcher />
      </div>
    </main>
  );
}
