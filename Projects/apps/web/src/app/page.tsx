import Link from 'next/link';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-gradient-to-b from-blue-50 to-white">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold text-center text-blue-600 mb-8">
          🎉 MicroMentor
        </h1>
        <p className="text-center text-gray-600 mb-8">
          Plataforma de micromentorias assíncronas — Bem-vindo!
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <Link href="/create-question" className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer">
            <h2 className="text-xl font-semibold mb-2">📝 Fazer Pergunta</h2>
            <p className="text-gray-600">Envie uma dúvida em texto, áudio ou vídeo (até 3 min)</p>
          </Link>
          
          <Link href="/questions" className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer">
            <h2 className="text-xl font-semibold mb-2">🎤 Ver Respostas</h2>
            <p className="text-gray-600">Consulte o feed de perguntas e respostas da comunidade</p>
          </Link>
          
          <Link href="/questions" className="p-6 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition cursor-pointer">
            <h2 className="text-xl font-semibold mb-2">🤝 Responder</h2>
            <p className="text-gray-600">Seja mentor e ganhe com suas respostas</p>
          </Link>
        </div>

        <div className="mt-12 flex flex-col md:flex-row gap-4 justify-center">
          <Link
            href="/create-question"
            className="inline-block bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition text-center"
          >
            🚀 Fazer uma Pergunta
          </Link>
          <Link
            href="/questions"
            className="inline-block bg-gray-200 text-gray-900 px-8 py-3 rounded-lg font-semibold hover:bg-gray-300 transition text-center"
          >
            📚 Ver Feed de Perguntas
          </Link>
        </div>
      </div>
    </main>
  );
}
