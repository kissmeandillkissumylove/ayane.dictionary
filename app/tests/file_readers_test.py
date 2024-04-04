"""
tests for file_readers.py.
"""
import unittest
from json import JSONDecodeError
from unittest.mock import Mock

from app.config import NOT_EMPTY_JSON, EMPTY_JSON, NOT_EMPTY_TXT
from app.modules.file_readers import JsonFileReader
from app.modules.path_validators import PathValidator


class TestJsonFileReader(unittest.TestCase):
	"""
	tests for JsonFileReader.
	"""

	def test_read_existing_file(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		file_contents = {
			"key": "value", "key1": 1,
			"key2": 1.1, "key3": None
		}
		result = file_reader.read_(NOT_EMPTY_JSON)
		self.assertEqual(result, file_contents)

	def test_read_existing_file_data_substitution(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		with unittest.mock.patch(
				"builtins.open",
				unittest.mock.mock_open(read_data='{"key": "value"}')):
			result = file_reader.read_(NOT_EMPTY_JSON)

		file_contents = {"key": "value"}
		self.assertEqual(result, file_contents)

	def test_read_file_not_found_error(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		with unittest.mock.patch(
				"builtins.open",
				side_effect=FileNotFoundError()):
			result = file_reader.read_("not_existing_file.json")

		self.assertIsNone(result)

	def test_read_json_decode_error(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		with unittest.mock.patch(
				"builtins.open",
				side_effect=JSONDecodeError("Invalid JSON", "", 0)):
			result = file_reader.read_("invalid_json.json")

		self.assertIsNone(result)

	def test_read_invalid_file(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		result = file_reader.read_(NOT_EMPTY_TXT)
		self.assertIsNone(result)

	def test_read_empty_path(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		result = file_reader.read_("")
		self.assertIsNone(result)

	def test_read_empty_json(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = True
		file_reader = JsonFileReader(mock_validator)

		result = file_reader.read_(EMPTY_JSON)
		self.assertIsNone(result)

	def test_read_validator_false(self):
		mock_validator = Mock(spec=PathValidator)
		mock_validator.validate_path.return_value = False
		file_reader = JsonFileReader(mock_validator)

		result = file_reader.read_(NOT_EMPTY_JSON)
		self.assertIsNone(result)


if __name__ == '__main__':
	unittest.main()
