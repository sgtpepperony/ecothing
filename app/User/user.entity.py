from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Surname = db.Column(db.String(50), nullable=False)
    Patronymic = db.Column(db.String(50), nullable=False) # отчетство
    email = db.Column(db.String(120), unique=True, nullable=False)
    district = db.Column(db.String(50), nullable=False)
    roleid = db.Column(db.Integer, primary_key=True)
    Town = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'