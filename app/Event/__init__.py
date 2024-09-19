from flask import Blueprint
from app.Event.event.controller import event_bp

def register_event_module(app):
    app.register_blueprint(event_bp, url_prefix='/api')