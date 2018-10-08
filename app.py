from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
import pymysql
pymysql.install_as_MySQLdb()

from resources.login import Login
from resources.ativar_usuario import AtivarUsuario
from resources.perfil import Perfil
from resources.categoria import Categoria
from resources.cliente import Cliente
from resources.projeto import Projeto
from resources.usuario import Usuario
from resources.squad import Squad
from resources.membrosSquad import MembrosSquad
from resources.lancamentoHoras import LancamentoHoras

app = Flask(__name__)
app.config["SECRET_KEY"] = "s3cr3tp@ssw0rd"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:P@ssword1@localhost/flasktest'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config["JWT_DEFAULT_REALM"] = "Login Required"
jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'perfil_id': user.perfil_id}

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email

class ErrorFriendlyApi(Api):
    def error_router(self, original_handler, e):
        if type(e) is JWTManager:
            return original_handler(e)
        else:
            return super(ErrorFriendlyApi, self).error_router(original_handler, e)

api = ErrorFriendlyApi(app)#, errors=errors)

api.add_resource(Login, "/login")
api.add_resource(AtivarUsuario, "/ativar/<int:usuario_id>")
api.add_resource(Perfil, "/perfil", "/perfil/<int:perfil_id>")
api.add_resource(Categoria, "/categoria", "/categoria/<int:categoria_id>")
api.add_resource(Cliente, "/cliente", "/cliente/<int:cliente_id>")
api.add_resource(Projeto, "/projeto", "/projeto/<int:projeto_id>")
api.add_resource(Usuario, "/usuario", "/usuario/<int:usuario_id>")
api.add_resource(Squad, "/squad", "/squad/<int:squad_id>")
api.add_resource(MembrosSquad, "/membrossquad", "/membrossquad/<int:membros_squad_id>")
api.add_resource(LancamentoHoras, "/lancamentohoras", "/lancamentohoras/<int:lancamento_horas_id>")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
