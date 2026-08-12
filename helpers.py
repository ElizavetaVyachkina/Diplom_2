from faker import Faker
import uuid

fake = Faker()

def generate_random_user_body():
    return {
        "email": f"{uuid.uuid4()}@test.ru",
        "password": fake.password(length=10, upper_case=False, lower_case=True),
        "name": fake.first_name()
    }

