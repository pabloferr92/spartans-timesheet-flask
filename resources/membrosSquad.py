from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.membrosSquad import MembrosSquadModel
from models.squad import SquadModel
from models.usuario import UsuarioModel
from werkzeug.security import safe_str_cmp
import datetime

class MembrosSquad(Resource):

    @jwt_required
    def get(self, membros_squad_id):
        membros_squad = MembrosSquadModel.find_by_id(membros_squad_id)
        if membros_squad:
            return membros_squad.json()
        return {"message": "Memebro do Squad não encontrado"}, 404

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("squad_id",
            type=int,
            required=True,
            help="O campo 'squad_id' é obrigatório"
        )
        parser.add_argument("usuario_id",
            type=int,
            required=True,
            help="O campo 'usuario_id' é obrigatório"
        )

        data = parser.parse_args()
        membros_squad = MembrosSquadModel(None, data["squad_id"], data["usuario_id"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            membros_squad.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o squad."}, 500
        return membros_squad.json(), 201

    @jwt_required
    def delete(self, membros_squad_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        membros_squad = MembrosSquadModel.find_by_id(membros_squad_id)
        if not membros_squad:
            return {"mensagem": "Id de membro do squad inexistente"}, 400

        squad = SquadModel.find_by_id(membros_squad.squad_id)
        if not squad:
            return {"mensagem": "Id de squad inexistente"}, 400

        administrador = UsuarioModel.find_by_id(squad.administrador_id)
        if not administrador:
            return {'message': "Administrador não encontrado."}, 400

        if(not safe_str_cmp(administrador.email, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        membros_squad.ativo = 0
        membros_squad.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        membros_squad.atualizado_por = get_jwt_identity()
        membros_squad.save_to_db()
        return {"mensagem": "Membro do Squad excluído"}
