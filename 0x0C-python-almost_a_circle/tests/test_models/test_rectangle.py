#!/usr/bin/python3
"""Test Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_0(self):
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.id == 1)

        r2 = Rectangle(8, 8, 3, 8, 10)
        self.assertTrue(r2.id == 10)
