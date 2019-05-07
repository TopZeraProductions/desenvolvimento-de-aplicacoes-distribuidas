from flask import Blueprint, jsonify, request

from services.coordenadores_dao import CoordenadorServices

coordenadores_app = Blueprint('coordenadores_app', __name__, template_folder='templates')


@coordenadores_app.route('/coordenadores', methods=['GET'])
def listar():
    coo_list = CoordenadorServices.list_all()
    return jsonify(list(map(lambda pr: pr.to_dictionary(), coo_list)))


@coordenadores_app.route('/coordenadores/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    coordenador = CoordenadorServices.find(id)

    return jsonify(coordenador.to_dictionary())


@coordenadores_app.route('/coordenadores', methods=['POST'])
def novo():
    novo_coordenador = request.get_json()

    coo_list = CoordenadorServices.new(novo_coordenador)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), coo_list)))


@coordenadores_app.route('/coordenadores/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = CoordenadorServices.delete(id)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))


@coordenadores_app.route('/coordenadores/<int:id>', methods=['PUT'])
def atualiza(id):
    coordenador_data = request.get_json()
    coordenador_data['id'] = id

    post_list = CoordenadorServices.update(coordenador_data)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))
