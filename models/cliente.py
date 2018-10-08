from db import db

class ClienteModel(db.Model):
    __tablename__ = "cliente"

    cliente_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, cliente_id, nome, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.cliente_id = cliente_id
        self.nome = nome
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "cliente_id": self.cliente_id,
            "nome": self.nome,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, cliente_id):
        return ClienteModel.query.filter_by(cliente_id=cliente_id,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
