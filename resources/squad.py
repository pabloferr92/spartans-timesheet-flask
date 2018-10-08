from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.squad import SquadModel
from models.usuario import UsuarioModel
from werkzeug.security import safe_str_cmp
import datetime

class Squad(Resource):

    @jwt_required
    def get(self, squad_id):
        squad = SquadModel.find_by_id(squad_id)
        if squad:
            return squad.json()
        return {"message": "Squad não encontrado"}, 404

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str,
            required=True,
            help="O campo 'nome' é obrigatório"
        )
        parser.add_argument("administrador_id",
            type=int,
            required=True,
            help="O campo 'administrador_id' é obrigatório"
        )

        data = parser.parse_args()
        squad = SquadModel(None, data["nome"], data["administrador_id"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            squad.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o squad."}, 500
        return squad.json(), 201

    @jwt_required
    def put(self, squad_id):
        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str
        )
        parser.add_argument("administrador_id",
            type=int
        )
        data = parser.parse_args()

        squad = SquadModel.find_by_id(squad_id)
        if squad is None:
            return {'message': "Squad Inexistente."}, 400
        else:
            administrador = UsuarioModel.find_by_id(squad.administrador_id)
            if not administrador:
                return {'message': "Administrador não encontrado."}, 400

            if(not safe_str_cmp(administrador.email, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403

            if(data["nome"]):
                squad.nome = data["nome"]
            if(data["administrador_id"]):
                squad.administrador_id = data["administrador_id"]

            squad.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            squad.atualizado_por = get_jwt_identity()

            squad.save_to_db()
            return squad.json()

    @jwt_required
    def delete(self, squad_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        squad = SquadModel.find_by_id(squad_id)
        if squad:
            administrador = UsuarioModel.find_by_id(squad.administrador_id)
            if not administrador:
                return {'message': "Administrador não encontrado."}, 400

            if(not safe_str_cmp(administrador.email, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            squad.ativo = 0
            squad.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            squad.atualizado_por = get_jwt_identity()
            squad.save_to_db()
            return {"mensagem": "Squad excluído"}
        return {"mensagem": "Id de squad inexistente"}, 400
