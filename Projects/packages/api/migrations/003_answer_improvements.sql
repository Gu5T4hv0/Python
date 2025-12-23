-- Migration: Melhorias no Sistema de Respostas
-- Execute no Supabase SQL Editor

-- Adicionar campos à tabela answers
ALTER TABLE answers
ADD COLUMN IF NOT EXISTS is_best_answer BOOLEAN DEFAULT FALSE,
ADD COLUMN IF NOT EXISTS rating INTEGER CHECK (rating >= 1 AND rating <= 5);

-- Adicionar índice para melhor resposta
CREATE INDEX IF NOT EXISTS idx_answers_is_best_answer ON answers(is_best_answer) WHERE is_best_answer = TRUE;

-- Adicionar campo de melhor resposta na tabela questions
ALTER TABLE questions
ADD COLUMN IF NOT EXISTS best_answer_id UUID REFERENCES answers(id) ON DELETE SET NULL;

