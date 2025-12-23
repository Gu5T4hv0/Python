import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para verificar se um usuário está seguindo um mentor
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { follower_id, mentor_id } = body;

    if (!follower_id || !mentor_id) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const { data, error } = await supabaseAdmin
      .from('follows')
      .select('id')
      .eq('follower_id', follower_id)
      .eq('mentor_id', mentor_id)
      .single();

    if (error && error.code !== 'PGRST116') {
      // PGRST116 = no rows returned (não é erro, apenas não está seguindo)
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    return NextResponse.json({ following: !!data });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to check follow status' }, { status: 500 });
  }
}

