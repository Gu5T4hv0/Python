'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import Link from 'next/link';

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
  answer_count?: number;
}

export default function QuestionsGrid() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        setLoading(true);
        setError(null);

        let query = supabase
          .from('questions')
          .select(`
            id,
            title,
            description,
            price,
            tags,
            user_id,
            created_at,
            status,
            media_url
          `)
          .eq('status', 'open')
          .order('created_at', { ascending: false });

        if (selectedTag) {
          query = query.contains('tags', [selectedTag]);
        }

        const { data, error: fetchError } = await query;

        if (fetchError) throw fetchError;

        // Buscar dados dos autores separadamente
        const userIds = [...new Set(data?.map((q: any) => q.user_id) || [])];
        const { data: profilesData } = await supabase
          .from('profiles')
          .select('id, display_name, email')
          .in('id', userIds);

        const profilesMap = Object.fromEntries(
          profilesData?.map((p: any) => [p.id, p]) || []
        );

        const formattedQuestions = data?.map((q: any) => ({
          ...q,
          author: profilesMap[q.user_id] || { display_name: 'Anônimo', email: '' },
        })) || [];

        setQuestions(formattedQuestions);
      } catch (err: any) {
        setError(err?.message || 'Erro ao carregar perguntas');
      } finally {
        setLoading(false);
      }
    };

    fetchQuestions();
  }, [selectedTag]);

  // Extrair tags únicas
  const allTags = Array.from(
    new Set(questions.flatMap((q) => q.tags || []))
  );

  const formatDate = (date: string) => {
    return new Date(date).toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
    });
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <p className="text-gray-600">Carregando perguntas...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-red-50 p-4">
        <div className="max-w-4xl mx-auto">
          <div className="bg-red-100 border border-red-400 text-red-700 p-4 rounded">
            ❌ Erro: {error}
          </div>
        </div>
      </div>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            🎤 Feed de Perguntas
          </h1>
          <p className="text-gray-600">
            {questions.length} pergunta{questions.length !== 1 ? 's' : ''} aberta
            {questions.length !== 1 ? 's' : ''}
          </p>
        </div>

        {/* Filtro por tags */}
        {allTags.length > 0 && (
          <div className="mb-8">
            <p className="text-sm font-semibold text-gray-700 mb-3">Filtrar por tags:</p>
            <div className="flex flex-wrap gap-2">
              <button
                onClick={() => setSelectedTag(null)}
                className={`px-3 py-1 rounded-full text-sm transition ${
                  selectedTag === null
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                Todas
              </button>
              {allTags.map((tag) => (
                <button
                  key={tag}
                  onClick={() => setSelectedTag(tag)}
                  className={`px-3 py-1 rounded-full text-sm transition ${
                    selectedTag === tag
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  {tag}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Lista de perguntas */}
        {questions.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-600 mb-4">Nenhuma pergunta encontrada</p>
            <Link
              href="/create-question"
              className="inline-block text-blue-600 hover:underline font-semibold"
            >
              Seja o primeiro a fazer uma pergunta →
            </Link>
          </div>
        ) : (
          <div className="space-y-4">
            {questions.map((question) => (
              <Link key={question.id} href={`/questions/${question.id}`}>
                <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition p-6 cursor-pointer border border-gray-200">
                  {/* Título */}
                  <h2 className="text-xl font-semibold text-gray-900 mb-2 hover:text-blue-600">
                    {question.title}
                  </h2>

                  {/* Descrição (primeiras 150 chars) */}
                  <p className="text-gray-600 text-sm mb-3 line-clamp-2">
                    {question.description}
                  </p>

                  {/* Tags */}
                  {question.tags && question.tags.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-3">
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

                  {/* Footer */}
                  <div className="flex justify-between items-center pt-3 border-t border-gray-100">
                    <div className="text-sm text-gray-500">
                      <span className="font-semibold">
                        R${question.price.toFixed(2)}
                      </span>
                      {' • '}
                      {formatDate(question.created_at)}
                    </div>
                    <div className="text-sm">
                      <span className="text-blue-600 font-semibold">
                        {question.author?.display_name || 'Anônimo'}
                      </span>
                    </div>
                  </div>

                  {/* Media indicator */}
                  {question.media_url && (
                    <div className="mt-3 text-xs text-gray-500">
                      📎 Contém mídia
                    </div>
                  )}
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
