# 🔧 CORRIGIR: Trigger "on_auth_user_created" already exists

## 🚨 Erro Recebido
```
ERROR: 42710: trigger "on_auth_user_created" for relation "users" already exists
```

## ❌ Causa
O trigger já foi criado antes, e você está tentando criar novamente.

## ✅ SOLUÇÃO

### Opção 1: Usar Migration Atualizada (RECOMENDADO)

A migration foi corrigida automaticamente!

**Siga estes passos:**

1. Abra: `packages/api/migrations/001_initial_schema.sql`
2. Verifique se tem isto (ao final):
```sql
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
```

3. **Já está assim?** Copie TODO o arquivo novamente
4. No Supabase SQL Editor, execute novamente
5. Clique **[Run]**

**Resultado esperado:**
```
✓ Success
```

---

### Opção 2: Deletar Trigger Manualmente (se não funcionar)

```sql
-- Cole isto no SQL Editor:
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
DROP TRIGGER IF EXISTS update_profiles_updated_at ON profiles;
DROP TRIGGER IF EXISTS update_questions_updated_at ON questions;
DROP TRIGGER IF EXISTS update_answers_updated_at ON answers;
DROP TRIGGER IF EXISTS update_transactions_updated_at ON transactions;
```

**Clique [Run]**

**Depois:**
- Novo Query
- Cole migration completa
- Clique [Run]

---

## 🧪 Teste Após Corrigir

```
1. Crie pergunta nova: http://localhost:3003/create-question
2. Vá para feed: http://localhost:3003/questions
3. Clique na pergunta
4. Deve funcionar SEM ERRO ✅
```

---

## 📝 O Que Mudou na Migration

**Antes (causa erro):**
```sql
CREATE TRIGGER on_auth_user_created ...
```

**Depois (corrigido):**
```sql
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created ...
```

O `DROP IF EXISTS` deleta o trigger se ele já existe, evitando o erro.

---

## ✅ Checklist

- [ ] Abri migration `001_initial_schema.sql`
- [ ] Verifiquei que tem `DROP TRIGGER IF EXISTS`
- [ ] Copiei arquivo completo
- [ ] Colei no Supabase SQL Editor
- [ ] Cliquei [Run]
- [ ] Viu "Success" ✅
- [ ] Testei criar pergunta
- [ ] Pergunta aparece no feed ✅

**Feito?** Me avisa se funcionou! 🚀

