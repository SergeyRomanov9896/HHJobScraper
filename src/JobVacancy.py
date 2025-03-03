
from src.RequestMixin import RequestMixin

class JobVacancy:
    """Работа с данными вакансий на сайте hh.ru"""
    def __init__(self) -> None:
        """
        Инициализирует экземпляр класса

        :param name: Названия вакансии
        :param url: Ссылка на вакансию
        :param salary: Зарплата
        :param requirement: Краткое описания вакансии
        """
        self.name = [i['name']for i in RequestMixin.r_json['items']]
        self.url = [i['url'] for i in RequestMixin.r_json['items']]
        self.salary =  [
            i.get('salary', {}).get('from', i.get('salary', {}).get('to', 'Не указана'))
            if i.get('salary') else 'Не указана'
            for i in RequestMixin.r_json['items']]
        self.requirement = [i['snippet']['requirement'] for i in RequestMixin.r_json['items']]

job = JobVacancy()
