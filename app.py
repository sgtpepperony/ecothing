from flask import Flask
import sys
import os

# Включаем папку 'ecothing' в пути для поиска модулей
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Импортируем модули
from app.User_event_registration import register_user_event_registration_module
from app.Event import register_event_module
from app.User import register_user_module
from app.Organization import register_organizer_module
from app.Depth import register_department_employee_module
from app import db

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


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Настройка подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Определение модели для таблицы users
class User(db.Model):
    __tablename__ = 'users'
    
    userID = db.Column(db.BigInteger, primary_key=True)
    userFirstName = db.Column(db.String)
    userSecondName = db.Column(db.String)
    userSurName = db.Column(db.String)
    roleID = db.Column(db.Integer)
    email = db.Column(db.String(255))
    Town = db.Column(db.String)
    District = db.Column(db.String)

# Определение модели для таблицы DepartmentMembers
class DepartmentMembers(db.Model):
    __tablename__ = 'DepartmentMemebers'
    
    DepartmentMemberID = db.Column(db.BigInteger, primary_key=True)
    userID = db.Column(db.BigInteger)

# Определение модели для таблицы EventOrganizers
class EventOrganizer(db.Model):
    __tablename__ = 'EventOrganizers'
    
    organizerID = db.Column(db.BigInteger, primary_key=True)
    userID = db.Column(db.BigInteger)

# Определение модели для таблицы Events
class Event(db.Model):
    __tablename__ = 'Events'
    
    eventID = db.Column(db.BigInteger, primary_key=True)
    Rate = db.Column(db.ARRAY(db.Numeric))
    Category = db.Column(db.String)
    StartDate = db.Column(db.Date)
    FinalDate = db.Column(db.Date)
    organizerID = db.Column(db.BigInteger)

# Определение модели для таблицы PersonOnEvent
class PersonOnEvent(db.Model):
    __tablename__ = 'PersonOnEvent'
    
    eventID = db.Column(db.BigInteger, nullable=False)
    userID = db.Column(db.BigInteger, nullable=False)
    
    __table_args__ = (
        db.PrimaryKeyConstraint('eventID', 'userID'),
    )



@app.route('/')
def index():
    return "Welcome to the Events API"

if __name__ == '__main__':
    app.run(debug=True)

db.create_all()

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = User(userFirstName='Иван', userSecondName='Иванов', userSurName='Иванович', roleID=1, email='ivan@example.com')
    db.session.add(new_user)
    db.session.commit()
    return "User added"
