import unittest
from src.vacancy import Vacancy

class TestVacancy(unittest.TestCase):

    def setUp(self):
        """Создаем пример вакансии для тестов"""
        self.vacancy1 = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", 150000, "Опыт работы от 3 лет")
        self.vacancy2 = Vacancy("Java Developer", "https://hh.ru/vacancy/654321", 100000, "Опыт работы от 2 лет")

    def test_create_vacancy(self):
        """Тестируем создание вакансии"""
        self.assertEqual(self.vacancy1.name, "Python Developer")
        self.assertEqual(self.vacancy1.url, "https://hh.ru/vacancy/123456")
        self.assertEqual(self.vacancy1.salary, 150000)
        self.assertEqual(self.vacancy1.description, "Опыт работы от 3 лет")

    def test_compare_vacancies(self):
        """Тестируем сравнение вакансий по зарплате"""
        self.assertTrue(self.vacancy2 < self.vacancy1)

    def test_to_dict(self):
        """Тестируем преобразование вакансии в словарь"""
        expected = {
            'name': "Python Developer",
            'url': "https://hh.ru/vacancy/123456",
            'salary': 150000,
            'description': "Опыт работы от 3 лет"
        }
        self.assertEqual(self.vacancy1.to_dict(), expected)

if __name__ == "__main__":
    unittest.main()
