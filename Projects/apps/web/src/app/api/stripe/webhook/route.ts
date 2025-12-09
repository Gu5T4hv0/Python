import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';
import { supabaseAdmin } from '@/lib/supabaseAdmin';

function getStripe() {
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) throw new Error('Stripe secret key missing (STRIPE_SECRET_KEY)');
  return new Stripe(key, { apiVersion: '2023-10-16' });
}

export async function POST(req: NextRequest) {
  const stripe = getStripe();
  const sig = req.headers.get('stripe-signature');
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
  if (!sig || !webhookSecret) {
    return NextResponse.json({ error: 'Missing Stripe signature or webhook secret' }, { status: 400 });
  }

  let event: Stripe.Event;
  try {
    const payload = await req.text();
    event = stripe.webhooks.constructEvent(payload, sig, webhookSecret);
  } catch (err: any) {
    return NextResponse.json({ error: `Webhook signature verification failed: ${err.message}` }, { status: 400 });
  }

  try {
    if (event.type === 'checkout.session.completed') {
      const session = event.data.object as Stripe.Checkout.Session;
      const metadata = session.metadata || {};

      const user_id = metadata.user_id || null;
      const title = metadata.title || null;
      const description = metadata.description || null;
      const tagsCsv = metadata.tags || '';
      const priceStr = metadata.price || '0';
      const media_url = metadata.media_url || null;
      const media_type = metadata.media_type || null; // '' becomes null below
      const media_duration_seconds_str = metadata.media_duration_seconds || '';

      if (!user_id || !title || !description) {
        return NextResponse.json({ error: 'Missing required metadata in session' }, { status: 400 });
      }

      const tags = tagsCsv
        .split(',')
        .map((t) => t.trim())
        .filter((t) => t.length > 0);

      const price = Number.parseFloat(priceStr);
      const media_duration_seconds = media_duration_seconds_str
        ? Number.parseInt(media_duration_seconds_str, 10)
        : null;

      const insertPayload = {
        user_id,
        title,
        description,
        tags,
        price,
        media_url: media_url && media_url.length > 0 ? media_url : null,
        media_type: media_type && media_type.length > 0 ? media_type : null,
        media_duration_seconds,
        status: 'open',
      } as any;

      const { error: insertError } = await supabaseAdmin
        .from('questions')
        .insert([insertPayload]);

      if (insertError) {
        return NextResponse.json({ error: `Failed to insert question: ${insertError.message}` }, { status: 500 });
      }
    }
    return NextResponse.json({ received: true });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Webhook handler failed' }, { status: 500 });
  }
}
