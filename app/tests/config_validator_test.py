"""
tests for config_validator.py
"""
import json
import unittest
from unittest.mock import patch

from app.modules.config_validator import (
	ValidationTypes, ConfigValidationTemplate, ConfigValidator
)
from app.modules.paths import CONFIG_TEMPLATE


class TestValidationTypes(unittest.TestCase):

	def test_load_types_is_dict(self):
		result = ValidationTypes.load_types()
		self.assertIsInstance(result, dict)

	def test_load_types_dict_values(self):
		result = ValidationTypes.load_types()
		result = result.values()
		for _ in result:
			self.assertEqual(_, [str, None])

	def test_load_types_is_it_the_right_dict(self):
		with open(CONFIG_TEMPLATE, "r", encoding="utf-8") as file_json:
			dict_ = json.load(file_json)
		dict_ = dict_.keys()
		result = ValidationTypes.load_types().keys()
		self.assertEqual(result, dict_)

	def test_load_types_values_is_not_equal(self):
		with open(CONFIG_TEMPLATE, "r", encoding="utf-8") as file_json:
			dict_ = json.load(file_json)
		dict_ = dict_.values()
		result = ValidationTypes.load_types().values()
		self.assertNotEqual(result, dict_)


class TestConfigValidationTemplate(unittest.TestCase):

	@patch("app.modules.config_validator.JSONReader.read_json")
	@patch("app.modules.config_validator.ValidationTypes.load_types")
	def test_init(self, mock_load_types, mock_read_json):
		mock_load_types.return_value = {
			"key1": str,
			"key2": int
		}
		mock_read_json.return_value = {
			"key1": "value1",
			"key2": "value2"
		}

		result = ConfigValidationTemplate()
		self.assertEqual(
			result.get_types(), {"key1": str, "key2": int})
		self.assertEqual(
			result.get_patterns(), {"key1": "value1", "key2": "value2"})

	def test_get_types_is_dict(self):
		result = ConfigValidationTemplate().get_types()
		self.assertIsInstance(result, dict)

	def test_get_types_keys(self):
		with open(CONFIG_TEMPLATE, "r", encoding="utf-8") as file_json:
			dict_ = json.load(file_json)
		dict_ = dict_.keys()
		result = ConfigValidationTemplate().get_types().keys()
		self.assertEqual(result, dict_)

	def test_get_types_values(self):
		result = ConfigValidationTemplate().get_types().values()
		expected = [str, None]
		for _ in result:
			self.assertEqual(_, expected)

	def test_get_patterns_is_dict(self):
		result = ConfigValidationTemplate().get_patterns()
		self.assertIsInstance(result, dict)

	def test_get_patterns_keys(self):
		with open(CONFIG_TEMPLATE, "r", encoding="utf-8") as file_json:
			dict_ = json.load(file_json)
		dict_ = dict_.keys()
		result = ConfigValidationTemplate().get_patterns().keys()
		self.assertEqual(result, dict_)

	def test_get_patterns_values(self):
		with open(CONFIG_TEMPLATE, "r", encoding="utf-8") as file_json:
			expected = json.load(file_json)
		expected = expected.values()

		results = ConfigValidationTemplate().get_patterns().values()

		for expect, result in zip(expected, results):
			self.assertEqual(expect, result)


class TestConfigValidator(unittest.TestCase):

	def test_validate_config_is_not_dict(self):
		config = [1, 2, 3]
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config = (1, 2, 3)
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config = {1, 2, 3}
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config = 455743
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config = 43646.354654
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config = "configuration_file.json"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_is_empty_dict(self):
		config = {}
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_is_not_empty_dict(self):
		config = {1: "1", 2: "2", 3: "3", 4: "4"}
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_all_the_values_are_none(self):
		config = {
			"geometry": None,
			"title": None,
			"icon": None,
			"background": None
		}
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

	def test_validate_config_geometry_pattern(self):
		config = {
			"geometry": "500x265+500+200",
			"title": None,
			"icon": None,
			"background": None
		}
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["geometry"] = "500x265+500+"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["geometry"] = "500x265+500"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["geometry"] = "500x265+"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["geometry"] = "500x265"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["geometry"] = "1x1"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["geometry"] = "500x265+500+200+100"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["geometry"] = "500X265+500+200"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["geometry"] = 500 + 200
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_title_pattern(self):
		config = {
			"geometry": None,
			"title": "",
			"icon": None,
			"background": None
		}
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["title"] = "string"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["title"] = 123
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["title"] = "123"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["title"] = "32symbol" * 4
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["title"] = "more_than_32_symbols_title" * 3
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_icon_pattern(self):
		config = {
			"geometry": None,
			"title": "",
			"icon": "name.ico",
			"background": None
		}
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["icon"] = "path\\ico.ico"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["icon"] = "long\\long\\long\\long\\long\\long\\long\\long\\ico.ico"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["icon"] = "path\\ico.json"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

	def test_validate_config_background_pattern(self):
		config = {
			"geometry": None,
			"title": None,
			"icon": None,
			"background": "#000000"
		}
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["background"] = "#FFFFFF"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["background"] = "#abcdfg"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["background"] = "#abcdf1"
		result = ConfigValidator.validate_config(config)
		self.assertTrue(result)

		config["background"] = "abcdf1"
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)

		config["background"] = 111111
		result = ConfigValidator.validate_config(config)
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()
