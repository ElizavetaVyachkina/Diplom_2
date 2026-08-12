import requests
import allure

from url import URL

class OrderMethods:

    @allure.step("Получение данных об ингредиентах")
    def get_ingredients(self):
        return requests.get(URL.GETTING_INFORMATION_ABOUT_INGREDIENTS)
    
    @allure.step("Создание заказа без авторизации")
    def create_order_without_auth(self, ingredients):
        return requests.post(
            URL.CREATING_ORDER, 
            json={"ingredients": ingredients}
            )
    
    @allure.step("Создание заказа пользователя с авторизацией")
    def create_order_auth(self, ingredients, token):
        return requests.post(
            URL.CREATING_ORDER, 
            json={"ingredients": ingredients}, 
            headers={"Authorization": token}
            )
    

