class JobVacancy:
    def __init__(self, name: str, id: str, salary: dict, url: str, requirement: str, area: dict, experience: dict):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.name = name
        self.id = id
        self.salary = salary
        self.url = url
        self.requirement = requirement
        self.area = area
        self.experience = experience['name']
        self.currency = salary['currency']

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Регион: {self.area['name']}\n"
            f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
            f"Опыт: {self.experience['name']}\n"
        )

    def currency(self):
        return (
            f"Валюта : {self.salary['currency']}\n"
            f"ID : {self.id}\n"
            )

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.url}, {self.requirement},{self.experience})"

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']


