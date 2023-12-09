#!/usr/bin/python3
"""
This is a class defining city
"""


from models.base_model import BaseModel

class City(BaseModel):
    """
    This is city class

    Attributes:
        name: Name of city
        state_id: ID of the state
    """
    name = ""
    state_id = ""
