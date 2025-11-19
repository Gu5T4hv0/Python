"use client";

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import Link from 'next/link';
import { useParams, useRouter } from 'next/navigation';
import { useTranslation } from '@/components/TranslationsProvider';

interface Question {
  id: string;
  title: string;
  description: string;
  price: number;
  tags: string[];
  user_id: string;
  created_at: string;
  status: string;
  media_url?: string;
  author?: {
    display_name: string;
    email: string;
  };
}

interface Answer {
  id: string;
  body: string;
  media_url?: string;
  mentor_id: string;
  created_at: string;
  mentor?: {
    display_name: string;
    email: string;
  };
}

export default function LocalizedQuestionDetailPage() {
  const params = useParams();
  const router = useRouter();
  const questionId = params.id as string;
  const locale = params.locale as string;
  const { t } = useTranslation();

  const [question, setQuestion] = useState<Question | null>(null);
  const [answers, setAnswers] = useState<Answer[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [user, setUser] = useState<any>(null);
  const [showAnswerForm, setShowAnswerForm] = useState(false);
  const [answerContent, setAnswerContent] = useState('');
  const [submittingAnswer, setSubmittingAnswer] = useState(false);
  const [answerMediaType, setAnswerMediaType] = useState<'audio' | 'video' | 'none'>(
    'none',
  );
  const [answerMediaFile, setAnswerMediaFile] = useState<File | null>(null);
  const [answerMediaDuration, setAnswerMediaDuration] = useState<number | null>(null);
  const [answerError, setAnswerError] = useState<string | null>(null);

  const MAX_DURATION = 180; // 3min

  useEffect(() => {
    const fetchQuestion = async () => {
      try {
        setLoading(true);
        setError(null);

        const { data: questionData, error: qError } = await supabase
          .from('questions')
          .select(
            `id, title, description, price, tags, user_id, created_at, status, media_url`,
          )
          .eq('id', questionId)
          .single();

        if (qError) throw qError;

        const { data: authorData } = await supabase
          .from('profiles')
          .select('display_name, email')
          .eq('id', questionData.user_id)
          .single();

        const formattedQuestion = {
          ...questionData,
          author: authorData || { display_name: 'Anônimo', email: '' },
        };
        setQuestion(formattedQuestion);

        const { data: answersData, error: aError } = await supabase
          .from('answers')
          .select(`id, body, media_url, mentor_id, created_at`)
          .eq('question_id', questionId)
          .order('created_at', { ascending: false });

        if (aError) throw aError;

        const mentorIds = [...new Set(answersData?.map((a: any) => a.mentor_id) || [])];
        const { data: mentorsData } = await supabase
          .from('profiles')
          .select('id, display_name, email')
          .in('id', mentorIds);

        const mentorsMap = Object.fromEntries(
          mentorsData?.map((m: any) => [m.id, m]) || [],
        );

        const formattedAnswers =
          answersData?.map((a: any) => ({
            ...a,
            mentor:
              mentorsMap[a.mentor_id] || {
                display_name: 'Anônimo',
                email: '',
              },
          })) || [];

        setAnswers(formattedAnswers);

        const {
          data: { user: currentUser },
        } = await supabase.auth.getUser();
        setUser(currentUser);
      } catch (err: any) {
        setError(err?.message || t('question.error_load'));
      } finally {
        setLoading(false);
      }
    };

    if (questionId) fetchQuestion();
  }, [questionId, t]);

  const handleSubmitAnswer = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!user) {
      router.push(`/${locale}/auth/login?redirect=/${locale}/questions/${questionId}`);
      return;
    }

    if (!answerContent.trim()) {
      alert(t('question.answer_empty'));
      return;
    }

    if (
      answerMediaFile &&
      answerMediaDuration !== null &&
      answerMediaDuration > MAX_DURATION
    ) {
      setAnswerError(t('question.media_too_long'));
      return;
    }

    setSubmittingAnswer(true);
    try {
      let media_url: string | null = null;
      let media_type: 'audio' | 'video' | null = null;
      let media_duration_seconds: number | null = null;

      if (answerMediaFile) {
        const ext = answerMediaFile.name.split('.').pop();
        const key = `answers/${user.id}/${Date.now()}.${ext}`;

        const { data: uploadData, error: uploadError } = await supabase.storage
          .from('question-media')
          .upload(key, answerMediaFile as File, {
            cacheControl: '3600',
            upsert: false,
            contentType: answerMediaFile.type,
          });
        if (uploadError) {
          setAnswerError(`${t('question.media_upload_error')}: ${uploadError.message}`);
          setSubmittingAnswer(false);
          return;
        }
        const { data: publicUrlData } = supabase.storage
          .from('question-media')
          .getPublicUrl(uploadData.path);
        media_url = publicUrlData.publicUrl;
        media_type = answerMediaType === 'none' ? null : answerMediaType;
        media_duration_seconds = answerMediaDuration
          ? Math.floor(answerMediaDuration)
          : null;
      }

      const { error } = await supabase.from('answers').insert([
        {
          question_id: questionId,
          mentor_id: user.id,
          body: answerContent,
          media_url,
          media_type,
          media_duration_seconds,
        },
      ]);

      if (error) throw error;

      // Refetch answers (simplificado, sem otimização local para manter código claro)
      const { data: answersRefetch } = await supabase
        .from('answers')
        .select(`id, body, media_url, mentor_id, created_at`)
        .eq('question_id', questionId)
        .order('created_at', { ascending: false });

      const mentorIds = [...new Set(answersRefetch?.map((a: any) => a.mentor_id) || [])];
      const { data: mentorsData } = await supabase
        .from('profiles')
        .select('id, display_name, email')
        .in('id', mentorIds);

      const mentorsMap = Object.fromEntries(
        mentorsData?.map((m: any) => [m.id, m]) || [],
      );

      setAnswers(
        answersRefetch?.map((a: any) => ({
          ...a,
          mentor:
            mentorsMap[a.mentor_id] || { display_name: 'Anônimo', email: '' },
        })) || [],
      );

      setAnswerContent('');
      setShowAnswerForm(false);
      setAnswerMediaFile(null);
      setAnswerMediaType('none');
      setAnswerMediaDuration(null);
      setAnswerError(null);
    } catch (err: any) {
      alert(t('question.answer_submit_error') + ': ' + err?.message);
    } finally {
      setSubmittingAnswer(false);
    }
  };

  const formatDate = (date: string, withTime = false) => {
    const localeStr = locale === 'pt-BR' ? 'pt-BR' : 'en-US';
    const options: Intl.DateTimeFormatOptions = withTime
      ? {
          day: '2-digit',
          month: 'short',
          year: 'numeric',
          hour: '2-digit',
          minute: '2-digit',
        }
      : {
          day: '2-digit',
          month: 'short',
          year: 'numeric',
        };
    return new Date(date).toLocaleDateString(localeStr, options);
  };

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p className="text-gray-600">{t('question.loading')}</p>
      </main>
    );
  }

  if (error || !question) {
    return (
      <main className="min-h-screen bg-red-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-700 mb-4">❌ {error || t('question.not_found')}</p>
          <Link
            href={`/${locale}/questions`}
            className="text-blue-600 hover:underline"
          >
            {t('question.back_to_feed')}
          </Link>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-2xl mx-auto">
        {/* Back button */}
        <Link
          href={`/${locale}/questions`}
          className="text-blue-600 hover:underline text-sm mb-6 inline-block"
        >
          {t('question.back_to_feed')}
        </Link>

        {/* Pergunta */}
        <div className="bg-white rounded-lg shadow-md p-8 mb-8 border border-gray-200">
          <div className="flex justify-between items-start mb-4">
            <h1 className="text-3xl font-bold text-gray-900 flex-1">
              {question.title}
            </h1>
            <div className="text-right">
              <div className="text-2xl font-bold text-blue-600">
                R${question.price.toFixed(2)}
              </div>
              <div className="text-xs text-gray-500 mt-1">
                {formatDate(question.created_at)}
              </div>
            </div>
          </div>

          <p className="text-gray-700 mb-4">{question.description}</p>

          {question.tags && question.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-4">
              {question.tags.map((tag) => (
                <span
                  key={tag}
                  className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded"
                >
                  #{tag}
                </span>
              ))}
            </div>
          )}

          {question.media_url && (
            <div className="mb-4 p-4 bg-gray-100 rounded-lg">
              <p className="text-sm text-gray-600">
                📎
                <a
                  href={question.media_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 hover:underline ml-1"
                >
                  {t('question.view_media')}
                </a>
              </p>
            </div>
          )}

          <div className="pt-4 border-t border-gray-200">
            <p className="text-sm text-gray-600">
              <span className="font-semibold">{t('question.asked_by')}</span>{' '}
              {question.author?.display_name || 'Anônimo'}
            </p>
            <p className="text-sm text-gray-500 mt-1">{question.author?.email}</p>
          </div>
        </div>

        {/* Respostas */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            🎤 {t('question.answers_title')}
          </h2>

          {answers.length === 0 ? (
            <div className="bg-gray-50 rounded-lg p-8 text-center">
              <p className="text-gray-600 mb-4">{t('question.no_answers')}</p>
              <p className="text-sm text-gray-500">
                {t('question.no_answers_cta')}
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              {answers.map((answer) => (
                <div
                  key={answer.id}
                  className="bg-white rounded-lg shadow-sm p-6 border border-gray-200"
                >
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <p className="font-semibold text-gray-900">
                        {answer.mentor?.display_name}
                      </p>
                      <p className="text-sm text-gray-500">
                        {answer.mentor?.email}
                      </p>
                    </div>
                    <p className="text-xs text-gray-500">
                      {formatDate(answer.created_at, true)}
                    </p>
                  </div>

                  <p className="text-gray-700 mb-3">{answer.body}</p>

                  {answer.media_url && (
                    <p className="text-sm text-gray-600">
                      📎
                      <a
                        href={answer.media_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-600 hover:underline ml-1"
                      >
                        {t('question.view_answer_media')}
                      </a>
                    </p>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Formulário de resposta */}
        <div className="bg-white rounded-lg shadow-md p-8 border border-gray-200">
          <h3 className="text-xl font-bold text-gray-900 mb-4">
            {user ? t('question.answer_title') : t('question.login_to_answer')}
          </h3>

          {!user ? (
            <div className="text-center">
              <p className="text-gray-600 mb-4">
                {t('question.must_be_logged')}
              </p>
              <Link
                href={`/${locale}/auth/login?redirect=/${locale}/questions/${questionId}`}
                className="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
              >
                {t('question.login_button')}
              </Link>
            </div>
          ) : showAnswerForm ? (
            <form onSubmit={handleSubmitAnswer} className="space-y-4">
              <div>
                <label
                  htmlFor="content"
                  className="block text-sm font-medium text-gray-700 mb-2"
                >
                  {t('question.answer_label')}
                </label>
                <textarea
                  id="content"
                  value={answerContent}
                  onChange={(e) => setAnswerContent(e.target.value)}
                  placeholder={t('question.answer_placeholder')}
                  rows={5}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  required
                />
                <p className="text-xs text-gray-500 mt-1">
                  {t('question.answer_hint')}
                </p>
              </div>

              {/* Mídia opcional na resposta */}
              <div className="border-2 border-dashed border-gray-300 rounded-lg p-4">
                <p className="text-sm font-medium text-gray-700 mb-3">
                  {t('question.media_optional')}
                </p>
                <div className="flex gap-4 mb-3">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="radio"
                      checked={answerMediaType === 'audio'}
                      onChange={() => setAnswerMediaType('audio')}
                    />
                    <span className="text-sm">🎙️ {t('question.media_audio')}</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="radio"
                      checked={answerMediaType === 'video'}
                      onChange={() => setAnswerMediaType('video')}
                    />
                    <span className="text-sm">🎥 {t('question.media_video')}</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="radio"
                      checked={answerMediaType === 'none'}
                      onChange={() => setAnswerMediaType('none')}
                    />
                    <span className="text-sm">{t('question.media_none')}</span>
                  </label>
                </div>

                {answerMediaType !== 'none' && (
                  <div>
                    <input
                      type="file"
                      accept={
                        answerMediaType === 'audio'
                          ? 'audio/mpeg,audio/m4a,audio/mp4'
                          : 'video/mp4,video/quicktime'
                      }
                      onChange={(e) => {
                        const file = e.target.files?.[0] || null;
                        setAnswerError(null);
                        setAnswerMediaFile(file);
                        setAnswerMediaDuration(null);
                        if (!file) return;
                        const objUrl = URL.createObjectURL(file);
                        const isAudio = file.type.startsWith('audio');
                        const el = document.createElement(isAudio ? 'audio' : 'video');
                        el.preload = 'metadata';
                        el.src = objUrl;
                        el.onloadedmetadata = () => {
                          URL.revokeObjectURL(objUrl);
                          const d = Number(el.duration || 0);
                          setAnswerMediaDuration(Number.isFinite(d) ? d : null);
                          if (d && d > MAX_DURATION) {
                            setAnswerError(t('question.media_too_long'));
                            setAnswerMediaFile(null);
                            setAnswerMediaDuration(null);
                            e.currentTarget.value = '';
                          }
                        };
                        el.onerror = () => {
                          URL.revokeObjectURL(objUrl);
                          setAnswerError(t('question.media_duration_error'));
                        };
                      }}
                      className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                    />
                    {answerMediaFile && (
                      <div className="mt-2 p-3 bg-blue-50 rounded-lg">
                        <p className="text-sm text-gray-700">
                          📎 {answerMediaFile.name} ({
                            (answerMediaFile.size / 1024 / 1024).toFixed(2)
                          }
                          MB)
                        </p>
                        {answerMediaDuration !== null && (
                          <p className="text-xs text-gray-600 mt-1">
                            {t('question.media_duration_label')}{' '}
                            {Math.floor(answerMediaDuration / 60)}:
                            {String(Math.floor(answerMediaDuration % 60)).padStart(2, '0')}
                          </p>
                        )}
                      </div>
                    )}
                    <p className="text-xs text-gray-500 mt-2">
                      {t('question.media_limit')}
                    </p>
                    {answerError && (
                      <p className="text-red-500 text-sm mt-2">{answerError}</p>
                    )}
                  </div>
                )}
              </div>

              <div className="flex gap-3">
                <button
                  type="submit"
                  disabled={submittingAnswer}
                  className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400 transition"
                >
                  {submittingAnswer
                    ? t('question.sending_answer')
                    : t('question.submit_answer')}
                </button>
                <button
                  type="button"
                  onClick={() => setShowAnswerForm(false)}
                  className="px-4 py-2 border border-gray-300 rounded-lg font-semibold hover:bg-gray-50 transition"
                >
                  {t('question.cancel')}
                </button>
              </div>
            </form>
          ) : (
            <button
              onClick={() => setShowAnswerForm(true)}
              className="w-full bg-blue-600 text-white px-4 py-3 rounded-lg font-semibold hover:bg-blue-700 transition"
            >
              {t('question.cta_answer')}
            </button>
          )}
        </div>
      </div>
    </main>
  );
}

