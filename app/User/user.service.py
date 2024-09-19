from app import db
from app.User import User
from app.Event import Event  # Предполагается, что Event уже реализован
from app.User_event_registration import UserEventRegistration  # Связующая таблица для регистрации на события

class UserService:
    @staticmethod
    def register_user(data):
        """Регистрация нового пользователя"""
        new_user = User(
            Name=data['name'],
            Surname=data['surname'],
            Patronymic=data['patronymic'],
            email=data['email'],
            district=data['district'],
            roleid=data['roleid'],
            Town=data['town'],
            Password=data['password']  # Здесь нужно использовать хэширование паролей!
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        """Получение информации о пользователе по его id"""
        return User.query.get(user_id)

    @staticmethod
    def register_for_event(user_id, event_id):
        """Регистрация пользователя на мероприятие"""
        user = User.query.get(user_id)
        event = Event.query.get(event_id)
        if user and event:
            registration = UserEventRegistration(user_id=user.id, event_id=event.id)
            db.session.add(registration)
            db.session.commit()
            return registration
        return None

    @staticmethod
    def get_user_events(user_id):
        """Получение списка мероприятий, на которые зарегистрирован пользователь"""
        return UserEventRegistration.query.filter_by(user_id=user_id).all()

    @staticmethod
    def award_points(user_id, event_id, points):
        """Начисление баллов после мероприятия"""
        # Логика начисления баллов пользователю после успешного сканирования QR-кода
        # Здесь можно добавить проверку посещения мероприятия
        user = User.query.get(user_id)
        if user:
            user.points += points  # Предполагается, что у пользователя есть поле "points"
            db.session.commit()
            return user.points
        return None