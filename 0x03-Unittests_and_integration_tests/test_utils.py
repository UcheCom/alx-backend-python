#!/usr/bin/env python3
'''Module for testing utils file
'''
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''This is class for testing access_nestd_map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Tests that a KeyError is raised for various inputs """
        with self.assertRaises(KeyError) as er:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(er.exception))


class TestGetJson(unittest.TestCase):
    """ This is class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ This tests for the utils.get_json function to check
            that it returns the expected result.
        """
        config = {'return_value.json.return_value': test_payload}
        pat = patch('requests.get', **config)
        mock = pat.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        pat.stop()
