#ENTRADA HTTP (FLASK)

from flask import Blueprint
from controllers.product_controller import (
    criar_produto,
    buscar_produtos,
    buscar_produto,
    atualizar_produto,
    deletar_produto,
)
produto_bp = Blueprint("produto_bp", __name__)

produto_bp.route("/produtos", methods=["POST"])(criar_produto)
produto_bp.route("/produtos", methods=["GET"])(buscar_produtos)
produto_bp.route("/produtos/<int:id>", methods=["GET"])(buscar_produto)
produto_bp.route("/produtos/<int:id>", methods=["PATCH"])(atualizar_produto)
produto_bp.route("/produtos/<int:id>", methods=["DELETE"])(deletar_produto)
