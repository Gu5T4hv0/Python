import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para criar notificação
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { user_id, type, title, message, link, related_id } = body;

    if (!user_id || !type || !title) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    // Criar notificação
    const { data: notification, error } = await supabaseAdmin
      .from('notifications')
      .insert([
        {
          user_id,
          type,
          title,
          message: message || null,
          link: link || null,
          related_id: related_id || null,
          read: false,
        },
      ])
      .select()
      .single();

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    return NextResponse.json({ notification });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to create notification' }, { status: 500 });
  }
}

