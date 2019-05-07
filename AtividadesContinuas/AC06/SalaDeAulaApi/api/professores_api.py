from flask import Blueprint, jsonify, request

from services.professores_dao import ProfessorServices

professores_app = Blueprint('professores_app', __name__, template_folder='templates')


@professores_app.route('/professores', methods=['GET'])
def listar():
    pr_list = ProfessorServices.list_all()
    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@professores_app.route('/professores/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    professor = ProfessorServices.find(id)

    return jsonify(professor.to_dictionary())


@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()

    pr_list = ProfessorServices.new(novo_professor)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = ProfessorServices.delete(id)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))


@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualiza(id):
    professor_data = request.get_json()
    professor_data['id'] = id

    post_list = ProfessorServices.update(professor_data)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))
