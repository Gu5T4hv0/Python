import { NextRequest, NextResponse } from 'next/server';
import Stripe from 'stripe';

function getStripe() {
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) throw new Error('Stripe secret key missing (STRIPE_SECRET_KEY)');
  return new Stripe(key, { apiVersion: '2024-06-20' });
}

function getBaseUrl(req: NextRequest) {
  const header = req.headers.get('origin') || req.headers.get('x-forwarded-host');
  if (header) {
    if (header.startsWith('http')) return header;
    return `https://${header}`;
  }
  return process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3003';
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const {
      user_id,
      title,
      description,
      tags,
      price,
      media_url,
      media_type,
      media_duration_seconds,
    } = body || {};

    if (!user_id || !title || !description || !price) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const stripe = getStripe();
    const baseUrl = getBaseUrl(req);

    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      payment_method_types: ['card'],
      line_items: [
        {
          quantity: 1,
          price_data: {
            currency: 'brl',
            product_data: { name: `Pergunta: ${title}` },
            unit_amount: Math.round(Number(price) * 100),
          },
        },
      ],
      success_url: `${baseUrl}/success`,
      cancel_url: `${baseUrl}/cancel`,
      metadata: {
        user_id,
        title,
        description,
        tags: Array.isArray(tags) ? tags.join(',') : '',
        price: String(price),
        media_url: media_url || '',
        media_type: media_type || '',
        media_duration_seconds: media_duration_seconds != null ? String(media_duration_seconds) : '',
      },
    });

    return NextResponse.json({ url: session.url });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Checkout failed' }, { status: 500 });
  }
}
