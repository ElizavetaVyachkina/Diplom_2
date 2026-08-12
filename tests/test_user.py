import allure
import pytest

from api_methods.user_methods import UserMethods
from helpers import generate_random_user_body
from data import USER_ALREADY_EXISTS, REQUIRED_FIELDS

class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания нового пользователя"
                        "Система возвращает Status Code 200 OK поле 'success' is True")
    def test_create_unique_user(self, create_user):
        with allure.step("Получить данные созданного пользователя"):
            response, token, user_date = create_user

        with allure.step("Проверить успешное создание пользователя"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    
    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Нельзя создать пользователя с уже существующими данными"
                        "Система возвращает Status Code 403 Forbidden")
    def test_create_existing_user(self, create_user):

        with allure.step("Получить данные созданного пользователя"):
            _, _, user_data = create_user

        with allure.step("Повторно отправить запрос на создание пользователя"):
            user_methods = UserMethods()
            response = user_methods.create_user(user_data)

        with allure.step("Проверить код ответа и текст ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == USER_ALREADY_EXISTS


    @pytest.mark.parametrize("field", ["email", "password", "name"])
    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Нельзя создать пользователя без заполнения обязательных полей"
                        "Система возвращает Status Code 403 Forbidden")
    def test_create_user_without_required_field(self, field):

        user_methods = UserMethods()

        with allure.step("Сгенерировать данные пользователя"):
            user_data = generate_random_user_body()

        with allure.step(f"Удалить обязательное поле '{field}'"):
            user_data.pop(field)
        with allure.step("Отправить запрос на создание пользователя"):
            response = user_methods.create_user(user_data)
        with allure.step("Проверить код ответа и текст ошибки"):
            assert response.status_code == 403
            assert response.json()["success"] is False
            assert response.json()["message"] == REQUIRED_FIELDS


