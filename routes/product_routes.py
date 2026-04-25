#ENTRADA HTTP (FLASK)

from flask import Blueprint
from controllers.product_controller import criar_produto
produto_bp = Blueprint("produto_bp", __name__)

produto_bp.route("/produtos", methods=["POST"])(criar_produto)