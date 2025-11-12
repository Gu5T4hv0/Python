-- MicroMentor Database Schema
-- Migrations para Supabase
-- Crie um projeto no Supabase (https://supabase.com) e rode estes scripts no SQL Editor

-- ============================================
-- 1. TABELA: users (auth.users + profile extension)
-- ============================================
-- Nota: Supabase já cria auth.users automaticamente
-- Precisamos de uma tabela profiles para dados adicionais

CREATE TABLE IF NOT EXISTS profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT NOT NULL UNIQUE,
  display_name TEXT,
  bio TEXT,
  avatar_url TEXT,
  is_mentor BOOLEAN DEFAULT FALSE,
  mentor_tags TEXT[] DEFAULT '{}',  -- Tags de expertise (ex: ['growth', 'marketing'])
  mentor_rate DECIMAL(10, 2) DEFAULT 10.00,  -- Preço padrão que o mentor aceita
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- 2. TABELA: questions
-- ============================================
CREATE TABLE IF NOT EXISTS questions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  tags TEXT[] DEFAULT '{}',  -- Tags para matching
  price DECIMAL(10, 2) NOT NULL CHECK (price >= 5 AND price <= 500),
  status TEXT DEFAULT 'open' CHECK (status IN ('open', 'answered', 'closed')),
  
  -- Mídia
  media_url TEXT,
  media_type TEXT CHECK (media_type IN ('audio', 'video', NULL)),
  media_duration_seconds INTEGER,
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- 3. TABELA: answers
-- ============================================
CREATE TABLE IF NOT EXISTS answers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  mentor_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  
  body TEXT,
  media_url TEXT,
  media_type TEXT CHECK (media_type IN ('audio', 'video', NULL)),
  media_duration_seconds INTEGER,
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- 4. TABELA: transactions
-- ============================================
CREATE TABLE IF NOT EXISTS transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id UUID NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  mentor_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  answer_id UUID REFERENCES answers(id) ON DELETE SET NULL,
  
  amount DECIMAL(10, 2) NOT NULL,  -- Preço da pergunta
  platform_fee DECIMAL(10, 2) NOT NULL,  -- 20% (plataforma)
  mentor_amount DECIMAL(10, 2) NOT NULL,  -- 80% (mentor)
  
  stripe_payment_id TEXT,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- 5. TABELA: follows (mentores)
-- ============================================
CREATE TABLE IF NOT EXISTS follows (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  follower_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  mentor_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  
  UNIQUE(follower_id, mentor_id),
  CHECK (follower_id != mentor_id)
);

-- ============================================
-- 6. ÍNDICES (performance)
-- ============================================
CREATE INDEX idx_questions_user_id ON questions(user_id);
CREATE INDEX idx_questions_status ON questions(status);
CREATE INDEX idx_questions_tags ON questions USING GIN(tags);
CREATE INDEX idx_questions_created_at ON questions(created_at DESC);

CREATE INDEX idx_answers_question_id ON answers(question_id);
CREATE INDEX idx_answers_mentor_id ON answers(mentor_id);

CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_mentor_id ON transactions(mentor_id);
CREATE INDEX idx_transactions_status ON transactions(status);

CREATE INDEX idx_follows_follower_id ON follows(follower_id);
CREATE INDEX idx_follows_mentor_id ON follows(mentor_id);

CREATE INDEX idx_profiles_is_mentor ON profiles(is_mentor);
CREATE INDEX idx_profiles_mentor_tags ON profiles USING GIN(mentor_tags);

-- ============================================
-- 7. ROW LEVEL SECURITY (RLS) - Segurança
-- ============================================

-- Habilitar RLS em todas as tabelas
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE answers ENABLE ROW LEVEL SECURITY;
ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE follows ENABLE ROW LEVEL SECURITY;

-- ============================================
-- PROFILES - RLS Policies
-- ============================================
-- Qualquer usuário autenticado pode ler perfis públicos
CREATE POLICY "Profiles are publicly readable" ON profiles
  FOR SELECT USING (TRUE);

-- Usuários só podem atualizar seu próprio perfil
CREATE POLICY "Users can update their own profile" ON profiles
  FOR UPDATE USING (auth.uid() = id);

-- Usuários só podem inserir seu próprio perfil (ao fazer signup)
CREATE POLICY "Users can insert their own profile" ON profiles
  FOR INSERT WITH CHECK (auth.uid() = id);

-- ============================================
-- QUESTIONS - RLS Policies
-- ============================================
-- Qualquer usuário autenticado pode ler perguntas
CREATE POLICY "Questions are readable by authenticated users" ON questions
  FOR SELECT USING (auth.role() = 'authenticated');

-- Usuários só podem criar perguntas como eles mesmos
CREATE POLICY "Users can create questions" ON questions
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Usuários só podem atualizar suas próprias perguntas
CREATE POLICY "Users can update their own questions" ON questions
  FOR UPDATE USING (auth.uid() = user_id);

-- Usuários só podem deletar suas próprias perguntas
CREATE POLICY "Users can delete their own questions" ON questions
  FOR DELETE USING (auth.uid() = user_id);

-- ============================================
-- ANSWERS - RLS Policies
-- ============================================
-- Qualquer usuário autenticado pode ler respostas
CREATE POLICY "Answers are readable by authenticated users" ON answers
  FOR SELECT USING (auth.role() = 'authenticated');

-- Apenas mentores podem criar respostas (validado por trigger)
CREATE POLICY "Mentors can create answers" ON answers
  FOR INSERT WITH CHECK (auth.uid() = mentor_id);

-- Mentores só podem atualizar suas próprias respostas
CREATE POLICY "Mentors can update their own answers" ON answers
  FOR UPDATE USING (auth.uid() = mentor_id);

-- ============================================
-- TRANSACTIONS - RLS Policies
-- ============================================
-- Usuários só podem ler suas próprias transações (como payer ou mentor)
CREATE POLICY "Users can read their own transactions" ON transactions
  FOR SELECT USING (
    auth.uid() = user_id OR auth.uid() = mentor_id
  );

-- Sistema (service role) pode inserir transações
CREATE POLICY "Service can insert transactions" ON transactions
  FOR INSERT WITH CHECK (TRUE);

-- ============================================
-- FOLLOWS - RLS Policies
-- ============================================
-- Qualquer usuário autenticado pode ver quem segue quem
CREATE POLICY "Follows are readable by authenticated users" ON follows
  FOR SELECT USING (auth.role() = 'authenticated');

-- Usuários só podem seguir como eles mesmos
CREATE POLICY "Users can create follows" ON follows
  FOR INSERT WITH CHECK (auth.uid() = follower_id);

-- Usuários só podem deletar seus próprios follows
CREATE POLICY "Users can delete their own follows" ON follows
  FOR DELETE USING (auth.uid() = follower_id);

-- ============================================
-- 8. FUNÇÕES E TRIGGERS
-- ============================================

-- Função para atualizar updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers para updated_at
CREATE TRIGGER update_profiles_updated_at BEFORE UPDATE ON profiles
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_questions_updated_at BEFORE UPDATE ON questions
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_answers_updated_at BEFORE UPDATE ON answers
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_transactions_updated_at BEFORE UPDATE ON transactions
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Função para criar profile automaticamente ao fazer signup
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, email, display_name)
  VALUES (new.id, new.email, new.email);
  RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- Trigger para criar profile ao fazer signup
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- ============================================
-- 9. DADOS DE TESTE (OPCIONAL)
-- ============================================
-- Remova comentários (#) para executar
/*
-- Inserir um mentor de teste
INSERT INTO profiles (id, email, display_name, is_mentor, mentor_tags, mentor_rate)
VALUES 
  (gen_random_uuid(), 'mentor@example.com', 'João Mentor', TRUE, ARRAY['growth', 'marketing', 'startup'], 25.00);

-- Inserir uma pergunta de teste
INSERT INTO questions (user_id, title, description, tags, price, status)
VALUES 
  (gen_random_uuid(), 'Como crescer meu app?', 'Tenho 100 usuários, quero chegar a 1000 em 3 meses. Alguma estratégia?', ARRAY['growth', 'startup'], 15.00, 'pending');
*/

-- ============================================
-- 10. VIEWS ÚTEIS (OPCIONAL)
-- ============================================

-- View: Perguntas com info do autor
CREATE OR REPLACE VIEW questions_with_author AS
SELECT 
  q.id,
  q.title,
  q.description,
  q.tags,
  q.price,
  q.status,
  q.created_at,
  p.display_name as author_name,
  p.avatar_url as author_avatar
FROM questions q
LEFT JOIN profiles p ON q.user_id = p.id;

-- View: Respostas com info do mentor
CREATE OR REPLACE VIEW answers_with_mentor AS
SELECT 
  a.id,
  a.question_id,
  a.body,
  a.media_url,
  a.media_type,
  a.created_at,
  p.display_name as mentor_name,
  p.avatar_url as mentor_avatar,
  p.mentor_rate
FROM answers a
LEFT JOIN profiles p ON a.mentor_id = p.id;

-- ============================================
-- FIM DAS MIGRATIONS
-- ============================================
-- Próximos passos:
-- 1. Execute este script no Supabase SQL Editor
-- 2. Configure as variáveis de ambiente (.env) com SUPABASE_URL e SUPABASE_ANON_KEY
-- 3. Integre o cliente Supabase no frontend Next.js
