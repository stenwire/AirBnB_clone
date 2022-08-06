#!/usr/bin/python3
"""Contains State model class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    This is the state class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State class"""
        super().__init__(*args, **kwargs)
