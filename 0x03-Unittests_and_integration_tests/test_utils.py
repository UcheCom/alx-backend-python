#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class implements test cases for the above class"""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Method returns what it is expected return
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), keyError),
        ({"a": 1}, ("a", "b"), keyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test the KeyError exception"""
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)