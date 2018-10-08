from db import db
from models.perfil import PerfilModel
import datetime

class UsuarioModel(db.Model):
    __tablename__ = "usuario"

    usuario_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(12))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    perfil_id = db.Column(db.Integer, db.ForeignKey(PerfilModel.perfil_id))
    valor_hora = db.Column(db.Float(precision=2))
    timezone = db.Column(db.String(5))
    ultimo_login = db.Column(db.Date())
    confirmado = db.Column(db.Integer)
    criado_por = db.Column(db.String(100))
    data_criacao = db.Column(db.Date())
    atualizado_por = db.Column(db.String(100))
    data_ultima_atualizacao = db.Column(db.Date())
    ativo = db.Column(db.Integer)

    def __init__(self, usuario_id, nome, telefone, email, password, perfil_id, valor_hora, timezone, ultimo_login, confirmado, criado_por, data_criacao, atualizado_por, data_ultima_atualizacao, ativo):
        self.usuario_id = usuario_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.password = password
        self.perfil_id = perfil_id
        self.valor_hora = valor_hora
        self.timezone = timezone
        self.ultimo_login = ultimo_login
        self.confirmado = confirmado
        self.criado_por = criado_por
        self.data_criacao = data_criacao
        self.atualizado_por = atualizado_por
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.ativo = ativo

    def json(self):
        return {
            "usuario_id": self.usuario_id,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "password": self.password,
            "perfil_id": self.perfil_id,
            "valor_hora": self.valor_hora,
            "timezone": self.timezone,
            "ultimo_login": self.ultimo_login.strftime('%Y-%m-%d %H:%M:%S'),
            "criado_por": self.criado_por,
            "data_criacao": self.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
            "atualizado_por": self.atualizado_por,
            "data_ultima_atualizacao": self.data_ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S'),
        }

    @classmethod
    def find_by_email(cls, email):
        return UsuarioModel.query.filter_by(email=email,ativo=1).first()

    @classmethod
    def find_by_id(cls, usuario_id):
        return UsuarioModel.query.filter_by(usuario_id=usuario_id,ativo=1).first()

    @classmethod
    def update_last_login(cls, usuario_id):
        user = UsuarioModel.find_by_id(usuario_id)
        if user:
            user.ultimo_login = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            user.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
