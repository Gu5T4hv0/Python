import { NextResponse } from 'next/server';

// Disabled in production: client uploads directly to Supabase Storage with user session.
// This endpoint is intentionally returning 410 to avoid requiring service role envs during build.
export async function POST() {
  return NextResponse.json({ error: 'Upload API disabled' }, { status: 410 });
}
