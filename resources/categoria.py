from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.categoria import CategoriaModel
from werkzeug.security import safe_str_cmp
import datetime

class Categoria(Resource):
    parser = reqparse.RequestParser()

    @jwt_required
    def get(self, categoria_id):
        categoria = CategoriaModel.find_by_id(categoria_id)
        if categoria:
            return categoria.json()
        return {"message": "Categoria não encontrada"}, 404

    @jwt_required
    def post(self):
        Categoria.parser.add_argument("nome",
            type=str,
            required=True,
            help="O campo 'nome' é obrigatório"
        )
        Categoria.parser.add_argument("descricao",
            type=str
        )

        data = Categoria.parser.parse_args()
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        categoria = CategoriaModel(None, data["nome"], data["descricao"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            categoria.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo a categoria."}, 500
        return categoria.json(), 201

    @jwt_required
    def put(self, categoria_id):
        Categoria.parser.add_argument("nome",
            type=str
        )
        Categoria.parser.add_argument("descricao",
            type=str
        )

        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403
        data = Categoria.parser.parse_args()

        categoria = CategoriaModel.find_by_id(categoria_id)
        if categoria is None:
            categoria = CategoriaModel(categoria_id, data["nome"], data["descricao"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        else:
            if(not safe_str_cmp(categoria.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403

            if(data["nome"]):
                categoria.nome = data["nome"]
            if(data["descricao"]):
                categoria.descricao = data["descricao"]

            categoria.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            categoria.atualizado_por = get_jwt_identity()

        categoria.save_to_db()
        return categoria.json()

    @jwt_required
    def delete(self, categoria_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        categoria = CategoriaModel.find_by_id(categoria_id)
        if categoria:
            if(not safe_str_cmp(categoria.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            categoria.ativo = 0
            categoria.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            categoria.atualizado_por = get_jwt_identity()
            categoria.save_to_db()
            return {"mensagem": "Categoria excluída"}
        return {"mensagem": "Id de categoria inexistente"}, 400
