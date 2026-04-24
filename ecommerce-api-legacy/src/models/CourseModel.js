const db = require('./Database');

class CourseModel {
    async findActiveById(id) {
        return await db.get("SELECT * FROM courses WHERE id = ? AND active = 1", [id]);
    }

    async getAll() {
        return await db.all("SELECT * FROM courses");
    }

    async getReportData() {
        // Resolvendo AP-004 (N+1) usando JOIN
        const sql = `
            SELECT 
                c.title as course,
                u.name as student,
                p.amount as paid,
                p.status
            FROM courses c
            LEFT JOIN enrollments e ON c.id = e.course_id
            LEFT JOIN users u ON e.user_id = u.id
            LEFT JOIN payments p ON e.id = p.enrollment_id
        `;
        return await db.all(sql);
    }
}

module.exports = new CourseModel();
