# ⚡ FIX RÁPIDO: Relationship Error (2 MINUTOS)

## 🚨 Erro
```
"Could not find a relationship between 'questions' and 'user_id'"
```

## 🔧 Solução Rápida (3 passos)

### Passo 1: No Supabase SQL Editor, Cole Isto

```sql
-- Droppar constraints antigas
ALTER TABLE questions DROP CONSTRAINT IF EXISTS questions_user_id_fkey;
ALTER TABLE answers DROP CONSTRAINT IF EXISTS answers_mentor_id_fkey;
ALTER TABLE answers DROP CONSTRAINT IF EXISTS answers_question_id_fkey;

-- Criar constraints corretas
ALTER TABLE questions
ADD CONSTRAINT questions_user_id_fkey
FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_fkey
FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_mentor_id_fkey
FOREIGN KEY (mentor_id) REFERENCES profiles(id) ON DELETE CASCADE;

-- Limpar dados antigos
DELETE FROM answers;
DELETE FROM questions;
```

**Clique [Run]** → Espere "Success" ✅

### Passo 2: Recarregue Navegador

```
F5 (ou Ctrl+Shift+R para hard refresh)
```

### Passo 3: Teste

```
1. http://localhost:3003
2. Criar pergunta nova
3. Ir para /questions
4. Clique na pergunta
5. ✅ Deve funcionar agora!
```

---

## 🆘 Se Não Funcionar

Execute este comando de debug:

```sql
SELECT constraint_name FROM information_schema.table_constraints 
WHERE table_name = 'questions' AND constraint_type = 'FOREIGN KEY';
```

**Deve aparecer:**
```
questions_user_id_fkey
```

Se não aparecer = execute o Passo 1 novamente.

---

**Conseguiu?** Me avisa! 🚀

