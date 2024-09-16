from typing import List
from src.vacancy import Vacancy
import json



class FileWorker:
    def __init__(self, file_name: str = "vacancies.json"):
        self._file_name = file_name

    def read_all_vacancies(self) -> List[Vacancy]:
        with open(self._file_name, "r") as file:
            data = json. load(file)
        return [Vacancy(**vacancy) for vacancy in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        try:
            with open(self._file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        if vacancy.to_dict() not in data:  # Проверка на дублирование вакансий
            data.append(vacancy.to_dict())

        with open(self._file_name, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        with open(self._file_name, "r") as file:
            data = json.load(file)

        data = [v for v in data if v['url'] != vacancy.url]

        with open(self._file_name, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class JSONSaver:
    def __init__(self, file_name='vacancies.json'):
        self.file_name = file_name

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в JSON файл"""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
        except FileNotFoundError:
            vacancies = []

        if vacancy.to_dict() not in vacancies:
            vacancies.append(vacancy.to_dict())

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из JSON файла"""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
        except FileNotFoundError:
            return

        vacancies = [v for v in vacancies if v['url'] != vacancy.url]

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

