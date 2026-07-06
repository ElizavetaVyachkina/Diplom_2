import pytest

from api_methods.user_methods import UserMethods
from helpers import generate_random_user_body

@pytest.fixture(scope="function")
def create_user():

    user_methods = UserMethods()

    user_data = generate_random_user_body()
    print(user_data)

    response = user_methods.create_user(user_data)
    print("STATUS:", response.status_code)
    print("BODY:", response.json())

    token = response.json()["accessToken"]
    
    yield response, token, user_data

    user_methods.delete_user(token)


