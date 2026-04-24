const CourseModel = require('../models/CourseModel');
const UserModel = require('../models/UserModel');
const OrderModel = require('../models/OrderModel');

class CheckoutController {
    async checkout(req, res) {
        try {
            const { usr, eml, pwd, c_id, card } = req.body;

            // Validação de entrada básica (AP-005)
            if (!usr || !eml || !c_id || !card) {
                return res.status(400).json({ erro: "Dados incompletos" });
            }

            const course = await CourseModel.findActiveById(c_id);
            if (!course) {
                return res.status(404).json({ erro: "Curso não encontrado" });
            }

            let user = await UserModel.findByEmail(eml);
            let userId;

            if (!user) {
                userId = await UserModel.create(usr, eml, pwd || "123456");
            } else {
                userId = user.id;
            }

            // Simulação de gateway de pagamento (AP-001: Usando process.env)
            const gatewayKey = process.env.PAYMENT_GATEWAY_KEY;
            console.log(`[PAYMENT] Usando gateway: ${gatewayKey.substring(0, 7)}...`);
            
            const status = card.startsWith("4") ? "PAID" : "DENIED";
            if (status === "DENIED") {
                return res.status(400).json({ erro: "Pagamento recusado" });
            }

            const enrollmentId = await OrderModel.createEnrollment(userId, c_id);
            await OrderModel.createPayment(enrollmentId, course.price, status);
            await OrderModel.logAction(`Checkout curso ${c_id} por ${userId}`);

            return res.status(200).json({ 
                msg: "Sucesso", 
                enrollment_id: enrollmentId 
            });

        } catch (error) {
            console.error(error);
            return res.status(500).json({ erro: "Erro interno no checkout" });
        }
    }
}

module.exports = new CheckoutController();
