from flask import Flask
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'ecothing')))
from app.User_event_registration._init_ import register_user_event_registration_module
from app.Event._init_ import register_event_module
from app.User._init_ import register_user_module
from app.Organization._init_ import register_organizer_module
from app.Depth._init_ import register_department_employee_module

def create_app():
    app = Flask(__name__)
    # Подключение модулей
    register_user_event_registration_module(app)
    register_event_module(app)
    register_user_module(app)
    register_organizer_module(app)
    register_department_employee_module(app)
    
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)