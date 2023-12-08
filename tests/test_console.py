#!/usr/bin/python3
import unittest
from unittest import TestCase, mock, main
from console import HBNBCommand
from io import StringIO
import uuid
from models.base_model import BaseModel
import json
import models
import os
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage