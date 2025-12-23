import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para criar transação quando uma resposta é aceita
 * Calcula fee splitting: 80% mentor, 20% plataforma
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { question_id, answer_id, mentor_id, stripe_payment_id } = body;

    if (!question_id || !answer_id || !mentor_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    // Buscar dados da pergunta
    const { data: question, error: qError } = await supabaseAdmin
      .from('questions')
      .select('price, user_id')
      .eq('id', question_id)
      .single();

    if (qError || !question) {
      return NextResponse.json({ error: 'Question not found' }, { status: 404 });
    }

    const amount = Number(question.price);
    const platformFee = amount * 0.2; // 20% plataforma
    const mentorAmount = amount * 0.8; // 80% mentor

    // Criar transação
    const { data: transaction, error: tError } = await supabaseAdmin
      .from('transactions')
      .insert([
        {
          question_id,
          answer_id,
          user_id: question.user_id,
          mentor_id,
          amount,
          platform_fee: platformFee,
          mentor_amount: mentorAmount,
          stripe_payment_id: stripe_payment_id || null,
          status: 'completed',
        },
      ])
      .select()
      .single();

    if (tError) {
      return NextResponse.json({ error: tError.message }, { status: 500 });
    }

    // Atualizar status da pergunta para "answered"
    await supabaseAdmin
      .from('questions')
      .update({ status: 'answered' })
      .eq('id', question_id);

    // Criar notificação para o mentor
    try {
      await fetch(`${process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000'}/api/notifications/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: mentor_id,
          type: 'accepted',
          title: 'Resposta aceita!',
          message: `Sua resposta foi aceita! Você receberá R$ ${mentorAmount.toFixed(2)}.`,
          link: `/questions/${question_id}`,
          related_id: answer_id,
        }),
      });
    } catch (notifError) {
      console.error('Erro ao criar notificação:', notifError);
    }

    return NextResponse.json({ transaction });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to create transaction' }, { status: 500 });
  }
}

