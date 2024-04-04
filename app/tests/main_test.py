"""
tests for main.py.
"""
import unittest
from unittest import mock
from unittest.mock import Mock, patch

from app.config import TEST_ICON_ICO
from app.main import MainWindow
from app.modules.custom_exceptions import ConfigNotFoundError
from app.tests.mock_resetter import reset_mocks


class TestMainWindow(unittest.TestCase):

	@reset_mocks
	def test_init_with_valid_config(self):
		mock_config_validator = Mock()
		mock_config_validator.validate.return_value = True

		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {
			"geometry": "500x265+0+0",
			"title": "Test Window",
			"icon": None,
			"background": "#FFFFFF"
		}

		main_window = MainWindow(
			mock_config_validator, mock_file_reader)
		main_window.update()

		self.assertEqual(main_window.geometry(), "500x265+0+0")
		self.assertEqual(main_window.title(), "Test Window")
		self.assertEqual(main_window.cget("background"), "#FFFFFF")

	@reset_mocks
	@mock.patch("app.main.MainWindow")
	def test_set_icon(self, mock_main_window):
		main_window_instance = mock_main_window.return_value
		main_window_instance.iconbitmap(TEST_ICON_ICO)
		main_window_instance.mainloop()

		main_window_instance.iconbitmap.assert_called_once_with(
			TEST_ICON_ICO)

	@reset_mocks
	@patch('app.main.JsonFileReader')
	@patch('app.main.ConfigValidator')
	def test_init_with_invalid_config(
			self,
			mock_config_validator,
			mock_file_reader):
		mock_config_validator.validate.return_value = False
		mock_file_reader.read_.return_value = None

		with self.assertRaises(ConfigNotFoundError):
			MainWindow(mock_config_validator, mock_file_reader)


if __name__ == '__main__':
	unittest.main()
