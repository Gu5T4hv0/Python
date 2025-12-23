import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para marcar notificação como lida
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { notification_id, user_id } = body;

    if (!notification_id || !user_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const { error } = await supabaseAdmin
      .from('notifications')
      .update({ read: true })
      .eq('id', notification_id)
      .eq('user_id', user_id);

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    return NextResponse.json({ success: true });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to mark notification as read' }, { status: 500 });
  }
}

