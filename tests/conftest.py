import pytest

from src.api import HHApi
from src.vacancy import Vacancy
from src.worker import JSONWorker, my_json


@pytest.fixture
def first_vacancy():
    return Vacancy(
        name='Водитель',
        salary_from=120000,
        salary_to=250000,
        city='Казань',
        url='https://hh.ru/vacancy/99384178',
        requirement='Водительское удостоверение категории В',
        responsibility='300+ тыс пользователей.',
        employment='Полная занятость'
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        name='Водитель с личным автомобилем',
        salary_from=200000,
        salary_to=250000,
        city='Ташкент',
        url='https://hh.ru/vacancy/99470117',
        requirement='Знание русского языка обязательно, узбекский приветствуется.',
        responsibility='Развозить детей, доставки.',
        employment='Полная занятость'
    )


@pytest.fixture
def first_api():
    return HHApi(
        url = 'https://api.hh.ru/vacancies'
    )

@pytest.fixture
def hh_api():
    return HHApi()