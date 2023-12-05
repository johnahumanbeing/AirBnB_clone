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
        with open(self.__file_path) as json_file:
            json_obj = json.load(json_file)
            for key in json_obj:
                self.__objects[key] = BaseModel(**json_obj[key])