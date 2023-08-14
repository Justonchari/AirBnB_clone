#!/usr/bin/python3
"""Unit tests for the Amenity class."""

from models.amenity import Amenity
import unittest
from datetime import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit Test Cases for the Amenity class."""

    def setUp(self):
        """Set up for the test methods."""
        pass

    def tearDown(self):
        """Tear down after the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test the instantiation of the Amenity class."""

        amenity_instance = Amenity()
        self.assertEqual(str(type(amenity_instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Amenity class."""
        attributes = storage.attributes()["Amenity"]
        amenity_instance = Amenity()
        for attribute, expected_type in attributes.items():
            self.assertTrue(hasattr(amenity_instance, attribute))
            self.assertEqual(type(getattr(amenity_instance, attribute, None)), expected_type)

if __name__ == "__main__":
    unittest.main()

