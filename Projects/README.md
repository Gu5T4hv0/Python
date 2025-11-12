# MicroMentor (MVP)

MicroMentor — plataforma de micromentorias assíncronas (MVP).

Resumo rápido:
- Usuários enviam dúvidas em texto/áudio/vídeo (<=3min).
- Mentores gravam respostas curtas e recebem uma microtaxa.

Estrutura do repositório (scaffold):

- apps/web -> frontend Next.js + Tailwind (placeholder)
- packages/api -> backend (placeholders; usar Supabase para DB/Auth/Storage)
- docs/ -> requisitos e wireframes

Como começar (local)

1. Frontend (Next.js)
   - Vá para `apps/web` e inicialize um projeto Next.js se ainda não estiver criado:
     ```powershell
     cd apps/web
     npx create-next-app@latest . --use-npm
     npm install
     npm run dev
     ```
   - Recomendo adicionar Tailwind seguindo a documentação oficial.

2. Backend / Supabase
   - Para o MVP recomendável usar Supabase (Postgres + Auth + Storage).
   - Crie um projeto no Supabase e atualize `.env` com as chaves.

3. Variáveis de ambiente
   - Copie `.env.example` para `.env` e preencha as chaves necessárias.

4. Documentos
   - `docs/reqs.md` e `docs/wireframes.md` já estão neste repositório.

Próximos passos sugeridos:
- Criar o app Next.js dentro de `apps/web`.
- Configurar conta Supabase e criar esquema inicial.
- Implementar fluxo de autenticação e criação de pergunta.

