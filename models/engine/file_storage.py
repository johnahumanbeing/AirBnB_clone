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
        """ serializes __objects to the JSON file """
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
