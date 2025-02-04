import unittest
from CodeStreaks.api import get_user_submissions

class TestAPI(unittest.TestCase):
    def test_get_user_submissions(self):
        # Test with a valid handle
        submissions = get_user_submissions("tourist")
        self.assertIsInstance(submissions, list)

    def test_invalid_handle(self):
        # Test with an invalid handle
        with self.assertRaises(Exception):
            get_user_submissions("invalid_handle_123")