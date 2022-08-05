#!/usr/bin/python3
"""Contains Review model class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class to add a Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review class"""
        super().__init__(*args, **kwargs)