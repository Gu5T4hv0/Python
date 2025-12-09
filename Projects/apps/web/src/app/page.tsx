import { redirect } from 'next/navigation';

export default function Home() {
  // Redireciona para a versão com locale padrão (pt-BR)
  redirect('/pt-BR');
}
