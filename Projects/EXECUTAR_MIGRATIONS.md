# 📝 Como Executar as Migrations SQL no Supabase

## Passo a Passo Detalhado

### 1. Acessar o Supabase Dashboard

1. Abra seu navegador e vá para: **https://app.supabase.com**
2. Faça login na sua conta
3. Selecione o projeto **MicroMentor** (ou o nome do seu projeto)

### 2. Abrir o SQL Editor

1. No menu lateral esquerdo, procure por **"SQL Editor"** (ícone de código `</>`)
2. Clique nele
3. Você verá uma tela com uma área de texto grande para escrever SQL

### 3. Executar a Migration de Notificações

1. Abra o arquivo: `packages/api/migrations/002_notifications.sql`
2. **Copie TODO o conteúdo** (Ctrl+A, Ctrl+C)
3. Volte para o Supabase SQL Editor
4. **Cole o conteúdo** na área de texto (Ctrl+V)
5. Clique no botão **"Run"** (botão verde no canto inferior direito) ou pressione **Ctrl+Enter**
6. Aguarde alguns segundos
7. Você deve ver: **"Success. No rows returned"** ou **"Success"**

### 4. Executar a Migration de Melhorias de Respostas

1. Clique em **"New query"** (botão azul no canto superior direito) para criar uma nova query
2. Abra o arquivo: `packages/api/migrations/003_answer_improvements.sql`
3. **Copie TODO o conteúdo** (Ctrl+A, Ctrl+C)
4. Cole na nova query no Supabase
5. Clique em **"Run"** ou pressione **Ctrl+Enter**
6. Aguarde alguns segundos
7. Você deve ver: **"Success"**

### 5. Verificar se Funcionou

Execute esta query no SQL Editor para verificar:

```sql
-- Verificar tabela de notificações
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 
AND table_name = 'notifications';

-- Verificar colunas adicionadas em answers
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'answers' 
AND column_name IN ('is_best_answer', 'rating');
```

Se aparecerem resultados, está tudo certo! ✅

---

## 🚨 Problemas Comuns

### Erro: "relation already exists"
- Significa que a tabela já existe. Isso é OK, pode ignorar ou deletar a tabela primeiro.

### Erro: "column already exists"
- Significa que as colunas já foram adicionadas. Isso é OK também.

### Não aparece o botão "Run"
- Certifique-se de que está no **SQL Editor**, não em outra seção
- Tente recarregar a página

---

## ✅ Pronto!

Após executar as migrations, as novas funcionalidades estarão disponíveis!



