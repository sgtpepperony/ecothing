from app.d.controller import department_employee_blueprint

def register_department_employee_module(app):
    app.register_blueprint(department_employee_blueprint, url_prefix='/department_employee')