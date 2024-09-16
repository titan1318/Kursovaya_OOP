import unittest
from src.vacancy import Vacancy
from src.filter import filter_vacancies, get_vacancies_by_salary

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", 150000, "Опыт работы от 3 лет")
        self.vacancy2 = Vacancy("Java Developer", "https://hh.ru/vacancy/654321", 100000, "Опыт работы от 2 лет")
        self.vacancy3 = Vacancy("Frontend Developer", "https://hh.ru/vacancy/789123", 120000, "Знание JavaScript")

        self.vacancies = [self.vacancy1, self.vacancy2, self.vacancy3]

    def test_filter_vacancies_by_keyword(self):
        keywords = ["Java"]
        filtered = filter_vacancies(self.vacancies, keywords)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, "Java Developer")

    def test_filter_vacancies_no_results(self):
        keywords = ["C++"]
        filtered = filter_vacancies(self.vacancies, keywords)
        self.assertEqual(len(filtered), 0)

    def test_filter_by_salary(self):
        filtered = get_vacancies_by_salary(self.vacancies, 120000)
        self.assertEqual(len(filtered), 2)

if __name__ == "__main__":
    unittest.main()

