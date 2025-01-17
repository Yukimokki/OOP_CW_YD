import requests
from abc import ABC, abstractmethod

class Parser(ABC):

    @abstractmethod
    def load_vacancies(self,keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API Headhunter
    родительский класс - Parser
    """

    def __init__(self, keyword):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent':'HH-User-Agent'}
        self.params = {'text': keyword, 'page':0, 'per_page':50}
        self.vacancies = []
        super().__init__()


    def load_vacancies(self, *args, **kwargs):
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers = self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

# hh = HH("backend-Python")
# hh.load_vacancies()
# print(hh.vacancies)
