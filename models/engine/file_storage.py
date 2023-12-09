#!/usr/bin/python3
"""
This module is for storage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "File.json"
    __objects = {}

    def all(self):
        """Return all dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_obj, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            """if the JSON file (__file_path) exists"""
            with open(self.__file_path, "r", encoding="UTF8") as file:
                data = json.load(file)
                for key, value in data.items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """
        Delete obj from __objects if it's inside
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
