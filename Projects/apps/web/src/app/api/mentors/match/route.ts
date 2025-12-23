import { NextRequest, NextResponse } from 'next/server';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

/**
 * API para encontrar mentores que correspondem às tags de uma pergunta
 * Retorna mentores ordenados por relevância (número de tags em comum)
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { tags, questionId } = body;

    if (!tags || !Array.isArray(tags) || tags.length === 0) {
      return NextResponse.json({ mentors: [] });
    }

    // Buscar todos os mentores ativos
    const { data: mentors, error } = await supabaseAdmin
      .from('profiles')
      .select('id, display_name, email, bio, avatar_url, mentor_tags, mentor_rate, is_mentor')
      .eq('is_mentor', true)
      .not('mentor_tags', 'is', null);

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    if (!mentors || mentors.length === 0) {
      return NextResponse.json({ mentors: [] });
    }

    // Calcular score de matching para cada mentor
    const mentorsWithScore = mentors
      .map((mentor) => {
        const mentorTags = mentor.mentor_tags || [];
        // Contar quantas tags da pergunta estão nas tags do mentor
        const matchingTags = tags.filter((tag: string) =>
          mentorTags.some((mt: string) => mt.toLowerCase() === tag.toLowerCase())
        );
        const score = matchingTags.length;

        return {
          ...mentor,
          matchingTags,
          score,
        };
      })
      .filter((m) => m.score > 0) // Apenas mentores com pelo menos 1 tag em comum
      .sort((a, b) => b.score - a.score) // Ordenar por score (maior primeiro)
      .slice(0, 10); // Top 10 mentores

    return NextResponse.json({ mentors: mentorsWithScore });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Failed to match mentors' }, { status: 500 });
  }
}

