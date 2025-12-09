import { redirect } from 'next/navigation';

export default function QuestionsPage() {
  // Redireciona para a versão com locale
  redirect('/pt-BR/questions');
}
