from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class Note(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     data = db.Column(db.String(10000))
#     ##func.now() stores the current time
#     date = db.Column(db.DateTime(timezone=True),default = func.now())
#     ##creating a foreign key for one-to-many relationship. i.e one user having many notes
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


class User(db.Model,UserMixin):
    #__tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')