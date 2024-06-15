#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModelDict(unittest.TestCase):

    def test_reload_from_file(self):
        storage = FileStorage()
        self.assertTrue(storage.reload())

    def test_save_to_file(self):
        storage = FileStorage()
        self.assertTrue(storage.save())


if __name__ == "__main__":
    unittest.main()
