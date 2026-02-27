from dataclasses import dataclass


@dataclass
class Department:
    department_id: int
    department_name: str
    location: str
