"""contains a file readers that read the file, and return the contents if
the file exists or None if the file doesn't exist, or the path is specified
incorrectly."""
import json
from typing import Union

from injector import inject

from app.modules.base_structures import BaseFileReader
from app.modules.validators import PathValidator


class JsonFileReader(BaseFileReader):
	"""reads JSON file with UTF-8 encoding by default and returns dictionary
	if the file exists or None if the file doesn't exist, or the path is specified
	incorrectly."""

	@inject
	def __init__(self, path_validator: PathValidator, pattern: str = ""):
		"""JsonFileReader __init__.
		:param path_validator: path validator.
		:param pattern: file path validation pattern ("\\.json$" by default).
		"""
		if not isinstance(path_validator, PathValidator):
			raise TypeError
		else:
			self._path_validator = path_validator

		if not isinstance(pattern, str):
			pass
		else:
			self._pattern = "\\.json$"

	def read_(self, path: str, encoding: str = "utf-8") -> Union[dict, None]:
		"""reads JSON file and returns dictionary or None.
		:param path: path to JSON file.
		:param encoding: what encoding to read the file with
			(utf-8 by default).
		:return: dictionary or None.
		"""
		if self._path_validator.validate_path(path, self._pattern):
			try:
				with open(path, "r", encoding=encoding) as file_json:
					file = json.load(file_json)

				return file

			except FileNotFoundError:
				return None

			except json.JSONDecodeError:
				return None

			except LookupError:
				return None

		else:
			return None
