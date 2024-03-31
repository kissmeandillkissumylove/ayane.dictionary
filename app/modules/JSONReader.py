"""
contains a class whose job is to read json files or return None if the file is not
json.
"""
import json
import re
from dataclasses import dataclass
from typing import Union


@dataclass
class JSONReader:
	"""
	reads JSON file with UTF-8 encoding and returns dictionary or None.
	"""
	_pattern_json: str = r"\.json$"

	@classmethod
	def _validate_path(cls, path: str) -> bool:
		"""
		checks whether the path is a path to JSON.
		:param path: path to JSON file.
		:return: boolean.
		"""
		return False if not re.search(cls._pattern_json, path) else True

	@classmethod
	def read_json(cls, path: str) -> Union[dict, None]:
		"""
		reads JSON file and returns dictionary or None.
		:param path: path to JSON file.
		:return: dictionary.
		"""
		if cls._validate_path(path):
			try:
				with open(path, "r", encoding="utf-8") as file_json:
					file = json.load(file_json)
				return file
			except FileNotFoundError:
				return None
		else:
			return None
