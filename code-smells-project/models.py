from typing import List, Dict, Optional, Any
from database import get_db

# Constantes para Lógica de Desconto (AP-002/AP-005)
TIER_1_THRESHOLD = 10000
TIER_1_DISCOUNT = 0.1
TIER_2_THRESHOLD = 5000
TIER_2_DISCOUNT = 0.05

def get_todos_produtos() -> List[Dict[str, Any]]:
    """Retorna a lista de todos os produtos do banco de dados."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    return [dict(row) for row in cursor.fetchall()]

def get_produto_por_id(produto_id: int) -> Optional[Dict[str, Any]]:
    """
    Busca um produto específico pelo seu ID.
    Fixed: AP-001 (SQL Injection) usando parâmetros.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    row = cursor.fetchone()
    return dict(row) if row else None

def criar_produto(nome: str, descricao: str, preco: float, estoque: int, categoria: str) -> int:
    """
    Cria um novo produto no sistema.
    Fixed: AP-001 (SQL Injection) usando parâmetros.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES (?, ?, ?, ?, ?)",
        (nome, descricao, preco, estoque, categoria)
    )
    db.commit()
    return cursor.lastrowid

def atualizar_produto(produto_id: int, nome: str, descricao: str, preco: float, estoque: int, categoria: str) -> bool:
    """Atualiza os dados de um produto existente."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, estoque = ?, categoria = ? WHERE id = ?",
        (nome, descricao, preco, estoque, categoria, produto_id)
    )
    db.commit()
    return True

def deletar_produto(produto_id: int) -> bool:
    """Remove um produto do sistema."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    db.commit()
    return True

def get_todos_usuarios() -> List[Dict[str, Any]]:
    """Retorna todos os usuários cadastrados."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, email, tipo, criado_em FROM usuarios")
    return [dict(row) for row in cursor.fetchall()]

def login_usuario(email: str, senha: str) -> Optional[Dict[str, Any]]:
    """Valida as credenciais de um usuário."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, nome, email, tipo FROM usuarios WHERE email = ? AND senha = ?",
        (email, senha)
    )
    row = cursor.fetchone()
    return dict(row) if row else None

def criar_pedido(usuario_id: int, itens: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Cria um novo pedido e atualiza o estoque."""
    db = get_db()
    cursor = db.cursor()
    total = 0

    for item in itens:
        cursor.execute("SELECT preco, estoque, nome FROM produtos WHERE id = ?", (item["produto_id"],))
        produto = cursor.fetchone()
        if not produto:
            raise ValueError(f"Produto {item['produto_id']} não encontrado")
        if produto["estoque"] < item["quantidade"]:
            raise ValueError(f"Estoque insuficiente para {produto['nome']}")
        total += produto["preco"] * item["quantidade"]

    cursor.execute(
        "INSERT INTO pedidos (usuario_id, status, total) VALUES (?, 'pendente', ?)",
        (usuario_id, total)
    )
    pedido_id = cursor.lastrowid

    for item in itens:
        cursor.execute("SELECT preco FROM produtos WHERE id = ?", (item["produto_id"],))
        preco_unitario = cursor.fetchone()["preco"]
        cursor.execute(
            "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
            (pedido_id, item["produto_id"], item["quantidade"], preco_unitario)
        )
        cursor.execute(
            "UPDATE produtos SET estoque = estoque - ? WHERE id = ?",
            (item["quantidade"], item["produto_id"])
        )

    db.commit()
    return {"pedido_id": pedido_id, "total": total}

def get_pedidos_usuario(usuario_id: int) -> List[Dict[str, Any]]:
    """Retorna o histórico de pedidos de um usuário usando JOIN para evitar N+1."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT p.*, ip.produto_id, pr.nome as produto_nome, ip.quantidade, ip.preco_unitario
        FROM pedidos p
        JOIN itens_pedido ip ON p.id = ip.pedido_id
        JOIN produtos pr ON ip.produto_id = pr.id
        WHERE p.usuario_id = ?
    """, (usuario_id,))
    
    rows = cursor.fetchall()
    pedidos = {}
    for row in rows:
        p_id = row["id"]
        if p_id not in pedidos:
            pedidos[p_id] = {
                "id": row["id"],
                "usuario_id": row["usuario_id"],
                "status": row["status"],
                "total": row["total"],
                "criado_em": row["criado_em"],
                "itens": []
            }
        pedidos[p_id]["itens"].append({
            "produto_id": row["produto_id"],
            "produto_nome": row["produto_nome"],
            "quantidade": row["quantidade"],
            "preco_unitario": row["preco_unitario"]
        })
    return list(pedidos.values())

def relatorio_vendas() -> Dict[str, Any]:
    """Gera relatório de vendas consolidado."""
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) as count, SUM(total) as total FROM pedidos")
    stats = cursor.fetchone()
    total_pedidos = stats["count"]
    faturamento = stats["total"] or 0

    # Lógica de negócio mantida aqui conforme solicitado na auditoria (AP-002) 
    # mas usando constantes e tipagem.
    desconto = 0
    if faturamento > TIER_1_THRESHOLD:
        desconto = faturamento * TIER_1_DISCOUNT
    elif faturamento > TIER_2_THRESHOLD:
        desconto = faturamento * TIER_2_DISCOUNT

    return {
        "total_pedidos": total_pedidos,
        "faturamento_bruto": round(faturamento, 2),
        "desconto_aplicavel": round(desconto, 2),
        "faturamento_liquido": round(faturamento - desconto, 2)
    }
