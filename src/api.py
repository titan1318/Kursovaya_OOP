from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import requests
from typing import List, Dict, Any

class AbstractApi(ABC):
    @abstractmethod
    def get_request(self, *args):
        pass

class HHApi(AbstractApi):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_request(self, keyword: str, page: int) -> requests.Response:
        params = {
            "text": keyword,
            "page": page
        }
        response = requests.get(self.url, params=params, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Ошибка запроса к API: {response.status_code}")
        return response

    def from_vacancy(self, vacancies: List[Dict[str, Any]]) -> List[Vacancy]:
        return [
            Vacancy(
                vacancy.get('name', 'No title'),
                vacancy.get('alternate_url', 'No URL'),
                vacancy.get('salary', {}).get('from', 0),
                vacancy.get('snippet', {}).get('requirement', 'No description')
            ) for vacancy in vacancies
        ]


    def from_vacancy(self, vacancies: list[dict[str, Any]]) -> list[Vacancy]:
        return [Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy.get('snippet', {}).get('requirement')) for vacancy in vacancies]