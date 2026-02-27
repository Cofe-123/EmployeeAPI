from typing import List
from app.models.emp import Employee


class EmployeeService:
    _employees: List[Employee] = []
    _id_counter = 1

    @classmethod
    def create(cls, first_name, last_name, gender, dob, department_id):
        employee = Employee(
            id=cls._id_counter,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=dob,
            department_id=department_id,
        )
        cls._employees.append(employee)
        cls._id_counter += 1
        return employee

    @classmethod
    def get_all(cls):
        return cls._employees

    @classmethod
    def get_by_id(cls, emp_id):
        return next((e for e in cls._employees if e.id == emp_id), None)

    @classmethod
    def update(cls, emp_id, data):
        emp = cls.get_by_id(emp_id)
        if not emp:
            return None

        for key, value in data.items():
            if hasattr(emp, key):
                setattr(emp, key, value)

        return emp

    @classmethod
    def delete(cls, emp_id):
        emp = cls.get_by_id(emp_id)
        if not emp:
            return False

        cls._employees.remove(emp)
        return True
