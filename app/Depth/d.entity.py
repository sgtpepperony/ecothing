from app import db

class DepartmentEmployee(db.Model):
    __tablename__ = 'department_employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)  # Отчество может быть пустым
    snils = db.Column(db.String(14), unique=True, nullable=False)  # СНИЛС в формате "XXX-XXX-XXX-XX"
    is_verified = db.Column(db.Boolean, default=False)  # Признак верификации сотрудника

    def __repr__(self):
        return f'<DepartmentEmployee {self.surname} {self.name}>'