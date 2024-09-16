from src.vacancy import Vacancy
import json


def process_vacancies():
    # Открытие и чтение данных из JSON-файла
    with open('C:/Users/titan/PycharmProjects/Курсовая 4.ООП/data/raw.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Извлекаем список вакансий
    vacancies_data = data.get('items', [])

    # Преобразование данных в объекты Vacancy
    vacancies_list = []
    for vacancy in vacancies_data:
        name = vacancy.get('name', 'No title')
        url = vacancy.get('alternate_url', 'No URL')
        salary_info = vacancy.get('salary')
        if salary_info:
            salary = salary_info.get('from', 0)
        else:
            salary = 0
        description = vacancy.get('snippet', {}).get('requirement', 'No description')

        # Создаем объект Vacancy
        vacancy_obj = Vacancy(name, url, salary, description)
        vacancies_list.append(vacancy_obj)

    # Пример вывода вакансий
    for v in vacancies_list:
        print(v)


# Вызываем функцию для обработки данных
process_vacancies()
