# 🔧 SOLUÇÃO: Foreign Key Constraint Violation

## 🚨 Erro Recebido
```
Key (user_id)=(6283ab8a-...) is not present in table "profiles"
```

## ❌ Causa
Você tem perguntas antigas cujo `user_id` não corresponde a nenhum usuário em `profiles`.

## ✅ SOLUÇÃO (3 passos)

### Passo 1: Deletar Dados Incompatíveis

**No Supabase SQL Editor:**

```sql
-- PRIMEIRO: Deletar dados que violam a constraint
DELETE FROM questions WHERE user_id NOT IN (SELECT id FROM profiles);
DELETE FROM answers WHERE mentor_id NOT IN (SELECT id FROM profiles);
DELETE FROM answers WHERE question_id NOT IN (SELECT id FROM questions);
```

**Clique [Run]** → Espere "Success" ✅

### Passo 2: Agora Criar a Constraint

```sql
-- Agora sim, criar a constraint (sem dados ruins)
ALTER TABLE questions DROP CONSTRAINT IF EXISTS questions_user_id_fkey;

ALTER TABLE questions
ADD CONSTRAINT questions_user_id_fkey
FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE;
```

**Clique [Run]** → Espere "Success" ✅

### Passo 3: Criar Outras Constraints

```sql
ALTER TABLE answers DROP CONSTRAINT IF EXISTS answers_question_id_fkey;
ALTER TABLE answers DROP CONSTRAINT IF EXISTS answers_mentor_id_fkey;

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_fkey
FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_mentor_id_fkey
FOREIGN KEY (mentor_id) REFERENCES profiles(id) ON DELETE CASCADE;
```

**Clique [Run]** → Espere "Success" ✅

---

## 🧪 Teste Agora

```
1. Recarregue navegador: F5
2. Crie pergunta nova: http://localhost:3003/create-question
3. Vá para feed: http://localhost:3003/questions
4. Clique na pergunta
5. ✅ Deve funcionar agora!
```

---

## ✅ Checklist

- [ ] Executei DELETE para limpar dados ruins
- [ ] Cliquei [Run] e viu "Success"
- [ ] Criei constraint questions_user_id_fkey
- [ ] Criei constraint answers_question_id_fkey
- [ ] Criei constraint answers_mentor_id_fkey
- [ ] Recarreguei navegador
- [ ] Criei pergunta nova
- [ ] Pergunta aparece em /questions ✅
- [ ] Cliquei e carregou SEM ERRO ✅

**Feito?** Me avisa! 🚀

