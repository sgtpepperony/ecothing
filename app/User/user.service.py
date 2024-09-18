from app import db
from .user.entity.py import User

class UserService:
    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, name=None, email=None):
        user = User.query.get(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()