"""
contains classes whose job is to validate the configuration file.
"""
import re
from dataclasses import dataclass

from app.modules.JSONReader import JSONReader
from app.modules.paths import CONFIG_TEMPLATE


@dataclass
class ValidationTypes:
	"""
	contains valid configuration file types.
	"""

	@classmethod
	def load_types(cls) -> dict:
		"""
		creates valid types for configuration file.
		"""
		keys = JSONReader.read_json(CONFIG_TEMPLATE).keys()
		valid_types = {}
		for key in keys:
			valid_types[key] = [str, None]
		return valid_types


class ConfigValidationTemplate:
	"""
	contains valid types and patterns for checking the configuration file.
	"""

	def __init__(self):
		"""
		contains valid types and patterns for checking the configuration file.
		"""
		self._template = {
			"types": ValidationTypes.load_types(),
			"patterns": JSONReader.read_json(CONFIG_TEMPLATE)
		}

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


class ConfigValidator:
	"""
	checks the validity of the configuration file.
	"""

	@classmethod
	def validate_config(cls, config: dict) -> bool:
		"""
		checks that the config matches the types and template.
		:param config: config dictionary.
		:return: boolean.
		"""
		config_template = ConfigValidationTemplate()
		for key, value in config.items():
			if key not in config_template.get_types():
				return False
			if type(value) not in config_template.get_types()[key]:
				return False
			if not re.search(config_template.get_patterns()[key], value):
				return False
		return True
