# Implementação de Autenticação ✅

## O que foi criado

### 1. **AuthForm Component** (`src/components/AuthForm.tsx`)
Componente reutilizável com dois modos:
- **Modo `login`**: Email + Senha
- **Modo `signup`**: Email + Senha + Nome

Recursos:
- ✅ Validação de email, senha (min 6 caracteres), nome
- ✅ Integração com `supabase.auth.signUp()` e `supabase.auth.signInWithPassword()`
- ✅ Tratamento de erros
- ✅ Carregamento e estado de sucesso
- ✅ Links entre páginas de login/signup

### 2. **Header Component** (`src/components/Header.tsx`)
Componente de navegação que:
- ✅ Escuta mudanças de autenticação em tempo real (`onAuthStateChange`)
- ✅ Mostra email do usuário quando autenticado
- ✅ Botão "Sair" que faz logout
- ✅ Links "Login" e "Cadastro" quando desautenticado

### 3. **Páginas de Auth**
- **`/auth/login`** - Página de login
- **`/auth/signup`** - Página de cadastro

### 4. **Proteção de Rota**
- **`/create-question`** agora requer autenticação
- Redireciona para `/auth/login` se não autenticado

---

## Fluxo de Uso

### ✅ Cadastro (Novo Usuário)
1. Clique em **"Cadastro"** no header
2. Preencha: Nome, Email, Senha
3. Clique em **"📝 Criar Conta"**
4. Será redirecionado para login com mensagem de sucesso
5. Faça login com suas credenciais

### ✅ Login (Usuário Existente)
1. Clique em **"Login"** no header
2. Preencha: Email, Senha
3. Clique em **"🔓 Entrar"**
4. Será redirecionado para home autenticado
5. Header agora mostra seu email e botão "Sair"

### ✅ Fazer Pergunta (Autenticado)
1. Clique em **"🚀 Fazer uma Pergunta"** (home)
2. Será permitido acessar `/create-question`
3. Preencha o formulário e envie a pergunta
4. A pergunta será salva no Supabase com seu `user_id`

---

## ⚙️ Próximos Passos Necessários

### 1. **Criar Projeto Supabase** (se ainda não fez)
- Acesse: https://app.supabase.com
- Clique em **"New Project"**
- Preencha: Project Name, Database Password, Region
- Clique em **"Create new project"**

### 2. **Executar Migrations SQL**
- No Supabase Dashboard, vá para **SQL Editor**
- Crie um novo query e copie o conteúdo de:
  ```
  packages/api/migrations/001_initial_schema.sql
  ```
- Execute (botão **"Run"** ou Ctrl+Enter)
- ✅ Tabelas e RLS policies criadas

### 3. **Criar Storage Bucket**
- No Supabase Dashboard, vá para **Storage**
- Clique em **"Create a new bucket"**
- Nome: `question-media`
- Tipo: **Public**
- Clique em **"Create bucket"**

### 4. **Configurar Variáveis de Ambiente**
- No Supabase Dashboard, clique em **Settings → API**
- Copie:
  - **Project URL** → `NEXT_PUBLIC_SUPABASE_URL`
  - **anon public** key → `NEXT_PUBLIC_SUPABASE_ANON_KEY`

- Crie arquivo `.env.local` na raiz do projeto (`apps/web/.env.local`):
  ```env
  NEXT_PUBLIC_SUPABASE_URL=https://seu-project-url.supabase.co
  NEXT_PUBLIC_SUPABASE_ANON_KEY=seu-anon-key-aqui
  ```

### 5. **Reiniciar Dev Server**
```bash
npm run dev
```

---

## ✨ Resultado Final

Agora você pode:
1. ✅ Criar conta (cadastro com email)
2. ✅ Fazer login
3. ✅ Ver seu email no header
4. ✅ Acessar `/create-question` protegido
5. ✅ Enviar pergunta que fica associada ao seu perfil
6. ✅ Fazer logout

---

## 📝 Validações Implementadas

### AuthForm
- Email válido (regex)
- Senha mínimo 6 caracteres
- Nome mínimo 2 caracteres
- Mensagens de erro específicas

### CreateQuestionForm (existente)
- Título não vazio
- Descrição mínimo 10 caracteres
- Preço R$5-500
- Arquivo até 50MB (se selecionado)

---

## 🚀 Testar Agora

1. Acesse: http://localhost:3003
2. Clique em **"Cadastro"**
3. Preencha o formulário
4. Clique em **"Fazer uma Pergunta"** 
5. ✅ Você será redirecionado para login (se não autenticado) ou poderá preencher o formulário (se autenticado)

---

## 📚 Código Importante

### AuthForm.tsx - Signup
```tsx
const { data, error } = await supabase.auth.signUp({
  email,
  password,
  options: {
    data: { display_name: displayName },
  },
});
```

### AuthForm.tsx - Login
```tsx
const { data, error } = await supabase.auth.signInWithPassword({
  email,
  password,
});
```

### CreateQuestionPage.tsx - Proteção
```tsx
const { data: { user } } = await supabase.auth.getUser();
if (!user) {
  router.push('/auth/login?redirect=/create-question');
}
```

### Header.tsx - Listener em Tempo Real
```tsx
const { data: listener } = supabase.auth.onAuthStateChange((_event, session) => {
  setUser(session?.user ?? null);
});
```

---

## ❓ Perguntas Comuns

**P: Por que preciso criar um projeto Supabase?**
R: Sem Supabase, não há banco de dados para salvar usuários, perguntas e respostas.

**P: Posso usar outro provedor de autenticação?**
R: Sim, mas precisaria refatorar para Auth0, Firebase, etc. Por agora, Supabase é a escolha.

**P: Como os dados de autenticação são seguros?**
R: Supabase usa JWT. Token é armazenado no localStorage do navegador (seguro para leitura apenas).

**P: Posso usar senha do GitHub/Google para login?**
R: Sim! Isso pode ser adicionado com `signInWithOAuth()` em uma próxima fase.

---

**Status**: ✅ Autenticação completa e funcional
**Próximo passo sugerido**: Criar página de Feed (listar perguntas) ou implementar resposta de mentores

