from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Surname = db.Column(db.String(50), nullable=False)
    Patronymic = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    district = db.Column(db.String(50), nullable=False)
    roleid = db.Column(db.Integer, nullable=False)  # Здесь не должно быть primary_key
    Town = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)  # Храните хэш, а не сам пароль

    def __repr__(self):
        return f'<User {self.Name}>'