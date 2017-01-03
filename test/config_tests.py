import unittest

from script import config


class TestArgument(unittest.TestCase):
    NOT_FOUND_FILE_PATH = ""

    def test_not_file(self):
        temp = config.CONFIG_FILE_PATH
        self.assertTrue(config.exists_config_file())
        config.CONFIG_FILE_PATH = self.NOT_FOUND_FILE_PATH
        self.assertFalse(config.exists_config_file())
        config.CONFIG_FILE_PATH = temp


if __name__ == '__main__':
    unittest.main()
