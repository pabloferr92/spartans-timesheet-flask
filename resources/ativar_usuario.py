from flask_restful import Resource, reqparse, request
from models.usuario import UsuarioModel
from werkzeug.security import safe_str_cmp
import datetime

class AtivarUsuario(Resource):

    def put(self, usuario_id):
        usuario = UsuarioModel.find_by_id(usuario_id)
        if usuario is None:
            return {'message': "Usuário Inexistente."}, 400
        else:
            usuario.ativo = 1
            usuario.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

            usuario.save_to_db()
            return {"message", "Usuário ativo"}
