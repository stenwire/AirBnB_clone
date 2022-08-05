#!/usr/bin/python3
"""Contains city model class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to add a city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City class"""
        super().__init__(*args, **kwargs)