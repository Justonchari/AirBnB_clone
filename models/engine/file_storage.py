#!/usr/bin/python3
<<<<<<< HEAD

"""Class for handling file storage."""

import json
import os
import datetime

class FileStorage:
    """Class for handling the serialization and deserialization of base classes."""
      
        __file_path = "file.json"
        __objects = {}

        class FileStorage:
    def all(self):
        """Returns the dictionary of stored objects."""
        # TODO: Consider using a copy() for this.
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the stored objects dictionary."""
        # TODO: Consider using more specific specifiers.
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes stored objects to a JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            object_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(object_dict, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """Deserializes a JSON file into stored objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            object_dict = json.load(f)
            object_dict = {
                k: self.classes()[v["__class__"]](**v)
                for k, v in object_dict.items()
            }
            # TODO: Decide whether to overwrite or insert.
            FileStorage.__objects = object_dict

    def attributes(self):
        """Returns valid attributes and their types for each class name."""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes

=======
"""
This module defines Filestorage class which serializes objects to JSON
Saves objects to JSON, and retrieves objects from JSON file
"""
import json
from pathlib import Path

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class BaseModelEncoder(json.JSONEncoder):
    """
    Serialize instances of BaseModel to dictionary

    Returns:
        dictionary if obj is instance of BaseModel, else default object
    """
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        return super().default(self, obj)


def base_model_object_hook(dct):
    """
    Function that will be called with the result of any object literal decoded

    Returns:
        BaseModel instance or default object
    """

    if "__class__" in dct:
        return eval(f"{dct['__class__']}(**dct)")
    return dct


class FileStorage:
    """
    Serialize BaseModel instances to JSON file and vice versa
    """
    __file_path = "file.json"
    __objects = {}

    # def __init__(self, file_path=None):
    #     """
    #     Initialize Filestorage object
    #     """
    #     if file_path is not None:
    #         FileStorage.__file_path = file_path

    def all(self):
        """
        Get all object instances
        Returns:
            All object instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new object instance
        """
        FileStorage.__objects[
                f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serialize objects (__objects) to JSON file
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fd:
            json.dump(FileStorage.__objects, fd, cls=BaseModelEncoder)

    def reload(self):
        """
        De-serialize object from JSON file and store in __objects
        """
        if Path(FileStorage.__file_path).exists():
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fd:
                FileStorage.__objects = json.load(
                        fd, object_hook=base_model_object_hook)
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
