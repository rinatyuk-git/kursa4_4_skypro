import json
import os
from abc import ABC, abstractmethod

from config import DATA_PATH


class BaseWorker(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass

    @abstractmethod
    def see_vacancy(self, keyword):
        pass


class JSONWorker(BaseWorker):
    """Класс для создания/построения локального хранилища"""
    def __init__(self, file_name):
        self.path_file = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        """Метод для создания файла на локальном хранилище"""
        with open(self.path_file, 'w', encoding='utf-8') as file:
            json.dump([], file)

    def __read_json(self):
        """Чтение JSON-файла"""
        with open(self.path_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def __write_json(self, data):
        """Запись данных в JSON-файл"""
        with open(self.path_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл на локальном хранилище"""
        data = self.__read_json()
        data.append(vacancy.to_dict())
        self.__write_json(data)

    def read(self):
        """Метод для чтения файла на локальном хранилище"""
        return self.__read_json()

    def add_vacancies(self, vacancies):
        """Метод для добавления списка вакансий в файл на локальном хранилище"""
        data = self.__read_json()
        data.extend([vacancy.to_dict() for vacancy in vacancies])
        self.__write_json(data)

    def del_vacancy(self, vacancy):
        """Метод для удаления вакансии в файл на локальном хранилище"""
        data = self.__read_json()
        data = [line for line in data if line != vacancy.to_dict()]
        self.__write_json(data)

    def see_vacancy(self, filter_word):
        """Метод для просмотра вакансии в файле на локальном хранилище"""
        data = self.__read_json()
        result = []
        for line in data:
            if filter_word and set(line.values()) & set(filter_word):
                result.append(line)
        return result


my_json = JSONWorker('vacancies.json')
"""Вызов экземпляра класса"""
