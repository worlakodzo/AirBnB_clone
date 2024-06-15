#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):

    def test_is_id_string(self):
        b1 = BaseModel()
        self.assertTrue(isinstance(b1.id, str))

    def test_created_at_a_datetime(self):
        b1 = BaseModel()
        self.assertTrue(isinstance(b1.created_at, datetime))

    def test_compare_two_obj_id(self):
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertFalse(b1.id == b2.id)

    def test_save(self):
        b1 = BaseModel()

        self.assertIsNone(b1.save())

    def test_to_dict(self):
        b1 = BaseModel()

        self.assertTrue(isinstance(b1.to_dict(), dict))


if __name__ == "__main__":
    unittest.main()
