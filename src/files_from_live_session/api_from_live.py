from abc import ABC, abstractmethod
import requests

class BaseVacanciesAPI(ABC):

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[dict]:
        ...


class HHVacanciesAPI(BaseVacanciesAPI):

    def get_vacancies(self, search_text: str) -> list[dict]:
        url = "https://api.hh.ru/vacancies"
        params = {
            'text': search_text,
            'only_with_salary': True,
            'page': 0,
            'per_page': 10
        }


        items = []
        while True:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            items.extend(data['items'])
            params['page'] += 1

            if params['page'] == 5:
                break

            if data['found'] == 0:
                break

            if data['found'] == 0:
                break

        return data['items']


