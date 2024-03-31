"""
tests for JSONReader.
"""
import json
import os.path
import unittest
from unittest.mock import patch

from app.modules.JSONReader import JSONReader
from app.modules.paths import CONFIG_0


class TestJSONReader(unittest.TestCase):

	def test_validate_path_valid_json_path(self):
		path = "valid_path.json"
		result = JSONReader._validate_path(path)
		self.assertTrue(result)

	def test_validate_path_long_valid_json_path(self):
		path = "../../modules/very/long/path/to/json/file/valid_path.json"
		result = JSONReader._validate_path(path)
		self.assertTrue(result)

	def test_validate_path_invalid_json_path(self):
		path = "invalid_path.txt"
		result = JSONReader._validate_path(path)
		self.assertFalse(result)

	def test_validate_path_long_invalid_json_path(self):
		path = "../../modules/very/long/path/to/json/file/invalid_path.txt"
		result = JSONReader._validate_path(path)
		self.assertFalse(result)

	def test_validate_path_empty_path(self):
		path = ""
		result = JSONReader._validate_path(path)
		self.assertFalse(result)

	@patch("json.load")
	def test_read_json_valid_path(self, mock_json_load):
		mock_data = {"key": "value"}
		mock_json_load.return_value = mock_data

		path = CONFIG_0
		result = JSONReader.read_json(path)
		self.assertEqual(result, mock_data)

	@patch("json.load")
	def test_read_json_invalid_path(self, mock_json_load):
		mock_data = {"key": "value"}
		mock_json_load.return_value = mock_data

		path = "../modules/config_0.txt"
		result = JSONReader.read_json(path)
		self.assertNotEqual(result, mock_data)
		self.assertEqual(result, None)

	def test_read_json_file_not_found(self):
		path = "nonexistent_file.json"
		result = JSONReader.read_json(path)
		self.assertIsNone(result)

	@patch("builtins.open", side_effect=FileNotFoundError)
	def test_read_json_mock_file_not_found(self, mock_open):
		path = "nonexistent_file.json"
		result = JSONReader.read_json(path)
		self.assertIsNone(result)

	@patch("json.load")
	def test_read_json_invalid_json(self, mock_json_load):
		mock_json_load.side_effect = json.JSONDecodeError(
			"Invalid JSON", "", 0)

		path = "invalid_json.json"
		result = JSONReader.read_json(path)
		self.assertIsNone(result)

	def test_read_json_empty_json_file(self):
		path = path = os.path.join(
			os.path.dirname(__file__), "tests_files/empty_file.json")
		result = JSONReader.read_json(path)
		self.assertIsNone(result)

	def test_read_json_not_empty_json_file(self):
		path = os.path.join(
			os.path.dirname(__file__), "tests_files/not_empty_file.json")
		result = JSONReader.read_json(path)
		expected = {
			"key": "value",
			"key1": 1,
			"key2": 1.1,
			"key3": None,
		}
		self.assertEqual(result, expected)


if __name__ == "__main__":
	unittest.main()
