from db import db
from models.usuario import UsuarioModel

class SquadModel(db.Model):
    __tablename__ = "squad"

    squad_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    administrador_id = db.Column(db.Integer, db.ForeignKey(UsuarioModel.usuario_id))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, squad_id, nome, administrador_id, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.squad_id = squad_id
        self.nome = nome
        self.administrador_id = administrador_id
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "squad_id": self.squad_id,
            "nome": self.nome,
            "administrador_id": self.administrador_id,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, squad_id):
        return SquadModel.query.filter_by(squad_id=squad_id,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
