const CourseModel = require('../models/CourseModel');

class AdminController {
    async financialReport(req, res) {
        try {
            const rawData = await CourseModel.getReportData();
            
            // Transformação dos dados JOIN em formato estruturado (AP-004 fix)
            const reportMap = {};
            
            rawData.forEach(row => {
                if (!reportMap[row.course]) {
                    reportMap[row.course] = { course: row.course, revenue: 0, students: [] };
                }
                
                if (row.student) {
                    if (row.status === 'PAID') {
                        reportMap[row.course].revenue += row.paid;
                    }
                    reportMap[row.course].students.push({
                        student: row.student,
                        paid: row.paid || 0
                    });
                }
            });

            return res.json(Object.values(reportMap));
        } catch (error) {
            console.error(error);
            return res.status(500).json({ erro: "Erro ao gerar relatório" });
        }
    }
}

module.exports = new AdminController();
