from dataclasses import dataclass
from typing import Union

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
			valid_types[key] = Union[str, None]
		return valid_types
