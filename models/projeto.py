from db import db
from models.cliente import ClienteModel
from models.squad import SquadModel

class ProjetoModel(db.Model):
    __tablename__ = "projeto"

    projeto_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cliente_id = db.Column(db.Integer, db.ForeignKey(ClienteModel.cliente_id))
    squad_id = db.Column(db.Integer, db.ForeignKey(SquadModel.squad_id))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, projeto_id, nome, cliente_id, squad_id, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.projeto_id = projeto_id
        self.nome = nome
        self.cliente_id = cliente_id
        self.squad_id = squad_id
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "projeto_id": self.projeto_id,
            "nome": self.nome,
            "cliente_id": self.cliente_id,
            "squad_id": self.squad_id,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, projeto_id):
        return ProjetoModel.query.filter_by(projeto_id=projeto_id,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
