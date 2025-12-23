'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';

interface MentorProfile {
  id: string;
  display_name: string;
  email: string;
  bio: string;
  avatar_url: string;
  mentor_tags: string[];
  mentor_rate: number;
  is_mentor: boolean;
}

interface MentorStats {
  totalAnswers: number;
  followerCount: number;
}

export default function PublicMentorProfilePage() {
  const params = useParams();
  const router = useRouter();
  const mentorId = params.id as string;
  
  const [mentor, setMentor] = useState<MentorProfile | null>(null);
  const [stats, setStats] = useState<MentorStats>({ totalAnswers: 0, followerCount: 0 });
  const [loading, setLoading] = useState(true);
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [isFollowing, setIsFollowing] = useState(false);
  const [loadingFollow, setLoadingFollow] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);

        // Buscar perfil do mentor
        const { data: mentorData, error: mError } = await supabase
          .from('profiles')
          .select('*')
          .eq('id', mentorId)
          .single();

        if (mError || !mentorData || !mentorData.is_mentor) {
          router.push('/questions');
          return;
        }

        setMentor(mentorData);

        // Buscar estatísticas
        const { data: answersData } = await supabase
          .from('answers')
          .select('id')
          .eq('mentor_id', mentorId);

        const followerCountRes = await fetch('/api/follows/count', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ mentor_id: mentorId }),
        });
        const followerData = await followerCountRes.json();

        setStats({
          totalAnswers: answersData?.length || 0,
          followerCount: followerData.count || 0,
        });

        // Verificar usuário atual e se está seguindo
        const { data: { user } } = await supabase.auth.getUser();
        setCurrentUser(user);

        if (user && user.id !== mentorId) {
          const followStatusRes = await fetch('/api/follows/status', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ follower_id: user.id, mentor_id: mentorId }),
          });
          const followStatus = await followStatusRes.json();
          setIsFollowing(followStatus.following || false);
        }
      } catch (err: any) {
        console.error('Erro ao carregar perfil:', err);
      } finally {
        setLoading(false);
      }
    };

    if (mentorId) fetchData();
  }, [mentorId, router]);

  const handleToggleFollow = async () => {
    if (!currentUser) {
      router.push('/auth/login?redirect=/mentor/' + mentorId);
      return;
    }

    setLoadingFollow(true);
    try {
      const response = await fetch('/api/follows/toggle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          follower_id: currentUser.id,
          mentor_id: mentorId,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        setIsFollowing(data.following);
        setStats((prev) => ({
          ...prev,
          followerCount: data.following ? prev.followerCount + 1 : prev.followerCount - 1,
        }));
      } else {
        alert('Erro: ' + (data.error || 'Erro desconhecido'));
      }
    } catch (err: any) {
      alert('Erro ao seguir/deixar de seguir: ' + err.message);
    } finally {
      setLoadingFollow(false);
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p className="text-gray-600">Carregando...</p>
      </main>
    );
  }

  if (!mentor) {
    return (
      <main className="min-h-screen bg-red-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-700 mb-4">Mentor não encontrado</p>
          <Link href="/questions" className="text-blue-600 hover:underline">
            ← Voltar para o feed
          </Link>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <Link href="/questions" className="text-blue-600 hover:underline text-sm mb-6 inline-block">
          ← Voltar para o feed
        </Link>

        <div className="bg-white rounded-lg shadow-md p-8 mb-8 border border-gray-200">
          <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-6">
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{mentor.display_name}</h1>
              <p className="text-gray-600 mb-4">{mentor.email}</p>
              
              {mentor.bio && (
                <p className="text-gray-700 mb-4">{mentor.bio}</p>
              )}

              {mentor.mentor_tags && mentor.mentor_tags.length > 0 && (
                <div className="flex flex-wrap gap-2 mb-4">
                  {mentor.mentor_tags.map((tag) => (
                    <span key={tag} className="text-xs bg-blue-100 text-blue-800 px-3 py-1 rounded-full">
                      #{tag}
                    </span>
                  ))}
                </div>
              )}

              <div className="flex gap-6 text-sm text-gray-600">
                <div>
                  <span className="font-semibold">{stats.totalAnswers}</span> respostas
                </div>
                <div>
                  <span className="font-semibold">{stats.followerCount}</span> seguidores
                </div>
                <div>
                  Taxa: <span className="font-semibold">R$ {Number(mentor.mentor_rate).toFixed(2)}</span>
                </div>
              </div>
            </div>

            {currentUser && currentUser.id !== mentorId && (
              <button
                onClick={handleToggleFollow}
                disabled={loadingFollow}
                className={`px-6 py-3 rounded-lg font-semibold transition shadow-sm ${
                  isFollowing
                    ? 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                    : 'bg-blue-600 text-white hover:bg-blue-700'
                }`}
              >
                {loadingFollow ? '⏳' : isFollowing ? '✓ Seguindo' : '+ Seguir'}
              </button>
            )}
          </div>
        </div>

        {/* Respostas recentes do mentor */}
        <div className="bg-white rounded-lg shadow-md p-8 border border-gray-200">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Respostas Recentes</h2>
          <p className="text-gray-600 text-sm">
            Este mentor ainda não tem respostas públicas ou você precisa estar autenticado para ver.
          </p>
        </div>
      </div>
    </main>
  );
}

