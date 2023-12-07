#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "File.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self,obj):
        self.__objects[obj.id] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (including deletions)
        """
        objs_dict = {k: self.__objects[k].to_dict()
                     for k in self.__objects.keys()}

        with open(self.__file_path, "w") as f:
            json.dump(objs_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF8") as f:
                data = json.load(f)
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