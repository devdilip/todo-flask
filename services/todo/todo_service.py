from sqlalchemy.exc import IntegrityError
from models.todo.todo import Todo
from app import db, app
from models.status.status import Status
from services.status import status_service

from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_active')


@app.before_first_request
def create_tables():
    db.create_all()


def add_todo(id, name, is_active):
    try:
        create_todo = Todo(id=id, name=name, is_active=is_active)
        db.session.add(create_todo)
        db.session.commit()
        return "Todo has been Saved Successfully!"
    except IntegrityError as err:
        db.session.rollback()
        err_msg = err.args[0]

        if "UNIQUE constraint failed: todo.id" in err_msg:
            return "Id should be unique : (%s)" % id
        elif "FOREIGN KEY constraint failed" in err_msg:
            return "supplier does not exist"
        else:
            return "unknown error adding user"


def fetch_todo():
    todos = Todo.query.all()
    todo_schema = TodoSchema(many=True)
    result = todo_schema.dump(todos)
    return result


def fetch_todo_by_id(id):
    todos = Todo.query.filter_by(id=id).first()
    print(todos.id)
    status = status_service.fetch_status_by_todo_id(todos.id)
    print(status)
    todo_schema = TodoSchema()
    result = todo_schema.dump(todos)

    return result


def update_todo(id, name, is_active):
    try:
        todos = Todo.query.filter_by(id=id).first()
        res = not bool(todos)
        if res is not True:
            todos.name = name
            todos.is_active = is_active
            db.session.commit()
            return "Todo has been Updated Successfully!"
        else:
            return "Todo has not found from given id!"
    except IntegrityError as err:
        db.session.rollback()
        err_msg = err.args[0]
        return err_msg


def delete_todo(id):
    try:
        todos = Todo.query.filter_by(id=id).first()
        res = not bool(todos)
        if res is not True:
            db.session.delete(todos)
            db.session.commit()
            return "Todo has been Deleted Successfully!"
        else:
            return "Todo has not found from given id!"
    except IntegrityError as err:
        db.session.rollback()
        err_msg = err.args[0]
        return err_msg
