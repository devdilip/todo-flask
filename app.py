import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from services.todo import todo_service

app = Flask(__name__)
db = SQLAlchemy()

from routes.todo import todo_route


def setup(app, **kwargs):
    # Setup extensions
    db_name = 'todo.sqlite'
    app.secret_key = "5223"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


@app.route('/')
def health():
    return 'Fine!'


@app.route('/test_db')
def test_db_connection():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

app.add_url_rule("/todos", "Fetch all todos", todo_route.get_todos, methods=['GET'])
app.add_url_rule("/todo/<id>", "Get, Update and Delete specific todo", todo_route.todo_by_id, methods=['GET', 'DELETE', 'PUT'])
app.add_url_rule("/todo", "Add new todo", todo_route.add_todo, methods=['POST'])


if __name__ == '__main__':
    application = setup(app, **os.environ)
    application.run(debug=True)
