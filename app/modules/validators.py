"""
contains file path validators.
"""
import re

from app.modules.base_structures import BaseValidator


class PathValidator(BaseValidator):
	"""validator for file paths."""

	@staticmethod
	def validate(path: str, pattern: str) -> bool:
		"""checks if the path ends with "*.extension".
		:param path: path to the file.
		:param pattern: file path validation pattern.
		:return: boolean.
		"""
		if isinstance(path, str) and isinstance(pattern, str):
			return bool(re.search(pattern, path))
		else:
			return False
