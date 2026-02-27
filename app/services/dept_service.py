from typing import List
from app.models.dept import Department


class DepartmentService:
    _departments: List[Department] = []
    _id_counter = 1

    @classmethod
    def create(cls, name, location):
        department = Department(
            department_id=cls._id_counter, department_name=name, location=location
        )
        cls._departments.append(department)
        cls._id_counter += 1
        return department

    @classmethod
    def get_all(cls):
        return cls._departments
