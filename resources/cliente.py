from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.cliente import ClienteModel
from werkzeug.security import safe_str_cmp
import datetime

class Cliente(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("nome",
        type=str,
        required=True,
        help="O campo 'nome' é obrigatório"
    )

    @jwt_required
    def get(self, cliente_id):
        cliente = ClienteModel.find_by_id(cliente_id)
        if cliente:
            return cliente.json()
        return {"message": "Cliente não encontrado"}, 404

    @jwt_required
    def post(self):
        data = Cliente.parser.parse_args()
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        cliente = ClienteModel(None, data["nome"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            cliente.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o cliente."}, 500
        return cliente.json(), 201

    @jwt_required
    def put(self, cliente_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403
        data = Cliente.parser.parse_args()

        cliente = ClienteModel.find_by_id(cliente_id)
        if cliente is None:
            cliente = ClienteModel(cliente_id, data["nome"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        else:
            if(not safe_str_cmp(cliente.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            cliente.nome = data["nome"]
            cliente.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            cliente.atualizado_por = get_jwt_identity()

        cliente.save_to_db()
        return cliente.json()

    @jwt_required
    def delete(self, cliente_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        cliente = ClienteModel.find_by_id(cliente_id)
        if cliente:
            if(not safe_str_cmp(cliente.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            cliente.ativo = 0
            cliente.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            cliente.atualizado_por = get_jwt_identity()
            cliente.save_to_db()
            return {"mensagem": "Cliente excluído"}
        return {"mensagem": "Id de cliente inexistente"}, 400
