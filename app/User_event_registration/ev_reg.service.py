from app import db
from app.User_event_registration.ev_reg.entity import UserEventRegistration
import qrcode
from io import BytesIO

class UserEventRegistrationService:
    
    @staticmethod
    def register_user_for_event(user_id, event_id):
        existing_registration = UserEventRegistration.query.filter_by(user_id=user_id, event_id=event_id).first()

        if existing_registration:
            return existing_registration
        
        # Генерация QR-кода для пользователя
        qr_code_data = f'user_{user_id}_event_{event_id}'
        qr_code = qrcode.make(qr_code_data)
        qr_buffer = BytesIO()
        qr_code.save(qr_buffer)
        qr_code_str = qr_buffer.getvalue().hex()  # Сохранение QR-кода в строковом формате
        
        registration = UserEventRegistration(user_id=user_id, event_id=event_id, qr_code=qr_code_str)
        db.session.add(registration)
        db.session.commit()
        return registration

    @staticmethod
    def mark_attendance(user_id, event_id):
        registration = UserEventRegistration.query.filter_by(user_id=user_id, event_id=event_id).first()
        if not registration or registration.attended:
            return None
        
        registration.attended = True
        db.session.commit()
        return registration

    @staticmethod
    def get_user_events(user_id, attended=False):
        return UserEventRegistration.query.filter_by(user_id=user_id, attended=attended).all()

    @staticmethod
    def rate_event(user_id, event_id, rating):
        registration = UserEventRegistration.query.filter_by(user_id=user_id, event_id=event_id).first()
        if not registration or not registration.attended or registration.rated:
            return None
        
        # Допустим, мероприятие имеет поле `rating` для сбора оценок
        registration.rated = True
        db.session.commit()
        return registration