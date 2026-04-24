require('dotenv').config();
const express = require('express');
const apiRoutes = require('./routes/apiRoutes');

const app = express();
app.use(express.json());

// Registro de Rotas (View/Route Layer no MVC)
app.use('/api', apiRoutes);

// Rota Root
app.get('/', (req, res) => {
    res.json({
        mensagem: "Frankenstein LMS Refatorado (MVC)",
        versao: "2.0.0",
        ambiente: process.env.NODE_ENV
    });
});

// Middleware Global de Erro
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ erro: "Erro interno do servidor" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`[SERVER] Rodando na porta ${PORT}...`);
});
