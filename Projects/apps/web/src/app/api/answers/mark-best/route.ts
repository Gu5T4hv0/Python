import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para marcar resposta como melhor resposta
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { answer_id, question_id, user_id } = body;

    if (!answer_id || !question_id || !user_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    // Verificar se o usuário é o autor da pergunta
    const { data: question, error: qError } = await supabaseAdmin
      .from('questions')
      .select('user_id')
      .eq('id', question_id)
      .single();

    if (qError || !question) {
      return NextResponse.json({ error: 'Question not found' }, { status: 404 });
    }

    if (question.user_id !== user_id) {
      return NextResponse.json({ error: 'Only question author can mark best answer' }, { status: 403 });
    }

    // Remover melhor resposta anterior se houver
    await supabaseAdmin
      .from('answers')
      .update({ is_best_answer: false })
      .eq('question_id', question_id)
      .eq('is_best_answer', true);

    // Marcar nova melhor resposta
    const { error: updateError } = await supabaseAdmin
      .from('answers')
      .update({ is_best_answer: true })
      .eq('id', answer_id);

    if (updateError) {
      return NextResponse.json({ error: updateError.message }, { status: 500 });
    }

    // Atualizar question com best_answer_id
    await supabaseAdmin
      .from('questions')
      .update({ best_answer_id: answer_id })
      .eq('id', question_id);

    return NextResponse.json({ success: true });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to mark best answer' }, { status: 500 });
  }
}

