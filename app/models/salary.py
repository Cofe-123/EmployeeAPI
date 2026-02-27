from dataclasses import dataclass


@dataclass
class Salary:
    salary_id: int
    employee_id: int
    basic_salary: float
    bonus: float
    allowances: float
