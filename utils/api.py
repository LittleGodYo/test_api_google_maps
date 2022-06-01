from utils.http_methods import Http_method

"""Методы для тестирования Google maps api"""

URL = "https://rahulshettyacademy.com"  # URL
KEY = "?key=qaclick123"  # Параметр для всех запросов
http = Http_method()


class Google_maps_api():
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post
        post_url = URL + post_resource + KEY
        result_post = http.post(post_url, json_for_create_new_place)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # Ресурс метода Get
        get_url = URL + get_resource + KEY + "&place_id=" + place_id
        result_get = http.get(get_url)
        return result_get

    """Метод для зменения новой локации"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"  # Ресурс метода Put
        put_url = URL + put_resource + KEY
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = http.put(put_url, json_for_update_new_location)
        return result_put

    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Delete
        put_url = URL + delete_resource + KEY
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = http.delete(put_url, json_for_delete_new_location)
        return result_delete
