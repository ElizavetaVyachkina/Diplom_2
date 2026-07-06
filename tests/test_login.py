import allure
import pytest

from api_methods.user_methods import UserMethods
from data import LOGIN_FAILED


class TestLoginUser:

    @allure.title("Логин существующего пользователя")
    @allure.description("Проверка успешной авторизации пользователя")
    def test_login_valid_user(self, create_user):

        with allure.step("Получить данные созданного пользователя"):
            _, _, user_data = create_user

        user_methods = UserMethods()

        with allure.step("Отправить запрос на логин"):
            login_data = {
                "email": user_data["email"],
                "password": user_data["password"]
            }
            response = user_methods.login_user(login_data)

        with allure.step("Проверить успешный ответ"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert "accessToken" in response.json()

    @pytest.mark.parametrize(
        "field, new_value", 
        [
            ("email","wronglogin"),
            ("password", "wrongpassword")
        ]
    )
    @allure.title("Логин пользователя с неверными данными")
    @allure.description("Проверка ошибки при неправильном email или пароле")
    def test_login_invalid_user(self, create_user, field, new_value):

        user_methods = UserMethods()

        with allure.step("Получить данные созданного пользователя"):
            _, _, user_data = create_user

        with allure.step("Создать данные с ошибкой"):
            test_data = user_data.copy()
            test_data[field] = new_value

        with allure.step("Отправить запрос на логин с неверными данными"):
            response = user_methods.login_user(test_data)

        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 401
            assert response.json()["success"] is False
            assert response.json()["message"] == LOGIN_FAILED


