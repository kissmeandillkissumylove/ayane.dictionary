"""
injector_.py tests.
"""
import unittest

from injector import Injector

from app.modules.config_validator import (
	JsonTypesContainer, BaseContainer, ConfigValidationContainer)
from app.modules.file_readers import JsonFileReader, BaseFileReader
from app.modules.injector_ import ModuleDI
from app.modules.path_validators import (
	PathValidator, BasePathValidator)


class TestModuleDI(unittest.TestCase):
	"""
	tests for the ModuleDI class.
	"""

	def test_injector_creates_objects(self):
		_injector_ = Injector([ModuleDI])
		json_path_validator = _injector_.get(PathValidator)
		self.assertIsInstance(json_path_validator, BasePathValidator)
		self.assertIsInstance(json_path_validator, PathValidator)

		json_reader = _injector_.get(JsonFileReader)
		self.assertIsInstance(json_reader, BaseFileReader)
		self.assertIsInstance(json_reader, JsonFileReader)

		json_types_container = _injector_.get(JsonTypesContainer)
		self.assertIsInstance(json_types_container, BaseContainer)
		self.assertIsInstance(json_types_container, JsonTypesContainer)

		config_validation_container = _injector_.get(
			ConfigValidationContainer)
		self.assertIsInstance(config_validation_container, BaseContainer)
		self.assertIsInstance(
			config_validation_container, ConfigValidationContainer)

	def test_singleton_for_objects(self):
		injector_0 = Injector([ModuleDI])

		json_path_validator_0 = injector_0.get(PathValidator)
		json_path_validator_1 = injector_0.get(PathValidator)
		self.assertIs(json_path_validator_0, json_path_validator_1)

		json_file_reader_0 = injector_0.get(JsonFileReader)
		json_file_reader_1 = injector_0.get(JsonFileReader)
		self.assertIs(json_file_reader_0, json_file_reader_1)

	def test_dependency_injection_failure(self):
		with self.assertRaises(TypeError):
			injector = Injector([ModuleDI()])
			json_file_reader = injector.get()


if __name__ == '__main__':
	unittest.main()
