# 🔐 SUPABASE: Desabilitar Confirmação de Email - GUIA VISUAL

## 📍 Onde Encontrar

### 1️⃣ Abra Dashboard Supabase
```
URL: https://app.supabase.com
```

### 2️⃣ Selecione Seu Projeto
```
Procure "micromentor" na lista
Clique nele
```

### 3️⃣ Vá para Settings

**Opção A: No Sidebar (esquerda)**
```
Sidebar → Settings (ícone de engrenagem)
```

**Opção B: Se não ver Settings**
```
Menu em baixo → Project Settings
```

---

## 🎯 Encontrar a Opção "Email Confirmation"

### Passo 1: Em Settings, vá para "Authentication"

```
Sidebar → Authentication
```

### Passo 2: Clique em "Providers" ou "Email Provider"

```
Você verá:
- Email/Password
- Google
- GitHub
- etc
```

### Passo 3: Configure Email/Password

```
Procure por opções tipo:
❌ "Require email confirmation"
❌ "Enable email confirmations"
❌ "Double confirm email"
```

### Passo 4: Desabilite (coloque OFF/FALSE)

```
Se está LIGADO (azul) → DESLIGUE (cinza)
```

### Passo 5: Salve

```
Clique "Save" ou "Update"
```

---

## 🏠 Se Não Achar, Tente Aqui

### Local 1: Authentication → Settings

```
Supabase Dashboard
  → Authentication (sidebar)
    → Settings (ou Auth Settings)
      → Procure "Require email confirmation"
```

### Local 2: Authentication → Providers

```
Supabase Dashboard
  → Authentication (sidebar)
    → Providers
      → Email (clique)
        → Procure checkbox de confirmação
```

### Local 3: Project Settings → Email

```
Supabase Dashboard
  → Settings (engrenagem)
    → Email Configuration
      → Procure "Email Confirmations"
```

---

## ✅ DEPOIS: Teste Signup/Login

### 1. Abra seu app local
```
http://localhost:3003
```

### 2. Clique "Cadastro"
```
http://localhost:3003/auth/signup
```

### 3. Preencha:
```
Nome: João Silva
Email: joao.silva@email.com
Senha: Senha123!

Clique [📝 Criar Conta]
```

### 4. Deve redirecionar para login automaticamente
```
http://localhost:3003/auth/login
```

### 5. Preencha novamente:
```
Email: joao.silva@email.com
Senha: Senha123!

Clique [🔓 Entrar]
```

### 6. ✅ Esperado: Redireciona para Home com seu email no header!

---

## ❌ Se Ainda Não Funcionar

### Verifique 3 Coisas:

#### 1. Confirmação está desabilitada?
```
Supabase → Authentication → Procure a opção
Status deve ser: OFF/FALSE/Disabled/Unchecked
```

#### 2. Criar nova conta após desabilitar
```
Contas antigas podem estar "marcadas" como não confirmadas
Crie conta NOVA com email diferente
```

#### 3. Limpar cache navegador
```
F12 → DevTools
Ctrl+Shift+Delete → Clear Data
Reabra http://localhost:3003
Tente novamente
```

---

## 🔨 Solução Nuclear (SQL)

Se nada funcionar, execute isto no **SQL Editor** do Supabase:

```sql
-- Marcar TODOS os emails como confirmados
UPDATE auth.users 
SET email_confirmed_at = NOW() 
WHERE email_confirmed_at IS NULL;
```

Depois teste login novamente.

---

## 📊 Checklist Final

- [ ] Abri https://app.supabase.com
- [ ] Selecionei projeto "micromentor"
- [ ] Fui para Authentication
- [ ] Procurei "Require email confirmation"
- [ ] Desabilitei (toggle OFF)
- [ ] Salvei mudanças
- [ ] Criei nova conta em /auth/signup
- [ ] Fiz login com essa conta
- [ ] ✅ Funcionou! (Redireciona para home)

---

**Feito?** Volta aqui e me avisa se funcionou! 🚀

