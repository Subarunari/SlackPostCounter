import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from scripts.driver import csv


class TestDriverCsv(unittest.TestCase):
    def test_load_result(self):
        with patch('os.path.exists', MagicMock(return_value=False)):
            self.assertEqual(csv.load_result(), [])

    def test_load_latest_info(self):
        with patch('os.path.exists', MagicMock(return_value=False)):
            self.assertEqual(csv.load_latest_info(), [])


if __name__ == '__main__':
    unittest.main()
