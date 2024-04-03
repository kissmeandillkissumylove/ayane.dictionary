"""
contains classes whose job is to validate the configuration file.
"""
import re
from abc import ABC, abstractmethod

from injector import singleton, inject

from app.config import CONFIG_PATTERNS
from app.modules.file_readers import JsonFileReader


@singleton
class BaseContainer(ABC):
	"""
	abstract class for storing data from file.
	"""
	pass


@singleton
class BaseValidator(ABC):
	"""
	abstract class for validator.
	"""

	@abstractmethod
	def validate(self, *args, **kwargs):
		"""
		validate function.
		"""
		raise NotImplementedError


class JsonTypesContainer(BaseContainer):
	"""
	contains valid configuration file types.
	"""

	@inject
	def __init__(self, file_reader: JsonFileReader):
		"""
		:param file_reader: requires file reader.
		"""
		self._file_reader = file_reader

	def load_types(self) -> dict:
		"""
		creates valid types from the file.
		:return: dictionary.
		"""
		keys = self._file_reader.read_(str(CONFIG_PATTERNS))
		valid_types = {}

		for key in keys:
			valid_types[key] = [str, None]

		return valid_types


class ConfigValidationContainer(BaseContainer):
	"""
	contains valid types and patterns for checking the configuration file.
	"""

	@inject
	def __init__(
			self,
			types_container: JsonTypesContainer,
			file_reader: JsonFileReader):
		"""
		ConfigValidationContainer __init__.
		"""
		self._template = {
			"types": types_container.load_types(),
			"patterns": file_reader.read_(CONFIG_PATTERNS)
		}

		if self._template["patterns"]:
			if self._template["types"].keys() != self._template["patterns"].keys():
				raise TypeError

	def get_types(self) -> dict:
		"""
		:return: types dictionary.
		"""
		return self._template["types"]

	def get_patterns(self) -> dict:
		"""
		:return: patterns dictionary.
		"""
		return self._template["patterns"]


class ConfigValidator(BaseValidator):
	"""
	checks the validity of the configuration file.
	"""

	@inject
	def __init__(self, validation_container: ConfigValidationContainer):
		"""
		ConfigValidator __init__.
		:param validation_container: ConfigValidationContainer object.
		"""
		self._validation_container = validation_container

	def validate(self, config: dict) -> bool:
		"""
		checks that the config matches the types and template.
		:param config: config dictionary.
		:return: boolean.
		"""
		if isinstance(config, dict) and config != {}:

			for key, value in config.items():
				if key not in self._validation_container.get_types():
					return False

				if value is None:
					continue

				if type(value) not in self._validation_container.get_types()[key]:
					return False

				if value is not None and not re.search(
						self._validation_container.get_patterns()[key], value):
					return False

			return True

		return False
