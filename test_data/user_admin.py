from dataclasses import dataclass


@dataclass
class UserAdmin:
    name: str = 'user'
    password: str = 'bitnami'
