#!/usr/bin/python3

"""
This is a class defining BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Initialize a new BaseModel
    Args:
        *args: unused parameters
        **kwargs: attributes
    """
    def __init__(self, *args, **kwargs):
        self.id= str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


        if len(kwargs) != 0:
            format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, format)
                else:
                    self.__dict__[key] = value
        models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel
        Returns:
            str representation of the BaseModel
        """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """
        update the model
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dict of keys and values
        Returns:
            dict of keys and values
        """
        dict_copy = self.__dict__.copy()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
