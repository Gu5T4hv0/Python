"use client";

import Link from 'next/link';
import { useTranslation } from '@/components/TranslationsProvider';

export default function HomePage() {
  const { t, locale } = useTranslation();

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-gradient-to-b from-blue-50 to-white">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold text-center text-blue-600 mb-8">
          {t('home.title')}
        </h1>
        <p className="text-center text-gray-600 mb-8">{t('home.subtitle')}</p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <Link
            href={`/${locale}/create-question`}
            className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer"
          >
            <h2 className="text-xl font-semibold mb-2">{t('home.card_ask_title')}</h2>
            <p className="text-gray-600">{t('home.card_ask_desc')}</p>
          </Link>

          <Link
            href={`/${locale}/questions`}
            className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer"
          >
            <h2 className="text-xl font-semibold mb-2">{t('home.card_feed_title')}</h2>
            <p className="text-gray-600">{t('home.card_feed_desc')}</p>
          </Link>

          <Link
            href={`/${locale}/questions`}
            className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer"
          >
            <h2 className="text-xl font-semibold mb-2">{t('home.card_answer_title')}</h2>
            <p className="text-gray-600">{t('home.card_answer_desc')}</p>
          </Link>
        </div>

        <div className="mt-12 flex flex-col md:flex-row gap-4 justify-center">
          <Link
            href={`/${locale}/create-question`}
            className="inline-block bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition text-center"
          >
            {t('home.cta_ask')}
          </Link>
          <Link
            href={`/${locale}/questions`}
            className="inline-block bg-gray-200 text-gray-900 px-8 py-3 rounded-lg font-semibold hover:bg-gray-300 transition text-center"
          >
            {t('home.cta_feed')}
          </Link>
        </div>
      </div>
    </main>
  );
}
