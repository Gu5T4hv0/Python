# 🔧 Setup Completo do Supabase para MicroMentor MVP

## ⚠️ IMPORTANTE: Antes de Usar

Para que o MVP funcione completamente, você **PRECISA**:
1. Criar um projeto Supabase
2. Executar as migrations SQL
3. Criar o bucket de armazenamento
4. Copiar as chaves de ambiente

---

## 📋 Passo 1: Criar Projeto Supabase

### 1.1 Acesse https://app.supabase.com

### 1.2 Clique em "New Project"

### 1.3 Preencha:
- **Project name**: `micromentor` (ou seu nome)
- **Database Password**: Escolha uma senha forte (salve!)
- **Region**: Escolha a mais próxima de você (Brazil = `sa-east-1`)

### 1.4 Clique "Create new project"

**Aguarde 2-3 minutos para inicializar...**

---

## 🗂️ Passo 2: Executar Migrations SQL

### 2.1 Vá para **SQL Editor** (no dashboard do Supabase)

### 2.2 Clique em "New query"

### 2.3 Copie TODO o conteúdo do arquivo:
```
packages/api/migrations/001_initial_schema.sql
```

### 2.4 Cole no editor do Supabase

### 2.5 Clique em "Run" (ou Ctrl+Enter)

**Resultado esperado:**
```
✓ Success
Executed in ...ms
```

### ✅ Tabelas Criadas:
- `profiles`
- `questions`
- `answers`
- `transactions`
- `follows`

### ✅ Policies Criadas (RLS):
- Cada tabela tem policies para restringir acesso por usuário

### ✅ Triggers Criados:
- Auto-atualização de `updated_at`
- Auto-criação de perfil no signup

---

## 🪣 Passo 3: Criar Storage Bucket

### 3.1 Vá para **Storage** (no sidebar do Supabase)

### 3.2 Clique em "Create a new bucket"

### 3.3 Configure:
- **Name**: `question-media`
- **Type**: Public (importante!)
- **File size limit**: 50MB
- Clique "Create bucket"

### 3.4 Verifique (Security)

Clique em `question-media` e vá para "Policies"

### 3.5 Adicione Policy (se não existir):
- Click "New policy"
- Selecione "Create policy from template"
- Template: "Enable read access for all users"
- Clique "Review"
- Clique "Save policy"

**Resultado esperado:**
```
✓ Bucket "question-media" criado
✓ Acesso público para leitura
✓ Apenas usuários autenticados podem fazer upload
```

---

## 🔐 Passo 4: Copiar Chaves de Ambiente

### 4.1 Vá para **Settings → API** (no Supabase)

### 4.2 Copie estas informações:

```
Project URL:     https://xxxxx.supabase.co
Anon public key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 📄 Passo 5: Configurar .env.local

### 5.1 Na raiz do projeto (`apps/web/`), crie arquivo `.env.local`:

```bash
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Stripe (opcional por agora)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

### 5.2 Salve o arquivo

### ⚠️ IMPORTANTE:
- **NÃO faça commit** deste arquivo para Git
- Arquivo `.env.local` já está no `.gitignore` ✅

---

## 🚀 Passo 6: Reiniciar Dev Server

### 6.1 Terminal (no `apps/web`):
```powershell
npm run dev
```

### 6.2 Abra navegador:
```
http://localhost:3003
```

### 6.3 Teste o fluxo completo:
1. Clique "Cadastro"
2. Crie conta (João Silva, joao@email.com, senha123)
3. Clique "🚀 Fazer uma Pergunta"
4. Preencha formulário
5. Clique "Enviar Pergunta"
6. Vá para `/questions` e veja sua pergunta! ✅

---

## ✅ Verificação de Setup

### Checklist Final:

- [ ] Projeto Supabase criado
- [ ] SQL migrations executadas (5 tabelas criadas)
- [ ] Bucket "question-media" criado (público)
- [ ] `.env.local` preenchido com chaves do Supabase
- [ ] Servidor Next.js rodando (`npm run dev`)
- [ ] http://localhost:3003 carrega sem erros
- [ ] Cadastro funciona (novo usuário criado)
- [ ] Login funciona
- [ ] Criar pergunta funciona
- [ ] Pergunta aparece em `/questions`
- [ ] Resposta funciona
- [ ] Resposta aparece na página de detalhe

---

## 🆘 Troubleshooting

### Erro: "Unexpected end of JSON input"
- Solução: Limpe cache com `Remove-Item -Recurse -Force .next`
- Depois reinicie: `npm run dev`

### Erro: "Missing env variables"
- Solução: Verifique `.env.local` tem as duas chaves
- Reinicie servidor

### Erro: "CORS error" ao fazer upload
- Solução: Verifique bucket é "Public"
- Adicione policy de acesso público (veja Passo 3.5)

### Erro: "Pergunta não aparece no feed"
- Solução: Verifique status da pergunta é 'open' (não 'draft')
- Verifique migração SQL foi executada corretamente

### Erro: "Não consigo responder"
- Solução: Faça login primeiro (botão "Login" no header)
- Após login, botão "[💬 Responder...]" deve aparecer

---

## 📚 Documentos Úteis

### Em `docs/`:
- `reqs.md` - Requisitos e user stories
- `architecture.md` - Tech stack
- `auth.md` - Setup de autenticação
- `TASK_8_SUMMARY.md` - Resumo autenticação
- `TASK_9_SUMMARY.md` - Resumo feed + respostas
- `PROGRESS.md` - Status geral do projeto

### Arquivo de Migrations:
- `packages/api/migrations/001_initial_schema.sql`

---

## 🔗 URLs Importantes

### Supabase Dashboard
https://app.supabase.com

### Projeto MicroMentor (local)
http://localhost:3003

### Páginas do MVP:
- Home: http://localhost:3003
- Cadastro: http://localhost:3003/auth/signup
- Login: http://localhost:3003/auth/login
- Criar Pergunta: http://localhost:3003/create-question
- Feed: http://localhost:3003/questions
- Detalhe: http://localhost:3003/questions/[id]

---

## 📞 Próximos Passos

### Após confirmar que tudo funciona:

1. **Criar dados de teste**
   - Crie 2-3 contas diferentes
   - Crie 3-5 perguntas
   - Responda em conta diferente
   - Teste filtro por tags

2. **Testar edge cases**
   - Pergunta sem mídia
   - Pergunta com mídia
   - Resposta sem mídia
   - Resposta com mídia (link)

3. **Próxima tarefa** (escolha uma):
   - Task 10: Validação de mídia (3min max)
   - Task 11: Pagamentos (Stripe)
   - Task 13: Deploy (Vercel)

---

## 💬 Dúvidas Comuns

**P: Posso usar Supabase Free?**  
R: Sim! Free tier tem 500MB storage, até 50k requisições/mês. Suficiente para MVP.

**P: Meus dados são seguros?**  
R: Sim! Supabase usa PostgreSQL com RLS (Row Level Security). Cada usuário só acessa seus dados.

**P: Posso mudar de região depois?**  
R: Não é simples. Escolha região certa agora (Brasil = `sa-east-1`).

**P: E se eu perder a senha do Supabase?**  
R: Pode resetar em Settings → Database. Salve bem!

---

**Status**: ⏳ Aguardando setup do Supabase  
**Após setup**: MVP pronto para testar! ✅

