import unittest
from CodeStreaks.utils import load_handles

class TestUtils(unittest.TestCase):
    def test_load_handles(self):
        # Create a temporary handles file
        with open("test_handles.txt", "w") as f:
            f.write("jiangly\ntourist\nBenq\n")
        handles = load_handles("test_handles.txt")
        self.assertEqual(handles, ["jiangly", "tourist", "Benq"])