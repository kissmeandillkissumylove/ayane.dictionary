"""contains a file readers that read the file, and return the contents if
the file exists or None if the file doesn't exist, or the path is specified
incorrectly."""
import json
from typing import Union

from injector import inject

from app.modules.base_structures import BaseFileReader
from app.modules.logger import CustomLogger
from app.modules.validators import PathValidator


class JsonFileReader(BaseFileReader):
	"""reads JSON file with UTF-8 encoding by default and returns dictionary
	if the file exists or None if the file doesn't exist, or the path is specified
	incorrectly."""

	@inject
	def __init__(
			self,
			path_validator: PathValidator,
			logger: CustomLogger,
			pattern: str = ""):
		"""JsonFileReader __init__.
		:param path_validator: path validator.
		:param pattern: file path validation pattern ("\\.json$" by default).
		"""
		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong value for the logger.")
		else:
			self._logger = logger
			self._logger.log_debug("set: _logger", self._logger)

		if not isinstance(path_validator, PathValidator):
			self._logger.log_critical("set: _path_validator", path_validator)
			raise TypeError
		else:
			self._path_validator = path_validator
			self._logger.log_debug(
				"set: _path_validator", self._path_validator)

		if not isinstance(pattern, str):
			self._logger.log_warning("try: _pattern", pattern)
		else:
			self._pattern = "\\.json$"
			self._logger.log_debug("set: _pattern", self._pattern)

	def read_(self, path: str, encoding: str = "utf-8") -> Union[dict, None]:
		"""reads JSON file and returns dictionary or None.
		:param path: path to JSON file.
		:param encoding: what encoding to read the file with
			(utf-8 by default).
		:return: dictionary or None.
		"""
		if self._path_validator.validate(self._logger, path, self._pattern):
			self._logger.log_debug("validator admits the path.")

			try:
				with open(path, "r", encoding=encoding) as file_json:
					file = json.load(file_json)

				return file

			except FileNotFoundError as error:
				self._logger.log_traceback("no msg", error)
				return None

			except json.JSONDecodeError as error:
				self._logger.log_traceback("no msg", error)
				return None

			except LookupError as error:
				self._logger.log_traceback("no msg", error)
				return None

		else:
			self._logger.log_debug("validator didn't admit the path.")
			return None
