#!/usr/bin/python3
"""Contains User model class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User class"""
        super().__init__(*args, **kwargs)
