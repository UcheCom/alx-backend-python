#!/usr/bin/env python3
"""
Module for testing access_nested_map function
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """
        Test the access_nested_map method.
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",),)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
        path: Sequence) -> None:
        """
        Test the access_nested_map method raises an error when expected
        Args:
            nested_map (Dict): A dictionary that may have nested dict
            path (List, tuple, set): Keys to get to the required value in the
                                     nested dict
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test the get_json function
    """
    @ parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @ patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Tests the get_json method to ensure it returns the expected output.
        Args:
            url: url to send http request
            payload: expected json resp
        """
        mock_requests_get.return_value.json.return_value=test_payload
        res=get_json(test_url)
        self.assertEqual(res, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the memoization decorator, memoize
    """
    def test_memoize(self):
        """
        Test that utils.memoize decorator works as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @ memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            test=TestClass()
            test.a_property()
            test.a_property()
            mock_method.assert_called_once()
