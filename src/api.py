from abc import ABC, abstractmethod
import requests, json

class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, vac_qty):
        pass

class HHApi(BaseAPI):
    """Класс для осуществления подключения к API службе внешнего источника данных согласно заданных параметров"""
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': '',
            'page': 0,
            'per_page': 100
        }

    def get_vacancies(self, keyword, vac_qty) -> dict:
        """Метод для загрузки данных согласно сутруктуры запроса"""
        self.params.update({'text': keyword, 'per_page': vac_qty})
        response = requests.get(self.url, params=self.params)
        return response.json()['items']


hh_api = HHApi()
"""Вызов экземпляра класса"""
