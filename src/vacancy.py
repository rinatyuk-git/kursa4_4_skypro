class Vacancy:
    """Класс для создания/построения структуры вакансий"""
    def __init__(self, name, salary_from, salary_to, city, url, requirement, responsibility, employment) -> list:
        """Конструктор для создания карточки вакансии с необходимыми полями"""
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.employment = employment
        self.__validate1()

    @staticmethod
    def validate(salary, key):
        """Метод для валидации значений поля Зарплата"""
        if not salary:
            return 0
        return salary[key] or 0

    def __validate1(self):
        """Метод для валидации прочих полей"""
        if not self.requirement:
            self.requirement = 'Отстутсвует'
            return

        if not self.responsibility:
            self.responsibility = 'Отстутсвует'
            return

    @classmethod
    def create_vacancies(cls, vacancies_data) -> list:
        """Метод для создания карточки вакансий"""
        result = []
        for line in vacancies_data:
            name = line['name']
            url = line['alternate_url']
            salary_from = cls.validate(line['salary'],'from')
            salary_to = cls.validate(line['salary'], 'to')
            requirement = line['snippet']['requirement']
            responsibility = line['snippet']['responsibility']
            city = line['area']['name']
            employment = line['employment']['name']
            vacancy = cls(name, salary_from, salary_to, city, url, requirement, responsibility, employment)
            result.append(vacancy)
        return result

    def to_dict(self) -> dict:
        """Метод для форматирования карточки вакансий"""
        return {
            'name': self.name,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'url': self.url,
            'city': self.city,
            'employment': self.employment,
            'requirement': self.requirement,
            'responsibility': self.responsibility
        }

    def __lt__(self, other):
        """Метод для сравнения вакансий по полю Зарплата"""
        if self.salary_from == other.salary_from:
            return self.salary_to < other.salary_to
        return self.salary_from < other.salary_from

    def is_matching(self, filter_words):
        """Метод соответствия вводимых данных формату структуры карточки вакансий"""
        for value in self.to_dict().values():
            for word in filter_words:
                if word.lower() in str(value).lower():
                    return True
        return False

    def __str__(self):
        """Метод для вывода карточки вакансий"""
        return f'{self.name}: {self.salary_from}->{self.salary_to}, {self.url}'
