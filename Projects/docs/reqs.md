# MicroMentor — Requisitos de Alto Nível

Versão: MVP 0.1
Data: 2025-11-12

## Visão resumida
MicroMentor é uma plataforma de micromentorias assíncronas onde mentores gravam respostas curtas (até 3 minutos) para perguntas objetivas de mentorados. O usuário paga uma microtaxa por resposta; o mentor recebe a maior parte do valor e a plataforma retém uma comissão.

## Público-alvo
- Fundadores early-stage e indie hackers que precisam de conselhos pontuais.
- Profissionais (devs, designers, PMs) buscando feedback prático rápido.
- Mentores experientes que querem monetizar pequenas orientações.

## Problema que resolvemos
- Respostas longas e demoradas em fóruns.
- Mentoria cara e demorada para dúvidas pontuais.
- Dificuldade de encontrar mentores com experiência específica.

## Objetivos do MVP
- Validar se usuários pagariam por respostas curtas e se mentores aceitariam responder por microtaxas.
- Conseguir X perguntas e Y respostas no primeiro mês (definir metas com você).

## Métricas de sucesso iniciais
- Taxa de conversão: perguntas criadas / perguntas pagas (meta inicial: 10%).
- Tempo médio para resposta (meta: <48h).
- Retenção: % de usuários que pedem >1 resposta (meta: 15%).
- Receita por usuário e LTV/CPA básicos.

## Requisitos funcionais (MVP mínimo)
1. Autenticação de usuários (signup/login) — via email (Supabase Auth).
2. Perfil de usuário com flag `is_mentor` e campos públicos: bio, tags, experiência.
3. Criar pergunta: título, descrição (texto), upload opcional de áudio/vídeo (<=3 minutos), tags, preço (padrão R$10).
4. Listagem/Feed de perguntas públicas (ou próximas a tags do usuário).
5. Sistema de matching simples por tags (apenas sugestão, não obrigatório automaticamente).
6. Mentor grava resposta em texto/áudio/vídeo (<=3 minutos) e submete como resposta.
7. Pagamento: checkout para pagar pela resposta (Stripe/CSP); plataforma retém 20% e registra transação.
8. Notificações básicas (email ou in-app) para mentor quando houver pergunta relevante.
9. Histórico de interações — usuário vê respostas recebidas; mentor vê perguntas respondidas.
10. Administração básica: listar transações e perguntas (pode ser um dashboard mínimo nesta fase).

## Regras e validações
- Uploads de mídia limitados a 3 minutos; validar duração e tamanho no cliente e no backend.
- Tipos permitidos: mp3, m4a, mp4, mov (ouvidos/visuals padrões).
- Política de conteúdo/relato: botão para reportar resposta/questão para revisão manual.

## Restrições e premissas
- Usaremos Supabase para Auth/DB/Storage para acelerar desenvolvimento.
- Stripe será utilizado para pagamentos; integrações BR podem ser avaliadas depois.
- Não haverá transcodificação avançada no MVP; aceitaremos uploads em formatos comuns e validaremos duração.
- Relatórios e analytics simples via eventos no banco (Postgres).

## Fluxos principais
- Usuário cria pergunta -> paga -> mentor grava resposta -> resposta vinculada à pergunta -> mentor recebe pagamento (após confirmação) e plataforma guarda comissão.
- Usuário segue mentor / solicita respostas futuras / marca mentoria maior (futuro feature).

## Requisitos não-funcionais
- Segurança: RLS (Row Level Security) para proteger dados de cada usuário (implementar no Supabase).
- Performance: suportar uploads de pequenos vídeos; latência aceitável para feed.
- Observability: logs básicos e integração com Sentry (futuro).

## Cronograma sugerido (estimativa)
- Kickoff & requisitos + wireframes: 2–3 dias (feito)
- Scaffold + Auth + DB schema: 3–5 dias
- Criar pergunta + upload: 3–5 dias
- Pagamento + respostas: 4–6 dias
- QA e deploy: 3–5 dias

## Entregáveis deste documento
- Documento de requisitos curto (este arquivo)
- Wireframes iniciais (arquivo separado)

---

Notas: este documento é o ponto de partida. Podemos detalhar user stories, acceptance criteria e priorização assim que você aprovar o escopo do MVP.