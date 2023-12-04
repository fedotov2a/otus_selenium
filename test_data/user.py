from dataclasses import dataclass
from helpers import random_email, random_phone, random_string


@dataclass
class User:
    first_name: str = 'User' + random_string()
    last_name: str = 'User' + random_string()
    email: str = random_email()
    phone_number: str = random_phone()
    password: str = '0000'
    confirm_password: str = '0000'
