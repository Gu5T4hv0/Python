"use client";

import CreateQuestionForm from '@/components/CreateQuestionForm';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import { useRouter, useParams } from 'next/navigation';
import { useTranslation } from '@/components/TranslationsProvider';

export default function CreateQuestionPage() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const params = useParams();
  const { t } = useTranslation();
  const locale = params?.locale as string;

  useEffect(() => {
    const checkAuth = async () => {
      const {
        data: { user },
      } = await supabase.auth.getUser();
      if (!user) {
        router.push(`/${locale}/auth/login?redirect=/${locale}/create-question`);
      } else {
        setUser(user);
      }
      setLoading(false);
    };
    checkAuth();
  }, [router, locale]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white flex items-center justify-center">
        <p className="text-gray-600">{t('common.loading')}</p>
      </main>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="mb-8">
          <Link
            href={`/${locale}`}
            className="text-blue-600 hover:underline text-sm"
          >
            {t('create.back_home')}
          </Link>
          <h1 className="text-4xl font-bold text-gray-900 mt-4">
            {t('create.title')}
          </h1>
          <p className="text-gray-600 mt-2">{t('create.description')}</p>
        </div>

        {/* Tips */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-8">
          <h2 className="font-semibold text-blue-900 mb-2">
            {t('create.tips_title')}
          </h2>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>{t('create.tips_item_1')}</li>
            <li>{t('create.tips_item_2')}</li>
            <li>{t('create.tips_item_3')}</li>
            <li>{t('create.tips_item_4')}</li>
          </ul>
        </div>

        <div className="bg-white rounded-lg shadow-md p-8">
          <CreateQuestionForm />
        </div>

        {/* FAQ */}
        <div className="mt-12 bg-gray-50 rounded-lg p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">
            {t('create.faq_title')}
          </h2>
          <div className="space-y-4 text-sm text-gray-700">
            <div>
              <p className="font-semibold">{t('create.faq_price_q')}</p>
              <p>{t('create.faq_price_a')}</p>
            </div>
            <div>
              <p className="font-semibold">{t('create.faq_media_q')}</p>
              <p>{t('create.faq_media_a')}</p>
            </div>
            <div>
              <p className="font-semibold">{t('create.faq_payment_q')}</p>
              <p>{t('create.faq_payment_a')}</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
