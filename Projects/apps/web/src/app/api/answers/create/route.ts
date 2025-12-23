import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para criar resposta - valida se o usuário é mentor
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { question_id, mentor_id, body: answerBody, media_url, media_type, media_duration_seconds } = body;

    if (!question_id || !mentor_id || !answerBody) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    // Verificar se o usuário é mentor
    const { data: profile, error: profileError } = await supabaseAdmin
      .from('profiles')
      .select('is_mentor')
      .eq('id', mentor_id)
      .single();

    if (profileError || !profile) {
      return NextResponse.json({ error: 'Profile not found' }, { status: 404 });
    }

    if (!profile.is_mentor) {
      return NextResponse.json(
        { error: 'Apenas mentores podem responder perguntas. Torne-se um mentor em /mentor/profile' },
        { status: 403 }
      );
    }

    // Verificar se a pergunta existe e está aberta
    const { data: question, error: qError } = await supabaseAdmin
      .from('questions')
      .select('id, status')
      .eq('id', question_id)
      .single();

    if (qError || !question) {
      return NextResponse.json({ error: 'Question not found' }, { status: 404 });
    }

    if (question.status !== 'open') {
      return NextResponse.json({ error: 'Esta pergunta já foi respondida ou fechada' }, { status: 400 });
    }

    // Criar resposta
    const { data: answer, error: insertError } = await supabaseAdmin
      .from('answers')
      .insert([
        {
          question_id,
          mentor_id,
          body: answerBody,
          media_url: media_url || null,
          media_type: media_type || null,
          media_duration_seconds: media_duration_seconds || null,
        },
      ])
      .select()
      .single();

    if (insertError) {
      return NextResponse.json({ error: insertError.message }, { status: 500 });
    }

    // Criar notificação para o autor da pergunta
    try {
      await fetch(`${process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000'}/api/notifications/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: question.user_id,
          type: 'answer',
          title: 'Nova resposta na sua pergunta',
          message: `Um mentor respondeu sua pergunta: "${question.title.substring(0, 50)}..."`,
          link: `/questions/${question_id}`,
          related_id: question_id,
        }),
      });
    } catch (notifError) {
      // Não falhar se notificação não for criada
      console.error('Erro ao criar notificação:', notifError);
    }

    return NextResponse.json({ answer });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to create answer' }, { status: 500 });
  }
}

