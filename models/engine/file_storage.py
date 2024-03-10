#!/usr/bin/python3
"""
Module for serializing and deserializing data.
"""

import json
import os

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Handles storage, serialization, and deserialization of data.
    """

    __file_path = "file.json"
    __objects = {}

    def save(self):
        """
        Serialize stored objects into JSON format and save to file.
        """
        all_objs = FileStorage.__objects
        obj_dict = {key: obj.to_dict() for key, obj in all_objs.items()}
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
            
    def new(self, obj):
        """
        Store a new object in the storage system.
        
        Args:
            obj: The object to be stored.
        """
        obj_cls_name = obj.__class__.__name__
        key = f"{obj_cls_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Retrieve all stored objects.
        
        Returns:
            A dictionary containing all stored objects.
        """
        return FileStorage.__objects


    def reload(self):
        """
        Deserialize stored objects from JSON file.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

# Optional Instructions:
# - You may add additional methods to handle specific functionalities.
# - Ensure proper testing before using in production.

