import requests
from abc import ABC, abstractmethod

class Parser(ABC):
    """
    Абстрактный класс для создания парсера
    """

    @abstractmethod
    def load_vacancies(self,keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API Headhunter
    родительский класс - Parser
    """

    def __init__(self, keyword):
        self._url = "https://api.hh.ru/vacancies"
        self._headers = {'User-Agent':'HH-User-Agent'}
        self._params = {'text': keyword, 'page':0, 'per_page':50, 'area': 113}
        self.vacancies = []
        super().__init__()


    def load_vacancies(self, *args, **kwargs):
        """
        Функция загрузки вакансии с сайта по ключевыму слову
        фильтрует по региону Россия
        :return:
        """

        response = requests.get(self._url, headers=self._headers, params=self._params)
        response_info = response.json()
        total_pages = response_info['pages']
        while self._params['page'] < total_pages:
            response = requests.get(self._url, headers=self._headers, params=self._params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self._params['page'] += 1
    @property
    def connect(self):
        return requests.get(self._url).status_code

