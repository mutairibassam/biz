"""
compare function in the biz.config module. The compare function takes 
two lists of integers and returns the difference between them, i.e., 
the elements that are in the first list but not in the second.
"""
import unittest
from unittest.mock import mock_open, patch
from biz.config import compare, get_secret

class TestListDifference(unittest.TestCase):
    """
    The TestListDifference class contains two test methods:
    
    1. `test_compare_function_with_valid_prev_ids`: 
        This method tests the compare function with a valid input where 
        the previous list contains some of the same elements as the new list.

    2. `test_compare_function_with_empty_prev_ids`: 
        This method tests the compare function with an empty previous list.
    """

    def test_compare_function_with_valid_prev_ids(self):
        """
        This method tests the compare function with a valid input where 
        the previous list contains some of the same elements as the new list.
        """
        new_ids: list = [222,444,555]
        prev_ids: list = [222,333,444,555]
        expected_result: list = [333]
        function_result: list = compare(new=new_ids, prev=prev_ids)

        self.assertTrue(expected_result == function_result, "Lists are not equal.")
        self.assertIsNotNone(function_result, "Function returning None")

    def test_compare_function_with_empty_prev_ids(self):
        """
        This method tests the compare function with an empty previous list.
        """
        new_ids: list = [222,444,555]
        prev_ids: list = []
        expected_result: list = []
        function_result: list = compare(new=new_ids, prev=prev_ids)

        self.assertTrue(expected_result == function_result, "Lists are not equal.")
        self.assertIsNotNone(function_result, "Function returning None")

class TestGetSecret(unittest.TestCase):
    """
    The @patch annotation is a decorator provided by the unittest.mock 
    module in Python. It allows us to temporarily replace an object with 
    a mock object during testing. This is useful when we want to test a 
    function that depends on an external resource, such as 
    a file or a database, without actually interacting with that resource.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="telegram:\n  token: xxxxxxxxxxxxxxxxxxxxx\n  chat_id: xxxxxxxxxx\n")
    def test_get_secret_success(self, _):
        """
        Test that the get_secret function returns the expected result 
        when called with a valid YAML file.
        """
        expected_result = ["xxxxxxx","xxxxxx"]
        actual_result = get_secret()
        self.assertIsNotNone(actual_result, "Secret returns None")
        self.assertEqual(len(actual_result), len(expected_result), "Unpack Error")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_secret_file_not_found(self,_):
        """
        Test that the get_secret function raises a [FileNotFoundError]
        when called with a non-existent file.
        """
        with self.assertRaises(FileNotFoundError):
            get_secret()