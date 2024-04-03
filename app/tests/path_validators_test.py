"""
tests for path_validators.py.
"""
import unittest

from app.modules.path_validators import PathValidator


class TestPathValidator(unittest.TestCase):

	def test_validate_path_valid_json_path(self):
		validator = PathValidator()
		result = validator.validate_path("path/to/file.json", r"\.json$")
		self.assertTrue(result)

	def test_validate_path_invalid_json_path(self):
		validator = PathValidator()
		result = validator.validate_path("path/to/file", r"\.json$")
		self.assertFalse(result)

	def test_validate_path_other_extension_path(self):
		validator = PathValidator()
		result = validator.validate_path("path/to/file.xml", r"\.json$")
		self.assertFalse(result)

	def test_validate_path_invalid_input_types(self):
		validator = PathValidator()
		result = validator.validate_path(123, r"\.json$")
		self.assertFalse(result)

		result = validator.validate_path(23.32, r"\.json$")
		self.assertFalse(result)

		result = validator.validate_path([1, 2, 3], r"\.json$")
		self.assertFalse(result)

		result = validator.validate_path({"key": "value"}, r"\.json$")
		self.assertFalse(result)

	def test_validate_path_valid_txt_path_and_pattern(self):
		validator = PathValidator()
		result = validator.validate_path("path/to/file.txt", r"\.txt$")
		self.assertTrue(result)

	def test_validate_path_valid_cvs_path_and_pattern(self):
		validator = PathValidator()
		result = validator.validate_path("path/to/file.cvs", r"\.cvs$")
		self.assertTrue(result)


if __name__ == '__main__':
	unittest.main()
