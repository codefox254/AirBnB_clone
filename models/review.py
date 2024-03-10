#!/usr/bin/python3
"""
Module defining the Review class, representing user reviews.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review provided by a user for a specific place.

    Attributes:
        place_id (str): The unique identifier of the place being reviewed.
        text (str): The text content of the review.
        user_id (str): The unique identifier of the user who wrote the review.
    """

    place_id = ""
    text = ""
    user_id = ""

