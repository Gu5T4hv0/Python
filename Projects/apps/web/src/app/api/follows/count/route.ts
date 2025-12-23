import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para contar quantos seguidores um mentor tem
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { mentor_id } = body;

    if (!mentor_id) {
      return NextResponse.json({ error: 'Missing mentor_id' }, { status: 400 });
    }

    const { count, error } = await supabaseAdmin
      .from('follows')
      .select('*', { count: 'exact', head: true })
      .eq('mentor_id', mentor_id);

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    return NextResponse.json({ count: count || 0 });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to count followers' }, { status: 500 });
  }
}

