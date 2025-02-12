import unittest
import json
import os
from CodeStreaks.api import get_user_submissions

class TestAPI(unittest.TestCase):
    def test_get_user_submissions(self):
        # Test with a valid handle
        handle = "tourist"
        submissions = get_user_submissions(handle)
        self.assertIsInstance(submissions, list)
        
        # Create responses directory if it doesn't exist
        directory = "api_responses"
        os.makedirs(directory, exist_ok=True)
        
        # Save the submissions to a file in the directory
        filename = os.path.join(directory, f"{handle}_submissions.json")
        with open(filename, 'w') as f:
            json.dump(submissions, f, indent=2)

    def test_invalid_handle(self):
        # Test with an invalid handle
        with self.assertRaises(Exception):
            get_user_submissions("invalid_handle_123")