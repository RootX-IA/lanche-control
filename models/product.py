#banco (SQLALCHEMY)

from extensions import db #e isso que transforma a classe em tabela
from datetime import datetime

class Produto(db.Model): # a classe esta herdando db.Model / quando ela herda db.Model, ela vira um Model mapeado para o banco.
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, default=True) #Produto nasce ativo, nao precisa obrigar envio!
    criado_em = db.Column(db.DateTime, default=datetime.utcnow) #Aqui registra autom quando o registro for criado
    

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "estoque": self.estoque,
            "ativo": self.ativo,
            "criado_em": self.criado_em,
        }