#!/usr/bin/python3
"""
Module defining the City class, representing cities within states.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city within a state.

    Attributes:
        state_id (str): The unique identifier of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

