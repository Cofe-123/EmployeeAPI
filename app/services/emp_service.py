from typing import List
from app.models.emp import Employee


class EmployeeService:
    _employees: List[Employee] = []
    _id_counter = 1

    @classmethod
    def create(cls, first_name, last_name, gender, dob, department_id):
        employee = Employee(
            employee_id=cls._id_counter,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=dob,
            department_id=department_id
        )
        cls._employees.append(employee)
        cls._id_counter += 1
        return employee

    @classmethod
    def get_all(cls):
        return cls._employees