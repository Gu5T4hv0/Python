# 🛠️ Comandos Úteis - MicroMentor MVP

## 🚀 Iniciar Desenvolvimento

### PowerShell (Windows)
```powershell
# Ir para pasta do projeto
cd "c:\Users\Arthur Gustavo\Documents\Arthur\Code\Python\Projects\apps\web"

# Instalar dependências (primeira vez)
npm install

# Iniciar servidor de desenvolvimento
npm run dev

# Acessar em navegador
Start-Process "http://localhost:3003"
```

### Alias Permanente (salvar no PowerShell Profile)
```powershell
# Abrir profile
notepad $PROFILE

# Adicionar no arquivo:
Set-Alias -Name node -Value "C:\Program Files\nodejs\node.exe" -Force
Set-Alias -Name npm -Value "C:\Program Files\nodejs\npm.cmd" -Force
Set-Alias -Name npx -Value "C:\Program Files\nodejs\npx.cmd" -Force
```

---

## 📦 Gerenciar Dependências

```powershell
# Instalar novo pacote
npm install nome-do-pacote

# Instalar versão específica
npm install nome-do-pacote@1.2.3

# Atualizar pacotes
npm update

# Verificar vulnerabilidades
npm audit
npm audit fix

# Limpar cache
npm cache clean --force

# Listar pacotes instalados
npm list --depth=0
```

---

## 🧹 Limpeza e Troubleshooting

```powershell
# Limpar build cache
Remove-Item -Recurse -Force .next

# Deletar node_modules e reinstalar
Remove-Item -Recurse -Force node_modules
npm install

# Verificar portas em uso
Get-NetTCPConnection -State Listen | Where-Object { $_.LocalPort -like "300*" }

# Matar processo Node.js em porta específica
Get-Process node | Stop-Process -Force
# ou
taskkill /PID 12345 /F
```

---

## 🔍 Debugging

```bash
# Verificar erros de build
npm run dev  # Vê todos os erros no console

# Validar TypeScript
npx tsc --noEmit

# Verificar ESLint
npx eslint src/

# Verificar formato com Prettier (se instalado)
npx prettier --check .
npx prettier --write .
```

---

## 📁 Estrutura de Pastas

```
projeto/
├── apps/
│   └── web/                      # Frontend Next.js
│       ├── src/
│       │   ├── app/              # Pages (App Router)
│       │   │   ├── page.tsx      # Home
│       │   │   ├── auth/         # Auth pages
│       │   │   ├── create-question/
│       │   │   ├── questions/    # Feed
│       │   │   └── layout.tsx    # Root layout
│       │   ├── components/       # React components
│       │   ├── lib/              # Utilitários (supabaseClient.ts)
│       │   └── globals.css       # Estilos globais
│       ├── next.config.ts
│       ├── tailwind.config.ts
│       ├── tsconfig.json
│       └── package.json
│
├── packages/
│   └── api/                      # Backend docs
│       └── migrations/           # SQL files
│
├── docs/                         # Documentação
│   ├── reqs.md
│   ├── architecture.md
│   ├── auth.md
│   ├── TASK_*.md
│   └── wireframes.md
│
└── .env.local                   # Env vars (NÃO commitar!)
```

---

## 🗄️ Supabase SQL Útil

```sql
-- Ver todas as perguntas
SELECT * FROM questions ORDER BY created_at DESC;

-- Ver perguntas abertas com autor
SELECT q.*, p.display_name, p.email
FROM questions q
JOIN profiles p ON q.user_id = p.id
WHERE q.status = 'open'
ORDER BY q.created_at DESC;

-- Ver respostas de uma pergunta
SELECT a.*, p.display_name, p.email
FROM answers a
JOIN profiles p ON a.mentor_id = p.id
WHERE a.question_id = 'ID_DA_PERGUNTA'
ORDER BY a.created_at DESC;

-- Atualizar status de pergunta
UPDATE questions SET status = 'answered' WHERE id = 'ID';

-- Contar respostas por pergunta
SELECT question_id, COUNT(*) as resposta_count
FROM answers
GROUP BY question_id;

-- Deletar dado (CUIDADO!)
DELETE FROM questions WHERE id = 'ID_DA_PERGUNTA';
```

---

## 🔐 Gerenciar Autenticação (Supabase)

### Dashboard Supabase
```
1. Vá para https://app.supabase.com
2. Selecione projeto "micromentor"
3. Vá para "Authentication" → "Users"
```

### Verificar User ID
```sql
SELECT id, email, user_metadata FROM auth.users;
```

