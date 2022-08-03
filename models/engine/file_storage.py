#!/usr/bin/python3
"""
This is the file storage module
    methods:
        all() - Returns all objects attrs
        new() - Creates new object key
        save() - Appends object key to new dictionary of class attrs
        reload() - Deserializes json file to retrieve old json objects
"""

import json
from os import path
from models.base_model import BaseModel


file = 'file.json'

class FileStorage:
    """
    Serializes and Deserializes class instance to a json file
    """
    
    def __init__(self, __file_path=file, __objects={}):
        self.__file_path = __file_path
        self.__objects = __objects

    def all(self):
        """Returns all objects attrs"""
        return self.__objects

    def new(self, obj):
        """Creates new object key"""
        obj_key = type(obj).__name__ + "." + obj.id
        self.__objects[obj_key] = obj

    def save(self):
        """Appends object key to new dictionary of class attrs"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(json_objects, indent=4))
            # json.dump(json_objects, f)

    def reload(self):
        """Deserializes json file to retrieve old json objects"""
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                d = json.load(f)
                for k, v in d.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))
        else:
            pass
