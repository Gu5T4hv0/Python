export default function CancelPage() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-yellow-50">
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <h1 className="text-2xl font-semibold text-yellow-700">Pagamento cancelado</h1>
        <p className="mt-2 text-gray-600">Você pode tentar novamente quando quiser.</p>
        <a href="/create-question" className="mt-6 inline-block text-white bg-yellow-600 hover:bg-yellow-700 px-4 py-2 rounded">Voltar ao formulário</a>
      </div>
    </main>
  );
}
