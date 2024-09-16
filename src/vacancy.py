
class Vacancy:
    __slots__ = ['name', 'url', 'salary', 'description']

    def __init__(self, name: str,
                 url: str,
                 salary: int | None,
                 description: str | None):
        self.name: str = name
        self. url: str = url
        self.salary: int = self._validate(salary)
        self.description: str | None = description

    @staticmethod
    def _validate(salary: int | None) -> int:
        return salary or 0

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.salary < other.salary

    def __repr__(self) -> str:
        return f"Vacancy('{self.name}', '{self.url}', {self.salary}, '{self.description}')"

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'description': self.description
        }

a = Vacancy(name= "a", url= "a", salary= None, description= None)
print (a)

