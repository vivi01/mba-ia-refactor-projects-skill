const db = require('./Database');
const bcrypt = require('bcryptjs');

class UserModel {
    async findByEmail(email) {
        return await db.get("SELECT * FROM users WHERE email = ?", [email]);
    }

    async findById(id) {
        return await db.get("SELECT id, name, email FROM users WHERE id = ?", [id]);
    }

    async create(name, email, password) {
        const hash = await bcrypt.hash(password, 10); // Resolvendo AP-003
        const result = await db.run(
            "INSERT INTO users (name, email, pass) VALUES (?, ?, ?)",
            [name, email, hash]
        );
        return result.id;
    }

    async delete(id) {
        return await db.run("DELETE FROM users WHERE id = ?", [id]);
    }

    async getAll() {
        return await db.all("SELECT id, name, email FROM users");
    }
}

module.exports = new UserModel();
