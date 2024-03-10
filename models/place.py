#!/usr/bin/python3
"""
Module defining the Place class, representing various rental places.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a rental place with various attributes for accommodation.

    Attributes:
        amenity_ids (list): A list of unique identifiers of amenities available in the rental place.
        city_id (str): The unique identifier of the city where the place is located.
        description (str): A description of the rental place.
        latitude (float): The latitude coordinate of the rental place.
        longitude (float): The longitude coordinate of the rental place.
        max_guest (int): The maximum number of guests allowed in the rental place.
        name (str): The name of the rental place.
        number_bathrooms (int): The number of bathrooms available in the rental place.
        number_rooms (int): The number of rooms available in the rental place.
        price_by_night (int): The price per night for renting the place.
        user_id (str): The unique identifier of the user who owns or manages the place.
    """

    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    user_id = ""

