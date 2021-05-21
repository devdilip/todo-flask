from app import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    is_active = db.Column(db.Integer)

    def __init__(self, id, name, is_active):
        self.id = id
        self.name = name
        self.is_active = is_active


