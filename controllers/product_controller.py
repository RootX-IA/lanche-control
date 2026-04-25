#REGRAS DE NEGOCIO
#-valida dados
#-conversa com banco
#-retorna resultado puro
from flask import request, jsonify, Flask
from extensions import db
from models.product import Produto

def criar_produto():
    dados = request.get_json()
    
    if not dados:
        return jsonify({"error": "JSON inválido"}), 400

    nome = dados.get("nome")
    preco = dados.get("preco")
    estoque = dados.get("estoque")

    if not nome or preco is None or estoque is None:
        return jsonify({"error": "Campos: Nome, Preço e Estoque são obrigatórios!"}), 400
    
    produto = Produto(
        nome = nome,
        preco = preco,
        estoque = estoque
    )

    db.session.add(produto)
    db.session.commit()
    return jsonify(produto.to_dict()), 201