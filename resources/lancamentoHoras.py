from flask_restful import Resource, reqparse, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from models.lancamentoHoras import LancamentoHorasModel
from werkzeug.security import safe_str_cmp
import datetime

class LancamentoHoras(Resource):

    @jwt_required
    def get(self, lancamento_horas_id):
        lancamento_horas = LancamentoHorasModel.find_by_id(lancamento_horas_id)
        if lancamento_horas:
            return lancamento_horas.json()
        return {"message": "Lançamento de horas não encontrado"}, 404

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("projeto_id",
            type=int
        )
        parser.add_argument("cliente_id",
            type=int
        )
        parser.add_argument("usuario_id",
            type=int
        )
        parser.add_argument("categoria_id",
            type=int
        )
        parser.add_argument("data_inicio",
            type=str,
            required=True,
            help="O campo 'data_inicio' é obrigatório"
        )
        parser.add_argument("data_fim",
            type=str
        )
        parser.add_argument("descricao",
            type=str
        )

        data = parser.parse_args()
        lancamento_horas = LancamentoHorasModel(None, data["projeto_id"], data["cliente_id"], data["usuario_id"], data["categoria_id"], data["data_inicio"], data["data_fim"], data["descricao"], get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), get_jwt_identity(), datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), 1)
        try:
            lancamento_horas.save_to_db()
        except:
            return {"mensagem": "Um erro ocorreu inserindo o lançamento de horas."}, 500
        return lancamento_horas.json(), 201

    @jwt_required
    def put(self, lancamento_horas_id):
        parser = reqparse.RequestParser()
        parser.add_argument("projeto_id",
            type=int
        )
        parser.add_argument("cliente_id",
            type=int
        )
        parser.add_argument("usuario_id",
            type=int
        )
        parser.add_argument("categoria_id",
            type=int
        )
        parser.add_argument("data_inicio",
            type=str,
        )
        parser.add_argument("data_fim",
            type=str
        )
        parser.add_argument("descricao",
            type=str
        )
        data = parser.parse_args()

        lancamento_horas = LancamentoHorasModel.find_by_id(lancamento_horas_id)
        if lancamento_horas is None:
            return {'message': "Lançamento de Horas Inexistente."}, 400
        else:
            if(not safe_str_cmp(lancamento_horas.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403

            if(data["projeto_id"]):
                lancamento_horas.projeto_id = data["projeto_id"]
            if(data["cliente_id"]):
                lancamento_horas.cliente_id = data["cliente_id"]
            if(data["usuario_id"]):
                lancamento_horas.usuario_id = data["usuario_id"]
            if(data["categoria_id"]):
                lancamento_horas.categoria_id = data["categoria_id"]
            if(data["data_inicio"]):
                lancamento_horas.data_inicio = data["data_inicio"]
            if(data["data_fim"]):
                lancamento_horas.data_fim = data["data_fim"]
            if(data["descricao"]):
                lancamento_horas.descricao = data["descricao"]

            lancamento_horas.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            lancamento_horas.atualizado_por = get_jwt_identity()

            lancamento_horas.save_to_db()
            return lancamento_horas.json()

    @jwt_required
    def delete(self, lancamento_horas_id):
        if(get_jwt_claims()["perfil_id"] != 1 and get_jwt_claims()["perfil_id"] != 2):
            return {'message': "Você não tem permissão para fazer essa ação."}, 403

        lancamento_horas = LancamentoHorasModel.find_by_id(lancamento_horas_id)
        if lancamento_horas:
            if(not safe_str_cmp(lancamento_horas.criado_por, get_jwt_identity()) and get_jwt_claims()["perfil_id"] != 1):
                return {'message': "Você não tem permissão para fazer essa ação."}, 403
            lancamento_horas.ativo = 0
            lancamento_horas.data_ultima_atualizacao = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            lancamento_horas.atualizado_por = get_jwt_identity()
            lancamento_horas.save_to_db()
            return {"mensagem": "Lançamento de Horas excluído"}
        return {"mensagem": "Id de Lançamento de Horas inexistente"}, 400
