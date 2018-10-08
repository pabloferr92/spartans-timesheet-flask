from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.perfil import PerfilModel
from werkzeug.security import safe_str_cmp
import datetime

class Perfil(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("nome",
        type=str,
        required=True,
        help="O campo 'nome' é obrigatório"
    )

    @jwt_required
    def get(self, perfil_id):
        perfil = PerfilModel.find_by_id(perfil_id)
        if perfil:
            return perfil.json()
        return {"message": "Perfil não encontrado"}, 404

    @jwt_required
    def post(self):
        data = Perfil.parser.parse_args()
        if PerfilModel.find_by_name(data["nome"]):
            return {'message': "Um perfil com o nome '{}' já existe.".format(data["nome"])}, 400
        if(get_jwt_claims()["perfil_id"] != 1):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        perfil = PerfilModel(None, data["nome"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            perfil.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o perfil."}, 500
        return perfil.json(), 201

    @jwt_required
    def put(self, perfil_id):
        if(get_jwt_claims()["perfil_id"] != 1):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403
        data = Perfil.parser.parse_args()

        perfil = PerfilModel.find_by_id(perfil_id)
        if perfil is None:
            perfil = PerfilModel(perfil_id, data["nome"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        else:
            perfil.nome = data["nome"]
            perfil.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            perfil.atualizado_por = get_jwt_identity()

        perfil.save_to_db()
        return perfil.json()

    @jwt_required
    def delete(self, perfil_id):
        if(get_jwt_claims()["perfil_id"] != 1 or perfil_id == 1):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        perfil = PerfilModel.find_by_id(perfil_id)
        if perfil:
            perfil.ativo = 0
            perfil.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            perfil.atualizado_por = get_jwt_identity()
            perfil.save_to_db()
            return {"mensagem": "Perfil excluído"}

        return {"mensagem": "Id de perfil inexistente"}, 400
