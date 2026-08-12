import requests
import allure
from url import URL

class UserMethods:

    @allure.step("Создание пользователя")
    def create_user(self, user_data):
        return requests.post(URL.CREATING_USER, json=user_data)
    
    @allure.step("Авторизация пользователя")
    def login_user(self, login_data):
        return requests.post(URL.USER_LOGIN, json=login_data)
    
    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        return requests.delete(URL.DELETE_USER, headers={"Authorization": token})


