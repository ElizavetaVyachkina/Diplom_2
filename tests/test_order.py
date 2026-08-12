import allure

from api_methods.order_methods import OrderMethods
from data import (INGREDIENTS_REQUIRED)


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    @allure.description("Проверка успешного создания заказа авторизованного пользователя"
                        "Система возвращает Status Code 200 OK поле 'success' is True")
    def test_create_order_without_auth_success(self, create_user):
        order_methods = OrderMethods()
        with allure.step("Получить токен пользователя"):
            _, token, _ = create_user
        with allure.step("Получить список ингредиентов"):
            response = order_methods.get_ingredients()
            ingredients = [
                response.json()["data"][0]["_id"],
                response.json()["data"][1]["_id"]
            ]
        with allure.step("Создать заказ"):
            response = order_methods.create_order_auth(ingredients, token)

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200
            assert response.json()["success"] is True    


    @allure.title("Создание заказа без авторизации")
    @allure.description("Проверка успешного создания заказа без авторизации"
                        "Система возвращает Status Code 200 OK поле 'success' is True")
    def test_create_order_auth_success(self):
        order_methods = OrderMethods()

        with allure.step("Получить список ингредиентов"):
            response = order_methods.get_ingredients()
            ingredients = [
                response.json()["data"][0]["_id"],
                response.json()["data"][1]["_id"]
            ]
        with allure.step("Создать заказ"):
            response = order_methods.create_order_without_auth(ingredients)
            
        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200
            assert response.json()["success"] is True    


    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки создания заказа без ингредиентов"
                        "Система возвращает Status Code 400 Bad Request поле 'success' is False")
    
    def test_create_order_without_ingredients_failed(self):
        order_methods = OrderMethods()

        with allure.step("Создание заказа без ингредиентов"):
            response = order_methods.create_order_without_auth([])

        with allure.step("Проверить код и сообщение ошибки создания заказа без ингредиентов"):
            assert response.status_code == 400
            assert response.json()["success"] is False
            assert response.json()["message"] == INGREDIENTS_REQUIRED


    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки создания заказа без ингредиентов"
                        "Система возвращает Status Code 500 Internal Server Error")
    
    def test_create_order_invalid_hash_error(self):
        order_methods = OrderMethods()

        with allure.step("Создание заказа с неверным хэшем ингредиентов"):
            response = order_methods.create_order_without_auth(["incorrect"])

        with allure.step("Проверить код и сообщение ошибки создания заказа без ингредиентов"):
            assert response.status_code == 500


