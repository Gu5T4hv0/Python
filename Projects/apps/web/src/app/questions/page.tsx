import QuestionsGrid from '@/components/QuestionsGrid';
import Link from 'next/link';

export default function QuestionsPage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <div>
            <Link href="/" className="text-blue-600 hover:underline text-sm">
              ← Voltar para home
            </Link>
          </div>
          <Link
            href="/create-question"
            className="inline-block bg-blue-600 text-white px-4 py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
          >
            + Fazer Pergunta
          </Link>
        </div>
      </div>
      <QuestionsGrid />
    </main>
  );
}
