# import requests module
import requests
from abc import ABC, abstractmethod
class Currency(ABC):
    @abstractmethod
    def load_currencies(self):
        pass

class Central_bank(Currency):
    """
    класс для получения словаря с курсами валют
    """
    def __init__(self):
        self.url = 'https://www.cbr-xml-daily.ru/latest.js'
        self.currencies = []
        super().__init__()

    def load_currencies(self, *args):
        response = requests.get(self.url)
        self.currencies = response.json()['rates']
        #print(response.headers)

Cur = Central_bank()
Cur.load_currencies()
print(Cur.currencies)