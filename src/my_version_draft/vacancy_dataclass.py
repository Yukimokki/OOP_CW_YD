from dataclasses import dataclass, field, astuple, asdict
import inspect
from pprint import pprint


@dataclass
class Vacancy:
    name: str
    url: str
    area: str
    experience: str
    salary_currency: str = "RUR"
    salary_from: int | None = None
    salary_to: int | None = None
    rate: float = 1.0
    #rate: float = field(init = False, repr = False)
    salary_from_converted: float = field(init = False, repr = False)
    salary_to_converted: float = field(init = False, repr = False)


    def __post_init__(self):
        self._validate_salary(self.salary_from)
        self._validate_salary(self.salary_to)
        self.salary_from_converted = self.salary_from * self.rate
        self.salary_to_converted = self.salary_to * self.rate


    @staticmethod
    def _validate_salary(salary: int | None) -> None:
        if salary is not None and salary < 0:
            raise ValueError("Salary cannot be negative")

    def __lt__(self, other: 'Vacancy') -> bool:
        if self.salary_from and other.salary_from:
            return self.salary_from < other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to < other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary < other_salary

    def __eq__(self, other: 'Vacancy') -> bool:
        eq_from = self.salary_from == other.salary_from
        eq_to = self.salary_to == other.salary_to
        return eq_from and eq_to

#pprint(inspect.getmembers(Vacancy, inspect.isfunction))
Vac = Vacancy('Java', 'http://xxxxx.com', 'USA', 'None', 'USD', 10000, 12000, 89.24,)
print(Vac.salary_from_converted, Vac.salary_to_converted)