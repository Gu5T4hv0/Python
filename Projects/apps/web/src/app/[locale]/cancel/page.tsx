"use client";

import { useTranslation } from '@/components/TranslationsProvider';

export default function CancelPage() {
  const { t, locale } = useTranslation();

  return (
    <main className="min-h-screen flex items-center justify-center bg-yellow-50">
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <h1 className="text-2xl font-semibold text-yellow-700">
          {t('cancel.title')}
        </h1>
        <p className="mt-2 text-gray-600">{t('cancel.description')}</p>
        <a
          href={`/${locale}/create-question`}
          className="mt-6 inline-block text-white bg-yellow-600 hover:bg-yellow-700 px-4 py-2 rounded"
        >
          {t('cancel.back_form')}
        </a>
      </div>
    </main>
  );
}
