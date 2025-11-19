"use client";

import { useTranslation } from '@/components/TranslationsProvider';

export default function SuccessPage() {
  const { t, locale } = useTranslation();

  return (
    <main className="min-h-screen flex items-center justify-center bg-green-50">
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <h1 className="text-2xl font-semibold text-green-700">
          {t('success.title')}
        </h1>
        <p className="mt-2 text-gray-600">{t('success.description')}</p>
        <a
          href={`/${locale}/`}
          className="mt-6 inline-block text-white bg-green-600 hover:bg-green-700 px-4 py-2 rounded"
        >
          {t('success.back_home')}
        </a>
      </div>
    </main>
  );
}
