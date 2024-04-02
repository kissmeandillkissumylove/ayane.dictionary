"""
injector_.py tests.
"""
import unittest
from unittest.mock import MagicMock

from injector import Injector

from app.modules.file_readers import JsonFileReader, BaseFileReader
from app.modules.injector_ import ModuleDI
from app.modules.path_validators import (
	JsonPathValidator, BasePathValidator)


class TestModuleDI(unittest.TestCase):
	"""
	tests for the ModuleDI class.
	"""

	def test_injector_creates_objects(self):
		_injector_ = Injector([ModuleDI])
		json_path_validator = _injector_.get(JsonPathValidator)
		self.assertIsInstance(json_path_validator, BasePathValidator)
		self.assertIsInstance(json_path_validator, JsonPathValidator)

		json_reader = _injector_.get(JsonFileReader)
		self.assertIsInstance(json_reader, BaseFileReader)
		self.assertIsInstance(json_reader, JsonFileReader)

	def test_singleton_for_objects(self):
		injector_0 = Injector([ModuleDI])

		json_path_validator_0 = injector_0.get(JsonPathValidator)
		json_path_validator_1 = injector_0.get(JsonPathValidator)
		self.assertIs(json_path_validator_0, json_path_validator_1)

		json_file_reader_0 = injector_0.get(JsonFileReader)
		json_file_reader_1 = injector_0.get(JsonFileReader)
		self.assertIs(json_file_reader_0, json_file_reader_1)


class TestJsonFileReaderInjection(unittest.TestCase):
	"""
	tests for the JsonFileReader class.
	"""

	def test_dependency_injection(self):
		json_path_validator = MagicMock(spec=JsonPathValidator)
		injector = Injector(
			[ModuleDI()], {JsonPathValidator: json_path_validator})

		json_file_reader = injector.get(JsonFileReader)

		self.assertIsInstance(
			json_file_reader.path_validator, JsonPathValidator)

	def test_dependency_injection_failure(self):
		with self.assertRaises(TypeError):
			injector = Injector([ModuleDI()])
			json_file_reader = injector.get()


if __name__ == '__main__':
	unittest.main()
