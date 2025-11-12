# ⚠️ DELETAR TABELAS - Guia Seguro

## ❓ Você Perguntou
"Preciso deletar isso para colar o 001_initial_schema?"

## ✅ Resposta: SIM, mas siga EXATAMENTE esta ordem

---

## 🚨 IMPORTANTE

Este comando **DELETA TODOS OS DADOS** nas tabelas! 

Se você tem dados importantes (perguntas, respostas), eles DESAPARECERÃO.

**Para MVP é OK**, pois você pode recriar dados depois.

---

## ✅ PASSO A PASSO CORRETO

### OPÇÃO 1: Se Quer Deletar TUDO (Recomendado para MVP)

**No Supabase SQL Editor:**

```sql
-- Cole isto e clique [Run]
DROP TABLE IF EXISTS answers CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS follows CASCADE;
DROP TABLE IF EXISTS questions CASCADE;
DROP TABLE IF EXISTS profiles CASCADE;
```

**Resultado esperado:**
```
✓ Success
```

**Depois:**
- Novo Query
- Cole migration completa (001_initial_schema.sql)
- Clique [Run]
- ✅ Pronto!

---

### OPÇÃO 2: Se Quer Manter ALGUNS Dados

Se você quer **preservar dados de usuários** (profiles):

```sql
-- Cole isto (deleta apenas dados, mantém tabelas)
TRUNCATE answers CASCADE;
TRUNCATE questions CASCADE;
TRUNCATE transactions CASCADE;
TRUNCATE follows CASCADE;
```

**Depois:**
- Cole migration completa
- Clique [Run]
- ✅ Estrutura atualizada, usuários preservados

---

## 🎯 RECOMENDAÇÃO PARA VOCÊ

**Use OPÇÃO 1** (deletar tudo) porque:

✅ Mais simples
✅ Garante que tudo funciona do zero
✅ Para MVP é aceitável perder dados
✅ Você pode recriar pergunta em 1 minuto

---

## 🧪 TESTE DEPOIS

Após rodar os drops + migration:

```
1. Crie pergunta nova
2. Vá para /questions
3. Clique na pergunta
4. Deve carregar SEM ERRO ✅
```

---

## ⚠️ CUIDADO

**NUNCA execute DROP sem estar 100% certo!**

Perguntas:
- [ ] Você quer deletar TODOS os dados?
- [ ] Você tem backup dos dados?
- [ ] Você está no projeto CERTO (micromentor)?

Se responder SIM-SIM-SIM → pode deletar seguro.

---

## 📝 RESUMO

| Ação | Comando | Resultado |
|------|---------|-----------|
| Deletar TUDO | DROP | ✅ Recomendado para MVP |
| Deletar dados, manter tabelas | TRUNCATE | ⚠️ Para preservar estrutura |

---

**Quer deletar agora?** Confirme que quer usar OPÇÃO 1 (DROP) 👇

