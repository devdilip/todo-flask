from flask import request, jsonify, Blueprint

todo_route_page = Blueprint('todo_route_page', __name__, template_folder='todo_templates')
from services.todo import todo_service


@todo_route_page.route("/todos", methods=["GET"])
def get_todos():
    todos = todo_service.fetch_todo()
    print(todos)
    return jsonify(todos)


@todo_route_page.route('/todo', methods=["POST"])
def add_todo():
    json_data = request.json
    id = json_data["id"]
    name = json_data["name"]
    is_active = json_data["isActive"]
    todo = todo_service.add_todo(id, name, is_active)
    return todo


@todo_route_page.route("/todo/<id>", methods=['GET', 'PUT', 'DELETE'])
def todo_by_id(id):
    if request.method == 'GET':
        return get_todo_by_id(id)
    elif request.method == 'DELETE':
        return delete_todo_by_id(id)
    elif request.method == 'PUT':
        return update_todo(id)


def get_todo_by_id(id):
    todos = todo_service.fetch_todo_by_id(id)
    return jsonify(todos)


def delete_todo_by_id(id):
    todos = todo_service.delete_todo(id)
    return jsonify(todos)


def update_todo(id):
    json_data = request.json
    name = json_data["name"]
    is_active = json_data["isActive"]
    todo = todo_service.update_todo(id, name, is_active)
    return todo
