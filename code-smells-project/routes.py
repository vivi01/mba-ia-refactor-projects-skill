from flask import Blueprint, jsonify, request
import controllers

api_bp = Blueprint('api', __name__)

# Product Routes
api_bp.route("/produtos", methods=["GET"])(controllers.listar_produtos)
api_bp.route("/produtos/busca", methods=["GET"])(controllers.buscar_produtos)
api_bp.route("/produtos/<int:id>", methods=["GET"])(controllers.buscar_produto)
api_bp.route("/produtos", methods=["POST"])(controllers.criar_produto)
api_bp.route("/produtos/<int:id>", methods=["PUT"])(controllers.atualizar_produto)
api_bp.route("/produtos/<int:id>", methods=["DELETE"])(controllers.deletar_produto)

# User Routes
api_bp.route("/usuarios", methods=["GET"])(controllers.listar_usuarios)
api_bp.route("/usuarios/<int:id>", methods=["GET"])(controllers.buscar_usuario)
api_bp.route("/usuarios", methods=["POST"])(controllers.criar_usuario)
api_bp.route("/login", methods=["POST"])(controllers.login)

# Order Routes
api_bp.route("/pedidos", methods=["POST"])(controllers.criar_pedido)
api_bp.route("/pedidos", methods=["GET"])(controllers.listar_todos_pedidos)
api_bp.route("/pedidos/usuario/<int:usuario_id>", methods=["GET"])(controllers.listar_pedidos_usuario)
api_bp.route("/pedidos/<int:pedido_id>/status", methods=["PUT"])(controllers.atualizar_status_pedido)

# Report Routes
api_bp.route("/relatorios/vendas", methods=["GET"])(controllers.relatorio_vendas)

# System Routes
api_bp.route("/health", methods=["GET"])(controllers.health_check)
