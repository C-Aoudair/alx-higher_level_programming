#!/usr/bin/python3
"""Test Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class."""

    def test_0(self):
        """Test Rectangle class."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(2, 10)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
