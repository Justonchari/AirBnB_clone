#!/usr/bin/python3
<<<<<<< HEAD
"""
Storage testing
"""
from time import sleep
import json
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest

class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
=======
import unittest
import tempfile
from models import BaseModel, FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fp = tempfile.NamedTemporaryFile()
        cls.file_path = cls.fp.name
        cls.storage = FileStorage()
        cls.base = BaseModel()

    @classmethod
    def tearDownClass(cls):
        del cls.storage
        del cls.base
        cls.fp.close()

    def test_new(self):
        self.storage.new(self.base)
        self.assertIn(self.base,
                      [v for k, v in self.storage.all().items()])

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)
        self.assertTrue(
                all([isinstance(v, BaseModel)
                     for k, v in self.storage.all().items()])
                )

    def test_save(self):
        self.storage.new(self.base)
        self.storage.save()
        self.storage.reload()
        self.assertIn(self.base,
                      [v for k, v in self.storage.all().items()])

    def test_reload(self):
        for i in range(5):
            self.storage.new(BaseModel())

        self.storage.new(self.base)
        self.storage.save()
        self.storage.reload()

        self.assertTrue(self.storage.all() != {})
        self.assertIn(self.base,
                      [v for k, v in self.storage.all().items()])
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c
