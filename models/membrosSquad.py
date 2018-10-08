from db import db
from models.squad import SquadModel
from models.usuario import UsuarioModel

class MembrosSquadModel(db.Model):
    __tablename__ = "membros_squad"

    membros_squad_id = db.Column(db.Integer, primary_key=True)
    squad_id = db.Column(db.Integer, db.ForeignKey(SquadModel.squad_id))
    usuario_id = db.Column(db.Integer, db.ForeignKey(UsuarioModel.usuario_id))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, membros_squad_id, squad_id, usuario_id, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.membros_squad_id = membros_squad_id
        self.squad_id = squad_id
        self.usuario_id = usuario_id
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "membros_squad_id": self.membros_squad_id,
            "squad_id": self.squad_id,
            "usuario_id": self.usuario_id,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, membros_squad_id):
        return MembrosSquadModel.query.filter_by(membros_squad_id=membros_squad_id,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
