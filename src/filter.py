

def filter_vacancies(vacancies, keywords):
    """
    Фильтрует вакансии по ключевым словам в названии вакансии.
    :param vacancies: список вакансий
    :param keywords: список ключевых слов для фильтрации
    :return: отфильтрованный список вакансий
    """
    filtered_vacancies = []
    for vacancy in vacancies:
        if any(keyword.lower() in vacancy.name.lower() for keyword in keywords):
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
