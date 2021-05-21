from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    todo_id = Column(Integer, ForeignKey('todo.id'))
    todo = relationship("Todo", backref=backref("todo", uselist=False))
    is_done = db.Column(db.Integer)

    def __init__(self, id, title, todo_id, is_done):
        self.id = id
        self.title = title
        self.todo_id = todo_id
        self.is_done = is_done
