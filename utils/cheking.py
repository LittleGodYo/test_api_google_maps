"""Методы для проверки ответов на запросы"""
import json

from requests import Response


class Checking:
    """Метод для проверки статус кода"""

    @staticmethod
    def status_code(response: Response, status_code):
        assert status_code == response.status_code

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value

    """Метод для проверки значений обязательных полей в ответе запроса"""

    @staticmethod
    def json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""

    @staticmethod
    def json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info
