const express = require('express');
const router = express.Router();
const CheckoutController = require('../controllers/CheckoutController');
const AdminController = require('../controllers/AdminController');
const UserController = require('../controllers/UserController');

router.post('/checkout', CheckoutController.checkout);
router.get('/admin/financial-report', AdminController.financialReport);
router.delete('/users/:id', UserController.delete);

module.exports = router;
