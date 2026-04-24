const db = require('./Database');

class OrderModel {
    async createEnrollment(userId, courseId) {
        const result = await db.run(
            "INSERT INTO enrollments (user_id, course_id) VALUES (?, ?)",
            [userId, courseId]
        );
        return result.id;
    }

    async createPayment(enrollmentId, amount, status) {
        return await db.run(
            "INSERT INTO payments (enrollment_id, amount, status) VALUES (?, ?, ?)",
            [enrollmentId, amount, status]
        );
    }

    async logAction(action) {
        return await db.run(
            "INSERT INTO audit_logs (action, created_at) VALUES (?, datetime('now'))",
            [action]
        );
    }
}

module.exports = new OrderModel();
