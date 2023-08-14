#!/usr/bin/python3
<<<<<<< HEAD
"""A module containing the Place class."""
=======
"""
This module defines Place Class
"""
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c

from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """Class representing a Place."""
=======
    """
    Place  class
    """
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
