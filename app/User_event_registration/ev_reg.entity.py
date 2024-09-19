from app import db

class UserEventRegistration(db.Model):
    __tablename__ = 'user_event_registrations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    qr_code = db.Column(db.String(255), nullable=True)  # QR-код для мероприятия
    attended = db.Column(db.Boolean, default=False)  # Участвовал ли пользователь
    rated = db.Column(db.Boolean, default=False)  # Оценил ли пользователь мероприятие

    user = db.relationship('User', backref='event_registrations')
    event = db.relationship('Event', backref='user_registrations')