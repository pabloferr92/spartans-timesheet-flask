from db import db
from models.cliente import ClienteModel
from models.projeto import ProjetoModel
from models.usuario import UsuarioModel
from models.categoria import CategoriaModel

class LancamentoHorasModel(db.Model):
    __tablename__ = "lancamento_horas"

    lancamento_horas_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey(ProjetoModel.projeto_id))
    cliente_id = db.Column(db.Integer, db.ForeignKey(ClienteModel.cliente_id))
    usuario_id = db.Column(db.Integer, db.ForeignKey(UsuarioModel.usuario_id))
    categoria_id = db.Column(db.Integer, db.ForeignKey(CategoriaModel.categoria_id))
    data_inicio = db.Column(db.Date())
    data_fim = db.Column(db.Date())
    descricao = db.Column(db.String(5000))
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, lancamento_horas_id, projeto_id, cliente_id, usuario_id, categoria_id, data_inicio, data_fim, descricao, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.lancamento_horas_id = lancamento_horas_id
        self.projeto_id = projeto_id
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
        self.categoria_id = categoria_id
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.descricao = descricao
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        data_inicio = self.data_inicio.strftime('%Y-%m-%d %H:%M:%S') if self.data_inicio else ""
        data_fim = self.data_fim.strftime('%Y-%m-%d %H:%M:%S') if self.data_fim else ""
        return {
            "lancamento_horas_id": self.lancamento_horas_id,
            "projeto_id": self.projeto_id,
            "cliente_id": self.cliente_id,
            "usuario_id": self.usuario_id,
            "categoria_id": self.categoria_id,
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "descricao": self.descricao,
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_id(cls, lancamento_horas_id):
        return LancamentoHorasModel.query.filter_by(lancamento_horas_id=lancamento_horas_id,ativo=1).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
