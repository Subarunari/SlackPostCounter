import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from scripts import config


class TestArgument(unittest.TestCase):
    NOT_FOUND_FILE_PATH = ""

    def test_not_file(self):
        temp = config.CONFIG_FILE_PATH
        self.assertTrue(config.exists_config_file())
        config.CONFIG_FILE_PATH = self.NOT_FOUND_FILE_PATH
        self.assertFalse(config.exists_config_file())
        config.CONFIG_FILE_PATH = temp

    def test_backup_count(self):
        with patch('yaml.load', MagicMock(return_value=dict())):
            self.assertEqual(config.DEFAULT_BACKUP_COUNT, config.get_logging_backup_count())

        with patch('yaml.load', MagicMock(return_value={"logging": {"backup_count": 10}})):
            self.assertEqual(10, config.get_logging_backup_count())


if __name__ == '__main__':
    unittest.main()
