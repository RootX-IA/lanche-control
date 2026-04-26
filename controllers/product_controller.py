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


def buscar_produtos():

    dados = Produto.query.all()
    if not dados:
        return jsonify({"error": "Sem produtos cadastrados."}), 404
    produtos_dict = [produto.to_dict() for produto in dados]
    return jsonify(produtos_dict), 200   


def buscar_produto(id):

    produto = Produto.query.get(id)

    if produto is None:
        return jsonify({"error": "Produto não encontrado."}), 404
    return jsonify(produto.to_dict()), 200


def atualizar_produto(id):

    produto = Produto.query.get(id)
    dado = request.get_json()

    if produto is None:
        return jsonify({"error": "Produto não encontrado"}), 404
    if not dado:
        return jsonify({"error": "JSON inválido"}), 400
    
    campos_permitidos = ["nome", "preco", "estoque", "ativo"]

    for chave, valor in dado.items():
        if chave not in campos_permitidos:
            return jsonify({"error": "Nao é possível atualizar esse campo."}), 403
        
        setattr(produto, chave, valor)
        
    db.session.commit()
    return jsonify(produto.to_dict()), 200