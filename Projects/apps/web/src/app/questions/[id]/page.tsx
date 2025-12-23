'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import Link from 'next/link';
import { useParams, useRouter } from 'next/navigation';

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
  is_best_answer?: boolean;
  rating?: number;
  mentor?: {
    display_name: string;
    email: string;
  };
}

interface SuggestedMentor {
  id: string;
  display_name: string;
  email: string;
  bio?: string;
  avatar_url?: string;
  mentor_tags: string[];
  mentor_rate: number;
  matchingTags: string[];
  score: number;
}

export default function QuestionDetailPage() {
  const params = useParams();
  const router = useRouter();
  const questionId = params.id as string;

  const [question, setQuestion] = useState<Question | null>(null);
  const [answers, setAnswers] = useState<Answer[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [user, setUser] = useState<any>(null);
  const [showAnswerForm, setShowAnswerForm] = useState(false);
  const [answerContent, setAnswerContent] = useState('');
  const [submittingAnswer, setSubmittingAnswer] = useState(false);
  const [answerMediaType, setAnswerMediaType] = useState<'audio' | 'video' | 'none'>('none');
  const [answerMediaFile, setAnswerMediaFile] = useState<File | null>(null);
  const [answerMediaDuration, setAnswerMediaDuration] = useState<number | null>(null);
  const [answerError, setAnswerError] = useState<string | null>(null);
  const [suggestedMentors, setSuggestedMentors] = useState<SuggestedMentor[]>([]);
  const [loadingMentors, setLoadingMentors] = useState(false);
  const [isUserMentor, setIsUserMentor] = useState<boolean | null>(null);
  const [followingMentors, setFollowingMentors] = useState<Set<string>>(new Set());

  const MAX_DURATION = 180; // 3min

  useEffect(() => {
    const fetchQuestion = async () => {
      try {
        setLoading(true);
        setError(null);

        // Fetch question
        const { data: questionData, error: qError } = await supabase
          .from('questions')
          .select(
            `
            id,
            title,
            description,
            price,
            tags,
            user_id,
            created_at,
            status,
            media_url
          `
          )
          .eq('id', questionId)
          .single();

        if (qError) throw qError;

        // Buscar dados do autor
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

        // Fetch answers
        const { data: answersData, error: aError } = await supabase
          .from('answers')
          .select(
            `
            id,
            body,
            media_url,
            mentor_id,
            created_at,
            is_best_answer,
            rating
          `
          )
          .eq('question_id', questionId)
          .order('is_best_answer', { ascending: false })
          .order('created_at', { ascending: false });

        if (aError) throw aError;

        // Buscar dados dos mentores
        const mentorIds = [...new Set(answersData?.map((a: any) => a.mentor_id) || [])];
        const { data: mentorsData } = await supabase
          .from('profiles')
          .select('id, display_name, email')
          .in('id', mentorIds);

        const mentorsMap = Object.fromEntries(
          mentorsData?.map((m: any) => [m.id, m]) || []
        );

        const formattedAnswers = answersData?.map((a: any) => ({
          ...a,
          mentor: mentorsMap[a.mentor_id] || { display_name: 'Anônimo', email: '' },
        })) || [];

        setAnswers(formattedAnswers);

        // Get current user
        const { data: { user: currentUser } } = await supabase.auth.getUser();
        setUser(currentUser);

        // Verificar se o usuário é mentor
        if (currentUser) {
          const { data: userProfile } = await supabase
            .from('profiles')
            .select('is_mentor')
            .eq('id', currentUser.id)
            .single();
          
          setIsUserMentor(userProfile?.is_mentor || false);
        } else {
          setIsUserMentor(null);
        }

        // Buscar mentores sugeridos se houver tags
        if (formattedQuestion.tags && formattedQuestion.tags.length > 0) {
          setLoadingMentors(true);
          try {
            const mentorResponse = await fetch('/api/mentors/match', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ tags: formattedQuestion.tags, questionId }),
            });
            const mentorData = await mentorResponse.json();
            if (mentorData.mentors) {
              setSuggestedMentors(mentorData.mentors);

              // Verificar quais mentores o usuário está seguindo
              if (currentUser && mentorData.mentors.length > 0) {
                const mentorIds = mentorData.mentors.map((m: any) => m.id);
                const followChecks = await Promise.all(
                  mentorIds.map(async (mentorId: string) => {
                    try {
                      const res = await fetch('/api/follows/status', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ follower_id: currentUser.id, mentor_id: mentorId }),
                      });
                      const data = await res.json();
                      return { mentorId, following: data.following };
                    } catch {
                      return { mentorId, following: false };
                    }
                  })
                );
                const followingSet = new Set(
                  followChecks.filter((c) => c.following).map((c) => c.mentorId)
                );
                setFollowingMentors(followingSet);
              }
            }
          } catch (err) {
            console.error('Erro ao buscar mentores:', err);
          } finally {
            setLoadingMentors(false);
          }
        }
      } catch (err: any) {
        setError(err?.message || 'Erro ao carregar pergunta');
      } finally {
        setLoading(false);
      }
    };

    if (questionId) fetchQuestion();
  }, [questionId]);

  const handleSubmitAnswer = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!user) {
      router.push('/auth/login');
      return;
    }

    // Verificar se é mentor
    if (!isUserMentor) {
      alert('Apenas mentores podem responder perguntas. Torne-se um mentor em /mentor/profile');
      return;
    }

    if (!answerContent.trim()) {
      alert('Resposta não pode ser vazia');
      return;
    }

    // Validate media duration if present
    if (answerMediaFile && answerMediaDuration !== null && answerMediaDuration > MAX_DURATION) {
      setAnswerError('Duração máxima de 3 minutos excedida.');
      return;
    }

    setSubmittingAnswer(true);
    try {
      // Optional upload first
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
          setAnswerError(`Erro ao enviar mídia: ${uploadError.message}`);
          setSubmittingAnswer(false);
          return;
        }
        const { data: publicUrlData } = supabase.storage
          .from('question-media')
          .getPublicUrl(uploadData.path);
        media_url = publicUrlData.publicUrl;
        media_type = answerMediaType === 'none' ? null : answerMediaType;
        media_duration_seconds = answerMediaDuration ? Math.floor(answerMediaDuration) : null;
      }

      // Usar API route para validar se é mentor
      const response = await fetch('/api/answers/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question_id: questionId,
          mentor_id: user.id,
          body: answerContent,
          media_url,
          media_type,
          media_duration_seconds,
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || 'Erro ao criar resposta');
      }

      // Atualizar lista de respostas
      setAnswers([
        {
          id: `temp-${Date.now()}`,
          body: answerContent,
          mentor_id: user.id,
          created_at: new Date().toISOString(),
          mentor: {
            display_name: user.user_metadata?.display_name || user.email,
            email: user.email,
          },
        },
        ...answers,
      ]);

      setAnswerContent('');
      setShowAnswerForm(false);
      setAnswerMediaFile(null);
      setAnswerMediaType('none');
      setAnswerMediaDuration(null);
      setAnswerError(null);

      // Refetch para atualizar ID real
      const { data: answersRefetch } = await supabase
        .from('answers')
        .select(
          `
          id,
          body,
          media_url,
          mentor_id,
          created_at
        `
        )
        .eq('question_id', questionId)
        .order('created_at', { ascending: false });

      // Buscar mentores para refetch
      const mentorIds = [...new Set(answersRefetch?.map((a: any) => a.mentor_id) || [])];
      const { data: mentorsData } = await supabase
        .from('profiles')
        .select('id, display_name, email')
        .in('id', mentorIds);

      const mentorsMap = Object.fromEntries(
        mentorsData?.map((m: any) => [m.id, m]) || []
      );

      setAnswers(
        answersRefetch?.map((a: any) => ({
          ...a,
          mentor: mentorsMap[a.mentor_id] || { display_name: 'Anônimo', email: '' },
        })) || []
      );
    } catch (err: any) {
      alert('Erro ao enviar resposta: ' + err?.message);
    } finally {
      setSubmittingAnswer(false);
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p className="text-gray-600">Carregando...</p>
      </main>
    );
  }

  if (error || !question) {
    return (
      <main className="min-h-screen bg-red-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-700 mb-4">❌ {error || 'Pergunta não encontrada'}</p>
          <Link href="/questions" className="text-blue-600 hover:underline">
            ← Voltar para o feed
          </Link>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-2xl mx-auto">
        {/* Back button */}
        <Link href="/questions" className="text-blue-600 hover:underline text-sm mb-6 inline-block">
          ← Voltar para o feed
        </Link>

        {/* Pergunta */}
        <div className="bg-white rounded-lg shadow-md p-8 mb-8 border border-gray-200">
          <div className="flex justify-between items-start mb-4">
            <h1 className="text-3xl font-bold text-gray-900 flex-1">{question.title}</h1>
            <div className="text-right">
              <div className="text-2xl font-bold text-blue-600">R${question.price.toFixed(2)}</div>
              <div className="text-xs text-gray-500 mt-1">
                {new Date(question.created_at).toLocaleDateString('pt-BR')}
              </div>
            </div>
          </div>

          <p className="text-gray-700 mb-4">{question.description}</p>

          {question.tags && question.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-4">
              {question.tags.map((tag) => (
                <span key={tag} className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">
                  #{tag}
                </span>
              ))}
            </div>
          )}

          {question.media_url && (
            <div className="mb-4 p-4 bg-gray-100 rounded-lg">
              <p className="text-sm text-gray-600">
                📎 <a href={question.media_url} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                  Ver mídia anexada
                </a>
              </p>
            </div>
          )}

          <div className="pt-4 border-t border-gray-200">
            <p className="text-sm text-gray-600">
              <span className="font-semibold">Perguntado por:</span> {question.author?.display_name || 'Anônimo'}
            </p>
            <p className="text-sm text-gray-500 mt-1">{question.author?.email}</p>
          </div>
        </div>

        {/* Mentores Sugeridos */}
        {suggestedMentors.length > 0 && (
          <div className="bg-white rounded-lg shadow-md p-6 mb-8 border border-gray-200">
            <h2 className="text-xl font-bold text-gray-900 mb-4">
              👥 Mentores Sugeridos para esta Pergunta
            </h2>
            <p className="text-sm text-gray-600 mb-4">
              Estes mentores têm experiência nas tags desta pergunta:
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {suggestedMentors.slice(0, 4).map((mentor) => {
                const isFollowing = followingMentors.has(mentor.id);
                return (
                  <div
                    key={mentor.id}
                    className="border border-gray-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-sm transition"
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <Link
                          href={`/mentor/${mentor.id}`}
                          className="block hover:underline"
                        >
                          <h3 className="font-semibold text-gray-900">{mentor.display_name}</h3>
                        </Link>
                        <p className="text-xs text-gray-500 mb-2">{mentor.email}</p>
                        {mentor.bio && (
                          <p className="text-sm text-gray-600 mb-2 line-clamp-2">{mentor.bio}</p>
                        )}
                        <div className="flex flex-wrap gap-1 mb-2">
                          {mentor.matchingTags.map((tag) => (
                            <span
                              key={tag}
                              className="text-xs bg-green-100 text-green-800 px-2 py-0.5 rounded"
                            >
                              #{tag}
                            </span>
                          ))}
                        </div>
                        <p className="text-xs text-gray-500 mb-2">
                          Taxa: R$ {Number(mentor.mentor_rate).toFixed(2)} • Match: {mentor.score} tag{mentor.score !== 1 ? 's' : ''}
                        </p>
                        {user && user.id !== mentor.id && (
                          <button
                            onClick={async () => {
                              try {
                                const response = await fetch('/api/follows/toggle', {
                                  method: 'POST',
                                  headers: { 'Content-Type': 'application/json' },
                                  body: JSON.stringify({
                                    follower_id: user.id,
                                    mentor_id: mentor.id,
                                  }),
                                });
                                const data = await response.json();
                                if (response.ok) {
                                  setFollowingMentors((prev) => {
                                    const newSet = new Set(prev);
                                    if (data.following) {
                                      newSet.add(mentor.id);
                                    } else {
                                      newSet.delete(mentor.id);
                                    }
                                    return newSet;
                                  });
                                }
                              } catch (err) {
                                console.error('Erro ao seguir:', err);
                              }
                            }}
                            className={`text-xs px-3 py-1 rounded transition ${
                              isFollowing
                                ? 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                                : 'bg-blue-100 text-blue-700 hover:bg-blue-200'
                            }`}
                          >
                            {isFollowing ? '✓ Seguindo' : '+ Seguir'}
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Respostas */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            🎤 {answers.length} Resposta{answers.length !== 1 ? 's' : ''}
          </h2>

          {answers.length === 0 ? (
            <div className="bg-gray-50 rounded-lg p-8 text-center">
              <p className="text-gray-600 mb-4">Nenhuma resposta ainda</p>
              <p className="text-sm text-gray-500">Seja o primeiro mentor a responder!</p>
            </div>
          ) : (
            <div className="space-y-4">
              {answers.map((answer) => (
                <div
                  key={answer.id}
                  className={`bg-white rounded-lg shadow-sm p-6 border ${
                    answer.is_best_answer
                      ? 'border-yellow-400 bg-yellow-50'
                      : 'border-gray-200'
                  }`}
                >
                  <div className="flex justify-between items-start mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-2">
                        <p className="font-semibold text-gray-900">{answer.mentor?.display_name}</p>
                        {answer.is_best_answer && (
                          <span className="text-xs bg-yellow-400 text-yellow-900 px-2 py-1 rounded font-semibold">
                            ⭐ Melhor Resposta
                          </span>
                        )}
                      </div>
                      <p className="text-sm text-gray-500">{answer.mentor?.email}</p>
                      {answer.rating && (
                        <div className="flex items-center gap-1 mt-1">
                          <span className="text-xs text-gray-600">Avaliação:</span>
                          {[...Array(5)].map((_, i) => (
                            <span key={i} className={i < answer.rating! ? 'text-yellow-400' : 'text-gray-300'}>
                              ⭐
                            </span>
                          ))}
                          <span className="text-xs text-gray-500">({answer.rating}/5)</span>
                        </div>
                      )}
                    </div>
                    <p className="text-xs text-gray-500">
                      {new Date(answer.created_at).toLocaleDateString('pt-BR', {
                        day: '2-digit',
                        month: 'short',
                        year: 'numeric',
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </p>
                  </div>

                  <p className="text-gray-700 mb-3">{answer.body}</p>

                  {answer.media_url && (
                    <p className="text-sm text-gray-600 mb-3">
                      📎 <a href={answer.media_url} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                        Ver resposta em áudio/vídeo
                      </a>
                    </p>
                  )}

                  {/* Ações do autor da pergunta */}
                  {user && user.id === question.user_id && (
                    <div className="pt-3 border-t border-gray-200 space-y-2">
                      {question.status === 'open' && (
                        <>
                          <button
                            onClick={async () => {
                              if (!confirm(`Aceitar esta resposta? O mentor receberá R$ ${(question.price * 0.8).toFixed(2)} (80% do valor).`)) {
                                return;
                              }
                              try {
                                const response = await fetch('/api/transactions/create', {
                                  method: 'POST',
                                  headers: { 'Content-Type': 'application/json' },
                                  body: JSON.stringify({
                                    question_id: question.id,
                                    answer_id: answer.id,
                                    mentor_id: answer.mentor_id,
                                  }),
                                });
                                const data = await response.json();
                                if (response.ok) {
                                  alert('Resposta aceita! Transação criada com sucesso.');
                                  window.location.reload();
                                } else {
                                  alert('Erro ao aceitar resposta: ' + (data.error || 'Erro desconhecido'));
                                }
                              } catch (err: any) {
                                alert('Erro ao aceitar resposta: ' + err.message);
                              }
                            }}
                            className="bg-green-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-green-700 transition text-sm mr-2"
                          >
                            ✓ Aceitar Resposta (Pagar R$ {question.price.toFixed(2)})
                          </button>
                          <button
                            onClick={async () => {
                              try {
                                const response = await fetch('/api/answers/mark-best', {
                                  method: 'POST',
                                  headers: { 'Content-Type': 'application/json' },
                                  body: JSON.stringify({
                                    answer_id: answer.id,
                                    question_id: question.id,
                                    user_id: user.id,
                                  }),
                                });
                                if (response.ok) {
                                  window.location.reload();
                                } else {
                                  const data = await response.json();
                                  alert('Erro: ' + (data.error || 'Erro desconhecido'));
                                }
                              } catch (err: any) {
                                alert('Erro: ' + err.message);
                              }
                            }}
                            className={`px-4 py-2 rounded-lg font-semibold transition text-sm ${
                              answer.is_best_answer
                                ? 'bg-yellow-200 text-yellow-900 hover:bg-yellow-300'
                                : 'bg-yellow-100 text-yellow-800 hover:bg-yellow-200'
                            }`}
                          >
                            {answer.is_best_answer ? '⭐ Melhor Resposta' : '⭐ Marcar como Melhor'}
                          </button>
                        </>
                      )}
                      {question.status === 'answered' && !answer.rating && (
                        <div className="flex items-center gap-2">
                          <span className="text-sm text-gray-600">Avaliar resposta:</span>
                          {[1, 2, 3, 4, 5].map((rating) => (
                            <button
                              key={rating}
                              onClick={async () => {
                                try {
                                  const response = await fetch('/api/answers/rate', {
                                    method: 'POST',
                                    headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify({
                                      answer_id: answer.id,
                                      rating,
                                      user_id: user.id,
                                    }),
                                  });
                                  if (response.ok) {
                                    window.location.reload();
                                  }
                                } catch (err) {
                                  console.error('Erro ao avaliar:', err);
                                }
                              }}
                              className="text-2xl hover:scale-110 transition"
                            >
                              ⭐
                            </button>
                          ))}
                        </div>
                      )}
                      {question.status === 'open' && (
                        <p className="text-xs text-gray-500 mt-2">
                          Mentor receberá R$ {(question.price * 0.8).toFixed(2)} • Plataforma: R$ {(question.price * 0.2).toFixed(2)}
                        </p>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Formulário de resposta */}
        <div className="bg-white rounded-lg shadow-md p-8 border border-gray-200">
          <h3 className="text-xl font-bold text-gray-900 mb-4">
            {user ? (isUserMentor ? '📝 Sua Resposta' : '👤 Torne-se um Mentor') : '🔐 Faça Login para Responder'}
          </h3>

          {!user ? (
            <div className="text-center">
              <p className="text-gray-600 mb-4">Você precisa estar autenticado para responder</p>
              <Link
                href={`/auth/login?redirect=/questions/${questionId}`}
                className="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
              >
                Faça Login
              </Link>
            </div>
          ) : !isUserMentor ? (
            <div className="text-center bg-yellow-50 border border-yellow-200 rounded-lg p-6">
              <p className="text-yellow-800 mb-4 font-semibold">
                ⚠️ Apenas mentores podem responder perguntas
              </p>
              <p className="text-yellow-700 mb-4 text-sm">
                Torne-se um mentor para começar a responder perguntas e ganhar dinheiro!
              </p>
              <Link
                href="/mentor/profile"
                className="inline-block bg-yellow-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-yellow-700 transition"
              >
                Tornar-se Mentor
              </Link>
            </div>
          ) : showAnswerForm ? (
            <form onSubmit={handleSubmitAnswer} className="space-y-4">
              <div>
                <label htmlFor="content" className="block text-sm font-medium text-gray-700 mb-2">
                  Sua resposta *
                </label>
                <textarea
                  id="content"
                  value={answerContent}
                  onChange={(e) => setAnswerContent(e.target.value)}
                  placeholder="Escreva uma resposta concisa e útil..."
                  rows={5}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  required
                />
                <p className="text-xs text-gray-500 mt-1">
                  Dica: Seja conciso, objetivo e útil. Respostas com áudio/vídeo aparecem como links.
                </p>
              </div>

              {/* Mídia opcional na resposta */}
              <div className="border-2 border-dashed border-gray-300 rounded-lg p-4">
                <p className="text-sm font-medium text-gray-700 mb-3">Adicionar mídia (opcional)</p>
                <div className="flex gap-4 mb-3">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="radio" checked={answerMediaType === 'audio'} onChange={() => setAnswerMediaType('audio')} />
                    <span className="text-sm">🎙️ Áudio</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="radio" checked={answerMediaType === 'video'} onChange={() => setAnswerMediaType('video')} />
                    <span className="text-sm">🎥 Vídeo</span>
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="radio" checked={answerMediaType === 'none'} onChange={() => setAnswerMediaType('none')} />
                    <span className="text-sm">Nenhum</span>
                  </label>
                </div>

                {answerMediaType !== 'none' && (
                  <div>
                    <input
                      type="file"
                      accept={answerMediaType === 'audio' ? 'audio/mpeg,audio/m4a,audio/mp4' : 'video/mp4,video/quicktime'}
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
                            setAnswerError('Duração máxima de 3 minutos excedida.');
                            setAnswerMediaFile(null);
                            setAnswerMediaDuration(null);
                            e.currentTarget.value = '';
                          }
                        };
                        el.onerror = () => {
                          URL.revokeObjectURL(objUrl);
                          setAnswerError('Não foi possível ler a duração da mídia.');
                        };
                      }}
                      className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                    />
                    {answerMediaFile && (
                      <div className="mt-2 p-3 bg-blue-50 rounded-lg">
                        <p className="text-sm text-gray-700">📎 {answerMediaFile.name} ({(answerMediaFile.size / 1024 / 1024).toFixed(2)}MB)</p>
                        {answerMediaDuration !== null && (
                          <p className="text-xs text-gray-600 mt-1">Duração: {Math.floor(answerMediaDuration / 60)}:{String(Math.floor(answerMediaDuration % 60)).padStart(2, '0')}</p>
                        )}
                      </div>
                    )}
                    <p className="text-xs text-gray-500 mt-2">Máximo 3 minutos, 50MB</p>
                    {answerError && <p className="text-red-500 text-sm mt-2">{answerError}</p>}
                  </div>
                )}
              </div>

              <div className="flex gap-3">
                <button
                  type="submit"
                  disabled={submittingAnswer}
                  className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400 transition"
                >
                  {submittingAnswer ? '⏳ Enviando...' : '✓ Enviar Resposta'}
                </button>
                <button
                  type="button"
                  onClick={() => setShowAnswerForm(false)}
                  className="px-4 py-2 border border-gray-300 rounded-lg font-semibold hover:bg-gray-50 transition"
                >
                  Cancelar
                </button>
              </div>
            </form>
          ) : (
            <button
              onClick={() => setShowAnswerForm(true)}
              className="w-full bg-blue-600 text-white px-4 py-3 rounded-lg font-semibold hover:bg-blue-700 transition"
            >
              💬 Responder esta Pergunta
            </button>
          )}
        </div>
      </div>
    </main>
  );
}
