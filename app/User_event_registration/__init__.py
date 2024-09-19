from flask import Blueprint
from .ev_reg.controller import user_event_bp

def register_user_event_registration_module(app):
    app.register_blueprint(user_event_bp, url_prefix='/user_event')