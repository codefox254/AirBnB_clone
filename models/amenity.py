#!/usr/bin/python3
"""
Module defining the Amenity class, representing various amenities.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity, providing essential services or facilities.

    Attributes:
        name (str): The descriptive name of the amenity.
    """

    name = ""

