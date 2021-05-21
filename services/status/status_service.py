from sqlalchemy.exc import IntegrityError
from models.status.status import Status
from app import db, app

from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'todo_id', 'is_done')


@app.before_first_request
def create_tables():
    db.create_all()


def fetch_status_by_todo_id(todo_id):
    status = Status.query.filter_by(todo_id=todo_id).all()
    print(status)
    todo_schema = StatusSchema(many=True)
    result = todo_schema.dump(status)
    return result

