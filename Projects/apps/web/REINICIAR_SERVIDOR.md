# 🔄 Como Reiniciar o Servidor

## Método Rápido

### No Terminal/PowerShell:

1. **Parar o servidor atual:**
   - Pressione `Ctrl+C` no terminal onde o servidor está rodando
   - Ou feche o terminal

2. **Iniciar novamente:**
   ```powershell
   cd apps/web
   npm run dev
   ```

3. **Aguarde aparecer:**
   ```
   ▲ Next.js 14.x.x
   - Local:        http://localhost:3000
   ```

4. **Limpar cache do navegador:**
   - Pressione `Ctrl+Shift+R` (ou `Cmd+Shift+R` no Mac)
   - Ou abra em aba anônima/privada

---

## 🔍 Verificar se as Migrations Foram Aplicadas

### No Supabase SQL Editor, execute:

```sql
-- Verificar tabela de notificações
SELECT COUNT(*) as total FROM notifications;

-- Verificar colunas em answers
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'answers' 
AND column_name IN ('is_best_answer', 'rating');

-- Verificar coluna em questions
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'questions' 
AND column_name = 'best_answer_id';
```

**Resultado esperado:**
- `notifications`: deve retornar uma linha com `total: 0` (ou número de notificações)
- `answers`: deve retornar 2 linhas (`is_best_answer`, `rating`)
- `questions`: deve retornar 1 linha (`best_answer_id`)

Se aparecerem esses resultados, as migrations foram aplicadas! ✅

---

## 🐛 Se Ainda Não Funcionar

### 1. Limpar Cache do Navegador
- Pressione `F12` para abrir DevTools
- Clique com botão direito no botão de recarregar
- Escolha "Limpar cache e recarregar forçadamente"

### 2. Verificar Console do Navegador
- Pressione `F12`
- Vá na aba "Console"
- Veja se há erros em vermelho
- Me envie os erros se houver

### 3. Verificar se o Servidor Está Rodando
- Acesse: http://localhost:3000
- Se não abrir, o servidor não está rodando

### 4. Verificar Variáveis de Ambiente
- Certifique-se de que `.env.local` existe em `apps/web/`
- Verifique se tem as chaves do Supabase configuradas

---

## ✅ Checklist Rápido

- [ ] Migrations executadas no Supabase
- [ ] Servidor reiniciado (`npm run dev`)
- [ ] Cache do navegador limpo (Ctrl+Shift+R)
- [ ] Logado no site
- [ ] Console do navegador sem erros



