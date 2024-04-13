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


class TestMemoize(unittest.TestCase):
    """ test class to tes utils.memoize"""

    def test_memoize(self):
        """ This tests the function when calling a_property twice,
        the correct result is returned but a_method is only
        called once using assert_called_once
        """

        class TestClass:
            """ This is test Class for memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
