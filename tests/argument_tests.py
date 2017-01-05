import sys
import unittest

from scripts import argument


class TestArgument(unittest.TestCase):
    parser = None

    @classmethod
    def setUpClass(cls):
        cls.parser = argument.create()

    def test_argument(self):
        sys.argv = ['module']
        self.assertEqual('mongodb', vars(argument.parse(self.parser)).get(argument.ARG_NAME))


if __name__ == '__main__':
    unittest.main()
