#!/usr/bin/python3
<<<<<<< HEAD
"""
AirBnB clone console base class model.
"""
import uuid
from models import storage
from datetime import datetime

class BaseModel:

    """Foundation class for the object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialize a Base instance.

        Args:
            - *args: List of arguments
            - **kwargs: Dictionary of key-value arguments
        """
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a human-readable string representation of an instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

=======
import models
from uuid import uuid4
from datetime import datetime

"""
This module defines the BaseModel class which defines all common attr/methods
of other classes
"""


class BaseModel:
    """
    BaseModel Class

    __init__ Creates new instance if no args otherwise
    recreate object from dict

    Args:
        args (list): Positional arguments
        kwargs (dict): Keyword arguments
    """

    def __eq__(self, other):
        if isinstance(other, dict):
            if self.to_dict() == other:
                return True
            return False
        else:
            if self.to_dict() == other.to_dict():
                return True
            return False

    def __init__(self, *args, **kwargs):
        """
        Create BaseModel object, or load from dict object

        Arguments:
            args (list): list (not used)
            kwargs (dict): dictionary
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            kwargs.pop('__class__')
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)

    def __str__(self):
        """
        String representation of Base class

        Returns:
            String representation of Base class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert class object to dictionary

        Returns:
            Dictionary representation of class instance
        """
        # bm_dict ; base_model_dict
        bm_dict = {k: v for k, v in self.__dict__.items() if v is not None}
        bm_dict["__class__"] = self.__class__.__name__

        # isoformat() == strftime("%Y-%m-%dT%H:%M:%S.%f")
        bm_dict["created_at"] = bm_dict["created_at"].isoformat()
        bm_dict["updated_at"] = bm_dict["updated_at"].isoformat()

        return bm_dict
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
