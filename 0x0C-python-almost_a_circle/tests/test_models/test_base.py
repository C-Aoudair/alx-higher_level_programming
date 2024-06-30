#!/usr/bin/python3
"""Test Base class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_0(self):
        """Test Base class."""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(-1)
        self.assertEqual(b.id, -1)
        b = Base()
        self.assertEqual(b.id, 4)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base()
        self.assertEqual(b.id, 5)    
