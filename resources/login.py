from flask_restful import Resource, request
from models.usuario import UsuarioModel
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp

class Login(Resource):
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = UsuarioModel.find_by_email(username)
        if user and user.confirmado == 1 and safe_str_cmp(user.password, password):
            access_token = create_access_token(identity=user)
            UsuarioModel.update_last_login(user.usuario_id)
            return {'access_token': access_token}, 200

        return {"message": "Usuário ou senha incorretos"}, 401
