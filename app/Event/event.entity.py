from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Название мероприятия
    format = db.Column(db.String(50), nullable=False)  # Формат мероприятия
    address = db.Column(db.String(255), nullable=False)  # Адрес проведения
    applicant_full_name = db.Column(db.String(100), nullable=False)  # ФИО заявителя
    applicant_phone = db.Column(db.String(20), nullable=False)  # Телефон заявителя
    social_media_link = db.Column(db.String(255), nullable=True)  # Ссылка на анонс в соцсетях
    start_date = db.Column(db.DateTime, nullable=False)  # Дата начала мероприятия
    end_date = db.Column(db.DateTime, nullable=False)  # Дата конца мероприятия
    description = db.Column(db.Text, nullable=False)  # Описание мероприятия

    def __repr__(self):
        return f'<Event {self.name}>'