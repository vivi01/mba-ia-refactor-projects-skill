from flask import request, jsonify, Response
from typing import Tuple, Any
import models

def listar_produtos() -> Tuple[Response, int]:
    """Controller para listar todos os produtos."""
    produtos = models.get_todos_produtos()
    return jsonify({"dados": produtos, "sucesso": True}), 200

def buscar_produto(id: int) -> Tuple[Response, int]:
    """Controller para buscar um produto por ID."""
    produto = models.get_produto_por_id(id)
    if produto:
        return jsonify({"dados": produto, "sucesso": True}), 200
    return jsonify({"erro": "Produto não encontrado", "sucesso": False}), 404

def buscar_produtos() -> Tuple[Response, int]:
    """Controller para buscar produtos por termo, categoria e preço."""
    termo = request.args.get("q", "")
    categoria = request.args.get("categoria")
    preco_min = request.args.get("preco_min", type=float)
    preco_max = request.args.get("preco_max", type=float)

    resultados = models.buscar_produtos(termo, categoria, preco_min, preco_max)
    return jsonify({"dados": resultados, "total": len(resultados), "sucesso": True}), 200

def criar_produto() -> Tuple[Response, int]:
    """Controller para criar um novo produto."""
    dados = request.get_json()
    if not dados or not all(k in dados for k in ("nome", "preco", "estoque")):
        return jsonify({"erro": "Dados incompletos"}), 400
    
    id = models.criar_produto(
        dados["nome"], 
        dados.get("descricao", ""), 
        dados["preco"], 
        dados["estoque"], 
        dados.get("categoria", "geral")
    )
    return jsonify({"dados": {"id": id}, "sucesso": True}), 201

def atualizar_produto(id: int) -> Tuple[Response, int]:
    """Controller para atualizar um produto existente."""
    dados = request.get_json()
    if not models.get_produto_por_id(id):
        return jsonify({"erro": "Produto não encontrado"}), 404

    models.atualizar_produto(
        id, 
        dados.get("nome"), 
        dados.get("descricao", ""), 
        dados.get("preco"), 
        dados.get("estoque"), 
        dados.get("categoria", "geral")
    )
    return jsonify({"sucesso": True, "mensagem": "Produto atualizado"}), 200

def deletar_produto(id: int) -> Tuple[Response, int]:
    """Controller para remover um produto."""
    if not models.get_produto_por_id(id):
        return jsonify({"erro": "Produto não encontrado"}), 404
    models.deletar_produto(id)
    return jsonify({"sucesso": True}), 200

def listar_usuarios() -> Tuple[Response, int]:
    """Controller para listar todos os usuários."""
    usuarios = models.get_todos_usuarios()
    return jsonify({"dados": usuarios, "sucesso": True}), 200

def buscar_usuario(id: int) -> Tuple[Response, int]:
    """Controller para buscar um usuário por ID."""
    usuario = models.get_usuario_por_id(id)
    if usuario:
        return jsonify({"dados": usuario, "sucesso": True}), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

def criar_usuario() -> Tuple[Response, int]:
    """Controller para cadastrar novo usuário."""
    dados = request.get_json()
    if not dados or not all(k in dados for k in ("nome", "email", "senha")):
        return jsonify({"erro": "Nome, email e senha são obrigatórios"}), 400

    id = models.criar_usuario(dados["nome"], dados["email"], dados["senha"])
    return jsonify({"dados": {"id": id}, "sucesso": True}), 201

def login() -> Tuple[Response, int]:
    """Controller para autenticação."""
    dados = request.get_json()
    usuario = models.login_usuario(dados.get("email"), dados.get("senha"))
    if usuario:
        return jsonify({"dados": usuario, "sucesso": True}), 200
    return jsonify({"erro": "Credenciais inválidas"}), 401

def criar_pedido() -> Tuple[Response, int]:
    """Controller para processar um novo pedido."""
    dados = request.get_json()
    resultado = models.criar_pedido(dados.get("usuario_id"), dados.get("itens", []))
    return jsonify({"dados": resultado, "sucesso": True}), 201

def listar_pedidos_usuario(usuario_id: int) -> Tuple[Response, int]:
    """Controller para listar pedidos de um usuário."""
    pedidos = models.get_pedidos_usuario(usuario_id)
    return jsonify({"dados": pedidos, "sucesso": True}), 200

def listar_todos_pedidos() -> Tuple[Response, int]:
    """Controller para listar todos os pedidos."""
    pedidos = models.get_todos_pedidos()
    return jsonify({"dados": pedidos, "sucesso": True}), 200

def atualizar_status_pedido(pedido_id: int) -> Tuple[Response, int]:
    """Controller para atualizar o status de um pedido."""
    status = request.get_json().get("status")
    if status not in ["pendente", "aprovado", "enviado", "entregue", "cancelado"]:
        return jsonify({"erro": "Status inválido"}), 400
    models.atualizar_status_pedido(pedido_id, status)
    return jsonify({"sucesso": True, "mensagem": "Status atualizado"}), 200

def relatorio_vendas() -> Tuple[Response, int]:
    """Controller para gerar relatório de vendas."""
    relatorio = models.relatorio_vendas()
    return jsonify({"dados": relatorio, "sucesso": True}), 200

def health_check() -> Tuple[Response, int]:
    """Controller para verificação de saúde do sistema."""
    from database import get_db
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT 
            (SELECT COUNT(*) FROM produtos) as produtos,
            (SELECT COUNT(*) FROM usuarios) as usuarios,
            (SELECT COUNT(*) FROM pedidos) as pedidos
    """)
    counts = dict(cursor.fetchone())
    return jsonify({"status": "ok", "database": "connected", "counts": counts}), 200
