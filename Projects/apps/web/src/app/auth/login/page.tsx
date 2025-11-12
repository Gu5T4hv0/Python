import AuthForm from '@/components/AuthForm';
import Link from 'next/link';

export default function LoginPage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-blue-50 to-white flex items-center justify-center py-12 px-4">
      <div className="w-full max-w-md">
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-gray-900">Bem-vindo de volta!</h1>
          <p className="text-gray-600 mt-2">Faça login na sua conta MicroMentor</p>
        </div>

        <div className="bg-white rounded-lg shadow-md p-8">
          <AuthForm mode="login" />
        </div>

        <div className="mt-6 text-center">
          <Link href="/" className="text-blue-600 hover:underline text-sm">
            ← Voltar para home
          </Link>
        </div>
      </div>
    </main>
  );
}
