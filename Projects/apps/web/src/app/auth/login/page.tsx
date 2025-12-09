import { redirect } from 'next/navigation';

export default function LoginPage() {
  // Redireciona para a versão com locale padrão (pt-BR)
  redirect('/pt-BR/auth/login');
  return null;
}
