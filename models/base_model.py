#!/usr/bin/python3
"""
This is the file containing the BaseModel class
    methods:
        __init__() - Initialises the class BaseModel
        __str__() - Returns information on class attrs
        save() - "Updates class attr - updated_at to time of update
        to_dict() - returns dictionary representaion of the class
"""

from datetime import datetime as dt
import models, uuid


class BaseModel:
    """
    A class BaseModel that defines all common 
        attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):
        """Initialises the class BaseModel"""
        id = str(uuid.uuid4())
        created_at = dt.now()
        updated_at = dt.now()
        str_time = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) == 0:
            self.id = id
            self.created_at = created_at
            self.updated_at = updated_at
            models.storage.new(self)
            models.storage.save()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = dt.strptime(kwargs["created_at"], str_time)
            self.updated_at = dt.strptime(kwargs["updated_at"], str_time)

    def __str__(self):
        """Returns information on class attrs"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates class attr - updated_at to time of update"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary representaion of the class"""
        dict_class = self.__dict__.copy()
        if "created_at" in dict_class:
            dict_class["created_at"] = dict_class["created_at"].isoformat()
        if "updated_at" in dict_class:
            dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        dict_class["__class__"] = type(self).__name__
        return dict_class