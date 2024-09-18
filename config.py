from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Строка подключения к удалённой базе данных PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://MargoRita:password@<10.10.103.0>:5432/your_database'

db = SQLAlchemy(app)