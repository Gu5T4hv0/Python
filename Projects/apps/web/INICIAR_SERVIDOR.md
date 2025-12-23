# 🚀 Como Iniciar o Servidor

## Passo a Passo

### 1. Abrir Terminal no Diretório Correto

```powershell
cd "C:\Users\Arthur Gustavo\Documents\Arthur\Code\Python\Projects\apps\web"
```

### 2. Instalar Dependências (se necessário)

```powershell
npm install
```

### 3. Iniciar Servidor de Desenvolvimento

```powershell
npm run dev
```

### 4. Aguardar Compilação

Você deve ver algo como:
```
▲ Next.js 14.x.x
- Local:        http://localhost:3000
- Ready in Xs
```

### 5. Acessar no Navegador

Abra: **http://localhost:3000**

---

## ⚠️ Problemas Comuns

### Porta já em uso

Se a porta 3000 estiver ocupada, o Next.js tentará usar 3001, 3002, etc.

### Erro de Variáveis de Ambiente

Certifique-se de ter um arquivo `.env.local` em `apps/web/` com:

```env
NEXT_PUBLIC_SUPABASE_URL=sua_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=sua_chave
SUPABASE_SERVICE_ROLE_KEY=sua_service_role_key
STRIPE_SECRET_KEY=sua_chave_stripe
STRIPE_WEBHOOK_SECRET=seu_webhook_secret
NEXT_PUBLIC_SITE_URL=http://localhost:3000
```

### Erro de Compilação

Verifique o terminal para ver erros específicos. Comum:
- Imports incorretos
- Tipos TypeScript incorretos
- Arquivos faltando

---

## 📝 Comandos Úteis

```powershell
# Ver processos Node rodando
Get-Process -Name node

# Parar servidor (Ctrl+C no terminal)
# Ou matar processo:
Stop-Process -Name node -Force

# Verificar porta em uso
netstat -ano | findstr :3000
```

---

## 🧪 Testar Funcionalidades

Após iniciar o servidor:

1. **Home:** http://localhost:3000
2. **Criar Pergunta:** http://localhost:3000/create-question
3. **Feed de Perguntas:** http://localhost:3000/questions
4. **Perfil Mentor:** http://localhost:3000/mentor/profile

