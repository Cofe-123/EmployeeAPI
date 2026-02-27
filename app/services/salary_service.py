from typing import List
from app.models.salary import Salary


class SalaryService:
    _salaries: List[Salary] = []
    _id_counter = 1

    @classmethod
    def create(cls, employee_id, basic, bonus, allowances):
        salary = Salary(
            salary_id=cls._id_counter,
            employee_id=employee_id,
            basic_salary=basic,
            bonus=bonus,
            allowances=allowances,
        )
        cls._salaries.append(salary)
        cls._id_counter += 1
        return salary

    @classmethod
    def get_all(cls):
        return cls._salaries
