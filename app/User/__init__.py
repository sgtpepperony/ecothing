from flask import Blueprint
from app.User import user_controller

def register_user_module(app):
    """Регистрация контроллера пользователя"""
    app.register_blueprint(user_controller, url_prefix='/api/user')