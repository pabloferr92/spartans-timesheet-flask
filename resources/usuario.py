from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.usuario import UsuarioModel
from werkzeug.security import safe_str_cmp
import datetime

class Usuario(Resource):

    @jwt_required
    def get(self, usuario_id):
        usuario = UsuarioModel.find_by_id(usuario_id)
        if usuario:
            return usuario.json()
        return {"message": "Usuário não encontrado"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str,
            required=True,
            help="O campo 'nome' é obrigatório"
        )
        parser.add_argument("telefone",
            type=str
        )
        parser.add_argument("email",
            type=str,
            required=True,
            help="O campo 'email' é obrigatório"
        )
        parser.add_argument("password",
            type=str,
            required=True,
            help="O campo 'password' é obrigatório"
        )
        parser.add_argument("perfil_id",
            type=int,
            required=True,
            help="O campo 'perfil_id' é obrigatório"
        )
        parser.add_argument("valor_hora",
            type=float
        )
        parser.add_argument("timezone",
            type=str,
            required=True,
            help="O campo 'timezone' é obrigatório"
        )

        data = parser.parse_args()
        if UsuarioModel.find_by_email(data["email"]):
            return {'message': "Um usuário com o email '{}' já existe.".format(data["email"])}, 400

        usuario = UsuarioModel(None, data["nome"], data["telefone"], data["email"], data["password"], data["perfil_id"], data["valor_hora"], data["timezone"], None, 0, data["email"], datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), data["email"], datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            usuario.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o usuario."}, 500
        return usuario.json(), 201

    @jwt_required
    def put(self, usuario_id):
        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str
        )
        parser.add_argument("telefone",
            type=str
        )
        parser.add_argument("email",
            type=str
        )
        parser.add_argument("password",
            type=str
        )
        parser.add_argument("perfil_id",
            type=int
        )
        parser.add_argument("valor_hora",
            type=float
        )
        parser.add_argument("timezone",
            type=str
        )
        data = parser.parse_args()

        usuario = UsuarioModel.find_by_id(usuario_id)
        if usuario is None:
            return {'message': "Usuário Inexistente."}, 400
        else:
            if(not safe_str_cmp(usuario.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403

            if(data["nome"]):
                usuario.nome = data["nome"]
            if(data["telefone"]):
                usuario.telefone = data["telefone"]
            if(data["email"]):
                usuario.email = data["email"]
            if(data["password"]):
                usuario.password = data["password"]
            if(data["perfil_id"]):
                usuario.perfil_id = data["perfil_id"]
            if(data["valor_hora"]):
                usuario.valor_hora = data["valor_hora"]
            if(data["timezone"]):
                usuario.timezone = data["timezone"]

            usuario.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            usuario.atualizado_por = get_jwt_identity()

            usuario.save_to_db()
            return usuario.json()
