import allure
from requests import Response
from utils.cheking import Checking
from utils.api import Google_maps_api

check = Checking()
api = Google_maps_api()

"""Создание, изменение и удаление новой локации"""


@allure.epic("Test create place")
class Test_create_place:

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        # Метод POST
        result_post: Response = api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        check.status_code(result_post, 200)
        check.json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        check.json_value(result_post, 'status', 'OK')

        # Метод GET POST
        result_get: Response = api.get_new_place(place_id)
        check.status_code(result_get, 200)
        check.json_token(result_get,
                            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        check.json_value(result_get, 'address', '29, side layout, cohen 09')

        # Метод PUT
        result_put: Response = api.put_new_place(place_id)
        check.status_code(result_put, 200)
        check.json_token(result_put, ['msg'])
        check.json_value(result_put, 'msg', 'Address successfully updated')

        # Метод GET PUT
        result_get: Response = api.get_new_place(place_id)
        check.status_code(result_get, 200)
        check.json_token(result_get,
                            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        check.json_value(result_get, 'address', '100 Lenina street, RU')

        # Метод DELETE
        result_delete: Response = api.delete_new_place(place_id)
        check.status_code(result_delete, 200)
        check.json_token(result_delete, ['status'])
        check.json_value(result_delete, 'status', 'OK')

        # Метод GET DELETE"
        result_get: Response = api.get_new_place(place_id)
        check.status_code(result_get, 404)
        check.json_token(result_get, ['msg'])
        check.json_search_word_in_value(result_get, 'msg', 'failed')
