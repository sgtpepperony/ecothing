from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создаем объект SQLAlchemy для работы с БД
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Конфигурация приложения
    app.config.from_object('config.Config')
    
    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Регистрация контроллеров (BluePrints)
    from app.controllers import main_bp
    app.register_blueprint(main_bp)
    
    return app