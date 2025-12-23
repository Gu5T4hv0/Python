import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para seguir/deixar de seguir um mentor
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { follower_id, mentor_id } = body;

    if (!follower_id || !mentor_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    if (follower_id === mentor_id) {
      return NextResponse.json({ error: 'Cannot follow yourself' }, { status: 400 });
    }

    // Verificar se já está seguindo
    const { data: existingFollow } = await supabaseAdmin
      .from('follows')
      .select('id')
      .eq('follower_id', follower_id)
      .eq('mentor_id', mentor_id)
      .single();

    if (existingFollow) {
      // Deixar de seguir
      const { error } = await supabaseAdmin
        .from('follows')
        .delete()
        .eq('follower_id', follower_id)
        .eq('mentor_id', mentor_id);

      if (error) {
        return NextResponse.json({ error: error.message }, { status: 500 });
      }

      return NextResponse.json({ following: false, action: 'unfollowed' });
    } else {
      // Seguir
      const { error } = await supabaseAdmin
        .from('follows')
        .insert([{ follower_id, mentor_id }]);

      if (error) {
        return NextResponse.json({ error: error.message }, { status: 500 });
      }

      return NextResponse.json({ following: true, action: 'followed' });
    }
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to toggle follow' }, { status: 500 });
  }
}

