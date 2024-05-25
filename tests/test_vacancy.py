
def test_vacancy_init(first_vacancy):
    assert first_vacancy.name == 'Водитель'
    assert first_vacancy.salary_from == 120000
    assert first_vacancy.salary_to == 250000
    assert first_vacancy.city == 'Казань'
    assert first_vacancy.url == 'https://hh.ru/vacancy/99384178'
    assert first_vacancy.requirement == 'Водительское удостоверение категории В'
    assert first_vacancy.responsibility == '300+ тыс пользователей.'
    assert first_vacancy.employment == 'Полная занятость'




