# ⚡ SOLUÇÃO RÁPIDA: "Could not find a relationship"

## 🚨 Erro ao Ver Feed/Pergunta
```
"Could not find a relationship between 'questions' and 'user_id'"
```

## ❌ Causa
Tabelas foram criadas sem foreign keys.

---

## ✅ SOLUÇÃO (2 MINUTOS)

### 1️⃣ Abra Supabase SQL Editor
```
https://app.supabase.com
→ Seu projeto
→ SQL Editor (no sidebar)
→ New Query
```

### 2️⃣ Copie Migration
```
Abra: packages/api/migrations/001_initial_schema.sql
Copie TODO o arquivo
```

### 3️⃣ Cole no Supabase
```
Cole tudo no SQL Editor
Clique [Run] (ou Ctrl+Enter)
```

### 4️⃣ Espere Resultado
```
✓ Success = funcionou!
✗ Error = tente novamente ou veja abaixo
```

---

## 🆘 Se Não Funcionar

### Opção A: Dropar Tudo e Recriar

```sql
-- Cole isto no SQL Editor:
DROP TABLE IF EXISTS answers CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS follows CASCADE;
DROP TABLE IF EXISTS questions CASCADE;
DROP TABLE IF EXISTS profiles CASCADE;
```

**Depois clique [Run]**

Depois:
- Cole novamente a migration completa
- Clique [Run]

### Opção B: Criar Foreign Keys Manualmente

```sql
ALTER TABLE questions
ADD CONSTRAINT questions_user_id_fkey
FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_question_id_fkey
FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE;

ALTER TABLE answers
ADD CONSTRAINT answers_mentor_id_fkey
FOREIGN KEY (mentor_id) REFERENCES profiles(id) ON DELETE CASCADE;
```

**Cole isto e clique [Run]**

---

## 🧪 Teste

1. Crie pergunta nova: http://localhost:3003/create-question
2. Vá para feed: http://localhost:3003/questions
3. Clique pergunta
4. Deve carregar SEM ERRO ✅

---

## 📞 Próximo

Se funcionou:
- ✅ Crie pergunta
- ✅ Veja no feed
- ✅ Responda
- ✅ MVP completo!

**Feito?** Me avisa! 🚀

