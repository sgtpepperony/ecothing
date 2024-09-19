from flask import Flask
from app.Organization import organizer_bp

def register_organizer_module(app: Flask):
    app.register_blueprint(organizer_bp, url_prefix='/api')