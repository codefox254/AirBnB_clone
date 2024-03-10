#!/usr/bin/python3
"""
Module defining the User class, handling users' information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with associated information.

    Attributes:
        email (str): The email address of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        password (str): The password of the user.
    """

    email = ""
    first_name = ""
    last_name = ""
    password = ""

