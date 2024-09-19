from flask import Blueprint, request, jsonify
from app.Depth import DepartmentEmployeeService

department_employee_blueprint = Blueprint('department_employee', __name__)

@department_employee_blueprint.route('/register', methods=['POST'])
def register_employee():
    data = request.json
    try:
        employee = DepartmentEmployeeService.create_employee(data)
        return jsonify({'message': 'Сотрудник зарегистрирован', 'employee': {
            'email': employee.email,
            'name': employee.name,
            'surname': employee.surname,
            'patronymic': employee.patronymic
        }}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@department_employee_blueprint.route('/export', methods=['GET'])
def export_data():
    filters = request.args.to_dict()
    data = DepartmentEmployeeService.export_data(filters)
    return jsonify({'data': [str(record) for record in data]})