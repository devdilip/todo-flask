import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.todo.todo_route import todo_route_page

app = Flask(__name__)
db = SQLAlchemy()
app.register_blueprint(todo_route_page)


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


if __name__ == '__main__':
    application = setup(app, **os.environ)
    application.run(debug=True)
