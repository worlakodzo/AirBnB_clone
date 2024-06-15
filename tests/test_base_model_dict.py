#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):

    def test_compare_base_instance_ids(self):
        b1 = BaseModel()
        b2 = BaseModel(**b1.to_dict())
        self.assertEqual(b2.id, b1.id)


if __name__ == "__main__":
    unittest.main()
