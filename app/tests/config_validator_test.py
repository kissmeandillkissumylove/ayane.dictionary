"""
tests for config_validator.py
"""
import json
import unittest
from unittest.mock import Mock

from app.config import CORRECT_CONFIG, INCORRECT_CONFIG
from app.modules.config_validator import (
	JsonTypesContainer, ConfigValidationContainer, ConfigValidator)


class TestJsonTypesContainer(unittest.TestCase):

	def test_load_types_is_dict(self):
		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {"key1": 1, "key2": 2}
		types_container = JsonTypesContainer(mock_file_reader)

		result = types_container.load_types()
		self.assertIsInstance(result, dict)

	def test_load_types(self):
		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {"key1": 1, "key2": 2}
		types_container = JsonTypesContainer(mock_file_reader)

		result = types_container.load_types()
		expected = {"key1": [str, None], "key2": [str, None]}
		self.assertEqual(result, expected)


class TestConfigValidationContainer(unittest.TestCase):

	def test_init(self):
		mock_types_container = Mock()
		mock_types_container.load_types.return_value = {
			"key": [str, None]}

		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {"key": "pattern"}

		config_validator_container = ConfigValidationContainer(
			mock_types_container, mock_file_reader)

		self.assertIsInstance(config_validator_container._template, dict)

		expected = {
			"types": {"key": [str, None]}, "patterns": {"key": "pattern"}}
		self.assertEqual(config_validator_container._template, expected)

	def test_get_types(self):
		mock_container = Mock()
		mock_container.load_types.return_value = {"key": [str, None]}

		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {"key": "pattern"}

		config_validator_container = ConfigValidationContainer(
			mock_container, mock_file_reader)

		expected = {"key": [str, None]}
		self.assertIsInstance(config_validator_container.get_types(), dict)
		self.assertEqual(config_validator_container.get_types(), expected)

	def test_get_patterns(self):
		mock_container = Mock()
		mock_container.load_types.return_value = {"key": [str, None]}

		mock_file_reader = Mock()
		mock_file_reader.read_.return_value = {"key": "pattern"}

		config_validator_container = ConfigValidationContainer(
			mock_container, mock_file_reader)

		expected = {"key": "pattern"}
		self.assertIsInstance(config_validator_container.get_patterns(), dict)
		self.assertEqual(config_validator_container.get_patterns(), expected)


class TestConfigValidator(unittest.TestCase):

	def test_validate_correct_config_files(self):
		mock_validation_container = Mock()
		mock_validation_container.get_types.return_value = {
			"geometry": [str, None],
			"title": [str, None],
			"icon": [str, None],
			"background": [str, None]
		}
		mock_validation_container.get_patterns.return_value = {
			"geometry": "^500x265(?:\\+\\d+)?(?:\\+\\d+)?$",
			"title": "^.{0,32}$",
			"icon": "\\.ico$",
			"background": "^#[0-9a-fA-F]{6}$"
		}

		config_validator = ConfigValidator(mock_validation_container)

		with open(CORRECT_CONFIG, "r", encoding="utf-8") as file_json:
			correct_configs_list = json.load(file_json)

		for correct_config in correct_configs_list:
			self.assertTrue(config_validator.validate(correct_config))

	def test_validate_incorrect_config_files(self):
		mock_validation_container = Mock()
		mock_validation_container.get_types.return_value = {
			"geometry": [str, None],
			"title": [str, None],
			"icon": [str, None],
			"background": [str, None]
		}
		mock_validation_container.get_patterns.return_value = {
			"geometry": "^500x265(?:\\+\\d+)?(?:\\+\\d+)?$",
			"title": "^.{0,32}$",
			"icon": "\\.ico$",
			"background": "^#[0-9a-fA-F]{6}$"
		}

		config_validator = ConfigValidator(mock_validation_container)

		with open(INCORRECT_CONFIG, "r", encoding="utf-8") as file_json:
			incorrect_configs_list = json.load(file_json)

		for incorrect_config in incorrect_configs_list:
			self.assertFalse(config_validator.validate(incorrect_config))

	def test_validate_incorrect_config_files_one_field(self):
		mock_validation_container = Mock()
		mock_validation_container.get_types.return_value = {
			"geometry": [str, None],
			"title": [str, None],
			"icon": [str, None],
			"background": [str, None]
		}
		mock_validation_container.get_patterns.return_value = {
			"geometry": "^500x265(?:\\+\\d+)?(?:\\+\\d+)?$",
			"title": "^.{0,32}$",
			"icon": "\\.ico$",
			"background": "^#[0-9a-fA-F]{6}$"
		}

		config_validator = ConfigValidator(mock_validation_container)
		config = {"geometry": "500x265"}
		self.assertFalse(config_validator.validate(config))


if __name__ == "__main__":
	unittest.main()
