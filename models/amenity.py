#!/usr/bin/python3
"""Contains city Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity class"""
        super().__init__(*args, **kwargs)
