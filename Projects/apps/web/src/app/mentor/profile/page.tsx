'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

interface MentorStats {
  totalAnswers: number;
  totalEarnings: number;
  pendingEarnings: number;
  completedEarnings: number;
}

interface Answer {
  id: string;
  body: string;
  created_at: string;
  question: {
    id: string;
    title: string;
    price: number;
  };
}

export default function MentorProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [profile, setProfile] = useState<any>(null);
  const [stats, setStats] = useState<MentorStats>({
    totalAnswers: 0,
    totalEarnings: 0,
    pendingEarnings: 0,
    completedEarnings: 0,
  });
  const [recentAnswers, setRecentAnswers] = useState<Answer[]>([]);
  const [loading, setLoading] = useState(true);
  const [isMentor, setIsMentor] = useState(false);
  const [editing, setEditing] = useState(false);
  const [bio, setBio] = useState('');
  const [mentorTags, setMentorTags] = useState('');
  const [mentorRate, setMentorRate] = useState(10);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data: { user: currentUser } } = await supabase.auth.getUser();
        if (!currentUser) {
          router.push('/auth/login?redirect=/mentor/profile');
          return;
        }

        setUser(currentUser);

        // Buscar perfil
        const { data: profileData, error: pError } = await supabase
          .from('profiles')
          .select('*')
          .eq('id', currentUser.id)
          .single();

        if (pError) throw pError;

        setProfile(profileData);
        setIsMentor(profileData.is_mentor || false);
        setBio(profileData.bio || '');
        setMentorTags((profileData.mentor_tags || []).join(', '));
        setMentorRate(Number(profileData.mentor_rate) || 10);

        if (profileData.is_mentor) {
          // Buscar estatísticas
          const { data: answersData } = await supabase
            .from('answers')
            .select('id, question_id')
            .eq('mentor_id', currentUser.id);

          const { data: transactionsData } = await supabase
            .from('transactions')
            .select('mentor_amount, status')
            .eq('mentor_id', currentUser.id);

          const totalAnswers = answersData?.length || 0;
          const completedTransactions = transactionsData?.filter((t) => t.status === 'completed') || [];
          const completedEarnings = completedTransactions.reduce((sum, t) => sum + Number(t.mentor_amount), 0);
          const pendingTransactions = transactionsData?.filter((t) => t.status === 'pending') || [];
          const pendingEarnings = pendingTransactions.reduce((sum, t) => sum + Number(t.mentor_amount), 0);

          setStats({
            totalAnswers,
            totalEarnings: completedEarnings + pendingEarnings,
            pendingEarnings,
            completedEarnings,
          });

          // Buscar respostas recentes
          const { data: recentAnswersData } = await supabase
            .from('answers')
            .select(
              `
              id,
              body,
              created_at,
              question:questions!inner(id, title, price)
            `
            )
            .eq('mentor_id', currentUser.id)
            .order('created_at', { ascending: false })
            .limit(5);

          if (recentAnswersData) {
            setRecentAnswers(recentAnswersData as any);
          }
        }
      } catch (err: any) {
        console.error('Erro ao carregar dados:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [router]);

  const handleSaveProfile = async () => {
    if (!user) return;

    try {
      const tagsArray = mentorTags
        .split(',')
        .map((t) => t.trim())
        .filter((t) => t.length > 0);

      const { error } = await supabase
        .from('profiles')
        .update({
          bio,
          mentor_tags: tagsArray,
          mentor_rate: mentorRate,
          is_mentor: true,
        })
        .eq('id', user.id);

      if (error) throw error;

      setIsMentor(true);
      setEditing(false);
      setProfile({ ...profile, bio, mentor_tags: tagsArray, mentor_rate: mentorRate, is_mentor: true });
    } catch (err: any) {
      alert('Erro ao salvar perfil: ' + err.message);
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p className="text-gray-600">Carregando...</p>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <Link href="/" className="text-blue-600 hover:underline text-sm mb-6 inline-block">
          ← Voltar para home
        </Link>

        <div className="bg-white rounded-lg shadow-md p-8 mb-8 border border-gray-200">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Perfil de Mentor</h1>

          {!isMentor ? (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6">
              <h2 className="text-lg font-semibold text-yellow-900 mb-2">
                Você ainda não é um mentor
              </h2>
              <p className="text-yellow-800 mb-4">
                Complete seu perfil para começar a responder perguntas e ganhar dinheiro!
              </p>
              <button
                onClick={() => setEditing(true)}
                className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
              >
                Tornar-se Mentor
              </button>
            </div>
          ) : (
            <div className="space-y-6">
              {/* Estatísticas */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="bg-blue-50 rounded-lg p-4 border border-blue-200">
                  <p className="text-sm text-blue-600 font-semibold">Respostas</p>
                  <p className="text-2xl font-bold text-blue-900">{stats.totalAnswers}</p>
                </div>
                <div className="bg-green-50 rounded-lg p-4 border border-green-200">
                  <p className="text-sm text-green-600 font-semibold">Ganhos Totais</p>
                  <p className="text-2xl font-bold text-green-900">R$ {stats.totalEarnings.toFixed(2)}</p>
                </div>
                <div className="bg-yellow-50 rounded-lg p-4 border border-yellow-200">
                  <p className="text-sm text-yellow-600 font-semibold">Pendentes</p>
                  <p className="text-2xl font-bold text-yellow-900">R$ {stats.pendingEarnings.toFixed(2)}</p>
                </div>
                <div className="bg-purple-50 rounded-lg p-4 border border-purple-200">
                  <p className="text-sm text-purple-600 font-semibold">Recebidos</p>
                  <p className="text-2xl font-bold text-purple-900">R$ {stats.completedEarnings.toFixed(2)}</p>
                </div>
              </div>

              {/* Informações do Perfil */}
              <div>
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-xl font-bold text-gray-900">Informações do Perfil</h2>
                  <button
                    onClick={() => setEditing(true)}
                    className="text-blue-600 hover:underline text-sm"
                  >
                    Editar
                  </button>
                </div>
                <div className="space-y-2">
                  <p>
                    <span className="font-semibold">Nome:</span> {profile?.display_name || user?.email}
                  </p>
                  <p>
                    <span className="font-semibold">Email:</span> {user?.email}
                  </p>
                  <p>
                    <span className="font-semibold">Bio:</span> {bio || 'Não informado'}
                  </p>
                  <p>
                    <span className="font-semibold">Tags:</span>{' '}
                    {(profile?.mentor_tags || []).length > 0
                      ? profile.mentor_tags.join(', ')
                      : 'Nenhuma tag'}
                  </p>
                  <p>
                    <span className="font-semibold">Taxa padrão:</span> R$ {Number(profile?.mentor_rate || 10).toFixed(2)}
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Formulário de Edição */}
          {editing && (
            <div className="mt-8 border-t border-gray-200 pt-8">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Editar Perfil</h2>
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Bio</label>
                  <textarea
                    value={bio}
                    onChange={(e) => setBio(e.target.value)}
                    placeholder="Descreva sua experiência e expertise..."
                    rows={4}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Tags de Expertise (separadas por vírgula)
                  </label>
                  <input
                    type="text"
                    value={mentorTags}
                    onChange={(e) => setMentorTags(e.target.value)}
                    placeholder="ex: growth, marketing, startup, react, design"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <p className="text-xs text-gray-500 mt-1">
                    Essas tags ajudam os usuários a encontrar você para suas perguntas
                  </p>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Taxa Padrão (R$)
                  </label>
                  <input
                    type="number"
                    value={mentorRate}
                    onChange={(e) => setMentorRate(Number(e.target.value))}
                    min="5"
                    max="500"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div className="flex gap-3">
                  <button
                    onClick={handleSaveProfile}
                    className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
                  >
                    Salvar
                  </button>
                  <button
                    onClick={() => {
                      setEditing(false);
                      setBio(profile?.bio || '');
                      setMentorTags((profile?.mentor_tags || []).join(', '));
                      setMentorRate(Number(profile?.mentor_rate) || 10);
                    }}
                    className="px-6 py-2 border border-gray-300 rounded-lg font-semibold hover:bg-gray-50 transition"
                  >
                    Cancelar
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Respostas Recentes */}
        {isMentor && recentAnswers.length > 0 && (
          <div className="bg-white rounded-lg shadow-md p-8 border border-gray-200">
            <h2 className="text-xl font-bold text-gray-900 mb-4">Respostas Recentes</h2>
            <div className="space-y-4">
              {recentAnswers.map((answer) => (
                <div key={answer.id} className="border border-gray-200 rounded-lg p-4">
                  <Link
                    href={`/questions/${answer.question.id}`}
                    className="text-blue-600 hover:underline font-semibold"
                  >
                    {answer.question.title}
                  </Link>
                  <p className="text-sm text-gray-600 mt-1 line-clamp-2">{answer.body}</p>
                  <div className="flex justify-between items-center mt-2">
                    <p className="text-xs text-gray-500">
                      {new Date(answer.created_at).toLocaleDateString('pt-BR')}
                    </p>
                    <p className="text-sm font-semibold text-green-600">
                      R$ {Number(answer.question.price).toFixed(2)}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </main>
  );
}

