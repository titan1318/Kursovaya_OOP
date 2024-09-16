from src.api import HHApi
from src.vacancy import Vacancy
from file_worker import JSONSaver

def filter_vacancies(vacancies, keywords):
    """
    Фильтрует вакансии по ключевым словам в описании.
    :param vacancies: список вакансий
    :param keywords: список ключевых слов для фильтрации
    :return: отфильтрованный список вакансий
    """
    filtered_vacancies = []
    for vacancy in vacancies:
        if any(keyword.lower() in vacancy.description.lower() for keyword in keywords):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

def get_vacancies_by_salary(vacancies, min_salary):
    """
    Фильтрует вакансии по минимальной зарплате.
    :param vacancies: список вакансий
    :param min_salary: минимальная зарплата для фильтрации
    :return: список вакансий с зарплатой, превышающей указанную минимальную зарплату
    """
    ranged_vacancies = []
    for vacancy in vacancies:
        if vacancy.salary and vacancy.salary >= int(min_salary):
            ranged_vacancies.append(vacancy)
    return ranged_vacancies

def user_interaction():
    hh_api = HHApi()
    hh_vacancies = hh_api.get_request("Python", 0)  # Получаем вакансии по ключевому слову и странице
    vacancies_list = hh_api.from_vacancy(hh_vacancies.json().get('items', []))

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    # Фильтрация вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # Фильтрация вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # Пример вывода отфильтрованных вакансий
    print(f"Найдено {len(ranged_vacancies)} вакансий после фильтрации по зарплате:")
    for vacancy in ranged_vacancies[:top_n]:
        print(vacancy)

# Запуск программы
if __name__ == "__main__":
    user_interaction()
