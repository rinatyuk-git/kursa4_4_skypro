from src.api import HHApi, hh_api
from src.vacancy import Vacancy
from src.worker import JSONWorker, my_json
from pick import pick


class UserInteraction:
    """Класс для создания пользовательских функций"""
    def __init__(self, hh_api: HHApi, worker: JSONWorker, vac_model):
        self.vac_model = vac_model
        self.hh_api = hh_api
        self.worker = worker
        self.temp_result = []

    def get_vacancy(self):
        """Метод для загрузки данных в локальное хранилище"""
        self.worker.prepare()
        query = input("Введите поисковый запрос: \n")
        vac_qty = self.check_values('Введите количество вакансий, не больше 100:')
        vacancies_info = self.hh_api.get_vacancies(query, vac_qty)
        vacancies = self.vac_model.create_vacancies(vacancies_info)
        self.worker.add_vacancies(vacancies)
        self.check_temp_result()
        self.print_result()

    def check_temp_result(self):
        """Метод для проверки/загрузки данных из хранилища в память"""
        vacancies = self.worker.read()
        self.temp_result = [self.vac_model(**vacancies_data) for vacancies_data in vacancies]

    def get_filtered_vacancies(self):
        """Метод для создания фильтрации данных по запросу"""
        filter_key = input("Введите ключевые слова для фильтрации вакансий: \n").split()
        if not filter_key:
            return
        self.temp_result = [obj for obj in self.temp_result if obj.is_matching(filter_key)]
        self.print_result()

    def get_top_n(self):
        """Метод для создания отчета по TOP N"""
        top_n_user = int(self.check_values("Введите количество вакансий для вывода в топ N:"))
        result_top_n_sort = sorted(self.temp_result, reverse=True)
        self.temp_result = result_top_n_sort[:top_n_user]
        self.print_result()

    def get_ranged_vacancies(self):
        """Метод для создания отчета по ранжированию"""
        salary_from = int(self.check_values("Введите диапазон зарплат от:"))
        salary_to = int(self.check_values("до:"))

        self.temp_result = [
            obj for obj in self.temp_result if obj.salary_from >= salary_from and obj.salary_to <= salary_to
        ]
        self.print_result()

    def get_exit(self):
        """Метод для выхода из программы по вызову"""
        exit()

    def print_result(self):
        """Метод для вывода/печати результатов запросов"""
        for vacancy in self.temp_result:
            print(vacancy)
        print()

    def check_values(self, value):
        """Метод для проверки введенных данных на числовое значение"""
        temp_value = input(value + '\n')
        while not temp_value.isdigit():
            temp_value = input(value + '\n')
        return temp_value


vacancy_user_interaction = UserInteraction(hh_api=hh_api, worker=my_json, vac_model=Vacancy)
"""Вызов экземпляра класса"""

class Menu:
    """Класс для создания Меню"""
    def __init__(self, vacancy_user_interaction):

        self.vacancy_user_interaction = vacancy_user_interaction

    title = 'Пожалуйста, выберите команду: '
    options = ['Введите поисковый запрос по вакансии',
               'Фильтрация по ключевому слову',
               'TOP N',
               'Фильтр по диапазону ЗП',
               'Завершение программы Пользователем']
    fucs_method = ['get_vacancy',
                   'get_filtered_vacancies',
                   'get_top_n',
                   'get_ranged_vacancies',
                   'exit']

    def run(self):
        """Метод для запуска Меню"""
        self.vacancy_user_interaction.get_vacancy()
        key = 1
        while True:
            option, index = pick(self.options[key:], self.title)
            if self.fucs_method[index+key] == 'exit':
                exit()
            start = getattr(vacancy_user_interaction, self.fucs_method[index+key])
            start()
            if input('Для сброса фильтров, введите 0. Для продолжения - ENTER\n') == '0':
                key = 0
                self.vacancy_user_interaction.check_temp_result()
            else:
                key = 1


menu = Menu(vacancy_user_interaction)
"""Вызов экземпляра класса"""
