# repo2/test_utils.py
import unittest
from utils import fetch_and_transform

class TestUtils(unittest.TestCase):
    def test_fetch_and_transform(self):
        self.assertEqual(fetch_and_transform("test"), "Final Output: Processed: test")

if __name__ == '__main__':
    unittest.main()
