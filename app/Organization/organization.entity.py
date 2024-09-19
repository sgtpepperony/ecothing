from app import db
from datetime import datetime

class Organizer(db.Model):
    __tablename__ = 'organizers'

    id = db.Column(db.Integer, primary_key=True)
    is_legal_entity = db.Column(db.Boolean, nullable=False)  # Юридическое лицо или физическое
    organization_name = db.Column(db.String(150), nullable=True)  # Наименование организации (если юр. лицо)
    inn = db.Column(db.String(12), nullable=True)  # ИНН организации
    website = db.Column(db.String(255), nullable=True)  # Сайт (если юр. лицо)
    contact_phone = db.Column(db.String(20), nullable=False)  # Контактный телефон
    
    # Для физического лица
    full_name = db.Column(db.String(150), nullable=True)  # ФИО физического лица
    email = db.Column(db.String(120), nullable=True)  # Эл. почта физического лица
    social_link = db.Column(db.String(255), nullable=True)  # Соц. сеть (физическое лицо)
    
    # Статистика мероприятий
    total_registered = db.Column(db.Integer, default=0)  # Количество зарегистрированных пользователей
    total_visited = db.Column(db.Integer, default=0)  # Количество посетивших (отсканировавших QR-код)

    # Согласие на обработку данных
    data_processing_consent = db.Column(db.Boolean, nullable=False)  # Согласие на обработку данных

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        if self.is_legal_entity:
            return f'<Organizer {self.organization_name}>'
        return f'<Organizer {self.full_name}>'