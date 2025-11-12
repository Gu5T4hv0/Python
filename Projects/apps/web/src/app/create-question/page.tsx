'use client';

import CreateQuestionForm from '@/components/CreateQuestionForm';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import { useRouter } from 'next/navigation';

export default function CreateQuestionPage() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const checkAuth = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) {
        router.push('/auth/login?redirect=/create-question');
      } else {
        setUser(user);
      }
      setLoading(false);
    };
    checkAuth();
  }, [router]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white flex items-center justify-center">
        <p className="text-gray-600">Carregando...</p>
      </main>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white py-12 px-4">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <Link href="/" className="text-blue-600 hover:underline text-sm">
            ← Voltar para home
          </Link>
          <h1 className="text-4xl font-bold text-gray-900 mt-4">Fazer uma Pergunta</h1>
          <p className="text-gray-600 mt-2">
            Compartilhe sua dúvida e encontre um mentor experiente para respondê-la
          </p>
        </div>

        {/* Dicas */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-8">
          <h2 className="font-semibold text-blue-900 mb-2">💡 Dicas para uma ótima pergunta:</h2>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>✓ Seja específico e objetivo</li>
            <li>✓ Inclua contexto sobre seu problema</li>
            <li>✓ Mencione o que você já tentou</li>
            <li>✓ Adicionar áudio/vídeo aumenta as chances de resposta</li>
          </ul>
        </div>

        {/* Formulário */}
        <div className="bg-white rounded-lg shadow-md p-8">
          <CreateQuestionForm />
        </div>

        {/* FAQ */}
        <div className="mt-12 bg-gray-50 rounded-lg p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Perguntas Frequentes</h2>
          <div className="space-y-4 text-sm text-gray-700">
            <div>
              <p className="font-semibold">Quanto custa enviar uma pergunta?</p>
              <p>Você define o preço entre R$5 e R$500. Mentores ganham 80% do valor.</p>
            </div>
            <div>
              <p className="font-semibold">Posso adicionar áudio ou vídeo?</p>
              <p>Sim! Áudio (mp3) ou vídeo (mp4) até 3 minutos e 50MB aumentam as chances de resposta.</p>
            </div>
            <div>
              <p className="font-semibold">Como funciona o pagamento?</p>
              <p>Você paga via Stripe ao enviar a pergunta. O mentor grava a resposta assim que aceita.</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
