from app import db
from app.Depth import DepartmentEmployee
from app.Event import Event
from app.User import User
from app.Organization import Organization

class DepartmentEmployeeService:
    @staticmethod
    def create_employee(data):
        # Проверяем, существует ли сотрудник с таким СНИЛС
        snils = data.get('snils')
        if DepartmentEmployeeService.verify_snils(snils):
            employee = DepartmentEmployee(
                email=data['email'],
                name=data['name'],
                surname=data['surname'],
                patronymic=data.get('patronymic'),
                snils=snils,
                is_verified=True
            )
            db.session.add(employee)
            db.session.commit()
            return employee
        else:
            raise ValueError('Сотрудник не найден по СНИЛС')

    @staticmethod
    def verify_snils(snils):
        # Здесь логика проверки СНИЛС через внешнюю систему
        # Предположим, что возвращается True если сотрудник найден
        return True

    @staticmethod
    def export_data(filters):
        query = db.session.query(Event, Organization, User)

        # Применяем фильтры
        if filters.get('gender'):
            query = query.filter(User.gender == filters['gender'])
        if filters.get('age'):
            query = query.filter(User.age == filters['age'])
        if filters.get('organizer_type'):
            query = query.filter(Organization.is_legal_entity == filters['organizer_type'])

        # Выгружаем данные
        return query.all()