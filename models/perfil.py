from db import db

class PerfilModel(db.Model):
    __tablename__ = "perfil"

    perfil_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, perfil_id, nome, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.perfil_id = perfil_id
        self.nome = nome
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "perfil_id": self.perfil_id,
            "nome": self.nome,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, perfil_id):
        return PerfilModel.query.filter_by(perfil_id=perfil_id,ativo=1).first()

    @classmethod
    def find_by_name(cls, nome):
        return PerfilModel.query.filter_by(nome=nome,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
