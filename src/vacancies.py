class JobVacancy:
    def __init__(self, name: str, salary: dict, url: str, requirement: str, area: str):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.name = name
        self.salary = salary
        self.url = url
        self.requirement = requirement
        self.area = area

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
            f"Регион: {self.area}\n"
        )

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.url}, {self.requirement}, {self.area})"

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']