# MicroMentor — Wireframes e fluxo (texto)

Versão: MVP 0.1

## Tela: Home / Feed
- Header: logo, busca por tags, link para criar pergunta, perfil
- Lista de perguntas recentes (título, tags, preço, status)
- CTA: Criar nova pergunta

## Tela: Criar Pergunta
- Formulário:
  - Título (input)
  - Descrição (textarea)
  - Tags (multi-select)
  - Upload opcional (áudio/video) — botão `Gravar` (client) ou `Upload` (arquivo)
  - Preço (padrão R$10, editable)
  - Botão: `Enviar e pagar`
- Validações:
  - Duração máxima 3 minutos
  - Tipos permitidos: mp3, m4a, mp4, mov

## Tela: Pergunta (detail)
- Título, descrição completa, mídia anexada (player), tags
- Status (pending/answered)
- Se não paga: botão `Pagar e receber resposta`
- Se paga e não respondida: aguardar resposta (mostrar ETA)
- Se respondida: mostrar resposta (texto e/ou player de mídia), botão `Seguir mentor`

## Tela: Gravar resposta (mentor)
- Player/editor simples para gravar até 3 minutos
- Preview da gravação
- Botão: `Enviar resposta`

## Tela: Perfil do Mentor
- Foto, bio, tags, número de respostas, avaliações (futuro)
- Botão: `Seguir` e `Solicitar mentoria` (futuro)

## Tela: Checkout
- Resumo da pergunta, preço, método de pagamento (Stripe)
- Botão: `Pagar`

## Fluxo simples de matching
- Ao criar pergunta: salvar tags
- Mostrar feed de perguntas filtradas por tags para mentores com matching
- Notificar mentores (email/in-app) com lista resumida de perguntas relevantes

## Observações de UI/UX
- Manter experiência leve: foco em conteúdo (player/descrição)
- Feedback visual para uploads e gravações longas

---

Próximo: posso gerar PNGs rápidos (mockups) ou criar componentes React/Next com Tailwind para a tela `Criar Pergunta`. Qual você prefere?