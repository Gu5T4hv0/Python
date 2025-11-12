export default function SuccessPage() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-green-50">
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <h1 className="text-2xl font-semibold text-green-700">Pagamento concluído ✅</h1>
        <p className="mt-2 text-gray-600">Sua pergunta foi enviada e será listada em breve.</p>
        <a href="/" className="mt-6 inline-block text-white bg-green-600 hover:bg-green-700 px-4 py-2 rounded">Voltar para home</a>
      </div>
    </main>
  );
}
