# Supabase Schema Setup

## O que contém este arquivo

`001_initial_schema.sql` — schema completo do MicroMentor com:
- **Tabelas:** profiles, questions, answers, transactions, follows
- **Segurança:** Row Level Security (RLS) policies
- **Índices:** para performance de queries
- **Triggers:** para atualizar timestamps automaticamente
- **Funções:** para criar perfil ao fazer signup
- **Views:** para queries comuns

## Como usar

### 1. Criar projeto Supabase
- Acesse https://supabase.com e crie uma conta
- Crie um novo projeto (escolha região mais próxima, ex: São Paulo)
- Anote a URL e ANON KEY (você precisará depois)

### 2. Executar migrations
- Acesse o Supabase Dashboard > SQL Editor
- Crie um novo query
- Copie e cole todo o conteúdo de `001_initial_schema.sql`
- Clique em "Run" (botão verde)
- Aguarde a execução (deve ser rápido, ~5-10s)

### 3. Verificar se funcionou
- Vá para "Table Editor" no Supabase Dashboard
- Você deve ver as tabelas: `profiles`, `questions`, `answers`, `transactions`, `follows`
- Se vir, parabéns! ✓

### 4. Configurar variáveis de ambiente
- Na raiz do projeto, adicione ao `.env.local`:
  ```
  NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
  NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
  ```
- Encontre essas chaves em: Supabase Dashboard > Settings > API

### 5. (Opcional) Dados de teste
- Descomente a seção "DADOS DE TESTE" no SQL e execute novamente
- Isso insere dados fictícios para testar

## Estrutura do banco

### profiles
- Dados do usuário (nome, bio, avatar)
- Flag `is_mentor` (TRUE = é mentor)
- Array de tags de expertise (ex: ['growth', 'marketing'])

### questions
- Pergunta do usuário (título, descrição)
- Tags para matching
- Preço (R$5-R$500)
- Status (pending, answered, closed)
- Media (áudio/vídeo opcional)

### answers
- Resposta do mentor (body + media)
- Vinculada à pergunta e ao mentor

### transactions
- Registro de pagamento
- Calcula fee (20%) e mentor_amount (80%)
- Status: pending, completed, failed, refunded

### follows
- Usuário segue mentor
- Para notificações e relacionamento

## Segurança (RLS)

Todas as tabelas têm Row Level Security habilitado:
- Usuários só veem/editam seus próprios dados
- Mentores só podem responder como eles mesmos
- Service role (backend) tem acesso total

## Próximos passos

1. **Integrar Supabase no frontend** (instalar @supabase/supabase-js)
2. **Criar client Supabase** (utils/supabase.ts)
3. **Integrar CreateQuestionForm com Supabase** (salvar pergunta no BD)
4. **Integrar Auth** (signup/login com Supabase Auth)
5. **Criar feed de perguntas** (query com filtros)

