#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    This is the class user

    Attributes:
        email: the email of the user
        password: the password of the user acc
        first_name: the users first name
        last_name: the users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""