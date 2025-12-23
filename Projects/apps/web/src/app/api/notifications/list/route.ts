import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para listar notificações de um usuário
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { user_id, limit = 20 } = body;

    if (!user_id) {
      return NextResponse.json({ error: 'Missing user_id' }, { status: 400 });
    }

    const { data: notifications, error } = await supabaseAdmin
      .from('notifications')
      .select('*')
      .eq('user_id', user_id)
      .order('created_at', { ascending: false })
      .limit(limit);

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    return NextResponse.json({ notifications: notifications || [] });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to list notifications' }, { status: 500 });
  }
}

