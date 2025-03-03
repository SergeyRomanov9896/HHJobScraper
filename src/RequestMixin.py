
import requests

class RequestMixin:
    """
    Mixin Class для выполнения задач, связанных с запросом на сайт hh.ru.
    """
    URL = 'https://api.hh.ru/vacancies'
    response = requests.get(URL)
    r_json = response.json()
