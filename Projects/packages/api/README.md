# Backend (packages/api)

Placeholder para a API do MicroMentor. Para o MVP recomendamos usar Supabase (Auth, Postgres, Storage).

Se preferir rodar uma API local simples, você pode criar um servidor Express/Node ou FastAPI/Python aqui.

Exemplo rápido (Node/Express):

```js
// index.js
const express = require('express');
const app = express();
app.use(express.json());
app.get('/health', (req, res) => res.send({ok: true}));
app.listen(3001);
```

```powershell
cd packages/api
npm install express
npm run dev
```