### Resetar Senha
```
No dashboard: Authentication → Users → Selecione user → Reset password
```

---

## 📝 Editar Arquivos Importantes

### .env.local
```
Localização: apps/web/.env.local

Conteúdo:
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Variáveis de Ambiente
```typescript
// Acessar no código:
const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
```

---

## 🧪 Testar Localmente

```bash
# Testar página específica
GET http://localhost:3003/questions

# Testar com auth token (se implementado)
# Header: Authorization: Bearer TOKEN

# Inspecionar requisições
# DevTools → Network tab (F12)

# Testar formulário
1. Home → Cadastro
2. Preencha form
3. Veja console (F12 → Console)
4. Veja Network (F12 → Network)
```

---

## 📤 Deploy (Vercel)

### Setup Inicial
```bash
# Instalar Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd apps/web
vercel

# Deploy com custom env
vercel env add NEXT_PUBLIC_SUPABASE_URL
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY
vercel deploy
```

---

## 🔄 Git Workflow

```bash
# Ver status
git status

# Adicionar arquivos
git add .
git add arquivo.tsx

# Commit
git commit -m "feat: adicionar feed de perguntas"

# Push
git push origin main

# Ver histórico
git log --oneline

# Ver branches
git branch
```

---

## 📱 Mobile Testing

```bash
# Ver projeto no mobile (mesma rede)
1. Pega IP local: ipconfig (procura IPv4 Address)
2. No celular: http://192.168.1.X:3003
3. DevTools: Toggle device toolbar (F12)
```

---

## 🎬 Atalhos Úteis

### VS Code
```
Ctrl+Shift+D        Debug
Ctrl+Shift+L        Select all occurrences
Ctrl+K Ctrl+C       Comment line
Ctrl+K Ctrl+U       Uncomment line
Ctrl+/              Toggle comment
Alt+Up/Down         Move line
Ctrl+D              Select word
```

### Browser DevTools
```
F12                 Open DevTools
Ctrl+Shift+I        Open Inspector
Ctrl+Shift+J        Console
Ctrl+Shift+C        Element picker
Ctrl+Shift+N        Private mode
```

---

## 🆘 Troubleshooting Rápido

### "Port 3000 is in use"
```powershell
# Use outra porta
npm run dev -- -p 3001

# Ou mate processo no port 3000
lsof -i :3000 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

### "Cannot find module"
```bash
rm -rf node_modules
npm install
npm run dev
```

### "env variables not loading"
```
1. Salve .env.local
2. Reinicie servidor: npm run dev
3. Verifique variáveis: console.log(process.env)
```

### "Cannot reach Supabase"
```
1. Verifique URL está correta
2. Verifique internet
3. Teste curl: curl https://xxxxx.supabase.co/rest/v1/tables
4. Veja logs no console (F12)
```

---

## 📊 Performance

```bash
# Análise de build
npm run build

# Analisar pacotes (Next.js)
npm install --save-dev @next/bundle-analyzer
# Adicione em next.config.ts
# const withBundleAnalyzer = require('@next/bundle-analyzer')
# export default withBundleAnalyzer()(nextConfig)
```

---

## 🔐 Segurança

```
NÃO FAÇA:
- Commit de .env.local
- Expor chaves públicas sensíveis
- Usar Admin Key no frontend (apenas Anon Key)
- Armazenar senhas em plain text

SEMPRE FAÇA:
- Use .env.local (gitignore'd)
- Validate inputs no servidor
- Use HTTPS em produção
- Rotate API keys periodicamente
```

---

## 📚 Referências Rápidas

### Next.js
- App Router: https://nextjs.org/docs/app
- API Routes: https://nextjs.org/docs/app/building-your-application/routing/route-handlers

### Supabase
- Client SDK: https://supabase.com/docs/reference/javascript/client
- SQL: https://supabase.com/docs/guides/database

### Tailwind
- Classes: https://tailwindcss.com/docs/utility-first
- Components: https://tailwindui.com

---

## 🎯 Checklist Pré-Deploy

```
[ ] Variáveis de ambiente (.env.local)
[ ] SQL migrations executadas
[ ] Bucket Supabase criado
[ ] RLS policies ativas
[ ] Sem console.log() de debug
[ ] Sem hardcoded URLs
[ ] TypeScript sem erros (npx tsc --noEmit)
[ ] ESLint sem avisos (npx eslint src/)
[ ] Testar em móvel (responsividade)
[ ] Testar fluxo completo (signup → question → answer)
[ ] Build sem erros (npm run build)
```

---

**Última atualização**: 12 de novembro de 2025  
**Projeto**: MicroMentor MVP

