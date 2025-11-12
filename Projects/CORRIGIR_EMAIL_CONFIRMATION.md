# 🔧 Corrigir "Email not confirmed" - Supabase Auth

## ❌ Problema

Ao fazer signup, recebe mensagem:
```
"Email not confirmed"
```

Isso significa que o Supabase está exigindo confirmação de email antes de login.

---

## ✅ Solução

Desabilite a confirmação de email no Supabase Dashboard:

### Passo 1: Acesse Supabase Dashboard
https://app.supabase.com → Selecione projeto "micromentor"

### Passo 2: Vá para Settings → Authentication

### Passo 3: Procure por "Email confirmations"
- Localize: **"Require email confirmation"** ou similar
- Desative (toggle OFF)

### Passo 4: Salve as mudanças

---

## 🎯 Alternativa: Configurar via SQL

Se não conseguir na UI, execute no SQL Editor:

```sql
-- Desabilitar confirmação de email
ALTER TABLE auth.users SET (require_email_verification = false);
```

---

## 📸 Localização Exata no Supabase

1. Dashboard → Projeto
2. Sidebar → **Authentication** (ou **Auth**)
3. Clique em **"Providers"** ou **"Settings"**
4. Procure por:
   - "Require email confirmation" ❌ (desabilitar)
   - "Enable email confirmations" ❌ (desabilitar)
   - "Confirm email" ❌ (desabilitar)
   - Algo similar com "confirm"

---

## ✅ Teste Após Desabilitar

### 1. Crie novo usuário
```
http://localhost:3003/auth/signup
Nome: João Silva
Email: joao@email.com
Senha: senha123
Clique [📝 Criar Conta]
```

### 2. Faça login imediatamente
```
Email: joao@email.com
Senha: senha123
Clique [🔓 Entrar]
```

### ✅ Esperado
- ✅ Login bem-sucedido
- ✅ Redireciona para Home
- ✅ Header mostra seu email
- ✅ Mensagem "Email not confirmed" desaparece

---

## 🆘 Se ainda não funcionar

### Opção A: Deletar usuário e criar novo
1. Supabase Dashboard → Authentication → Users
2. Selecione o usuário
3. Clique "Delete user"
4. Crie novo usuário com email diferente
5. Tente fazer login

### Opção B: Confirmar email manualmente
```sql
-- No SQL Editor do Supabase
UPDATE auth.users 
SET email_confirmed_at = NOW() 
WHERE email = 'joao@email.com';
```

### Opção C: Verificar configurações de Email
1. Dashboard → Settings → Email
2. Verifique se "Email Confirmations" está DESABILITADO
3. Verifique se "Double Confirm" está DESABILITADO

---

## 📝 Resumo da Solução

| Passo | Ação |
|-------|------|
| 1 | Acesse Supabase Dashboard |
| 2 | Vá para Settings → Authentication |
| 3 | Desabilite "Require email confirmation" |
| 4 | Salve mudanças |
| 5 | Teste signup/login |
| ✅ | Deve funcionar agora |

---

## 🎯 Para o MVP

**A melhor prática para MVP é:**
- ✅ Desabilitar confirmação de email (mais rápido para testar)
- ✅ Depois em produção, você pode ativar + mandar email

---

## 📚 Referência

Supabase Docs: https://supabase.com/docs/guides/auth/auth-email

---

**Feito?** Teste signup/login novamente e confirme se funcionou! 

Se precisar de mais ajuda, me avise! 🚀

