# 🧪 Como Testar as Novas Funcionalidades

## 📋 Checklist de Funcionalidades

### ✅ 1. Sistema de Seguir Mentores

**Como testar:**
1. Faça login no site
2. Acesse uma pergunta com tags (ex: `/questions/[id]`)
3. Role até a seção **"👥 Mentores Sugeridos"**
4. Você verá cards de mentores
5. Clique no botão **"+ Seguir"** em um mentor
6. O botão deve mudar para **"✓ Seguindo"**

**Onde encontrar:**
- Cards de mentores sugeridos na página de detalhe da pergunta
- Página pública do mentor: `/mentor/[id]` (clique no nome do mentor)

---

### ✅ 2. Sistema de Notificações

**Como testar:**
1. Faça login no site
2. No **Header** (topo da página), procure pelo ícone **🔔** (sino)
3. Clique no sino
4. Você verá um dropdown com suas notificações

**Quando aparecem notificações:**
- Quando alguém responde sua pergunta
- Quando sua resposta é aceita (se você for mentor)

**Como gerar uma notificação:**
1. Crie uma pergunta
2. Faça login com outra conta (mentor)
3. Responda a pergunta
4. Volte para a primeira conta
5. Clique no sino 🔔 - deve aparecer a notificação!

---

### ✅ 3. Marcar Melhor Resposta

**Como testar:**
1. Crie uma pergunta
2. Faça login como mentor e responda
3. Volte para a conta que criou a pergunta
4. Na página de detalhe da pergunta, role até as respostas
5. Você verá um botão **"⭐ Marcar como Melhor"** abaixo de cada resposta
6. Clique no botão
7. A resposta deve ficar destacada com badge **"⭐ Melhor Resposta"**

**Onde encontrar:**
- Página de detalhe da pergunta (`/questions/[id]`)
- Apenas o autor da pergunta pode marcar melhor resposta

---

### ✅ 4. Avaliar Respostas (Rating)

**Como testar:**
1. Crie uma pergunta
2. Faça login como mentor e responda
3. Aceite a resposta (botão "Aceitar Resposta")
4. Após aceitar, você verá **"Avaliar resposta:"** com 5 estrelas ⭐
5. Clique em uma estrela (1 a 5)
6. A avaliação deve aparecer na resposta

**Onde encontrar:**
- Página de detalhe da pergunta (`/questions/[id]`)
- Aparece apenas após aceitar uma resposta
- Apenas o autor da pergunta pode avaliar

---

### ✅ 5. Perfil Público de Mentor

**Como testar:**
1. Na página de detalhe da pergunta, clique no **nome de um mentor** nos cards sugeridos
2. Ou acesse diretamente: `/mentor/[id]` (substitua `[id]` pelo ID do mentor)
3. Você verá:
   - Nome e email do mentor
   - Bio
   - Tags de expertise
   - Estatísticas (respostas, seguidores)
   - Botão "Seguir" (se não estiver seguindo)

**Como encontrar o ID do mentor:**
- Olhe o URL quando clicar no nome do mentor
- Ou veja no card de mentores sugeridos

---

## 🔍 Verificar se as Migrations Foram Executadas

### Teste Rápido no SQL Editor:

```sql
-- Verificar tabela de notificações
SELECT COUNT(*) FROM notifications;

-- Verificar colunas em answers
SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'answers' 
AND column_name IN ('is_best_answer', 'rating');
```

Se retornar resultados (mesmo que 0), as migrations foram executadas! ✅

---

## 🐛 Se Algo Não Funcionar

### Notificações não aparecem:
- Verifique se executou `002_notifications.sql`
- Verifique se está logado
- Tente criar uma nova resposta para gerar notificação

### Botão "Marcar como Melhor" não aparece:
- Verifique se executou `003_answer_improvements.sql`
- Certifique-se de que você é o autor da pergunta
- Recarregue a página

### Botão "Seguir" não funciona:
- Verifique se está logado
- Abra o console do navegador (F12) para ver erros
- Verifique se a tabela `follows` existe no Supabase

---

## 📞 Precisa de Ajuda?

Se algo não funcionar:
1. Abra o console do navegador (F12 → Console)
2. Veja se há erros em vermelho
3. Copie os erros e me envie



