# 🔧 CORRIGIR: "Could not find a relationship" Error

## 🚨 Erro Completo
```
"Could not find a relationship between 'questions' and 'user_id' in the schema cache"
```

## ❌ Causa
A migration SQL não executou corretamente, ou as tabelas estão sem foreign keys.

---

## ✅ SOLUÇÃO: Re-executar Migrations

### Passo 1: Limpar Banco de Dados (opcional mas recomendado)

**No Supabase SQL Editor:**

```sql
-- ⚠️ AVISO: Isto deleta TODOS os dados!
DROP TABLE IF EXISTS answers CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS follows CASCADE;
DROP TABLE IF EXISTS questions CASCADE;
DROP TABLE IF EXISTS profiles CASCADE;

-- Depois execute a migration
```

### Passo 2: Copiar Migration Completa

**Abra arquivo:**
```
packages/api/migrations/001_initial_schema.sql
```

**Copie TODO o conteúdo**

### Passo 3: No Supabase SQL Editor

1. Vá para: https://app.supabase.com → Projeto → **SQL Editor**
2. Clique **New Query**
3. **Cole TODO o conteúdo** da migration
4. Clique **Run** (Ctrl+Enter)

**Resultado esperado:**
```
✓ Success
Executed in ... ms
```

### Passo 4: Verificar Tabelas

No SQL Editor, execute:
```sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

Deve aparecer:
- ✅ profiles
- ✅ questions
- ✅ answers
- ✅ transactions
- ✅ follows

### Passo 5: Testar Foreignkey

```sql
-- Verificar que questions tem foreign key para user_id
SELECT constraint_name, table_name, column_name
FROM information_schema.constraint_column_usage
WHERE table_name = 'questions';
```

Deve aparecer algo como:
```
questions_user_id_fkey
```

---

## ⚠️ Se Ainda Não Funcionar

### Opção A: Executar SQL Manualmente (Criar Foreign Keys)

Se as tabelas existem mas sem foreign keys:

```sql
-- Criar foreign key manualmente
ALTER TABLE questions
ADD CONSTRAINT questions_user_id_fkey
FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_mentor_id_fkey
FOREIGN KEY (mentor_id) REFERENCES profiles(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_fkey
FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE;
```

### Opção B: Deletar Tudo e Recriar do Zero

```sql
-- 1. Dropar tabelas
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- 2. Re-executar migration completa (copiar de 001_initial_schema.sql)
```

---

## 🧪 Teste Após Corrigir

### 1. Crie pergunta nova
```
http://localhost:3003/create-question
Preencha formulário
Clique "Enviar Pergunta"
```

### 2. Vá para Feed
```
http://localhost:3003/questions
Sua pergunta deve aparecer ✅
```

### 3. Clique na Pergunta
```
http://localhost:3003/questions/[id]
Deve carregar detalhe SEM ERRO ✅
```

### 4. Tente Responder
```
Clique "[💬 Responder esta Pergunta]"
Escreva resposta
Clique "[✓ Enviar Resposta]"
Resposta aparece ✅
```

---

## 📝 Passo Completo Resumido

| Passo | Ação |
|-------|------|
| 1 | Supabase → SQL Editor → New Query |
| 2 | Cole migration de `001_initial_schema.sql` |
| 3 | Clique **Run** |
| 4 | Verifique tabelas existem |
| 5 | Crie pergunta nova |
| 6 | Teste /questions feed |
| ✅ | Deve funcionar! |

---

## 🔍 Se Precisar Debugar

### Ver todas as tabelas
```sql
SELECT * FROM information_schema.tables 
WHERE table_schema = 'public';
```

### Ver foreign keys
```sql
SELECT * FROM information_schema.table_constraints 
WHERE table_schema = 'public' AND constraint_type = 'FOREIGN KEY';
```

### Ver estrutura da tabela questions
```sql
\d questions
-- ou
DESC questions;
```

---

## ✨ Depois que Funcionar

O fluxo completo será:
- ✅ Criar pergunta
- ✅ Aparece no feed
- ✅ Clica e vê detalhe
- ✅ Responde
- ✅ Resposta aparece
- ✅ MVP funcional!

**Feito?** Me avisa quando conseguir! 🚀

