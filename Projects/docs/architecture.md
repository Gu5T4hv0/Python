# Arquitetura proposta (MVP)

- Frontend: Next.js + Tailwind (deploy Vercel)
- Backend: Supabase (Postgres, Auth, Storage)
- Pagamentos: Stripe (webhooks para confirmar pagamentos)
- Storage de mídia: Supabase Storage (ou S3)
- Deploy: Vercel (frontend), Supabase (backend)

Fluxo de exemplo:
1. Usuário cria pergunta no frontend -> faz upload de mídia para Supabase Storage.
2. Frontend cria registro `questions` no Supabase Postgres com metadados.
3. Usuário inicia pagamento via Stripe -> webhook confirma pagamento.
4. Mentor grava resposta -> upload para Storage e cria registro `answers`.
5. Sistema registra transação e calcula comissão.

Segurança:
- RLS (Row Level Security) no Supabase para proteger dados por usuário.

