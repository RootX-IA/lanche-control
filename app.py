from flask import Flask
from extensions import db, migrate
from models.product import Produto

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgre@localhost:5433/lanche_control"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

from routes.product_routes import produto_bp
app.register_blueprint(produto_bp)

if __name__ == "__main__":
    app.run(debug=True)