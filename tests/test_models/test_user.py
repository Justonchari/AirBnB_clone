#!/usr/bin/python3
<<<<<<< HEAD
"""Unit test for the User Class."""

from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import unittest
from datetime import datetime
import time

class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()

=======
import unittest
from datetime import datetime

from models import User, storage, BaseModel


class TestUserClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User()

    def test_user_initialization(self):
        self.assertIsInstance(self.user.id, str)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsNotNone(self.user.updated_at)
        self.assertIsInstance(self.user.updated_at, datetime)

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.assertIsInstance(self.user, BaseModel)
        self.assertEqual(type(self.user), User)

    def test_user_str(self):
        self.assertEqual(
            self.user.__str__(),
            f"[{self.user.__class__.__name__}] \
({self.user.id}) {self.user.__dict__}",
        )

    def test_user_save(self):
        prev_updated_at = self.user.updated_at
        self.user.save()

        self.assertNotEqual(self.user.updated_at, prev_updated_at)
        self.assertTrue(self.user.updated_at > prev_updated_at)

    def test_user_to_dict(self):
        bm_dict = self.user.to_dict()

        self.assertIsInstance(bm_dict, dict)
        self.assertTrue(all([isinstance(v, str) for k, v in bm_dict.items()]))
        self.assertEqual(
                bm_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(
                bm_dict["updated_at"], self.user.updated_at.isoformat())

    def test_user_from_dict(self):
        bm_dict = self.user.to_dict()
        dummy_user = User(**bm_dict)
        self.assertEqual(bm_dict, dummy_user.to_dict())


# if __name__ == "__main__":
# Do stuff
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
