import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para avaliar uma resposta (rating 1-5)
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { answer_id, rating, user_id } = body;

    if (!answer_id || !rating || !user_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    if (rating < 1 || rating > 5) {
      return NextResponse.json({ error: 'Rating must be between 1 and 5' }, { status: 400 });
    }

    // Verificar se a resposta existe e buscar a pergunta relacionada
    const { data: answer, error: aError } = await supabaseAdmin
      .from('answers')
      .select('question_id')
      .eq('id', answer_id)
      .single();

    if (aError || !answer) {
      return NextResponse.json({ error: 'Answer not found' }, { status: 404 });
    }

    // Verificar se o usuário é o autor da pergunta
    const { data: question, error: qError } = await supabaseAdmin
      .from('questions')
      .select('user_id')
      .eq('id', answer.question_id)
      .single();

    if (qError || !question || question.user_id !== user_id) {
      return NextResponse.json({ error: 'Only question author can rate answers' }, { status: 403 });
    }

    // Atualizar rating
    const { error: updateError } = await supabaseAdmin
      .from('answers')
      .update({ rating })
      .eq('id', answer_id);

    if (updateError) {
      return NextResponse.json({ error: updateError.message }, { status: 500 });
    }

    return NextResponse.json({ success: true, rating });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to rate answer' }, { status: 500 });
  }
}

