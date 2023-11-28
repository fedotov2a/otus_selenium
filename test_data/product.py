from dataclasses import dataclass
from helpers import random_string


@dataclass
class Product:
    name: str = 'TestProduct'
    meta_tag: str = random_string()
    model: str = random_string()
    price: str = '123'
