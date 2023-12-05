#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "File.json"
    __objects = {}