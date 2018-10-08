from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.projeto import ProjetoModel
import datetime

class Projeto(Resource):

    @jwt_required
    def get(self, projeto_id):
        projeto = ProjetoModel.find_by_id(projeto_id)
        if projeto:
            return projeto.json()
        return {"message": "Projeto não encontrado"}, 404

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str,
            required=True,
            help="O campo 'nome' é obrigatório"
        )
        parser.add_argument("cliente_id",
            type=int,
        )
        parser.add_argument("squad_id",
            type=int,
        )

        data = parser.parse_args()
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        if not data["cliente_id"]:
            data["cliente_id"] = None
        if not data["squad_id"]:
            data["squad_id"] = None
        projeto = ProjetoModel(None, data["nome"], data["cliente_id"], data["squad_id"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        print(projeto.cliente_id)
        print(projeto.squad_id)
        try:
            projeto.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o projeto."}, 500
        return projeto.json(), 201

    @jwt_required
    def put(self, projeto_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        parser = reqparse.RequestParser()
        parser.add_argument("nome",
            type=str,
        )
        parser.add_argument("cliente_id",
            type=int,
        )
        parser.add_argument("squad_id",
            type=int,
        )
        data = parser.parse_args()

        projeto = ProjetoModel.find_by_id(projeto_id)
        if projeto is None:
            return {'message': "Usuário Inexistente."}, 400
        else:
            if(not safe_str_cmp(projeto.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            if data["nome"]:
                projeto.nome = data["nome"]
            if data["cliente_id"]:
                projeto.cliente_id = data["cliente_id"]
            if data["squad_id"]:
                projeto.squad_id = data["squad_id"]
            projeto.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            projeto.atualizado_por = get_jwt_identity()

        projeto.save_to_db()
        return projeto.json()

    @jwt_required
    def delete(self, projeto_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        projeto = ProjetoModel.find_by_id(projeto_id)
        if projeto:
            if(not safe_str_cmp(projeto.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            projeto.ativo = 0
            projeto.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            projeto.atualizado_por = get_jwt_identity()
            projeto.save_to_db()
            return {"mensagem": "Projeto excluído"}
        return {"mensagem": "Id de projeto inexistente"}, 400
