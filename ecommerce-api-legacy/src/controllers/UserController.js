const UserModel = require('../models/UserModel');

class UserController {
    async delete(req, res) {
        try {
            const { id } = req.params;
            const user = await UserModel.findById(id);
            if (!user) return res.status(404).json({ erro: "Usuário não encontrado" });

            await UserModel.delete(id);
            return res.json({ msg: "Usuário deletado" });
        } catch (error) {
            return res.status(500).json({ erro: "Erro ao deletar usuário" });
        }
    }
}

module.exports = new UserController();
